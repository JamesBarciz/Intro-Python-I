grid = [
    ['.' for _ in range(15)],
    ['.' for _ in range(5)] + ['*'] + ['.' for _ in range(5)] + ['*', '.', '.', '.'],
    ['.' for _ in range(15)],
    ['.', '*'] + ['.' for _ in range(6)] + ['*'] + ['.' for _ in range(6)],
    ['.' for _ in range(15)],
    ['.' for _ in range(6)] + ['*'] + ['.' for _ in range(8)],
    ['.' for _ in range(8)] + ['*'] + ['.' for _ in range(6)]
]

#### or..
#  [
#    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#    ['.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '.', '.'],
#    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#    ['.', '*', '.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '.'],
#    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#    ['.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '.', '.', '.'],
#    ['.', '.', '.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '.']
#  ]

def display_grid(cur_row, cur_col):
    for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
            if row_idx == cur_row and col_idx == cur_col:
                print('Y', end=' ')
            else:
                print(col, end=' ')
        print()

row = 4
col = 10
pos = grid[row][col]

while True:
    if pos == '*':
        print('OUCH!  You hit a star - You\'re dead!')
        break
    else:
        display_grid(row, col)

        direction = input('Choose N, S, E or W: ').lower()

        if direction == 'n':
            row = (row - 1) % len(grid)
            pos = grid[row][col]
        elif direction == 's':
            row = (row + 1) % len(grid)
            pos = grid[row][col]
        elif direction == 'e':
            col = (col + 1) % len(grid[0])
            pos = grid[row][col]
        elif direction == 'w':
            col = (col - 1) % len(grid[0])
            pos = grid[row][col]
