class Vector2d:
    x = 0.0
    y = 0.0
    def __init__(self, x = None, y = None):
        if x is not None: self.x = x
        if y is not None: self.y = y
        
    def magnitude(self):
        mag2 = self.x ** 2 + self.y ** 2
        return sqrt(abs(mag2))
    
    def normalize_(self):
        magn = self.magnitude()
        return self.__truediv__(magn)
    
    def deg(self, newDeg = None):
        if newDeg is None:
            return degrees(atan2(self.y, self.x))
        else:
            self.rad(radians(newDeg))
    
    def rad(self, newRad = None):
        if newRad is None:
            return atan2(self.y, self.x)
        mg = self.magnitude()
        self.x = cos(newRad) * mg
        self.y = sin(newRad) * mg
    
    def __add__(self, other):
        if isinstance(other, Vector2d):
            return Vector2d(self.x + other.x, self.y + other.y)
        raise ValueType("'other' needs to be a Vector2d")
    
    def __sub__(self, other):
        if isinstance(other, Vector2d):
            return Vector2d(self.x - other.x, self.y - other.y)
        raise ValueType("'other' needs to be a Vector2d")
        
    def __mul__(self, other):
        if isinstance(other, Vector2d):
            return Vector2d(self.x * other.x, self.y * other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector2d(self.x * other, self.y * other)
        raise Exception("'other' needs to be a Vector2d or int or float, not " + str(type(other)))
    
    def __div__(self, other):
        if isinstance(other, Vector2d):
            return Vector2d(self.x / other.x, self.y / other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector2d(self.x / other, self.y / other)
        raise ValueType("'other' needs to be a Vector2d or int or float")
    
    def __truediv__(self, other):
        if isinstance(other, Vector2d):
            return Vector2d(self.x / other.x, self.y / other.y)
        elif isinstance(other, int) or isinstance(other, float):
            return Vector2d(self.x / other, self.y / other)
        raise ValueType("'other' needs to be a Vector2d or int or float")
    
    def __str__(self):
        return "({0},{1})".format(self.x, self.y)