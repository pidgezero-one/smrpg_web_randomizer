# E0723_MUSHROOM_KINGDOM_UNOCCUPIED_EXTERIOR_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Set0158Bit7Offset(),
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 10),
	PlaySound(sound=SO000_SILENCE, channel=4),
	FadeOutMusicToVolume(duration=1, volume=127),
	FadeInFromBlack(sync=False),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_723_ret_4"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_723_ret_4"]),
	RunEventAsSubroutine(E3889_MUSHROOM_KINGDOM_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_723_ret_4")
])
