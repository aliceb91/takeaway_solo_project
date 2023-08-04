from lib.menu import Menu
from unittest.mock import Mock

def test_return_single_item_list():
    # Given a list of a single item
    # It creates and returns a list of menu items.
    item = Mock()
    menu = Menu([item])
    result = menu.show_full_menu()
    assert result == [item]

def test_return_multi_item_list():
    # Given a list of multiple items
    # It creates and returns a list of meny items.
    item_1 = Mock()
    item_2 = Mock()
    item_3 = Mock()
    item_list = [item_1, item_2, item_3]
    menu = Menu(item_list)
    result = menu.show_full_menu()
    assert result == item_list

def test_mark_selected():
    # Given a list of a single item
    # Ensures the select_item method of Item is called
    item = Mock()
    menu = Menu([item])
    menu.select_item(menu.menu_list[0])
    menu.menu_list[0].select_item.assert_called()

def test_mark_selected_in_list():
    # Given a list of multiple items
    # Ensures the select_item method of Item is called.
    item_1 = Mock()
    item_2 = Mock()
    item_3 = Mock()
    item_list = [item_1, item_2, item_3]
    menu = Menu(item_list)
    menu.select_item(menu.menu_list[1])
    menu.menu_list[1].select_item.assert_called()

def test_generate_receipt():
    # Given a list of multiple items
    # It runs generate receipt on each item.
    item_1 = Mock()
    item_1.selected = 0
    item_1.total = 0
    item_2 = Mock()
    item_2.selected = 1
    item_2.total = 1
    item_3 = Mock()
    item_3.selected = 2
    item_3.total = 2
    item_list = [item_1, item_2, item_3]
    menu = Menu(item_list)
    menu.generate_receipt()
    for item in menu.menu_list:
        if item.selected > 0:
            item.generate_receipt_entry.assert_called()

def test_send_text():
    # Given an instances of Menu
    # Sends a text message confirming the order.
    item = Mock()
    menu = Menu([item])
    client = Mock()
    menu.send_confirmation("+447921818906", client)
    client.messages.create.assert_called()
