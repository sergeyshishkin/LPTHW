def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" % cheese_count)
    print("You have %d boxes of crackers!" % boxes_of_crackers)
    print("Man that's enough for a party!")
    print ("Get blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# my example function

def print_lions(lions, cheetah):
    print("So, you see %r lions and %r cheetah. Well done for one day!" % (lions, cheetah))


user_lions = int(input("How many lions to you see?\n> "))
user_cheetah  = int(input("How many cheetah do you see?\n> "))

print_lions(user_lions, user_cheetah)
