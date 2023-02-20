class Pokemon:
    """Creates a pokemon class with health,attack,amour, and level. Has an element and an name
    I READ THE TESTS AND INSTRUCTIONS
    I would improve the game if you pokemon is at a negative amount of health it will check and reset it to zero
    Replacing the self.armor with defense
    """
    def __init__(self,name:str,element:str) -> None:
        self.name = name
        self.element = element
        self.health = 100
        self.attack = 0
        self.armor = 0
        self.level = 1
        if self.element not in ["fire", "water", "grass", "electric"]:
            raise ValueError("pokemon not of correct attribute!")
        
        if self.health < 0 or self.health > 100 :
            raise ValueError("health must be between 0-100")
        if self.attack < 0 or self.attack > 9999 :
            raise ValueError("attack must be between 0-100")
        if self.armor < 0 or self.armor > 9999 :
            raise ValueError("defense must be between 0-100")
        if self.level < 0 or self.level > 100 :
            raise ValueError("level must be between 0-100")

    def set_health(self,number:int):
        if type(number) != int:
            raise ValueError("health must be an integer")
        if number > 0:
            self.health = number
        else:
            self.health = 0

    def is_active(self:bool):     
        if self.health > 0:
            return True
        else:
            return False

    def level_up(self):
        self.level += 1
        self.health = 100 * self.level
    
    def fight(self,opp):
        if not isinstance(opp,Pokemon):
            raise valueError("opp must be a pokemon")
        opp.health = opp.health - (self.attack - opp.armor) 
        if opp.health < 0:
            opp.health = 0
        # self.health = self.health - (opp.attack - self.armor) 
        # if self.health < 0:
        #     self.health = 0
        c_health = self.health - (opp.attack - self.armor - self.attack) 
        if c_health < 0:
            c_health = 0
        self.set_health(c_health)

    def __str__(self):
        return f"<{self.name} [{self.element}] ({self.health}, {self.attack}, {self.armor})>"

