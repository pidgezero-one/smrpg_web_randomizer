# E1734_EMPTY

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
	Pause(1, identifier="EVENT_1734_pause_0"),
	JmpIfBitClear(TEMP_7076_0, ["EVENT_1734_pause_0"]),
	SetVarToConst(TEMP_70AB, 22, identifier="EVENT_1734_set_var_to_const_2"),
	StartLoopNTimes(3),
	JmpIfObjectInCurrentLevel(MEM_70AB, ["EVENT_1734_set_action_script_7"]),
	ResumeActionScript(MEM_70AB),
	Jmp(["EVENT_1734_inc_8"]),
	SetSyncActionScript(MEM_70AB, A0770_EMPTY, identifier="EVENT_1734_set_action_script_7"),
	Inc(TEMP_70AB, identifier="EVENT_1734_inc_8"),
	EndLoop(),
	Pause(4),
	Jmp(["EVENT_1734_set_var_to_const_2"])
])
