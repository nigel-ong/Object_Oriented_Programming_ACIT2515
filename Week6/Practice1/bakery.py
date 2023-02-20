class Bakery:
    def __init__(self, name) -> None:
        self.name = name
        self.croissants = 0
        self.money = 0

    def bake(self,num):
        if str(num).isnumeric() == False:
            raise ValueError("Please enter whole number!")
        else:
            self.croissants += int(num) 
            
    def sell(self,number=1):
        if type(number) is not int or number < 0:
            raise ValueError("Please enter a whole number, not a string!")
        
        if number > self.croissants:
            raise RuntimeError(f"You cannot sell more croissants than we made! we only have {self.croissants} croissants")
        else:
            self.croissants = self.croissants - number
            self.money += number*3
        
    def __str__(self) -> str:
        return self.name

# if __name__ == "__main__":
#     n = Bakery("A bakery")
#     n.bake(100)
    

