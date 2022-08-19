#classes
from randomizer.types.actionscripts.commands import *
from randomizer.types.actionscripts.classes import ActionScript
#ids
from randomizer.types.eventscripts.constants.script_ids import *
from randomizer.types.actionscripts.constants.script_ids import *
from randomizer.types.packets.constants.packet_ids import *
from randomizer.types.constants.sound_names import *
from randomizer.types.constants.directions import *
#types
from randomizer.types.constants.area_objects import *
from randomizer.types.constants.coords import *
from randomizer.types.actionscripts.constants.sequence_speeds import *
from randomizer.types.actionscripts.constants.vram_priority import *
from randomizer.types.variables.variables import *

script = ActionScript([
	SetPriority(3, identifier="ACTION_433_set_priority_0"),
	ClearSolidityBits(cant_pass_walls=True),
	SetSpriteSequence(index=0, is_sequence=True),
	IncPaletteRowBy(1),
	SetWalkingSpeed(speed=FAST),
	Return(),
	IncPaletteRowBy(15, identifier="ACTION_433_inc_palette_row_by_6"),
	ClearBit(TEMP_7043_0),
	Pause(1, identifier="ACTION_433_pause_8"),
	Set700CToPressedButton(),
	DecVarFrom700C(TEMP_7034),
	JmpIfLoadedMemoryIsNot0(["ACTION_433_pause_8"]),
	IncPaletteRowBy(1),
	SetBit(TEMP_7043_0),
	Return()
])
