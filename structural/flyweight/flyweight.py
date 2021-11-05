"""
- Share objects
- Substitute many objects by few shared objects
- Share intrinsic (not change) state
- Does not share extrinsic states

All these Conditions must be satfied to use flywitgh
1. A application shares a too many objetcs
2. The cousts of storaging are high due to large amount of objects
3. The major states of the objects can intrisic
4. Many objects can be replaced by fex shared objetcs
5. The application does'nt depends on the object id
"""
from __future__ import annotations
from typing import List, Dict


class Client:
    """Context"""

    def __init__(self, name: str) -> None:
        self.name = name
        self._addresses: List = []

        # Extrinsic address data
        self.address_number: str
        self.address_detail: str

    def add_address(self, address: Address) -> None:
        """append client address"""
        self._addresses.append(address)

    def list_addresses(self) -> None:
        """list client addresses"""
        for address in self._addresses:
            address.show_address(self.address_number, self.address_detail)


class Address:
    """Flyweight"""

    def __init__(self, street: str, neighborhood: str, zip_code: str) -> None:
        """"""
        self._street = street
        self._neighborhood = neighborhood
        self._zip_code = zip_code

    def show_address(self, address_number: str, address_detail: str) -> None:
        """show client address in terminal"""
        print(
            self._street,
            address_number,
            self._neighborhood,
            address_detail,
            self._zip_code,
        )

    def __str__(self):
        return f"<{self.__class__.__name__}> object"

    def __repr__(self):
        return self.__str__()


class AddressFactory:
    """Address Factory"""

    _addresses: Dict = {}

    @staticmethod
    def _get_key(**kwargs) -> str:
        """"""
        return "".join(kwargs.values())

    def get_address(self, **kwargs):
        """Get address by access a created object
        or creating a new object"""
        key = self._get_key(**kwargs)

        try:
            address_flyweight = self._addresses[key]
            print("Using created object")

        except KeyError:
            print("Creating new object")
            address_flyweight = Address(**kwargs)
            self._addresses[key] = address_flyweight

        return address_flyweight

    def __str__(self):
        return f"<{self.__class__.__name__}> object"

    def __repr__(self):
        return self.__str__()


if __name__ == "__main__":

    address_factory = AddressFactory()

    a1 = address_factory.get_address(
        street="Av Brasil", neighborhood="Centro", zip_code="0000000-000"
    )

    a2 = address_factory.get_address(
        street="Av Brasil", neighborhood="Centro", zip_code="0000000-000"
    )

    bruno_client = Client(name="Bruno")
    bruno_client.address_number = "50"
    bruno_client.address_detail = "Home"
    bruno_client.add_address(a1)
    bruno_client.list_addresses()

    joana_client = Client(name="Joana")
    joana_client.address_number = "30"
    joana_client.address_detail = "Work"
    joana_client.add_address(a2)
    joana_client.list_addresses()

    print(a1 == a2)
