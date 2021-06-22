from random import randint
from duck import MallardDuck


class DuckAdapter:
    def __init__(self, duck) -> None:
        self.duck = duck
        self.rand = randint

    def gobble(self):
        self.duck.perform_quack()

    def fly(self):
        if self.rand(0, 4) == 0:
            self.duck.perform_fly()


def turkey_test_drive():
    duck = MallardDuck()
    tuckey = DuckAdapter(duck)
    for _ in range(10):
        print("The DuckAdapter says...")
        tuckey.gobble()
        tuckey.fly()


if __name__ == "__main__":
    turkey_test_drive()
