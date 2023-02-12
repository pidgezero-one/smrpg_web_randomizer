# referenced by items BadMushroom

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 31, script = [
	SetAMEM60ToCurrentTarget(identifier="queuestart_0x35dc70"),
	SetAMEM32ToXYZCoords(origin=TARGET_CURRENT_POSITION, x=0, y=-28, z=0, set_x=True, set_y=True, set_z=True),
	NewSpriteAtCoords(sprite_id=SPR0778_POISON_GAS_GREEN_GAS_CLOUD, sequence=0, priority=3, vram_address=0x6200, palette_row=0, overwrite_vram=True, overwrite_palette=True, overlap_all_sprites=True),
	PlaySound(sound=S0178_POISON_GAS_2),
	PauseScriptUntilSpriteSequenceDone(),
	RemoveObject(),
	SetAMEM8BitToConst(0x6F, 1),
	SetOMEMMainToAMEM8Bit(omem=0x6F, amem=0x6F),
	ReturnObjectQueue()
])
