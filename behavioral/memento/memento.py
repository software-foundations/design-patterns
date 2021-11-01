"""
Memento - desgin pattern to restores a state of an object

Originator - imutable object which saves its state
Memento - saves a Originator state
Caretaker - stores mementos
"""

from __future__ import annotations
from typing import List, Dict, Any
from copy import deepcopy


class Memento:
    def __init__(self, state):
        self._state: Dict
        super().__setattr__('_state', state)

    def get_state(self) -> Dict:
        return self._state

    def __setattr__(self, name: str, value: Any) -> None:
        raise AttributeError('Sorry, I am immutable')


class ImageEditor:
    def __init__(self, name: str, width: int, height: int) -> None:
        self.name = name
        self.width = width
        self.height = height

    def save_state(self) -> Memento:
        return Memento(deepcopy(self.__dict__))

    def restore(self, memento: Memento) -> None:
        self.__dict__ = memento.get_state()

    def __str__(self):
        return f'{self.__class__.__name__}({self.__dict__})'


class Caretaker:
    def __init__(self, originator: ImageEditor):
        self._originator = originator
        self._mementos: List[Memento] = []

    def backup(self) -> None:
        self._mementos.append(self._originator.save_state())

    def restore(self) -> None:
        if not self._mementos:
            return

        self._originator.restore(self._mementos.pop())


if __name__ == '__main__':

    img = ImageEditor('PHOTO_1.jpg', 111, 111)

    caretaker = Caretaker(img)
    caretaker.backup()

    img.name = 'PHOTO2.jpg'
    img.width = 222
    img.height = 222
    caretaker.backup()

    img.name = 'PHOTO3.jpg'
    img.width = 333
    img.height = 333
    caretaker.backup()

    img.name = 'PHOTO4.jpg'
    img.width = 444
    img.height = 444

    caretaker.restore()
    caretaker.restore()
    caretaker.restore()
    caretaker.restore()
    caretaker.restore()

    print(img)
