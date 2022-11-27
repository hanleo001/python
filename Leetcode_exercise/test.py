class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

if __name__ == '__main__':
    points = []
    for i in range(1000):
        points.append(new Point(i,i,i))