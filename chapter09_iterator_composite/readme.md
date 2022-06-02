# Chapter 9: Iterator and Composite design patterns

> **Iterator Method**: provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

Java offers either the "Look Before You Leap" (LBYL) philosophy or the "Easier to Ask for Forgiveness than for Permission"(EAFP) with its [`iterator`](https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html) interface: The former involves calling `hasNext()` prior to calling `next()` whilst the latter uses the more recent `forEachRemaining()` method.

Iteration is built in to the Python object model.

Python requires only the `__iter__()` method to be implemented for an object to return `True` to `isinstance(obj, Iterable)`, however if an object implements just `__getitem__()` without `__iter__` then it will function as an iterable in Cpython!

> **Composite Pattern**: allows you to compose objects into tree structures to represent whole-part hierarchies.  Composite lets clients treat individual objects and compositions of objects uniformly.
