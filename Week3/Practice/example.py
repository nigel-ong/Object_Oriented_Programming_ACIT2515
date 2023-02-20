class Person:
    def __init__(self, name_of_the_person, useless_parameter):
        print("IN THE CONSTRUCTOR")
        self.name = name_of_the_person
    
    def hello(self, other_name, something="default"):
        print("Hello there, my name is ", self.name)
        print("Nice to meet you, ", other_name)
        print(something)
    # def __init__(self) -> None:
    #     pass

class Calculator:
    # def __init__(self, value1, value2):
    #     self.value1 = value1
    #     self.value2 = value2

    # def sum(self):
    #     self.result = self.value1 + self.value2
    #     return self.result
    def __init__(self):
        pass
    
