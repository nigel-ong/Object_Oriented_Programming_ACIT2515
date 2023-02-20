import csv

class Student:
    def __init__(self, name:str, stu_id:str, grade:list) -> None:
        """Creates a student object with a name, student ID, and grade

        Args:
            name (str): takes a string that is the students name
            stu_id (str): takes a string that is the students ID
            grade (int): takes a list of grades 
        """
        self.name = name
        self.stu_id = stu_id
        self.grade = grade

    def average_grade(self):
        """computers the average grade 

        Returns:
            float: returns a float that is the average grade of a student 
        """
        counter = 0
        for grades in self.grade:
            counter += int(grades)
        return (counter/len(self.grade))



class School:

    def __init__(self) -> None:
        """Creates an school object that will create the student object that is read from students.csv and grades.csv. creates a dictionary and uses the dictionary to create a list of student objects.
        """
        student_dictionary ={}
        self.student_obj_list = []
        
        with open("students.csv", newline="") as students:
            reader = csv.reader(students)
            next(reader)
            for row in reader:
                student_dictionary.update({row[1]:[row[0]]})

        with open("grades.csv", newline="") as grades:
            reader = csv.reader(grades)
            for row in reader:
                if row[0] in student_dictionary.keys():
                    student_dictionary[row[0]].append(row[1:-1])
                    

        for key,value in student_dictionary.items():
            new_student = Student(value[0],key,value[1])
            self.student_obj_list.append(new_student)


    def find_student_by_name(self,name:str):
        """Takes a string and returns a list of all the student object instances whos name matches the argument.

        Args:
            name (str): the string is the name of a student you want to search for. Can be is case insensitive. 

        Returns:
            (list): returns a list of student object instance memory location. 
        """
        list_of_names = []
        for item in self.student_obj_list:
            if name.upper() in item.name.upper():
                list_of_names.append(item)
        return list_of_names

    def find_student_by_id(self, student_id:str):

        """Takes a string and returns a list of all the student object instances whos student matches the argument 

        Args:
            name (str): the string is the student id of a student you want to search for.

        Returns:
            (list): returns a list of student object instance memory location. 
        """
        list_of_ids = []
        for item in self.student_obj_list:
            if student_id == item.stu_id:
                list_of_ids.append(item)
        return list_of_ids
    
    def print_student_by_name(self, sort:str=None, full:bool=False):
        """Prints a list that shows all students with their names, student id, and average grade. If optional arguments are added then it shows all the grades for each student and sorts it by either name, id, or average

        Args:
            sort (str, optional): 1 of 3 strings that allows the method to sort the returned list. Defaults to None.
            full (bool, optional): allows the method to return the full information which includes the grades for every student in the list. Defaults to False.

        Raises:
            AttributeError: raises an error if a string is entered that does not match the word: name, id, average
        """
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
                print(f'{full_student.name}, {full_student.stu_id},{full_student.average_grade()}, {full_student.grade}')


        else:
            for full_student in self.student_obj_list:
                print(f'{full_student.name}, {full_student.stu_id}, {full_student.average_grade()}')
            




def main():
    school = School()
    school.print_student_by_name("name",True)
    print(school.find_student_by_name("lisa")[0].name)
    print(school.find_student_by_id("A0563260")[0].name)


if __name__ == "__main__":
    main()