from adventurelib import Item

class RPGItem(Item):
    def __init__(self, name, *aliases, can_take=True, description=""):
        super().__init__(name, *aliases)
        self.can_take = can_take
        self.description = description

# Define Items
flashlight = RPGItem('flashlight', can_take=True, description='A simple flashlight that takes two D batteries.')
rusty_sword = RPGItem('rusty sword', 'sword', can_take=True, description='Dull and covered in rust.')
dented_shield = RPGItem('dented shield', 'shield', can_take=True, description='Battered and scarred, still offers some protection.')
flamethrower = RPGItem('flamethrower', 'flame thrower', can_take=True, description='A homemade contraption of doom: air freshener + lighter.')
chips = RPGItem('chips', 'bag of chips', can_take=True, description='A greasy bag of Lay’s potato chips.')
scroll = RPGItem('scroll', can_take=True, description='Ancient parchment with broken seal and arcane glyphs.')
