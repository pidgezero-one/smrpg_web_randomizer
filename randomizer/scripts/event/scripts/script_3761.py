# E3761_NIMBUS_MEZZANINE_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 49),
	FadeInFromBlack(sync=False),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_3761_ret_4"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3761_ret_4"]),
	RunEventAsSubroutine(E3912_NIMBUS_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_3761_ret_4")
])
