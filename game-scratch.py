from sys import exit
from random import randint
import time

## WEATHER CONDITIONS SETTER, THAT DEFINES PROPER ITEM IN INVADING SCENE
# weather_dict = {'turn on':'storm','keep off':'heat', 'turn favorite':'cloudy'}
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
#         print(weather_conditions)
#         exit(0)
#     else:
#         print("No such mode, try one more time")


## HEALTH/DAMAGE MANAGMENT

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
    time.sleep(1)

## INVADING A BASE

# # If the weather is heat
# heat = """Here is a base. Guard stands at the door. It's too hot. You understand
#  that you can trick guard, to slip to the base.
# As remember, you have 'items'. What you can offer, to distract his attention?"""
#
#
# #if the weather is stormy
# storm = """Here is a base. Guard stands at the door. It's very windy, almost
# stormy. You understand that you can trick guard, to slip to the base.
# As remember, you have 'items'. What you can offer, to distract his attention?"""
#
#
# # if te weather is Cloudy
# cloudy = """Here is a base. Guard stands at the door. It's cloudy, and
# melancholic weather. You understand that you can trick guard, to slip to the base.
# As remember, you have 'items'. What you can offer, to distract his attention?"""
#
#
# items = ['gun', 'cigarettes', 'phone', 'hat']
# weather_conditions = 'cloudy'
#
#
# item_choice = input(">_> ")
# ## # IDEA: REFACTOR THIS BY STORING OPTIONS IN DICTIONARY
# if item_choice == 'gun':
#     print('start battle')
# elif weather_conditions == 'heat' and item_choice != 'hat':
#     print("You fail")
# elif weather_conditions == 'heat' and item_choice == 'hat':
#     print("You pass")
# elif weather_conditions == 'storm' and item_choice != 'phone':
#     print("You fail")
# elif weather_conditions == 'storm' and item_choice == 'phone':
#     print("You pass")
# elif weather_conditions == 'cloudy' and item_choice != 'cigarettes':
#     print("You fail")
# elif weather_conditions == 'cloudy' and item_choice == 'cigarettes':
#     print("You pass")
# else:
#     print("Hold on! You have only 4 items. Try one more time")
