class Order:
    def __init__(self, products_and_amounts):
        self.products = products_and_amounts # e.g., {"apple": 5, "bread": 2}
        self.status = "unpaid"

    def calculate_total(self):
        # Simplified: let's assume every item is 10kr for this lab
        return sum(self.products.values()) * 10

    def make_payment(self, gateway):
        total = self.calculate_total()
        success = gateway.execute_payment(total)

        if success:
            self.status = "paid"
        else:
            self.status = "error"
        return success