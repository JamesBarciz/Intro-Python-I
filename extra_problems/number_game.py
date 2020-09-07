# Write a number guessing game
# User thinks of a number 1-100
# Program makes a guess
# Tell it if the number is > or < than its guess
# Uses that info to modify its guess until it homes in
import random
import time


user_number = int(input('Select a number from 1-100: '))
time.sleep(1)

print('Computer is selecting a number...')
time.sleep(2)

computer_number = random.randint(1, 100)

response_0 = input(f'Is your number {computer_number}? (yes/no) ')
if response_0 == 'no':
    response_1 = input(f'Is your number > or < than {computer_number}? ')
    while response_1 == '>':
        computer_number = random.randint(user_number + 1, 100)
        break
    while response_1 == '<':
        computer_number = random.randint(1, user_number - 1)
        break
breakpoint()