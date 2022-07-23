def converttobinary(n):
    if n==0:
        return 0
    else:
        return n%2+10*converttobinary(n//2)
dec=int(input("enter a number:"))
print("the binary of",dec,"is:",converttobinary(dec))

