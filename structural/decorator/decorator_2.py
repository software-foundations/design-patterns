"""
Decorator is a structural design pattern wich allows add
new behaviors in objects by put them inside of a "wrapper"
(decorator) of objects

Decorators provide an flexible alternative by the use of
subclasses for the functionality extension

Decorator (design pattern) != Python decorator

Python decorator -> A decorator is a callable wich accepts
other function as argument (a decorated function). The
decorator can realize some processing within the decorated
function and wrapper it or change by another function or
invocable object (RAMALHO, 2015, p. 223)
"""
from __future__ import annotations
from abc import abstractmethod, ABC
from dataclasses import dataclass
from typing import List
from copy import deepcopy

# Dataclasses don't work well with inheritance
# We will use prototype pattern within decorators


# INGREDIENTS
@dataclass
class Ingredient:
    """Ingredient"""
    price: float


@dataclass
class Bread(Ingredient):
    """Ingredient Specialization"""
    price: float = 1.50


@dataclass
class Sausage(Ingredient):
    """Ingredient Specialization"""
    price: float = 4.99


@dataclass
class Bacon(Ingredient):
    """Ingredient Specialization"""
    price: float = 7.99


@dataclass
class Egg(Ingredient):
    """Ingredient Specialization"""
    price: float = 1.50


@dataclass
class Cheese(Ingredient):
    """Ingredient Specialization"""
    price: float = 6.35


@dataclass
class MashedPotatoes(Ingredient):
    """Ingredient Specialization"""
    price: float = 2.25


@dataclass
class PotatoSticks(Ingredient):
    """Ingredient Specialization"""
    price: float = 0.99


# HOT-DOGS


class Hotdog:
    """A concrete class and a abstract class
    for Special Hotdog"""

    _name: str
    _ingredients: List[Ingredient]

    @property
    def price(self) -> float:
        """Calculate Hotdog Price, considering its ingredients"""
        return round(
            sum([ingredient.price for ingredient in self._ingredients]), 2)

    @property
    def name(self) -> str:
        """Hotdog name property
        :return: str"""
        return self._name

    @property
    def ingredients(self) -> List[Ingredient]:
        """"Hotdog ingredients property
        :return: List[Imgredient]"""
        return self._ingredients

    def __repr__(self) -> str:
        """representation of the object
        :return: string"""
        return f'{self.name}({self.price}) -> {self.ingredients}'


class SpecialHotdog(Hotdog):
    """Hotdog specialization"""

    def __init__(self) -> None:
        self._name: str = "SpecialHotdog"
        self._ingredients: List[Ingredient] = [
            Bread(),
            Cheese(),
            Egg(),
            MashedPotatoes(),
            PotatoSticks(),
            Sausage()
        ]


class SimpleHotdog(Hotdog):
    """Hotdog specialization"""

    def __init__(self) -> None:
        self._name: str = "SimpleHotDog"
        self._ingredients: List[Ingredient] = [
            Bread(),
            PotatoSticks(),
            Sausage()
        ]


# And about custom hotdogs?
# Use ONE decorator to do that
class HotdogDecorator(Hotdog):
    """Hotdog Decorator"""

    def __init__(self, hotdog: Hotdog, ingredient: Ingredient) -> None:
        self.hotdog = hotdog
        self._ingredient = ingredient

        self._ingredients = deepcopy(self.hotdog.ingredients)
        self._ingredients.append(self._ingredient)

    @property
    def name(self) -> str:
        return f'{self.hotdog.name} + {self._ingredient.__class__.__name__}'


if __name__ == "__main__":

    special_hotdog = SpecialHotdog()

    simple_hotdog = SimpleHotdog()

    bacon_simple_hotdog = HotdogDecorator(simple_hotdog, Bacon())

    egg_bacon_simple_hotdog = HotdogDecorator(bacon_simple_hotdog, Egg())

    mashed_potatoes_eggs_bacon_simple_hotdog = HotdogDecorator(
        egg_bacon_simple_hotdog, MashedPotatoes())

    print(special_hotdog)

    print(simple_hotdog)

    print(bacon_simple_hotdog)

    print(egg_bacon_simple_hotdog)

    print(mashed_potatoes_eggs_bacon_simple_hotdog)
