############################################
# OOP

############################################
# Inheritance
# Encapsulation
# Polymorphism

############################################
# Inheritance
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


    def describe(self):
        print(f"This is a {self.brand} {self.model}")

class RaceCar(Car):
    def __init__(self, brand, model, top_speed):
        super().__init__(brand, model)
        self.top_speed = top_speed

        # override method
    def describe(self):
        print(f"This is a super race car {self.brand} {self.model}")

    def race(self):
        print(f"The {self.brand} {self.model} can race a top speed {self.top_speed}")

class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity
        self.year = 2024
        self.options = {}

race_car = RaceCar("Nissan", "GTR", 250)
race_car.describe()
race_car.race()


############################################
# Encapsulation
class Car:
    def __init__(self, brand, model, mileage, fuel_level):
        self.brand = brand
        self.model = model              # public
        self._mileage = mileage         # protected (Encapsulation)
        self.__fuel_level = fuel_level  # private
        self._engine_status = False

        # public method
    def get_mileage(self):
        return self._mileage

    def set_mileage(self):
        self._mileage

    def start_engine(self):
        if self._check_fuel():
            self._engine_status = True
            print("The engine started")
        else:
            print(f"The engine can`t be started. The fuel level is {self.__fuel_level}")

    # protected method (Encapsulation) - -> can be used inheritance class
    def _check_fuel(self):
        if self.__fuel_level > 0:
            return True
        return False

    # private method (Encapsulation)
    def _check_motor(self):
        pass

car = Car("Handa", "CRV", 10000, 0)
print(car.get_mileage())
# print(car._mileage)
# print(car._Car__fuel_level)
# print(car._check_fuel())
car.start_engine()


############################################
# Polymorphism

class Car:

    def describe(self):
        print("This is a base car")

class RaceCar(Car):
    def describe(self):
        print("This is a race car")

class ElectricCar(Car):
    def describe(self):
        print("This is a electric car")

def car_description(new_car: Car):
    new_car.describe()

base_car = Car()
rase_car = RaceCar()
tesla = ElectricCar()

car_description(base_car)
car_description(rase_car)
car_description(tesla)

############################################
class DataSource:
    def read_data(self):
        raise NotImplemented("This method must be implemented in a subclass")

class JsonSource(DataSource):
    def read_data(self):
        print("Reading from json file")

class CsvSource(DataSource):
    def read_data(self):
        print("Reading from csv file")

class APISource(DataSource):
    def read_data(self):
        # API calls
        print("Reading from API")

def fetch_data(data_source: DataSource):
    data_source.read_data()

def test_production_data():
    # Arrange
    json_source = JsonSource()
    fetch_data(json_source)

def test_sandbox_data():
    # Arrange
    api_source = APISource()
    fetch_data(api_source)
