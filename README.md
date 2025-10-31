# Schimmler Puzzle Game

Schimmler Puzzle Game is a small sliding-block puzzle implemented in Python and Pygame.

- Game concept: Prof. Dr. Manfred Schimmler
- Implementation: Atakan Kara

The goal of the puzzle is to slide the pieces on a 4×6 board so that the central 2×2 piece (MID) reaches the goal position near the bottom of the board.

## Quick overview

- Board: 4 columns × 6 rows
- Pieces: five named pieces (TL, TR, BL, BR, MID). Pieces occupy 2×2 or 2×1/1×2 L-shaped configurations as defined in the code.
- Controls: drag pieces with the mouse (left click + drag) to slide them. Press `R` to reset, `ESC` to quit.

## Initial and goal illustrations

Below are simple illustrations showing the initial layout and the goal layout.

Initial position:

![Initial position](init.png)

Goal position — the MID piece moves down to row 4:

![Goal position](goal.png)

## How to run

Prerequisites:

- Python 3.8+ (3.11 recommended)
- Pygame (tested with pygame 2.x)

Install Pygame (if needed):

```bash
python -m pip install pygame
```

Run the game from the project root:

```bash
python main.py
```

Notes:

- `main.py` uses a small `resource_path()` helper to allow bundling with PyInstaller. If you run the bundled EXE, resources (like `icon.ico`) are loaded from the PyInstaller temporary directory.
- There is a `build.bat` in the repo. On Windows you can run `build.bat` to create a packaged EXE (it uses PyInstaller). A built [EXE](dist/schimmler.exe) is already included in the `dist/` folder in this repository.

## Files in this project

- `main.py` — entry point; sets up Pygame loop and event handling.
- `model.py` — game model and rules (pieces, movement, win condition).
- `view.py` — drawing code and basic UI hints.
- `constants.py` — board sizes, colors, and other constants.
- `build.bat` — simple build helper for Windows (optional).

## Edge cases & behavior

- Pieces only move by whole cell steps (no partial placements).
- A piece can move only if its destination cells are inside the board and not occupied by other pieces.
- Pieces are selected by clicking any occupied cell; the code prefers top-most pieces when overlapping.
