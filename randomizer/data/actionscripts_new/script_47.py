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
	SetPriority(3),
	Db(bytearray(b'\xc8#')),
	AddConstToVar(X_COORD_2, 224),
	AddConstToVar(Y_COORD_2, 112),
	AddConstToVar(Z_COORD_2, 384),
	TransferTo70167018701A(),
	PlaySound(sound=S113_OPEN_CHAMBER_DOOR, channel=4),
	VisibilityOn(),
	SetVarToConst(TEMP_7034, 65535),
	CreatePacketAtNPCCoords(packet_id=P032_BLUE_CLOUD, object=DUMMY_0X07, destinations=["ACTION_47_set_animation_speed_10"]),
	SetAllSpeeds(speed=FAST, identifier="ACTION_47_set_animation_speed_10"),
	SetBit(TEMP_7044_5),
	ShiftSoutheastSteps(2),
	SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	ShiftSoutheastSteps(15),
	SetVRAMPriority(NORMAL),
	ShiftSoutheastSteps(12),
	VisibilityOff(),
	Return()
])
