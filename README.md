# Minesweeper — Tkinter

An 8×8 desktop Minesweeper game with 20 mines, a guaranteed safe first click, flood reveal of empty cells, right-click flags, win detection, and a New Game button.

## Run
Requires Python 3.10+ with Tkinter installed (usually included on Windows).

```bash
python main.py
```

Left-click to reveal cells. Right-click to place or remove a flag. Use **New Game** to reset the board.

## Structure
- `main.py`: Tkinter user interface
- `minesweeper.py`: pure Python game rules (no GUI dependency)
- `test_minesweeper.py`: unit tests

## Tests
```bash
python -m unittest -v test_minesweeper
```

Author: Mohsin Atta
