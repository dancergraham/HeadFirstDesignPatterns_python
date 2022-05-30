# Chapter 8: Template design pattern

> **Template Method**: Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.

The template design pattern is widely used in frameworks such as Django, providing base classes which can be extended to provide required methods.

Variants of the template pattern are found throughout the Python object model, for instance iterable sorting is implemented by running the *less than* (`__lt__`) comparison operator between items in the collection. In this sense the [list sorting algorithm](https://docs.python.org/3/howto/sorting.html#odd-and-ends) is a partial implementation of sort, delegating the comparison behavior to individual objects.
