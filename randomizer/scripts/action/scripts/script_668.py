#A0668_PIPE_VAULT_PIRANHA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ShadowOff(identifier="ACTION_668_shadow_off_0"),
	Pause(90),
	Pause(1, identifier="ACTION_668_pause_2"),
	JmpIfBitClear(TEMP_7044_6, ["ACTION_668_visibility_on_5"]),
	Jmp(["ACTION_668_pause_2"]),
	VisibilityOn(identifier="ACTION_668_visibility_on_5"),
	SetPriority(3),
	SetSpriteSequence(index=0, is_sequence=True, looping=True),
	AddZCoord1Step(),
	ShiftZUpPixels(12),
	SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	SetSpriteSequence(index=1, is_sequence=True, looping=True),
	Pause(48),
	SetSpriteSequence(index=0, is_sequence=True, looping=True),
	DecZCoord1Step(),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	ShiftZDownPixels(12),
	VisibilityOff(),
	JmpIfRandom1of2(["ACTION_668_pause_2"]),
	Jmp(["ACTION_668_shadow_off_0"])
])
