
class FlyBehavior():
    def fly(self):
        raise NotImplementedError


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!!")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly")


class QuackBehavior():
    def quack(self):
        raise NotImplementedError


class Quack(QuackBehavior):
    def quack(self):
        print("Quack")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")


class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")


class Duck():
    def display():
        raise NotImplementedError

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()


class MallardDuck(Duck):
    quack_behavior = Quack()
    fly_behavior = FlyWithWings()

    def display(self):
        print("I'm a real Mallard duck")


def mini_duck_simulator():
    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()


if __name__ == '__main__':
    mini_duck_simulator()
