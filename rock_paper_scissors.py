import random
import rps_art

print(rps_art.logo)

rps_moves = ["Rock", "Paper", "Scissors"]
rps_win_moves = [["Rock", "Scissors"], ["Paper", "Rock"], ["Scissors", "Paper"]]
user_score = 0
computer_score = 0

while True:
    computer = random.randint(0, 2)
    try:
        user = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors (Q to quit)\n")
        if user.lower() == "q":
            print(f"\nFinal Score - You: {user_score}, Computer: {computer_score}")
            print("Thanks for playing!")
            break
        else:
            user = int(user)    
            if user not in [0, 1, 2]:
                print("Invalid choice!")
                continue
    except ValueError:
        print("Please enter a number!")
        continue

    print(f"Your choice:\n\n{rps_art.art[user]}")
    print(f"Computer's choice:\n\n{rps_art.art[computer]}")

    if user == computer:
        print("It's a tie!")
        print(f"You: {user_score}\nComputer: {computer_score}")
    else:
        for win in rps_win_moves:
            if rps_moves[user] == win[0] and rps_moves[computer] == win[1]:
                user_score += 1
                print("You Won!")
                print(f"You: {user_score}\nComputer: {computer_score}")
                break
            elif rps_moves[computer] == win[0] and rps_moves[user] == win[1]:
                computer_score += 1
                print("Computer Won!")
                print(f"You: {user_score}\nComputer: {computer_score}")
                break
