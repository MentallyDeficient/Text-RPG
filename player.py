class Player:
    def __init__(self):
        self.name = "Nameless Janitor"
        self.health = 100
        self.max_health = 100
        self.inventory = []
        self.character_created = True
        self.current_room = None
        self.in_combat = False

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)

    def has_item(self, item_name):
        return any(item.name.lower() == item_name.lower() for item in self.inventory)

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)
