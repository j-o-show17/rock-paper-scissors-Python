import random, ui

print('Welcome to Rock, Paper, Scissors')

user_choice = int(input('Enter 0 for Rock, 1 for Paper and 2 for Scissors: '))

print("Computer Chose: ")
random_computer = random.randint(0,2)
computer_choice = ui.ui_list[random_computer]

print(computer_choice)

print(f"You Chose {ui.ui_list}")
print(ui.ui_list[user_choice])

if user_choice == 2 and random_computer == 0:
    print("You lose")
elif user_choice <  random_computer:
    print("You lose")
elif user_choice == random_computer:
    print("Draw")
else:
    print("You win!")
