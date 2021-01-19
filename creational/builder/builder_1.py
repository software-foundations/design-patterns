from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class StringReprMixin:
    def __str__(self) -> str:
        params = ', '.join(
            [f'{k}={v}' for k, v in self.__dict__.items()]
        )
        return f'{self.__class__.__name__}({params})'

    def __repr__(self) -> str:
        return self.__str__()

# Class to be instantiated
class User(StringReprMixin):
    def __init__(self) -> None:
        self.firstname: str = None
        self.lastname: str = None
        self.age: int = None
        self.phone_numbers: List = []
        self.addresses: List = []

# Interface of User Builder
# Interface/Abstract class has abstract methods
# Doesn't have __init__ because it is an interface/abstract class
class IUserBuilder(ABC):
    """
    Methods to be specializated by the builder instance
    """
    @property
    @abstractmethod
    def result(self) -> User: pass

    @abstractmethod
    def add_firstname(self, firstname) -> UserBuilder: pass

    @abstractmethod
    def add_lastname(self, lastname) -> UserBuilder: pass

    @abstractmethod
    def add_age(self, age) -> UserBuilder: pass

    @abstractmethod
    def add_phone(self, phone) -> UserBuilder: pass

    @abstractmethod
    def add_address(self, address) -> UserBuilder: pass

# Builder of User
class UserBuilder(IUserBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._result = User() # The user instance to be returned

    @property
    def result(self) -> User: # overrides the result of the abstract class
        """
        Every time it is called, return the User instance itself
        and instantiate a new User object and storage it in
        the self._result (agregation, a kind of association)
        """
        return_data = self._result
        self.reset() # Reset The User instance to be returned
        return return_data

    """
    implement the abstract methods defined in IUserBuilder(ABC)
    with the same signature
    """
    
    """ return self -> it is to anable to chain methods at the UserDirector class (a kind of an User class, not a subclass)

    Returning the object, it is possible to invoque other methods in chain
    at the same object
    """
    def add_firstname(self, firstname) -> UserBuilder:
        self._result.firstname = firstname
        return self

    def add_lastname(self, lastname) -> UserBuilder:
        self._result.lastname = lastname
        return self

    def add_age(self, age) -> UserBuilder:
        self._result.age = age
        return self

    def add_phone(self, phone) -> UserBuilder:
        self._result.phone_numbers.append(phone)
        return self

    def add_address(self, address) -> UserBuilder:
        self._result.addresses.append(address)
        return self

# Instantiate a Directory User (kind of User, but not a subclass of user)
class UserDirector:
    def __init__(self, builder: UserBuilder) -> None:
        self._builder = builder # Receives the builder of the user

    # Returns a User (of Directory kind) with age
    def with_age(self, firstname, lastname, age) -> User:
        # chaining methods (obj.method1.method2 ...)
        self._builder.add_firstname(firstname)\
            .add_lastname(lastname)\
            .add_age(age)
        return self._builder.result # return the object creacted with firstname, last_name and age and clear it of the memory of the UserBuilder instance (in fact, remove the recently created and create a new empty User instance)

    # Returns a User (of Director kind) with address
    def with_address(self, firstname, lastname, address) -> User:
        # chaining methods (obj.method1.method2 ...)        
        self._builder.add_firstname(firstname)\
            .add_lastname(lastname)\
            .add_address(address)
        return self._builder.result


if __name__ == "__main__":
    user_builder = UserBuilder() # The builder of the user
    user_director = UserDirector(user_builder) # The builder of the Director
    user1 = user_director.with_age('Luiz', 'Otávio', 30) # Build a Director User with age
    user2 = user_director.with_address('Maria', 'Miranda', 'Av Brasil') # Build a Director user with address
    print(user1)
    print(user2)
