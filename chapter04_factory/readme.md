# Chapter 4: Factory patterns

**Simple Factory**: A class which chooses which product class to instantiate and return, based upon method parameters.

**Factory Method**: Defines an interface for creating an object, but lets subclasses decide which class to instantiate. The Factory method lets a class defer instantiation to subclasses.

For instance the `PizzaStore` abstract class in this repo provides an abstract `create_pizza` interface for creating one product.  

**Abstract Factory**: Provides an interface for creating families of related or dependent objects without specifying their concrete classes.

For instance the `PizzaIngredientFactory` abstract class defines an interface for a family of products.
