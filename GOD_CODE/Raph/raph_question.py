import random

class Question:
    def __init__(self, question, correct_answer, incorrect_answers, category, difficulty):
        if difficulty not in ["easy", "medium", "hard"]:
            raise AttributeError
        else:
            self.difficulty = difficulty
        self.question = question
        self.correct_answer = correct_answer
        self.incorrect_answers = incorrect_answers
        self.category = category
        self.answers = incorrect_answers + [correct_answer]
        random.shuffle(self.answers)
        self.answer_id = self.answers.index(correct_answer) + 1

    def __str__(self):
        answer_str = ''
        for i, answer in enumerate(self.answers, start=1):
            answer_str += f"{i} {answer}\n"
        return f"{self.question}\n{answer_str}"
    
# if __name__ == "__main__":
#     q = Question("What is the name of the instructor?", correct_answer="Tim", incorrect_answers=["Alice", "Bob", "John"], category="random", difficulty="easy")
#     print(q.answers)
#     str(q)
#     print(q)
#     print(q.answer_id)
