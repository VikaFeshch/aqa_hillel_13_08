from pytest import mark

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        self.team_size = team_size

def validate_class_attribute_contain(val_class, name_attr, expected_value):
    assert hasattr(val_class,name_attr), \
        f"class {val_class.__class__.__name__} doesn't have attribute {name_attr}"

    actual_value = getattr(val_class, name_attr)
    assert actual_value == expected_value, \
        f"value of {name_attr} is {actual_value}, but expected {expected_value}"

@mark.parametrize("name_attr, expected_value", [
    ("department", "Dev"),
    ("programming_language", "Python")
])
def test_team_lead_attributes_params(name_attr, expected_value):
    team_lead = TeamLead("Igor", 5000, "Dev", "Python", 5)
    validate_class_attribute_contain(team_lead, name_attr, expected_value)

