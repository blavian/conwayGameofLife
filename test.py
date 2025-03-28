# -----------------
# | X | X |   |   |
# -----------------
# |   |   |   | X |
# -----------------
# |   |   | X |   |
# -----------------
# |   |   |   |   |
# -----------------



x_value = 0
y_value = 0
grid = [['X', 'X', 0, 0], [0, 0, 0, 'X'], [0, 0, 'X', 0], [0, 0, 0, 0]]
x = 4
y = 4
neighbor_count = 0
# check to the right and make sure we dont check past the column length
if y_value + 1 < y:
    if grid[x_value][y_value + 1] == "X":
        print('neighbor on right')
        neighbor_count += 1

    # check to the left and make sure there is a cell there
if y_value - 1 >= 0:
    if grid[x_value][y_value - 1] == "X":
         print('neighbor on left')
         neighbor_count += 1
    # check up and make sure there is a cell there
if x_value - 1 >= 0:
    if grid[x_value - 1][y_value] == "X":
        print('neighbor on up')
        neighbor_count += 1
    # check down and make sure we dont check past the row length
if x_value + 1 < x:
    if grid[x_value + 1][y_value] == "X":
        print('neighbor on diagnal 1')
        neighbor_count += 1
if x_value + 1 < x and y_value + 1 < y:
    if grid[x_value + 1][y_value + 1] == "X":
            print('neighbor on diagnal 2')
            neighbor_count += 1
if x_value - 1 >= 0 and y_value - 1 >= 0:
    if grid[x_value - 1][y_value - 1] == "X":
        print('neighbor on diagnal 3')
        neighbor_count += 1
if x_value - 1 >= 0 and y_value + 1 < y:
    if grid[x_value - 1][y_value + 1] == "X":
        print('neighbor on diagnal 4')
        neighbor_count += 1
if x_value + 1 < x and y_value - 1 >= 0:
    if grid[x_value + 1][y_value - 1] == "X":
        print([x_value + 1], [y_value - 1])
        print('neighbor on diagnal 4')
        neighbor_count += 1
print(f'{(x_value, y_value)} has {neighbor_count} neighbors')