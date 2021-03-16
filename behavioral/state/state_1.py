"""
author: Bruno Conde Costa da Silva
"""

from __future__ import annotations
from abc import ABC, abstractmethod

class Order():
	""" Context """

	def __init__(self) -> None:
		self.state: OrderState = PaymentPending(self)

	def pending(self) -> None:
		print('Trying to execute pending()')
		self.state.pending()
		print('Current state: {}'.format(self.state))
		print()

	def approve(self) -> None:
		print('Trying to execute approve()')
		self.state.approve()
		print('Current state: {}'.format(self.state))
		print()

	def reject(self) -> None:
		print('Trying to execute reject()')
		self.state.reject()
		print('Current state: {}'.format(self.state))
		print()


class OrderState(ABC):
	def __init__(self, order: Order) -> None:
		self.order = order

	@abstractmethod
	def pending(self) -> None: pass

	@abstractmethod
	def approve(self) -> None: pass

	@abstractmethod
	def reject(self) -> None: pass

	def __str__(self) -> str:
		return self.__class__.__name__



class PaymentPending(OrderState):

	def pending(self) -> None:
		print('Payment already pending. We cannot doing anything')
	
	def approve(self) -> None:
		self.order.state = PaymentApprove(self.order)
		print('Payment approved')
	
	def reject(self) -> None:
		self.order.state = PaymentReject(self.order)
		print('Payment rejected')


class PaymentApprove(OrderState):

	def pending(self) -> None:
		self.order.state = PaymentPending(self.order)
		print('Payment pending')
	
	def approve(self) -> None:
		print('Payment already approved. We cannot doing anything')
	
	def reject(self) -> None:
		self.order.state = PaymentReject(self.order)
		print('Payment rejected')


class PaymentReject(OrderState):

	def pending(self) -> None:
		print('Payment rejected. We cannot move to pending')
	
	def approve(self) -> None:
		print('Payment rejected. We cannot move to approved')
	
	def reject(self) -> None:
		print('Payment already rejected. We cannot move to rejected')


if __name__ == "__main__":
	order = Order()
	order.pending()
	order.approve()
	order.pending()
	order.reject()
	order.pending()
	order.approve()	
