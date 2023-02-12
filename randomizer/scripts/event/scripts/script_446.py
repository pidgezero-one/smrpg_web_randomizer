# E0446_GOOMBA_THUMPIN_SCOREKEEPING

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Dec(TEMP_7026),
	JmpIfVarEqualsConst(TEMP_7026, 10, ["EVENT_446_set_7000_to_7000_short_mem_23"]),
	JmpIfVarEqualsConst(TEMP_7026, 0, ["EVENT_446_run_dialog_6"], identifier="EVENT_446_jmp_if_var_equals_const_2"),
	CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
	RunDialog(dialog_id=DI0835_DUPLICATE, above_object=MARIO, closable=False, sync=True, multiline=True, use_background=False),
	Jmp(["EVENT_446_set_short_20"]),
	RunDialog(dialog_id=DI0866_X_POINTS, above_object=MARIO, closable=False, sync=True, multiline=True, use_background=False, identifier="EVENT_446_run_dialog_6"),
	StopAllBackgroundEvents(),
	Db(bytearray(b'\xfdD')),
	UnfreezeCamera(),
	FadeOutMusicToVolume(duration=2, volume=0),
	ClearBit(TEMP_7044_6),
	SetBit(TEMP_7044_5),
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	SetBit(UNKNOWN_7083_7),
	SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Pause(1, identifier="EVENT_446_pause_16"),
	JmpIfMarioInAir(["EVENT_446_pause_16"]),
	PlayMusicAtDefaultVolume(M07_PIPE_VAULT),
	Return(),
	SetVarToConst(TIMER_701C, 80, identifier="EVENT_446_set_short_20"),
	RunBackgroundEventWithPauseReturnOnExit(event_id=E0446_GOOMBA_THUMPIN_SCOREKEEPING, timer_var=TIMER_701C),
	Return(),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000, identifier="EVENT_446_set_7000_to_7000_short_mem_23"),
	CompareVarToConst(PRIMARY_TEMP_7000, 20),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_446_set_bit_27"]),
	Jmp(["EVENT_446_jmp_if_var_equals_const_2"]),
	SetBit(TEMP_7049_6, identifier="EVENT_446_set_bit_27"),
	Jmp(["EVENT_446_jmp_if_var_equals_const_2"])
])
