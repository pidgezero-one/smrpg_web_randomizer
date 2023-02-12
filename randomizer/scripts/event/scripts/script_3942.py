# E3942_RIVER_CROWN

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI2098_GOT_CROWN, above_object=BOWSER, closable=False, sync=False, multiline=False, use_background=False),
	Inc(UNUSED_70B2),
	AddToInventory(Crown),
	Return()
])
