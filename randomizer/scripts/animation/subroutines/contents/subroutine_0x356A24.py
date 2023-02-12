# referenced by monster_attacks PhysicalAttack40

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 90, script = [
	SetAMEM32ToXYZCoords(origin=CASTER_CURRENT_POSITION, x=0, y=256, z=0, set_x=True, set_y=True, set_z=True, identifier="queuestart_0x356a24"),
	NewSpriteAtCoords(sprite_id=SPR0777_STAR_EGG_LITTLE_BROWN_BIRD, sequence=0, priority=3, vram_address=0x6200, palette_row=0, overwrite_vram=True, param_2_and_0x10=True, overwrite_palette=True, overlap_all_sprites=True),
	ClearAMEM8Bit(0x68),
	ClearAMEM8Bit(0x69),
	SetAMEM16BitToConst(0x60, 10),
	ObjectQueueAtOffsetAndIndex(index=0, target_address=0x356B15),
	ObjectQueueAtOffsetAndIndex(index=2, target_address=0x356B15),
	Pause1Frame(identifier="command_0x356a45"),
	JmpIfAMEM8BitNotEqualsConst(0x69, 2, ["command_0x356a45"]),
	RunSubroutine(["command_0x35336f"]),
	RemoveObject(),
	ReturnObjectQueue(),
	SetAMEM32ToXYZCoords(origin=CASTER_CURRENT_POSITION, x=0, y=256, z=0, set_x=True, set_y=True, set_z=True, identifier="queuestart_0x356a51"),
	NewSpriteAtCoords(sprite_id=SPR0777_STAR_EGG_LITTLE_BROWN_BIRD, sequence=1, priority=3, vram_address=0x6200, palette_row=0, overwrite_vram=True, param_2_and_0x10=True, overwrite_palette=True, overlap_all_sprites=True),
	ClearAMEM8Bit(0x67),
	ClearAMEM8Bit(0x69),
	SetAMEM16BitToConst(0x60, 10),
	ObjectQueueAtOffsetAndIndex(index=4, target_address=0x356B15),
	ObjectQueueAtOffsetAndIndex(index=6, target_address=0x356B15),
	Pause1Frame(identifier="command_0x356a72"),
	JmpIfAMEM8BitNotEqualsConst(0x69, 2, ["command_0x356a72"]),
	RunSubroutine(["command_0x35337d"]),
	RemoveObject(),
	ReturnObjectQueue()
])
