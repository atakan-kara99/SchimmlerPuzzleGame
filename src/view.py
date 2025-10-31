import pygame
from constants import WIDTH, HEIGHT, CELL, ROWS, COLS, BG, GRID, COLORS
from model import Game, Piece

class View:
    def __init__(self, screen):
        self.s = screen
        self.font = pygame.font.Font(None, 22)

    def draw_grid(self):
        self.s.fill(BG)
        for r in range(ROWS):
            for c in range(COLS):
                pygame.draw.rect(
                    self.s, GRID,
                    pygame.Rect(c*CELL, r*CELL, CELL, CELL), 1
                )

    def draw_piece(self, p: Piece):
        color = COLORS[p.type]
        for dc, dr in p.offsets:
            x = (p.col + dc) * CELL
            y = (p.row + dr) * CELL
            pygame.draw.rect(
                self.s, color,
                pygame.Rect(x, y, CELL, CELL)
            )

    def draw(self, game: Game):
        self.draw_grid()

        for p in game.pieces.values():
            self.draw_piece(p)

        # Normal hint text
        txt = self.font.render("R to reset.                Drag to slide.                ESC to quit.", True, (230,230,230))
        self.s.blit(txt, (8, HEIGHT - 24))

        if game.won:
            # Big centered victory text
            big_font = pygame.font.Font(None, 80)  # Larger font
            text = big_font.render("YOU WIN!", True, (255,255,255))

            text_rect = text.get_rect(
                center=(WIDTH // 2, HEIGHT // 2)
            )
            self.s.blit(text, text_rect)
