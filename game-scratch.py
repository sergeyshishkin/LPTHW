from sys import exit
from random import randint
import time

## HEALTH/DAMAGE MANAGMENT

# health = 800 # updatable health level during battle
# damage = 0 # variable storing damage level
#
# while health >= 0:
#     damage = randint(50, 150)
#     health -= damage
# ## MESSAGING DURING BATTLE
#     if damage >= 50 and damage <= 70:
#         print("Shaking hands, huh? Damage is just",damage)
#         #print("New health is ", health)
#     elif damage >= 130 and damage <= 150:
#         print("What a hit! Damage is",damage)
#         #print("New health is ", health)
#     else:
#         print("Damage is",damage)
#         #print("New health is ", health)
#
#     if health <= 0:
#         print("Well, looks like somebody is dead. Farewell, buddy")
#         break
#     time.sleep(1)

# def make_damage(health_level):
#     damage = randint(30, 50) # GENERATE DAMAGE
#     print("Damage is", damage)
#     health = health_level
#     health -= damage # SUBTRACT DAMAGE FROM HEALTH
#     print("Current health is", health)
#     return damage, health
#
# make_damage(100)

a = 100
b = 60

def fun(a,b):
    loc_a = 0
    loc_b = 0
    damage = 10
    loc_a = a
    loc_b = b

    while loc_a > 0 and loc_b > 0:
        loc_a -= damage
        loc_b -= damage
        print ("loc_a: ", loc_a, "loc_b: ", loc_b)
        if loc_a <= 0 or loc_b <= 0:
            break

fun(a,b)
