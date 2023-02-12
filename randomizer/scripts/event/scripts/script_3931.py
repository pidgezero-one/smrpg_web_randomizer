# E3931_GET_SHOES

from randomizer.scripts.event.script_imports import *

script = EventScript([
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	RunDialog(dialog_id=DI2096_GOT_SHOES, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	AddToInventory(Shoes),
	Inc(UNUSED_70B2),
	Return()
])
