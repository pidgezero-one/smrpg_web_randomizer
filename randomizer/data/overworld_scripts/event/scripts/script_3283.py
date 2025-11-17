# E3283_EMPTY

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
	JmpIfBitSet(UNKNOWN_7058_4, ["EVENT_3283_ret_43"]),
	SetBit(UNKNOWN_7058_4),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=10, y=111, z=14, direction=EAST),
		A_FloatingOn(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestSteps(10),
		A_SetWalkingSpeed(NORMAL),
		A_Walk1StepWest(),
		A_StartLoopNTimes(1),
		A_FaceNorthwest(),
		A_Pause(8),
		A_FaceSouthwest(),
		A_Pause(8),
		A_EndLoop()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=11, y=112, z=14, direction=EAST),
		A_FloatingOn(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestSteps(11),
		A_SetWalkingSpeed(NORMAL),
		A_StartLoopNTimes(1),
		A_FaceSoutheast(),
		A_Pause(8),
		A_FaceSouthwest(),
		A_Pause(8),
		A_EndLoop()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_TransferToXYZF(x=10, y=111, z=14, direction=EAST),
		A_FloatingOn(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_FaceSouthwest(),
		A_Pause(16),
		A_VisibilityOn(),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestSteps(9),
		A_SetWalkingSpeed(NORMAL),
		A_StartLoopNTimes(2),
		A_FaceNorthwest(),
		A_Pause(8),
		A_FaceSoutheast(),
		A_Pause(8),
		A_EndLoop(),
		A_Walk1StepNorthwest()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=11, y=112, z=14, direction=EAST),
		A_FloatingOn(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_FaceSouthwest(),
		A_Pause(16),
		A_VisibilityOn(),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestSteps(9),
		A_SetWalkingSpeed(NORMAL),
		A_StartLoopNTimes(1),
		A_FaceNorthwest(),
		A_Pause(8),
		A_FaceSouthwest(),
		A_Pause(8),
		A_FaceSoutheast(),
		A_Pause(8),
		A_EndLoop()
	]),
	RunDialog(dialog_id=DI1788_EMPTY, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(4),
		A_ClearSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_JumpToHeight(48),
		A_Pause(30),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestSteps(2),
		A_SetSpriteSequence(index=8, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(30),
	CloseDialog(),
	Pause(20),
	ActionQueueSync(target=NPC_0, subscript=[
		A_JumpToHeight(48)
	]),
	RunDialog(dialog_id=DI1789_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_1, subscript=[
		A_JumpToHeight(48)
	]),
	RunDialog(dialog_id=DI1790_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	SetVarToConst(TEMP_70AE, 20),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	ActionQueueSync(target=NPC_3, subscript=[
		A_FaceNortheast(),
		A_JumpToHeight(height=48, silent=True)
	]),
	RunDialog(dialog_id=DI1791_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_0, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_FaceNortheast()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties(),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_SetSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_JumpToHeight(108),
		A_SetAllSpeeds(FAST),
		A_Pause(30),
		A_WalkNortheastSteps(3),
		A_SetWalkingSpeed(NORMAL)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[]),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, bit_7=True),
		A_Pause(16),
		A_Walk1StepEast(),
		A_WalkNortheastSteps(3)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[]),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, bit_7=True),
		A_Pause(24),
		A_WalkNortheastSteps(3)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[]),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, bit_7=True),
		A_Walk1StepSoutheast(),
		A_WalkNortheastSteps(3)
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[]),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, bit_7=True),
		A_Pause(16),
		A_WalkNortheastSteps(3)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_FloatingOn(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_VisibilityOn(),
		A_JumpToHeight(height=48, silent=True)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_FloatingOn(),
		A_SetSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_VisibilityOn(),
		A_Pause(8),
		A_JumpToHeight(height=48, silent=True)
	]),
	RunDialog(dialog_id=DI1774_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_Pause(50),
		A_SetWalkingSpeed(VERY_FAST),
		A_PlaySoundBalance(sound=SO109_BIG_SHELL_HIT, balance=128),
		A_StartLoopNTimes(3),
		A_WalkSouthPixels(4),
		A_WalkNorthPixels(4),
		A_EndLoop(),
		A_Pause(8),
		A_PlaySoundBalance(sound=SO109_BIG_SHELL_HIT, balance=64),
		A_StartLoopNTimes(3),
		A_WalkSouthPixels(2),
		A_WalkNorthPixels(2),
		A_EndLoop(),
		A_SetWalkingSpeed(NORMAL),
		A_PlaySoundBalance(sound=SO109_BIG_SHELL_HIT, balance=32)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_ShiftXYPixels(x=8, y=4),
		A_VisibilityOn(),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(10),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSouthwestPixels(10),
		A_JumpToHeight(height=96, silent=True),
		A_FloatingOn(),
		A_Walk1StepSouthwest(),
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestSteps(2),
		A_JumpToHeight(height=48, silent=True),
		A_WalkSouthwestSteps(2),
		A_JumpToHeight(height=16, silent=True),
		A_WalkSouthwestSteps(2),
		A_JumpToHeight(height=8, silent=True),
		A_WalkSouthwestSteps(4),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=16, sprite_offset=2, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_Jmp(["EVENT_3283_action_queue_34_SUBSCRIPT_pause_0"])
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(65, identifier="EVENT_3283_action_queue_34_SUBSCRIPT_pause_0"),
		A_FixedFCoordOn(),
		A_JumpToHeight(32),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkSouthwestSteps(3),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray(b'\xfd\xf2')),
		A_ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_walk_through=True),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_Jmp(["EVENT_3283_action_queue_36_SUBSCRIPT_pause_0"])
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_Pause(55, identifier="EVENT_3283_action_queue_36_SUBSCRIPT_pause_0"),
		A_FixedFCoordOn(),
		A_JumpToHeight(32),
		A_SetAllSpeeds(FAST),
		A_WalkSouthwestSteps(3),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray(b'\xfd\xf2')),
		A_ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_walk_through=True),
		A_ReturnQueue()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_JumpToHeight(height=48, silent=True),
		A_Pause(10),
		A_JumpToHeight(height=48, silent=True),
		A_Pause(10)
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_Pause(10),
		A_JumpToHeight(height=48, silent=True),
		A_Pause(10),
		A_JumpToHeight(height=48, silent=True)
	]),
	RunDialog(dialog_id=DI1775_EMPTY, above_object=NPC_14, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SequenceLoopingOn(),
		A_SetAllSpeeds(FAST),
		A_Pause(50),
		A_Walk1StepNortheast(),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SequenceLoopingOn(),
		A_SetAllSpeeds(FAST),
		A_Pause(30),
		A_Walk1StepNortheast(),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray(b'\xfd\xf2'))
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_ResetProperties()
	]),
	Return(identifier="EVENT_3283_ret_43")
])
