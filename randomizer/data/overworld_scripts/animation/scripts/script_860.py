#A0860_ABYSS_BEFORE_1ST_BOSS_JUMP_BACK_UP
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
	A_FaceNortheast(),
	A_SetSpriteSequence(index=4, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True),
	A_SetPriority(3),
	A_ToggleSubroutineSlots(mask=0x07),
	A_SetSubroutineXTargets(slot_26_x=0x0120, slot_27_x=0xFEC0),
	A_UnknownCommand(bytearray([0x25, 0x00, 0x0E, 0x80, 0xFF])),
	A_Pause(46),
	A_KillAllSubroutineSlots(),
	A_PlaySound(sound=SO058_INSERT, channel=4),
	A_OverwriteSolidity(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_ReturnQueue()
])
