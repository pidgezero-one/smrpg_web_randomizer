# E3637_TEMPLE_BACKDOOR_LOCKED

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI2811_ITS_LOCKED, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	Return()
])
