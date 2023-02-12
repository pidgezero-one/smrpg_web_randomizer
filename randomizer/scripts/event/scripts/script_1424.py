# E1424_MUSHROOM_WAY_2_LONE_TROOPA

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E1604_EXP_STAR_SUBROUTINE_CANCEL_NPC_EVENT_REMOVE_FROM_LEVEL),
	StartBattleAtBattlefield(4, BF33_PLATEAUS),
	SetBit(TEMP_707C_5),
	SetBit(TEMP_707C_6),
	SetBit(TEMP_707C_7),
	RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
	FadeInFromBlack(sync=False),
	Return()
])
