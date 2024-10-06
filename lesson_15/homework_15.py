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
                print(f"Not valid meaning angle of rhombus: {value}. It must be > 0 and < 180")
        else:
            print(f"Invalid attribute: {key}. Rhombus only has 'side_a' and 'angle_a'.")

    def __str__(self):
        return f"angel_a {self.angle_a}, angel_b {self.angle_b}, side a = {self.side_a}"

    def __check_side(self, v):
        return v > 0

    def __check_angle_a(self, v):
        return 0 < v < 180


rhombus = Rhombus()


def test_valid_data():
    rhombus.side_a = 5
    rhombus.angle_a = 60
    assert str(rhombus) == "angel_a 60, angel_b 120, side a = 5"

def test_side_of_rhombus():
    try:
        rhombus.side_a = 0
    except ValueError as e:
        assert str(e) == "Side of rhombus must be greater than 0"

def test_angle_of_rhombus():
    try:
        rhombus.angle_a = 190
    except ValueError as e:
        assert str(e) == "Not valid meaning angle of rhombus: 190. It must be > 0 and < 180"

def test_not_valid_attribute():
    try:
        rhombus.side_b = 10
    except AttributeError as e:
        assert str(e) == "Invalid attribute: 'side_b'. Rhombus only has 'side_a' and 'angle_a'."


test_valid_data()
test_side_of_rhombus()
test_angle_of_rhombus()
test_not_valid_attribute()
