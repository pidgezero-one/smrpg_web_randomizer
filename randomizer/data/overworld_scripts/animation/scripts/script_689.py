#A0689_BEAN_VALLEY_BOSS_PRIZE_DRIFTS_DOWN
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
	A_Pause(64),
	A_ClearSolidityBits(cant_walk_through=True),
	A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
	A_WalkNorthwestPixels(5),
	A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
	A_VisibilityOn(),
	A_ToggleSubroutineSlots(mask=0x07),
	A_EmbeddedAnimationRoutine(bytearray([0x26, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0xF0, 0x03, 0x00, 0x01, 0x00, 0x00, 0x00, 0x04, 0x80])),
	A_EmbeddedAnimationRoutine(bytearray([0x27, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0xF0, 0x03, 0x00, 0x01, 0x00, 0x00, 0x00, 0x04, 0x80])),
	A_EmbeddedAnimationRoutine(bytearray([0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20, 0xF0, 0x03, 0x00, 0x01, 0x00, 0x00, 0x00, 0x08, 0x80])),
	A_ShiftZDownSteps(10),
	A_SetSolidityBits(cant_walk_through=True),
	A_ReturnQueue()
])
