import random

class Monster:
    def __init__(self,hp,type,speed,power,armor_rating,name):
        self.name = name
        self.hp = hp
        self.type = type
        self.speed = speed
        self.power = power
        self.armor_rating = armor_rating
        self.weapon = ["סכין","חרב","גרזן"][random.randint(0,2)]

    def speak(self):
        print(f"{self.type} {self.name}")

    def attack(self,player,game):
        total_start = game.roll_dice(20) + self.speed
        if total_start > player.armor_rating:
            impact_calculation = game.roll_dice(6) + self.power
            if self.weapon == "סכין":
                impact_calculation = impact_calculation * 0.5
            elif self.weapon == "גרזן":
                impact_calculation = impact_calculation *1.5
            player.hp -= impact_calculation

