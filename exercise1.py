import math

class Circle:
    def __init__(self, radius):
        self.radius = float ( radius )
        print ("A circle with radius :", self.radius)

    def area(self):
        try :
            A1 = math.pi*(self.radius**2)
            print ("The area of the circle is :", A1)
            return A1;
        except:
            print("Can`t calculate the area")

    def perimeter(self):
        try :
            P1 = 2*math.pi*self.radius
            print ("The perimeter of the circle is :", P1)
            return 2*self.radius*3.14
        except:
            print("Can`t calculate the perimeter")

    
try:
    x = input("Enter your circle radius:")
    p1 = Circle(x)
    p1.area()
    p1.perimeter()
except ValueError:
    print("No valid integer! Please try again ...")

