# E0543_ROSE_TOWN_OCCUPIED_KID_1

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI0821_KID_NOT_FROZEN, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
