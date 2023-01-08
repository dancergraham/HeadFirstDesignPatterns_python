# Chapter 7: Adapter and Facade design patterns

> **Adapter**: Converts the interface of a class into another interface the clients expect. Adapter lets classes work
> together that couldn't otherwise because of incompatible interfaces.

Compiled C modules in Python could be seen as examples of the adapter pattern: the Python implementation provides an
interface for python code to work with the incompatible underlying C code.

I find the adapter pattern useful when using external libraries like skipy spatial to support my own code. 
I want features from the external library but I want to use it with my own objects and the library api doesnt
exactly fit my own. I write a small adapter to make the external library feel right and work well with my own 
objects.

> **Facade**: Provides a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level
> interface that makes the subsystem easier to use.

I also find myself using the adapter and facade patterns a lot when refactoring existing code. I know how I want it to work
and I know how it works now, but I don't have time _right now_ to fix it, so I add an adapter or facade to give it a clean
interface and I make a plan to change the underlying code when it suits me.

The [pathlib](https://github.com/python/cpython/blob/main/Lib/pathlib.py) Python library provides a simplified
high-level cross-platform interface to methods and attributes from the `os`, `sys`, `io` and other modules.

## Running the code

```bash
python duck_adapter.py
```
