# E0655_MARRYMORE_GEAR_GRANT_CROWN

from randomizer.scripts.event.script_imports import *

script = EventScript([
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	RemoveObjectFromCurrentLevel(NPC_5),
	RunDialog(dialog_id=DI2098_GOT_CROWN, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
	Inc(UNUSED_70B2),
	Return()
])
