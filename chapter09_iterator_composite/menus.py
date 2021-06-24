class MenuItem():
    def __init__(self, 
                name: str,
                description: str,
                vegetarian: bool,
                price: float,
                ):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price


class Menu():
    def __iter__(self):
        raise NotImplementedError

class CafeMenu(Menu):
    def __init__(self) -> None:
        self.menu_items = {}
        self.add_item("Veggie Burger and Air Fries",
            "Veggie burger on a whole wheat bun, lettuce, tomato, and fries",
            True, 3.99)
        self.add_item("Soup of the day",
            "A cup of the soup of the day, with a side salad",
            False, 3.69)
        self.add_item("Burrito",
            "A large burrito, with whole pinto beans, salsa, guacamole",
            True, 4.29)

    def add_item(self,
                name: str,
                description: str,
                vegetarian: bool,
                price: float,
                ):
        self.menu_items[name] = MenuItem(name, description, vegetarian, price)

    def __iter__(self):
        self.menu_items.values()


class DinerMenu(Menu):
    def __init__(self):
        self.menu_items = []
        self.add_item("Vegetarian BLT",
            "(Fakin') Bacon with lettuce & tomato on whole wheat", True, 2.99)
        self.add_item("BLT",
            "Bacon with lettuce & tomato on whole wheat", False, 2.99)
        self.add_item("Soup of the day",
            "Soup of the day, with a side of potato salad", False, 3.29)
        self.add_item("Hotdog",
            "A hot dog, with sauerkraut, relish, onions, topped with cheese",
            False, 3.05)
        self.add_item("Steamed Veggies and Brown Rice",
            "A medly of steamed vegetables over brown rice", True, 3.99)
        self.add_item("Pasta",
            "Spaghetti with Marinara Sauce, and a slice of sourdough bread",
            True, 3.89);       

    def add_item(self,
                name: str,
                description: str,
                vegetarian: bool,
                price: float,
                ):
        self.menu_items.append(MenuItem(name, description, vegetarian, price))

    def __iter__(self):
        return self.menu_items


class Waitress():
    def __init__(self, cafe_menu, diner_menu):
        self.cafe_menu = cafe_menu
        self.diner_menu = diner_menu

    def print_menu(self):
        pass

    def is_item_vegetarian(self, name):
        

def menu_test_drive():
    cafe_menu = CafeMenu()
    diner_menu = DinerMenu()
    waitress = Waitress(cafe_menu, diner_menu)
    waitress.print_menu()
    print("\nCustomer asks, is the Hotdog vegetarian?")
    print("Waitress says: ", end="")
    if (waitress.isItemVegetarian("Hotdog")):
        print("Yes")
    else:
        print("No")

    print("\nCustomer asks, are the Waffles vegetarian?")
    print("Waitress says: ", end="")
    if (waitress.isItemVegetarian("Waffles")):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    menu_test_drive()