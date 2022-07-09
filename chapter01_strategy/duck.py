class FlyBehavior:
    def fly(self):
        raise NotImplementedError


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!!")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly")


class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket!'")


class QuackBehavior:
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


class Duck:
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
        print("All ducks float, even decoys!")


class MallardDuck(Duck):
    _fly_behavior = FlyWithWings()
    _quack_behavior = Quack()

    def display(self):
        print("I'm a real Mallard duck")


class ModelDuck(Duck):
    _fly_behavior = FlyNoWay()
    _quack_behavior = Squeak()

    def display(self):
        print("I'm a real Mallard duck")


def mini_duck_simulator():
    mallard = MallardDuck()
    mallard.perform_quack()
    mallard.perform_fly()

    model = ModelDuck()
    model.perform_fly()
    model.set_fly_behavior(FlyRocketPowered())
    model.perform_fly()


if __name__ == "__main__":
    mini_duck_simulator()
