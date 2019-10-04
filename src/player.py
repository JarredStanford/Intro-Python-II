# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item
class Player:
    def __init__(self, name, current_room):
        self.name = name;
        self.current_room = current_room;
        self.inventory = []

    def add_item(self, new_item):
        self.inventory.append(new_item)
        Item(new_item).on_take()

    def drop_item(self, item):
        self.inventory.remove(item)
        Item(item).on_drop()