# E0292_MUSHROOM_KINGDOM_WEST_BLUE_TOAD

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI0530_MUSHROOM_KINGDOM_NPC, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
