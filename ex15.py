from sys import argv

# script, filename = argv
# txt = open(filename)

print("What file you want to open?")
user_file = input("> ")
txt = open(user_file)

# print("Here's your file %r:" % filename)
print("Here's your file %r:" % user_file)
'''
Above are different options of script beginining
'''
print(txt.read())
txt.close()

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()
