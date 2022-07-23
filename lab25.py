from collections import Counter
a=list()
b=list()
n=int(input('Enter size of 1st list:'))
for i in range(n):
	c=input("Enter string:")
	a.append(c)
print("The 1st list is:",a)
n1=int(input('Enter size of 2nd list:'))
for i in range(n1):
	c=input('Enter string:')
	b.append(c)
print('The 2nd list is:',b)
a[-1:]=b
print('The resultant list is:',a)