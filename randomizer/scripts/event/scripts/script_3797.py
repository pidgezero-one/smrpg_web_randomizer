# E3797_ENDING_CREDITS_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	FadeOutMusicToVolume(duration=0, volume=1),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	SetBit(TEMP_704A_2),
	RunEventAsSubroutine(E1011_POST_MINES_BOSS_CHECK_IF_WON),
	SetBit(FACTORY_BOSS_DEFEATED),
	SetBit(GAMEBOY_KID_PURCHASE_COMPLETE),
	JmpIfBitSet(WIN_CONDITION_STAR_PIECES, ["EVENT_3797_leave_to_moleville"]),
	JmpIfBitSet(WIN_CONDITION_MONSTRO_DOOR, ["EVENT_3797_leave_to_moleville"]),
	JmpToEvent(E3885_END_GAME),
	JmpIfBitSet(BUCKET_WARP_DIRECTIONAL_BIT, ["EVENT_3797_enter_moleville"], identifier="EVENT_3797_leave_to_moleville"),
	JmpIfBitSet(CASINO_WARP_DIRECTIONAL_BIT, ["EVENT_3797_enter_casino"]),
	ClearBit(BUCKET_WARP_DIRECTIONAL_BIT),
	ClearBit(CASINO_WARP_DIRECTIONAL_BIT),
	EnterArea(room_id=R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM, face_direction=SOUTHEAST, x=7, y=82, z=0, run_entrance_event=True),
	Return(),
	EnterArea(room_id=R108_MOLEVILLE_OUTSIDE, face_direction=SOUTH, x=3, y=62, z=1, run_entrance_event=True, identifier="EVENT_3797_enter_moleville"),
	Return(),
	ClearBit(BUCKET_WARP_DIRECTIONAL_BIT, identifier="EVENT_3797_enter_casino"),
	ClearBit(CASINO_WARP_DIRECTIONAL_BIT),
	EnterArea(room_id=R092_GRATE_GUYS_CASINO_INSIDE_CASINO, face_direction=SOUTH, x=3, y=13, z=10, run_entrance_event=True),
	Return()
])
