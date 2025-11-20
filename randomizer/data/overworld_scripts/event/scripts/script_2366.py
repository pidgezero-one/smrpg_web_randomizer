# E2366_EMPTY
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
	ActionQueueAsync(target=NPC_11, subscript=[
		A_SetSpriteSequence(index=28, sprite_offset=1, is_mold=True, is_sequence=True, looping=True),
		A_Pause(2),
		A_ResetProperties()
	]),
	CharacterJoinsParty(GENO),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=14, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_11, subscript=[
		A_ShadowOn()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_ShiftToXYCoords(x=13, y=34),
		A_SetSpriteSequence(index=2, sprite_offset=4, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkToXYCoords(x=7, y=16)
	]),
	FadeInFromBlack(sync=False),
	Pause(32),
	ActionQueueAsync(target=NPC_14, subscript=[
		A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(3),
		A_SetSpriteSequence(index=5, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(3),
		A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(3),
		A_SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(3),
		A_SetSpriteSequence(index=8, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(6),
		A_SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(6),
		A_SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(6),
		A_SetSpriteSequence(index=11, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(9),
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	SetSyncActionScript(MARIO, A0766_EMPTY),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthwestPixels(12),
		A_WalkWestPixels(6),
		A_VisibilityOn(),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_Pause(48)
	]),
	Pause(16),
	RemoveObjectFromCurrentLevel(NPC_12),
	SetSyncActionScript(NPC_11, A0767_EMPTY),
	ActionQueueSync(target=NPC_14, subscript=[
		A_SetSpriteSequence(index=13, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(20),
	SummonObjectToCurrentLevel(NPC_13),
	Pause(8),
	ActionQueueSync(target=NPC_13, subscript=[
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_Walk1StepSoutheast(),
		A_WalkSoutheastPixels(3)
	]),
	Pause(8),
	ScreenFlashesWithColour(RED),
	Pause(3),
	ScreenFlashesWithColour(YELLOW),
	Pause(3),
	ScreenFlashesWithColour(RED),
	Pause(3),
	ScreenFlashesWithColour(YELLOW),
	Pause(2),
	RemoveObjectFromCurrentLevel(NPC_13),
	ScreenFlashesWithColour(RED),
	FreezeCamera(),
	Pause(16),
	CircleMaskShrinkToObject(target=NPC_11, width=24, speed=5, static=False),
	Pause(32),
	RemoveObjectFromCurrentLevel(NPC_0),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_4),
	RemoveObjectFromCurrentLevel(NPC_5),
	RemoveObjectFromCurrentLevel(NPC_6),
	RemoveObjectFromCurrentLevel(NPC_7),
	RemoveObjectFromCurrentLevel(NPC_8),
	RemoveObjectFromCurrentLevel(NPC_10),
	RemoveObjectFromCurrentLevel(NPC_14),
	Pause(32),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceNorthwest(),
		A_SequenceLoopingOff(),
		A_ResetProperties(),
		A_SequencePlaybackOff(),
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetWalkingSpeed(SLOW),
		A_WalkSoutheastSteps(2)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkSoutheastSteps(3)
	]),
	SetSyncActionScript(NPC_11, A0854_EMPTY),
	DisplayIntroTitleText(text=GENO, y=17),
	Pause(150),
	FadeOutToBlack(sync=False, duration=30),
	JmpToEvent(E0137_EMPTY),
	Return()
])
