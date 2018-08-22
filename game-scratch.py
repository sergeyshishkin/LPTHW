from sys import exit
from random import randint
import time


### PROTOTYPE OF BEDROOM TO INVADE SCENE TRANSITION
### A = CLASSNAME().FUNCNAME()

class Bedroom():
    def enter(self):
        print("Launch Bedroom")
        global o
        o = input("Choose item> ")
        i = input("Next scene> ")
        if i == "1":
            next_scene = Invade().enter()
        else:
            print("DEAD END")
            exit(1)

class Invade():
    def enter(self):
        print("Launch Invade")
        v = input("Choose your item> ")
        if v == o:
            print("MATCH")
        elif v == '2':
            next_scene = Battle().enter()
        else:
            print("NOPE")
            exit(1)


class Battle():
    def enter(self):
        hero_health = 200
        enemy_health = 200

        def fun(hero_health, enemy_health):

            while hero_health > 0 and enemy_health > 0:

                # FUNCTION THAT GENERATES DAMAGE, SHOW TEXT ABOUT DAMAGE AND WHO DID THE DAMAGE
                def generate_damage(user):
                    damage = randint(50, 150)
                    if damage >= 50 and damage <= 70:
                        print(user, "strikes poorly and hit only",damage,"damage")
                    elif damage >= 130 and damage <= 150:
                        print(user, "strikes a great hit! Damage is",damage)
                    else:
                        print(user, "strikes ordinary",damage,"damage")
                    return damage

                # CALLING generate_damage FUNCTION
                damage = generate_damage("Enemy")

                # HERE IS CALCULATING HEALTH AND FATAL LEVEL FOR HERO
                hero_health -= damage
                print ("New hero health is: ", hero_health) #IN PRODUCTION, MOVE THIS LINE AFTER "ELSE: PASS"
                if hero_health <= 0:
                    print("Well, looks like hero is dead. Farewell, buddy")
                    print("Luckly, you are in the game, it's a fiction. You can try kick his ass again")
                    keys = input("Press Enter to continue...")
                    next_scene = Battle().enter()
                    break

                else:
                    pass

                time.sleep(1) #DELAY TO MAKE GAME NOT SO RAPID

                # CALLING generate_damage FUNCTION
                damage = generate_damage("Hero")

                # HERE IS CALCULATING HEALTH AND FATAL LEVEL FOR ENEMY
                enemy_health -= damage
                print ("New enemy health is: ", enemy_health) #IN PRODUCTION, MOVE THIS LINE AFTER "ELSE: PASS"
                if enemy_health <= 0:
                    print("Enemy is dead. Hero goes further")
                    break
                else:
                    pass

                time.sleep(1) #DELAY TO MAKE GAME NOT SO RAPID

        fun(hero_health, enemy_health)

class Start():

    def __init__(self, scene):
        self.scene = scene
        scene = Bedroom().enter()

a = Start('bedroom')




# ### PROTOTYPE OF BEDROOM TO INVADE SCENE TRANSITION
# ### A = CLASSNAME().FUNCNAME()
#
# class Bedroom():
#     def enter(self):
#         print("Launch Bedroom")
#         global o
#         o = input("Choose item> ")
#         i = input("Next scene> ")
#         if i == "1":
#             next_scene = Invade().enter()
#         else:
#             print("DEAD END")
#             exit(1)
#
# class Invade():
#     def enter(self):
#         print("Launch Invade")
#         v = input("Choose your item> ")
#         if v == o:
#             print("MATCH")
#         else:
#             print("NOPE")
#             exit(1)
#
# class Start():
#
#     def __init__(self, scene):
#         self.scene = scene
#         scene = Bedroom().enter()
#
# a = Start('bedroom')
