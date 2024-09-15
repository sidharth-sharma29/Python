'''11. Write a Python class named Circle constructed from a radius and two methods that will
compute the area and the perimeter of a circle.'''
pi=3.14
class circle:
    def __init__(self):
        a=int(input("Enter radius of circle: "))
        self.r=a
    def area(self):
        ab=pi*self.r*self.r
        print(f"Area of circle: {ab}")
    def parameter(self):
        para=2*pi*self.r
        print(f"Parameter of circle: {para}")

a=circle()
a.area()
a.parameter()