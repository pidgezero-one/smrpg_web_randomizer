#A0271_EMPTY

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
	A_ResetProperties(identifier="ACTION_271_reset_properties_0"),
	A_SetWalkingSpeed(SLOW),
	A_SetSequenceSpeed(NORMAL),
	A_Pause(15, identifier="ACTION_271_pause_3"),
	A_TurnClockwise45DegreesNTimes(4),
	A_JmpIfRandom2of3(['ACTION_271_face_mario_8', 'ACTION_271_pause_3']),
	A_Walk1StepFDirection(),
	A_Jmp(["ACTION_271_pause_3"]),
	A_FaceMario(identifier="ACTION_271_face_mario_8"),
	A_SetWalkingSpeed(NORMAL),
	A_SetSequenceSpeed(FAST),
	A_Walk1StepFDirection(),
	A_JmpIfRandom1of2(["ACTION_271_face_mario_8"]),
	A_Pause(15),
	A_JmpIfRandom1of2(["ACTION_271_face_mario_18"]),
	A_Pause(15),
	A_TurnClockwise45DegreesNTimes(4),
	A_Jmp(["ACTION_271_face_mario_8"]),
	A_FaceMario(identifier="ACTION_271_face_mario_18"),
	A_Walk1StepFDirection(),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=3, destinations=["ACTION_271_set_animation_speed_22"]),
	A_Jmp(["ACTION_271_reset_properties_0"]),
	A_SetWalkingSpeed(NORMAL, identifier="ACTION_271_set_animation_speed_22"),
	A_SetSequenceSpeed(FAST),
	A_FaceMario(),
	A_Walk1StepFDirection(),
	A_JmpIfRandom1of2(["ACTION_271_face_mario_18"]),
	A_Pause(12),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=0, tiles=2, destinations=["ACTION_271_jump_to_height_30"]),
	A_Jmp(["ACTION_271_face_mario_18"]),
	A_JumpToHeight(48, identifier="ACTION_271_jump_to_height_30"),
	A_Jmp(["ACTION_271_set_animation_speed_22"])
])
