# E3211_SHIP_3D_MAZE_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	ApplyTileModToLevel(use_alternate=True, room_id=R168_SUNKEN_SHIP_PUZZLE_ROOM_3, mod_id=32),
	SummonObjectToCurrentLevel(NPC_0),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	RunBackgroundEvent(event_id=E3212_SHIP_3D_MAZE_FORFEIT_LISTENER, return_on_level_exit=True),
	RunDialog(dialog_id=DI1657_3D_MAZE_OVERLAY, above_object=BOWSER, closable=False, sync=True, multiline=False, use_background=False),
	Return()
])
