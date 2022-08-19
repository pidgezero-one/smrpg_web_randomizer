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
	VisibilityOff(),
	SetSpriteSequence(index=2, looping_off=True, is_sequence=True),
	SetPaletteRow(4),
	Pause(24),
	CreatePacketAtNPCCoords(packet_id=P024_REGULAR_SOUND_EXPLOSION, object=DUMMY_0X07, destinations=["ACTION_319_visibility_on_5"]),
	VisibilityOn(identifier="ACTION_319_visibility_on_5"),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	SetSolidityBits(bit_4=True, cant_walk_through=True),
	StartLoopNTimes(4),
	ShadowOn(),
	Walk1StepSoutheast(),
	EndLoop(),
	PlaySound(sound=S088_WRONG_SIGNAL, channel=4),
	VisibilityOff(),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	Return()
])
