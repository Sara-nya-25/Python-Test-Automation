
class StockItem:
    def __init__(self, name, qty):
        self.name = name
        self.quantity = qty

class Stock:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)

    def reduce_quantity(self, name, qty):
        # Find the product in the list by name
        for item in self.items:
            if item.name == name:
                if item.quantity >= qty:
                    item.quantity -= qty
                    return
                else:
                    raise ValueError("Insufficient stock")
        raise KeyError("Product not found")

    def get_quantity(self, name):
        for item in self.items:
            if item.name == name:
                return item.quantity
        return 0