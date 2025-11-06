import random

class Player:
    def __init__(self,name):
        self.name = name
        self.profession = ["לוחם", "מרפא"][random.randint(0, 1)]
        self.armor_rating = random.randint(5,15)
        self.speed = random.randint(5, 10)
        self.power = random.randint(5,10)
        if self.profession == "לוחם":
            self.power += 2
        self.hp = 50
        if self.profession == "מרפא":
            self.hp += 10

    def speak(self):
        print(f"i am {self.name} player")

    def attack(self,monster,game):
        total_start = game.roll_dice(20) + self.speed
        if total_start > monster.armor_rating:
            impact_calculation = game.roll_dice(6) + self.power
            monster.hp -= impact_calculation








