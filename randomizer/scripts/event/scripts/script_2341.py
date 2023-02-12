# E2341_TOWER_SEESAW_CHEST

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_0, ["EVENT_2341_ret_3"]),
	SetBit(TEMP_7043_0),
	RunBackgroundEvent(event_id=E2342_TOWER_SEESAW_CHEST_CONTD, return_on_level_exit=True),
	Return(identifier="EVENT_2341_ret_3")
])
