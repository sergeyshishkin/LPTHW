from sys import argv
from os.path import exists

''' It is possible to make one line '''
#script, from_file, to_file = argv; indata = open(from_file).read();out_file = open(to_file, 'w');out_file.write(indata);out_file.close()

script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file))

indata = open(from_file).read()
print("File contains next: \n" + indata)
# in_file = open(from_file)
# indata = in_file.read()

print("The input file is %d bytes long" % len(indata))

print("Does the output file exist? %r" % exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
#in_file.close()
