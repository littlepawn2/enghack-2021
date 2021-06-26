from entities import Player
from entities import Enemy
from obstacles import Obstacle


def setup():
    global player, enemies, obstacles, sky
    
    pic =  loadImage ("kirbypuffy.png")
    sky = loadImage ("sky.jpeg")
    player = Player(400, 300, 25, pic)
    enemies = []
    obstacles = []
    
    size(800, 600)
    stroke(255)
    
    ##add enemies
    enemies.append(Enemy(100, 100, 25, 0))
    enemies.append(Enemy(500, 100, 25, 100))
    enemies.append(Enemy(100, 800, 25, 250))
    
    ##add obstacles
    for i in range(10):
        obstacles.append(Obstacle(random(100, 1700), random(100, 1700), random(50, 200), random(50, 200), "SOFT"))
    for i in range(5):
        obstacles.append(Obstacle(random(100, 1700), random(100, 1700), random(50, 200), random(50, 200), "HARD"))
    
def draw():
    global player, enemies, obstacles, sky
    
    background(0)
    image (sky,0,0)
    
    pushMatrix()
    translate(-player.pos.x+400, -player.pos.y+300)
    
    #boundary
    noFill()
    strokeWeight(1)
    rect(0, 0, 2000, 2000)
    strokeWeight(0)
    
    for obstacle in obstacles:
        obstacle.drawObject()
    
    for enemy in enemies:
        enemy.move(player)
        enemy.boundaryCollision()
        for obstacle in obstacles:
            enemy.collide(obstacle)
        enemy.drawObject()
    
    popMatrix()
    
    
    player.move()
    player.boundaryCollision()
    for enemy in enemies:
        player.collide(enemy)
    for obstacle in obstacles:
        player.collide(obstacle)
    player.drawObject()
