def add(a, b):
    print("ADDING %d + %d" % (a, b))
    return a + b

def subtract(a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b

def multiply(a, b):
    print("MULTIPLYING %d * %d" % (a, b))
    return a * b

def divide(a, b):
    print("DIVIDING %d / %d" % (a, b))
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: %d\nHeight: %d\nWeight: %d\nIQ: %d\n" % (age, height, weight, iq))

# Puzzle piece of code
print("Here is a puzzle")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes: ", what, "Can you do it by hand?")

'''
Answer is - 4391.
Start from the end.
Calculate divide(iq, 2). Result is 50
That goes as a second arg in multyply(weight, divide(iq, 2) )
Take value of weight variable. So calculate multiply(180, 50)
That goes as a second arg in subtract(height, multiply() )
Take value of height variable. So calculate subtract(74, 4500)
That goes as a second arg in add(age, subtract() )
Take value of age variable. So calculate add(35, -4426)
what = -4391
'''

def mult_subtract(a,b,c):
    return (a*b)-c
def add_divide(a,b,c):
    return (a/b)+c

what1 = mult_subtract(2,2,2)
what2 = int(add_divide(10,5,2))
what3 = add_divide(what1, 2, mult_subtract(what2, 4, add_divide(what1, 2, 2)))
print(what1, what2, what3)
