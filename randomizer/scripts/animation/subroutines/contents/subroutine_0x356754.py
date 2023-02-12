# referenced by monster_attacks PhysicalAttack10, monster_spells WillyWisp

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 55, script = [
	SetAMEM32ToXYZCoords(origin=CASTER_CURRENT_POSITION, x=0, y=256, z=0, set_x=True, set_y=True, set_z=True, identifier="queuestart_0x356754"),
	NewSpriteAtCoords(sprite_id=SPR0792_BLACK_ROCK, sequence=3, priority=3, vram_address=0x6200, palette_row=0, overwrite_vram=True, overwrite_palette=True, overlap_all_sprites=True),
	ClearAMEM8Bit(0x68),
	ClearAMEM8Bit(0x69),
	SetAMEM16BitToConst(0x60, 5),
	ObjectQueueAtOffsetAndIndex(index=0, target_address=0x356B15),
	ObjectQueueAtOffsetAndIndex(index=2, target_address=0x356B15),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
	ObjectQueueAtOffsetAndIndex(index=0, target_address=0x356B15),
	ObjectQueueAtOffsetAndIndex(index=2, target_address=0x356B15),
	Pause1Frame(identifier="command_0x356781"),
	JmpIfAMEM8BitNotEqualsConst(0x69, 4, ["command_0x356781"]),
	Jmp(["command_0x356b01"])
])
