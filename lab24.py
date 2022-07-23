from collections import Counter
a=list()
b=list()
n=int(input("Enter size of 1st list:"))
for i in range(n):
	c=input("Enter a string")
	a.append(c)
n1=int(input("Enter size of 2nd list:"))
for i in range(n1):
	c=input("Enter a string:")
	b.append(c)
Counter1=Counter(a)
print(Counter1)
Counter2=Counter(b)
print(Counter2)
print("The diff between 1st and 2nd lists is:",list(Counter1-Counter2))
print("The diff between 2nd and 1st lists is:",list(Counter2-Counter1))
