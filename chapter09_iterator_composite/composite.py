# package headfirst.designpatterns.iterator.dinermergercafe
class MenuComponent:
    def add(self, menu_component):
        raise NotImplementedError

    def remove(self, menu_component):
        raise NotImplementedError
    
    def get_child(self, i: int):
        raise NotImplementedError
    
    def print(self):
        raise NotImplementedError


class MenuItem(MenuComponent):
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

    def print(self):
        print(" " + self.name + "(v)" * self.vegetarian + ", " + str(self.price))
        print("     -- " + self.description)


class Menu(MenuComponent):
    name: str
    description: str

    def __init__(self, name: str, description: str):
        self.menu_components: list[MenuComponent] = []
        self.name = name
        self.description = description

    def add(self, menu_component: MenuComponent):
        self.menu_components.append(menu_component)

    def remove(self, menu_component: MenuComponent):
        self.menu_components.remove(menu_component)

    def get_child(self, i: int):
        return self.menu_components[i]
    
    def print(self):
        print('\n' + self.name + ", " + self.description)
        print('--------------------')

        for menu_component in self.menu_components:
            menu_component.print()

    def __iter__(self):
        raise NotImplementedError


class CafeMenu(Menu):
    def __iter__(self):
        return iter(self.menu_items.values())


class DinerMenu(Menu):
    def __iter__(self):
        return iter(self.menu_items)


class Waitress:
    def __init__(self, all_menus: MenuComponent):
        self.all_menus = all_menus

    def print_menu(self):
        self.all_menus.print()


def menu_test_drive():
    cafe_menu = CafeMenu('Cafe Menu', 'For Dinner')
    diner_menu = DinerMenu('Diner Menu', 'For Lunch')
    all_menus: MenuComponent = Menu('all menus', 'all menus')
    all_menus.add(cafe_menu)
    all_menus.add(diner_menu)
    cafe_menu.add(
        MenuItem(
            "Veggie Burger and Air Fries",
            "Veggie burger on a whole wheat bun, lettuce, tomato, and fries",
            True,
            3.99,
        )
    )
    cafe_menu.add(
        MenuItem(
            "Soup of the day",
            "A cup of the soup of the day, with a side salad",
            False,
            3.69,
        )
    )
    cafe_menu.add(
        MenuItem(
            "Burrito",
            "A large burrito, with whole pinto beans, salsa, guacamole",
            True,
            4.29,
        )
    )
    diner_menu.add(
        MenuItem(
            "Vegetarian BLT",
            "(Fakin') Bacon with lettuce & tomato on whole wheat",
            True,
            2.99,
        )
    )
    diner_menu.add(
        MenuItem(
            "BLT",
            "Bacon with lettuce & tomato on whole wheat",
            False,
            2.99,
        )
    )
    diner_menu.add(
        MenuItem(
            "Soup of the day",
            "Soup of the day, with a side of potato salad",
            False,
            3.29,
        )
    )
    diner_menu.add(
        MenuItem(
            "Hotdog",
            "A hot dog, with sauerkraut, relish, onions, topped with cheese",
            False,
            3.05,
        )
    )
    diner_menu.add(
        MenuItem(
            "Steamed Veggies and Brown Rice",
            "A medly of steamed vegetables over brown rice",
            True,
            3.99,
        )
    )
    diner_menu.add(
        MenuItem(
            "Pasta",
            "Spaghetti with Marinara Sauce, and a slice of sourdough bread",
            True,
            3.89,
        )
    )
    cafe_menu.print()
    waitress = Waitress(all_menus)
    waitress.print_menu()
    # print("\nCustomer asks, is the Hotdog vegetarian?")
    # print("Waitress says: ", end="")
    # if waitress.is_item_vegetarian("Hotdog"):
    #     print("Yes")
    # else:
    #     print("No")


"""    print("\nCustomer asks, are the Waffles vegetarian?")  # Not implemented
    print("Waitress says: ", end="")
    if (waitress.is_item_vegetarian("Waffles")):
        print("Yes")
    else:
        print("No")"""

if __name__ == "__main__":
    menu_test_drive()
