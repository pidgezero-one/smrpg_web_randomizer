# E3335_CORKPEDITE_COLLISION

from randomizer.scripts.event.script_imports import *

script = EventScript([
	StopAllBackgroundEvents(),
	JmpIfBitClear(TEMP_7076_0, ["EVENT_3335_start_battle_3"]),
	JmpToEvent(E0255_EXP_STAR_HIT),
	StartBattleAtBattlefield(145, BF20_BARREL_VOLCANO, identifier="EVENT_3335_start_battle_3"),
	JmpIfBitSet(RUN_AWAY, ["EVENT_3335_set_temp_action_script_sync_12"]),
	JmpIfBitSet(GAME_OVER, ["EVENT_3335_reset_and_choose_game_16"]),
	SetAsyncActionScript(MEM_70A8, A1023_ERUPTED_MAGMITES),
	RemoveObjectFromCurrentLevel(MEM_70A8),
	DisableObjectTrigger(MEM_70A8),
	Pause(2),
	FadeInFromBlack(sync=False),
	Return(),
	SetTempSyncActionScript(MEM_70A8, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES, identifier="EVENT_3335_set_temp_action_script_sync_12"),
	RunBackgroundEvent(event_id=E3337_CORKPEDITE_ANIMATION, return_on_level_exit=True),
	FadeInFromBlack(sync=False),
	Return(),
	ResetAndChooseGame(identifier="EVENT_3335_reset_and_choose_game_16")
])
