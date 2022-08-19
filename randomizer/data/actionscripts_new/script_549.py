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
	Dec(GAME_OVER_COUNTER_MAYBE, identifier="ACTION_549_dec_0"),
	ResetProperties(),
	SetWalkingSpeed(speed=NORMAL),
	SetSequenceSpeed(speed=FAST),
	Pause(16),
	SetSolidityBits(cant_pass_walls=True, identifier="ACTION_549_set_solidity_bits_5"),
	JmpIfRandom2of3(['ACTION_549_face_mario_10', 'ACTION_549_face_mario_10']),
	TurnRandomDirection(),
	Walk1StepFDirection(),
	Jmp(["ACTION_549_set_solidity_bits_5"]),
	FaceMario(identifier="ACTION_549_face_mario_10"),
	Walk1StepFDirection(),
	Jmp(["ACTION_549_set_solidity_bits_5"])
])
