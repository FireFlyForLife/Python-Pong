def linedir(x, y, dir, dirY = None):
    if dirY is None:
        line(x, y, x + dir.x, y + dir.y)
    else:
        line(x, y, x + dir, y + dirY)