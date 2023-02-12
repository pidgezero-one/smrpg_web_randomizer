# E0209_UNLOCK_SWITCH_MENU_IF_ENOUGH_MEMBERS

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetObjectMemoryToVar(),
	CompareVarToConst(PRIMARY_TEMP_7000, 4),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_209_set_switch_menu"]),
	Return(),
	SetBit(SWITCH_MENU_UNLOCKED, identifier="EVENT_209_set_switch_menu"),
	Return()
])
