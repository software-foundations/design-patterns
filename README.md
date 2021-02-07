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

---

# Comportamental

## Strategy

It is a behavioral design pattern which aims to define a family of algorithms, encapsulating each one of the family and turn these interchangeable.

Strategy allows that the algorithm varies independently of the clients that use it.

- The open/closed principle: Entities should be opened to extensions, but closed to modifications

## Observer

The observer design pattern aims to define a dependency 1:n (one to many) between objects, in a way that when an object changes its state, all of its dependents are notified and automatically refreshed

- An observer is an object which would like to be informed
1. update() -> method in observer

- An observable (subject) is the entity which generate informations to be notified to the observer
1. getState() -> method in observable
2. setState() -> method in observable

## Command

Command aims to encapsulate a solicitation as an object,
allowing parametrize clients with different solicitations,
out the solicitations in a queue or register (making a log)
the solicitations and suport operations that can be undone

It is formed for:
- A client (whose orquestrate everything);
- A invoker (that invokes the solicitations);
- One or various command objects (that make the ligation between the receiver and the action to be done);
- A receiver (the object which will executes the action at the end).