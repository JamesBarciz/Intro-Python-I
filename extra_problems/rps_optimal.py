# Different approach to rock/paper/scissors game using index logic

import random


choices = ['rock', 'paper', 'scissors']

scores = {
    'User': 0,
    'Computer': 0
}

difficulty = int(input('Please select your difficulty (1-5): '))


def winning_choice(index):
    '''Returns the index of the winning choice given an index.'''
    '''Uses list.index(str/int/float) to obtain index value.'''
    '''Example: winning_choice('rock') == 1 | 'paper'.'''
    return (index + 1) % 3


def losing_choice(index):
    '''Returns the index of the losing choice given an index.'''
    '''Uses list.index(str/int/float) to obtain index value.'''
    '''Example: losing_choice('rock') == 2 | 'scissors'.'''
    return (index - 1) % 3


while True:
    user_opt = choices.index(str(input(f'Please choose: {choices}: ')))
    computer_opt = choices.index(random.choice(
        choices + ([choices[winning_choice(user_opt)]] * difficulty)))

    print(f'You chose: {choices[user_opt].upper()} - '
          f'Computer chose: {choices[computer_opt].upper()}')

    if user_opt == computer_opt:
        print(f'It\'s a tie!  Scores: User: {scores["User"]} - '
              f'Computer: {scores["Computer"]}')
    elif losing_choice(user_opt) < computer_opt:
        scores['User'] += 1
        if scores['User'] == 3:
            print('Congratulations - you beat the computer!')
            break
        else:
            print(f'You win!  Scores: User: {scores["User"]} - '
                  f'Computer: {scores["Computer"]}')
    else:
        scores['Computer'] += 1
        if scores['Computer'] == 3:
            print('The computer beat you... better luck next time!')
            break
        else:
            print(f'Computer wins...  Scores: User: {scores["User"]} - '
                  f'Computer: {scores["Computer"]}')
