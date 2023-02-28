class Student:
    def __init__(self, name:str, student_id:str, grades=None) -> None:
        self.name = name
        self.student_id = student_id
        self.grades = grades

        if self.grades is None:
            self.grades = []
        

    def to_dict(self):
        self.my_dict2 = {
            "name": self.name, 
            "student_id": self.student_id, 
            "grade": self.grades
            } 
        return self.my_dict2
    
    # def to_dict(self):
    #     return {"name": self.name, "student_id": self.student_id, "grade": self.grades} 

    def __str__(self) -> str:
        return f'${self.my_dict2}'
    
    @property
    def gpa(self):
        if self.grades == []:
            return 0
        else:
            return round(sum(self.grades)/len(self.grades),2)  

    
if __name__ == "__main__":
    n = Student("Nigel","id1",[1,2,3,4,5])