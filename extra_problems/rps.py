# Create a class which will perform a basic Rock/Paper/Scissors game that:
# Has an AI play against us
# Keeps track of score
# Rules: rock>paper>scissors>rock...
import random


options = ['rock', 'paper', 'scissors']

# Dictionary {'option': ['same', 'option_lose', 'option_win']}
# May be able to use to clean up code?
rps_dict = {
    'rock': ['rock', 'paper', 'scissors'],
    'paper': ['paper', 'scissors', 'rock'],
    'scissors': ['scissors', 'rock', 'paper']
}

user_counter = 0
computer_counter = 0

def game(choice=random.choice(options)):
    '''
    Args: choice=('rock', 'paper', 'scissors')

    Plays a game of Rock/Paper/Scissors with an AI that will randomly select one
    of the options: 'rock', 'paper' or 'scissors'.  A 'hard mode' is enabled when
    the user's score is 3 or more than the AI in which case, the computer will choose
    between the user's choice and another random choice from the 3 options.
    '''

    global user_counter
    global computer_counter
    global rps_dict
    global options

    if (choice == '') or (choice.isspace() == True):
        choice = random.choice(options)
 
    computer_choice = random.choice(options)

    if (user_counter - computer_counter) >= 3:
        computer_choice = random.choice([choice, computer_choice])
    else:
        pass

    if (choice == 'rock') and (computer_choice == 'scissors'):
        user_counter += 1
        print(f'You win! {choice.capitalize()} beats {computer_choice}!')
        return f'Score: You: {user_counter} - AI: {computer_counter}'
    elif (choice == 'rock') and (computer_choice == 'paper'):
        computer_counter += 1
        print(f'You lose!  {computer_choice.capitalize()} covers {choice}!')
        return f'Score: You: {user_counter} - AI: {computer_counter}'
    elif (choice == 'rock') and (computer_choice == 'rock'):
        print(f'Push!  You both chose {choice}!')
        return f'Score: You: {user_counter} - AI: {computer_counter}'
    elif (choice == 'paper') and (computer_choice == 'rock'):
        user_counter += 1
        print(f'You win! {choice.capitalize()} covers {computer_choice}!')
        return f'Score: You: {user_counter} - AI: {computer_counter}'
    elif (choice == 'paper') and (computer_choice == 'scissors'):
        computer_counter += 1
        print(f'You lose!  {computer_choice.capitalize()} cuts {choice}!')
        return f'Score: You: {user_counter} - AI: {computer_counter}'
    elif (choice == 'paper') and (computer_choice == 'paper'):
        print(f'Push!  You both chose {choice}!')
        return f'Score: You: {user_counter} - AI: {computer_counter}'
    elif (choice == 'scissors') and (computer_choice == 'paper'):
        user_counter += 1
        print(f'You win! {choice.capitalize()} cuts {computer_choice}!')
        return f'Score: You: {user_counter} - AI: {computer_counter}'
    elif (choice == 'scissors') and (computer_choice == 'rock'):
        computer_counter += 1
        print(f'You lose!  {computer_choice.capitalize()} beats {choice}!')
        return f'Score: You: {user_counter} - AI: {computer_counter}'
    elif (choice == 'scissors') and (computer_choice == 'scissors'):
        print(f'Push!  You both chose {choice}!')
        return f'Score: You: {user_counter} - AI: {computer_counter}'
    else:
        return 'TODO'
