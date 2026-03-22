
class InventoryItem:
    def __init__(self, id, name, price, amount_in_stock):
        pass

class Inventory:
    def __init__(self):
        self.stock = {}

    def add_item(self, item: InventoryItem):
        self.stock[item.id] = item

    def check_stock(self, item_id):
        item = self.stock.get(item_id)
        return item.amount_in_stock if item else 0