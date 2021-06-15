# Chapter 3: Decorator design pattern

> **Decorator**: Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.

Not quite the same as python decorator syntax as in python you call the _decorated function_ and the decorating function is called first whereas the _decorating function_ must be called here.

I subclass `ABC` and used the `@abstractmethod` decorator from the `abc` module here but do not use any of this functionality - it just serves as documentation.