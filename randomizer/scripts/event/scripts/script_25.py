# E0025_BATTLE_RESULT_CHECK_BLINKING

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(RUN_AWAY, ["EVENT_25_set_temp_action_script_sync_3"]),
	JmpIfBitSet(GAME_OVER, ["EVENT_24_reset_and_choose_game_17"]),
	Jmp(["EVENT_24_jmp_if_bit_clear_2"]),
	SetTempSyncActionScript(MEM_70A8, A0284_IFRAME_BLINK, identifier="EVENT_25_set_temp_action_script_sync_3"),
	JmpIfBitSet(TEMP_707C_5, ["EVENT_24_clear_bit_14"]),
	FadeInFromBlack(sync=False),
	Jmp(["EVENT_24_reactivate_trigger_if_mario_on_top_of_object_15"])
])
