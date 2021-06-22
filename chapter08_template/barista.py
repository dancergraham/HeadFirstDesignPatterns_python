class CaffeineBeverage:
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def brew(self):
        raise NotImplementedError

    def add_condiments(self):
        raise NotImplementedError

    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring into cup")


class Tea(CaffeineBeverage):
    def brew(self):
        print("Steeping the tea")

    def add_condiments(self):
        print("Adding Lemon")


class Coffee(CaffeineBeverage):
    def brew(self):
        print("Dripping Coffee through filter")

    def add_condiments(self):
        print("Adding Sugar and Milk")


def beverage_test_drive():
    tea = Tea()
    coffee = Coffee()
    print("\nMaking tea...")
    tea.prepare_recipe()
    print("\nMaking coffee...")
    coffee.prepare_recipe()


if __name__ == "__main__":
    beverage_test_drive()
