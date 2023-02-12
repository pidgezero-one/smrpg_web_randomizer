# E2210_KEEP_1ST_BOSS_HEALS_YOU

from randomizer.scripts.event.script_imports import *

script = EventScript([
	PlaySound(sound=SO071_MUSHROOM_CURE, channel=6),
	TintLayers(layers=[LAYER_1, LAYER_2, LAYER_3, LAYER_4, NPC_SPRITES, BACKGROUND], red=64, green=160, blue=64, speed=3, bit_7=True),
	TintLayers(layers=[LAYER_1, LAYER_2, LAYER_3, LAYER_4, NPC_SPRITES, BACKGROUND], red=0, green=0, blue=0, speed=3, bit_7=True),
	ResetPrioritySet(),
	RestoreAllHP(),
	RestoreAllFP(),
	Return()
])
