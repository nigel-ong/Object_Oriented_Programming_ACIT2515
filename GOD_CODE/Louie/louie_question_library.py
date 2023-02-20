# file name: question_library.py
# Author: Louie Jade Causing
# Student #: A01317095
# Set-B
# Last Modified on February 10, 2023

import json
import random

# import pathlib
from question import Question


class QuestionLibrary:
    """This class represents a library of questions and allows filtering of
    questions by category, difficulty, and number."""
    def __init__(self, file_name="trivia.json"):
        """Initializes the QuestionLibrary class by loading questions from a file in JSON format.
        Args:
            file_name (str, optional): _The name of the file containing the questions in JSON format. Defaults to "trivia.json".
        """
        # The 3 commented lines of code are what you need to use to look for the file path of the trivia question file if you are receiveing an error on the file name
        # cwd = pathlib.Path(__file__).parent
        # file_path = cwd / file_name
        # with open(file_path, "r") as fp:
        with open(file_name, "r") as fp:
            files = json.load(fp)
        self.questions = []
        for details in files:
            self.questions.append(
                Question(**details))

    def get_categories(self) -> list:
        category_list = []
        for details in self.questions:
            if details.category not in category_list:
                category_list.append(details.category)
        return category_list

    def get_questions(self, category=None, difficulty=None, number=None):
        """Returns a list of questions filtered by category, difficulty, and number of questions requested

        Args:
            category (str , optional): The category of the questions. Defaults to None.
            difficulty (str, optional): The difficulty level of the questions. Defaults to None.
            number (int, optional): The number of questions to return. Defaults to None.

        Returns:
            list: list of questions filtered by category, difficulty and number of questions requested.
        """
        list_questions = self.questions[:]
        if category and category in self.get_categories():
            list_questions = [
                details for details in list_questions if details.category == category]
        if difficulty and difficulty in ["easy", "medium", "hard"]:
            list_questions = [
                details for details in list_questions if details.difficulty == difficulty]
        random.shuffle(list_questions)
        if number:
            list_questions = list_questions[:int(number)]
        return list_questions

    def __len__(self):
        """
        Returns the number of questions in the library.

        Returns:
            length of the question
        """
        return len(self.questions)
