from abc import ABC, abstractmethod


# Abstract Vehicle classes

class LuxVehicle(ABC):
    @abstractmethod
    def search_client(self) -> None: pass


class PopularVehicle(ABC):
    @abstractmethod
    def search_client(self) -> None: pass


# Specialized Vehicle classes for filial 01

class LuxCarFilial01(LuxVehicle):
    def search_client(self) -> None:
        print('LuxCar Filial01 is looking for the client ...')


class LuxMotorcyleFilial01(LuxVehicle):
    def search_client(self) -> None:
        print('LuxMotorcycle Filial01 is looking for the client ...')


class PopularCarFilial01(PopularVehicle):
    def search_client(self) -> None:
        print('PopularCar Filial01 is looking for the client ...')


class PopularMotorcycleFilial01(PopularVehicle):
    def search_client(self) -> None:
        print('PopularMotorcycle Filial01 is looking for the client ...')


# Specialized Vehicle classes for filial 02

class LuxCarFilial02(LuxVehicle):
    def search_client(self) -> None:
        print('LuxCar Filial02 is looking for the client ...')


class LuxMotorcyleFilial02(LuxVehicle):
    def search_client(self) -> None:
        print('LuxMotorcycle Filial02 is looking for the client ...')


class PopularCarFilial02(PopularVehicle):
    def search_client(self) -> None:
        print('PopularCar Filial02 is looking for the client ...')


class PopularMotorcycleFilial02(PopularVehicle):
    def search_client(self) -> None:
        print('PopularMotorcycle Filial02 is looking for the client ...')


# Abstract Factory class

class VehicleFactory(ABC):
    """
    Abstract Vehicle Factory
    """

    """
    get lux and pop vehicles will be overrided
    by the filial. It consider that each filial
    has their own ways/RULES to get lux and pop
    vehicles, like different costs or taxes.
    
    Observ that 'if' is not used in neither of filial
    implementations. It's accourding to open/closed
<<<<<<< HEAD
    SOLID principle
=======
    SOLID principle: open to extension, closed to
    modification
>>>>>>> (creational/factories/abstract_factory.py) some comments, like open/closed SOLID principle
    """
    @staticmethod
    @abstractmethod
    def get_lux_car() -> LuxVehicle: pass

    @staticmethod
    @abstractmethod
    def get_lux_motorcycle() -> LuxVehicle: pass

    @staticmethod
    @abstractmethod
    def get_popular_car() -> PopularVehicle: pass

    @staticmethod
    @abstractmethod
    def get_popular_motorcycle() -> PopularVehicle: pass


# Specialized Factory classes for filial 01

class VehicleFactoryFilial01(VehicleFactory):
    """
    Vehicle Factory of the Filial 01
    """
    @staticmethod
    def get_lux_car() -> LuxVehicle:
        return LuxCarFilial01()
    
    @staticmethod
    def get_lux_motorcycle() -> LuxVehicle:
        return LuxMotorcyleFilial01()
    
    @staticmethod
    def get_popular_car() -> PopularVehicle:
        return PopularCarFilial01()
    
    @staticmethod
    def get_popular_motorcycle() -> PopularVehicle:
        return PopularMotorcycleFilial01()


# Specialized Factory classes for filial 02

class VehicleFactoryFilial02(VehicleFactory):
    """
    Vehicle Factory of the Filial 02
    """
    @staticmethod
    def get_lux_car() -> LuxVehicle:
        return LuxCarFilial02()
    
    @staticmethod
    def get_lux_motorcycle() -> LuxVehicle:
        return LuxMotorcyleFilial02()
    
    @staticmethod
    def get_popular_car() -> PopularVehicle:
        return PopularCarFilial02()
    
    @staticmethod
    def get_popular_motorcycle() -> PopularVehicle:
        return PopularMotorcycleFilial02()


# Client code

class Client():
    def search_clients(self) -> None:
        for factory in [VehicleFactoryFilial01(), VehicleFactoryFilial02()]:

            # lux vehicles
            lux_car = factory.get_lux_car()
            lux_car.search_client()

            lux_motorcycle = factory.get_lux_motorcycle()
            lux_motorcycle.search_client()


            # popular vehicles
            popular_car = factory.get_popular_car()
            popular_car.search_client()

            popular_motorcycle = factory.get_popular_motorcycle()
            popular_motorcycle.search_client()
            

if __name__ == '__main__':
    client = Client()
    client.search_clients()
