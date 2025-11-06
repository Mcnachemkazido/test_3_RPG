import random
from core.monster import Monster


class Orc(Monster):
    def __init__(self,name):
        super().__init__(hp=50,
        type="orc",
        name = name,
        speed=random.randint(0,5),
        power=random.randint(10,15),
        armor_rating=random.randint(2,8))

