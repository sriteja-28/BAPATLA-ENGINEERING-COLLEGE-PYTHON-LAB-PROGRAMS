def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input("enter a numbert"))
if n<0:
    print("factorial is not possible for negative numbers")
elif n==0:
    print("factorial of 0 is:1")
else:
    print("factorial of",n,"is:",factorial(n))
