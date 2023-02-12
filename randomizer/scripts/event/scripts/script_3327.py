# E3327_STUMPET_FIGHT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E1603_EXP_STAR_SUBROUTINE_CANCEL_TILE_EVENT),
	StopAllBackgroundEvents(),
	StartBattleAtBattlefield(144, BF20_BARREL_VOLCANO),
	JmpIfBitSet(RUN_AWAY, ["EVENT_3327_set_temp_action_script_sync_13"]),
	JmpIfBitSet(GAME_OVER, ["EVENT_3327_reset_and_choose_game_22"]),
	MoveScriptToMainThread(),
	SetAsyncActionScript(NPC_0, A1023_ERUPTED_MAGMITES),
	SetAsyncActionScript(NPC_1, A1023_ERUPTED_MAGMITES),
	SetAsyncActionScript(NPC_2, A1023_ERUPTED_MAGMITES),
	SetAsyncActionScript(NPC_3, A1023_ERUPTED_MAGMITES),
	SetAsyncActionScript(NPC_4, A1023_ERUPTED_MAGMITES),
	SetAsyncActionScript(NPC_5, A1023_ERUPTED_MAGMITES),
	FadeInFromBlack(sync=False),
	Return(),
	SetTempSyncActionScript(NPC_0, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES, identifier="EVENT_3327_set_temp_action_script_sync_13"),
	SetSyncActionScript(NPC_1, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
	SetSyncActionScript(NPC_2, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
	SetSyncActionScript(NPC_3, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
	SetSyncActionScript(NPC_4, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
	SetSyncActionScript(NPC_5, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
	RunBackgroundEvent(event_id=E3326_STUMPET_ERUPTION, return_on_level_exit=True),
	FadeInFromBlack(sync=False),
	Return(),
	ResetAndChooseGame(identifier="EVENT_3327_reset_and_choose_game_22")
])
