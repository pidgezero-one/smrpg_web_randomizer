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
	ShadowOff(),
	SetVRAMPriority(PRIORITY_3),
	SetPriority(3),
	SetObjectMemoryBits(arg_1=0x0E, bits=[0, 2]),
	FaceMario(identifier="ACTION_608_face_mario_4"),
	Pause(1),
	Set700CToPressedButton(),
	AddConstToVar(PRIMARY_TEMP_700C, 65535),
	JmpIfMem704XAt700CBitClear(["ACTION_608_face_mario_4"]),
	ShadowOn(),
	SetObjectMemoryBits(arg_1=0x0E),
	JumpToHeight(108),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=F, pixel=True),
	CompareVarToConst(PRIMARY_TEMP_700C, 3),
	JmpIfComparisonResultIsGreaterOrEqual(["ACTION_608_set_sprite_sequence_19"]),
	CompareVarToConst(PRIMARY_TEMP_700C, 7),
	JmpIfComparisonResultIsLesser(["ACTION_608_set_sprite_sequence_19"]),
	SetSpriteSequence(index=4, looping_off=True, mirror_sprite=True),
	Jmp(["ACTION_608_shift_f_direction_steps_20"]),
	SetSpriteSequence(index=4, looping_off=True, identifier="ACTION_608_set_sprite_sequence_19"),
	ShiftFDirectionSteps(2, identifier="ACTION_608_shift_f_direction_steps_20"),
	SetVRAMPriority(NORMAL),
	ObjectMemoryModifyBits(arg_1=0x09, set_flags=[5], clear_bits=[4, 6]),
	PlaySound(sound=S079_YELP_IN_DISTANCE, channel=4),
	Pause(30),
	ResetProperties(),
	Set700CToPressedButton(identifier="ACTION_608_set_700C_to_pressed_button_26"),
	SetVarToConst(SECONDARY_TEMP_7024, 5),
	DecVarFrom700C(SECONDARY_TEMP_7024),
	CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_70A9),
	FaceSouthwest7D(),
	Walk1StepFDirection(),
	JumpToHeight(56),
	Pause(25),
	JmpIfRandom2of3(['ACTION_608_set_700C_to_pressed_button_26', 'ACTION_608_set_700C_to_pressed_button_26']),
	TurnRandomDirection(),
	Walk1StepFDirection(),
	Jmp(["ACTION_608_set_700C_to_pressed_button_26"])
])
