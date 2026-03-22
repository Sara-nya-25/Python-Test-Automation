
class CartItem:
    def __init__(self, id, name, price, amount_in_cart):
        self.id = id
        self.name = name
        self.price = price
        self.amount_in_cart = amount_in_cart

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_inventory_item(self, item, amount, inventory):
        """
                Integration Point: Consults the inventory instance
                before adding to the cart.
                """
        available = inventory.check_stock(item.id)

        if amount <= available:
            if item.id in self.items:
                self.items[item.id].amount_in_cart += amount
            else:
                self.items[item.id] = CartItem(item.id, item.name, item.price, amount)
            return True

        return False  # Not enough stock!