# E1778_TEMPLE_GENERIC_PIPE_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitClear(TEMP_7076_0, ["EVENT_1778_run_event_as_subroutine_3"]),
	JmpIfBitSet(EXP_STAR_BIT_5, ["EVENT_1778_run_event_as_subroutine_3"]),
	SetVarToConst(TIMER_7022, 30),
	RunEventAsSubroutine(E1844_SUMMON_CLOUD_BOSS, identifier="EVENT_1778_run_event_as_subroutine_3"),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_1778_ret_26"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1778_ret_26"]),
	RunEventAsSubroutine(E3908_TEMPLE_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_1778_ret_26")
])
