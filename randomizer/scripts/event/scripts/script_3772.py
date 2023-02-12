# E3772_HOT_SPRINGS_WATER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_1, ["EVENT_3584_ret_0"]),
	SetBit(TEMP_7043_1),
	RestoreAllHP(),
	RestoreAllFP(),
	RunEventAsSubroutine(E3075_HEAL_FLASH),
	SetVarToConst(TIMER_701C, 240),
	RunBackgroundEventWithPauseReturnOnExit(event_id=E3773_HOT_SPRINGS_EJECT_FROM_WATER, timer_var=TIMER_701C),
	Return()
])
