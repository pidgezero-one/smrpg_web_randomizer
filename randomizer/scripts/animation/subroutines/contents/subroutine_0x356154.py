# referenced by monster_attacks PhysicalAttack47

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 38, script = [
	SetAMEM60ToCurrentTarget(identifier="queuestart_0x356154"),
	SetAMEM32ToXYZCoords(origin=TARGET_CURRENT_POSITION, x=0, y=-24, z=0, set_x=True, set_y=True, set_z=True),
	Db(bytearray(b' \xbeC\x00')),
	JmpIfAMEM8BitNotEqualsConst(0x6E, 4, ["command_0x35253b"]),
	PlaySound(sound=S0134_BOO_DISAPPEARS),
	EnableSpritesOnSubscreen(),
	NewSpriteAtCoords(sprite_id=SPR0793_BIG_PINK_HEART, sequence=0, priority=3, vram_address=0x6200, palette_row=0, overwrite_vram=True, overwrite_palette=True, overlap_all_sprites=True),
	PauseScriptUntilSpriteSequenceDone(),
	SpriteSequence(sequence=1),
	PauseScriptUntilSpriteSequenceDone(),
	RunSubroutine(["command_0x35252f"])
])
