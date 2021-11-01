from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Mediator(ABC):

    @abstractmethod
    def broadcast(self, person: Colleague, message: str) -> None:
        pass

    @abstractmethod
    def direct(self, sender: Colleague, receiver: str, message: str) -> None:
        pass

class Colleague(ABC):

    def __init__(self) -> None:
        self.name: str

    @abstractmethod
    def broadcast(self, message: str) -> None:
        pass

    @abstractmethod
    def direct(self, message: str) -> None:
        pass


class Person(Colleague):
    def __init__(self, name: str, mediator: Mediator) -> None:
        self.name: str = name
        self.mediator = mediator

    def broadcast(self, message: str) -> None:
        self.mediator.broadcast(self, message)

    def direct(self, message: str) -> None:
        print(message)

    def send_direct(self, receiver: Colleague, message: str) -> None:
        self.mediator.direct(self, receiver, message)


class Chatroom(Mediator):

    def __init__(self) -> None:
        self.colleagues: List[Colleague] = []

    def is_colleague(self, colleague: Colleague) -> bool:
        return colleague in self.colleagues

    def add(self, colleague: Colleague) -> None:
        if not self.is_colleague(colleague):
            self.colleagues.append(colleague)

    def remove(self, colleague: Colleague) -> None:
        if self.is_colleague(colleague):
            self.colleagues.remove(colleague)

    def broadcast(self, colleague: Colleague, message: str) -> None:
        if not self.is_colleague(colleague):
            return

        print(f'{colleague.name} says {message}')

    def direct(self, sender: Colleague, receiver: str, message: str) -> None:
        if not self.is_colleague(sender):
            return

        receiver_obj: List[Colleague] = [
            colleague for colleague in self.colleagues
            if colleague.name == receiver
        ]

        if not receiver_obj:
            return

        receiver_obj[0].direct(
            f'{sender.name} for {receiver_obj[0].name}: {message}')


if __name__ == '__main__':

    chat = Chatroom()

    john = Person('John', chat)
    mary = Person('Mary', chat)
    janet = Person('janet', chat)
    kant = Person('kant', chat)

    chat.add(john)
    chat.add(mary)
    chat.add(janet)
    # chat.add(kant)

    john.broadcast('Hello people')
    janet.broadcast('Hi')
    # kant.broadcast('I was not added to chat')

    print()

    john.send_direct('Mary', 'Hi Mary, are you okay?')
    mary.send_direct('John', 'I am pretty good. And how about you ?')
