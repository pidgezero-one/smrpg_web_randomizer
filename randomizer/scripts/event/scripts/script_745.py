# E0745_MUSHROOM_KINGDOM_INN_SLEEPING_GUY

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI2506_CASINO_SECRET_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
