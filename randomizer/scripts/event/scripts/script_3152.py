# E3152_ROSE_WAY_FIVE_CHESTS

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfVarEqualsConst(ACTIVE_NPC, 21, ["EVENT_3152_set_bit_8"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 22, ["EVENT_3152_set_bit_12"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 23, ["EVENT_3152_set_bit_16"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 24, ["EVENT_3152_set_bit_20"]),
	SetBit(TEMP_7043_0),
	JmpToEvent(E0172_CHEST_1_CONTAINER),
	SetBit(TEMP_7043_1, identifier="EVENT_3152_set_bit_8"),
	JmpToEvent(E0173_CHEST_2_CONTAINER),
	SetBit(TEMP_7043_2, identifier="EVENT_3152_set_bit_12"),
	JmpToEvent(E0174_CHEST_3_CONTAINER),
	SetBit(TEMP_7043_3, identifier="EVENT_3152_set_bit_16"),
	JmpToEvent(E0175_CHEST_4_CONTAINER),
	SetBit(TEMP_7043_4, identifier="EVENT_3152_set_bit_20"),
	JmpToEvent(E0176_CHEST_5_CONTAINER)
])
