# E1701_BANDITS_WAY_2_RIGHT_PLATFORM

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_5, ["EVENT_1701_ret_19"]),
	PlaySound(sound=SO058_INSERT, channel=6),
	SetBit(TEMP_7043_5),
	EnableControlsUntilReturn([]),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_1701_pause_action_script_9"]),
	SetBit(TEMP_7043_3),
	SetBit(TEMP_7043_1),
	ClearBit(TEMP_7043_2),
	RunBackgroundEvent(event_id=E1705_BANDITS_WAY_2_DOGS_BACKGROUND, return_on_level_exit=True),
	PauseActionScript(NPC_7, identifier="EVENT_1701_pause_action_script_9"),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 27),
	JmpIfLoadedMemoryIsNot0(["EVENT_1701_set_14"]),
	AddConstToVar(SECONDARY_TEMP_7024, 128),
	SetVarToConst(TEMP_70A9, 27, identifier="EVENT_1701_set_14"),
	SetVarToConst(ROSE_WAY_703E, 27),
	SetSyncActionScript(NPC_6, A0478_BANDITS_WAY_1ST_PLATFORMS_SWING),
	Pause(34),
	SetSyncActionScript(NPC_6, A0477_BANDITS_WAY_1ST_PLATFORMS_STATIC),
	Return(identifier="EVENT_1701_ret_19")
])
