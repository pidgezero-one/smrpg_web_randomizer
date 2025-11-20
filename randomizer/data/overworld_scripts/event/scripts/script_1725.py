# E1725_EMPTY
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
	EnableControls([], identifier="EVENT_1725_enable_controls_0"),
	EnterArea(room_id=R147_GAME_INTRO_MIDAS_RIVER_WATER_TUNNEL, face_direction=SOUTHEAST, x=4, y=24, z=0),
	FadeInFromBlack(sync=True),
	FreezeCamera(),
	RunBackgroundEvent(event_id=E1724_EMPTY, return_on_level_exit=True),
	SetSyncActionScript(MARIO, A0598_MIDAS_RIVER_TOP_TUNNEL_PLAYER_OUTER),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkEastSteps(8),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=10, sprite_offset=1, is_sequence=True, looping=True)
	], identifier="EVENT_1725_action_queue_7"),
	StartLoopNTimes(2),
	Pause(1),
	EndLoop(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=13, sprite_offset=1, is_sequence=True, looping=True)
	]),
	StartLoopNTimes(2),
	Pause(1),
	EndLoop(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=12, sprite_offset=1, is_sequence=True, looping=True)
	]),
	StartLoopNTimes(2),
	Pause(1),
	EndLoop(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=14, sprite_offset=1, is_sequence=True, looping=True)
	]),
	StartLoopNTimes(2),
	Pause(1),
	EndLoop(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=11, sprite_offset=1, is_sequence=True, looping=True)
	]),
	StartLoopNTimes(2),
	Pause(1),
	EndLoop(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=14, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	StartLoopNTimes(2),
	Pause(1),
	EndLoop(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=12, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	StartLoopNTimes(2),
	Pause(1),
	EndLoop(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=13, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	StartLoopNTimes(2),
	Pause(1),
	EndLoop(),
	Jmp(["EVENT_1725_action_queue_7"])
])
