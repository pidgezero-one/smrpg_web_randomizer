# E3932_GET_BROOCH

from randomizer.scripts.event.script_imports import *

script = EventScript([
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	RunDialog(dialog_id=DI2095_GOT_BROOCH, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	AddToInventory(Brooch),
	Inc(UNUSED_70B2),
	Return()
])
