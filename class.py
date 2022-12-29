# Author: Oladapo Okikiola
class Person:
    def __init__(self, age, name):
        self.name = name
        self.age = age

john = Person('john', 22)
print(john.name + ' ' + str(john.age))