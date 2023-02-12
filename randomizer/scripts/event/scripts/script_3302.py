# E3302_SHIP_BOSS_ROOM_INNER_RIGHT_HENCHMAN

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunDialog(dialog_id=DI1785_SHIP_BOSS_SIDEKICK_IN_ROOM_1, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	Return()
])
