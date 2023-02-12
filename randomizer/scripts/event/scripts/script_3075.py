# E3075_HEAL_FLASH

from randomizer.scripts.event.script_imports import *

script = EventScript([
	TintLayers(layers=[LAYER_1, LAYER_2, LAYER_3, LAYER_4, NPC_SPRITES, BACKGROUND], red=64, green=160, blue=64, speed=3, bit_7=True),
	TintLayers(layers=[LAYER_1, LAYER_2, LAYER_3, LAYER_4, NPC_SPRITES, BACKGROUND], red=0, green=0, blue=0, speed=3, bit_7=True),
	ResetPrioritySet(),
	Return()
])
