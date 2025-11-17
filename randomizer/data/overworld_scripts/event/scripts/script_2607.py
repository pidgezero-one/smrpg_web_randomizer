# E2607_EMPTY

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
	JmpIfBitSet(UNUSED_7091_1, ["EVENT_2607_ret_43"]),
	SetBit(UNUSED_7091_1),
	Pause(1, identifier="EVENT_2607_pause_2"),
	JmpIfMarioInAir(["EVENT_2607_pause_2"]),
	SummonObjectToCurrentLevelAtMariosCoords(NPC_7),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(32),
		A_FaceSouthwest7D(arg=0x14)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_WalkToXYCoords(x=1, y=13)
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_OverwriteSolidity(),
		A_ResetProperties(),
		A_SetAllSpeeds(NORMAL),
		A_WalkToXYCoords(x=5, y=34),
		A_FaceSouthwest(),
		A_Pause(24),
		A_SetSpriteSequence(index=16, is_mold=True, is_sequence=True, looping=True)
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3256_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_OverwriteSolidity(cant_pass_walls=True),
		A_ResetProperties(),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_Pause(24),
		A_JumpToHeight(128),
		A_WalkSouthwestSteps(2)
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_PlaySound(sound=SO009_GREEN_SWITCH, channel=4),
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	Pause(48),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3258_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SequenceLoopingOn(),
		A_SetWalkingSpeed(SLOW),
		A_ShiftZDownSteps(5)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(64),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3259_EMPTY, above_object=NPC_14, closable=True, sync=True, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_FaceSoutheast()
	]),
	PauseScriptResumeOnNextDialogPageB(),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_SetVRAMPriority(NORMAL_PRIORITY)
	]),
	UnsyncDialog(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=9, is_sequence=True, looping=True)
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_ResetProperties()
	]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_DecZCoord1Step(),
		A_ShiftZDownPixels(8),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_Pause(13),
		A_SetSpriteSequence(index=5, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	Pause(16),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
		A_ShiftZUpSteps(4)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_ShiftZUpSteps(4)
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3257_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	StopEmbeddedActionScript(NPC_7),
	StopEmbeddedActionScript(NPC_8),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_OverwriteSolidity(),
		A_SetSequenceSpeed(FASTER),
		A_SetWalkingSpeed(FAST),
		A_WalkToXYCoords(x=4, y=36),
		A_SetSpriteSequence(index=0, sprite_offset=6, is_sequence=True, looping=True),
		A_FaceNortheast(),
		A_Pause(16),
		A_SetSpriteSequence(index=4, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_JumpToHeight(128),
		A_OverwriteSolidity(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_Pause(5),
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'$0\x02\x00\x01')),
		A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
		A_Pause(40),
		A_BPL262728()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSequenceSpeed(FAST),
		A_JumpToHeight(108),
		A_WalkSoutheastSteps(4)
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_FaceSoutheast(),
		A_ResetProperties(),
		A_Pause(21),
		A_FaceNorthwest()
	]),
	UnknownCommand(bytearray(b'\xfd\x8d')),
	RunDialog(dialog_id=DI3260_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_Walk1StepNorthwest(),
		A_VisibilityOff()
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	Return(identifier="EVENT_2607_ret_43")
])
