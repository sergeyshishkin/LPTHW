from sys import exit
from random import randint
import time

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


# ### EXTENDED PROTOTYPE OF HEALTH|DAMAGE MECHANIZM
hero_health = 500
enemy_health = 500

def fun(hero_health, enemy_health):

## # TODO: WRAP DAMAGE VARIATOR IN FUNCTION

    while hero_health > 0 and enemy_health > 0:
        # HERE IS CALCULATING DAMAGE FOR HERO
        damage = randint(50, 150)
        if damage >= 50 and damage <= 70:
            print("Shaking hands, huh? Damage is just",damage)

        elif damage >= 130 and damage <= 150:
            print("What a hit! Damage is",damage)

        else:
            print("Damage is",damage)
        # HERE IS CALCULATING HEALTH AND FATAL LEVEL FOR HERO
        hero_health -= damage
        if hero_health <= 0:
            print("Well, looks like hero is dead. Farewell, buddy")
            break
        else:
            pass
        print ("New hero health is: ", hero_health)

        time.sleep(1) #DELAY TO MAKE GAME MORE USER FRIENDLY

        # HERE IS CALCULATING DAMAGE FOR ENEMY
        damage = randint(50, 150)
        if damage >= 50 and damage <= 70:
            print("Shaking hands, huh? Damage is just",damage)

        elif damage >= 130 and damage <= 150:
            print("What a hit! Damage is",damage)

        else:
            print("Damage is",damage)
        # HERE IS CALCULATING HEALTH AND FATAL LEVEL FOR ENEMY
        enemy_health -= damage
        if enemy_health <= 0:
            print("Enemy is dead. Hero goes further")
            break
        else:
            pass
        print ("New enemy health is: ", enemy_health)

        time.sleep(1) #DELAY TO MAKE GAME MORE USER FRIENDLY


fun(hero_health, enemy_health)
