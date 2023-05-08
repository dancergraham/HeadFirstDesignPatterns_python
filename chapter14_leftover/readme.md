# Chapter 14: Leftover Patterns

> **Manager Pattern**: _(Bonus pattern)_ Manages multiple entities of the same or similar type.

Unlike the factory patterns which handle object creation or the
mediator pattern which handles interaction between related objects, the 
manager pattern has the role of managing multiple identical or related objects.

For example in the Python standard library the [`Manager` object](https://docs.python.org/3/library/multiprocessing.html#multiprocessing.Manager)
in the `multiprocessing` library manages shared objects between child
processes.