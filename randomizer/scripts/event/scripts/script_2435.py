# E2435_FOREST_MAZE_TRANSITION

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(DIRECTIONAL_7045_0, ["EVENT_2435_clear_bit_8"]),
	JmpIfBitSet(DIRECTIONAL_7045_1, ["EVENT_2435_clear_bit_8"]),
	JmpIfBitSet(DIRECTIONAL_7045_2, ["EVENT_2435_clear_bit_8"]),
	JmpIfBitSet(DIRECTIONAL_7045_3, ["EVENT_2435_clear_bit_8"]),
	JmpIfBitSet(DIRECTIONAL_7045_4, ["EVENT_2435_clear_bit_8"]),
	JmpIfBitSet(DIRECTIONAL_7045_6, ["EVENT_2435_set_bit_19"]),
	JmpIfBitSet(DIRECTIONAL_7045_7, ["EVENT_2435_set_bit_23"]),
	JmpIfBitSet(DIRECTIONAL_7046_0, ["EVENT_2435_clear_bit_8"]),
	ClearBit(DIRECTIONAL_7045_0, identifier="EVENT_2435_clear_bit_8"),
	ClearBit(DIRECTIONAL_7045_1),
	ClearBit(DIRECTIONAL_7045_2),
	ClearBit(DIRECTIONAL_7045_3),
	ClearBit(DIRECTIONAL_7045_4),
	ClearBit(DIRECTIONAL_7045_6),
	ClearBit(DIRECTIONAL_7045_7),
	ClearBit(DIRECTIONAL_7046_0),
	ClearBit(DIRECTIONAL_7046_1),
	EnterArea(room_id=R227_FOREST_MAZE_AREA_09_LEADS_TO_4PATH_MAZE, face_direction=SOUTHWEST, x=16, y=18, z=0, run_entrance_event=True),
	Return(),
	SetBit(DIRECTIONAL_7045_7, identifier="EVENT_2435_set_bit_19"),
	ClearBit(DIRECTIONAL_7045_6),
	EnterArea(room_id=R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09, face_direction=SOUTHWEST, x=9, y=46, z=0, run_entrance_event=True),
	Return(),
	SetBit(DIRECTIONAL_7046_0, identifier="EVENT_2435_set_bit_23"),
	ClearBit(DIRECTIONAL_7045_7),
	EnterArea(room_id=R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09, face_direction=SOUTHWEST, x=8, y=47, z=0, run_entrance_event=True),
	Return()
])
