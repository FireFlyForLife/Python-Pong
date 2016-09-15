from MathF import Vector2d as Vector
from RandomUtils import deltaTime as dTime

def test():
    print("test")

class MoveObject:
    #vars:
    #x, y, vX, vY
    #pos, vel
    
    def load(self, pX, pY):
        #self.x = pX
        #self.y = pY
        #self.vX = 0
        #self.vY = 0
        
        self.pos = Vector(pX, pY)
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
        ellipse(self.pos.x, self.pos.y, self.r, self.r)
    
    def update(self):
        newY = self.pos.y + self.vel.y
        if newY + self.r / 2 > height:
            self.pos.y = height - self.r / 2
        elif newY - self.r / 2 <= 0:
            self.pos.y = 0 + self.r / 2
        else:
            self.pos.y = newY
        
        newX = self.pos.x + self.vel.x
        self.pos.x = newX
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
        rect(self.pos.x, self.pos.y, self.w, self.h)
    
    def update(self):
        newY = self.pos.y + self.vel.y
        if newY > height - self.h:
            self.pos.y = height - self.h
        elif newY < 0:
            self.pos.y = 0
        else:
            self.pos.y = newY