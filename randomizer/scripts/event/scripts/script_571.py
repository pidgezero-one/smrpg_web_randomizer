# E0571_ROSE_TOWN_LIBERATED_YELLOW_TOAD

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI0870_THREE_INVISIBLE_ITEMS_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
