from sys import argv
from os.path import exists

script , file_1, file_2 = argv

print "Copying from %r to %r." % (file_1,file_2)

a_1=open(file_1)
b_1=a_1.read()

print "%r has %d long." % (file_1,len(b_1))

# print b_1
# a_1.close()

print "Does the %r exist? %r." % (file_2,exists(file_2))

a_2=open(file_2,'w')
a_2.write(b_1)

# a_2.close()
print ">>>End<<<"

#b_2=open(file_2)
#print b_2.read()
#b_2.close()
