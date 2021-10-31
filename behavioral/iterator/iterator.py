from collections.abc import Iterator, Iterable
from typing import List, Any


class MyIterator(Iterator):

    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = 0

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index += 1
            return item
        except IndexError:
            raise StopIteration

class ReverseIterator(Iterator):

    def __init__(self, collection: List[Any]) -> None:
        self._collection = collection
        self._index = -1

    def __next__(self):
        try:
            item = self._collection[self._index]
            self._index -= 1
            return item
        except IndexError:
            raise StopIteration

class MyList(Iterable):

    def __init__(self) -> None:
        self._items: List[Any] = []
        self._my_iterator = MyIterator(self._items)
        self._reverse_iterator = ReverseIterator(self._items)

    def add(self, value: Any) -> None:
        self._items.append(value)

    def __iter__(self) -> Iterator:
        return self._my_iterator

    def reverse_iterator(self) -> Iterator:
        return self._reverse_iterator

    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self._items}'


if __name__ == '__main__':

    myList = MyList()

    myList.add('Bruno')

    myList.add('Alex')

    myList.add('Matheus')

    print(myList)

    print('roubei um valor: ', next(iter(myList)))

    for value in myList:

        print('value: ', value)

    for value in myList.reverse_iterator():

        print('value: ', value)
