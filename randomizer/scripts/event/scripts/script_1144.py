# E1144_SHED_WINDOW

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI2849_OCCUPIED_SEASIDE_WINDOW, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	Return()
])
