# E1831_KEEP_INVISIBLE_FLOOR_ROOM_BACKGROUND_1

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Pause(1, identifier="EVENT_1831_pause_0"),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_1831_set_bit_3"]),
	Jmp(["EVENT_1831_pause_0"]),
	SetBit(TEMP_7043_2, identifier="EVENT_1831_set_bit_3"),
	ClearBit(TEMP_7043_1),
	PrioritySet(mainscreen=[LAYER_1, LAYER_2, NPC_SPRITES], subscreen=[LAYER_3], colour_math=[LAYER_1, LAYER_2, NPC_SPRITES, HALF_INTENSITY]),
	Pause(6),
	PrioritySet(mainscreen=[LAYER_1, LAYER_2, NPC_SPRITES], subscreen=[], colour_math=[LAYER_1, LAYER_2, NPC_SPRITES, HALF_INTENSITY]),
	ClearBit(TEMP_7043_2),
	Jmp(["EVENT_1831_pause_0"])
])
