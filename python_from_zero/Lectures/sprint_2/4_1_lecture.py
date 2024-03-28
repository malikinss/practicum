"""
This module collects helper functions and classes that "span" multiple levels
of MVC. In other words, these functions/classes introduce controlled coupling
for convenience's sake.
"""
...

def render():
    """
    Return a HttpResponse whose content is filled with the result of calling
    django.template.loader.render_to_string() with the passed arguments.
    """
    ...


"""Документация модуля. Описывает работу классов и функций. 
Размещается в верхней части файла (начиная с 1-й строки).
"""


def foo(self):
    """Описывает работу функции foo."""
    ...


class Test:
    """Класс Test используется для демонстрации docstring. 
    После этой строки нужна пустая строка, поскольку методы в классе 
    отделяются одной пустой строкой.
    """
        
    def first(self):
        """Описывает метод first и демонстрирует перенос строки 
        документации.
        """
        ...

"""Возвращает число 1."""

def foo():
    """Можно перенести
    так.
    """


def bar():
    """
    А можно - 
    так.
    """ 

import math

# Спросим, что хорошего в этой библиотеке
print(math.__doc__)

# Будет напечатано:
# This module provides access to the mathematical functions
# defined by the C standard. 


"""Документация модуля. Описывает работу классов и функций. 
Размещается в верхней части файла (начиная с первой строки).
"""
def tricky_func(self):
    """Описывает работу функции tricky_func."""
    ...


class Test:
    """Класс Test используется для демонстрации docstring."""

    def first(self):
        """Описывает метод first и демонстрирует перенос строки 
        документации.
        """
        ...


print(__doc__)
print(tricky_func.__doc__)
print(Test.__doc__)
print(Test.first.__doc__)



"""Документация модуля. Описывает работу классов и функций. 
Размещается в верхней части файла (начиная с первой строки).
"""
import inspect


def tricky_func(self):
    """Описывает работу функции tricky_func."""
    ...


class Test:
    """Класс Test используется для демонстрации docstring."""

    def first(self):
        """Описывает метод first и демонстрирует перенос строки 
        документации.
        """
        ...


print("Без применения cleandoc:")
print(Test.first.__doc__)
print("С применением cleandoc:")
print(inspect.cleandoc(Test.first.__doc__))
