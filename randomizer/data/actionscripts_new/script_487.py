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
	Set700CToPressedButton(identifier="ACTION_487_set_700C_to_pressed_button_0"),
	AddConstToVar(PRIMARY_TEMP_700C, 65516),
	LoadMemory(PRIMARY_TEMP_700C),
	Pause(1),
	EndLoop(),
	JumpToHeight(64, identifier="ACTION_487_jump_to_height_5"),
	Pause(1),
	JmpIfMarioInAir(["ACTION_487_jump_to_height_5"]),
	JmpIfBitClear(TEMP_7043_0, ["ACTION_487_set_700C_to_pressed_button_0"]),
	Return()
])
