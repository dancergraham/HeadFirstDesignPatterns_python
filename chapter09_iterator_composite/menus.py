# package headfirst.designpatterns.iterator.dinermergercafe


class MenuItem:
    def __init__(
        self,
        name: str,
        description: str,
        vegetarian: bool,
        price: float,
    ):
        self.name = name
        self.description = description
        self.vegetarian = vegetarian
        self.price = price


class Menu:
    def __iter__(self):
        raise NotImplementedError


class CafeMenu(Menu):
    def __init__(self) -> None:
        self.menu_items = {}
        self.add_item(
            "Veggie Burger and Air Fries",
            "Veggie burger on a whole wheat bun, lettuce, tomato, and fries",
            True,
            3.99,
        )
        self.add_item(
            "Soup of the day",
            "A cup of the soup of the day, with a side salad",
            False,
            3.69,
        )
        self.add_item(
            "Burrito",
            "A large burrito, with whole pinto beans, salsa, guacamole",
            True,
            4.29,
        )

    def add_item(
        self,
        name: str,
        description: str,
        vegetarian: bool,
        price: float,
    ):
        self.menu_items[name] = MenuItem(name, description, vegetarian, price)

    def __iter__(self):
        return iter(self.menu_items.values())


class DinerMenu(Menu):
    def __init__(self):
        self.menu_items = []
        self.add_item(
            "Vegetarian BLT",
            "(Fakin') Bacon with lettuce & tomato on whole wheat",
            True,
            2.99,
        )
        self.add_item("BLT", "Bacon with lettuce & tomato on whole wheat", False, 2.99)
        self.add_item(
            "Soup of the day",
            "Soup of the day, with a side of potato salad",
            False,
            3.29,
        )
        self.add_item(
            "Hotdog",
            "A hot dog, with sauerkraut, relish, onions, topped with cheese",
            False,
            3.05,
        )
        self.add_item(
            "Steamed Veggies and Brown Rice",
            "A medly of steamed vegetables over brown rice",
            True,
            3.99,
        )
        self.add_item(
            "Pasta",
            "Spaghetti with Marinara Sauce, and a slice of sourdough bread",
            True,
            3.89,
        )

    def add_item(
        self,
        name: str,
        description: str,
        vegetarian: bool,
        price: float,
    ):
        self.menu_items.append(MenuItem(name, description, vegetarian, price))

    def __iter__(self):
        return iter(self.menu_items)


class Waitress:
    def __init__(self, cafe_menu, diner_menu):
        self.cafe_menu = cafe_menu
        self.diner_menu = diner_menu

    def _print_menu(self, itermenu):
        for menu_item in itermenu:
            print(f"{menu_item.name}, {menu_item.price} -- {menu_item.description}")

    def print_menu(self):
        print("MENU\n----\nBREAKFAST")
        print("not implemented")
        print("\nLUNCH")
        self._print_menu(self.diner_menu)
        print("\nDINNER")
        self._print_menu(self.cafe_menu)

    def _is_vegetarian(self, name, itermenu):
        for menu_item in itermenu:
            if menu_item.name == name:
                return menu_item.vegetarian
        return False

    def is_item_vegetarian(self, name):
        if self._is_vegetarian(name, self.cafe_menu):
            return True
        if self._is_vegetarian(name, self.diner_menu):
            return True
        return False


def menu_test_drive():
    cafe_menu = CafeMenu()
    diner_menu = DinerMenu()
    waitress = Waitress(cafe_menu, diner_menu)
    waitress.print_menu()
    print("\nCustomer asks, is the Hotdog vegetarian?")
    print("Waitress says: ", end="")
    if waitress.is_item_vegetarian("Hotdog"):
        print("Yes")
    else:
        print("No")


"""    print("\nCustomer asks, are the Waffles vegetarian?")  # Not implemented
    print("Waitress says: ", end="")
    if (waitress.is_item_vegetarian("Waffles")):
        print("Yes")
    else:
        print("No")"""

if __name__ == "__main__":
    menu_test_drive()
