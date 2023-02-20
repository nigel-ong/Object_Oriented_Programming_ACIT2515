class Pokemon:
    """Creates a pokemon object with element attribute within fire,water,grass,electric.
    
    Damage multiplier like for weaknesses (ie fire is weak to water. 1.5X damage)
    replace the name of self.armor with self.defense
    "I READ THE TESTS AND INSTRUCTIONS"
    """
    def __init__(self,name:str, element:str) -> None:
        self.name = name
        self.health = 100
        self.attack = 0
        self.armor = 0
        self.level = 1
        self.element = element

        if self.element not in ["fire", "water", "grass", "electric"]:
            raise ValueError('Element must be "fire", "water", "grass", "electric"')

    def set_health(self,number):
        if not isinstance(number,int):
            raise ValueError("Needs to be a whole number without quotes")
        if number < 0:
            self.health = 0
        else:
            self.health = number
    
    def is_active(self):
        if self.health > 0:
            return True
        else:
            return False

    def fight(self,opp):
        if not isinstance(opp,Pokemon):
            raise ValueError("Needs to be a pokemon")
        opp_damage = self.attack - opp.armor
        if opp_damage < 0:
            opp_damage = 0
        opp.health -= opp_damage

        player_damage = opp.attack - self.armor - self.attack 
        if player_damage < 0:
            player_damage = 0
        self.health -= player_damage

            

    def level_up (self) -> None:
        self.level += 1
        self.health = self.level * 100

    def __str__(self) -> str:
        return f"<{self.name} [{self.element}] ({self.health}, {self.attack}, {self.armor})>"