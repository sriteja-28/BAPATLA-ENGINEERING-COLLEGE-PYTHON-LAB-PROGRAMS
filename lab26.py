from collections import Counter
l=[]
n=int(input('Enter size of tuple:'))
for i in range(n):
	c=input('Enter element')
	l.append(c)
t=tuple(l)
c=Counter(t)
print('The tuple is:',t)
t1=tuple(dict.fromkeys(t))
c1=Counter(t1)
print('The repeated elements in tuple are:',tuple(dict.fromkeys(c-c1)))

