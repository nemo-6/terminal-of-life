import random
import time

live_cell_rules = {
    # rule 1: Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    0: False,
    1: False,
    # rule2: Any live cell with two or three live neighbours lives on to the next generation.
    2: True,
    3: True,
    # rule3: Any live cell with more than three live neighbours dies, as if by overpopulation.
    4: False,
    5: False,
    6: False,
    7: False,
    8: False,
}

dead_cell_rules = {
    0: False,
    1: False,
    2: False,
    #rule4: Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    3: True,
    4: False,
    5: False,
    6: False,
    7: False,
    8: False,
}


class Cell:
    def __init__(self, value):
        self.value = value


class Board:
    def __init__(self, size_x, size_y):
        self.cells = [[Cell(False) for x in range(size_y)] for y in range(size_x)]
        self.size_x = size_x
        self.size_y = size_y
        self.OOB_CELL = Cell(False)

    def populate(self):
        self.cells = [[Cell(random.choice([False] + [True])) for x in range(self.size_y)] for y in range(self.size_x)]
    
    def get_cell(self, x, y):
        try:
            return self.cells[x][y]
        except IndexError:
            return self.OOB_CELL

    def count_neighbours(self, x, y):
        value = [
            self.get_cell(x-1, y-1,).value,
            self.get_cell(x, y-1,).value,
            self.get_cell(x+1, y-1,).value,
            self.get_cell(x-1, y,).value, 
            self.get_cell(x+1, y,).value,
            self.get_cell(x-1, y+1,).value,
            self.get_cell(x, y+1,).value,
            self.get_cell(x+1, y+1,).value,
        ].count(True)
        return value
        
    def __str__(self):
        string = ''
        for x in range(board.size_x):
            for y in range(board.size_y):
                if board.get_cell(x, y).value:
                    string += '██'
                else:
                    string += '  '
            string += '\n'
        return string

    def time_pass(self):
        newboard = Board(self.size_x, self.size_y)
        
        for x in range(self.size_x):
            for y in range(self.size_y):
                cell_is_alive = self.get_cell(x, y).value
                neighbours = self.count_neighbours(x, y)
                if cell_is_alive:  # if cell is alive
                    newboard.get_cell(x,y).value = live_cell_rules[neighbours]
                else:  # cell is dead
                    newboard.get_cell(x,y).value = dead_cell_rules[neighbours]

        return newboard

if __name__ == "__main__":
    board = Board(80, 80)
    board.populate()

    while True:
        print('blep-----------------------')
        print(board)
        board = board.time_pass()
        time.sleep(0.1)


# ---------------
# ---██-----██---
# ----██---██----
# -█--█-█-█-█--█-
# -███-██-██-███-
# --█-█-█-█-█-█--
# ---███---███---
# ---------------
# ---███---███---
# --█-█-█-█-█-█--
# -███-██-██-███-
# -█--█-█-█-█--█-
# ----██---██----
# ---██-----██---
# ---------------
