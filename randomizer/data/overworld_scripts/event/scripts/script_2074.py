# E2074_ENTER_MONSTRO_SEALED_ROOM

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
	EnterArea(room_id=R351_CULEXS_ROOM, face_direction=NORTH, x=29, y=45, z=0),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkEastPixels(12)
	]),
	SetSyncActionScript(LAYER_1, A0575_MONSTRO_LAIR_TRANSPARENCY_LAYER),
	RunEventAsSubroutine(E0816_MONSTRO_SUPERBOSS_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False, duration=70),
	Pause(60),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkSouthSteps(1),
		A_Pause(30),
		A_WalkSouthSteps(1),
		A_Pause(30),
		A_WalkSouthSteps(1),
		A_Pause(30),
		A_WalkSouthSteps(1),
		A_Pause(30),
		A_WalkSouthSteps(1),
		A_Pause(30),
		A_WalkSouthSteps(1),
		A_Pause(30)
	]),
	RunDialog(dialog_id=DI3057_MONSTRO_SUPERBOSS_PROMPT, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_2074_action_queue_12"]),
	RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
	JmpIfBitClear(GAME_OVER, ["EVENT_2074_fade_in_from_black_async_23"]),
	ResetAndChooseGame(),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkNorthSteps(1),
		A_Pause(30),
		A_WalkNorthSteps(1),
		A_Pause(30),
		A_WalkNorthSteps(1),
		A_Pause(30),
		A_WalkNorthSteps(1),
		A_Pause(30),
		A_WalkNorthSteps(1),
		A_Pause(30),
		A_WalkNorthSteps(1),
		A_Pause(30)
	], identifier="EVENT_2074_action_queue_12"),
	JmpIfBitSet(MONSTRO_MIDDLE_DOOR_COMPLETED, ["EVENT_2074_apply_solidity_mod_17"]),
	EnterArea(room_id=R324_MONSTRO_TOWN_OUTSIDE, face_direction=SOUTHWEST, x=11, y=63, z=4),
	SetBit(GAMEBOY_KID_PURCHASE_COMPLETE),
	Jmp(["EVENT_2048_set_bit_0"]),
	ApplySolidityModToLevel(permanent=False, room_id=R324_MONSTRO_TOWN_OUTSIDE, mod_id=0, identifier="EVENT_2074_apply_solidity_mod_17"),
	ApplyTileModToLevel(use_alternate=True, room_id=R324_MONSTRO_TOWN_OUTSIDE, mod_id=33),
	JmpIfBitClear(WIN_CONDITION_MONSTRO_DOOR, ["EVENT_2074_enter_area_21"]),
	JmpToEvent(E3886_END_GAME_CONTAINER_FROM_ALT_WIN_CONDITIONS),
	EnterArea(room_id=R324_MONSTRO_TOWN_OUTSIDE, face_direction=SOUTHWEST, x=11, y=63, z=4, identifier="EVENT_2074_enter_area_21"),
	Jmp(["EVENT_2048_set_bit_0"]),
	FadeInFromBlack(sync=False, identifier="EVENT_2074_fade_in_from_black_async_23"),
	Pause(5),
	PlayMusicAtDefaultVolume(M0058_CONVERSATIONWITHCULEX),
	Pause(60),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	Pause(15),
	SetBit(MONSTRO_MIDDLE_DOOR_COMPLETED),
	RestoreAllHP(),
	RestoreAllFP(),
	Jmp(["EVENT_2074_action_queue_12"])
])
