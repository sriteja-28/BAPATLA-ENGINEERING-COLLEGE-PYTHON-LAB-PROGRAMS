class Rectangle:
	length=int(input('Enter length of rectangle:'))
	breadth=int(input('Enter breadth of rectangle:'))
	def area(self):
		area=self.length*self.breadth
		print('The area is:',area)
r=Rectangle()
r.area()