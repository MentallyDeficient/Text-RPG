from adventurelib import Room

Room.items = []

entrance = Room("""The cave entrance is hidden behind a large tree,
its gnarled roots creeping out of the ground like tentacles.
...""", """ENTRANCE. The tree limbs and vines...""")

cave_down = Room("""As you make your way down the narrow, winding path...""", """CAVE: Slopes up and down...""")
four_chamber = Room("""With a sense of dread and foreboding...""", """FOUR CHAMBER ROOM. Glass globe glows...""")
shrine_room = Room("""The door creaked open to reveal a small, dimly lit chamber...""", """SHRINE ROOM. The shrine remains...""")
terminal_room = Room("""You step inside the computer terminal room, wires crisscross...""", """COMPUTER ROOM. Terminal hums...""")
armory = Room("""You push open the door of shimmering metal...""", """ARMORY. Dust motes float...""")

# Connect rooms
entrance.south = cave_down
cave_down.south = four_chamber
four_chamber.west = shrine_room
four_chamber.south = terminal_room
four_chamber.east = armory
