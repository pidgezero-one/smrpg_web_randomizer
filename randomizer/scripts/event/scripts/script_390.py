# E0390_MUSHROOM_KINGDOM_OCCUPIED_LEFT_STAIRWAY_TOAD

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI0660_TOO_SCARED_TO_PASS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
