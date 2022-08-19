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
	SetBit(TEMP_7043_5, identifier="ACTION_125_set_bit_0"),
	SetVarToRandom(PRIMARY_TEMP_700C, 2),
	Inc(PRIMARY_TEMP_700C),
	LoadMemory(PRIMARY_TEMP_700C),
	JmpToSubroutine(["ACTION_103_clear_solidity_bits_0"]),
	EndLoop(),
	JmpToSubroutine(["ACTION_104_set_animation_speed_0"]),
	JmpToSubroutine(["ACTION_106_set_animation_speed_0"]),
	FaceSouthwest(),
	Jmp(["ACTION_125_set_bit_0"])
])
