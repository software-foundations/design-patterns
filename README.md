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