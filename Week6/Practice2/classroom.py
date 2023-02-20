class Classroom:
    def __init__(self,room,instructor) -> None:
        self.instructor = instructor
        self.room = room
        self.students = []


    def __add__(self,name):
        self.students.append(name)
        

    def __len__(self) -> int:
        return len(self.students)

    def __str__(self) -> str:
        return str(f"Room {self.room} [{self.instructor}] - {len(self)} students")


if __name__ == "__main__":
    cr = Classroom("123", "Teacher")
    cr + "John"