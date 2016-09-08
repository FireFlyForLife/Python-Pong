def randomRanges(ranges):
    index = int( random(len(ranges)) )
    val = random(float(ranges[index][0]), float(ranges[index][1]))
    return val