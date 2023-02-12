# E0569_ROSE_TOWN_LIBERATED_PINK_TOAD

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI0858_HIDDEN_NPCS_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
