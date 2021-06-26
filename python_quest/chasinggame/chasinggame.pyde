from entities import Player
from entities import Enemy
from obstacles import Obstacle


player = Player(400, 300, 25)
enemies = []
obstacles = []

def setup():
    global player, enemies, obstacles
    
    size(800, 600)
    
    ##add enemies
    enemies.append(Enemy(100, 100, 25))
    
    ##add obstacles
    
def draw():
    global player, enemies, obstacles
    
    println((mouseX, mouseY))
    
    background(0)
    
    player.move()
    player.drawObject()
    
    pushMatrix()
    translate(-player.pos.x, -player.pos.y)
    for enemy in enemies:
        enemy.move()
        enemy.drawObject()
    
    for obstacle in obstacles:
        obstacle.move()
        obstacle.drawObject()
    
    popMatrix()
