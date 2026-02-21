#A0535_MUSHROOM_WAY_2_RECRUITABLE_CHARACTER
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
	A_UnknownCommand(bytearray([0x20, 0x04]), identifier="ACTION_535_db_0"),
	A_EmbeddedAnimationRoutine(bytearray([0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x40, 0x00, 0x02, 0x00, 0x01, 0x00, 0x00, 0x00, 0x08, 0x80])),
	A_SetSequenceSpeed(FAST),
	A_SetWalkingSpeed(SLOW),
	A_WalkSoutheastSteps(2),
	A_WalkNortheastSteps(2),
	A_WalkNorthwestSteps(2),
	A_WalkSouthwestSteps(2),
	A_Jmp(["ACTION_535_db_0"])
])
