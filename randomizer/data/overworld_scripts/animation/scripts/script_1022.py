#A1022_HIT_BY_EXP_STAR
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
	A_SetObjectMemoryBits(arg_1=0x0B, bits=[0, 1]),
	A_UnknownCommand(bytearray([0xFD, 0xF2])),
	A_PlaySound(sound=SO066_KICK_BALL_SHELL, channel=4),
	A_UnknownCommand(bytearray([0xFD, 0xF2])),
	A_SetVRAMPriority(PRIORITY_3),
	A_SetPriority(3),
	A_OverwriteSolidity(),
	A_ObjectMemoryClearBit(arg_1=0x08, bits=[3, 4]),
	A_FloatingOff(),
	A_FixedFCoordOn(),
	A_ToggleSubroutineSlots(mask=0x07),
	A_EmbeddedAnimationRoutine(bytearray([0x26, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x05, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00])),
	A_EmbeddedAnimationRoutine(bytearray([0x27, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x05, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00])),
	A_UnknownCommand(bytearray([0xFD, 0x24, 0x00, 0x07])),
	A_JmpIfRandom1of2(["ACTION_1022_db_17"]),
	A_JmpIfRandom1of2(["ACTION_1022_add_16"]),
	A_AddConstToVar(PRIMARY_TEMP_700C, 24),
	A_Jmp(["ACTION_1022_db_17"]),
	A_AddConstToVar(PRIMARY_TEMP_700C, 232, identifier="ACTION_1022_add_16"),
	A_UnknownCommand(bytearray([0xFD, 0x25]), identifier="ACTION_1022_db_17"),
	A_UnknownCommand(bytearray([0x25, 0xA0, 0x08, 0x80, 0xFF])),
	A_Pause(64),
	A_KillAllSubroutineSlots(),
	A_VisibilityOff(),
	A_ReturnAll()
])
