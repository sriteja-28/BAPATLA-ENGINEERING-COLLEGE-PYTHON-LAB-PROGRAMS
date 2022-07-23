def converttobinary(n):
	if n==0:
		return 0
	else:
		return n%2+10*converttobinary(n//2)
dec=int(input("Enter a decimal number:"))
print("binary of",dec,"is",converttobinary(dec))


