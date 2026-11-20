"""Minesweeper game using Tkinter and testable game rules."""
import tkinter as tk
from tkinter import messagebox

from minesweeper import Board


class MinesweeperApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Minesweeper")
        self.root.resizable(False, False)
        self.board = Board()
        self.status = tk.StringVar(value="Left-click to reveal • Right-click to flag")
        tk.Label(root, textvariable=self.status, pady=8).pack()
        frame = tk.Frame(root)
        frame.pack(padx=10)
        self.buttons: list[list[tk.Button]] = []
        for r in range(self.board.rows):
            row = []
            for c in range(self.board.cols):
                button = tk.Button(frame, width=4, height=2,
                                   command=lambda row=r, col=c: self.reveal(row, col))
                button.grid(row=r, column=c)
                button.bind("<Button-3>", lambda event, row=r, col=c:
                            self.toggle_flag(row, col))
                row.append(button)
            self.buttons.append(row)
        tk.Button(root, text="New Game", command=self.reset).pack(pady=8)

    def toggle_flag(self, row: int, col: int):
        self.board.toggle_flag(row, col)
        self.refresh()

    def reveal(self, row: int, col: int):
        was_over = self.board.over
        self.board.reveal(row, col)
        self.refresh()
        if self.board.over and not was_over:
            messagebox.showinfo("Minesweeper",
                                "You cleared the minefield!" if self.board.won else
                                "Boom! You hit a mine.")

    def refresh(self):
        flags = 0
        for r in range(self.board.rows):
            for c in range(self.board.cols):
                cell = self.board.cells[r][c]
                button = self.buttons[r][c]
                flags += int(cell.flagged)
                if cell.revealed:
                    label = "💣" if cell.mine else (str(self.board.number(r, c)) or "")
                    color = "tomato" if cell.mine else "#dedede"
                    button.configure(text=label, bg=color, relief=tk.SUNKEN,
                                     state=tk.DISABLED)
                elif self.board.over and cell.mine:
                    button.configure(text="💣", bg="#ffc6c6", state=tk.DISABLED)
                else:
                    button.configure(text="🚩" if cell.flagged else "", bg="#f0f0f0",
                                     relief=tk.RAISED, state=tk.NORMAL)
        if self.board.over:
            self.status.set("YOU WIN!" if self.board.won else "Game over — try again")
        else:
            self.status.set(f"Mines: {self.board.mines} • Flags: {flags}")

    def reset(self):
        self.board = Board()
        self.refresh()


if __name__ == "__main__":
    root = tk.Tk()
    MinesweeperApp(root)
    root.mainloop()
