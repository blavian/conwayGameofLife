

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

def find_next_iteration(grid):
    cells_to_kill = []
    cells_to_regenerate = []
    # loop through the grid
    for x_idx, x in enumerate(grid):
        for y_idx, y in enumerate(x):
            num_neighbors = find_neigbors(x_idx, y_idx)
            if  y == 'X':
                if num_neighbors < 2 or num_neighbors > 3:
                    cells_to_kill.append((x_idx, y_idx))
            else: # otherwise y is not x and is a dead cell
                    if num_neighbors == 3:
                        cells_to_regenerate.append((x_idx, y_idx))
    for cell in cells_to_kill:
        grid[cell[0]][cell[1]] = 0
    for cell in cells_to_regenerate:
        grid[cell[0]][cell[1]] = 'X'
    print_grid(grid)
    
               


def find_neigbors(x, y):
    return 3

g = generate_grid(4,4, [(2,2), (1,3), (0,0), (0,1)])
print(g)
print_grid(g)
find_next_iteration(g)



    

