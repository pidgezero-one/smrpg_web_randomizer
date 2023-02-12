# E2426_FOREST_MUSHROOM_PICKUP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	FreezeAllNPCsUntilReturn(),
	RemoveObjectAt70A8FromCurrentLevel(),
	RemoveObjectFromCurrentLevel(MEM_70A8),
	Pause(1),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	Pause(1),
	RunEventAsSubroutine(E0021_FOREST_MAZE_MUSHROOM_GRANT),
	RunDialog(dialog_id=DI3213_PICKED_UP_A_70A7, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	Pause(1),
	AddToInventory(ITEM_ID),
	UnfreezeAllNPCs(),
	Return()
])
