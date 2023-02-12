# E2433_FOREST_MAZE_TRANSITION

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(DIRECTIONAL_7045_0, ["EVENT_2433_clear_bit_11"]),
	JmpIfBitSet(DIRECTIONAL_7045_1, ["EVENT_2433_clear_bit_11"]),
	JmpIfBitSet(DIRECTIONAL_7045_2, ["EVENT_2433_clear_bit_11"]),
	JmpIfBitSet(DIRECTIONAL_7045_3, ["EVENT_2433_clear_bit_11"]),
	JmpIfBitSet(DIRECTIONAL_7045_4, ["EVENT_2433_clear_bit_23"]),
	JmpIfBitSet(DIRECTIONAL_7045_6, ["EVENT_2433_clear_bit_11"]),
	JmpIfBitSet(DIRECTIONAL_7045_7, ["EVENT_2433_clear_bit_11"]),
	JmpIfBitSet(DIRECTIONAL_7046_0, ["EVENT_2433_clear_bit_26"]),
	JmpIfBitSet(DIRECTIONAL_7046_1, ["EVENT_2433_set_bit_9"]),
	SetBit(DIRECTIONAL_7045_6, identifier="EVENT_2433_set_bit_9"),
	Jmp(["EVENT_2433_clear_bit_12"]),
	ClearBit(DIRECTIONAL_7045_6, identifier="EVENT_2433_clear_bit_11"),
	ClearBit(DIRECTIONAL_7045_0, identifier="EVENT_2433_clear_bit_12"),
	ClearBit(DIRECTIONAL_7045_1),
	ClearBit(DIRECTIONAL_7045_2),
	ClearBit(DIRECTIONAL_7045_3),
	ClearBit(DIRECTIONAL_7045_4),
	SetBit(DIRECTIONAL_7045_5),
	ClearBit(DIRECTIONAL_7045_7),
	ClearBit(DIRECTIONAL_7046_0),
	ClearBit(DIRECTIONAL_7046_1),
	EnterArea(room_id=R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09, face_direction=NORTHWEST, x=8, y=61, z=0, run_entrance_event=True),
	Return(),
	ClearBit(DIRECTIONAL_7045_4, identifier="EVENT_2433_clear_bit_23"),
	EnterArea(room_id=R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD, face_direction=NORTHWEST, x=16, y=40, z=0, run_entrance_event=True),
	Return(),
	ClearBit(DIRECTIONAL_7046_0, identifier="EVENT_2433_clear_bit_26"),
	EnterArea(room_id=R231_FOREST_MAZE_SECRET_ENTRANCE, face_direction=NORTHWEST, x=21, y=76, z=0, run_entrance_event=True),
	Return()
])
