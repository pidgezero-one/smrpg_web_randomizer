# E2130_EMPTY

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
	RunDialog(dialog_id=DI3350_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_2130_run_dialog_0"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	EnableControlsUntilReturn([]),
	Pause(60),
	FadeOutMusicToVolume(duration=5, volume=0),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_ShiftToXYCoords(x=2, y=56),
		A_WalkSouthwestPixels(5),
		A_WalkSoutheastPixels(16),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(FAST),
		A_VisibilityOn(),
		A_WalkSoutheastSteps(9),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(30),
		A_SetSequenceSpeed(SLOW),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True),
		A_Pause(120)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True),
		A_Pause(40),
		A_SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True),
		A_Pause(40),
		A_SetSpriteSequence(index=11, is_mold=True, is_sequence=True, looping=True),
		A_Pause(40),
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True),
		A_Pause(40)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(40),
		A_Pause(40),
		A_Pause(30),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=9, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(50)
	]),
	StartBattleAtBattlefield(PACK208_DODO_BOSS_STATIC, BF22_NIMBUS_CASTLE),
	JmpIfBitClear(GAME_OVER, ["EVENT_2130_unfreeze_camera_11"]),
	ResetAndChooseGame(),
	UnfreezeCamera(identifier="EVENT_2130_unfreeze_camera_11"),
	PaletteSet(palette_set=84, row=1, bit_3=True),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_FaceNortheast()
	]),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_Pause(60),
		A_FaceNorthwest(),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNorthwestSteps(11),
		A_VisibilityOff()
	]),
	Pause(35),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	Pause(10),
	SetBit(UNKNOWN_TOWER_BOSS_2_FIGHT_7092_6),
	RemoveObjectFromSpecificLevel(NPC_1, R112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	RestoreAllHP(),
	RestoreAllFP(),
	PlayMusicAtDefaultVolume(M0061_VALENTINA),
	Return()
])
