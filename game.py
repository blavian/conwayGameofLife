

def generate_grid(rows, columns):
    grid =  [[0 for _ in range(columns)] for _ in range(rows)]
    return grid





def print_grid(grid):
    num_of_columns = len(grid[0])
    vertical_divider = ("----" * num_of_columns) + "-\n"
    printout = vertical_divider
    for row in grid:
        for _ in row:
            # open up a new cell for each column
            printout += '|   '
        printout += "|\n"
        printout += vertical_divider
    print(printout)
    

        

g = generate_grid(3,2)
print(g)
print(print_grid(g))




