from sys import exit
from random import randint
import time


# ### BRANCHING SCENARIO IN START SCENE
# weather_dict = {'turn on':'storm','keep off':'heat', 'turn favorite':'cloudy'}
# item_dict = {'storm': 'phone', 'heat': 'cap', 'cloudy':'cigarrete'}
#
# weather_choice = input('Choose weather mode> ')
#
# ## DEFINE WEATHER
# if weather_choice in weather_dict:
#     item_key = weather_dict[weather_choice]
#     print(item_key)
# else:
#     print("None")
#
# ## DEFINE PROPER ITEM
# if item_key in item_dict:
#     item_val = item_dict[item_key]
#     print(item_val)
# else:
#     print("None")
#
#
# ### DEFINE PASS OR FAIL IN INVADING SCENE
# next_step = input("Choose item > ")
# if next_step == item_val:
#     print("Go further")
#     print(next_step, item_val)
# elif next_step == 'gun':
#     print("Start battle")
# else:
#     print("You fail")
#     print(next_step, item_val)

# ### PROTOTYPE OF HEALTH|DAMAGE MECHANIZM

# a = 100
# b = 60
#
# def fun(a,b):
#     damage = 10
#
#     while a > 0 and b > 0:
#         a -= damage
#         b -= damage
#         print ("loc_a: ", a, "loc_b: ", b)
#         if a <= 0 or b <= 0:
#             break
#
# fun(a,b)
