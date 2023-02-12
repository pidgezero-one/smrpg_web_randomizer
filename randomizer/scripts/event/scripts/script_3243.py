# E3243_SHIP_COIN_SNAKE_HINT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetSyncActionScript(MEM_70A8, A0340_SHIP_PUZZLE_HINT_VANISH),
	RunDialog(dialog_id=DI1667_SNAKE_PUZZLE_HINT, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Return()
])
