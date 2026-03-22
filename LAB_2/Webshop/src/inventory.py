
class InventoryItem:
    def __init__(self, id, name, price, amount_in_stock):
        self.id = id
        self.name = name
        self.price = price
        self.amount_in_stock = amount_in_stock

class Inventory:
    def __init__(self):
        self.stock = {}

    def add_to_stock(self, item: InventoryItem):
        self.stock[item.id] = item

    def check_stock(self, item_id):
        item = self.stock.get(item_id)
        return item.amount_in_stock if item else 0