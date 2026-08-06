#A0228_ENDING_CUTSCENE_EFFECT
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
	A_ToggleSubroutineSlots(mask=0x07),
	A_EmbeddedAnimationRoutine(bytearray([0x26, 0x00, 0x00, 0x00, 0x00, 0x00, 0x3C, 0x00, 0x1C, 0x00, 0x01, 0x00, 0x00, 0x80, 0xFE, 0x80])),
	A_EmbeddedAnimationRoutine(bytearray([0x27, 0x00, 0x00, 0x00, 0x00, 0x00, 0xFC, 0x00, 0x15, 0x00, 0x01, 0x00, 0x00, 0x80, 0xFE, 0x80])),
	A_Pause(150),
	A_SetVarToConst(PRIMARY_TEMP_700C, 65024),
	A_UnknownCommand(bytearray([0x35, 0x00, 0x06])),
	A_UnknownCommand(bytearray([0x35, 0x01, 0x06])),
	A_SetVarToConst(PRIMARY_TEMP_700C, 257),
	A_UnknownCommand(bytearray([0x35, 0x00, 0x04])),
	A_UnknownCommand(bytearray([0x35, 0x01, 0x04])),
	A_UnknownCommand(bytearray([0x25, 0x20, 0x00, 0x00, 0x00])),
	A_Pause(180),
	A_SetVarToConst(PRIMARY_TEMP_700C, 258),
	A_UnknownCommand(bytearray([0x35, 0x00, 0x04])),
	A_UnknownCommand(bytearray([0x35, 0x01, 0x04])),
	A_SetVarToConst(PRIMARY_TEMP_700C, 64768),
	A_UnknownCommand(bytearray([0x35, 0x00, 0x06])),
	A_UnknownCommand(bytearray([0x35, 0x01, 0x06])),
	A_UnknownCommand(bytearray([0x25, 0x00, 0x00, 0x00, 0x00])),
	A_Pause(120),
	A_SetWalkingSpeed(FASTEST),
	A_ShiftZUpSteps(20),
	A_ReturnQueue()
])
