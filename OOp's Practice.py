# class employee:
#     def function(self):
#         print("Hey!!!!! i am Sheikh.....")
    
# class dept(employee):
#     pass

# emp=employee()
# print(emp.function())

# dept=dept()
# print(dept.function())
class Shape :
    def set_color(self, color):
        self.color = color
        
    def calculate_area(self):
        pass
        
    def color_the_shape(self):
        color_price = {"red" : 10, "blue" : 15, "green" : 5}
        return self.calculate_area() * color_price[self.color]
    
class Circle(Shape) :
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
        
    def calculate_area(self):
        return Circle.pi * self.radius
    
c = Circle(5)
# Accessing set_color from parent class, because of inheritance
c.set_color("red")
print("Circle with radius =",c.radius ,"when colored", c.color,"costs $",c.color_the_shape())

class Rectangle(Shape) :
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth
        
     # Overriding user defined method   
    def calculate_area(self):
        return self.length * self.breadth
    
    # Overriding python default method
    def __str__(self):
        return "area of rectangle = " + str(self.calculate_area())
    
    
r = Rectangle(5, 10)
r.set_color("blue")
print("Rectangle with length =",r.length ," and breadth = ",r.breadth ,"when colored", r.color,"costs $",r.color_the_shape())