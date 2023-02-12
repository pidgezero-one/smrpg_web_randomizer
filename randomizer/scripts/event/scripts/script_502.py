# E0502_PIPE_VAULT_CROUCH_ITEM_INIT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	MoveScriptToBackgroundThread2(),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_256_ret_0"]),
	SetBit(TEMP_7043_0),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
	SetVarToConst(TIMER_701C, 24),
	RunBackgroundEventWithPauseReturnOnExit(event_id=E0509_PIPE_VAULT_CROUCH_ITEM_RESET, timer_var=TIMER_701C),
	MoveScriptToMainThread(),
	Return()
])
