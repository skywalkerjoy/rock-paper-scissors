import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input('Input rock/paper/scissors or q to quit: ').lower()
    if user_input == 'q':
        break
    elif user_input in options:
        computer_index = random.randint(0, 2)
        computer_input = options[computer_index]

        if user_input == computer_input:
            print('tie and try again because computer also picked',user_input)
            continue

        if user_input == 'rock' and computer_input == 'scissors':
            user_wins = user_wins+1
            print('Computer picks ',computer_input)
            print('You won! and your socre is ',user_wins,'computer score is ',computer_wins)

        elif user_input == 'paper' and computer_input == 'rock':
            user_wins = user_wins + 1
            print('Computer picks ', computer_input)
            print('You won! and your socre is ',user_wins,'computer score is ',computer_wins)

        elif user_input == 'scissors' and computer_input == 'paper':
            user_wins = user_wins+1
            print('Computer picks ', computer_input)
            print('You won! and your socre is ',user_wins,'computer score is ',computer_wins)

        else:
            computer_wins = computer_wins+1
            print('Computer picks ', computer_input)
            print('You lost! and your socre is ',user_wins,'computer score is ',computer_wins)

    else:
        continue

print('user wins ', user_wins , ' times')
print('computer wins ', computer_wins , ' times')
