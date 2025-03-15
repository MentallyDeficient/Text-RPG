class Enemy:
    def __init__(self, name, description, health=50):
        self.name = name
        self.description = description
        self.health = health

    def is_alive(self):
        return self.health > 0

def combat_round(player, enemy):
    enemy.health -= 10
    player.health -= 5
    return f"You hit the {enemy.name} for 10 damage. It hits you back for 5."

goblin = Enemy("Goblin", "A nasty little creature with sharp teeth.")
wolf = Enemy("Wolf", "A snarling beast with glowing eyes.")
skeleton = Enemy("Skeleton", "A clattering pile of bones held together by bad vibes.")
