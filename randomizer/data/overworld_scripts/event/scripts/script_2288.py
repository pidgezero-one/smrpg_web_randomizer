# E2288_EMPTY
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
	EnterArea(room_id=R246_GAME_INTRO_KERO_SEWERS_ENTRANCE, face_direction=SOUTHEAST, x=4, y=18, z=0),
	FreezeCamera(),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkEastSteps(1)
	]),
	FadeInFromBlack(sync=False),
	Pause(15),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(height=108, silent=True),
		A_SetAllSpeeds(NORMAL),
		A_WalkSoutheastSteps(2),
		A_Pause(10),
		A_FaceSouth()
	]),
	Pause(5),
	SetVarToConst(X_COORD_2, 5),
	SetVarToConst(Y_COORD_2, 20),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ShadowOn(),
		A_FaceSouth(),
		A_FixedFCoordOn(),
		A_FloatingOff(),
		A_ClearSolidityBits(cant_pass_walls=True, cant_pass_npcs=True),
		A_SetWalkingSpeed(FAST),
		A_WalkTo70167018(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSolidityBits(cant_pass_walls=True),
		A_PlaySound(sound=SO028_PIPE_ENTRANCE, channel=6),
		A_SetSpriteSequence(index=30, sprite_offset=2, is_mold=True, is_sequence=True, looping=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ShiftZDownSteps(1),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_WalkSouthPixels(3),
		A_SetSolidityBits(cant_pass_walls=True, cant_pass_npcs=True),
		A_VisibilityOff()
	]),
	Pause(10),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestSteps(1),
		A_Pause(10),
		A_SetWalkingSpeed(NORMAL),
		A_JumpToHeight(80),
		A_WalkSouthwestSteps(1),
		A_Pause(45),
		A_FaceSoutheast(),
		A_Pause(20),
		A_FaceSouthwest(),
		A_Pause(30),
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(80),
		A_WalkNortheastSteps(2)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSouthwest(),
		A_FixedFCoordOff(),
		A_ResetProperties(),
		A_WalkNorthPixels(6),
		A_VisibilityOn(),
		A_JumpToHeight(112),
		A_SetSequenceSpeed(FAST),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthwestSteps(2),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestSteps(3),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_Pause(20),
		A_VisibilityOn(),
		A_FaceSouthwest(),
		A_SetSequenceSpeed(VERY_FAST),
		A_JumpToHeight(112),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthwestSteps(2),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestSteps(3),
		A_VisibilityOff()
	]),
	CircleMaskShrinkToObject(target=NPC_0, width=30, speed=5, static=False),
	Pause(90),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_UnknownCommand(bytearray(b' \x03')),
		A_UnknownCommand(bytearray(b'$3\x01\xec\xfe')),
		A_Pause(33),
		A_BPL262728()
	]),
	DisplayIntroTitleText(text=MALLOW, y=7),
	Pause(150),
	FadeOutToBlack(sync=False, duration=30),
	CharacterJoinsParty(MALLOW),
	JmpToEvent(E0135_EMPTY),
	Return()
])
