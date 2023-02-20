textfile = "words.txt"
# textfile = 'Week3\Lab3\words.txt'
import random


class SecretWord:
    def __init__(self, word=None):
        if word is None:
            with open(textfile, "r") as f:
                content = f.readlines()
                selected_word = random.choice(content)
                self.selected_word = selected_word.strip()
        else:
            self.selected_word = word

    def show_letters(self, letters):
        upper_list = []

        word = self.selected_word.strip().upper()
        my_string = ""
        for upper_char in letters:
            upper_list += upper_char.upper()

        for char in word:
            if char in upper_list:
                my_string += f"{char} "
            else:
                my_string += "_ "
        my_string = my_string.strip()

        return my_string

    def check_letters(self, letters):
        if "_" in self.show_letters(letters):
            return False
        else:
            return True

    def check(self, string):
        if string.upper() == self.selected_word.upper():
            return True
        else:
            return False


class Game:
    def __init__(self, turns=10):
        self.turns = turns
        self.tried_letters = []
        self.secret_word = SecretWord()

    def play_one_round(self):
        print(self.secret_word.selected_word)
        letters_m = input(f"Please Enter a Letter: ").upper()
        while (
            letters_m.isalpha() == False
            or letters_m == None
            or letters_m in self.tried_letters
        ):
            if letters_m in self.tried_letters:
                print("Letter already tried, try a different letter")
                letters_m = input(f"Please Enter a Letter: ").upper()
                continue
            else:
                print("Please enter a valid input!")
                letters_m = input(f"Please Enter a Letter: ").upper()
                continue

        if len(letters_m) == 1:
            self.tried_letters.append(letters_m)
            print(self.secret_word.show_letters((self.tried_letters)))
            self.turns -= 1
            print(f"You have {self.turns} turns left!")
            if self.secret_word.check_letters(self.tried_letters) == True:
                return True
            else:
                return False
        else:
            print(self.secret_word.show_letters((self.tried_letters)))
            self.turns -= 1
            if self.secret_word.check(letters_m) == True:
                return True
            else:
                return False

    def play(self):
        while self.turns > 0:
            if self.play_one_round() == True:
                print("Congratulations, you win!")
                return True

        print(
            f"No more turns left :( \nNice try! The word was {self.secret_word.selected_word}~"
        )
        return False


def main():
    my_game = Game(10)  # for 10 turns
    my_game.play()
    print()


if __name__ == "__main__":
    main()
