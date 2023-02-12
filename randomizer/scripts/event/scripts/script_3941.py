# E3941_RIVER_RING

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI2097_GOT_RING, above_object=BOWSER, closable=False, sync=False, multiline=False, use_background=False),
	Inc(UNUSED_70B2),
	AddToInventory(Ring),
	Return()
])
