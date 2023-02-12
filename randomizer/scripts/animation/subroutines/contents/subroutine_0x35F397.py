# referenced by weapons FryingPan

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 81, script = [
	SetAMEM32ToXYZCoords(origin=CASTER_CURRENT_POSITION, x=0, y=0, z=0, set_x=True, set_y=True, set_z=True, identifier="queuestart_0x35f397"),
	NewSpriteAtCoords(sprite_id=SPR0035_FRYING_PAN, sequence=0, priority=3, vram_address=0x6600, palette_row=8, overwrite_vram=True, overwrite_palette=True, behind_all_sprites=True, overlap_all_sprites=True),
	PauseScriptUntilSpriteSequenceDone(),
	Pause1Frame(identifier="command_0x35f3a9"),
	SetAMEM8BitToOMEMMain(amem=0x63, omem=0x63),
	JmpIfAMEM8BitNotEqualsConst(0x63, 1, ["command_0x35f3a9"]),
	RemoveObject(),
	SetOMEMMainToAMEM8Bit(omem=0x64, amem=0x63),
	ReturnObjectQueue(),
	PlaySound(sound=S0083_FRYING_PAN_HIT_1, identifier="queuestart_0x35f3ba"),
	SetAMEM32ToXYZCoords(origin=CASTER_CURRENT_POSITION, x=0, y=0, z=0, set_x=True, set_y=True, set_z=True),
	Pause1Frame(identifier="command_0x35f3c4"),
	SetAMEM8BitToOMEMMain(amem=0x64, omem=0x64),
	JmpIfAMEM8BitNotEqualsConst(0x64, 1, ["command_0x35f3c4"]),
	NewSpriteAtCoords(sprite_id=SPR0035_FRYING_PAN, sequence=1, priority=3, vram_address=0x6600, palette_row=8, overwrite_vram=True, overwrite_palette=True, behind_all_sprites=True, overlap_all_sprites=True),
	PauseScriptUntilSpriteSequenceDone(),
	PlaySound(sound=S0038_FRYING_PAN_HIT_2),
	Pause1Frame(identifier="command_0x35f3db"),
	SetAMEM8BitToOMEMMain(amem=0x65, omem=0x65),
	JmpIfAMEM8BitNotEqualsConst(0x65, 1, ["command_0x35f3db"]),
	RemoveObject(),
	ReturnObjectQueue()
])
