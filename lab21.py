import random
f=open("file1.txt",'r')
t=f.readlines()
print(random.choice(t))
