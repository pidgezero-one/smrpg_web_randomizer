# E3947_EMPTY

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
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 470, ["EVENT_3947_jmp_to_event_21"]),
	Set7016701BToObjectXYZ(target=MARIO),
	Set70107015ToObjectXYZ(target=MARIO),
	FadeOutToBlack(sync=False),
	EnterArea(room_id=R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM, face_direction=SOUTH, x=7, y=82, z=0),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_14, subscript=[
		A_VisibilityOff()
	]),
	RemoveObjectFromCurrentLevel(MARIO),
	CircleMaskShrinkToObject(target=MARIO, width=96, speed=8, static=True),
	Pause(180),
	ActionQueueAsync(target=NPC_14, subscript=[
		A_StartLoopNTimes(3),
		A_VisibilityOn(),
		A_Pause(8),
		A_VisibilityOff(),
		A_Pause(8),
		A_EndLoop(),
		A_StartLoopNTimes(3),
		A_VisibilityOn(),
		A_Pause(4),
		A_VisibilityOff(),
		A_Pause(4),
		A_EndLoop(),
		A_StartLoopNTimes(3),
		A_VisibilityOn(),
		A_Pause(2),
		A_VisibilityOff(),
		A_Pause(2),
		A_EndLoop(),
		A_VisibilityOn(),
		A_Pause(180)
	]),
	CircleMaskShrinkToObject(target=MARIO, width=0, speed=8, static=True),
	JmpToEvent(E3948_EMPTY),
	JmpToEvent(E3400_RESTART_MUSIC_AFTER_STAR_PIECE_SEQUENCE, identifier="EVENT_3947_jmp_to_event_21")
])
