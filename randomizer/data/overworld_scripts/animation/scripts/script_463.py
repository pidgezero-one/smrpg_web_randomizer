#A0463_FACTORY_SWITCH_ROOM_AMEBOID
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
	A_ShadowOn(),
	A_VisibilityOff(),
	A_Pause(64),
	A_VisibilityOn(),
	A_SetWalkingSpeed(SLOW),
	A_SequenceLoopingOn(),
	A_WalkSouthwestSteps(6),
	A_WalkSouthwestPixels(10),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True),
	A_FloatingOn(),
	A_JumpToHeight(0),
	A_ShadowOff(),
	A_Pause(24),
	A_SetWalkingSpeed(NORMAL),
	A_ToggleSubroutineSlots(mask=0x07),
	A_SetSubroutineXTargets(slot_26_x=0x0200, slot_27_x=0x0200),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_SetSubroutineXTargets(slot_26_x=0xFB80, slot_27_x=0xFE70, identifier="ACTION_463_db_18"),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_SetSubroutineXTargets(slot_26_x=0x0100, slot_27_x=0x0380),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_SetSubroutineXTargets(slot_26_x=0xFC80, slot_27_x=0xFE70),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_KillAllSubroutineSlots(),
	A_ResetProperties(),
	A_WalkToXYCoords(x=17, y=92),
	A_Pause(16),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True),
	A_ToggleSubroutineSlots(mask=0x07),
	A_SetSubroutineXTargets(slot_26_x=0x0380, slot_27_x=0x0190),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_SetSubroutineXTargets(slot_26_x=0xFF00, slot_27_x=0xFD00),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_SetSubroutineXTargets(slot_26_x=0x0480, slot_27_x=0x0190),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(32),
	A_KillAllSubroutineSlots(),
	A_ResetProperties(),
	A_WalkToXYCoords(x=23, y=91),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True),
	A_ToggleSubroutineSlots(mask=0x07),
	A_Jmp(["ACTION_463_db_18"])
])
