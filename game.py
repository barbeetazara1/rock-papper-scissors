import random

user_wins = 0
computer_wins = 0

options = ['scissors', 'paper', 'rock']

while True:
    user_input = input("Type Scisssors/Paper/Rock or Quit (q): ").lower()
    
    if user_input == 'q':
        break
    if user_input not in options:
        continue
    
    random_number = random.randint(0, 2)
    compute_pick = options[random_number]
    print('Computer Pick', compute_pick)
    
    if user_input == 'rock' and compute_pick == 'scissors':
        print('You Won!')
        user_wins += 1
    elif user_input == 'paper' and compute_pick == 'rock':
        print('You Won')
        user_wins += 1
    elif user_input == 'scissors' and compute_pick == 'paper':
        print('You Won')
        user_wins += 1
    else:
        print('You Lose!')
        computer_wins += 1
        
print('You wins', user_wins, 'times!')
print('Computer wins', computer_wins, 'times!')      
print('GoodBye!')
