# Chapter 6: Command design pattern

> **Command**: Encapsulates a request as an object, thereby letting you parameterise clients with different requests, queue or log requests, and support undoable operations.

## Use in Python

[Threading](https://docs.python.org/3/library/threading.html) In the Python standard library follows the command design pattern: The _Client_ is the main thread and the _receiver_ is the target thread.  The _Command_ is a callable Python object which is executed by calling its `__call__()` method. The _Invoker_ is the `Thread` instance and its `run()` method is equivalent to calling _execute_ in the Command pattern. `Thread`'s `run` method can be overridden in subclasses to customise the functionality beyond simply providing a function and input `args` and `kwargs`.
