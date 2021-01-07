from abc import ABC, abstractmethod


class Veihcle(ABC):
	"""
	Abstract Veihcle class
	"""
	@abstractmethod
	def search_client(self) -> None: pass


class LuxCar(Veihcle):
	def search_client(self) -> None:
		print('Lux Car is looking for the client')


class PopularCar(Veihcle):
	def search_client(self) -> None:
		print('Popular Car is looking for the client')


class PopularMotorcycle(Veihcle):
	def search_client(self) -> None:
		print('Popular Motorcycle is looking for the client')


class LuxMotorcycle(Veihcle):
	def search_client(self) -> None:
		print('Lux Motorcycle is looking for the client')


class VehicleFactory(ABC):
	"""
	Headquarter enterprise wich defines the business rules
	"""
	def __init__(self, veihcle_type) -> None:
		self.vehicle = self.get_vehicle(veihcle_type)		

	@staticmethod
	@abstractmethod
	def get_vehicle(veihcle_type: str) -> Veihcle:
		"""
		The get vehicle will be implemented and overrided
		by the subclasses of VehicleFactory
		"""
		pass

	def search_client(self) -> None:
		"""
		This is the wrapper which envolves the
		search_client() method of the
		Vehicle object
		This is the same of the simple factory 2
		"""
		self.vehicle.search_client()


class Afiliated01VehicleFactory(VehicleFactory):
	"""
	Afiliated 01 dicide how objects can be created
	"""

	@staticmethod	
	def get_vehicle(veihcle_type: str) -> Veihcle:
		"""
		Overrides the get_vehicle() method
		of the Vehicle factory
		"""
		if veihcle_type == 'LuxCar':
			return LuxCar()
		if veihcle_type == 'PopularCar':
			return PopularCar()
		if veihcle_type == 'LuxMotorcycle':
			return LuxMotorcycle()
		if veihcle_type == 'PopularMotorcycle':
			return LuxMotorcycle()
		assert 0, 'Vehicle does not exist'


class Afiliated02VehicleFactory(VehicleFactory):
	"""
	Afiliated 02 dicide how objects can be created
	"""

	@staticmethod	
	def get_vehicle(veihcle_type: str) -> Veihcle:
		"""
		Overrides the get_vehicle() method
		of the Vehicle factory
		"""

		if veihcle_type == 'PopularCar':
			return PopularCar()
		assert 0, 'Vehicle does not exist'


if __name__ == '__main__':
	from random import choice

	print('\n', 10 * '_' ,'Afiliated 01', 10 * '_')
	available_vehicles_afiliated_01 = ['LuxCar', 'PopularCar', 'LuxMotorcycle', 'PopularMotorcycle']
	for i in range(10):
		vehicle = Afiliated01VehicleFactory(choice(available_vehicles_afiliated_01))
		vehicle.search_client()

	print('\n', 10 * '_' ,'Afiliated 02', 10 * '_')
	available_vehicles_afiliated_02 = ['PopularCar']
	for i in range(10):
		vehicle = Afiliated02VehicleFactory(choice(available_vehicles_afiliated_02))
		vehicle.search_client()
