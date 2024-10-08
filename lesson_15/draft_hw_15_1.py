class Rhombus:
    def __setattr__(self, key, value):
        if key == "side_a" and value <= 0:
            raise ValueError("Side length must be greater than 0.")
        if key == "angle_a":
            if value <= 0 or value >= 180:
                raise ValueError("Angle must be greater than 0 and less than 180.")
            # Automatically calculate the opposite angle
            super().__setattr__("angle_b", 180 - value)
        super().__setattr__(key, value)

    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a  # `angle_b` will be set automatically here

    def __str__(self):
        return f"Rhombus with side_a = {self.side_a}, angle_a = {self.angle_a}, and angle_b = {self.angle_b}"

# Testing the class
try:
    rhombus = Rhombus(5, 60)
    print(rhombus)

    # Invalid side length (should raise an error)
    rhombus.side_a = -1

    # Invalid angle (should raise an error)
    rhombus.angle_a = 200

except ValueError as e:
    print(e)

# Valid case
rhombus = Rhombus(7, 120)
print(f"angle_a = {rhombus.angle_a}, angle_b = {rhombus.angle_b}, side_a = {rhombus.side_a}")
