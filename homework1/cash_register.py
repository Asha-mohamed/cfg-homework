items = {"dress": 70, "purse": 65, "jacket": 149, "heels": 99}
class CashRegister:

    def __init__(self, total_items, total_price, discount, price):
        self.total_items = []
        self.price = []
        self.discount = 0.15
        self.total_price = 0

    def add_item(self, ):
        self.item = {"dress": 70, "purse": 65, "jacket": 149, "heels": 99}
        for i in range(0,50):
            self.x = input()
            if self.x == "=":
                break
            elif self.x not in self.item:
                print("error")
            elif self.x in self.item:
                self.total_items.append(self.x)
                self.price.append(self.item[self.x])
                self.total_price = self.total_price + self.item[self.x]







        #print(f"I want to add {self.add_item} to my bill")


    def remove_item(self):
        pass

    def apply_discount(self):
        pass

    def get_total(self):
        pass

    def show_items(self):
        pass

    def reset_register(self):
        pass



clothes = CashRegister([],[],0.12, [])
clothes.add_item()





print(f)
print(clothes.total_items)

print(clothes.price)

print(clothes.total_price)

# use a for loop to print it in a way that it comes out 1. dress : 65
# It will look more like a receipt and will make removing items easier


#clothes.add_item({"watch": 200})
#clothes.remove_item("purse")

