class Person:
    def __init__(self,name,age) -> None:
        self.name = name
        self.age = age
        if len(self.name) < 3 or str(self.age).isnumeric() == False or type(self.age) != int:
            raise AttributeError("Please enter a String name in '' larger than 2 and a positive whole number")
    def get_name(self):
        self.name.upper() 

        
# if __name__ == "__main__":