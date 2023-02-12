# E2345_TOWER_THWOMP_SEESAW

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_0, ["EVENT_2345_ret_3"]),
	SetBit(TEMP_7043_0),
	RunBackgroundEvent(event_id=E2346_TOWER_THWOMP_SEESAW_CONTD, return_on_level_exit=True),
	Return(identifier="EVENT_2345_ret_3")
])
