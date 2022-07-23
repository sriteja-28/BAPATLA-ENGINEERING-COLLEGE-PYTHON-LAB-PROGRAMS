f1=open('samplefile.txt','r')
t=f1.readlines()
for i in t:
    max=' '
    for j in i.split():
        if(len(j)>len(max)):
            max=j
    print(max)