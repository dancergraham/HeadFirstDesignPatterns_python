# Chapter 4: Factory patterns

> **Simple Factory**: A class which chooses which product class to instantiate and return, based upon method parameters.

The Python standard library contains multiple references to factory objects, for instances in [dataclasses](https://docs.python.org/3/library/dataclasses.html?highlight=factory)

> **Factory Method**: Defines an interface for creating an object, but lets subclasses decide which class to instantiate. The Factory method lets a class defer instantiation to subclasses.

For instance the `PizzaStore` abstract class in this repo provides an abstract `create_pizza` interface for creating one product.

The [python-qrcode](https://github.com/dancergraham/python-qrcode) module uses the factory method pattern nicely to separate only the part of the code that changes (generating png, svg, etc) from the underlying logic of the code generation and to allow extension through the creation of new factory methods without modification of the existing code.  I took advantage of this to add a new class for the creation of 3D QR codes with my favourite NURBS modelling software Rhino.

> **Abstract Factory**: Provides an interface for creating families of related or dependent objects without specifying their concrete classes.

For instance the `PizzaIngredientFactory` abstract class defines an interface for a family of products.
