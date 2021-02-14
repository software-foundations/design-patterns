from abc import ABC, abstractmethod

class Pizza(ABC):

	def prepare(self) -> None:
		"""Template method"""
		self.hook_before_add_ingredients() # Hook
		self.add_ingredients() # Abstract
		self.hook_before_cook() # Hook		
		self.cook() # Abstract
		self.cut() # Concrete
		self.serve()# Concrete

	# Hooks
	def hook_before_add_ingredients(self) -> None: pass
	def hook_before_cook(self) -> None: pass

	# Concrete methods
	def cut(self) -> None:
		print(f'{self.__class__.__name__}: Cutting the pizza')

	def serve(self) -> None:
		print(f'{self.__class__.__name__}: Serving the pizza')

	# Abstract methods
	@abstractmethod
	def add_ingredients(self) -> None: pass

	@abstractmethod
	def cook(self) -> None: pass


class StylishPizza(Pizza):

	def add_ingredients(self) -> None:
		print('StylishPizza: Chesse, Hum, and Guava Paste')

	def cook(self) -> None:
		print('StylishPizza: Cooking for 45 minutes in the wood oven')


class VeganPizza(Pizza):

	def hook_before_add_ingredients(self) -> None:
		print('VeganPizza: washing the ingredients')

	def add_ingredients(self) -> None:
		print('VeganPizza: Soy, Potato, and Tomato')

	def cook(self) -> None:
		print('StylishPizza: Cooking for 5 minutes in the commom oven')	

if __name__ == '__main__':

	stylish = StylishPizza()
	stylish.prepare()

	print(30 * '-')

	vegan = VeganPizza()
	vegan.prepare()
