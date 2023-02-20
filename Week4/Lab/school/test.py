import csv

class Student:
    def __init__(self, name, stu_id, grades):
        self.name = name
        self.stu_id = stu_id
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)

class School:
    def __init__(self):
        self.student_obj_list = []
        with open("students.csv", "r") as student_file:
            student_reader = csv.reader(student_file)
            next(student_reader) # skip header row
            for row in student_reader:
                name, stu_id = row[0], row[1]
                grades = []
                with open("grades.csv", "r") as grades_file:
                    grades_reader = csv.reader(grades_file)
                    next(grades_reader) # skip header row
                    for grade_row in grades_reader:
                        if grade_row[0] == stu_id:
                            grades.append(float(grade_row[1]))
                self.student_obj_list.append(Student(name, stu_id, grades))

    def find_students_by_name(self, name):
        return [student for student in self.student_obj_list if student.name.lower() == name.lower()]

    def find_students_by_id(self, stu_id):
        return [student for student in self.student_obj_list if student.stu_id == stu_id]

    def print_student_list(self, sort=None, full=False):
        if sort is not None:
            if sort.lower() in ["name", "id", "average"]:
                if sort.lower() == "name":
                    self.student_obj_list = sorted(self.student_obj_list,key= lambda n: n.name)
                elif sort.lower() == "id":
                    self.student_obj_list = sorted(self.student_obj_list,key= lambda i: i.stu_id)
                elif sort.lower() == "average":
                    self.student_obj_list = sorted(self.student_obj_list,key= lambda a: a.average_grade())
            else:
                raise AttributeError("Name, ID, Average or nothing.")

        if full:
            for full_student in self.student_obj_list:
                print(f'{full_student.name}, {full_student.stu_id},{full_student.average_grade()}, {full_student.grades}')
        else:
            for full_student in self.student_obj_list:
                print(f'{full_student.name}, {full_student.stu_id}, {full_student.average_grade()}')

def main():
    school = School()
    school.print_student_list(sort="average", full=True)
    print(school.find_students_by_name("John"))
    print(school.find_students)

if __name__ == '__main__':
    main()