# Chapter 8: Iterator design pattern

> **Template Method**: provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

Python requires only the `__iter__()` method to be implemented for an object to return `True` to `isinstance(obj, Iterable)`, however if an object implements the `__getitem__()` method then it will be iterable.