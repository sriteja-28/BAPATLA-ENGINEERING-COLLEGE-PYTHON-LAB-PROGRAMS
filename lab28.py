l=[]
n=int(input('Enter size of tuple:'))
for i in range(n):
	c=input('Enter element:')
	l.append(c)
t=tuple(l)
print('The tuple is:',t)
r=t[::-1]
print('The tuple after reversing is:',r)
