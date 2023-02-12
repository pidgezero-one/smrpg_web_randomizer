# E3933_GET_RING

from randomizer.scripts.event.script_imports import *

script = EventScript([
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	RunDialog(dialog_id=DI2097_GOT_RING, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	Inc(UNUSED_70B2),
	AddToInventory(Ring),
	Return()
])
