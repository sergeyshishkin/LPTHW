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

### COMPLETED HEALTH|DAMAGE MECHANISM
# hero_health = 200
# enemy_health = 200
#
# def fun(hero_health, enemy_health):
#
#     while hero_health > 0 and enemy_health > 0:
#
#         # FUNCTION THAT GENERATES DAMAGE, SHOW TEXT ABOUT DAMAGE AND WHO DID THE DAMAGE
#         def generate_damage(user):
#             damage = randint(50, 150)
#             if damage >= 50 and damage <= 70:
#                 print(user, "strikes poorly and hit only",damage,"damage")
#             elif damage >= 130 and damage <= 150:
#                 print(user, "strikes a great hit! Damage is",damage)
#             else:
#                 print(user, "strikes ordinary",damage,"damage")
#             return damage
#
#         # CALLING generate_damage FUNCTION
#         damage = generate_damage("Enemy")
#
#         # HERE IS CALCULATING HEALTH AND FATAL LEVEL FOR HERO
#         hero_health -= damage
#         print ("New hero health is: ", hero_health) #IN PRODUCTION, MOVE THIS LINE AFTER "ELSE: PASS"
#         if hero_health <= 0:
#             print("Well, looks like hero is dead. Farewell, buddy")
#             break
#         else:
#             pass
#
#         time.sleep(1) #DELAY TO MAKE GAME NOT SO RAPID
#
#         # CALLING generate_damage FUNCTION
#         damage = generate_damage("Hero")
#
#         # HERE IS CALCULATING HEALTH AND FATAL LEVEL FOR ENEMY
#         enemy_health -= damage
#         print ("New enemy health is: ", enemy_health) #IN PRODUCTION, MOVE THIS LINE AFTER "ELSE: PASS"
#         if enemy_health <= 0:
#             print("Enemy is dead. Hero goes further")
#             break
#         else:
#             pass
#
#         time.sleep(1) #DELAY TO MAKE GAME NOT SO RAPID
#
# fun(hero_health, enemy_health)


### EXTENDED HEALTH\DAMAGE MECHANISM WITH RANDOM ORDER OF WHO MAKE DAMAGE
# SET VARIABLES OF INITIAL HEALTH

hero_health = 300
enemy_health = 300


while hero_health > 0 and enemy_health > 0:

    # FUNCTION THAT RANDOMLY DEFINE WHO MAKE DAMAGE, RANDOMLY DEFINE DAMAGE VALUE. PASS damage VALUE AND user TO health_calc()
    def generate_damage():
        b = randint(1,2)
        if b == 1:
            print("Enemy strikes")
            damage = randint(50, 150)
            print("Enemy make",damage, "damage")
            health_calc(damage, "Enemy")

        else:
            print("Hero strikes")
            damage = randint(50, 150)
            print("Hero make",damage,"damage")
            health_calc(damage, "Hero")

    # CALCULATING HEALTH AFTER GETTING DAMAGE, AND FATAL LEVEL FOR user
    def health_calc(damage, user):

        global hero_health
        global enemy_health

        if user == 'Enemy':
            print("Enemy kick hero")
            print("current hero health is", hero_health)
            hero_health -= damage
            print("New Hero health",hero_health)

        else:
            print("Hero kick enemy")
            print("Current enemy health is", enemy_health)
            enemy_health -= damage
            print("New Enemy health",enemy_health)

        if hero_health <= 0:
            print("Hero is dead")
        elif enemy_health <= 0:
            print("Enemy is dead")
        else:
            generate_damage()

    generate_damage()
