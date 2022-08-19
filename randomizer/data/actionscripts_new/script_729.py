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
	VisibilityOff(identifier="ACTION_729_visibility_off_0"),
	Pause(1),
	JmpIfBitClear(TEMP_7043_4, ["ACTION_729_visibility_off_0"]),
	VisibilityOn(),
	SequenceLoopingOn(),
	PlaySound(sound=S089_LIT_FUSE, channel=4),
	SequencePlaybackOn(),
	SetSpriteSequence(index=2, is_sequence=True),
	Pause(60),
	SetSpriteSequence(index=3, looping_off=True, is_sequence=True),
	Pause(20),
	VisibilityOff(),
	Db(bytearray(b'\xc7\x07')),
	StartLoopNTimes(2),
	AddConstToVar(Z_COORD_1, 32),
	JmpToSubroutine(["ACTION_729_pause_42"]),
	CreatePacketAtNPCCoords(packet_id=P024_REGULAR_SOUND_EXPLOSION, destinations=["ACTION_729_pause_38"]),
	AddConstToVar(Z_COORD_1, 32),
	AddConstToVar(X_COORD_1, 64),
	Pause(10),
	JmpToSubroutine(["ACTION_729_pause_42"]),
	CreatePacketAtNPCCoords(packet_id=P024_REGULAR_SOUND_EXPLOSION, destinations=["ACTION_729_pause_38"]),
	AddConstToVar(Z_COORD_1, 32),
	AddConstToVar(X_COORD_1, 65408),
	Pause(11),
	JmpToSubroutine(["ACTION_729_pause_42"]),
	CreatePacketAtNPCCoords(packet_id=P024_REGULAR_SOUND_EXPLOSION, destinations=["ACTION_729_pause_38"]),
	AddConstToVar(Z_COORD_1, 32),
	AddConstToVar(Y_COORD_1, 64),
	Pause(9),
	JmpToSubroutine(["ACTION_729_pause_42"]),
	CreatePacketAtNPCCoords(packet_id=P024_REGULAR_SOUND_EXPLOSION, destinations=["ACTION_729_pause_38"]),
	AddConstToVar(Z_COORD_1, 32),
	AddConstToVar(Y_COORD_1, 65472),
	AddConstToVar(X_COORD_1, 64),
	Pause(11),
	JmpToSubroutine(["ACTION_729_pause_42"]),
	CreatePacketAtNPCCoords(packet_id=P024_REGULAR_SOUND_EXPLOSION, destinations=["ACTION_729_pause_38"]),
	Pause(10, identifier="ACTION_729_pause_38"),
	EndLoop(),
	SetBit(TEMP_7043_5),
	Return(),
	Pause(1, identifier="ACTION_729_pause_42"),
	JmpIfBitSet(BAMBINO_BOMB_UNKNOWN, ["ACTION_729_pause_42"]),
	Return()
])
