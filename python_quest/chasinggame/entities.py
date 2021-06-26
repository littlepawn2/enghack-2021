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
    
    CONTROL_DAMPER = 100
    
    def __init__(self, posx, posy, rad):
        super(Player, self).__init__(posx, posy)
        self.rad = rad
        self.hitbox = Circle(posx, posy, rad)
        self.pic =  loadImage ("kirbypuffy.png")
        
    def getHitbox(self):
        return self.hitbox
        
    def move(self):
        #accelerates player towards mouse
        super(Player, self).move()
        relativeMousePos = PVector(mouseX-400, mouseY-300).div(Player.CONTROL_DAMPER)
        self.acc = relativeMousePos
        
    def collide(self, sh):
        #decides what to do after a collision
        if self.hitbox.detect(sh.hitbox):
            if isinstance(sh, Enemy):
                pass
            elif isinstance(sh, Obstacle):
                if sh.getType == "SOFT":
                    pass
                elif sh.getType == "HARD":
                    pass
                    
    def boundaryCollision(self):
        if self.pos.x < 0:
            self.pos.x = 0
        elif self.pos.x > 2000:
            self.pos.x = 2000
            
        if self.pos.y < 0:
            self.pos.y = 0
        elif self.pos.y > 2000:
            self.pos.y = 2000
                
    def drawObject(self):
        fill(255, 0, 0)
        circle(400, 300, self.rad)
        copy(self.pic, 0, 0, 500, 500, int(self.pos.x), int(self.pos.y), self.rad, self.rad)
        
        



class Enemy(Movable):
    
    def __init__(self, posx, posy, rad):
        super(Enemy, self).__init__(posx, posy)
        self.rad = rad
        self.hitbox = Circle(posx, posy, rad)
        
    def getHitbox(self):
        return self.hitbox
    
    def move(self):
        super(Enemy, self).move()
        pass #some kind of "ai" needs to go in here
        
    def collide(self, sh):
        #decides what to do after a collision
        if self.hitbox.detect(sh.hitbox):
            if isinstance(sh, Obstacle):
                if sh.getType == "SOFT":
                    pass
                elif sh.getType == "HARD":
                    pass
                    
    def boundaryCollision(self):
        if self.pos.x < 0:
            self.pos.x = 0
        elif self.pos.x > 2000:
            self.pos.x = 2000
            
        if self.pos.y < 0:
            self.pos.y = 0
        elif self.pos.y > 2000:
            self.pos.y = 2000
                
    def drawObject(self):
        fill(0, 0, 255)
        circle(self.pos.x, self.pos.y, self.rad)
