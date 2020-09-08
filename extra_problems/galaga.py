# grid = [
#     ['.' for _ in range(15)],
#     ['.' for _ in range(5)] + ['*'] + ['.' for _ in range(5)] + ['*', '.', '.', '.'],
#     ['.' for _ in range(15)],
#     ['.', '*'] + ['.' for _ in range(6)] + ['*'] + ['.' for _ in range(6)],
#     ['.' for _ in range(15)],
#     ['.' for _ in range(6)] + ['*'] + ['.' for _ in range(8)],
#     ['.' for _ in range(8)] + ['*'] + ['.' for _ in range(6)]
# ]

from termcolor import colored
import random
import os

grid = []
max_row, max_col = input('Enter the dimensions of your space grid (e.g. 25x15): ').split('x')
max_row, max_col = int(max_row), int(max_col)
cur_row = random.randint(0, max_row - 1)
cur_col = random.randint(0, max_col - 1)

generate_space = lambda: random.choice(['.'] * 5 + [colored('*', 'yellow')] + ['.'] * 5)

def generate_grid(clear=False):
    if clear: grid.clear()
    for row in range(max_row):
        grid.append([])
        for col in range(max_col):
            grid[row].append('.' if row == cur_row and col == cur_col else generate_space())

def display_grid(cur_row, cur_col):
    for row_idx, row in enumerate(grid):
        for col_idx, col in enumerate(row):
            if row_idx == cur_row and col_idx == cur_col:
                print(colored('Y', 'magenta', attrs=['bold']), end=' ')
            else:
                print(col, end=' ')
        print()

generate_grid()

while True:
    pos = grid[cur_row][cur_col]

    if '*' in pos:
        print(colored('''
                             ____
         ''', 'red', attrs=['bold']) + colored('BOOM!', 'red') + colored('''       __,-~~/~    `---.
                   _/_,---(      ,    )
               __ /        <    /   )  \___
- ------===;;;'====------------------===;;;===----- -  -
                  \/  ~"~"~"~"~"~\~"~)~"/
                  (_ (   \  (     >    \)
                   \_( _ <         >_>'
                      ~ `-i' ::>|--"
                          I;|.|.|
                         <|i::|i|`.
                        (` ^'"`-' ")        
        ''', 'red', attrs=['bold']))

        print('OUCH!  You hit a star - You\'re dead!')

        play_again = input('Want to play again? (yes/no): ')
        if play_again == 'yes':
            generate_grid(True)
            continue

        print('Pathetic...')

        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

        display_grid(cur_row, cur_col)

        direction = input('Choose N, S, E or W: ').lower()

        if direction == 'n':
            cur_row = (cur_row - 1) % len(grid)
            pos = grid[cur_row][cur_col]
        elif direction == 's':
            cur_row = (cur_row + 1) % len(grid)
            pos = grid[cur_row][cur_col]
        elif direction == 'e':
            cur_col = (cur_col + 1) % len(grid[0])
            pos = grid[cur_row][cur_col]
        elif direction == 'w':
            cur_col = (cur_col - 1) % len(grid[0])
            pos = grid[cur_row][cur_col]
