# Simple Factory

In POO, the factory term ("fábrica") refers to a class or a method which is responsible for creating objects.

---

### Advantages:
	
- Ables to create a system with low coupling between classes because hide, from client code, the classes wich create the objects.

- Facilitate the edition of new classes to the code, because the client doesn't know and doesn't uses the class implementation (uses the factory).

- Maybe facilitate the process of "cache" or the creation of the "singletons" because the factory can return an object already created to the client instead of create new objects every time that the client needs.

### Disadvantages:
	
- Can introduce too many classes to the code.

---

### Considerations:

- Simple Factory is a kind of parametrized Factory Method.

- Simple Factory cannot be considered a design pattern by itself.

- Simple Factory can broke SOLID principles.
	