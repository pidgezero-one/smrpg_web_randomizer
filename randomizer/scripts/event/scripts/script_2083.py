# E2083_MUSTY_FEARS_AWAY_NOTE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI3004_MUSTY_FEARS_NO_HUNT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
