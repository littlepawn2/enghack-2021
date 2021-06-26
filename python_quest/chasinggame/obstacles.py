from collision_detectors import Rectangle

##file for obstacles

class Obstacle(object):
    
    TYPES = ["SOFT", "HARD"]
    #soft - slows player
    #hard - stops player
    
    def __init__(self, posx, posy, lenx, leny, type):
        self.hitbox = Rectangle(posx, posy, lenx, leny)
        self.posx = posx
        self.posy = posy
        self.lenx = lenx
        self.leny = leny
        if not type in Obstacle.TYPES:
            raise ValueError("Unsupported obstacle type")
        self.type = type
        
    def getHitbox(self):
        return self.hitbox
    
    def getType(self):
        return self.type
    
    def drawObject(self):
        if self.type == "HARD":
            fill(255)
        elif self.type == "SOFT":
            fill(100)
        rect(self.posx, self.posy, self.lenx, self.leny)
        
