# E1832_KEEP_INVISIBLE_FLOOR_ROOM_BACKGROUND_2

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Pause(1, identifier="EVENT_1832_pause_0"),
	JmpIfMarioInAir(["EVENT_1832_pause_3"]),
	Jmp(["EVENT_1832_pause_0"]),
	Pause(1, identifier="EVENT_1832_pause_3"),
	Set7000ToPressedButton(),
	JmpIf7000AnyBitsSet(destinations=["EVENT_1832_pause_13"]),
	JmpIfMarioInAir(["EVENT_1832_pause_3"]),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_1832_pause_0"]),
	PlaySound(sound=SO022_CLOSE_DOOR, channel=6),
	PrioritySet(mainscreen=[LAYER_1, LAYER_2, NPC_SPRITES], subscreen=[LAYER_3], colour_math=[LAYER_1, LAYER_2, NPC_SPRITES, HALF_INTENSITY]),
	Pause(6),
	PrioritySet(mainscreen=[LAYER_1, LAYER_2, NPC_SPRITES], subscreen=[], colour_math=[LAYER_1, LAYER_2, NPC_SPRITES, HALF_INTENSITY]),
	Jmp(["EVENT_1832_pause_0"]),
	Pause(1, identifier="EVENT_1832_pause_13"),
	JmpIfMarioInAir(["EVENT_1832_pause_13"]),
	Jmp(["EVENT_1832_pause_0"])
])
