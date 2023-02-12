# E1274_SHIP_BOSS_ROOM_RIGHTMOST_HENCHMAN

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI1793_SHIP_BOSS_SIDEKICK_IN_ROOM_4, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
