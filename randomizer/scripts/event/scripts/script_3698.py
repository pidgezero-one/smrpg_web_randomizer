# E3698_NIMBUS_CASTLE_WEST_LOWER_HALL_PINWHEEL

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E1604_EXP_STAR_SUBROUTINE_CANCEL_NPC_EVENT_REMOVE_FROM_LEVEL),
	StartBattleAtBattlefield(96, BF22_NIMBUS_CASTLE),
	RunEventAsSubroutine(E1008_POST_MINES_BOSS_SUBROUTINE),
	JmpIfBitSet(RUN_AWAY, ["EVENT_3698_ret_6"]),
	StopAllBackgroundEvents(),
	ClearBit(TEMP_7043_0),
	SetSyncActionScript(MARIO, A0814_MARIO_BLOWN_BY_FAN),
	Return(identifier="EVENT_3698_ret_6")
])
