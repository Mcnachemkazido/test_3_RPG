import random
from core.monster import Monster

class Goblin(Monster):
    def __init__(self,name):
        super().__init__(hp=20,
        type="goblin",
        name=name,
        speed=random.randint(5,10),
        power=random.randint(5,10),
        armor_rating=1)