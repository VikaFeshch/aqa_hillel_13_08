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


def validate_class_attribute_contain(val_class, name_attr):
    assert hasattr(val_class,name_attr), \
        f"class {val_class.__class__.__name__} doesn't have attribute {name_attr}"


@mark.parametrize("name_attr", [
    "department1",
    "programming_language"
])
def test_team_lead_attributes_params(name_attr):
    team_lead = TeamLead("Igor", 5000, "Dev", "Python", 5)
    validate_class_attribute_contain(team_lead, name_attr)

