from sys import argv

script, user_name, action = argv
prompt = '> '

print ("Hi %s, I'm the %s script." % (user_name, script))
print ("I'd like to ask you a few questions.")
print ("Do you like me %s?" % user_name)
likes = input(prompt)

print ("Where do you live %s?" % user_name)
lives = input(prompt)

print ("What kind of computer do you have?")
computer = input(prompt)

print("%s is NOT your favourite action?" % action)
act = input(prompt)

print("""
Alright, so you said %s about liking me.
You live in %s. Not sure where that is.
And you have a %s computer. Nice.
And you don't like %s.
""" % (likes, lives, computer, action))
