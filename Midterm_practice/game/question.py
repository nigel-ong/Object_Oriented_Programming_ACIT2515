import random

class Question:
    def __init__(self, question, correct_answer, incorrect_answers, category, difficulty) -> None:
        self.answers = []
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers
        self.category = category
        self.difficulty = difficulty
        
        for wr in self.incorrect_answers:
            self.answers.append(wr)
        self.answers.append(self.correct_answer)
        random.shuffle(self.answers)
        self.answer_id = self.answers.index(correct_answer) +1
        if self.difficulty not in ["easy", "medium", "hard"]:
            raise AttributeError("Please enter a difficulty")

    def __str__(self) -> str:
        string = ""
        for index, answer in enumerate(self.answers, start=1):
            string += f'\n{index} {answer}'
        return f'{self.question}{string}' 



        

# if __name__ == "__main__":
#      q = Question("What is the name of the instructor?", correct_answer="Tim", incorrect_answers=["Alice", "Bob", "John"], category="some", difficulty="hard")
