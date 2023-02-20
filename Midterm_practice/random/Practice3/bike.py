class Bike:
    def __init__(self) -> None:
        self.rider:str = None
        self.distance = 0

    def start_rental(self,name):
        if self.rider != None:
            raise RuntimeError("Bike is rented outZZZ")
        else:
            self.rider = name

        
    def bike(self,distance_num):
        if distance_num < 1:
            raise AttributeError("you cannot bike less than 1")
        self.distance +=distance_num
        if self.rider == None:
            raise RuntimeError("Bike is not rented out")
        
        
    def end_rental(self):
        if self.rider == None:
            raise RuntimeError("cannot end rental if never rented")
        distance = self.distance
        self.rider = None
        self.distance = 0
        return distance