# E3346_VOLCANO_1ST_BOSS_SCREEN_TINT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	TintLayers(layers=[LAYER_1, LAYER_2, LAYER_3, LAYER_4, NPC_SPRITES, BACKGROUND], red=128, green=32, blue=32, speed=4, bit_7=True, identifier="EVENT_3346_tint_layers_0"),
	Pause(8),
	TintLayers(layers=[LAYER_1, LAYER_2, LAYER_3, LAYER_4, NPC_SPRITES, BACKGROUND], red=0, green=0, blue=0, speed=4, bit_7=True),
	Pause(8),
	ResetPrioritySet(),
	Jmp(["EVENT_3346_tint_layers_0"])
])
