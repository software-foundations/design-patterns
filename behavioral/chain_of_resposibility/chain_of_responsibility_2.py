from abc import ABC, abstractmethod


class Handler(ABC):

	def __init__(self):
		self.next_handler: Handler

	@abstractmethod
	def handle(self, letter: str) -> str:
		pass


class HandlerABC(Handler):
	def __init__(self, next_handler: Handler) -> None:
		self.letters = ['A', 'B', 'C']
		self.next_handler = next_handler		

	def handle(self, letter: str) -> str:
		if letter in self.letters:
			return f'HandlerDEF: managed to handle the error {letter}'

		return self.next_handler.handle(letter)


class HandlerDEF(Handler):
	def __init__(self, next_handler: Handler) -> None:
		self.letters = ['D', 'E', 'F']
		self.next_handler = next_handler

	def handle(self, letter: str) -> str:
		if letter in self.letters:
			return f'HandlerDEF: managed to handle the error {letter}'

		return self.next_handler.handle(letter)


class HandlerUnsolved(Handler):
	def handle(self, letter: str) -> str:
		return f"HandlerUnsolved: not handle the {letter}"

###############
# Client Code #
###############

if __name__ == "__main__":

	handler_unsolved = HandlerUnsolved()						# Last handle
	handler_def = HandlerDEF(next_handler=handler_unsolved)
	handler_abc = HandlerABC(next_handler=handler_def)			# First handle

	print(handler_abc.handle('A'))
	print(handler_abc.handle('B'))
	print(handler_abc.handle('C'))
	print(handler_abc.handle('D'))
	print(handler_abc.handle('E'))
	print(handler_abc.handle('G'))
	print(handler_abc.handle('H'))
	print(handler_abc.handle('I'))

	print(handler_def.handle('A'))
	print(handler_def.handle('B'))
	print(handler_def.handle('C'))
	print(handler_def.handle('D'))
	print(handler_def.handle('E'))
	print(handler_def.handle('G'))
	print(handler_def.handle('H'))
	print(handler_def.handle('I'))