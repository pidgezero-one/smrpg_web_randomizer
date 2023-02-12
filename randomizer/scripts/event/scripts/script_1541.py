# E1541_UNKNOWN

from randomizer.scripts.event.script_imports import *

script = EventScript([
	ClearBit(UNKNOWN_707B_4),
	ClearBit(MIDAS_RIVER_TUNNEL_1_BIT),
	Pause(1, identifier="EVENT_1541_pause_2"),
	Set7000ToTappedButton(),
	JmpIf7000AllBitsClear(destinations=["EVENT_1541_pause_2"]),
	JmpIf7000AnyBitsSet(destinations=["EVENT_1541_set_bit_8"]),
	JmpIf7000AnyBitsSet(destinations=["EVENT_1541_set_bit_10"]),
	Return(),
	SetBit(UNKNOWN_707B_4, identifier="EVENT_1541_set_bit_8"),
	Return(),
	SetBit(MIDAS_RIVER_TUNNEL_1_BIT, identifier="EVENT_1541_set_bit_10"),
	Return()
])
