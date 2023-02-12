# E1811_TEMPLE_FOUR_CHEST_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	ClearBit(TEMPLE_ELEVATOR_DIRECTION),
	RunEventAsSubroutine(E1844_SUMMON_CLOUD_BOSS),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	Return()
])
