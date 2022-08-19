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
	Db(bytearray(b'\xfd\xf2')),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	PlaySound(sound=S013_COIN, channel=4),
	SetVRAMPriority(PRIORITY_3),
	SetPriority(3),
	SetSpriteSequence(index=2, looping_off=True),
	SetSequenceSpeed(speed=NORMAL),
	SetWalkingSpeed(speed=VERY_FAST),
	AddZCoord1Step(),
	Pause(26),
	VisibilityOff(),
	Return()
])
