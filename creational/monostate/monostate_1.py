from __future__ import annotations
from typing import Dict


class StringReprMixin:
    """
    Super class to ne used to create
    instances with __str__ and the __repr__
    overrided by these bellow, allowing to see
    instances information prettyly
    """
    def __str__(self) -> str:
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()


class MonoStateSimple(StringReprMixin):
    # It is a class property
    _state: Dict = {} # shared state (property) between classes

    def __init__(self, nome=None, sobrenome=None) -> None:        
        # This line override the self.__dict__ by the shared state
        # Remember that the shared state owns to class,
        # so all the classes instances inherance this
        # as well as all instances have their __dict__
        # overrided by this
        # al remenber that all instance execute __init__ when instantiated
        self.__dict__ = self._state # THIS LINE IS TOO MUCH IMPORTANT

        if nome is not None:
            self.nome = nome

        if sobrenome is not None:
            self.sobrenome = sobrenome


if __name__ == "__main__":
    m1 = MonoStateSimple(nome='Luiz')
    m2 = MonoStateSimple(sobrenome='Miranda')
    print(m1)
    print(m2)