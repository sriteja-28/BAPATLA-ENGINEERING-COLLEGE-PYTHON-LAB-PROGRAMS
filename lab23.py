a=list()
n=int(input("Enter how many no.s you want"))
for i in range(n):
	b=input("Enter a character:")
	a.append(b)
print(a)
def list_slice(s,step):
	return [s[i::step] for i in range(step)]
c=int(input("Enter the slicing point:"))
print(list_slice(a,c))
