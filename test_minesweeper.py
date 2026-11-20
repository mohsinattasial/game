"""Unit tests for Minesweeper, no GUI/display required."""
import unittest
from minesweeper import Board


class BoardTests(unittest.TestCase):
    def test_first_move_is_safe(self):
        board = Board(seed=42)
        opened = board.reveal(0, 0)
        self.assertIn((0, 0), opened)
        self.assertFalse(board.cells[0][0].mine)
        self.assertEqual(sum(c.mine for row in board.cells for c in row), 20)

    def test_flags_prevent_revealing(self):
        board = Board(seed=2)
        self.assertTrue(board.toggle_flag(0, 0))
        self.assertEqual(board.reveal(0, 0), set())
        self.assertFalse(board.started)
        self.assertFalse(board.toggle_flag(0, 0))
        self.assertIn((0, 0), board.reveal(0, 0))

    def test_mine_is_losing_move(self):
        board = Board(rows=3, cols=3, mines=1, seed=42)
        board.reveal(0, 0)
        mine = next((r, c) for r in range(3) for c in range(3)
                    if board.cells[r][c].mine)
        if not board.over:
            board.reveal(*mine)
            self.assertTrue(board.over)
            self.assertFalse(board.won)

    def test_win_when_all_safe_cells_revealed(self):
        board = Board(rows=3, cols=3, mines=1, seed=2)
        board.reveal(0, 0)
        for r in range(3):
            for c in range(3):
                if not board.over and not board.cells[r][c].mine:
                    board.reveal(r, c)
        self.assertTrue(board.won)

    def test_invalid_mine_count(self):
        with self.assertRaises(ValueError):
            Board(rows=2, cols=2, mines=4)


if __name__ == "__main__":
    unittest.main()
