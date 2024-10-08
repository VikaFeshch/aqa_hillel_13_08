class Rhombus:
    def __setattr__(self, key, value):
        if key == "side_a":
            # Перевірка сторони ромба
            if value > 0:
                super().__setattr__(key, value)
            else:
                raise ValueError("Side length must be greater than 0.")
        elif key == "angle_a":
            # Перевірка кута ромба
            if 0 < value < 180:
                super().__setattr__(key, value)
                super().__setattr__("angle_b", 180 - value)  # Автоматично обчислюємо кут b
            else:
                raise ValueError("Angle must be greater than 0 and less than 180.")
        else:
            raise AttributeError(f"Invalid attribute: {key}. Rhombus only has 'side_a' and 'angle_a'.")

    def __str__(self):
        # Метод для відображення об'єкта ромба як рядка
        return f"Side a: {self.side_a}, Angle a: {self.angle_a}, Angle b: {self.angle_b}"

# Створюємо об'єкт ромба і задаємо атрибути
rhombus = Rhombus()
rhombus.side_a = 5  # Успішне встановлення сторони
rhombus.angle_a = 60  # Успішне встановлення кута a і обчислення кута b

print(f"Side a: {rhombus.side_a}, Angle a: {rhombus.angle_a}, Angle b: {rhombus.angle_b}")

# Тести

def test_valid_data():
    rhombus = Rhombus()
    rhombus.side_a = 5
    rhombus.angle_a = 60
    print(rhombus)  # Виклик методу __str__

def test_side_of_rhombus():
    rhombus = Rhombus()
    try:
        rhombus.side_a = 0  # Це повинно викинути ValueError
    except ValueError as e:
        print(e)
    rhombus.angle_a = 170
    print(rhombus)

def test_angle_of_rhombus():
    rhombus = Rhombus()
    rhombus.side_a = 5
    try:
        rhombus.angle_a = 190  # Це повинно викинути ValueError
    except ValueError as e:
        print(e)

# Виконуємо тести
test_valid_data()
test_side_of_rhombus()
test_angle_of_rhombus()
