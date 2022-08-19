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
	SetVarToConst(TEMP_7034, 1),
	Db(bytearray(b'\xc7\x07')),
	StartLoopNTimes(2),
	AddConstToVar(TEMP_7034, 1),
	AddConstToVar(Z_COORD_1, 8),
	CreatePacketAtNPCCoords(packet_id=P032_BLUE_CLOUD, destinations=["ACTION_976_end_loop_7"]),
	Pause(2),
	EndLoop(identifier="ACTION_976_end_loop_7"),
	SetVarToConst(TEMP_7034, 1),
	Db(bytearray(b'\xc7\x07')),
	StartLoopNTimes(2),
	AddConstToVar(TEMP_7034, 1),
	AddConstToVar(Z_COORD_1, 8),
	CreatePacketAtNPCCoords(packet_id=P032_BLUE_CLOUD, destinations=["ACTION_976_end_loop_15"]),
	Pause(2),
	EndLoop(identifier="ACTION_976_end_loop_15"),
	Return()
])
