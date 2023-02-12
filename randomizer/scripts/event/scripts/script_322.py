# E0322_MUSHROOM_KINGDOM_THRONE_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Set0158Bit7Offset(),
	Set0158Bit7Offset(),
	FadeInFromBlack(sync=False),
	Return()
])
