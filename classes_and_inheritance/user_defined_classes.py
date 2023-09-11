"""Every class should have a method with the special name __init__. This initializer method, often referred to as the
constructor, is automatically called whenever a new instance of Point is created. It gives the programmer the
opportunity to set up the attributes required within the new instance by giving them their initial state values. The
self parameter (you could choose any other name, but nobody ever does!) is automatically set to reference the newly
created object that needs to be initialized."""


class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self):
        """ Create a new point at the origin """
        self.x = 0
        self.y = 0

    def getX(self):
        return self.x


# Methods are like functions, except they belong to a class


point1 = Point()  # create instance
point2 = Point()  # create instance

point1.x = 5  # instance variable
point2.x = 10  # instance variable

print(point1.getX())
print(point2.getX())

p = Point()         # Instantiate an object of type Point
q = Point()         # and make a second point
print(p)  # <__main__.Point object at 0x1005265d0>
print(q)

print(p is q)  # False
