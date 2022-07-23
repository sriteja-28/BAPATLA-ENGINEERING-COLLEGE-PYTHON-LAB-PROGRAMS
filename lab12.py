a=input("Enter body to insert in html code:")
b=a.upper()
c=input("Enter head:")
def html(b,c):
	print("<{}>{}</{}>".format(c,b,c))
html(b,c)
