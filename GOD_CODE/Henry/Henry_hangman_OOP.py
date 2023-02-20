import random


class SecretWord:
    def __init__(self, word: str = None):
        if word is None or word == "":
            with open("words.txt") as f:
                word = random.choice(f.readlines())
        self.word = word.strip()

    def show_letters(self, guess_list: list[str]):
        word = self.word.upper()
        upper_list = [letter.upper() for letter in guess_list]
        for char in word:
            if char not in upper_list:
                word = word.replace(char, "_")
        my_string = " ".join(word)
        return my_string

    def check_letters(self, guess_list: list[str]):
        return "_" not in self.show_letters(guess_list)

    def check(self, guess: str):
        return self.word.upper() == guess.upper()


class Game:
    def __init__(self, turns: int = 10):
        self.turns = turns
        self.secretword = SecretWord()
        self.guess_list = []

    def play_one_round(self):
        print(f"You have {self.turns} turns left.") if self.turns > 1 else print(
            "Final turn!"
        )
        guess = input("Please enter a letter or a word for your guess: ")
        while (
            type(guess) is not str
            or len(guess) < 1
            or not guess.isalpha()
            or guess in self.guess_list
        ):
            if guess in self.guess_list:
                print("You've tried this before, try something else.")
                guess = input("Please enter a letter or a word for your guess: ")
            else:
                print("Invalid guess, please enter a letter or a word.")
                guess = input("Please enter a letter or a word for your guess: ")
        self.guess_list.append(guess.upper())
        if len(guess) == 1:
            print(self.secretword.show_letters(self.guess_list))
            self.turns -= 1
            return self.secretword.check_letters(self.guess_list)
        else:
            print(self.secretword.show_letters(self.guess_list))
            self.turns -= 1
            return self.secretword.check(guess)

    def play(self):
        print("Welcome to hangman, let's play a game!")
        print(self.secretword.show_letters(self.guess_list))
        while self.turns > 0:
            if self.play_one_round():
                print("Congratulations, you won!")
                print(f"The word was {self.secretword.word}")
                return True

        print("You lost, better luck next time!")
        print(f"The word was {self.secretword.word}.")
        return False


def main():
    my_game = Game(10)
    my_game.play()


if __name__ == "__main__":
    main()
