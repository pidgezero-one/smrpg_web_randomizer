#A0937_EMPTY

from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.event_script_names import *
from ....variables.overworld_sfx_names import *
from ....variables.room_names import *
from ....variables.variable_names import *
from ....packets import *
from ....items import *

script = ActionScript([
	A_ShadowOn(),
	A_SequenceLoopingOn(),
	A_SetPriority(3),
	A_UnknownCommand(bytearray(b' \x07')),
	A_Set700CToPressedButton(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 26, ["ACTION_937_fixed_f_coord_on_9"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 27, ["ACTION_937_fixed_f_coord_on_16"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 28, ["ACTION_937_embedded_animation_routine_23"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 29, ["ACTION_937_embedded_animation_routine_27"]),
	A_FixedFCoordOn(identifier="ACTION_937_fixed_f_coord_on_9"),
	A_WalkNortheastPixels(6),
	A_ShiftZDownPixels(5),
	A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x00\x00`\x00\x01\xd0\xff\x80\x01\x80')),
	A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\x00\x004\x00\x01\xe6\xff \x01\x80")),
	A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x00\x00\x04\x00\x01\x00\x00\x00\x02\x80')),
	A_Jmp(["ACTION_937_pause_30"]),
	A_FixedFCoordOn(identifier="ACTION_937_fixed_f_coord_on_16"),
	A_WalkNortheastPixels(6),
	A_ShiftZDownPixels(3),
	A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x00\x00p\x00\x01\xc3\xff\x00\x02\x80')),
	A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00@\x008\x00\x01\xe2\xff\xc0\x00\x80")),
	A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x00\x00\x04\x00\x01\x00\x00\x00\x01\x80')),
	A_Jmp(["ACTION_937_pause_30"]),
	A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x00\x00P\x00\x01\xd1\xff@\x02\x80'), identifier="ACTION_937_embedded_animation_routine_23"),
	A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\x80\x000\x00\x01\xe4\xff\x00\x01\x80")),
	A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x00\x00\x04\x00\x01\x00\x00\x00\x03\x80')),
	A_Jmp(["ACTION_937_pause_30"]),
	A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x00\x00h\x00\x01\xc5\xff\x00\x01\x80'), identifier="ACTION_937_embedded_animation_routine_27"),
	A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\xc0\x00P\x00\x01\xd3\xff\x80\x01\x80")),
	A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x00\x00\x04\x00\x01\x00\x00\x00\x03\x80')),
	A_Pause(500, identifier="ACTION_937_pause_30"),
	A_StartLoopNTimes(9),
	A_VisibilityOff(),
	A_Pause(4),
	A_VisibilityOn(),
	A_Pause(4),
	A_EndLoop(),
	A_StartLoopNTimes(9),
	A_VisibilityOff(),
	A_Pause(2),
	A_VisibilityOn(),
	A_Pause(2),
	A_EndLoop(),
	A_StartLoopNTimes(9),
	A_VisibilityOff(),
	A_Pause(1),
	A_VisibilityOn(),
	A_Pause(1),
	A_EndLoop(),
	A_VisibilityOff(),
	A_ReturnQueue()
])
