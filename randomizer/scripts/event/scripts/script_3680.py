# E3680_NIMBUS_CASTLE_EGG_POST_DEFEAT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E1603_EXP_STAR_SUBROUTINE_CANCEL_TILE_EVENT),
	JmpIfBitSet(NIMBUS_MID_BOSS_COMPLETED, ["EVENT_3680_run_dialog_35"]),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	SetBit(TEMP_704A_2),
	RunEventAsSubroutine(E1011_POST_MINES_BOSS_CHECK_IF_WON),
	SetBit(NIMBUS_MID_BOSS_COMPLETED),
	RestoreAllHP(),
	RestoreAllFP(),
	FadeInFromBlack(sync=False),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	Return(),
	RunDialog(dialog_id=DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING, above_object=MARIO, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_3680_run_dialog_35"),
	Return()
])
