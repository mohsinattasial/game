"""Testable Minesweeper rules, separate from the Tkinter display."""
from __future__ import annotations

import random
from dataclasses import dataclass


@dataclass
class Cell:
    mine: bool = False
    revealed: bool = False
    flagged: bool = False


class Board:
    def __init__(self, rows: int = 8, cols: int = 8, mines: int = 20, seed: int | None = None):
        if rows <= 0 or cols <= 0 or not 0 < mines < rows * cols:
            raise ValueError("Board dimensions and mine count are invalid")
        self.rows, self.cols, self.mines = rows, cols, mines
        self.cells = [[Cell() for _ in range(cols)] for _ in range(rows)]
        self.rng = random.Random(seed)
        self.started = False
        self.over = False
        self.won = False

    def neighbors(self, row: int, col: int):
        for r in range(max(0, row - 1), min(self.rows, row + 2)):
            for c in range(max(0, col - 1), min(self.cols, col + 2)):
                if (r, c) != (row, col):
                    yield r, c

    def number(self, row: int, col: int) -> int:
        return sum(self.cells[r][c].mine for r, c in self.neighbors(row, col))

    def _place_mines(self, first: tuple[int, int]):
        candidates = [(r, c) for r in range(self.rows) for c in range(self.cols)
                      if (r, c) != first]
        for r, c in self.rng.sample(candidates, self.mines):
            self.cells[r][c].mine = True
        self.started = True

    def toggle_flag(self, row: int, col: int) -> bool:
        cell = self.cells[row][col]
        if not self.over and not cell.revealed:
            cell.flagged = not cell.flagged
        return cell.flagged

    def reveal(self, row: int, col: int) -> set[tuple[int, int]]:
        if self.over:
            return set()
        start = self.cells[row][col]
        if start.revealed or start.flagged:
            return set()
        if not self.started:
            self._place_mines((row, col))  # First move is always safe.
        opened = set()
        todo = [(row, col)]
        while todo:
            r, c = todo.pop()
            cell = self.cells[r][c]
            if cell.revealed or cell.flagged:
                continue
            cell.revealed = True
            opened.add((r, c))
            if cell.mine:
                self.over = True
                break
            if self.number(r, c) == 0:
                todo.extend((nr, nc) for nr, nc in self.neighbors(r, c)
                            if not self.cells[nr][nc].revealed and not self.cells[nr][nc].flagged)

        safe_opened = sum(c.revealed and not c.mine for row in self.cells for c in row)
        if safe_opened == self.rows * self.cols - self.mines:
            self.over = True
            self.won = True
        return opened
