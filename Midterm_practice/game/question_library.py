import json
import random

from question import Question


class QuestionLibrary:
    def __init__(self, filename="trivia.json") -> None:
        self.questions = []
        with open(filename, 'r') as f:
            data = json.load(f)
            for qs in data:
                self.questions.append(Question(**qs))

    def get_categories(self):
        cat_list = []
        for qs in self.questions:
            if qs.category not in cat_list:
                cat_list.append(qs.category)
        return cat_list
    
    def get_questions(self,category:str=None, difficulty:str=None, number:int=0):
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
    
    def __len__(self):
        return len(self.questions)



if __name__ == "__main__":
    ql = QuestionLibrary()
    print(ql.get_questions(category="Geography", difficulty="hard", number=7))
    str(ql.get_questions(category="Geography", difficulty="hard", number=3))