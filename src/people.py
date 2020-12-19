# -*- coding: utf-8 -*-

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def presentation(self):
        print(f"Hola! Soy {self.name} y tengo {self.age} años")

class Worker(Person):
    def __init__(self, name, age, department, position):
        super().__init__(name, age)
        self.department = department
        self.position = position
    
    def presentation(self):
        print(f"Hola! Soy {self.name} y tengo {self.age} años. Estoy en el puesto {self.position} del departamento {self.department}.")
