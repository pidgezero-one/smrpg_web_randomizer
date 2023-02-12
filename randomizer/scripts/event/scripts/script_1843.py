# E1843_KEEP_INVISIBLE_FLOOR_SHOW_FLOOR

from randomizer.scripts.event.script_imports import *

script = EventScript([
	PrioritySet(mainscreen=[LAYER_1, LAYER_2, NPC_SPRITES], subscreen=[], colour_math=[LAYER_1, LAYER_2, NPC_SPRITES, HALF_INTENSITY]),
	Return()
])
