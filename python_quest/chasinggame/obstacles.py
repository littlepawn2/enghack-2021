from collision_detectors import Rectangle

##file for obstacles

class Obstacle(object):
    
    TYPES = ["SOFT", "HARD"]
    #soft - slows player
    #hard - stops player
    
    def __init__(self, pic, posx, posy, lenx, leny, type):
        self.hitbox = Rectangle(posx, posy, lenx, leny)
        self.posx = posx
        self.posy = posy
        self.lenx = lenx
        self.leny = leny
        if not type in Obstacle.TYPES:
            raise ValueError("Unsupported obstacle type")
        self.type = type
        
        self.pic = pic
        self.x = int(posx)
        self.y = int(posy)
        self.pic_lenx = int(self.lenx)
        self.pic_leny = int(self.leny)
        
    def getHitbox(self):
        return self.hitbox
    
    def getType(self):
        return self.type
    
    def drawObject(self):
        if self.type == "HARD":
            fill(255, 255, 255, 100)
            copy(self.pic, 100, 100, 700, 600, self.x, self.y, self.pic_lenx, self.pic_leny)
            #rect(self.posx, self.posy, self.lenx, self.leny)
            
        elif self.type == "SOFT":
            fill(0)
            #rect(self.posx, self.posy, self.lenx, self.leny)
            copy(self.pic, 0, 0, 1000, 1000, self.x-40, self.y-30, self.pic_lenx *4 + 10, self.pic_leny *5 + 20)
        
