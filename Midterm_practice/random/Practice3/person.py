#create me a class of Person with name and age as attributes
class Person:
    def __init__(self, name, age):
        self.name = name   
        self.age = age
        if type(name) != str or len(name) < 3 or age < 0 or type(age) != int:
            raise AttributeError("Enter a string name or a Positive Age")

    def get_name(self):
        return f'{self.name.upper()} / {self.age}' 