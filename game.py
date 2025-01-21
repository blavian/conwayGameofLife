

def generate_grid(rows, columns):
    grid =  [[0 for _ in range(columns)] for _ in range(rows)]
    return grid





def print_grid(grid):
    for col in grid:
        for row in col:
            row = '| '
            print(row, end = '')
            print()
    
        



print(print_grid(generate_grid(2, 4)))




