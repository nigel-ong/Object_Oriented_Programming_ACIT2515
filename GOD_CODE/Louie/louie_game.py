# PyQuiz
# file name: game.py
# Author: Louie Jade Causing
# Student #: A01317095
# Set-B
# Last Modified on February 10, 2023

# Note: If you receive an error when launching the game, make sure you modify
# question_library.py by pointing it to the actual path of the trivia file instead of just the file name
# If you have any questions, or if you found any bugs, contact me at lcausing@my.bcit.ca

from question_library import QuestionLibrary


class Game:
    """A class to represent the Trivia Game.

        Attributes:
            play_game (QuestionLibrary): An instance of QuestionLibrary class.
            questions (list): A list of question instances, filtered based on category, difficulty, and number.
            score (int): The total score of the player.
            number (int): The number of turns for the game.
        """
    def __init__(self, file_name="trivia.json", category=None, difficulty=None, number=None):
        """The constructor for Game class.
        Args:
            file_name (str, optional): The file name to retrieve questions from. Defaults to "trivia.json".
            category (str, optional): The category of questions to include in the game. Defaults to None.
            difficulty (str, optional): The difficulty of questions to include in the game. Defaults to None.
            number (int, optional): The number of turns for the game. Defaults to None.
        """
        self.play_game = QuestionLibrary(file_name)
        self.questions = self.play_game.get_questions(
            category, difficulty, number)
        self.score = 0
        self.number = number

    def play(self):
        """The method to start the trivia game.
        """
        print("\nGame Instructions: Type 1, 2, 3, or 4 to answer the questions\n")
        for question in self.questions:
            print(f"{self.questions.index(question)+1}.) {question}")
            answer = ""
            while answer not in ["1", "2", "3", "4"]:
                answer = input("Enter your Choice: ")
                if answer not in ["1", "2", "3", "4"]:
                    print("Invalid Input, Type 1, 2, 3, or 4 only\n")
            if int(answer) == question.answer_id:
                print("You Guessed it Right!\n")
                if question.difficulty == "easy":
                    self.score += 1
                if question.difficulty == "medium":
                    self.score += 2
                if question.difficulty == "hard":
                    self.score += 3
            else:
                print(f"\nWrong!\nThe Answer was {question.correct_answer}\nYour Final Score: {self.score}\n")


def main():
    """The main function to start the trivia game.
    """
    trivia_file_name = "trivia.json"
    print("\nWelcome to PyQuiz!\nDo you have what it takes to answer these trivia questions?\n")
    # Choose your category
    category_list = QuestionLibrary().get_categories()
    print(f"Category: {category_list}")
    category_list = [category.lower() for category in category_list]
    category_input = ""
    while category_input.lower() not in category_list:
        category_input = input(
            "Enter your Category (Press Enter if you want random): ").lower()
        if not category_input:
            break
        elif category_input.lower() not in category_list:
            print("Invalid Input, Select the right category\n")
        else:
            print("Category Confirmed!\n")
    # Choose your difficulty
    difficulty_list = ["easy", "medium", "hard"]
    print(f"Difficulty: {difficulty_list[0].title()}, {difficulty_list[1].title()}, {difficulty_list[2].title()}")
    difficulty_input = ""
    while difficulty_input not in difficulty_list:
        difficulty_input = input(
            "Enter your Difficulty (Press Enter if you want random): ").lower()
        if not difficulty_input:
            break
        elif difficulty_input.lower() not in difficulty_list:
            print("Invalid Input, Select a valid difficulty!\n")
        else:
            print("Difficulty Confirmed!\n")
    # Choose the number of turns you want
    number_input = ""
    while not number_input.isnumeric():
        number_input = input("Enter the Number of Turns: ")
        if not number_input.isnumeric():
            print("Invalid Input, Enter a Number only!\n")
        else:
            print("Number of Turns Confirmed!\n")
    input("Press Enter to Start the Game!\n")
    session = Game(file_name=trivia_file_name, category=category_input, difficulty=difficulty_input, number=number_input)
    session.play()


if __name__ == '__main__':
    main()
