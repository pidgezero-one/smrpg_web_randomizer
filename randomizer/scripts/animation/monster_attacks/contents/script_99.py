# PhysicalAttack113

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x352523"]),
	SpriteSequence(sequence=4, looping_on=True),
	RunSubroutine(["command_0x357f5e"]),
	PlaySound(sound=S0012_BOMB_EXPLOSION),
	RemoveObject(),
	NewSpriteAtCoords(sprite_id=SPR0519_DRAIN_EXPLOSION, sequence=0, priority=3, vram_address=0x6200, palette_row=8, overwrite_vram=True, overwrite_palette=True, overlap_all_sprites=True),
	AttackTimerBegins(),
	PauseScriptUntilSpriteSequenceDone(),
	RemoveObject(),
	ReturnSubroutine()
])
