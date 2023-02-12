# toad_tutorial

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 79, script = [
	SetAMEM32ToXYZCoords(origin=ABSOLUTE_POSITION, x=128, y=192, z=0, set_x=True, set_y=True, set_z=True),
	SummonMonster(monster=Terrapin, position=0),
	SetAMEM16BitToConst(0x60, 64128),
	SetAMEM8BitToConst(0x62, 128),
	Set7E5xToAMEM8Bit(0x7E0000, 0x62),
	SetAMEM16BitToConst(0x62, 255),
	Set7E5xToAMEM16Bit(0x7E0070, 0x62),
	Pause1Frame(),
	ClearAMEM16Bit(0x68),
	ClearAMEM16Bit(0x6A),
	SetAMEM32ToXYZCoords(origin=CASTER_INITIAL_POSITION, x=112, y=56, z=0, set_y=True, set_z=True),
	NewSpriteAtCoords(sprite_id=SPR0064_TOAD, sequence=1, priority=2, vram_address=0x7E00, palette_row=14, overwrite_vram=True, looping=True, overwrite_palette=True, behind_all_sprites=True, overlap_all_sprites=True),
	Pause1Frame(identifier="command_0x2f4f5"),
	SetAMEM8BitToAMEM(amem=0x62, source_amem=0x60),
	JmpIfAMEMBitsSet(0x62, [6], ["command_0x2f513"]),
	Db(bytearray(b'!\x922\x00')),
	JmpIfAMEM16BitGreaterOrEqualThanConst(0x62, 128, ["command_0x2f50e"]),
	SpriteSequence(sequence=1, looping_off=True),
	Jmp(["command_0x2f4f5"])
])
