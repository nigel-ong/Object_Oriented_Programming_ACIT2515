# file name: question.py
# Author: Louie Jade Causing
# Student #: A01317095
# Set-B
# Last Modified on February 10, 2023

import random


class Question:
    def __init__(self, question: str, correct_answer: str, incorrect_answers: list, category: str, difficulty: str) -> None:
        """
        Initializes a Question object with the given parameters.

        Args:
            question (str): The question text.
            correct_answer (str): The correct answer to the question.
            incorrect_answers (list): A list of incorrect answers to the question.
            category (str): The category of the question.
            difficulty (str): The difficulty level of the question, either "easy", "medium", or "hard".

        Raises:
            AttributeError: If the difficulty level is not "easy", "medium", or "hard".
        """
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers
        self.category = category
        if difficulty.lower() not in ["easy", "medium", "hard"]:
            raise AttributeError("Difficulty is only easy, medium, or hard")
        self.difficulty = difficulty.lower()
        # Housing all the answers in the list: answers
        self.answers: list[str] = []
        self.answers.append(self.correct_answer)
        self.answers.extend(incorrect_answers)
        random.shuffle(self.answers)
        self.answer_id = self.answers.index(correct_answer) + 1

    def __str__(self) -> str:
        """
        Returns a string representation of the Question object.

        Returns:
            str: A string representation of the Question object, including the question text and all possible answers.
        """
        question_answer_format = f"{self.question}\n"
        for count, line in enumerate(self.answers, start=1):
            question_answer_format += f"{count} {line}\n"
        return question_answer_format
