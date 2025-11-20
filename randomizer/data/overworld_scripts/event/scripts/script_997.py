# E0997_EMPTY
# pyright: reportWildcardImportFromLibrary=false

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
	EnterArea(room_id=R429_GAME_INTRO_NIMBUS_LAND_OUTSIDE_WITH_PATROLLING_BIRDIES, face_direction=NORTHEAST, x=12, y=56, z=0),
	FreezeCamera(),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkSouthwestSteps(2),
		A_WalkNorthSteps(1)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(5),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(140),
		A_WalkNortheastSteps(3),
		A_WalkNortheastPixels(12),
		A_Pause(90),
		A_SetSequenceSpeed(FAST),
		A_JumpToHeight(height=108, silent=True),
		A_Pause(40),
		A_WalkNorthSteps(2),
		A_WalkNortheastSteps(12),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkNortheastSteps(20)
	]),
	FadeInFromBlack(sync=True, duration=20),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkSoutheastSteps(2),
		A_WalkSouthwestSteps(5)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Pause(60),
		A_WalkSoutheastSteps(9)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_Pause(60),
		A_SetWalkingSpeed(SLOW),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(150),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSouthwest(),
		A_FaceSoutheast(),
		A_FixedFCoordOn(),
		A_Walk1StepNorthwest(),
		A_FixedFCoordOff(),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Pause(150),
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepSouthwest(),
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_Walk1StepSoutheast(),
		A_FixedFCoordOff(),
		A_FaceSouthwest()
	]),
	Pause(270),
	FadeOutToBlack(sync=True, duration=30),
	PauseScriptUntilEffectDone(),
	JmpToEvent(E0146_EMPTY)
])
