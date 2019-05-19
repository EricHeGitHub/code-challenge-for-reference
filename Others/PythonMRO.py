class Square:
    def __init__(self, edge):
        self.edge = edge
    def area(self):
        print("area in Square is called. The area is {0}".format(self.edge ** 2))


class Triangle:
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def area(self):
        print("area in Triangle is called. The area is {0}".format(0.5 * self.height * self.base))

    def __repr__(self):
        return "repr is called"

    def __str__(self):
        return "str is called"

class MyShape(Square, Triangle):
    def __init__(self, edge, height, base):
        Square.__init__(self,edge)
        Triangle.__init__(self, height, base)

    def area(self):
        Square.area(self) #must pass self for parent class
        Triangle.area(self)
        MyShape.staticMethod() #not need to pass self to parent class

    def staticMethod():
        print("Static Method is called")


ms = MyShape(1,2,2)
ms.area()
print(ms)
