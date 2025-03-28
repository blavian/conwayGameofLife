class Game:
    def __init__(self,rows, columns, initial_living_cells):
        self.rows = rows
        self.columns = columns
        self.initial_living_cells = initial_living_cells
        self.grid = self.generate_grid()
    
    
    def generate_grid(self):
        grid = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        for cell in self.initial_living_cells:
            x = cell[0]
            y = cell[1]
            grid[x][y] = "X"
        return grid
    def __str__(self):
        vertical_divider = ("----" * self.columns) + "-\n"
        printout = vertical_divider
        for column in self.grid:
            for row in column:
                if row == "X":
                    printout += "| X "
                else:
                    printout += "|   "
            printout += "|\n"
            printout += vertical_divider
        return printout
    
    def find_neigbors(self, x_value, y_value):
        neighbor_count = 0
        #x = len(self.grid)
        x = self.columns
        # y = len(self.grid[1])
        y = self.rows
    # check to the right and make sure we dont check past the column length
        if y_value + 1 < self.rows:
            if self.grid[x_value][y_value + 1] == "X":
                neighbor_count += 1

        # check to the left and make sure there is a cell there
        if y_value - 1 >= 0:
            if self.grid[x_value][y_value - 1] == "X":
                neighbor_count += 1
        # check up and make sure there is a cell there
        if x_value - 1 >= 0:
            if self.grid[x_value - 1][y_value] == "X":
                neighbor_count += 1
        # check down and make sure we dont check past the row length
        if x_value + 1 < x:
            if self.grid[x_value + 1][y_value] == "X":
                neighbor_count += 1
        if x_value + 1 < x and y_value + 1 < y:
            if self.grid[x_value + 1][y_value + 1] == "X":
                neighbor_count += 1
        if x_value - 1 >= 0 and y_value - 1 >= 0:
            if self.grid[x_value - 1][y_value - 1] == "X":
                neighbor_count += 1
        if x_value - 1 >= 0 and y_value + 1 < y:
            if self.grid[x_value - 1][y_value + 1] == "X":
                neighbor_count += 1
        if x_value + 1 < x and  y_value - 1 >= 0:
            if self.grid[x_value + 1][y_value - 1] == "X":
                neighbor_count += 1
        return neighbor_count
    

g = Game(3,3,[(0,1), (1,2)])
print(g)
print(g.find_neigbors(0,1))

