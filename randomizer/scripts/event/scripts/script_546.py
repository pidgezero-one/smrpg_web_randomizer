# E0546_ROSE_TOWN_OCCUPIED_BLUE_TOAD_RIGHT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI0814_CANT_CHOP_WOOD, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
