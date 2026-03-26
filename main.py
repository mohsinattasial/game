import random
import tkinter as tk

# Settings
GRID_SIZE = 8
MINES_COUNT = 20

class Cell:
    all = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.is_mine = False
        self.is_open = False
        self.button = None
        Cell.all.append(self)

    def create_button(self, root):
        btn = tk.Button(root, width=4, height=2, command=self.left_click)
        btn.grid(row=self.x, column=self.y)
        self.button = btn

    def left_click(self):
        if self.is_open:
            return

        self.is_open = True

        if self.is_mine:
            self.button.configure(text="💣", bg="red")
            self.show_all_mines()
        else:
            mines = self.count_mines()
            self.button.configure(text=str(mines), bg="lightgrey")

    def count_mines(self):
        count = 0
        for cell in self.get_neighbors():
            if cell.is_mine:
                count += 1
        return count

    def get_neighbors(self):
        neighbors = []
        for cell in Cell.all:
            if abs(cell.x - self.x) <= 1 and abs(cell.y - self.y) <= 1:
                if cell != self:
                    neighbors.append(cell)
        return neighbors

    def show_all_mines(self):
        for cell in Cell.all:
            if cell.is_mine:
                cell.button.configure(text="💣", bg="red")

    @staticmethod
    def create_mines():
        mines = random.sample(Cell.all, MINES_COUNT)
        for cell in mines:
            cell.is_mine = True


class Game:
    def __init__(self, root):
        self.root = root
        self.cells = []

        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                cell = Cell(x, y)
                cell.create_button(root)
                self.cells.append(cell)

        Cell.create_mines()


# Run game
root = tk.Tk()
root.title("Minesweeper")

game = Game(root)

root.mainloop()