__author__ = 'keleigong'

file=open('/Users/keleigong/Dropbox/Python/Project-SCRC/keyword list.txt')

file2 = open('keyword list2.txt','w')
#line = file.readline()
list = []
for line in file:
    list.append("'"+line+"'")
    file2.write("'"+line[0:-1]+"',\n")
    #line = file.readline()

# file2.write(list)
file2.close()