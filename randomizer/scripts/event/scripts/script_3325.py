# E3325_STUMPET_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetSyncActionScript(NPC_6, A1023_ERUPTED_MAGMITES),
	SetSyncActionScript(NPC_7, A1023_ERUPTED_MAGMITES),
	SetSyncActionScript(NPC_8, A1023_ERUPTED_MAGMITES),
	SetSyncActionScript(NPC_9, A1023_ERUPTED_MAGMITES),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 390, ["EVENT_3325_jmp_if_object_not_in_level_9"]),
	JmpIfObjectNotInSpecificLevel(NPC_0, R386_VOLCANO_AREA_12_ERUPTING_STUMPET, ["EVENT_3325_ret_11"]),
	Jmp(["EVENT_3325_run_background_event_10"]),
	JmpIfObjectNotInSpecificLevel(NPC_0, R390_VOLCANO_AREA_16_ERUPTING_STUMPET, ["EVENT_3325_ret_11"], identifier="EVENT_3325_jmp_if_object_not_in_level_9"),
	RunBackgroundEvent(event_id=E3326_STUMPET_ERUPTION, return_on_level_exit=True, identifier="EVENT_3325_run_background_event_10"),
	Return(identifier="EVENT_3325_ret_11")
])
