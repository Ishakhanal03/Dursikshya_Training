# Methods are the functions defines inside the class.Theyare used to perform operation with the attributes of the objects.
import math
class Circle:
    pi=3.14
    def setRadius(self,radius):
        self.radius=radius
        self.area=self.pi*radius*radius
        
    def getCircumference(self,ra):
        self.r=ra
        self.cfr=2*self.pi*ra


x=Circle()
x.setRadius(10)
print(f"The radius of circle is {x.radius}")
print(f"The area of circle is {x.area}")



#circumference of a circle
x.getCircumference(5)
print(f"The circumference of circle is {x.cfr}")
