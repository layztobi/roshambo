import random

while True:
    user_action = input("Enter a choice (R for rock, P for paper, S for scissors): ")
    user_action = user_action.upper()
    print(user_action)
    while True:
        user_action = user_action.upper()
        if user_action == "R" or user_action == "S" or user_action == "P":
            break
        user_action = input("Enter a valid choice (R for rock, P for paper, S for scissors): ")
    
    possible_actions = ["R", "P", "S"]
    computer_action = random.choice(possible_actions)
    if user_action == "R":
        user_action = "Rock"
    elif user_action == "P":
        user_action = "Paper"
    else :
        user_action = "Scissors" 

    if computer_action == "R":
        computer_action = "Rock"
    elif computer_action == "P":
        computer_action = "Paper"
    else :
        computer_action = "Scissors" 
        
    print(f"\nPlayer ({user_action}) : Computer ({computer_action})\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "Rock":
        if computer_action == "Scissors":
            print("Rock smashes scissors! Player wins!")
        else:
            print("Paper covers rock! Player loses.")

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break

    
    elif user_action == "Paper":
        if computer_action == "Rock":
            print("Paper covers rock! Player wins!")
        else:
            print("Scissors cuts paper! Player loses.")

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break

            
    elif user_action == "Scissors":
        if computer_action == "Paper":
            print("Scissors cuts paper! player wins!")
        else:
            print("Rock smashes scissors! Player loses.")
            
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != "y":
            break
    
