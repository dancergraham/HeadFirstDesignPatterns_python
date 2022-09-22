# Chapter 7: Adapter and Facade design patterns

I find myself using the adapter and facade patterns a lot when refactoring existing code. I know how I want it to work
and I know how it works now, but I don't have time _right now_ to fix it, so I add an adapter or facade to give it a clean
interface and I only change the underlying code if I need to make significant changes to the underlying implementation.

> **Adapter**: Converts the interface of a class into another interface the clients expect. Adapter lets classes work
> together that couldn't otherwise because of incompatible interfaces.

Compiled C modules in Python could be seen as examples of the adapter pattern: the Python implementation provides an
interface for python code to work with the incompatible underlying C code.

> **Facade**: Provides a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level
> interface that makes the subsystem easier to use.

The [pathlib](https://github.com/python/cpython/blob/main/Lib/pathlib.py) Python library provides a simplified
high-level cross-platform interface to methods and attributes from the `os`, `sys`, `io` and other modules.

## Running the code

```bash
python duck.py
```
