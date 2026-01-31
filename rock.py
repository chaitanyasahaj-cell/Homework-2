import random
user_points = 0
computer_points = 0
options = ["Rock", "Paper", "Scissor"]
user_choice = ("Rock, Paper, Scissor Shoot")
computer_choice = random.choice(options)


for i in range(10):
    user_choice = input("Rock, Paper, Scissor Shoot! --- ")
    computer_choice = random.choice(options)
    if user_choice == computer_choice:
        print("It's a tie! No points")
    
    elif user_choice == "Rock" and computer_choice == "Scissors" or user_choice == "Scissors" and computer_choice == "Paper" or user_choice == "Paper" and computer_choice == "Rock":
        print("You win this round! +1 Points.")
        print("The computer choice is {}".format(computer_choice))
        user_points += 1

    else:
        print("Computer wins this round! +1 Points.")
        print("The computer choice is {}".format(computer_choice))
        computer_points += 1

print("The final scores are. You got", user_points, "points. And the computer got",computer_points, "points.")
if user_points > computer_points:
    print("You win!!!")
else:
    print("Computer wins!!!")