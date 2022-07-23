f1=open("tej.txt",'r')
t1=f1.readlines()
print("the content in the file1 is:",t1)
f2=open("file1.txt",'r')
t2=f2.readlines()
print("the content in the file2 is:",t2)
print("combining the each line:")
for i,j in zip(t1,t2):
    print((i+j).replace("\n"," "))
