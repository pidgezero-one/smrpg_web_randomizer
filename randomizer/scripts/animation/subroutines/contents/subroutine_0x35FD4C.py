# referenced by weapons HandCannon

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 68, script = [
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=50, identifier="queuestart_0x35fd4c"),
	SetAMEM32ToXYZCoords(origin=CASTER_CURRENT_POSITION, x=20, y=240, z=0, set_x=True, set_y=True, set_z=True),
	NewSpriteAtCoords(sprite_id=SPR0527_YELLOW_MIST_STEAM_FORMS_INTO_SMALL_STAR, sequence=2, priority=3, vram_address=0x6600, palette_row=8, overwrite_vram=True, looping=True, overwrite_palette=True, behind_all_sprites=True, overlap_all_sprites=True),
	ClearAMEM16Bit(0x60),
	ClearAMEM8Bit(0x6F),
	ObjectQueueAtOffsetAndIndex(index=2, target_address=0x35F9A2),
	PlaySound(sound=S0109_GENO_HAND_CANNON_SHOOT),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=6),
	ObjectQueueAtOffsetAndIndex(index=14, target_address=0x35F9A2),
	PlaySound(sound=S0109_GENO_HAND_CANNON_SHOOT),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=6),
	ObjectQueueAtOffsetAndIndex(index=12, target_address=0x35F9A2),
	PlaySound(sound=S0109_GENO_HAND_CANNON_SHOOT),
	Pause1Frame(identifier="command_0x35fd7f"),
	JmpIfAMEM8BitNotEqualsConst(0x6F, 3, ["command_0x35fd7f"]),
	RemoveObject(),
	SetAMEM8BitToConst(0x66, 1),
	SetOMEMMainToAMEM8Bit(omem=0x66, amem=0x66),
	ReturnObjectQueue()
])
