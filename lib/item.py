class Item():
    def __init__(self, name, price):
        # Sets the initial state of the item.
        #
        # Parameters:
        #   name: The name of the dish as a string.
        #   price: The price of the item as an integer in pounds.
        #
        # Side effects:
        #   Sets selected to 0.
        self.name = name
        self.price = price
        self.selected = 0
        self.total = 0

    def select_item(self):
        # Increments the value of selected by one.
        #
        # Parameters:
        #   None.
        #
        # Returns:
        #   None.
        #
        # Side effects:
        #   Increments the value of selected by 1.
        self.selected += 1

    def generate_receipt_entry(self):
        # Produces a dictionary containing the relevent class vairables
        #
        # Parameters:
        #   None.
        #
        # Returns:
        #   A dictionary containing the name, individual cost, selected total and total cost of the item.
        #
        # Side effects:
        #   None.
        self.total = self.price * self.selected
        return {
            "name": self.name,
            "price": self.price,
            "selected": self.selected,
            "total": self.total
        }
