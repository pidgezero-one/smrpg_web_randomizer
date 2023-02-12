# E3224_SHIP_PASSWORD_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SummonObjectToCurrentLevel(NPC_0),
	SummonObjectToCurrentLevel(NPC_1),
	SummonObjectToCurrentLevel(NPC_2),
	SummonObjectToCurrentLevel(NPC_3),
	SummonObjectToCurrentLevel(NPC_4),
	SummonObjectToCurrentLevel(NPC_5),
	ResumeActionScript(NPC_0),
	ResumeActionScript(NPC_1),
	ResumeActionScript(NPC_2),
	ResumeActionScript(NPC_3),
	ResumeActionScript(NPC_4),
	ResumeActionScript(NPC_5),
	SetVarToConst(SECONDARY_TEMP_7024, 0),
	SetVarToConst(TEMP_7026, 0),
	SetVarToConst(TEMP_7028, 0),
	SetVarToConst(TEMP_702A, 0),
	SetVarToConst(TEMP_702C, 0),
	SetVarToConst(TEMP_702E, 0),
	SetVarToConst(TEMP_70AC, 0),
	RunEventAsSubroutine(E0800_SHIP_PASSWORD_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
	JmpIfBitClear(TEMP_7042_6, ["EVENT_3224_run_event_as_subroutine_12"]),
	ApplySolidityModToLevel(permanent=True, room_id=R177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM, mod_id=0),
	ApplyTileModToLevel(use_alternate=True, room_id=R177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM, mod_id=32),
	SetBit(TEMP_7043_0),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3224_run_event_as_subroutine_12"),
	RunBackgroundEvent(event_id=E3225_SHIP_PASSWORD_BOX_DIALOG, return_on_level_exit=True),
	Return()
])
