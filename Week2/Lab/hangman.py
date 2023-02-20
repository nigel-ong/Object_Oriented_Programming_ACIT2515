"""
ACIT2515 Lab

Week 2 -- complete this file!

"""

# The number of turns allowed is a global constant
textfile = 'words.txt'
import random

NB_TURNS = 10


def pick_random_word(file): ##OK
    """Opens the words.txt file, picks and returns a random word from the file"""
    with open (file, 'r') as f:
        content = f.readlines()
        selected_word = random.choice(content)
        
        return selected_word

def show_letters_in_word(word, letters): #OK
    """
    This function RETURNS A STRING.
    This function scans the word letter by letter.
    First, make sure word is uppercase, and all letters are uppercase.
    If the letter of the word is in the list of letters, keep it.
    Otherwise, replace it with an underscore (_).

    DO NOT USE PRINT!

    Example:
    >>> show_letters_in_word("VANCOUVER", ["A", "V"])
    'V A _ _ _ _ V _ _'
    >>> show_letters_in_word("TIM", ["G", "V"])
    '_ _ _'
    >>> show_letters_in_word("PIZZA", ["A", "I", "P", "Z"])
    'P I Z Z A'
    """
    upper_list =[]
    word = word.strip().upper()
    my_string = ""
    for upper_char in letters:
        upper_list += upper_char.upper()
    
#    upper_list = list("".join(letters).upper())

    for char in word:
        if char in upper_list:
            my_string += (f'{char} ')
        else:
            my_string += "_ "
    my_string = my_string.strip()

    return my_string

def all_letters_found(word, letters): #OK
    """Returns True if all letters in word are in the list 'letters'"""
    if "_" in show_letters_in_word(word, letters):
        return False
    else:
        return True

def main(turns): ##OK
    """
    Runs the game. Allows for "turns" loops (attempts).
    At each turn:
    1. Ask the user for a letter
    2. Add the letter to the list of letters already tried by the player
    3. If the letter was already tried, ask again
    4. Use the show_letters_in_word function to display hints about the word
    5. Remove 1 to the number of tries left
    6. Check if the player
        - won (= word has been found)
        - lost (= word has not been found, no tries left)

    Do not forget to pick a random word first :-)

    """
    
    tested_letters = []
    word_m = (pick_random_word(textfile))
    winner = all_letters_found(word_m, tested_letters)
    
    while turns > 0:
        letters_m = input(f"Please Enter a Letter: ")
        if letters_m.isalpha() == False or ((len(letters_m))>1):
            print("Please enter a valid input!")
            continue
        elif letters_m in tested_letters:
            print("Letter already tried, try a different letter")
            continue
        else:
            tested_letters.append(letters_m)

        print(show_letters_in_word(word_m, tested_letters))
        turns -= 1
        winner = all_letters_found(word_m, tested_letters)
        print(f"You have {turns} turns left!")
    
        if winner:
            print("You win!")
            break
        elif turns == 0:
            print(f"No more turns left :( \nNice try! The word was {word_m}~")


if __name__ == "__main__":
    main(NB_TURNS)