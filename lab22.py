a=list()
n=int(input("Enter how many no.s you want"))
for i in range(n):
	b=input("Enter a character")
	a.append(b)
print(a)
n1=int(input("Enter a number"))
print("output is:")
l=['{}{}'.format(x,y+1) for y in range(n1) for x in a]
print(l)