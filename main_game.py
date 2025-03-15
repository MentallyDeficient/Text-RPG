from adventurelib import start, say, when
from rooms import entrance, cave_down, four_chamber, shrine_room, terminal_room, armory
from items import flashlight, rusty_sword, dented_shield, flamethrower, chips, scroll
from terminal import OldTerminal
from player import Player
from character import start_character_creation
from combat import Enemy, combat_round, goblin, wolf, skeleton
import random

player = Player()
player.current_room = entrance

# Add initial items to rooms (example setup)
entrance.items.append(flashlight)
armory.items.extend([rusty_sword, dented_shield, flamethrower])
terminal_room.items.append(chips)
shrine_room.items.append(scroll)

current_enemy = None

@when('look')
def look():
    if not player.character_created:
        say("You must create your character first! Use 'create character' to begin.")
        return
    say(player.current_room.description)
    if player.current_room.items:
        for item in player.current_room.items:
            say(f'There is a {item.name} here: {item.description}')

@when('go DIRECTION')
@when('north')
@when('south')
@when('east')
@when('west')
@when('up')
@when('down')
def go(direction=None):
    if not player.character_created:
        say("You must create your character first! Use 'create character' to begin.")
        return

    if player.in_combat:
        say("You can't move while in combat!")
        return

    direction = direction or 'north'
    next_room = getattr(player.current_room, direction, None)
    if next_room:
        player.current_room = next_room
        look()
        if player.current_room == shrine_room and random.random() < 0.3:
            enemy = random.choice([goblin, wolf, skeleton])
            say(f"A {enemy.name} appears! {enemy.description}")
            player.in_combat = True
            set_context('combat')
            global current_enemy
            current_enemy = enemy
    else:
        say("You can't go that way.")

@when('inventory')
def show_inventory():
    if not player.character_created:
        say("You must create your character first! Use 'create character' to begin.")
        return
    if not player.inventory:
        say('You are not carrying anything.')
        return
    say('You are carrying:')
    for item in player.inventory:
        say(f'- {item.name}: {item.description}')

@when('get ITEM')
@when('take ITEM')
def get(item):
    if not player.character_created:
        say("You must create your character first! Use 'create character' to begin.")
        return

    item_name = item.lower()
    found_item = None
    for room_item in player.current_room.items:
        if room_item.name.lower() == item_name:
            found_item = room_item
            break

    if found_item:
        if getattr(found_item, "can_take", True):
            player.current_room.items.remove(found_item)
            player.add_item(found_item)
            say(f'You pick up the {found_item.name}.')
        else:
            say(f"You can't take the {found_item.name}.")
    else:
        say(f"There is no {item_name} here.")

@when('drop ITEM')
def drop(item):
    if not player.character_created:
        say("You must create your character first! Use 'create character' to begin.")
        return
    item_name = item.lower()
    for inv_item in player.inventory:
        if inv_item.name.lower() == item_name:
            player.remove_item(inv_item)
            player.current_room.items.append(inv_item)
            say(f'You drop the {inv_item.name}.')
            return
    say(f"You don't have a {item_name}.")

@when('stats')
def show_stats():
    if not player.character_created:
        say("You must create your character first! Use 'create character' to begin.")
        return
    say(f"Health: {player.health}/{player.max_health}")
    if player.in_combat and current_enemy:
        say(f"Fighting: {current_enemy.name} (Health: {current_enemy.health})")

@when('use terminal')
@when('use computer')
def use_terminal():
    if player.current_room != terminal_room:
        say("There is no terminal here.")
        return
    term = OldTerminal('192.168.171.116', 'null', 'y3ll0wIceCre@m')
    term.enter()

@when('use ITEM')
def use(item):
    if not player.character_created:
        say("You must create your character first! Use 'create character' to begin.")
        return
    item_name = item.lower()
    if item_name == "potion" and player.has_item("potion"):
        player.heal(50)
        for inv_item in player.inventory:
            if inv_item.name.lower() == "potion":
                player.remove_item(inv_item)
                break
        say("You drink the potion and feel refreshed!")
        show_stats()
    else:
        say(f"You can't use the {item_name}.")

@when('attack', context='combat')
def attack():
    if not player.character_created:
        say("You must create your character first! Use 'create character' to begin.")
        return
    if not player.in_combat:
        say("There's nothing to attack!")
        return

    global current_enemy
    result = combat_round(player, current_enemy)
    say(result)

    if not current_enemy.is_alive():
        say("Victory! The enemy has been defeated!")
        player.in_combat = False
        set_context('default')
    elif player.health <= 0:
        say("You have been defeated! Game Over!")
        exit()

@when('flee', context='combat')
def flee():
    if not player.character_created:
        say("You must create your character first! Use 'create character' to begin.")
        return
    if random.random() < 0.5:
        say("You successfully flee from combat!")
        player.in_combat = False
        set_context('default')
    else:
        say("You failed to escape!")
        result = combat_round(player, current_enemy)
        say(result)

@when('help')
def help():
    say("""
Available commands:
- look, inventory, stats
- go [direction] or use n/s/e/w/u/d
- get/take ITEM, drop ITEM, use ITEM
- use terminal (in terminal room)
- attack, flee (combat only)
- create character, show rolls, assign stats (during creation)
    """)

def start_game():
    say("""
Welcome to the Shadowed Depths.
You awaken in a place of damp stone and whispering vines.
Type 'help' for commands.
    """)
    start_character_creation()

if __name__ == '__main__':
    start_game()
    start()
