import json
from question import Question
import random

class QuestionLibrary:
    def __init__(self, filename='trivia.json'):
        self.questions = []
        try:
            with open(filename, 'r') as file:
                questions_data = json.load(file)
                for q_data in questions_data:
                    self.questions.append(Question(
                        q_data['question'], 
                        q_data['correct_answer'], 
                        q_data['incorrect_answers'],
                        q_data['category'],
                        q_data['difficulty']
                    ))
        except:
            raise AssertionError
        
    def get_categories(self):
        return list(set(q.category for q in self.questions))

    def get_questions(self, category=None, difficulty=None, number=None):
        questions = self.questions[:]
        if category:
            questions = [q for q in questions if q.category == category]
        if difficulty and difficulty in ["easy", "medium", "hard"]:
            questions = [q for q in questions if q.difficulty == difficulty]
        if number:
            questions = questions[:number]
        random.shuffle(questions)
        return questions
    
    def __len__(self):
        return len(self.questions)
