import random
from core.player import Player
from core.goblin import Goblin
from core.orc import Orc



class Game:
    def start(self):
        flag = True
        while flag:
            self.show_menu()
            my_input = input()
            if my_input == "no":
                flag = False
            p = self.create_player()
            m = self.choose_random_monster()
            self.battle(p, m)



    def show_menu(self):
        print("יש לך אפשרות לבחור בין קרב ליציאה בכל עת yrs or no")

    def create_player(self):
        player = Player("menachem")
        return player


    def choose_random_monster(self):
        monsters = [Goblin,Orc]
        monster = monsters[random.randint(0,1)]("a_mess")
        return monster

    def battle(self,player,monster):
        begins = self.no_begins(player,monster)
        flag = True
        while flag:
            if begins == player:
                begins = monster
                no_begins = player
            else:
                begins = player
                no_begins = monster
            begins.attack(no_begins,self)
            if no_begins.hp <= 0:
                print(no_begins.name, "lost")
                flag = False


    def no_begins(self, player, monster):
        first_player = self.roll_dice(6) + player.speed
        first_monster = self.roll_dice(6) + monster.speed
        if first_player > first_monster:
            no_begins_to_attack = monster
        elif first_monster > first_player:
            no_begins_to_attack = player
        else:
            no_begins_to_attack = monster
        return no_begins_to_attack


    def roll_dice(self,sides):
        if sides == 6 or sides == 20:
            return random.randint(1,sides)
        return None

