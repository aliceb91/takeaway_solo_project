from lib.item import Item

def test_creates_item():
    # Given an item name and price
    # Creates an instance of Item with those values and a selected value of 0
    item = Item("Fish and Chips", 6.5)
    result = [item.name, item.price, item.selected]
    assert result == ["Fish and Chips", 6.5, 0]

def test_selects_item():
    # Given a call of select_item
    # It incremends selected by 1.
    item = Item("Fish and Chips", 6.5)
    item.select_item()
    result = item.selected
    assert result == 1

def test_generate_receipt():
    # Given a call of generate_receipt_entry
    # It returns a dictionary entry containing the classes current information.
    item = Item("Fish and Chips", 6.5)
    item.select_item()
    result = item.generate_receipt_entry()
    assert result == {
        "name": "Fish and Chips",
        "price": 6.5,
        "selected": 1,
        "total": 6.5,
    }

def test_generate_multi_item_receipt_entry():
    # Given multiple selections of a single item
    # It returns a receipt entry with the correct total price.
    item = Item("Donner Kebab", 5)
    item.select_item()
    item.select_item()
    result = item.generate_receipt_entry()
    assert result == {
        "name": "Donner Kebab",
        "price": 5,
        "selected": 2,
        "total": 10
    }
