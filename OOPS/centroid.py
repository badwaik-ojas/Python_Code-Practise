
class Centroid:

    coordinates = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Centroid.coordinates.append([x,y])

    @classmethod
    def get_coordinates(cls):
        return cls.coordinates
    
x = Centroid(1,2)
y = Centroid(2,3)
z = Centroid(3,4)

print(Centroid.get_coordinates())