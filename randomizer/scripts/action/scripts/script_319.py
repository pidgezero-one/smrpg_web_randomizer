#A0319_SHIP_CANNONBALL_PUZZLE_CANNONBALL

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	VisibilityOff(),
	SetSpriteSequence(index=2, is_sequence=True, looping=False),
	SetPaletteRow(4),
	Pause(24),
	CreatePacketAtObjectCoords(packet=P024_REGULAR_SOUND_EXPLOSION, object=DUMMY_0X07, destinations=["ACTION_319_visibility_on_5"]),
	VisibilityOn(identifier="ACTION_319_visibility_on_5"),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	SetSolidityBits(bit_4=True, cant_walk_through=True),
	StartLoopNTimes(4),
	ShadowOn(),
	Walk1StepSoutheast(),
	EndLoop(),
	PlaySound(sound=SO088_WRONG_SIGNAL, channel=4),
	VisibilityOff(),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	Return()
])
