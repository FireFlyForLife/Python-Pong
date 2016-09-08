from MathF import Vector2d as Vector

def test():
    print("test")

class MoveObject:
    #vars:
    #x, y, vX, vY
    #pos, vel
    
    def load(self, pX, pY):
        self.x = pX
        self.y = pY
        self.vX = 0
        self.vY = 0
        
        self.pos = Vector(self.x, self.y)
        self.vel = Vector()
        
class Ball(MoveObject):
    #vars x, y, r
    def __init__(self, pX, pY, radius=None):
        self.load(pX, pY)
        
        if radius is None:
            self.r = 10
        else:
            self.r = radius
    
    def render(self):
        ellipse(self.x, self.y, self.r, self.r)
    
    def update(self):
        newY = self.y + self.vY
        if newY > height - self.r:
            self.y = height - self.r
        elif newY < 0:
            self.y = 0
        else:
            self.y = newY
        
        newX = self.x + self.vX
        self.x = newX
        #if newX > width - self.r:
        #    self.x = width - self.r
        #elif newX < 0:
        #    self.x = 0
        #else:

class Platform(MoveObject):
    #vars: 
    #x, y, w, h
    #
    def __init__(self, pX, pY, pW=None, pH=None):
        self.load(pX, pY)
        
        if pW is None:
            self.w = 10
        else:
            self.w = pW
            
        if pH is None:
            self.h = 60
        else:
            self.h = pH
        
    def render(self):
        rect(self.x, self.y, self.w, self.h)
    
    def update(self):
        newY = self.y + self.vY
        if newY > height - self.h:
            self.y = height - self.h
        elif newY < 0:
            self.y = 0
        else:
            self.y = newY