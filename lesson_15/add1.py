class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def volume(self):
        return (4/3) * 3.14 * self.radius**3

class Cube:
    def __init__(self, side_length):
        self.side_length = side_length

    def volume(self):
        return self.side_length**3

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return 3.14 * self.radius**2 * self.height

def calculate_volume(obj):
    return obj.volume()

sphere = Sphere(5)
print(calculate_volume(sphere))

cube = Cube(5)
print(calculate_volume(cube))

cylinder = Cylinder(5, 5)
print(calculate_volume(cylinder))