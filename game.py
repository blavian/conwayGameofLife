def generate_grid(rows, columns, initial_living_cells):
    grid = [[0 for _ in range(columns)] for _ in range(rows)]
    for cell in initial_living_cells:
        x = cell[0]
        y = cell[1]
        grid[x][y] = "X"
    return grid


def print_grid(grid):
    num_of_columns = len(grid[0])
    vertical_divider = ("----" * num_of_columns) + "-\n"
    printout = vertical_divider
    for column in grid:
        for row in column:
            if row == "X":
                printout += "| X "
            else:
                printout += "|   "
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
            if y == "X":
                if num_neighbors < 2 or num_neighbors > 3:
                    cells_to_kill.append((x_idx, y_idx))
            else:  # otherwise y is not x and is a dead cell
                if num_neighbors == 3:
                    cells_to_regenerate.append((x_idx, y_idx))
    for cell in cells_to_kill:
        grid[cell[0]][cell[1]] = 0
    for cell in cells_to_regenerate:
        grid[cell[0]][cell[1]] = "X"
    print_grid(grid)


def find_neigbors(x, y):
    return 2




def test(grid, x_value, y_value):
    neighbor_count = 0
    x = len(grid)
    y = len(grid[1])
    # check to the right and make sure we dont check past the column length
    if grid[x_value][y_value + 1] == 'X' and y_value + 1 < y:
        neighbor_count+=1
    # check to the left and make sure there is a cell there
    if  grid[x_value][y_value - 1] == 'X' and y_value - 1 >= 0:
        neighbor_count+=1
    # check up and make sure there is a cell there
    if  grid[x_value - 1][y_value] == 'X' and x_value - 1 >= 0:
        neighbor_count+=1
    #check down and make sure we dont check past the row length
    if grid[x_value + 1][y_value] == 'X' and x_value + 1 < x:
        neighbor_count+=1
    if grid[x_value+1][y_value+1] or grid[x_value-1][y_value-1] or grid[x_value-1][y_value+1] or grid[x_value+1][y_value-1] == 'X' and x_value + 1 < x and y_value + 1 < y and x_value - 1 >= 0 and y_value - 1 >= 0:
        neighbor_count+=1
    print(neighbor_count)
        
        
        



g = generate_grid(4, 4, [(2, 2), (1, 3), (0, 0), (0, 1)])
print(g)
print_grid(g)
find_next_iteration(g)

test(g, 2, 2)
