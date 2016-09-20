import MathF

def vectorTest():
    vec = MathF.Vector2d(0, 1)
    print vec
    print vec.deg()
    print vec.rad()
    print vec.magnitude()
    vec.deg(90.0)
    print vec