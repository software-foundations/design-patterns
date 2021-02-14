from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class IObservable(ABC):
	""" Observable Interface"""

	@property
	@abstractmethod
	def state(self):
		return self._state

	@abstractmethod
	def add_observer(self, observer: IObserver) -> None: pass

	@abstractmethod
	def remove_observer(self, observer: IObserver) -> None: pass

	@abstractmethod
	def notify_observers(self) -> None: pass


class WeatherStation(IObservable):
	""" Observable """
	def __init__(self):
		self._observers: List[IObserver] = []
		self._state: Dict = {}

	@property
	def state(self):
		return self._state
	
	@state.setter
	def state(self, state_update: Dict) -> None:
		new_state = {**self._state, **state_update}

		if new_state != self._state:
			self._state = new_state
			self.notify_observers()

	def reset_state(self):
		self._state = {}
		self.notify_observers()

	def add_observer(self, observer: IObserver) -> None:
		self._observers.append(observer)

	def remove_observer(self, observer: IObserver) -> None:

		if observer not in self._observers:
			return

		self._observers.remove(observer)

	def notify_observers(self) -> None:
		for observer in self._observers:
			observer.update()
			print()


class IObserver(ABC):
	""" Observer Interface"""
	@abstractmethod
	def update(self) -> None: pass


class Smartphone(IObserver):
	def __init__(self, name, observable: IObservable) -> None:
		self.name = name
		self.observable = observable

	def update(self) -> None:
		observable_name = self.observable.__class__.__name__
		print(f'{self.name} the object {observable_name} \
			was updated => ', end='')
		print(f'{self.observable.state}')


class Notebook(IObserver):
	def __init__(self, observable: IObservable) -> None:		
		self.observable = observable

	def show(self):
		state = self.observable.state
		print('I am the notebook and i will another thing' + \
			' with the state update. ', state)

	def update(self) -> None:
		self.show()

if __name__ == "__main__":
	weather_station = WeatherStation()

	smartphone_1 = Smartphone('Samsung', weather_station)
	smartphone_2 = Smartphone('iPhone', weather_station)
	notebook = Notebook(weather_station)

	weather_station.add_observer(smartphone_1)
	weather_station.add_observer(smartphone_2)
	weather_station.add_observer(notebook)

	weather_station.state = {'temperature': '30'}
	weather_station.state = {'humidity': '60'}

	weather_station.remove_observer(smartphone_2)
	weather_station.reset_state()

	weather_station.state = {'temperature': '40', 'humidity': '90'}




	# empty dictionaries doesn't update the state, because there are no 
	# arguments to unpack

	weather_station.state = {}
	weather_station.state = {}
	weather_station.state = {}
	weather_station.state = {}
	weather_station.state = {}
	weather_station.state = {}