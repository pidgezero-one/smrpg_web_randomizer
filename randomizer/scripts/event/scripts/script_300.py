# E0300_GENERIC_NO_HELP_MESSAGE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI2235_NO_ADVICE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
