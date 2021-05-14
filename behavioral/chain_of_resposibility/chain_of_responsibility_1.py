def handler_ABC(letter: str) -> str:
	letters = ['A', 'B', 'C']

	if letter in letters:
		return f'handler_ABC: managed to handle the error {letter}'

	return handler_DEF(letter)


def handler_DEF(letter: str) -> str:
	letters = ['D', 'E', 'F']

	if letter in letters:
		return f'handler_DEF: managed to handle the error {letter}'

	return handler_unsolved(letter)


def handler_unsolved(letter: str) -> str:
	return f"handler_unsolved: i don't know to treat the error {letter}"


if __name__ == "__main__":
	print(handler_ABC('A'))
	print(handler_ABC('B'))
	print(handler_ABC('C'))
	print(handler_ABC('D'))
	print(handler_ABC('G'))
	print(handler_ABC('H'))
	print(handler_ABC('I'))
	