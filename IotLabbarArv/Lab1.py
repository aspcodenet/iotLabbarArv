from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self,width,height):
        self._width = width
        self._height = height

    @abstractmethod
    def Area(self):
        pass


class Circle(Shape):
    def __init__(self,width,height):
        super().__init__(width,height)

    def Area(self):
        #No idea
        return 23561234



class Rectangle(Shape):
    def __init__(self,width,height):
        super().__init__(width,height)
    def Area(self):
        return self._width * self._height


class Triangle(Shape):
    def __init__(self,width,height):
        super().__init__(width,height)

    def Area(self):
         return (self._width * self._height)/2

r1 = Rectangle(3,4)
c = Circle(12,12)
c.Area()
t = Triangle(12,3)
t2 = Triangle(2,4)
r1 = Rectangle(3,4)
s = Shape(1,3)
s.Area()

lista = [c,t,t2,r1]
for s in lista:
    print(s.Area())

