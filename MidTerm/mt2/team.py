from pokemon import Pokemon
from arena import Arena

class Team:
    def __init__(self) -> None:
        self.arena = Arena()

    def make_team(self,level):
        team = []
        