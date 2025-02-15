#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from people import Person, Worker

if __name__ == '__main__':
    name = 'Alberto'
    person_1 = Person(name, 20)
    person_1.presentation()

    #Part 2: step 2
    worker_1 = Worker('Miguel', 26, 'Big Data', 'Data Engineeging')
    worker_1.presentation()

    #Part 2: step 5
    my_var_list = ["Andrea", 42, "Ventas", "Manager"]
    worker_2 = Worker(*my_var_list)
    worker_2.presentation()

    #Part 2: step 6
    my_var_dict = {"nombre": "Andrea",
                   "edad": "42",
                   "departamento": "Ventas",
                   "puesto": "Manager"}
    worker_3 = Worker(
        name=my_var_dict['nombre'],
        age=my_var_dict['edad'],
        department=my_var_dict['departamento'],
        position=my_var_dict['puesto']
    )
    worker_3.presentation()

    # With the keys in English:
    # my_var_dict = {"name": "Andrea",
    #                "age": "42",
    #                "department": "Ventas",
    #                "position": "Manager"}
    # worker_3 = Worker(**my_var_dict)
    # worker_3.presentation()
