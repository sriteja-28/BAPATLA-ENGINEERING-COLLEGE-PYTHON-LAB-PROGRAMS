def python():
    a=list()
    n=int(input("how many numbers you want"))
    for i in range(n):
        b=int(input("enter a number:"))
        a.append(b)
    print("the list is:",a)
    max=a[0]
    min=a[0]
    for i in a:
        if i>max:
            max=i
        if i<min:
            min=i
    print("the maximum numbers is",max)
    print("the minimum number is",min)
python()
