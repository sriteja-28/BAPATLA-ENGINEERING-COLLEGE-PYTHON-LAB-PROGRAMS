l=[]
n=int(input('Enter size of list:'))
for i in range(n):
	c=input('Enter element:')
	l.append(c)
print('The list with duplicates is:',l)
t1=tuple(dict.fromkeys(l))
print('The tuple without duplicates is:',t1)
