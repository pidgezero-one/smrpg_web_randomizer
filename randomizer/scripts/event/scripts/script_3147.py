# E3147_ROSE_WAY_TUTORIAL

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI1599_DUPLICATE, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	Return()
])
