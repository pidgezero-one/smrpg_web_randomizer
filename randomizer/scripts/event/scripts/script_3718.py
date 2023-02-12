# E3718_NIMBUS_CASTLE_ANGLED_PLANT_ROOM_RIGHT_FAN_BATTLE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E1604_EXP_STAR_SUBROUTINE_CANCEL_NPC_EVENT_REMOVE_FROM_LEVEL),
	StartBattleAtBattlefield(96, BF22_NIMBUS_CASTLE),
	RunEventAsSubroutine(E1008_POST_MINES_BOSS_SUBROUTINE),
	ClearBit(TEMP_7043_6),
	SetSyncActionScript(MARIO, A0814_MARIO_BLOWN_BY_FAN),
	Return()
])
