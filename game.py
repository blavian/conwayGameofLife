

def generate_grid(rows, columns, initial_living_cells):
    grid =  [[0 for _ in range(columns)] for _ in range(rows)]
    for cell in initial_living_cells:
        x = cell[0]
        y = cell[1]
        grid[x][y] = 'X'
    return grid





def print_grid(grid):
    num_of_columns = len(grid[0])
    vertical_divider = ("----" * num_of_columns) + "-\n"
    printout = vertical_divider
    for column in grid:
        for row in column:
            if row == 'X':
                printout += '| X '
            else:
                printout += '|   ' 
        printout += "|\n"
        printout += vertical_divider
    print(printout)
    

        

g = generate_grid(4,4, [(2,2), (1,3), (0,0), (0,1)])
print(g)
print(print_grid(g))




