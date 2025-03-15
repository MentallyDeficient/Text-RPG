#Imports
from adventurelib import *
import random
from fabric import Connection

#Define Rooms
Room.items = Bag()
Item.description = ""


current_room = starting_room = Room('''The cave entrance is hidden behind a large tree,
its gnarled roots creeping out of the ground like tentacles.
Vines and undergrowth cover the opening, as if trying to hide it from view.
It is as if the earth itself is trying to keep the secrets of the cave hidden from the world.
As you approach, the vines seem to writhe and twist, as if trying to deter you from entering.
The tree looms overhead, its branches reaching out like claws.
The air is heavy with the scent of decay and must,
as if the cave has not seen the light of day for centuries.
Despite your misgivings, you push aside the vines and undergrowth,
revealing the dark maw of the cave. It is as if you are peering into the abyss itself, 
the darkness seems to go on forever. You hesitate for a moment, wondering if you should turn back.
But something compels you to venture deeper into the cave,
as if there are secrets hidden within that are waiting to be discovered.
You now stand at the mouth of the cave, its ancient vines brushed back to reveal the light filtering
in through the twisted trees. Before you lies the dark, foreboding entrance to the cave,
beckoning you to delve into its shadows and uncover its secrets.''', '''ENTRANCE. 
The tree limbs and vines have closed ranks and have created an unnatural wall blocking your path out. The 
only path open to you is back south, down the sloping cave.''' )

@when('cut vines')
@when('cut tree')
@when('hack vines')
def cut_plants():
    if current_room == starting_room:
        say('''Your valiant efforts to trim the wild shrubbery have yielded little results, the tree branches and 
        vines seem to grow back without you witnessing any movement from the plants. What unholy trick is this?''')
    else:
        say("I'm affraid that's not going to work here.")

cave_down = Room('''As you make your way down the narrow, winding path, the darkness closes in around you like a thick, 
suffocating cloak. The air is heavy with the musty scent of mold and mildew,
and a chill runs down your spine as you feel the icy fingers of the cold touch your skin.
You descend deeper into the earth, your footsteps echoing off the rocky walls as you navigate the treacherous path. 
The darkness is complete, and you can barely make out the faint glow of your flashlight as it struggles
to pierce the inky blackness.The cave is silent except for the sound of your own breathing and the occasional 
drip of water echoing through the emptiness. You can't shake the feeling that you are being watched,
and you quicken your pace, your heart pounding in your chest. As you round a bend,
you see a faint glimmer of light in the distance. Hope flickers within you as you quicken your pace,
eager to escape the oppressive darkness of the cave. But as you draw closer, you realize with a sinking 
feeling that the light is not the exit you had hoped for. It is the flickering glow of something ancient 
and malevolent, something that should have remained buried in the darkness for all eternity.''', '''CAVE that slopes up north towards the enterance and south, down towards what waits for you below''')

four_chamber = Room('''With a sense of dread and foreboding, you step through the 
southern exit, a dark and foreboding cave that seems to lead
ever upward. The journey is steep and treacherous, but finally, 
you emerge into a chamber unlike any you have ever seen. The 
chamber is large and circular, with exits to the north, east, 
and west. To the south, a door of ancient, rotting wood stands 
slightly ajar, revealing only darkness beyond.To the west, a massive stone door, etched with eldritch runes
and symbols, looms ominously. And to the east, a door of shimmering, otherworldly 
metal seems to beckon you, drawing you towards the unknown.
But your gaze is immediately drawn to the center of the room, 
where a grotesque and eldritch sight awaits. A glass globe, 
resembling nothing so much as an unblinking eye, sits atop a
large chalice, its surface seemingly alive with an unholy light
that pours forth in waves of malevolent energy. The atmosphere is
thick with an almost tangible sense of evil and corruption, and you 
know that you are in a place of great power - a place where the very 
fabric of reality seems to have been twisted and corrupted by forces 
beyond mortal understanding. It is as if you have stumbled upon some ancient and forbidden chamber,
long sealed away from the world of man and now reopened to unleash its
eldritch horrors upon the unsuspecting. And yet, despite the overwhelming
sense of fear and revulsion that threatens to consume you, you can not help
but feel a strange and inexplicable pull towards the pulsing light of the globe, 
as if it were calling to you, drawing you ever closer to the depths of madness and oblivion.''',
'''FOUR CHAMBER ROOM, the glass globe continues to fill the room
with a sickly light. To the west is the stone door marked with runes, to the east
the door made of an odd metal, to the south the rotting wooden door, barely attached
to it's hinges.''')


shrine_room = Room('''The door creaked open to reveal a small, dimly lit chamber. 
The air inside was musty and still, as if it had not been disturbed
for centuries. In the center of the room stood a small shrine, its
intricate carvings and symbols seeming to writhe and twist in the
flickering torchlight. The shrine was a simple pedestal, adorned
with several slots for scrolls, but only one of these slots contained 
the ancient parchment. The front of the shrine bore the symbol of a
silver coin with two heads facing opposite directions, an image both 
enigmatic and unsettling. The eerie aura emanating from the shrine 
fills you with a sense of dread and unease, as if it were a portal 
to some arcane and forbidden knowledge. You can not shake the feeling 
that you are trespassing in a sacred place.''', '''SHRINE ROOM. The shrine 
remains as does the sense of dread and unease. The only exit is east, through the stone door.''')

terminal_room = Room('''As you push open the door of ancient, rotting wood, you step inside and the dust swirls around your feet. The room is filled with crisscrossing wires
of all sizes and colors, winding their way around piles of equipment and old machinery. You can hear a faint hum
coming from somewhere deep within the room. You make your way to the northern wall and find a computer terminal. It's
ancient, the kind you see in old science fiction movies with the screen embedded in the wall. The keyboard  is embedded in
a metal table that has flat square lights, a green, yellow and red light with some other equipment are connected to the table, 
and it seems to be the nexus of the many wires that snake throughout the room. There are LED lights on different
pieces of equipment, some of them flashing and others dimming. You look up and see a glass case directly above the 
computer terminal. Inside, there's an old book. The cover is simple, a blank scroll being unfurled. You can't help 
but feel a sense of unease as I look at it. I can't quite put my finger on it, but something about this room and
this book feels off, like it's not meant for human eyes. You hesitate for a moment, your hand hovering over the case.
But you can't shake the feeling that you're meant to be here, that this book holds the answers to questions you haven't 
even thought to ask yet ''', '''COMPUTER ROOM. Here the old terminal remains, waiting to be used. You hear the steady hum
of machinery in the walls.''')



class OldTerminal:
    def __init__(self, host, username, password):
        self.conn = Connection(host=host, user=username, connect_kwargs={
            "password": password
        })

    def enter(self):
        while True:
            cmd = input("$ ")
            if cmd == "exit":
                break
            try:
                result = self.conn.run(cmd, hide=True, warn=True)
                print(result.stdout)
            except AttributeError:
                print("ERROR: Command not recognized")
                continue

        print("You step away from the terminal and look around in the half-light of the screen and constellation of LED lights.")
        look()

       


# Potato ###################################################################################################



@when('use terminal')
@when('turn on computer')
@when('use computer')
def use_terminal():
    old_terminal = OldTerminal( '192.168.171.116', 'null','y3ll0wIceCre@m')
    old_terminal.enter()

armory = Room('''You push open the door, made of a shimmering metal that seems to writhe and twist under the light. 
It's as if it's alive, you find yourself in an ancient armory. The room is filled with debris and the remnants
of long-abandoned weapons racks. Many of the wooden racks have collapsed and are now rotting away, 
adding to the musty and 
decaying atmosphere of the room. It's clear that this armory has been thoroughly plundered, the 
once proud armaments of the warriors that wielded them now nothing more than a pile of debris on 
the ground. All that remains amidst the ruin is a single rusted sword and shield, propped up in a 
corner, as if forgotten by the looters. The sword's blade is dulled and chipped and the shield is 
dented and scarred, a testament to battles fought long ago. As you look around the room, you can't 
help but feel a sense of unease, as if the spirits of the warriors who once manned this armory still 
linger, resentful of the intrusion and the looting of their once-proud armaments. ''', '''You are
in the armory. Dust motes and the smell of the decaying weapons racks hang in the air.''')

#Define Connections, there's a function that allows the reverse, so if a room has north from the entered room south to return
starting_room.south = cave_down
cave_down.south = four_chamber
four_chamber.west = shrine_room
four_chamber.south = terminal_room
four_chamber.east = armory



#### Get rid of these items and put your own ####
#Define Items
inventory = Bag()


#Add Items to Rooms
flashlight = Item('flashlight')
inventory.add(flashlight)
flashlight.description = 'A simple Black and Dekker flashlight. It takes two D batteries.'

rusty_sword = Item('rusty sword', 'sword')
armory.items.add(rusty_sword)
rusty_sword.description = '''The sword in your hand is far from impressive. 
The blade is dull and covered in rust, having seen better days. 
The edge is nicked and chipped,
The hilt is wrapped in what was once leather, now rotted and frayed, 
offering little comfort to the hand that wields it.'''

dented_shield = Item('dented shield', 'shield', 'old shield')
armory.items.add(dented_shield)
dented_shield.description = '''You behold a battered and scarred shield, which bears the signs of countless battles fought and won.
The metal is dented and dull, as though it has absorbed the blows of countless enemies'''

flamethrower = Item('Flame Thrower', 'flamethrower')
armory.items.add(flamethrower)
flamethrower.description = "It's a can of air freshener lighter in the shape of a gun ducktaped together."

shrine_scroll = Item('scroll')
shrine_room.items.add(shrine_scroll)
shrine_scroll.description = "A scroll,parchment is yellowed and brittle, and you can barely make out the arcane symbols etched it's broken seal. "

chips = Item('bag of chips', 'chips')
terminal_room.items.add(chips)
chips.description = "Just a goddamned bag of Lay's Potato Chips"

#starting_room.items.add(key)
#Define any Variables
#binds and funtions 



@when('north', direction='north')
@when('south', direction='south')
@when('east', direction='east')
@when('west', direction='west')
def go(direction):
    global current_room
    room = current_room.exit(direction)
    if room:
        current_room = room
        say(f'You go {direction}.')
        look()
    else:
        print("I'm afraid you can't go that way.")

@when('look')
def look():
    if current_room.first_visit:
        current_room.first_visit = False
        say(current_room)
    else:
        say(current_room.sub_description) 
    if current_room.items:
        for Item in current_room.items:
            say(f'A {Item} is here.')
    
@when('exits')
def exits():
    x = 'You can go '
    x+= ', '.join(current_room.exits())
    x+= '.'
    print(x) 

@when('get ITEM')
@when('take ITEM')
def take(item):
    obj = current_room.items.take(item)
    if obj:
        say(f'You pick up the {obj}')
        inventory.add(obj)
    else:
        say(f'There is no {item} here')

@when('look at ITEM')
def look_item(item):
    if inventory.find(item):
        i = inventory.find(item)
        print(i.description)


# so when any of the three below are entered it will activate the same functions below them
@when('search body')
@when('look at body')
@when('look body')
def search_body():
    if current_room == magic_forest:
        print('You search the corpse and find NOTHING! But while you search his body shifts and underneath, you find chips!')
        magic_forest.items.add(chips)

@when('drop THING')
def drop(thing):
    obj = inventory.take(thing)
    if not obj:
        say('You do not have a %s.' % thing)
    else:
        say('You drop the %s.' % obj)
        current_room.items.add(obj)

@when('inventory')
def show_inventory():
    say('You have:')
    for thing in inventory:
        say(thing)

# Main
def main():
    look()
    start()

if __name__ == '__main__':
    main()