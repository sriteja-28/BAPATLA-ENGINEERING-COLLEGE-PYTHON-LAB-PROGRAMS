def python():
	a=list()
	n=int(input("How any nubers do you want:"))
	for i in range(n):
		b=int(input("Enter a number:"))
		a.append(b)
	print("The list is:",a)
	max=a[0]
	min=a[0]
	for i in a:
		if i>max:
			max=i
		if i<min:
			min=i
	print("The max no. is:",max)
	print("The min no. is:",min)
python()