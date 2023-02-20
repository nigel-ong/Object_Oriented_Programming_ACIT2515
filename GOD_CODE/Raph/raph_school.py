import csv

class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
        
    def average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        else:
            return None
        
    def __str__(self):
        return f'{self.name}, {self.id}, {self.average_grade()}'

class School:
    def __init__(self):
        self.students = []
        self.read_students()
        self.read_grades()

    def read_students(self):
        with open('students.csv', 'r') as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                name, id = row
                student = Student(name, id)
                self.students.append(student)

    def read_grades(self):
        with open('grades.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                id = row[0]
                grades = [int(x) for x in row[1:]]
                student = next((s for s in self.students if s.id == id), None)
                if student:
                    student.grades = grades


    def find_students_by_name(self, name):
        return [s for s in self.students if s.name.lower() == name.lower()]
    
    def find_students_by_id(self, id):
        return [s for s in self.students if s.id == id]
    
    def print_student_list(self, full=False, sort=None):
        students = self.students
        if sort:
            if sort == 'name':
                students.sort(key=lambda x: x.name)
            elif sort == 'id':
                students.sort(key=lambda x: x.id)
            elif sort == 'average':
                students.sort(key=lambda x: x.average_grade())
        for student in students:
            print(student)
            if full:
                print(student.grades)

if __name__ == '__main__':
    pass