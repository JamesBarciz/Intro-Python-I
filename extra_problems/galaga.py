grid = [
    ['.' for _ in range(15)],
    ['.' for _ in range(5)] + ['*'] + ['.' for _ in range(5)] + ['*', '.', '.', '.'],
    ['.' for _ in range(15)],
    ['.', '*'] + ['.' for _ in range(6)] + ['*'] + ['.' for _ in range(6)],
    ['.' for _ in range(10)] + ['Y'] + ['.' for _ in range(4)],
    ['.' for _ in range(6)] + ['*'] + ['.' for _ in range(8)],
    ['.' for _ in range(8)] + ['*'] + ['.' for _ in range(6)]
]
#### or..
#  [
#    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#    ['.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '.', '.'],
#    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
#    ['.', '*', '.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '.'],
#    ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', 'Y', '.', '.', '.', '.'],
#    ['.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '.', '.', '.'],
#    ['.', '.', '.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '.']
#  ]

arr = 4
ind = 10
pos = grid[arr][ind]

while True:
    if pos == '*':
        print('OUCH!  You hit a star - You\'re dead!')
        break
    else:
        direction = input('Choose N, S, E or W: ')
        if direction == 'N':
            arr -= 1
            pos = grid[arr][ind]
        elif direction == 'S':
            arr += 1
            pos = grid[arr][ind]
        elif direction == 'E':
            ind += 1
            pos = grid[arr][ind]
        elif direction == 'W':
            ind -= 1
            pos = grid[arr][ind]
