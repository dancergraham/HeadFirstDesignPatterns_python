# Chapter 3: Decorator design pattern

> **Decorator**: Attach additional responsibilities to an object dynamically. Decorators provide a flexible alternative
> to subclassing for extending functionality.

I subclass `ABC` and used the `@abstractmethod` decorator from the
`abc` module here but do not use any of this functionality -
it just serves as documentation.

## Use in Python

The python [decorator syntax](https://docs.python.org/3/reference/compound_stmts.html#grammar-token-decorators)
decorator syntax looks quite different as in python you call the _decorated function_ and the decorating function
is automatically called first whereas the _decorating function_ must be called according to the pattern in the book.

## Running the code

```bash
python coffee.py
```

