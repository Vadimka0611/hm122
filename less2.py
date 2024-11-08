class Item:

    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"Fruit: {self.name}. Price: {self.price}. Description: {self.description}. Dimensions: {self.dimensions}"

class User:

    def __init__(self, name, surname, patronymic, numberphone):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.numberphone = numberphone

    def __str__(self):
        return f"{self.name} {self.surname} {self.patronymic}. Numberphone: {self.numberphone}"

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user
        self.total = 0

    def add_item(self, item, cnt):
        # self.products[item] = cnt
        if item in self.products:
            self.products[item] += cnt
        else:
            self.products[item] = cnt

    def __str__(self):
        item_str = "\n".join([f"{item.name}: {pcs} pcs." for item, pcs in self.products.items()])
        return f"Items:\n{item_str}\nTotal: {self.get_total()}"

    def get_total(self):
        return sum(item.price * cnt for item, cnt in self.products.items())

lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)  # lemon, price: 5

buyer = User("Ivan", "Ivanov", "Ivanovich", "02628162")
print(buyer)  # Ivan Ivanov

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 20 pcs.
"""
isinstance(cart.user, User)
cart.get_total()
cart.get_total()
cart.add_item(apple, 10)
print(cart)
"""
User: Ivan Ivanov
Items:
lemon: 4 pcs.
apple: 10 pcs.
"""

cart.get_total()
