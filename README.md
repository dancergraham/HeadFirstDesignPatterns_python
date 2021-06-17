# HeadFirstDesignPatterns_python

<img src="images\learning.oreilly.jpg" alt="Girl in a jacket" width="200" align="right">Example code from [Head First Design Patterns second edition](https://www.wickedlysmart.com/head-first-design-patterns/) translated to python to help me understand and memorise the patterns.  

I am aiming for a literal translation without trying to make the code pythonic beyond, e.g. using python conventions for `ClassNames` and `method_names` and putting all of the code in a single file where it makes sense to do so.

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
    fly_behavior = None
    quack_behavior = None

    def set_fly_behavior(self, fly_behavior):
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior):
        self.quack_behavior = quack_behavior

    def display():
        raise NotImplementedError

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def swim():
        print("All ducks float, even decoys! 〰🦆〰")
```
