#A0725_MINES_LONG_TRACK_ROOM_MINECART

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSpriteSequence(index=7, is_sequence=True, looping=True),
	VisibilityOff(),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	JmpIfObjectInSpecificLevel(NPC_0, R286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM, ["ACTION_725_ret_27"]),
	JmpIfObjectNotInSpecificLevel(NPC_0, R287_MOLEVILLE_MINES_AREA_14_2LEVEL_ROOM_FROM_LONG_MINECART_TRACKS_ROOM, ["ACTION_725_ret_27"]),
	SetVarToConst(SECONDARY_TEMP_7024, 900),
	JmpIfBitSet(TEMP_7044_7, ["ACTION_725_set_bit_11"], identifier="ACTION_725_jmp_if_bit_set_7"),
	Pause(1),
	Dec(SECONDARY_TEMP_7024),
	JmpIfLoadedMemoryIsNot0(["ACTION_725_jmp_if_bit_set_7"]),
	SetBit(TEMP_7044_7, identifier="ACTION_725_set_bit_11"),
	RemoveFromLevel(NPC_0, R287_MOLEVILLE_MINES_AREA_14_2LEVEL_ROOM_FROM_LONG_MINECART_TRACKS_ROOM),
	RemoveFromLevel(NPC_4, R287_MOLEVILLE_MINES_AREA_14_2LEVEL_ROOM_FROM_LONG_MINECART_TRACKS_ROOM),
	SetWalkingSpeed(FAST),
	VisibilityOn(),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	SetSolidityBits(bit_4=True, cant_walk_through=True),
	PlaySound(sound=SO048_MINECART_START, channel=4),
	WalkToXYCoords(x=2, y=124),
	FadeOutSoundToVolume(duration=1, volume=0),
	VisibilityOff(),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	Db(bytearray(b'\xfd\xf2')),
	SummonToLevel(NPC_0, R286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM),
	Return(),
	Return(identifier="ACTION_725_ret_27")
])
