#A0953_FACTORY_2ND_ROOM_CONVEYOR_ENEMIES_BASE
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
	A_SetWalkingSpeed(SLOW, identifier="ACTION_953_set_animation_speed_0"),
	A_ShiftToXYCoords(x=3, y=70),
	A_FaceSoutheast(),
	A_WalkNorthSteps(2),
	A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	A_ToggleSubroutineSlots(mask=0x03),
	A_SetSubroutineXTargets(slot_26_x=0x0100, slot_27_x=0x0150),
	A_Pause(48),
	A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
	A_Pause(32),
	A_KillAllSubroutineSlots(),
	A_Pause(8),
    A_FaceNortheast(identifier="as_955_factory_lackey_faces_north_2"),
	A_WalkNortheastSteps(4),
	A_WalkNortheastPixels(11),
	A_ToggleSubroutineSlots(mask=0x03),
	A_SetSubroutineXTargets(slot_26_x=0x01C0, slot_27_x=0x02A0),
	A_Pause(5),
	A_FaceSoutheast(),
	A_Pause(3),
	A_KillAllSubroutineSlots(),
	A_WalkSoutheastSteps(16),
	A_ShiftToXYCoords(x=8, y=35),
	A_WalkSoutheastSteps(5),
	A_Jmp(["ACTION_953_set_animation_speed_0"])
])
