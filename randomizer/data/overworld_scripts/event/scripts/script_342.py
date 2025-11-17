# E0342_EMPTY

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.colours import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.controller_inputs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.intro_title_text import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.layers import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_types import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.scenes import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.tutorials import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.battlefield_names import *
from ....variables.dialog_names import *
from ....variables.event_script_names import *
from ....variables.music_names import *
from ....variables.overworld_area_names import *
from ....variables.overworld_sfx_names import *
from ....variables.pack_names import *
from ....variables.room_names import *
from ....variables.shop_names import *
from ....variables.variable_names import *
from ....items import *
from ....packets import *

script = EventScript([
	Pause(1, identifier="EVENT_342_pause_0"),
	JmpIfBitSet(TEMP_7044_5, ["EVENT_342_set_var_to_const_3"]),
	Jmp(["EVENT_342_pause_0"]),
	SetVarToConst(X_COORD_1, 29, identifier="EVENT_342_set_var_to_const_3"),
	SetVarToConst(Y_COORD_1, 92),
	UnknownCommand(bytearray(b'\xfd\xc9')),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 352, ["EVENT_342_ret_10"]),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	ApplyTileModToLevel(use_alternate=True, room_id=R320_MUSHROOM_KINGDOM_CASTLE_ENTRANCE_TO_THRONE_ROOM, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R320_MUSHROOM_KINGDOM_CASTLE_ENTRANCE_TO_THRONE_ROOM, mod_id=0),
	Return(identifier="EVENT_342_ret_10")
])
