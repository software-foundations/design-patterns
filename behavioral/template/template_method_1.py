from abc import ABC, abstractmethod

class Abstract(ABC):

	def tempalte_method(self):
		"""finall method/internal method
		(method taht cannot be overrided - by the subclasses - and
		then to be used by them)"""
		self.hook() # only has implementation if subclass wants to
		self.operation1()
		self.base_class_method()
		self.operation2()

	def hook(self): pass

	def base_class_method(self):
		print('base class method that not needs to be specialized')
		print('its definition and implementation' + \
			' is in the abstract class')

	@abstractmethod
	def operation1(self): pass

	@abstractmethod
	def operation2(self): pass


class ConcreteClass1(Abstract):

	def hook(self):
		print('ConcreteClass1 01 implements hook')

	def operation1(self):
		print('operation 1 executed')

	def operation2(self):
		print('operation 2 executed')


class ConcreteClass2(Abstract):

	def operation1(self):
		print('operation 1 executed in the way of ConcreteClass2')

	def operation2(self):
		print('operation 2 executed in the way of ConcreteClass2')


c1 = ConcreteClass1()
c1.tempalte_method()

print(30 * '-')

c2 = ConcreteClass2()
c2.tempalte_method()
