from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

class Menu():
    def __init__(self, item_list):
        # Stores a list of Item instances as menu_list
        self.menu_list = item_list

    def show_full_menu(self):
        # Presents the contents of item_list as a list of instances of item
        #
        # Parameters:
        #   None.
        #
        # Returns:
        #   A list of all items in item_list
        #
        # Side effects:
        #   None.
        return self.menu_list

    def select_item(self, item):
        # Marks a specified menu item as "selected"
        #
        # Parameters:
        #   An instance of Item from item_list
        #
        # Returns:
        #   None.
        #
        # Side effects:
        #   Increases the value of selected by 1.
        item.select_item()

    def generate_receipt(self):
        # Creates a list of dictionaries containing the information of each item selected by the user.
        #
        # Parameters:
        #   None.
        #
        # Returns:
        #   A list of dictionaeries containing each selected item, with the final entry being a "total" key value pair.
        #
        # Side effects:
        #   None.
        receipt_list = []
        total_price = 0
        for item in self.menu_list:
            if item.selected > 0:
                receipt_list.append(item.generate_receipt_entry())
                total_price += item.total
        receipt_list.append({"total_price": total_price})
        return receipt_list


    def send_confirmation(self, number, text_client):
        # Sends a confirmation text containing the estimated delivery time.
        #
        # Parameters:
        #   The phone number of the user.
        #
        # Returns:
        #   None.
        #
        # Side effects:
        #   Returns a confirmation text for the order containing the delivery time.
        message = text_client.messages.create(
            body="Your order is on the way!",
            from_="+447700141798",
            to=number
        )
