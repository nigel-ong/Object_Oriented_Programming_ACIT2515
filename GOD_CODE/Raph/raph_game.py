from question_library import QuestionLibrary

class Game:
    def __init__(self, filename="trivia.json", category=None, difficulty=None, number=None):
        self.library = QuestionLibrary(filename)
        self.questions = self.library.get_questions(category, difficulty, number)
        self.score = 0
        self.number = number

    def play(self):
        for question in self.questions:
            print(f'{self.questions.index(question) + 1}. {question}')
            answer = input("Enter the number of the correct answer: ")
            while answer not in ["1", "2", "3", "4"]:
                print("Invalid input. Please enter a number between 1 and 4.")
                answer = input("Enter the number of the correct answer: ")
            if int(answer) == question.answer_id:
                print(f"Correct!\n")
                self.score += 1 if question.difficulty == "easy" else 2 if question.difficulty == "medium" else 3
            else:
                print(f"Incorrect. The answer was {question.correct_answer}\n")
        print(f"Your final score is {self.score}.")

if __name__ == "__main__":
    first_question = Game(difficulty="hard", number=5)
    first_question.play()