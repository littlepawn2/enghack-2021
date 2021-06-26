from entities import Player
from entities import Enemy
from obstacles import Obstacle


player = Player(400, 300, 25)
enemies = []
obstacles = []

def setup():
    global player, enemies, obstacles
    
    size(800, 600)
    stroke(255)
    
    ##add enemies
    enemies.append(Enemy(100, 100, 25))
    
    ##add obstacles
    for i in range(10):
        obstacles.append(Obstacle(random(100, 1700), random(100, 1700), random(50, 200), random(50, 200), "SOFT"))
    for i in range(5):
        obstacles.append(Obstacle(random(100, 1700), random(100, 1700), random(50, 200), random(50, 200), "HARD"))
    
def draw():
    global player, enemies, obstacles
    
    background(0)
    
    player.move()
    player.boundaryCollision()
    player.drawObject()
    
    print(player.pos)
    
    pushMatrix()
    translate(-player.pos.x+400, -player.pos.y+300)
    
    #boundary
    noFill()
    rect(0, 0, 2000, 2000)
    
    for enemy in enemies:
        enemy.move()
        enemy.drawObject()
    
    for obstacle in obstacles:
        obstacle.drawObject()
    
    popMatrix()
