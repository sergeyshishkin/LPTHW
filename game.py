from sys import exit
from random import randint
import time


# class BattleScene(object):
#     def battle(self):
#         health = 800 # updatable health level during battle
#         damage = 0 # variable storing damage level
#
#         while health >= 0:
#             damage = randint(50, 150)
#             health -= damage
#         ## MESSAGING DURING BATTLE
#             if damage >= 50 and damage <= 70:
#                 print("Shaking hands, huh? Damage is just",damage)
#                 #print("New health is ", health)
#             elif damage >= 130 and damage <= 150:
#                 print("What a hit! Damage is",damage)
#                 #print("New health is ", health)
#             else:
#                 print("Damage is",damage)
#                 #print("New health is ", health)
#
#             if health <= 0:
#                 print("Well, looks like somebody is dead. Farewell, buddy")
#                 break
#             time.sleep(1)
# a = BattleScene()
# a.battle()


class StartScene(object):
    def choose_weather(self):
        weather_dict = {'turn on':'storm','keep off':'heat', 'turn favorite':'cloudy'}
        print("""Friend of yours gave you a weather generator few yers ago. Wanna change the weather?
        Here are 3 options: turn on, keep off, turn favorite""")

        weather_conditions = ''

        while weather_conditions != None:
            user_choice = input("> ")

            if user_choice in weather_dict:
                weather_conditions = weather_dict[user_choice]
                return weather_conditions
                exit(0)
            else:
                print("No such mode, try one more time")
    def weather_choice(weather_conditions):
        pick = weather_conditions
        print(pick)

a = StartScene()
a.choose_weather()
