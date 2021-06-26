from collision_detectors import Rectangle

##file for obstacles

class Obstacle():
    
    def __init__(self, posx, posy, lenx, leny):
        self.hitbox = Rectangle(posx, posy, lenx, leny)
        

class SoftObstacle:
    #slows down player while within bounds
    
    def __init__(self):
        pass
        
    def getHitbox(self):
        return self.hitbox
        
        
        
        
class HardObstacle:
    #stops player when colliding
    
    def __init__(self):
        pass
        
    def getHitbox(self):
        return self.hitbox
