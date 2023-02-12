# E3678_ROYAL_BUS_ATTENDANT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI3725_KEEP_ACCESS_HINT, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	RunDialog(dialog_id=DI3726_KEEP_ACCESS_HINT, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Return()
])
