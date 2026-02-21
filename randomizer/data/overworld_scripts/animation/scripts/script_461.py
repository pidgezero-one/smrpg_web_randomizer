#A0461_FACTORY_SWITCH_ROOM_AMEBOID
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
	A_WalkSouthwestSteps(6),
	A_WalkSouthwestPixels(10),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True),
	A_FloatingOn(),
	A_JumpToHeight(0),
	A_ShadowOff(),
	A_Pause(24),
	A_SetWalkingSpeed(NORMAL),
	A_ResetProperties(),
	A_WalkToXYCoords(x=22, y=85, identifier="ACTION_461_walk_to_xy_coords_12"),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True, mirror_sprite=True),
	A_UnknownCommand(bytearray([0x20, 0x07])),
	A_UnknownCommand(bytearray([0x24, 0x00, 0xFE, 0x00, 0x02])),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_BPL262728(),
	A_ResetProperties(),
	A_WalkToXYCoords(x=20, y=95),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True),
	A_UnknownCommand(bytearray([0x20, 0x07])),
	A_UnknownCommand(bytearray([0x24, 0x00, 0x02, 0x20, 0x00])),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_UnknownCommand(bytearray([0x24, 0x00, 0x02, 0x80, 0xFE])),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_BPL262728(),
	A_ResetProperties(),
	A_WalkToXYCoords(x=22, y=89),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True),
	A_UnknownCommand(bytearray([0x20, 0x07])),
	A_UnknownCommand(bytearray([0x24, 0x00, 0xFE, 0x00, 0x00])),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_UnknownCommand(bytearray([0x24, 0x00, 0xFE, 0x00, 0x00])),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_UnknownCommand(bytearray([0x24, 0x80, 0xFF, 0x80, 0x01])),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_BPL262728(),
	A_ResetProperties(),
	A_WalkToXYCoords(x=20, y=98),
	A_SetSpriteSequence(index=9, is_sequence=True, looping=True, mirror_sprite=True),
	A_UnknownCommand(bytearray([0x20, 0x07])),
	A_UnknownCommand(bytearray([0x24, 0x00, 0x02, 0x00, 0xFF])),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_UnknownCommand(bytearray([0x24, 0x00, 0x02, 0x00, 0xFF])),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_UnknownCommand(bytearray([0x24, 0x90, 0xFF, 0x00, 0x01])),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_UnknownCommand(bytearray([0x24, 0x00, 0x00, 0x00, 0xFE])),
	A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x80, 0xFF])),
	A_Pause(30),
	A_BPL262728(),
	A_ResetProperties(),
	A_Jmp(["ACTION_461_walk_to_xy_coords_12"])
])
