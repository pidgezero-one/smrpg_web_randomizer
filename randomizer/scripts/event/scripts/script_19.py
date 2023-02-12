# E0019_FIGHT_REMOVE_PERMANENTLY_BLINK_ON_RUN

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitClear(TEMP_7076_0, ["EVENT_19_set_bit_2"]),
	JmpToEvent(E0255_EXP_STAR_HIT),
	SetBit(TEMP_707C_1, identifier="EVENT_19_set_bit_2"),
	JmpToSubroutine(["EVENT_16_disable_trigger_2"]),
	ClearBit(TEMP_707C_1),
	Return()
])
