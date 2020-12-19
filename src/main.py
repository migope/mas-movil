#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from people import Person, Worker

if __name__ == '__main__':
    name = 'Alberto'
    person_1 = Person(name, 20)
    person_1.presentation()

    worker_1 = Worker('Miguel', 26, 'Big Data', 'Data Engineeging')
    worker_1.presentation()

    my_var_list = [ "Andrea", 42, "Ventas", "Manager"]
    worker_2 = Worker(*my_var_list)
    worker_2.presentation()