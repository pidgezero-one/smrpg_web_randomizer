# E2595_ABYSS_SAVE_ROOM_WITH_CHEST_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToConst(FACTORY_FALL_1, 237),
	JmpIfBitClear(TEMP_7044_7, ["EVENT_2595_fade_in_from_black_async_6"]),
	RunEventAsSubroutine(E0081_MARIO_LANDS_SUBROUTINE),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2595_ret_13"]),
	RunEventAsSubroutine(E3915_FACTORY_STAR_PIECE_SIGNAL),
	Jmp(["EVENT_2595_ret_13"]),
	FadeInFromBlack(sync=False, identifier="EVENT_2595_fade_in_from_black_async_6"),
	Return(identifier="EVENT_2595_ret_13")
])
