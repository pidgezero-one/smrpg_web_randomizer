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
	Pause(4),
	SetVarToConst(X_COORD_2, 15488),
	SetVarToConst(Y_COORD_2, 3584),
	SetVarToConst(Z_COORD_2, 864),
	TransferTo70167018701A(),
	SetPriority(3),
	ShadowOn(),
	SetVRAMPriority(PRIORITY_3),
	VisibilityOn(),
	JmpToSubroutine(["ACTION_15_ret_0"]),
	Pause(14),
	SequenceLoopingOn(),
	SetSpriteSequence(index=1, is_sequence=True),
	SetAllSpeeds(speed=FAST),
	FloatingOn(),
	Db(bytearray(b' \x04')),
	Db(bytearray(b'%`\x03\xe0\xff')),
	WalkToXYCoords(x=26, y=26),
	BPL262728(),
	SetAllSpeeds(speed=NORMAL),
	JumpToHeight(108),
	ShiftEastSteps(2),
	StartLoopNTimes(4),
	VisibilityOn(),
	Pause(2),
	VisibilityOff(),
	Pause(2),
	EndLoop(),
	ClearBit(TEMP_7043_4),
	Pause(1, identifier="ACTION_43_pause_28"),
	JmpIfBitClear(TEMP_7043_4, ["ACTION_43_pause_28"]),
	Pause(4),
	SetVarToConst(X_COORD_2, 11904),
	SetVarToConst(Y_COORD_2, 2304),
	SetVarToConst(Z_COORD_2, 864),
	TransferTo70167018701A(),
	VisibilityOn(),
	Pause(14),
	SequenceLoopingOn(),
	SetSpriteSequence(index=1, is_sequence=True),
	SetAllSpeeds(speed=FAST),
	Db(bytearray(b' \x04')),
	Db(bytearray(b'%`\x03\xe0\xff')),
	WalkToXYCoords(x=19, y=18),
	BPL262728(),
	PlaySound(sound=S065_THWOMP_STOMP, channel=4),
	JumpToHeight(108),
	JmpIfBitSet(MIDAS_BOTTOM_LEFT_TUNNEL_ITEM, ["ACTION_43_shift_west_steps_49"]),
	ShiftEastSteps(2),
	Jmp(["ACTION_298_clear_solidity_bits_0"]),
	ShiftWestSteps(2, identifier="ACTION_43_shift_west_steps_49"),
	StartLoopNTimes(4),
	VisibilityOn(),
	Pause(2),
	VisibilityOff(),
	Pause(2),
	EndLoop(),
	Return()
])
