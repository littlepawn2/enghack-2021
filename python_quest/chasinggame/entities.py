from collision_detectors import Circle
from collision_detectors import Rectangle

##file for anything that moves

class Movable:
    
    MAX_SPEED = 25
    
    def __init__(self, posx, posy):
        self.pos = PVector(posx, posy)
        self.vel = PVector(0, 0)
        self.acc = PVector(0, 0)
        
    def move():
        if self.vel.mag() > MAX_SPEED:
            self.vel.setMag(MAX_SPEED)
        
        self.pos.add(vel)
        self.vel.add(acc)

class Player(Movable):
    
    def __init__(self, posx, posy, rad):
        super().__init__(posx, posy)
        self.rad = rad
        self.hitbox = Circle(posx, posy, rad)
        
        



class Enemy(Movable):
    
    def __init__(self, posx, posy):
        pass
