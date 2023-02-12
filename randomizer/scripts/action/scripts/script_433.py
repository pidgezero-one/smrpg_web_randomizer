#A0433_ROSE_WAY_TRANSPORT_PLATFORM_SUBROUTINE

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetPriority(3, identifier="ACTION_433_set_priority_0"),
	ClearSolidityBits(cant_pass_walls=True),
	SetSpriteSequence(index=0, is_sequence=True, looping=True),
	IncPaletteRowBy(1),
	SetWalkingSpeed(FAST),
	Return(),
	IncPaletteRowBy(15, identifier="ACTION_433_inc_palette_row_by_6"),
	ClearBit(TEMP_7043_0),
	Pause(1, identifier="ACTION_433_pause_8"),
	Set700CToPressedButton(),
	Compare700CToVar(TEMP_7034),
	JmpIfLoadedMemoryIsNot0(["ACTION_433_pause_8"]),
	IncPaletteRowBy(1),
	SetBit(TEMP_7043_0),
	Return()
])
