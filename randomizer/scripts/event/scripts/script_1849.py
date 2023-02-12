# E1849_CANNONBALL_ROOM_BOMB_1_CONTD

from randomizer.scripts.event.script_imports import *

script = EventScript([
	MoveScriptToMainThread(),
	Db(bytearray(b'\xfdG')),
	RunEventAtReturn(E1847_CANNONBALL_ROOM_BOMB_1),
	Return()
])
