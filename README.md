# Head First Design Patterns python code

<img src="images\learning.oreilly.jpg" alt="Head First Design Patterns Second Edition" width="200" align="right">Example code from [Head First Design Patterns second edition](https://www.wickedlysmart.com/head-first-design-patterns/) translated to python to help me understand and memorise the patterns.

I have added examples of pattern usage in the Python standard library and pypi - I am starting to see patterns everywhere!

> **Note**
> I am aiming for a mostly literal translation whilst trying to make the code a little more pythonic by, e.g. using python conventions for `ClassNames` and `method_names` and putting all of the code in a single file where it makes sense to do so.

## Patterns Implemented

- [x] [Strategy](chapter01_strategy)
- [x] [Observer](chapter02_observer)
- [x] [Decorator](chapter03_decorator)
- [ ] [Factory Method](chapter04_factory)
- [ ] [Simple Factory](chapter04_factory)
- [x] [Abstract Factory](chapter04_factory)
- [x] [Singleton](chapter05_singleton)
- [x] [Command](chapter06_command)
- [x] [Adapter](chapter07_adapter_facade)
- [x] [Façade](chapter07_adapter_facade)
- [x] [Template Method](chapter08_template)
- [x] [Iterator](chapter09_iterator_composite)
- [ ] [Composite](chapter09_iterator_composite)
- [x] [State](chapter10_state)
- [ ] Proxy
- [ ] [Model View Controller (MVC)](chapter12_compound)


## Sample Code : Java

From the book 📖:
 
```java
package headfirst.designpatterns.strategy;

public abstract class Duck {
    FlyBehavior flyBehavior;
    QuackBehavior quackBehavior;

    public Duck() {
    }

    public void setFlyBehavior(FlyBehavior fb) {
        flyBehavior = fb;
    }

    public void setQuackBehavior(QuackBehavior qb) {
        quackBehavior = qb;
    }

    abstract void display();

    public void performFly() {
        flyBehavior.fly();
    }

    public void performQuack() {
        quackBehavior.quack();
    }

    public void swim() {
        System.out.println("All ducks float, even decoys!");
    }
}
```

### Sample Code : Python 🐍

From this repository :

```python
class Duck():
    _fly_behavior = None
    _quack_behavior = None

    def set_fly_behavior(self, fly_behavior):
        self._fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior):
        self._quack_behavior = quack_behavior

    def display(self):
        raise NotImplementedError

    def perform_fly(self):
        self._fly_behavior.fly()

    def perform_quack(self):
        self._quack_behavior.quack()

    def swim(self):
        print("All ducks float, even decoys! 〰🦆〰")
```

## Object Oriented Design Principles

- Encapsulate what varies
- Open-Closed Principle: Open for extension, closed for modification
- Program to an interface, not to an implementation
- Favour composition over inheritence
- Dependency Inversion Principle
- Depend upon abstractions
- The Hollywood Principle : _"Don't call us, we'll call you"_
- One Class, One Responsibility Principle
- Single Responsibility Principle
- Principle of Least Knowledge

## Model View Controller (MVC)

I started to work on the MVC pattern here but have a [small complete MVC implementation in JavaScript](https://github.com/dancergraham/HeadFirstJs/blob/master/battleship2D.js) in another repo. 
