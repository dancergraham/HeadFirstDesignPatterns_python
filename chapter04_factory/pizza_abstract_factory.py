import abc


class Cheese(abc.ABC):
    def __str__(self):
        raise NotImplementedError


class MozzarellaCheese(Cheese):
    def __str__(self):
        return "Shredded Mozzarella"


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
    def __str__self():
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
    def create_dough():
        raise NotImplementedError
    def create_sauce():
        raise NotImplementedError
    def create_cheese():
        raise NotImplementedError
    def create_veggies():
        raise NotImplementedError
    def create_pepperoni():
        raise NotImplementedError
    def create_clam():
        raise NotImplementedError


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough():
        return ThickCrustDough()
    def create_sauce():
        return PlumTomatoSauce()
    def create_cheese():
        return MozzarellaCheese()
    def create_veggies():
        return[BlackOlives(), Spinach(), Eggplant()]
    def create_pepperoni():
        return SlicedPepperoni()
    def create_clam():
        return FrozenClams()


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough():
        return ThinCrustDough()
    def create_sauce():
        return MarinaraSauce()
    def create_cheese():
        return ReggianoCheese()
    def create_veggies():
        return[Garlic(), Onion(), Mushroom(), RedPepper()]
    def create_pepperoni():
        return SlicedPepperoni()
    def create_clam():
        return FreshClams()


class Pizza:
    def __init__(self):
        self.name = None
        self.dough = None
        self.sauce = None
        self.cheese = None
        self.veggies = []
        self.pepperoni = None
        self.clams = None
    
    def prepare():
        raise NotImplementedError

    def bake():
        print("Bake for 25 minutes at 350")

    def cut():
        print("Cutting the pizza into diagonal slices")

    def box():
        print("Place pizza in official PizzaStore box")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        result = []
        result.append("---- " + name + " ----\n")
        if self.dough:
            result.append(self.dough)
            result.append("\n")
        
        if self.sauce:
            result.append(self.sauce)
            result.append("\n")
        
        if self.cheese:
            result.append(self.cheese)
            result.append("\n")
        
        if self.veggies:
            result.append(", ".join(self.veggies))
            result.append("\n")
        
        if self.clam:
            result.append(self.clam)
            result.append("\n")
        
        if self.pepperoni:
            result.append(self.pepperoni)
            result.append("\n")
        
        return "".join(result)


class PizzaStore:
    def create_pizza(self, item):
        raise NotImplementedError

    def order_pizza(self, type):
        pizza = self.create_pizza(type)
        print(f"--- Making a {pizza.get_name()} ---")
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, item):
        pizza = None
        ingredient_factory = ChicagoPizzaIngredientFactory()
        if item == 'cheese':
            pizza = new Chee
