#region Task
'''
Given four points, you're required to print tha angle btw the plane made by points
in degrees.
'''
#endregion

#region Class Points
class Points(object):
    def __init__(self, x, y, z):
        '''
        You can you object[index], however doing it like this is easier.
        '''
        self.x = x
        self.y = y
        self.z = z
    def __sub__(self, other):
        return Points((self.x-other.x), (self.y- other.y), (self.z-other.z))

    def dot(self, other):
        return self.x*other.x+ self.y*other.y+ self.z* other.z
    
    def cross(self, other):
        return Points((self.y*other.z - self.z*other.y), (self.z*other.x-self.x*other.z)
        , (self.x*other.y-self.y*other.x))
    
    def absolute(self):
        return pow((self.x**2 + self.y**2 + self.z**2), 0.5)
#endregion

if __name__ == "__main__":
    import math
    points = list()
    for i in range(4):
        a = list(map(float, input("Enter the point:   ").split()))
        points.append(a)
    
    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print(f"{math.degrees(angle):0.2f}")
