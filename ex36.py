from sys import exit

def start():
     print("""You are an ordinary guy. Nothing special. Just leave your apartment\nand go to do your stuff. Got it? (yes/no)""")

     while True:
         next = input("> ")

         if next == "yes":
             hijacking()
         elif next == "no":
             print("Alright, looks like you're too boring. Bye!")
             exit(0)
         else:
             print("Try again")

def hijacking():
    print("""You went to meet a girl you like. Need to take a bus. So, you enter a bus and\nwhen it start moving, found out you lost your money. What will you do?""")
    print("""
    1. Leave a bus
    2. Simulate that you feel sick
    3. Hijack a bus, threating a knife to a driver""")

    while True:
        next = input("> ")
        if next == "1":
            print("""Well, you'll late for a date. She will be upset. Go home and think about\nhow worth is she for you""")
            exit(0)
        elif next == "2":
            print("""Not bad! Hospital is near the place where you are going to meet her.\nBut be careful with simulation, in case of driver wants to call 911""")
            exit(0) # TODO: : Extend what is next after that choice
        elif next == "3":
            print("""So, what are you going to do then, Tony Montana?\nLooks like you date your girl only in court house""")
            exit(0) # TODO: : Extend what are the options in this case
        elif not next.isdigit():
            print("Don't like numbers? Please, do me a favor, type some")
        else:
            print("Only three options, choose your destiny.")


start()
