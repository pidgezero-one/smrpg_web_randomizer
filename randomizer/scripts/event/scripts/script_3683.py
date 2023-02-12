# E3683_VINE_INSTRUCTIONS

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI3840_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
