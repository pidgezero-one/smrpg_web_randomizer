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
	VisibilityOff(identifier="ACTION_318_visibility_off_0"),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	Pause(1, identifier="ACTION_318_pause_3"),
	Set700CToPressedButton(),
	CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=SECONDARY_TEMP_7024),
	CopyVarToVar(from_var=TEMP_70AE, to_var=PRIMARY_TEMP_700C),
	DecVarFrom700C(SECONDARY_TEMP_7024),
	JmpIfLoadedMemoryIsNot0(["ACTION_318_pause_3"]),
	VisibilityOn(),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	Pause(60),
	StartLoopNTimes(7),
	VisibilityOff(),
	Pause(2),
	VisibilityOn(),
	Pause(2),
	EndLoop(),
	VisibilityOff(),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	Return()
])
