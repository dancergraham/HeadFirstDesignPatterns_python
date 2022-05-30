# Chapter 7: Adapter and Façade design patterns

> **Adapter**: Converts the interface of a class into another interface the clients expect. Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.

Compiled C modules in Python could be seen as examples of the adapter pattern: the Python implementation provides an interface for python code to work with the incompatible underlying C code.

> **Façade**: Provides a unified interface to a set of interfaces in a subsystem.  Façade defines a higher-level interface that makes the subsystem easier to use.

The [pathlib](https://github.com/python/cpython/blob/main/Lib/pathlib.py) Python library provides a simplified high-level cross-platform interface to methods and attributes from the `os`, `sys`, `io` and other modules.
 