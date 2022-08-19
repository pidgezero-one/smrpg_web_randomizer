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
	SetSequenceSpeed(speed=NORMAL, identifier="ACTION_878_set_animation_speed_0"),
	SequenceLoopingOn(),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=F, pixel=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=SECONDARY_TEMP_7024),
	FaceSouthwest7D(),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=F, pixel=True),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 5, ["ACTION_878_face_east_7C_8"]),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_700C),
	FaceEast7C(identifier="ACTION_878_face_east_7C_8"),
	Pause(1),
	Jmp(["ACTION_878_set_animation_speed_0"])
])
