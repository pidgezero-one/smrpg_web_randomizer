# E1705_BANDITS_WAY_2_DOGS_BACKGROUND

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Pause(1, identifier="EVENT_1705_pause_0"),
	JmpIfMarioInAir(["EVENT_1705_clear_bit_3"]),
	Jmp(["EVENT_1705_pause_0"]),
	ClearBit(TEMP_7043_5, identifier="EVENT_1705_clear_bit_3"),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_1705_pause_13"]),
	SetBit(TEMP_7043_1),
	ClearBit(TEMP_7043_2),
	SetVarToConst(TEMP_70AB, 20),
	StartLoopNTimes(1),
	JmpIfObjectInCurrentLevel(MEM_70AB, ["EVENT_1705_inc_11"]),
	SetSyncActionScript(MEM_70AB, A0474_BANDITS_WAY_2_CHEST_ROOM_CHEST),
	Inc(TEMP_70AB, identifier="EVENT_1705_inc_11"),
	EndLoop(),
	Pause(1, identifier="EVENT_1705_pause_13"),
	JmpIfMarioInAir(["EVENT_1705_pause_13"]),
	Set7000ToObjectCoord(object=MARIO, coord=COORD_Z, pixel=True, bit_7=True),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1705_pause_0"]),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_1705_pause_0"]),
	SetBit(TEMP_7043_2),
	ClearBit(TEMP_7043_1),
	SetVarToConst(TEMP_70AB, 20),
	StartLoopNTimes(1),
	JmpIfObjectInCurrentLevel(MEM_70AB, ["EVENT_1705_inc_24"]),
	SetSyncActionScript(MEM_70AB, A0475_CHOW_UNKNOWN),
	Inc(TEMP_70AB, identifier="EVENT_1705_inc_24"),
	EndLoop(),
	Jmp(["EVENT_1705_pause_0"])
])
