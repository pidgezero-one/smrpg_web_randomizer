# E1549_SKY_BRIDGE_DONUT_LIFT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetBit(TEMP_7043_4),
	JmpIfBitSet(SKY_BRIDGE_COURSE_1_CHOSEN, ["EVENT_1549_jmp_if_bit_set_3"]),
	SetSyncActionScript(MEM_70A8, A0172_ENDING_CUTSCENE_SPARKLES),
	JmpIfBitSet(SKY_BRIDGE_COURSE_CHOICE, ["EVENT_1846_jmp_if_bit_set_0"], identifier="EVENT_1549_jmp_if_bit_set_3"),
	RunEventAsSubroutine(E1840_PLATFORM_SUBROUTINE),
	Return()
])
