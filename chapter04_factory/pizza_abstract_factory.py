import abc


class Cheese(abc.ABC):
    def __str__(self):
        raise NotImplementedError


class MozzarellaCheese(Cheese):
    def __str__(self):
        return "Shredded Mozzarella"


class ParmesanCheese(Cheese):
    def __str__(self):
        return "Shredded Parmesan"


class ReggianoCheese(Cheese):
    def __str__(self):
        return "Reggiano Cheese"


class Dough(abc.ABC):
    def __str__(self):
        raise NotImplementedError


class ThickCrustDough(Dough):
    def __str__(self):
        return "ThickCrust style extra thick crust dough"


class ThinCrustDough(Dough):
    def __str__(self):
        return "Thin Crust Dough"


class Clams(abc.ABC):
    def __str__(self):
        raise NotImplementedError


class FreshClams(Clams):
    def __str__(self):
        return "Fresh Clams from Long Island Sound"


class FrozenClams(Clams):
    def __str__(self):
        return "Frozen Clams from Chesapeake Bay"


class Sauce(abc.ABC):
    def __str__(self):
        raise NotImplementedError


class MarinaraSauce(Sauce):
    def __str__(self):
        return "Marinara Sauce"


class PlumTomatoSauce(Sauce):
    def __str__(self):
        return "Tomato sauce with plum tomatoes"


class Veggies(abc.ABC):
    def __str__(self):
        raise NotImplementedError


class Spinach(Veggies):
    def __str__(self):
        return "Spinach"


class BlackOlives(Veggies):
    def __str__(self):
        return "Black Olives"


class Eggplant(Veggies):
    def __str__(self):
        return "Eggplant"


class Garlic(Veggies):
    def __str__(self):
        return "Garlic"


class Mushroom(Veggies):
    def __str__(self):
        return "Mushrooms"


class Onion(Veggies):
    def __str__(self):
        return "Onion"


class RedPepper(Veggies):
    def __str__(self):
        return "Red Pepper"


class Pepperoni(abc.ABC):
    def __str__(self) -> str:
        raise NotImplementedError


class SlicedPepperoni(Pepperoni):
    def __str__(self) -> str:
        return "Sliced Pepperoni"


class PizzaIngredientFactory(abc.ABC):
    def create_dough(self):
        raise NotImplementedError

    def create_sauce(self):
        raise NotImplementedError

    def create_cheese(self):
        raise NotImplementedError

    def create_veggies(self):
        raise NotImplementedError

    def create_pepperoni(self):
        raise NotImplementedError

    def create_clam(self):
        raise NotImplementedError


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return PlumTomatoSauce()

    def create_cheese(self):
        return MozzarellaCheese()

    def create_veggies(self):
        return [BlackOlives(), Spinach(), Eggplant()]

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FrozenClams()


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaraSauce()

    def create_cheese(self):
        return ReggianoCheese()

    def create_veggies(self):
        return [Garlic(), Onion(), Mushroom(), RedPepper()]

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FreshClams()


class Pizza:
    def __init__(self, ingredient_factory):
        self.ingredient_factory = ingredient_factory
        self.name = None
        self.dough = None
        self.sauce = None
        self.cheese = None
        self.veggies = []
        self.pepperoni = None
        self.clam = None

    def prepare(self):
        raise NotImplementedError

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        result = []
        result.append("---- " + self.name + " ----")
        if self.dough:
            result.append(self.dough)

        if self.sauce:
            result.append(self.sauce)

        if self.cheese:
            result.append(self.cheese)

        if self.veggies:
            result.append(", ".join(map(str, self.veggies)))

        if self.clam:
            result.append(self.clam)

        if self.pepperoni:
            result.append(self.pepperoni)

        return "\n".join(map(str, result)) + "\n"


class CheesePizza(Pizza):
    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()


class ClamPizza(Pizza):
    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_clam()


class VeggiePizza(Pizza):
    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies()


class PepperoniPizza(Pizza):
    def prepare(self):
        print(f"Preparing {self.name}")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.veggies = self.ingredient_factory.create_veggies()
        self.pepperoni = self.ingredient_factory.create_pepperoni()


class PizzaStore:
    def create_pizza(self, item):
        raise NotImplementedError

    def order_pizza(self, type_):
        pizza = self.create_pizza(type_)
        print(f"--- Making a {pizza.name} ---")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, item):
        pizza = None
        ingredient_factory = ChicagoPizzaIngredientFactory()
        if item == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.name = "Chicago Style Cheese Pizza"
        elif item == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.name = "Chicago Style Veggie Pizza"
        elif item == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.name = "Chicago Style Clam Pizza"
        elif item == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.name = "Chicago Style Pepperoni Pizza"
        return pizza


class NYPizzaStore(PizzaStore):
    def create_pizza(self, item):
        pizza = None
        ingredient_factory = NYPizzaIngredientFactory()
        if item == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.name = "New York Style Cheese Pizza"
        elif item == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.name = "New York Style Veggie Pizza"
        elif item == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.name = "New York Style Clam Pizza"
        elif item == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.name = "New York Style Pepperoni Pizza"
        return pizza


def pizza_test_drive():
    ny_store = NYPizzaStore()
    chicago_store = ChicagoPizzaStore()

    pizza = ny_store.order_pizza("cheese")
    print(f"Joel ordered a {pizza}")
    pizza = chicago_store.order_pizza("cheese")
    print(f"Joel ordered a {pizza}")

    pizza = ny_store.order_pizza("clam")
    print(f"Joel ordered a {pizza}")
    pizza = chicago_store.order_pizza("clam")
    print(f"Joel ordered a {pizza}")

    pizza = ny_store.order_pizza("pepperoni")
    print(f"Joel ordered a {pizza}")
    pizza = chicago_store.order_pizza("pepperoni")
    print(f"Joel ordered a {pizza}")

    pizza = ny_store.order_pizza("veggie")
    print(f"Joel ordered a {pizza}")
    pizza = chicago_store.order_pizza("veggie")
    print(f"Joel ordered a {pizza}")


if __name__ == "__main__":
    pizza_test_drive()
