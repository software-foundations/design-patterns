from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
	def __init__(self, \
		total: float, discount: DiscountStrategy):
		self._total = total
		self._discount = discount

	@property
	def total(self):
		return self._total
	
	@property
	def total_with_discount(self):
		return self._discount.calculate(self.total)


class DiscountStrategy(ABC):
	@abstractmethod
	def calculate(self, value: float) -> float: pass


class TwentyPercent(DiscountStrategy):
	def calculate(self, value: float) -> float:
		return value * (1 - 0.2)


class FiftyPercent(DiscountStrategy):
	def calculate(self, value: float) -> float:
		return value * (1 - 0.5)


class NoDiscount(DiscountStrategy):
	def calculate(self, value: float) -> float:
		return value

class CustomDiscount(DiscountStrategy):
	def __init__(self, discount):
		self.discount = discount / 100

	def calculate(self, value: float) -> float:
		return value * (1 - self.discount)


if __name__ == '__main__':
	twenty_percent = TwentyPercent()
	fifty_discount = FiftyPercent()
	no_discount = NoDiscount()	
	custom_discount = CustomDiscount(discount=5)

	order = Order(1000, twenty_percent)
	print(order.total, order.total_with_discount)

	order = Order(1000, fifty_discount)
	print(order.total, order.total_with_discount)

	order = Order(1000, no_discount)
	print(order.total, order.total_with_discount)

	order = Order(1000, custom_discount)
	print(order.total, order.total_with_discount)

	order = Order(1000, CustomDiscount(80))
	print(order.total, order.total_with_discount)
