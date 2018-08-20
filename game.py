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
#     loc_a = 0
#     loc_b = 0
#     damage = 10
#     loc_a = a
#     loc_b = b
#
#     while loc_a > 0 and loc_b > 0:
#         loc_a -= damage
#         loc_b -= damage
#         print ("loc_a: ", loc_a, "loc_b: ", loc_b)
#         if loc_a <= 0 or loc_b <= 0:
#             break
#
# fun(a,b)
