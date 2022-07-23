from collections import Counter
f1=open('samplefile1.txt','w')
f1.write(input('Enter some text'))
f1.close()
f2=open('samplefile1.txt','r')
t=f2.read().split()
print('The word in the file are:',t)
print('The most common word is:')
print(Counter(t).most_common(1))