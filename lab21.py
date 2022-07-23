import random
f1=open('samplefile.txt','r')
t=f1.readlines()
print(random.choice(t))
