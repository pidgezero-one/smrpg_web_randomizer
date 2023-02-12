# E3940_RIVER_BROOCH

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI2095_GOT_BROOCH, above_object=BOWSER, closable=False, sync=False, multiline=False, use_background=False),
	Inc(UNUSED_70B2),
	AddToInventory(Brooch),
	Return()
])
