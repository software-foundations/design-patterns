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

# Behavioral

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

## Template

Template Method (behavioral) aims to define an algorithm in a method, postponing some steps to the subclasses by inheritance.

Template method allows the subclasses some steps of an algorithm without changes its structure

It is also possible to define hooks for the subclasses use whenever they have to.

The Hollywood principle: "Don't Call Us, We'll Call You!"
(IoC - Inversion of Control)

## State

State aims (behavioral) aims to allow an object change its behavior when some internal state changes

The object seams change its class

## Chain of responsibility

Chain of responsibility (COR) is a behavioral pattern which aims to avoid the
coupling of the sender of a request to the receiver by giving the responsability
of treat the solicitation for more than one object.

Chain the receiver objects passing the request along the chain ultil an object
treat the request.

In essence, a handler first receive the request and try to solve that and if it
solve it, it send back the response, else, it pass the request to other handler
who problably know to solve it and if it solve it, else, it pass the request to
other request ... At the end, the request will be answered by one of the
handlers.

## Mediator

<div style="text-align:justify;">
	<p>Mediator is a behavioral design pattern which aims to define an object which encapsulates the way of a set of objects interact to each other</p>
	<p>The mediator promote low accopling by avoiding that objects explicitly refers to each other, and allow many interactions regardless</p>
</div>

# Structural

## Proxy

- Proxy is a Class with the same interface of another
- Proxy seams (but far) to decorator
- Use proxy object instead of real object
- Kinds of proxy
    1. virtual: controll resource access
    2. remote: control remote resource access
    3. protection: control resource protection
    4. inteligence: increase inteligence in resource access

- Proxy can do many things:
    1. Authenticate users
    2. Create logs
    3. Distribute services
    4. Create cache
    5. Create and destroy objects
    6. Postpone