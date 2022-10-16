class CashRegister:

    def __init__(self):
        self.total_items = []
        self.total_price = 0
        self.discount = 0

    def add_item(self, item):
        self.total_items.append(item)

    def remove_item(self, item):
        self.total_items.remove(item)

    def apply_discount(self, percentage_discount):
        self.discount += percentage_discount

    def get_total(self):
        total_price = 0
        for item in self.total_items:
            total_price += item["price"]
        return total_price * (1 - self.discount/100)

    def show_items(self):
        for item in self.total_items:
            print(item)

    def reset_register(self):
        self.total_items = []
        self.total_price = 0
        self.discount = 0



clothes = CashRegister()
clothes.add_item({"name": "dress", "price": 70})
clothes.add_item({"name": "purse", "price": 65})
clothes.add_item({"name": "jacket", "price": 149})
clothes.add_item({"name": "heels", "price": 99})
print("Items in register")
clothes.show_items()
clothes.remove_item({"name": "heels", "price": 99})
print("Items in register after removing heels")
clothes.show_items()
clothes.apply_discount(15)
print("Total after discount")
print(clothes.get_total())
clothes.reset_register()
print("Items in register after clearing register")
clothes.show_items()