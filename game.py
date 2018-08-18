from sys import exit
from random import randint


class BattleScene(object):
    def battle(self):
        health = 800 # updatable health level during battle
        damage = 0 # variable storing damage level

        while health >= 0:
            damage = randint(50, 150)
            health -= damage
        ## MESSAGING DURING BATTLE
            if damage >= 50 and damage <= 70:
                print("Shaking hands, huh? Damage is just",damage)
                #print("New health is ", health)
            elif damage >= 130 and damage <= 150:
                print("What a hit! Damage is",damage)
                #print("New health is ", health)
            else:
                print("Damage is",damage)
                #print("New health is ", health)

            if health <= 0:
                print("Well, looks like somebody is dead. Farewell, buddy")
                break
            input("-"*30+"\nPress Enter to continue fighting...")
a = BattleScene()
a.battle()
