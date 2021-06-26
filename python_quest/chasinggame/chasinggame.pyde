from entities import Player


player = Player(200, 200, 25)

def setup():
    size(800, 600)
    
def draw():
    global player
    
    background(0)
    
    player.move()
    player.drawObject()
