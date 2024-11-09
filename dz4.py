class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"{self.age} is out of range"

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def set_age(self, age):
        if age < 0 or age > 120:
            raise InvalidAgeError(age)
        self.age = age
        return self

try:
    person = Person("Maksim", 100)
    print(person.age)
except InvalidAgeError as e:
    print(e)