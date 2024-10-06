"""Створіть клас геометричної фігури "Ромб". Клас повинен мати
наступні атрибути:

сторона_а (довжина сторони a).
кут_а (кут між сторонами a і b).
кут_б (суміжний з кутом кут_а).
Необхідно реалізувати наступні вимоги:

Значення сторони сторона_а повинно бути більше 0.
Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а,
значення кут_б обчислюється автоматично.
Для встановлення значень атрибутів використовуйте метод setattr."""



class Rhombus:

    def __setattr__(self, key, value):
        if key == "side_a":
            if self.__check_side(value):
                super().__setattr__(key, value)
            else:
                print("Side of rhombus must be greater than 0")
        elif key == "angle_a":
            if self.__check_angle_a(value):
                super().__setattr__(key, value)
                super().__setattr__("angle_b", 180 - value)
            else:
                print(f"Not valid meaning angle of rhombus: {self.angle_a}. It must be > 0 and < 180")
        else:
            print(f"Invalid attribute: {key}. Rhombus only has 'side_a' and 'angle_a'.")


    def __str__(self):
        return f"angel_a {rhombus.angle_a}, angel_b {rhombus.angle_b}, side a = {rhombus.side_a}"

    def __check_side(self, v):
        return v > 0

    def __check_angle_a(self, v):
        return 0 < v < 180


rhombus = Rhombus()

def test_valid_data():
    rhombus.side_a = 5
    rhombus.angle_a = 60
    print(rhombus)

def test_side_of_rhombus():
    rhombus.side_a = 0
    rhombus.angle_a = 170
    print(rhombus)

def test_angle_of_rhombus():
    rhombus.side_a = 5
    rhombus.angle_a = 190
    print(rhombus)

def test_not_valide_attribute():
    rhombus.side_b = 10
    rhombus.angle_a = 170
    print(rhombus)


test_valid_data()
test_side_of_rhombus()
test_angle_of_rhombus()
test_not_valide_attribute()
