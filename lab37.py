class Circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self,radius):
        print(self.radius**2*3.14,'is area')
    def perimeter(self,radius):
        print('perimeter is:',self.radius*2*3.14)
radius=int(input("Enter radius:"))
c=Circle(radius)
c.area(radius)
c.perimeter(radius)
