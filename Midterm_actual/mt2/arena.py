class Arena:
    def __init__(self,pokemon=None) -> None:
        self.pokemons = []
        if pokemon is None:
        with open (filename,"r") as f:
            for pokemon in f:
                pokemon = pokemon.strip().split(",")
                self.pokemons.append()

    def __add__(self):
        pass
    
    def __len__(self):
        pass

if __name__ == "__main__":
    A = Arena()
    print(A.pokemons)