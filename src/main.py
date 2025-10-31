import sys, os
import pygame

from constants import WIDTH, HEIGHT, CELL
from model import Game
from view import View

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Schimmler Puzzle Game")

    def resource_path(filename: str):
        """Return correct path whether running from source or from PyInstaller EXE."""
        if hasattr(sys, "_MEIPASS"):  # PyInstaller extraction folder
            return os.path.join(sys._MEIPASS, filename)
        return filename  # Running from script
    icon_path = resource_path("assets/icon.ico")
    icon_surface = pygame.image.load(icon_path)
    pygame.display.set_icon(icon_surface)

    clock = pygame.time.Clock()

    game = Game()
    view = View(screen)

    dragging = False
    move_anchor_px = (0, 0)

    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit(); sys.exit()

                if e.key == pygame.K_r:
                    game.reset()
                    continue  # skip movement events this frame

            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                mx, my = e.pos
                c, r = mx // CELL, my // CELL
                sel = game.piece_at((c, r))
                if sel:
                    game.selected = sel
                    dragging = True
                    move_anchor_px = (mx, my)

            if e.type == pygame.MOUSEBUTTONUP and e.button == 1:
                dragging = False
                game.selected = None

            if e.type == pygame.MOUSEMOTION and dragging and game.selected:
                mx, my = e.pos
                ax, ay = move_anchor_px
                dx_px, dy_px = mx - ax, my - ay
                moved = False

                if not moved and abs(dy_px) >= CELL and abs(dy_px) >= abs(dx_px):
                    step = 1 if dy_px > 0 else -1
                    if game.move(game.selected, 0, step):
                        move_anchor_px = (ax, ay + step * CELL)
                        moved = True
                    else:
                        move_anchor_px = (mx, my)

                if not moved and abs(dx_px) >= CELL:
                    step = 1 if dx_px > 0 else -1
                    if game.move(game.selected, step, 0):
                        move_anchor_px = (ax + step * CELL, ay)
                    else:
                        move_anchor_px = (mx, my)

        view.draw(game)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
