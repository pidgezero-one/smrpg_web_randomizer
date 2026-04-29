#A0459_FACTORY_SWITCH_ROOM_AMEBOID
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
	A_SetWalkingSpeed(SLOW),
	A_ShadowOn(),
	A_SequenceLoopingOn(),
	A_WalkSouthwestSteps(4),
	A_WalkSouthwestPixels(10),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True),
	A_FloatingOn(),
	A_JumpToHeight(0),
	A_ShadowOff(),
	A_Pause(24),
	A_SetWalkingSpeed(NORMAL),
	A_ResetProperties(),
	A_WalkToXYCoords(x=22, y=85),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True, mirror_sprite=True),
	A_ToggleSubroutineSlots(mask=0x07),
	A_SetSubroutineXTargets(slot_26_x=0xFF00, slot_27_x=0x00B0, identifier="ACTION_459_db_15"),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_SetSubroutineXTargets(slot_26_x=0xFE80, slot_27_x=0xFF00),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_SetSubroutineXTargets(slot_26_x=0x0180, slot_27_x=0x0100),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_SetSubroutineXTargets(slot_26_x=0x0100, slot_27_x=0xFF50),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_Jmp(["ACTION_459_db_15"])
])
