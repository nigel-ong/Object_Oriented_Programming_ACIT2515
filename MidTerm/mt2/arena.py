from pokemon import Pokemon
import csv
class Arena:
    def __init__(self) -> None:
        self.arena = []

    def add(self,pokemon):
        if not isinstance(pokemon,Pokemon):
            raise AttributeError("Is not a pokemon!")
        self.arena.append(pokemon)

    def active(self):
        active = []
        for pkmn in self.arena:
            if pkmn.health > 0:
                active.append(pkmn)
        return active

    def __len__(self):
        return len(self.active())
    
    def load_from_file(self,filename="pokemons.txt"):
       with open(filename, "r") as pkmn:
            reader = csv.reader(pkmn)
            for row in reader:
                name, health, level = row
                pokemon = Pokemon(name, int(health), int(level))
                self.add(pokemon)




# if __name__ == "__main__":
#     # A = Arena()
#     # print(A.arena)
#     # A + "nigelmon"
#     # print(A.arena)