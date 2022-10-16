items = {"dress": 70, "purse": 65, "jacket": 149, "heels": 99}
class CashRegister:
    def __init__(self, total_items, total_price, discount, items_purchased, items_price):
        self.items_purchased = []
        self.items_price = []
        self.total_items = []
        self.total_price = []
        self.discount = 0.15

    def add_item(self):
        self.item = {"dress": 70, "purse": 65, "jacket": 149, "heels": 99}
        print("select items to add from the list using the name of the item")
        print(self.item)

        for i in range(0,50):
            self.x = input()
            if self.x == "=":
                break
            elif self.x not in self.item:
                print("error, please type name of item")
            elif self.x in self.item:
                self.items_purchased.append(self.x)
                self.items_price.append(self.item[self.x])
                self.total_items = len(self.items_purchased)
                self.total_price = sum(self.items_price)

    def remove_item(self):
        while len(self.items_purchased) > 0:
            print("select items to remove, 1 is for the first item in the list, 0 is to exit")
            print(self.items_purchased)



            try:
                x = int(input())
                if(x == 0):
                    break

                self.items_purchased.pop(x - 1)
                self.items_price.pop(x - 1)

            except:
                print("There was an error, please provide a valid number")


    def apply_discount(self):
        print("press 1 to apply discount")
        x = input()
        if x == "1":
            self.total_price = self.total_price * (1 - self.discount)
            print(f'your new price £{self.total_price}')
            pass
        else:
            pass

    def get_total(self):
        print(f"{self.total_items} items in  basket")
        print(f"total costs: £{self.total_price}")

    def show_items(self):
        print("See items purchased below and price below")
        print(self.items_purchased)
        print(self.items_price)

    def reset_register(self):
        z = ()
        while z != 0:
            z = input("press 0 to clear list")

            if z == "0":
                self.items_purchased.clear()
                self.items_price.clear()
                self.total_price = 0
                self.total_items = 0
                print
                print(f'total items {self.total_items}')
                print(f'total price £{self.total_price}')
                print("items have been cleared")
                pass
            else:
                print("press 0, you do not really get a choice: ")
                print("items in basket and price")
                print(self.items_purchased)
                print(self.items_price)
                print(f'total items : {self.total_items}')
                print(f'total price : £{self.total_price}')

clothes = CashRegister([],[],0.15, [], [])
clothes.add_item()

clothes.show_items()
clothes.get_total()
clothes.remove_item()
clothes.apply_discount()
clothes.reset_register()
