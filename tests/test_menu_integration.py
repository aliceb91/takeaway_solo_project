from lib.menu import Menu
from lib.item import Item
import pytest

# @pytest.mark.skip(reason="integration test dependencies incomplete")

def test_displays_menu_list():
    # Given a list of instances of Item
    # It creates an instance of menu that stores this list as menu_list.
    item_1 = Item("Fish and Chips", 6.5)
    item_2 = Item("Donner Kebab", 5)
    item_3 = Item("Seet and Sour Chicken", 7)
    item_list = [item_1, item_2, item_3]
    menu = Menu(item_list)
    result = menu.show_full_menu()
    assert result == item_list

def test_selects_item():
    # Given an instance of Item
    # It increments the counter of the relevant Item by 1.
    item_1 = Item("Fish and Chips", 6.5)
    item_2 = Item("Donner Kebab", 5)
    item_3 = Item("Seet and Sour Chicken", 7)
    item_list = [item_1, item_2, item_3]
    menu = Menu(item_list)
    menu.select_item(menu.menu_list[1])
    result = menu.menu_list[1].selected
    assert result == 1

def test_selects_multiple_items():
    # Given an instance of Item
    # It increments selected multiple times.
    item_1 = Item("Fish and Chips", 6.5)
    item_2 = Item("Donner Kebab", 5)
    item_3 = Item("Seet and Sour Chicken", 7)
    item_list = [item_1, item_2, item_3]
    menu = Menu(item_list)
    menu.select_item(menu.menu_list[1])
    menu.select_item(menu.menu_list[1])
    result = menu.menu_list[1].selected
    assert result == 2

def test_generates_valid_recpit():
    # Given a list of Item instances
    # It produces a list of the items selected with the total cost.
    item_1 = Item("Fish and Chips", 6.5)
    item_2 = Item("Donner Kebab", 5)
    item_3 = Item("Sweet and Sour Chicken", 7.5)
    item_list = [item_1, item_2, item_3]
    menu = Menu(item_list)
    menu.select_item(menu.menu_list[1])
    menu.select_item(menu.menu_list[1])
    menu.select_item(menu.menu_list[2])
    result = menu.generate_receipt()
    assert result == [
        {
            "name": "Donner Kebab",
            "price": 5,
            "selected": 2,
            "total": 10
        },
        {
            "name": "Sweet and Sour Chicken",
            "price": 7.5,
            "selected": 1,
            "total": 7.5
        },
        {
            "total_price": 17.5
        }
    ]
