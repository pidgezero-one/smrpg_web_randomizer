# E2822_CLONE_RESERVED

from randomizer.scripts.event.script_imports import *

script = EventScript([
	DisableObjectTrigger(MEM_70A8),
	RemoveObjectFromCurrentLevel(MEM_70A8),
	PlaySound(sound=SO014_FLOWER, channel=6),
	MoveScriptToBackgroundThread2(),
	RestoreAllHP(),
	RestoreAllFP(),
	TintLayers(layers=[LAYER_2, LAYER_3, LAYER_4, NPC_SPRITES, BACKGROUND], red=64, green=160, blue=64, speed=3, bit_7=True),
	TintLayers(layers=[LAYER_2, LAYER_3, LAYER_4, NPC_SPRITES, BACKGROUND], red=0, green=0, blue=0, speed=3, bit_7=True),
	ResetPrioritySet(),
	MoveScriptToMainThread(),
	Return()
])
