# Minesweeper (Tkinter)

A desktop Minesweeper game written in Python using the standard-library Tkinter GUI.

## Run

Requires Python 3 with Tkinter available (usually included on Windows and macOS).

```bash
python main.py
```

Click a cell to reveal it. A mine ends the round; a safe cell displays the number of adjacent mines. The board is 8×8 with 20 mines. The current implementation is a learning project and does not yet provide flags or automatic win detection.

## Project structure

- `main.py` — cells, mine placement, and Tkinter interface.

## Possible improvements

- Flag cells with right-click; prevent opening flagged cells.
- Reveal neighboring empty cells automatically.
- Add a restart button and a clear win condition.

Author: Mohsin Atta
