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

weather_dict = {'turn on':'storm','keep off':'heat', 'turn favorite':'cloudy'}
item_dict = {'storm': 'phone', 'heat': 'cap', 'cloudy':'cigarrete'}

weather_choice = input('Choose weather > ')

## DEFINE WEATHER
if weather_choice in weather_dict:
    item_key = weather_dict[weather_choice]
    print(item_key)
else:
    print("None")

## DEFINE PROPER ITEM
if item_key in item_dict:
    item_val = item_dict[item_key]
    print(item_val)
else:
    print("None")

next_step = input("Choose item > ")

## DEFINE PASS OR FAIL
if next_step == item_val:
    print("Go further")
    print(next_step, item_val)
elif next_step == 'gun':
    print("Start battle")
else:
    print("You fail")
    print(next_step, item_val)

        # print("""Friend of yours gave you a weather generator few yers ago. Wanna change the weather?
        # Here are 3 options: turn on, keep off, turn favorite""")
        #
        # weather_conditions = ''
        #
        # while weather_conditions != None:
        #     user_choice = input("> ")
        #
        #     if user_choice in weather_dict:
        #         weather_conditions = weather_dict[user_choice]
        #         return weather_conditions
        #         exit(0)
        #     else:
        #         print("No such mode, try one more time")
