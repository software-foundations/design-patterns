# To typehinting classes that is below the
# typehinting annotations. It only works when
# it is at the first line
from __future__ import annotations

# To copy mutable value and not 
# point to the same memory position
from copy import deepcopy

from typing import List

"""
It is usefull to reuse objects already created,
put their informations in a new one who will
change little things/attributes
"""

class StringReprMixin:
    def __str__(self) -> str:
        params = ', '\
        .join([f'{k}={v}' for \
        	k, v in self.__dict__.items()])
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()


class Person(StringReprMixin):
	def __init__(\
		self, firstname: str, lastname: str) -> None:
		self.firstname: str = firstname
		self.lastname: str = lastname
		self.addresses: List[Address] = []

	def add_address(\
		self, address: Address) -> None:
		self.addresses.append(address)

	def clone(self) -> Person:
		"""return a copy of the person
		object (remember that an object
		is a mutable value so we need
		use deepcopy to make a copy of
		the object)
		"""
		return deepcopy(self)



class Address(StringReprMixin):
	def __init__(self, street: str, number: str):
		self.street: str = street
		self.number: str = number


if __name__ == "__main__":

	father = Person('Bruno', 'Silva')
	father_address = Address('Ananindeua', '169')
	father.add_address(father_address)
	
	mother = deepcopy(father)
	mother.firstname = 'Hanna'

	print(father)
	print(mother)