# E0530_ROSE_TOWN_OCCUPIED_BACKGROUND_1

from randomizer.scripts.event.script_imports import *

script = EventScript([
	ClearBit(TEMP_7044_6, identifier="EVENT_530_clear_bit_0"),
	ClearBit(TEMP_7044_5),
	ClearBit(TEMP_7044_2),
	ClearBit(TEMP_7044_1),
	Pause(1, identifier="EVENT_530_pause_4"),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_530_run_event_as_subroutine_7"]),
	Jmp(["EVENT_530_pause_4"]),
	RunEventAsSubroutine(E0548_ROSE_TOWN_OCCUPIED_ARROW_ANIMATE, identifier="EVENT_530_run_event_as_subroutine_7"),
	JmpIfBitSet(TEMP_7044_5, ["EVENT_530_jmp_if_random_above_128_11"], identifier="EVENT_530_jmp_if_bit_set_8"),
	Pause(1),
	Jmp(["EVENT_530_jmp_if_bit_set_8"]),
	JmpIfRandom1of2(["EVENT_530_pause_14"], identifier="EVENT_530_jmp_if_random_above_128_11"),
	Pause(60),
	Jmp(["EVENT_530_clear_bit_0"]),
	Pause(30, identifier="EVENT_530_pause_14"),
	Jmp(["EVENT_530_clear_bit_0"])
])
