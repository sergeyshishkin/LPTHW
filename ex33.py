'''
WORK THROUGH AGAIN!!!
'''


def iterwhile(base,iter):
    i = 0
    numbers = []
    while i < base:
        print("At the top i is %d" % i)
        numbers.append(i)
        i+=iter
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

    print("The numbers: ")

    for num in numbers:
        print(num)


iterwhile(6,1)

i = 0
numbers=[]
for i in range(6):
    print("At the top i is %d" % i)
    numbers.append(i)
    i+=1
    print("Numbers now: ", numbers)
    print("At the bottom i is %d" % i)

print("The numbers: ")

for num in numbers:
    print(num)
