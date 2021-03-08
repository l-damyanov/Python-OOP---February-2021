from multiple_inheritence.person import Person
from multiple_inheritence.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
