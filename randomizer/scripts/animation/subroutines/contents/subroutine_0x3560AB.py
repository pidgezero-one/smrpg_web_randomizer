# referenced by monster_attacks FullHouse

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 34, script = [
	SetAMEM60ToCurrentTarget(identifier="queuestart_0x3560ab"),
	SetAMEM32ToXYZCoords(origin=TARGET_CURRENT_POSITION, x=0, y=-16, z=0, set_x=True, set_y=True, set_z=True),
	Db(bytearray(b' \xbeC\x00')),
	JmpIfAMEM8BitNotEqualsConst(0x6E, 4, ["command_0x35253b"]),
	PlaySound(sound=S0122_POISONED),
	NewSpriteAtCoords(sprite_id=SPR0515_GREEN_EXPLOSION, sequence=0, priority=3, vram_address=0x6200, palette_row=8, overwrite_vram=True, overwrite_palette=True, overlap_all_sprites=True),
	PauseScriptUntilSpriteSequenceDone(),
	RunSubroutine(["command_0x35252f"])
])
