# E2290_EMPTY
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
	EnterArea(room_id=R250_GAME_INTRO_BOOSTER_TOWER_BALCONY_WITH_TOADSTOOL_CRYING, face_direction=NORTHEAST, x=4, y=17, z=0),
	ActionQueueSync(target=MARIO, subscript=[
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetPriority(3),
		A_WalkNortheastPixels(10),
		A_WalkNorthPixels(2),
		A_WalkWestPixels(2),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_WalkNortheastPixels(1),
		A_WalkSoutheastPixels(2),
		A_FaceSouthwest(),
		A_SetSequenceSpeed(SLOW),
		A_SequenceLoopingOn()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=6, y=16, z=0, direction=EAST),
		A_FaceNortheast(),
		A_SetSpriteSequence(index=5, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetPriority(3)
	]),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(60),
		A_ResetProperties(),
		A_Pause(30),
		A_FaceSouthwest(),
		A_SetSequenceSpeed(NORMAL),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestSteps(3),
		A_SetWalkingSpeed(VERY_SLOW),
		A_WalkSouthwestPixels(8),
		A_Pause(60),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=13, is_sequence=True, looping=True),
		A_Pause(50)
	]),
	CircleMaskShrinkToObject(target=NPC_0, width=30, speed=5, static=False),
	Pause(30),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=22, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthSteps(3)
	]),
	DisplayIntroTitleText(text=PRINCESS_TOADSTOOL, y=17),
	Pause(150),
	FadeOutToBlack(sync=False, duration=30),
	JmpToEvent(E0141_EMPTY)
])
