# referenced by items FireBomb

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(expected_size = 31, script = [
	SetAMEM32ToXYZCoords(origin=ABSOLUTE_POSITION, x=0, y=0, z=0, set_x=True, set_y=True, set_z=True, identifier="queuestart_0x35dc93"),
	NewEffectObject(effect=EF0059_ORANGE_RED_BLAST__FIRE_BOMB_, looping_off=True),
	Layer3On(property=OVERLAP_ALL, bpp4=True),
	PlaySound(sound=S0012_BOMB_EXPLOSION),
	PauseScriptUntil(condition=SEQ_4BPP_COMPLETE),
	Layer3Off(property=OVERLAP_ALL, bpp4=True),
	Pause2Frames(),
	ClearEffectIndex(),
	SetAMEM8BitToConst(0x6F, 1),
	SetOMEMMainToAMEM8Bit(omem=0x6F, amem=0x6F),
	ReturnObjectQueue()
])
