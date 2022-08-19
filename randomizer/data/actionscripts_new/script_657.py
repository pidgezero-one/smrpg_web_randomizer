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
	ShadowOff(identifier="ACTION_657_shadow_off_0"),
	SetWalkingSpeed(speed=NORMAL),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True),
	ClearBit(TEMP_7043_4),
	ShiftZUpPixels(10),
	ShiftZUpPixels(6),
	ShiftZUpSteps(4),
	JmpIfRandom1of2(["ACTION_657_pause_9"]),
	Pause(60),
	Pause(30, identifier="ACTION_657_pause_9"),
	SetWalkingSpeed(speed=FASTEST),
	ShiftZDownSteps(4),
	SetBit(TEMP_7043_4),
	DecZCoord1Step(),
	PlaySound(sound=S073_THWOMP_STOMP, channel=4),
	SetBit(TEMP_7043_1),
	SetSequenceSpeed(speed=FAST),
	SetSpriteSequence(index=0, is_sequence=True),
	Pause(2),
	ClearBit(TEMP_7043_1),
	Pause(28),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True),
	Jmp(["ACTION_657_shadow_off_0"])
])
