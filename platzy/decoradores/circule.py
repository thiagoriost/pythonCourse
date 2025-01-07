class Circle:

    def __init__(self, radius:float):
        self._radius = radius
    
    
    @property
    def area(self) -> float:
        return 3.141516 * (self._radius ** 2)
    
    @property
    def radius(self) -> float:
        return self._radius
    
    @radius.setter
    def radius(self, value: float):
        if value < 0 :
            raise ValueError('El radio no puede ser negativo')
    
    
circle = Circle(5)
print(circle.area)

print("---------------------")

circle.radius = 10
print(circle.area)
