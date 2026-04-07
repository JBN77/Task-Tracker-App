import json
import os
from models import Item


class ItemManager:
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.items = []
        self.load_items()

    def add_item(self, item):
        self.items.append(item)
        self.save_items()

    def get_all_items(self):
        return self.items

    def get_item(self, index):
        if 0 <= index < len(self.items):
            return self.items[index]
        return None

    def mark_item_complete(self, index):
        item = self.get_item(index)
        if item:
            item.mark_complete()
            self.save_items()

    def delete_item(self, index):
        if 0 <= index < len(self.items):
            self.items.pop(index)
            self.save_items()

    def save_items(self):
        data = [item.to_dict() for item in self.items]
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def load_items(self):
        if not os.path.exists(self.filename):
            self.items = []
            return

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                self.items = [Item.from_dict(item_data) for item_data in data]
        except (json.JSONDecodeError, FileNotFoundError):
            self.items = []