def factorial(n):
	if n==1:
		return 1
	else:
		return factorial(n-1)*n
c=int(input("Enter a number"))
if c<0:
	print("Factorial is not possible for negative numbers")
elif c==0:
	print("factorial is 1")
else:
	print("factorial of",c,"is",factorial(c))