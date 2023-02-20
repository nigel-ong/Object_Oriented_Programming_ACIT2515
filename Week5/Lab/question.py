import random


class Question:
    """Creates question objects with the arguments: questions, correct answer, incorrect answers, category, difficulty
    creates a list for all the of all the correct and incorrect answers. The list of possible answers are shuffled and their index numbers numbers
    increased by 1
    """
    def __init__(self,question, correct_answer, incorrect_answers, category, difficulty) -> None:
        self.question = question 
        self.correct_answer = correct_answer
        self.incorrect_answer = incorrect_answers
        self.category = category
        self.difficulty = difficulty 
        self.answers = [] #append correct_answer + incorrect_answer
        self.answers.append(self.correct_answer)
        for incorrect in self.incorrect_answer:
            self.answers.append(incorrect)
        random.shuffle(self.answers)
        self.answer_id = self.answers.index(correct_answer) + 1
        if self.difficulty not in ("easy", "medium", "hard"):
            raise AttributeError("Please enter a difficulty level")


    def __str__(self) -> str:
        """Creates a string that shows the random answers

        Returns:
            str: The original question and the list of answers in random order.
        """
        string = ""
        
        for index, answers in enumerate(self.answers, start=1): 
             string += f'\n{index} {answers}'
        return f"{self.question}{string}"




# if __name__ == "__main__":
#     q = Question("What is the name of the instructor?", "Tim", ["Alice", "Bob", "John"])
#     # print(q)
#     # main()