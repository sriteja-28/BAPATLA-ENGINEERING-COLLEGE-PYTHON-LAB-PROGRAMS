f=open("tej.txt",'r')
t=f.readlines()
for i in t:
    max=' '
    for j in i.split():
        if(len(j)>len(max)):
            max=j
    print(max)
