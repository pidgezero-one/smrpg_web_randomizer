# E2534_STAR_HILL_2ND_ROOM_WISH_TOP_RIGHT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	PlaySound(sound=SO110_ABSTRACT_MUSIC, channel=6),
	RunDialog(dialog_id=DI3110_WISH_6, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	PlaySound(sound=SO000_SILENCE, channel=6),
	Return()
])
