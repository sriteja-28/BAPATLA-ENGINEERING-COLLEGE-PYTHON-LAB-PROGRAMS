a='AEIOUaeiou'
b=input("Enter any string:")
count=0
count=[i for i in b if i in a]
print(count)
c=len(count)
print("The count of vowels:",c)
print("The percentage of vowels is ",c/len(b)*100)