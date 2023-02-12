# E0397_HEAL_IN_TOADSTOOLS_ROOM

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToConst(TIMER_7022, 8),
	RunBackgroundEventWithPause(event_id=E3075_HEAL_FLASH, timer_var=TIMER_7022),
	PlaySound(sound=SO071_MUSHROOM_CURE, channel=6),
	RestoreAllHP(),
	RestoreAllFP(),
	Return()
])
