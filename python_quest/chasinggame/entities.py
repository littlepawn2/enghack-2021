from collision_detectors import Circle

##file for anything that moves

class Movable(object):
    
    def __init__(self, posx, posy):
        self.pos = PVector(posx, posy)
        self.vel = PVector(0, 0)
        self.acc = PVector(0, 0)
        self.hitbox = None #movable will always have a hitbox

        
    def move(self, max_speed):
        if self.vel.mag() > max_speed:
            self.vel.setMag(max_speed)
        
        self.pos.add(self.vel)
        self.vel.add(self.acc)
        
        self.hitbox.update(self.pos.x, self.pos.y)

class Player(Movable):
    
    CONTROL_DAMPER = 100
    
    def __init__(self, posx, posy, rad, pic):
        super(Player, self).__init__(posx, posy)
        self.rad = rad
        self.hitbox = Circle(posx, posy, rad)
        self.pic = pic
        self.x = posx
        self.y = posy
        
    def getHitbox(self):
        return self.hitbox
        
    def move(self):
        #accelerates player towards mouse
        super(Player, self).move(10)
        relativeMousePos = PVector(mouseX-400, mouseY-300).div(Player.CONTROL_DAMPER)
        self.acc = relativeMousePos
        
    def collide(self, sh):
        #decides what to do after a collision
        if self.hitbox.detect(sh.hitbox):
            if isinstance(sh, Enemy):
                text("you lose", 100, 100)
                noLoop()
            elif isinstance(sh, Obstacle):
                if sh.getType == "SOFT":
                    self.vel.setMag(3)
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
        copy(self.pic, 0, 0, 500, 500, self.x - 15, self.y -15, self.rad +10, self.rad +10)
        
        



class Enemy(Movable):
    
    def __init__(self, posx, posy, rad, lookahead=0):
        super(Enemy, self).__init__(posx, posy)
        self.rad = rad
        self.hitbox = Circle(posx, posy, rad)
        self.lookAheadFactor = lookahead
        
    def getHitbox(self):
        return self.hitbox
    
    def move(self, player):
        super(Enemy, self).move(8)
        
        targetpos = player.pos.copy()
        targetpos.add(PVector.mult(player.vel, self.lookAheadFactor))
        
        self.acc = PVector.sub(targetpos, self.pos)
        
    
        
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
