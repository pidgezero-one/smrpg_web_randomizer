# referenced by monster_spells Boulder

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 52, script = [
	SetAMEM32ToXYZCoords(origin=CASTER_CURRENT_POSITION, x=0, y=256, z=0, set_x=True, set_y=True, set_z=True, identifier="queuestart_0x3567f7"),
	NewSpriteAtCoords(sprite_id=SPR0531_BLACK_ROLLING_COAL_ROCK, sequence=0, priority=3, vram_address=0x6200, palette_row=0, overwrite_vram=True, looping=True, overwrite_palette=True, overlap_all_sprites=True),
	ClearAMEM8Bit(0x68),
	ClearAMEM8Bit(0x69),
	ClearAMEM8Bit(0x64),
	SetAMEM16BitToConst(0x60, 5),
	ObjectQueueAtOffsetAndIndex(index=4, target_address=0x356B15, identifier="command_0x356812"),
	Pause1Frame(),
	IncAMEM8Bit(0x64),
	JmpIfAMEM8BitNotEqualsConst(0x64, 12, ["command_0x356812"]),
	Pause1Frame(identifier="command_0x35681f"),
	JmpIfAMEM8BitNotEqualsConst(0x69, 12, ["command_0x35681f"]),
	RunSubroutine(["command_0x35336f"]),
	RemoveObject(),
	ReturnObjectQueue()
])
