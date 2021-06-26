from collision_detectors import Circle

##file for anything that moves

class Movable(object):
    
    MAX_SPEED = 10
    
    def __init__(self, posx, posy):
        self.pos = PVector(posx, posy)
        self.vel = PVector(0, 0)
        self.acc = PVector(0, 0)
        self.hitbox = None #movable will always have a hitbox
        
    def move(self):
        if self.vel.mag() > Movable.MAX_SPEED:
            self.vel.setMag(Movable.MAX_SPEED)
        
        self.pos.add(self.vel)
        self.vel.add(self.acc)
        
        self.hitbox.update(self.pos.x, self.pos.y)

class Player(Movable):
    
    def __init__(self, posx, posy, rad):
        super(Player, self).__init__(posx, posy)
        self.rad = rad
        self.hitbox = Circle(posx, posy, rad)
        
    def getHitbox(self):
        return self.hitbox
        
    def move(self):
        #accelerates player towards mouse
        super(Player, self).move()
        relativeMousePos = PVector(mouseX-self.pos.x, mouseY-self.pos.y).div(100)
        self.acc = relativeMousePos
        
    def collide(self, sh):
        #decides what to do after a collision
        if self.hitbox.detect(sh.hitbox):
            if isinstance(sh, Enemy):
                pass
            elif isinstance(sh, SoftObstacle):
                pass
            elif isinstance(sh, HardObstacle):
                pass
                
    def drawObject(self):
        fill(255, 0, 0)
        circle(self.pos.x, self.pos.y, self.rad)
        



class Enemy(Movable):
    
    def __init__(self, posx, posy, rad):
        super().__init__(posx, posy)
        self.hitbox = Circle(posx, posy, rad)
        
    def getHitbox(self):
        return self.hitbox
    
    def move(self):
        #some kind of "ai" needs to go in here
        super(Enemy, self).move()
        pass
        
    def collide(self, sh):
        #decides what to do after a collision
        if self.hitbox.detect(sh.hitbox):
            if isinstance(sh, SoftObstacle):
                pass
            elif isinstance(sh, HardObstacle):
                pass
                
    def drawObject(self):
        fill(0, 0, 255)
        circle(self.pos.x, self.pos.y, self.rad)
