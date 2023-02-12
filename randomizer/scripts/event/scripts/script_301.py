# E0301_MUSHROOM_KINGDOM_MOM

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI0538_KINGDOM_SUPER_JUMP_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
