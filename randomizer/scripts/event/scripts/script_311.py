# E0311_MUSHROOM_KINGDOM_EAST_GUARD

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI2224_TOAD_GUARD, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
