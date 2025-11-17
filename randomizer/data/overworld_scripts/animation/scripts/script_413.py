#A0413_EMPTY

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
	A_SequenceLoopingOn(identifier="ACTION_413_sequence_looping_on_0"),
	A_Pause(2),
	A_JmpIfBitSet(TEMP_7044_6, ["ACTION_413_sequence_looping_off_4"]),
	A_Jmp(["ACTION_413_sequence_looping_on_0"]),
	A_SequenceLoopingOff(identifier="ACTION_413_sequence_looping_off_4"),
	A_Pause(3),
	A_JmpIfBitClear(TEMP_7044_5, ["ACTION_413_sequence_looping_off_4"]),
	A_Jmp(["ACTION_413_sequence_looping_on_0"])
])
