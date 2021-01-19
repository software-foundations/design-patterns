# Design Patterns

Common design patterns

---

# Creational

Create objects

## Factories

- Simple Factory
- Factory Method
- Abstract Factory

## Singleton

- with decorator (@singleton)
- with classes (using __call__ and executes __init__ only when instantiate)

## Monostate (a singleton variation developed by Alex Martelli)

It is to ensure that all instances have a class share the same value of state

## Builder

Builder is a creational pattern which aims to separate the construction of an complex object of its representation, so that the same process of construction can bre create different representations.

Builder gives the possibility to create objects step by step and this is already possible in python without the builder design pattern itself.

Generally builder accepts to chain methods

## Prototype

- Especify the type of the objects to be created
using an instance-prototype
- Create new objects using this prototype instance

Wich objects are copiated with the attribution signal
1. imutable objects (copied)
1.1 bool
1.2 init
1.3 float
1.4 tuple
1.5 str

Wich objects aren't copiated with the attribution signal, pointing to the same memory position

1. mutable objects (passed by reference)
1.1 list
1.2 set
1.3 dict
1.4 class (the user can change it)
