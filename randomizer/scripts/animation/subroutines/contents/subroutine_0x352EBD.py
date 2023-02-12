# referenced by monster_attacks Vigorup, monster_attacks Shaker

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 18, script = [
	NewSpriteAtCoords(sprite_id=SPR0436_EMPTY_ENEMY, sequence=0, priority=3, vram_address=0x6200, palette_row=8, overwrite_vram=True, looping=True, overwrite_palette=True, overlap_all_sprites=True, identifier="queuestart_0x352ebd"),
	ReturnSubroutine(),
	SetAMEMToRandom(amem=0x60, upper_bound=8),
	ObjectQueueAtOffsetAndIndexAtAMEM60(target_address=0x352ECF),
	ReturnSubroutine()
])
