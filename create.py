f1 = open("sequence.txt","r")
f2 = open("expect.txt", "w")
s = f1.readline()
while s:
    f2.write(s.split()[1]+"\n")
    s = f1.readline()
f1.close()
f2.close()
