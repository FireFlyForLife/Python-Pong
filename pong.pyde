#pong, made by Maiko Steeman
from GameObjects import Platform
from GameObjects import Ball
import RandomUtils

import Tests
Tests.vectorTest()

def setup():
    background(0, 0, 0)
    size(400, 400)
    fill(255, 255, 255)
    if width != wdth or height != hght:
        raise Exception("wdth or hght needs to be changed.")

def draw():
    clear()
    
    #platforms
    player1.update()
    player2.update()
    
    #bal
    ball.update()
    checkGoal(ball)
    #calc collision
    calcCollisions()
    checkPlatformCol(player1, False)
    checkPlatformCol(player2, True)
        
    #draw
    ball.render()
    player1.render()
    player2.render()
    
    #draw score
    text("Player 1: " + str(p1score), 10, 10 )
    p2txt = "Player 2: " + str(p2score)
    text(p2txt, width - len(p2txt) * 6, 10)

def calcCollisions():
    #TODO: Account for ball radius
    
    if ball.y == height - ball.r: #check floor
        ball.vY *= -1 + random(-randomRange, randomRange)
        ball.vX += random(-randomRange, randomRange)
        ball.vX *= random(1, float(speedMultiplier))
    elif ball.y == 0 : #check roof
        ball.vY *= -1 + random(-randomRange, randomRange)
        ball.vX += random(-randomRange, randomRange)
        ball.vX *= random(1, float(speedMultiplier))

def checkPlatformCol(platform, bigger):
    if ball.x >= platform.x and ball.x <= platform.x + platform.w and ball.y >= platform.y and ball.y <= platform.y + platform.h:
        if not bigger and ball.vX < 0:
            verticalBounce(ball)
        if bigger and ball.vX > 0:
            verticalBounce(ball)
            
def verticalBounce(ball):
    ball.vX *= -1
    ball.vX *= random(1, float(speedMultiplier))
    
    #TODO: define min and max
    ball.vX += random(-randomRange, randomRange)
    ball.vY += random(-randomRange, randomRange)
    
def checkGoal(ball):
    if ball.x > width:
        global p1score
        p1score += 1
        resetBall(ball)
    elif ball.x < 0:
        global p2score
        p2score += 1
        resetBall(ball)

def resetBall(ball):
    ball.x = wdth/2 - 5
    ball.y = hght/2 - 5
    
    xRange = (-initialSpeed , -initialSpeed * 0.75 ), (initialSpeed * 0.75, initialSpeed )
    ball.vX = RandomUtils.randomRanges(xRange)
    yRange = (-initialSpeed, -initialSpeed * 0.75), (initialSpeed * 0.75, initialSpeed)
    ball.vY = RandomUtils.randomRanges(yRange) / 2

def keyPressed():
    speed = 3
    
    if key == 'w': #player1
        player1.vY = -speed
    elif key == 's':
        player1.vY = speed
    elif keyCode == UP: #Player2
        player2.vY = -speed
    elif keyCode == DOWN:
        player2.vY = speed

def keyReleased():
    speed = 0
    
    if key == 'w': #player1
        player1.vY = -speed
    elif key == 's':
        player1.vY = speed
    elif keyCode == UP: #Player2
        player2.vY = -speed
    elif keyCode == DOWN:
        player2.vY = speed

wdth = 400
hght = 400

p1score = 0
p2score = 0

player1 = Platform(10, hght/2 - 30)
player2 = Platform(wdth-20, hght/2 - 30)

initialSpeed = 3
speedMultiplier = 1.1 #TODO: dont use lineair acceleration
randomRange = 0.5
ball = Ball(wdth/2 - 5, hght/2 - 5)
#ball.vX = random(-initialSpeed * 1, initialSpeed * 1)
#ball.vY = random(-initialSpeed / 2, initialSpeed / 2)
resetBall(ball)

#ball.vX = 10
#ball.vY = 6