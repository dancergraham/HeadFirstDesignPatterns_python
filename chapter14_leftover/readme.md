# Chapter 14: Leftover Patterns

> **Manager Pattern**: _(Bonus pattern)_ Manages multiple entities of the same or similar type.

Unlike the factory patterns which handle object creation or the
mediator pattern which handles interaction between related objects, the 
manager pattern has the role of managing multiple identical or related objects.

For example in the Python standard library the [`Manager` object](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Manager)
in the `multiprocessing` library manages shared objects and child processes.
It keeps track of the running processes, shared objects and the available methods
on those objects. Without a `Manager` object, multiple processes could try to access
or modify shared objects at the same time with unpredictable results.  
It uses the `Proxy` design pattern, providing a proxy to the shared objects, to help 
achieve this, passing messages and data across process boundaries.
