from abc import ABC, abstractmethod


class Veihcle(ABC):
	"""
	Abstract Veihcle class\
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


class VehicleFactory:
	"""
	Veihcle class (acting as an interface) which represents a taxi company
	"""
	@staticmethod
	def get_vehicle(veihcle_type: str) -> Veihcle:
		if veihcle_type == 'LuxCar':
			return LuxCar()
		if veihcle_type == 'PopularCar':
			return PopularCar()
		if veihcle_type == 'LuxMotorcycle':
			return LuxMotorcycle()
		if veihcle_type == 'PopularMotorcycle':
			return LuxMotorcycle()
		assert 0, 'Vehicle does not exist'


if __name__ == '__main__':

	from random import choice

	available_vehicles = ['LuxCar', 'PopularCar', 'PopularMotorcycle']

	for i in range(10):
		vehicle = VehicleFactory.get_vehicle(choice(available_vehicles))
		vehicle.search_client()
