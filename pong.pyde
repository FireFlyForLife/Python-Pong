#pong, made by Maiko Steeman
from GameObjects import Platform
from GameObjects import Ball
from MathF import Vector2d as Vector
from DrawUtils import linedir
import RandomUtils
import Config

#import Tests
#Tests.vectorTest()

def setup():
    background(0, 0, 0)
    size(400, 400)
    fill(255, 255, 255)
    if width != Config.wdth or height != Config.hght:
        raise Exception("Config.wdth or Config.hght need to be equal.")

def draw():
    if not focused:
        return
    
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
    text("Player 1: " + str(p1score), 25, 10 )
    p2txt = "Player 2: " + str(p2score)
    text(p2txt, width - len(p2txt) * 6 - 15, 10)
    
    if Config.debug:
        drawDebug()
        
def drawDebug():
    fill(255, 0, 255)
    stroke(255, 0 ,255)
    line(ball.pos.x, ball.pos.y, ball.pos.x + ball.vel.x * 115, ball.pos.y + ball.vel.y * 115)
    line(ball.pos.x - ball.r / 2, ball.pos.y, ball.pos.x + ball.r / 2, ball.pos.y )
    boxCenter = Vector(player1.pos.x + player1.w / 2, player1.pos.y + player1.h / 2)
    dir = ball.pos - boxCenter
    linedir(boxCenter.x, boxCenter.y, dir.x, dir.y)
    
    text("speed: " + str(ball.vel) + " w/ " + str(ball.vel.magnitude()), 10, 100)
    text("deg: " + str(ball.vel.deg()), 10, 110)
    
    stroke(0, 0, 0)
    fill(255, 255, 255)

def calcCollisions():
    if ball.pos.y + ball.r / 2 >= height: #check floor
        ball.vel.y *= -1
        angle = ball.vel.deg() + random(-Config.ballBounceRandom, Config.ballBounceRandom)
        ball.vel.deg(angle)
        #ball.vel.x += random(-Config.ballBounceRandom, Config.ballBounceRandom)
        #ball.vel.x *= random(1, float(Config.ballSpeedMultiplier))
    elif ball.pos.y - ball.r / 2== 0 : #check roof
        ball.vel.y *= -1
        angle = ball.vel.deg() + random(-Config.ballBounceRandom, Config.ballBounceRandom)
        ball.vel.deg(angle)
        #ball.vel.x += random(-Config.ballBounceRandom, Config.ballBounceRandom)
        #ball.vel.x *= random(1, float(Config.ballSpeedMultiplier))

def checkPlatformCol(platform, bigger):
    x = ball.pos.x + ball.r / 2
    y = ball.pos.y + ball.r / 2
    #if x >= platform.pos.x and x <= platform.pos.x + platform.w and y >= platform.pos.y and y <= platform.pos.y + platform.h:
    if RandomUtils.intersects(ball, platform):
        if not bigger and ball.vel.x < 0:
            verticalBounce(ball, platform)
        if bigger and ball.vel.x > 0:
            verticalBounce(ball, platform)
            
def verticalBounce(ball, platform):
    ball.vel.x *= -1
    oldmag = ball.vel.magnitude()
    ball.vel *= random(1, float(Config.ballSpeedMultiplier))
    
    boxCenter = Vector(platform.pos.x + platform.w / 2, platform.pos.y + platform.h / 2)
    dir = ball.pos - boxCenter
    leng = ball.vel.magnitude()
    norm_dir = dir.normalize_()
    avg = (ball.vel.normalize_() + norm_dir) / 2
    vec = avg.normalize_() * leng
    
    #TODO: define min and max
    ball.vel = vec
    angle = ball.vel.deg() + random(-Config.ballPlayerBounceRandom, Config.ballPlayerBounceRandom)
    ball.vel.deg(angle)
    print(ball.vel.magnitude() - oldmag)
    #ball.vel.x += random(-Config.ballBounceRandom, Config.ballBounceRandom)
    #ball.vel.y += random(-Config.ballBounceRandom, Config.ballBounceRandom)
    
def checkGoal(ball):
    if ball.pos.x > width:
        global p1score
        p1score += 1
        resetBall(ball)
    elif ball.pos.x < 0:
        global p2score
        p2score += 1
        resetBall(ball)

def resetBall(ball):
    ball.pos.x = Config.wdth/2 - 5
    ball.pos.y = Config.hght/2 - 5
    
    target = player1
    if lastScored == 1:
        target = player2
    
    directDir = ball.pos - target.pos
    dir = directDir.normalize_() * Config.initialBallSpeed
    deg = dir.deg() + random(-Config.initialBallAngleRandom, Config.initialBallAngleRandom)
    
    ball.vel.deg(deg)
    
    #xRange = (-Config.initialBallSpeed , -Config.initialBallSpeed * 0.75 ), (Config.initialBallSpeed * 0.75, Config.initialBallSpeed )
    #ball.vel.x = RandomUtils.randomRanges(xRange)
    #yRange = (-Config.initialBallSpeed, -Config.initialBallSpeed * 0.75), (Config.initialBallSpeed * 0.75, Config.initialBallSpeed)
    #ball.vel.y = RandomUtils.randomRanges(yRange) / 2

def keyPressed():
    if key == 'w': #player1
        player1.vel.y = -Config.playerSpeed
    elif key == 's':
        player1.vel.y = Config.playerSpeed
    elif keyCode == UP: #Player2
        player2.vel.y = -Config.playerSpeed
    elif keyCode == DOWN:
        player2.vel.y = Config.playerSpeed

def keyReleased():
    if key == 'w': #player1
        player1.vel.y = 0
    elif key == 's':
        player1.vel.y = 0
    elif keyCode == UP: #Player2
        player2.vel.y = 0
    elif keyCode == DOWN:
        player2.vel.y = 0

p1score = 0
p2score = 0
lastScored = int(random(0, 1))

player1 = Platform(10, Config.hght/2 - 30)
player2 = Platform(Config.wdth-20, Config.hght/2 - 30)

ball = Ball(Config.wdth/2 - 5, Config.hght/2 - 5)
resetBall(ball)