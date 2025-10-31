from dataclasses import dataclass
from constants import COLS, ROWS

@dataclass
class Piece:
    type: str
    col: int
    row: int

    @property
    def offsets(self):
        return {
            "MID": {(0,0),(1,0),(0,1),(1,1)},
            "TL":  {(0,0),(1,0),(0,1)},
            "TR":  {(0,0),(1,0),(1,1)},
            "BL":  {(0,1),(1,1),(0,0)},
            "BR":  {(1,0),(0,1),(1,1)},
        }[self.type]

    @property
    def cells(self):
        return {(self.col + c, self.row + r) for c, r in self.offsets}


class Game:
    def __init__(self):
        self.pieces = {
            "TL": Piece("TL", 0, 0),
            "TR": Piece("TR", 2, 0),
            "BL": Piece("BL", 0, 2),
            "BR": Piece("BR", 2, 2),
            "MID": Piece("MID", 1, 1),
        }
        self.selected: Piece | None = None

    def reset(self):
        self.__init__()

    @property
    def occupied(self):
        s = set()
        for p in self.pieces.values():
            s |= p.cells
        return s

    def piece_at(self, cell):
        order = ["TL","TR","BL","BR","MID"]
        for key in reversed(order):
            if cell in self.pieces[key].cells:
                return self.pieces[key]
        return None

    def can_move(self, piece: Piece, dx: int, dy: int) -> bool:
        new_cells = {(c+dx, r+dy) for (c, r) in piece.cells}
        for c, r in new_cells:
            if not (0 <= c < COLS and 0 <= r < ROWS):
                return False
        others = self.occupied - piece.cells
        return new_cells.isdisjoint(others)

    def move(self, piece: Piece, dx: int, dy: int) -> bool:
        if self.can_move(piece, dx, dy):
            piece.col += dx
            piece.row += dy
            return True
        return False

    @property
    def won(self) -> bool:
        goals = {
            "TL": (0,0),
            "TR": (2,0),
            "BL": (0,2),
            "BR": (2,2),
            "MID": (1,4),
        }
        return all(
            (p.col, p.row) == goals[name]
            for name, p in self.pieces.items()
        )