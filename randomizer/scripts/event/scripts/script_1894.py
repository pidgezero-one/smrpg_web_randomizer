# E1894_ABYSS_BOSS_2

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Pause(8),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	SetBit(TEMP_707C_5),
	ClearBit(TEMP_707C_6),
	ClearBit(TEMP_707C_7),
	RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
	ApplySolidityModToLevel(permanent=True, room_id=R103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM, mod_id=32),
	FadeInFromBlack(sync=False),
	RestoreAllHP(),
	RestoreAllFP(),
	SetBit(ABYSS_BOSS_2_DEFEATED),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	Return()
])
