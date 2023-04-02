# Chapter 2: Observer design pattern

> **Observer**: defines a one-to-many dependency between objects so that when one object changes state, all of its
> dependents are notified and updated automatically.

A very useful design pattern, often used in user interfaces
and as part of the popular Model-View-Controller (MVC) pattern used,
for instance, in Django.
As I wrote out the code I found it very appealing that I did not need
to change the subject at all to add new observers.

### Class Diagram

```mermaid

classDiagram

    Subject --> Observer : observers
    Subject1 <-- Observer1 : subject
    Subject1 <-- Observer2 : subject
    Subject <|-- Subject1
    Observer <|-- Observer1
    Observer <|-- Observer2
    Subject : attach(o)
    Subject : detach(o)
    Subject: notify()
    class Observer{
      update()
    }
    class Subject1{
      state
      get_state()
      set_state()
    }
    class Observer1{
        state
        update()
    }
        class Observer2{
        state
        update()
    }

```

## Running the code

```bash
python weather.py
```
