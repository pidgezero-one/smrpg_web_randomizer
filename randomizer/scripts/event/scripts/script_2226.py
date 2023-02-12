# E2226_KEEP_3RD_BOSS

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Pause(10),
	SetVarToConst(PRIMARY_TEMP_7000, 522),
	RunEventAsSubroutine(E0353_BOSS_BATTLE),
	JmpIfBitClear(GAME_OVER, ["EVENT_2226_restore_all_hp_22"]),
	ResetAndChooseGame(),
	RestoreAllHP(identifier="EVENT_2226_restore_all_hp_22"),
	RestoreAllFP(),
	SetBit(KEEP_BOSS_3_DEFEATED),
	SetBit(BATTLE_DOOR_STAR_PIECE),
	SetVarToConst(PRIMARY_TEMP_7000, 522),
	JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE),
	StopSound(),
	JmpToEvent(E2149_KEEP_RESUMMON_ENEMIES_ON_EXIT),
	Return()
])
