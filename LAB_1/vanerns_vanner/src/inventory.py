
class Item:
    def __init__(self, name, rent_price, amount ):
        self.name = name
        self.rent_price = rent_price
        self.amount = amount

class Inventory:
    def __init__(self):
        self.items = []

    def set_item(self, name, rent_price, amount):
        self.items[name] = Item(name, rent_price, amount)

    def rent(self, item_name):
        if item_name in self.items and self.items[item_name].amount > 0:
            self.items[item_name].amount -= 1
            return True
        return False

    def get_amount_left(self, name):
        if name in self.items:
            return self.items[name].amount
        return 0