"""
Composite is a design pattern to create composition
to create objects in tree structure.

This pattern allows clients to treat in uniform manner
individual objects (leaf) and objects composition (Composite)

IMPORTANT: only apply this pattern if a tree is the structure
of the composition

In composite pattern, we have two kind of objects:
1. Composite: represet inside nodes of the tree
2. Leaf: represent external nodes of the tree

Composite Objects are complex and have children. Generally,
they delegate job to its childen using a common method

Leaf objects are simple, located at the tip, and withou children. Generally,
these objects perform real job of the application
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class BoxStructure(ABC):
    """Component - Abstract Node (Root or Leaf)
    of the tree"""

    @abstractmethod
    def print_content(self) -> None:
        """Print node (leaf) content"""
        pass

    @abstractmethod
    def get_price(self) -> float:
        """Get node (leaf) price"""
        pass

    def add(self, child: BoxStructure) -> None:
        """break interface segregation
        but it is necessary do this"""
        pass

    def remove(self, child: BoxStructure) -> None:
        """break interface segregation
        but it is necessary do this"""
        pass


class Box(BoxStructure):
    """Composite - Concrete Root (Box) of the tree"""

    def __init__(self, name: str) -> None:
        self.name = name
        self._children: List[BoxStructure] = []

    def print_content(self) -> None:
        print(f"\n{self.name}:")
        for child in self._children:
            child.print_content()

    def get_price(self) -> float:
        return sum([child.get_price() for child in self._children])

    def add(self, child: BoxStructure) -> None:
        self._children.append(child)
        pass

    def remove(self, child: BoxStructure) -> None:
        if child in self._children:
            self._children.remove(child)


class Product(BoxStructure):
    """Leaf node"""

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    def print_content(self) -> None:
        print(self.name, self.price)

    def get_price(self) -> float:
        return self.price


if __name__ == "__main__":
    # Leaf
    tshirt_1 = Product("tshirt 01", 110.00)
    tshirt_2 = Product("tshirt 02", 50.00)
    tshirt_3 = Product("tshirt 03", 40.00)

    tshirt_3.print_content()

    # Composiste
    box_tshirts = Box("Box of tshirts")
    box_tshirts.add(tshirt_1)
    box_tshirts.add(tshirt_2)
    box_tshirts.add(tshirt_3)

    box_tshirts.print_content()

    # Leaf
    smartphone_1 = Product("smartphone 1", 2000)
    smartphone_2 = Product("smartphone 2", 5000)

    # Composite
    box_smartphones = Box("Box of Smartphones")

    box_smartphones.add(smartphone_1)
    box_smartphones.add(smartphone_2)

    box_smartphones.print_content()

    # Composite
    box_root = Box("Root Box")
    box_root.add(box_tshirts)
    box_root.add(box_smartphones)

    box_root.print_content()

    # shold result 7200
    print(box_root.get_price())
