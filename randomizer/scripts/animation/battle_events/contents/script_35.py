# BE0035_SOLO_WIND_CRYSTAL_APPEARS

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(script=[
	SetAMEM32ToXYZCoords(origin=ABSOLUTE_POSITION, x=183, y=127, z=0, set_x=True, set_y=True, set_z=True),
	NewSpriteAtCoords(sprite_id=SPR0786_WIND_CRYSTAL, sequence=0, priority=2, vram_address=0x7E00, palette_row=12, param_2_and_0x10=True, overwrite_palette=True, behind_all_sprites=True, overlap_all_sprites=True),
	SummonMonster(monster=WindCrystal, position=1, bit_7=True),
	Jmp(["command_0x3a7550"])
])
