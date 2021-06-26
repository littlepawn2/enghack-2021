
##different shaped hitboxes

class Circle:
    ##a circular hitbox
    
    def __init__(self, posx, posy, rad):
        self.posx = posx
        self.posy = posy
        self.rad = rad
        
    def detect(self, sh):
        #returns true if colliding with shape, false if not
        
        #detects circle circle collision
        if (self.rad/2) + (Enemy.rad/2) > ((self.posx - Enemy.posx)**2 + (self.posy - Enemy.posy)**2)**0.5:
            self.sh = True
        elif (self.rad/2) + (Enemy.rad/2) < ((self.posx - Enemy.posx)**2 + (self.posy - Enemy.posy)**2)**0.5:
            self.sh = False
        
        
        
        #detects rectangle circle collision    
        def clamp(num, min_value, max_value):
            return max(min(num, max_value), min_value)
        pointrect_x = clamp(self.posx, Rectangle.posx, Rectangle.posx + Rectangle.lenx)
        pointrect_y = clamp(self.posy, Rectangle.posy, Rectangle.posy + Rectangle.leny)
        
        if ((pointrect_x - self.posx)**2 + (pointrect_y - self.posy)**2)**0.5 < self.rad/2:
            self.sh = True
        
        
            #push back 5 px
            if pointrect_x < self.posx:
                self.posx -= 5
            if pointrect_x > self.posx:
                self.posx += 5
            if pointrect_y < self.posy:
                self.posy -=5
            if pointrect_y > self.posy:
                self.posy += 5
            
        elif ((pointrect_x - self.posx)**2 + (pointrect_y - self.posy)**2)**0.5 < self.rad/2:
            self.sh = False
        
        
    def update(self, x, y):
        #updates position
        self.posx = x
        self.posy = y
        
        
        



class Rectangle:
    ##a rectanglar hitbox
    ##should always be stationary, update not required
    
    def __init__(self, posx, posy, lenx, leny):
        pass
        
