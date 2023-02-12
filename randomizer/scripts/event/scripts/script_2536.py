# E2536_STAR_HILL_3RD_ROOM_WISH_TOP_LEFT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	PlaySound(sound=SO110_ABSTRACT_MUSIC, channel=6),
	RunDialog(dialog_id=DI3107_WISH_3, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False),
	PlaySound(sound=SO000_SILENCE, channel=6),
	Return()
])
