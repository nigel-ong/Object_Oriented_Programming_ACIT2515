from question_library import QuestionLibrary 

class Game:
    def __init__(self,filename="trivia.json",category:str=None,difficulty:str=None,number:int=None) -> None:
        self.library = QuestionLibrary(filename)
        self.score = 0
        self.questions = self.library.get_questions(category,difficulty,number)
        self.number = number

    def play(self):
        for qs in self.questions:
            print(qs,"\n")
            print(qs.answer_id)
            user_input = str(input("Enter number 1-4: "))
            while user_input.isnumeric() == False or user_input not in ["1","2","3","4"]:
                user_input = str(input("Please enter a number between 1-4: "))

            if int(user_input) == qs.answer_id:
                if qs.difficulty == "easy":
                    self.score += 1 
                elif qs.difficulty == "medium":
                    self.score += 2 
                elif qs.difficulty == "hard":
                    self.score += 3 
                print(f"\nNice, your current score is {self.score}\n")
            else:
                print(f"\nNice try, the correct answer was {qs.correct_answer}\n")
        print(f"Good game, your final score is {self.score}, great job\n")
            

if __name__ == "__main__":
    g= Game(category="Geography", difficulty="easy", number=8)
    g.play()