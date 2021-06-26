
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
        if isinstance(sh, Circle):
            
            if (self.rad/2) + (sh.rad/2) > ((self.posx - sh.posx)**2 + (self.posy - sh.posy)**2)**0.5:
                return True
            elif (self.rad/2) + (sh.rad/2) < ((self.posx - sh.posx)**2 + (self.posy - sh.posy)**2)**0.5:
                return False
        
        
        
        #detects rectangle circle collision
        elif isinstance(sh, Rectangle):    
            def clamp(num, min_value, max_value):
                return max(min(num, max_value), min_value)
            pointrect_x = clamp(self.posx, sh.posx, sh.posx + sh.lenx)
            pointrect_y = clamp(self.posy, sh.posy, sh.posy + sh.leny)
            
            if ((pointrect_x - self.posx)**2 + (pointrect_y - self.posy)**2)**0.5 < self.rad/2:
                return True
                
            elif ((pointrect_x - self.posx)**2 + (pointrect_y - self.posy)**2)**0.5 < self.rad/2:
                return False
        
        
    def update(self, x, y):
        #updates position
        self.posx = x
        self.posy = y
        
        
        



class Rectangle:
    ##a rectanglar hitbox
    ##should always be stationary, update not required
    
    def __init__(self, posx, posy, lenx, leny):
        self.posx = posx
        self.posy = posy
        self.lenx = lenx
        self.leny = leny
        
