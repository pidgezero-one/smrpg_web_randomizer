#A0815_NIMBUS_NPC_RANDOM_DIRECTIONS
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
	A_SetSequenceSpeed(SLOW),
	A_SetWalkingSpeed(VERY_SLOW),
	A_ToggleSubroutineSlots(mask=0x04),
	A_EmbeddedAnimationRoutine(bytearray([0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x02, 0x00, 0x01, 0x00, 0x00, 0x00, 0x08, 0x80])),
	A_SetVarToConst(PRIMARY_TEMP_700C, 6, identifier="ACTION_815_set_var_to_const_4"),
	A_WalkF20Steps(),
	A_TurnClockwise45DegreesNTimes(6),
	A_Pause(4),
	A_TurnClockwise45DegreesNTimes(6),
	A_Pause(4),
	A_JmpIfRandom1of2(["ACTION_815_jmp_12"]),
	A_Pause(30),
	A_Jmp(["ACTION_815_set_var_to_const_4"], identifier="ACTION_815_jmp_12")
])
