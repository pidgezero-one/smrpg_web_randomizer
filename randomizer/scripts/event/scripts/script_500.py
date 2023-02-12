# E0500_PIPE_VAULT_HIDDEN_PLATFORM

from randomizer.scripts.event.script_imports import *

script = EventScript([
	MoveScriptToBackgroundThread2(),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_256_ret_0"]),
	SetBit(TEMP_7043_1),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
	Set7000ToTappedButton(identifier="EVENT_500_set_7000_to_tapped_button_4"),
	JmpIfBitClear(TEMP_7043_1, ["EVENT_500_ret_14"]),
	JmpIf7000AnyBitsSet(destinations=["EVENT_500_jmp_if_present_in_current_level_9"]),
	Pause(1),
	Jmp(["EVENT_500_set_7000_to_tapped_button_4"]),
	JmpIfObjectInCurrentLevel(NPC_7, ["EVENT_500_play_sound_11"], identifier="EVENT_500_jmp_if_present_in_current_level_9"),
	Jmp(["EVENT_500_summon_to_current_level_12"]),
	PlaySound(sound=SO014_FLOWER, channel=6, identifier="EVENT_500_play_sound_11"),
	SummonObjectToCurrentLevel(NPC_7, identifier="EVENT_500_summon_to_current_level_12"),
	Return(),
	Return(identifier="EVENT_500_ret_14")
])
