# E3939_RIVER_SHOES

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI2096_GOT_SHOES, above_object=BOWSER, closable=False, sync=False, multiline=False, use_background=False),
	AddToInventory(Shoes),
	Inc(UNUSED_70B2),
	Return()
])
