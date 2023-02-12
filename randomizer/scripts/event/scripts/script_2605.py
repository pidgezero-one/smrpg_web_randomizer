# E2605_FACTORY_1ST_ROOM_BEFORE_FIGHT_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 1),
	JmpIfBitClear(FAST_TRAVEL_ENABLED, ["EVENT_2605_sequence_setter"]),
	SummonObjectToCurrentLevel(NPC_9),
	RunEventAsSubroutine(E0855_INNER_FACTORY_1ST_ROOM_SHUFFLED_NPC_ANIMATION_LOADER, identifier="EVENT_2605_sequence_setter"),
	FadeInFromBlack(sync=False),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_2605_ret_4"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2605_ret_4"]),
	RunEventAsSubroutine(E3916_INNER_FACTORY_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_2605_ret_4")
])
