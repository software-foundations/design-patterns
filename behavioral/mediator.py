"""
Mediator is a behavioral design pattern
which aims to define an object which
encapsulates the way of a set o objects
interact to each other.

The mediator promote low accopling by
avoiding that objects explicitly refers
to each other, and allow many
interactions regardless.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Colleague(ABC):

	def __init__(self):
		self.name: str

	@abstractmethod
	def broadcast(self, message: str) -> None:
		pass

	@abstractmethod
	def direct(self, message: str) -> None:
		pass


class Person(Colleague):

	def __init__(self, name: str, mediator: Mediator) -> None:
		self.name = name
		self.mediator = mediator

	def broadcast(self, message: str) -> None:
		self.mediator.broadcast(self, message)

	def send_direct(self, receiver: str, message: str) -> None:
		self.mediator.direct(self, receiver, message)

	def direct(self, message: str) -> None:
		print(message)


class Mediator(ABC):

	@abstractmethod
	def broadcast(self, person: Colleague, message: str) -> None:
		pass

	@abstractmethod
	def direct(self, sender: Colleague, receiver: str, message: str) -> None:
		pass


class Chatroom(Mediator):

	def __init__(self) -> None:
		self.colleagues: List[Colleague] = []

	def is_colleague(self, colleague: Colleague) -> bool:
		return colleague in self.colleagues

	def add_colleague(self, colleague) -> None:
		if not self.is_colleague(colleague):
			self.colleagues.append(colleague)

	def remove_coleague(self, colleague) -> None:
		if not self.is_colleague(colleague):
			self.colleagues.remove(colleague)

	def broadcast(self, colleague: Colleague, message: str) -> None:
		if not self.is_colleague(colleague):
			return

		print(f'{colleague.name} says: {message}')

	def direct(self, sender: str, receiver: str, message: str) -> None:
		if not self.is_colleague(sender):
			return

		receiver_obj: List[Colleague] = [
			colleague for colleague in self.colleagues
			if colleague.name == receiver
		]

		if not receiver_obj:
			return

		receiver_obj[0].direct(
			f'{sender.name} for {receiver}: {message}'
		)

if __name__ == "__main__":

	chat = Chatroom()

	john = Person(name='John', mediator=chat)
	mary = Person(name='Mary', mediator=chat)
	elis = Person(name='Elis', mediator=chat)
	jose = Person(name='Jose', mediator=chat)

	chat.add_colleague(john)
	chat.add_colleague(mary)
	chat.add_colleague(elis)	
	# chat.add_colleague(jose)

	john.broadcast('Hello everybody')
	mary.broadcast("Hi! What's up?")
	jose.broadcast("I was not add to the chat")

	john.send_direct('Mary', 'Hello, Mary. How are you?')
	mary.send_direct('John', 'Hi, John. I am fine')
