# Chapter 9: Iterator and Composite design patterns

> **Iterator Method**: provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.

Python requires only the `__iter__()` method to be implemented for an object to return `True` to `isinstance(obj, Iterable)`, however if an object implements just the `__getitem__()` without `__iter__` method then it will work as an  iterable!

> **Composite Pattern**: allows you to compose objects into tree structures to represent whole-part hierarchies.  Composite lets clients treat individual objects and compositions of objects uniformly.

A pythonic alternative would be to:

```python
try: 
    composition_method()
except CompositionMethodError:
    individual_method()
```
