# Chapter 8: Template design pattern

> **Template Method**: Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.

Variants of the template pattern are found throughout the Python object model, for instance iterable sorting is implemented by running the *less than* (`__lt__`) comparison operator between items in the collection. In this sense the [list sorting algorithm](https://docs.python.org/3/howto/sorting.html#odd-and-ends) is a partial implementation of sort, delegating the comparison behavior to individual objects.

## Template method in Django

The template design pattern is widely used in frameworks such as Django, providing base classes which can be extended to provide required methods. For instance the [`full_clean`](https://github.com/django/django/blob/0dd29209091280ccf34e07c9468746c396b7778e/django/forms/forms.py#L424) method on Django forms runs the `_clean_fields()`, `self._clean_form()` and `self._post_clean()` methods, the latter of which is a *hook* for additional model validation and cleaning after the built-in validation logic has been applied.    

## Running the code

```bash
python barista.py
```
