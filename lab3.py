from collections import counter
f1=open("file.txt",'w')
f1.write(input("enter some text:"))
f1.close()
f2=open("file1.txt","r")
t=f2.read().split()
print("the words in the file are:",t)
print("the most common words is:")
print(counter(t).most_common(t))
