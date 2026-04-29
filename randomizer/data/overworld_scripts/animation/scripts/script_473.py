#A0473_BANDITS_WAY_5_TROOPA_INIT
# pyright: reportWildcardImportFromLibrary=false

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
	A_SetPriority(3),
	A_Set700CToPressedButton(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65517),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(3),
	A_EndLoop(),
	A_ShadowOff(),
	A_ToggleSubroutineSlots(mask=0x05),
	A_EmbeddedAnimationRoutine(bytearray([0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x10, 0x00, 0x01, 0x00, 0x00, 0x00, 0x04, 0x80])),
	A_WalkNorthwestSteps(14, identifier="ACTION_473_shift_northwest_steps_9"),
	A_Walk1StepNortheast(),
	A_WalkSoutheastSteps(14),
	A_Walk1StepSouthwest(),
	A_Jmp(["ACTION_473_shift_northwest_steps_9"])
])
