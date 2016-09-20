def randomRanges(ranges):
    index = int( random(len(ranges)) )
    val = random(float(ranges[index][0]), float(ranges[index][1]))
    return val

lastTime = 0
def deltaTime():
    global lastTime
    delta = millis() - lastTime
    lastTime = millis()
    return delta

#http://stackoverflow.com/questions/401847/circle-rectangle-collision-detection-intersection
def intersects(ball, platform):
    closestX = constrain(ball.pos.x, platform.pos.x, platform.pos.x + platform.w);
    closestY = constrain(ball.pos.y, platform.pos.y, platform.pos.y + platform.h);
    
    distanceX = ball.pos.x - closestX;
    distanceY = ball.pos.y - closestY;
    
    radius = ball.r / 2
    
    distanceSquared = (distanceX * distanceX) + (distanceY * distanceY);
    return distanceSquared < (radius * radius);