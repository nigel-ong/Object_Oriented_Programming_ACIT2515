import question_library

class Game:
    def __init__(self,filename="trivia.json", category:str = None, difficulty:str = None, number:int =None) -> None:
        """ Initiates the game class to create a game object, passes the 4 arguments to question library
        to create return a filtered list depending on the arguments given. 

        Args:
            filename (str, optional): Takes in a optional argument to create question objects from a json file. Defaults to "trivia.json".
            
            category (str, optional): Takes in a argument that is listed in 
            ['General Knowledge', 'Science: Computers', 'Geography', 'Science & Nature', 'Animals']. 
            Defaults to None.
            
            difficulty (str, optional): Takes in a argument that is listed in 
            ["hard", "medium","easy"]. Defaults to None.
            
            number (int, optional): _description_. Defaults to None.
        """
        self.score = 0
        self.question_lib = question_library.QuestionLibrary(filename)
        self.questions = self.question_lib.get_questions(category, difficulty, number)
        self.number = number

    def play(self):
        """Starts the game of the game object. Prints all the questions of the filtered list
        Takes a int input, if the input is not a int will give warn user to enter a int
        each question will award the player points depending on the difficulty.
        """
        for qs in self.questions:
            print(qs,"\n")
            user_input = str(input("Enter an answer between 1-4: \n"))

            while user_input.isnumeric() == False or user_input not in ["1","2","3","4"]:
                user_input = str(input("Please enter an answer between 1-4: \n"))

            if user_input.isnumeric() == True:
                user_input = int(user_input)

            if user_input == qs.answer_id:
                if qs.difficulty == "easy":
                    self.score += 1
                elif qs.difficulty == "medium":
                    self.score += 2
                elif qs.difficulty == "hard":
                    self.score += 3
                
                print(f'Good choice, your score was {self.score}\n')

            else: 
                print(f'Nice try but the correct answer is {qs.answer_id}, your score is {self.score}\n')
        print(f'Your final score is {self.score}, Awesome Job.')

if __name__ == "__main__":
    g = Game(difficulty="hard", number=5)
    g.play()