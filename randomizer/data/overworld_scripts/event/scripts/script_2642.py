# E2642_EMPTY

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
	JmpIfBitSet(TOAD_SHOP_FREEBIE_RECEIVED, ["EVENT_2642_ret_67"]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI2514_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	SetBit(TOAD_SHOP_FREEBIE_RECEIVED),
	SummonObjectToSpecificLevel(NPC_9, R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD),
	SummonObjectToCurrentLevel(NPC_9),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_FloatingOff(),
		A_ShadowOn(),
		A_OverwriteSolidity(),
		A_TransferToXYZF(x=15, y=59, z=10, direction=EAST),
		A_WalkNorthPixels(16),
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_Pause(16),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkToXYCoords(x=10, y=29)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_OverwriteSolidity(cant_pass_walls=True, cant_walk_through=True),
		A_ShadowOff(),
		A_JumpToHeight(64),
		A_Pause(24),
		A_JumpToHeight(64),
		A_Pause(24),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(FAST),
		A_WalkNorthwestSteps(10)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(64),
		A_SetSequenceSpeed(VERY_FAST),
		A_SetWalkingSpeed(FAST),
		A_WalkToXYCoords(x=9, y=45),
		A_FaceSoutheast()
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_Pause(96),
		A_SetWalkingSpeed(FAST),
		A_WalkNorthwestSteps(8)
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI2515_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI2516_EMPTY, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_JumpToHeight(64),
		A_Pause(24),
		A_JumpToHeight(64),
		A_Pause(24)
	]),
	UnsyncDialog(),
	Pause(24),
	SummonObjectToCurrentLevelAtMariosCoords(NPC_10),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_Walk1StepNortheast(),
		A_WalkSoutheastPixels(6)
	]),
	Pause(48),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_JumpToHeight(108),
		A_Pause(32),
		A_WalkSoutheastSteps(2),
		A_FaceNorthwest()
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI2517_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(16),
	ActionQueueSync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=10, is_sequence=True, looping=True),
		A_Pause(6),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True)
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI2518_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_10, subscript=[
		A_ResetProperties()
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI2519_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_9, subscript=[
		A_ResetProperties(),
		A_SetSequenceSpeed(NORMAL),
		A_SetWalkingSpeed(SLOW),
		A_Pause(96),
		A_Walk1StepNorthwest()
	]),
	Pause(80),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI2520_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	StopEmbeddedActionScript(NPC_9),
	ActionQueueSync(target=NPC_9, subscript=[
		A_JumpToHeight(72)
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI2521_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=6, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI2522_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_10, subscript=[
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_JumpToHeight(64)
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI2523_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	OpenShop(SH24_FACTORY_TOAD),
	FadeInFromBlack(sync=False),
	ActionQueueSync(target=NPC_9, subscript=[
		A_JumpToHeight(64)
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3311_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3079_GOT_A_STAR_PIECE, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	AddToInventory(RockCandyItem),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(32),
		A_ResetProperties()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_Pause(32),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_Pause(48),
		A_ResetProperties()
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI2524_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Pause(24),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI2525_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	StopEmbeddedActionScript(NPC_9),
	Pause(16),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_WalkToXYCoords(x=9, y=45),
		A_VisibilityOff()
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return(identifier="EVENT_2642_ret_67")
])
