from collision_detectors import Circle

##file for anything that moves

class Movable:
    
    MAX_SPEED = 25
    
    def __init__(self, posx, posy):
        self.pos = PVector(posx, posy)
        self.vel = PVector(0, 0)
        self.acc = PVector(0, 0)
        self.hitbox = None #movable will always have a hitbox
        
    def move():
        if self.vel.mag() > MAX_SPEED:
            self.vel.setMag(MAX_SPEED)
        
        self.pos.add(vel)
        self.vel.add(acc)
        
        self.hitbox.update(pos.x, pos.y)

class Player(Movable):
    
    def __init__(self, posx, posy, rad):
        super().__init__(posx, posy)
        self.rad = rad
        self.hitbox = Circle(posx, posy, rad)
        
    def getHitbox(self):
        return self.hitbox
        
    def move():
        #accelerates player towards mouse
        super().move()
        relativeMousePos = PVector(mouseX-self.pos.x, mouseY-self.pos.y)
        acc = relativeMousePos
        
    def collide(sh):
        #decides what to do after a collision
        if self.hitbox.detect(sh.hitbox):
            if isinstance(sh, Enemy):
                pass
            elif isinstance(sh, SoftObstacle):
                pass
            elif isinstance(sh, HardObstacle):
                pass
                
    def drawObject():
        fill(255, 0, 0)
        circle(self.pos.x, self.pos.y, self.rad)
        



class Enemy(Movable):
    
    def __init__(self, posx, posy, rad):
        super().__init__(posx, posy)
        self.hitbox = Circle(posx, posy, rad)
        
    def getHitbox(self):
        return self.hitbox
    
    def move():
        #some kind of "ai" needs to go in here
        pass
        
    def collide(sh):
        #decides what to do after a collision
        if self.hitbox.detect(sh.hitbox):
            if isinstance(sh, SoftObstacle):
                pass
            elif isinstance(sh, HardObstacle):
                pass
                
    def drawObject():
        fill(0, 0, 255)
        circle(self.pos.x, self.pos.y, self.rad)
