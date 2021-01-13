from __future__ import annotations
from typing import Dict

"""
https://qastack.com.br/programming/4613000/what-is-the-cls-variable-used-for-in-python-classes

always use self for the first argument of an instance method

always use self for the first argument of a class method
"""
class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()


class MonoState(StringReprMixin):
    _state: Dict = {} # class attribute # https://stackoverflow.com/questions/7374748/whats-the-difference-between-a-python-property-and-attribute#:~:text=In%20general%20speaking%20terms%20a,attribute%20(or%20other%20data).

    # new is to set how will occurs the instantiation of a class, and it returs the object instantiated
    def __new__(cls, *args, **kwargs): # cls refers to MonoState class
        obj = super().__new__(cls) # instantiate the MonoState obj by the __new__ of the StringReprMixi class
        obj.__dict__ = cls._state # monoState obj.__dict__ is overrided by the _state attribute of the cls (MonoState) inheranced for the StringReprmixin
        return obj

    # init just inicializated the instantiated object, but it doesn't return
    # anything
    def __init__(self, nome=None, sobrenome=None) -> None:
        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome


class A(MonoState):
    pass


if __name__ == "__main__":
    m1 = MonoState(nome='Luiz')
    m2 = A(sobrenome='Miranda')
    print(m1)
    print(m2)