import random

def play():
    user = input(f"Whats your choice, 'r' for rock, 'p' for paper, 's' for scissor: \n")
    computer_choice = random.choice(["r","p","s"])

    if user == computer_choice:
        return "its a tie"
    
    if user == "r" and computer_choice == "s":
        return "rock breaks scissors, you win"
    
    elif user == "s" and computer_choice == "p":
        return "scissors cuts paper, you win"
    
    elif user == "p" and computer_choice == "r":
        return "paper covers rock, you win"
    
    elif computer_choice == "r" and user == "s":
        return "rock breaks scissors, you lose"
    
    elif computer_choice == "s" and user == "p":
        return "scissors cuts paper, you lose"
    
    elif computer_choice == "p" and user == "r":
        return "paper covers rock, you lose"
    
print(play())