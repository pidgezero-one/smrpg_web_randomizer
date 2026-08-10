# E2493_MIMIC_3
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
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_rows import *
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
from ....spells.spells import *
from ....variables.event_palette_names import *

script = EventScript([
	PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=CHEST_COIN_SIZE),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNorthSteps(2)
	]),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(FAST),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=False),
		A_ToggleSubroutineSlots(mask=0x04),
		A_UnknownCommand(bytearray([0x25, 0xC0, 0x03, 0x80, 0xFF])),
		A_Pause(8),
		A_KillAllSubroutineSlots(),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	]),
	Set70107015ToObjectXYZ(target=MEM_70A8),
	CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_7000),
	AddConstToVar(PRIMARY_TEMP_7000, 608),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Z_COORD_1),
	ClearBit(MIMIC_3_CLEARED),
	PlaySound(sound=SO014_FLOWER, channel=6),
	CreatePacketAt7010(packet=P004_MIMIC_3_POOF_ON_DEFEAT, destinations=["EVENT_2493_pause_12"]),
	Pause(38, identifier="EVENT_2493_pause_12"),
	StopEmbeddedActionScript(MEM_70A8),
	SetVarToConst(PRIMARY_TEMP_7000, 514),
	RunEventAsSubroutine(E0353_BOSS_BATTLE),
	JmpIfBitSet(GAME_OVER, ["EVENT_2493_reset_and_choose_game_30"]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkSouthSteps(2),
		A_SetWalkingSpeed(NORMAL)
	]),
	RestoreAllHP(identifier="E2493_heal_hp"),
	RestoreAllFP(identifier="E2493_heal_fp"),
	FadeInFromBlack(sync=False),
	SetBit(MIMIC_3_CLEARED),
	SetBit(UNKNOWN_MIMIC_BIT),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_ToggleSubroutineSlots(mask=0x04),
		A_UnknownCommand(bytearray([0x25, 0x40, 0x00, 0x80, 0xFF])),
		A_Pause(8),
		A_KillAllSubroutineSlots(),
		A_JmpIfBitSet(RUN_AWAY, ["EVENT_2493_action_queue_21_SUBSCRIPT_object_memory_clear_bit_9"]),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_SequenceLoopingOff(),
		A_ReturnQueue(),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4], identifier="EVENT_2493_action_queue_21_SUBSCRIPT_object_memory_clear_bit_9"),
		A_SequenceLoopingOff(),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=False),
		A_ReturnQueue()
	]),
	JmpIfBitSet(RUN_AWAY, ["EVENT_2493_ret_29"]),
	DisableObjectTrigger(MEM_70A8),
	DisableTriggerOfObjectAt70A8InCurrentLevel(),
	StopEmbeddedActionScript(MEM_70A8),
	SetAsyncActionScript(MEM_70A8, A0015_DO_NOTHING),
	RunEventAsSubroutine(E1251_MIMIC_3_BOSS_UNLOCKS),
    SetVarToConst(PRIMARY_TEMP_7000, 514),
	JmpToEvent(E0171_MIMIC_3_GRANT_STAR_PIECE_CONTAINER),
	Return(identifier="EVENT_2493_ret_29"),
	Set7000ToCurrentLevel(identifier="EVENT_2493_reset_and_choose_game_30"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM, ["EVENT_2493_keep_reset"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R321_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2A_SLOW_ELEVATING_PLATFORMS, ["EVENT_2493_keep_reset"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN, ["EVENT_2493_keep_reset"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS, ["EVENT_2493_keep_reset"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS, ["EVENT_2493_keep_reset"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING, ["EVENT_2493_keep_reset"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS, ["EVENT_2493_keep_reset"]),
	ResetAndChooseGame(),
	Return(),
	SetVarToConst(KEEP_DOOR_LIVES, 0, identifier="EVENT_2493_keep_reset"),
	JmpToEvent(E3356_KEEP_RESPAWN_IN_LOBBY_UPON_FAILURE),
])
