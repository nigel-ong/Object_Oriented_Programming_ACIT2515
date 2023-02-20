import json
import random

from question import Question


class QuestionLibrary:
    def __init__(self, filename="trivia.json") -> None:
        """creates a List of question objects by opening a json file and passing a json file into the imported Question class.

        Args:
            filename (str, optional): Takes a optional file but defaults to "trivia.json" if nothing entered. Creates a list of Question objects.
        """
        self.questions = []
        with open(filename, "r") as fn:
            data = json.load(fn)
            for q_dict in data:
                self.questions.append(Question(**q_dict))

    def get_categories(self):
        """Gets all categories from the pool of question objects

        Returns:
            (List): Creates a list of categories by looping in the self.questions list and adds category from 
            all the questions objects into the list. Once done returns the list, passes it through a set that helps
            remove the repeated categories and then turns the tuple back into a list. Returns that final list        
        """
        cat_list=[]
        for q_obj in self.questions:
            cat_list.append(q_obj.category)
        return list(set(cat_list))

    def get_questions(self, category:str = None, difficulty:str = None, number:int = None):
        """Takes the self.question list and filters the list based on category, difficulty, 
        and number of questions revealed in random order.  

        Args:
            category (str, optional): Passes a str argument and uses the argument and compares to a new filtered_list 
            of self.questions. Checks if argument exists and if it is in self.get_category
            if it does, loops through a filtered_list copy (copy of a copy) and if the object category is not matching to the argument
            removes the question object from the filtered_question list. Defaults to None.
            
            difficulty (str, optional): Passes a str argument and uses the argument and compares to filtered_list. 
            Checks if argument exists and if it is in a list of ["easy", "medium", "hard"]
            if it does, loops through a filtered_list copy and if the object difficulty is not matching to the argument
            removes the question object from the filtered_question list. Defaults to None.
            
            number (int, optional): Just a number to set the amount of question objects to show
            if none is entered will show all. Defaults to None.

        Returns:
            List: A filtered_list of questions matches the entered arguments, randomly shuffles the questions.
        """

        filtered_questions = self.questions[:]
        if category and category in self.get_categories():
            for qs in filtered_questions[:]:
                if qs.category != category:
                    filtered_questions.remove(qs)
        
        if difficulty and difficulty in ["easy", "medium", "hard"]:
            for qs in filtered_questions[:]:
                if qs.difficulty != difficulty:
                    filtered_questions.remove(qs)
        
        random.shuffle(filtered_questions)
        if number:
            filtered_questions = filtered_questions[:number]

        return filtered_questions

    def __len__(self) -> int:
        """uses the dunder "magic method" len and returns the len length of self.questions

        Returns:
            int: returns a int, the length of self.questions.
        """
        return len(self.questions)



if __name__ == "__main__":
     None
