# E1740_EMPTY
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
	EnableControls([], identifier="EVENT_1740_enable_controls_0"),
	EnterArea(room_id=R151_GAME_INTRO_BOOSTER_HILL, face_direction=NORTHWEST, x=7, y=57, z=0),
	SetVarToConst(SECONDARY_TEMP_7024, 0),
	SetVarToConst(TEMP_7026, 1),
	FreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ObjectMemorySetBit(arg_1=0x0B, bits=[3]),
		A_TransferToXYZF(x=7, y=58, z=0, direction=EAST),
		A_FixedFCoordOn(),
		A_SequenceLoopingOn(),
		A_SetSequenceSpeed(FAST)
	]),
	SetVarToConst(TEMP_70AE, 3),
	SetSyncActionScript(NPC_3, A0772_EMPTY),
	SetSyncActionScript(NPC_4, A0772_EMPTY),
	SetSyncActionScript(NPC_5, A0772_EMPTY),
	FadeInFromBlack(sync=True),
	RunBackgroundEvent(event_id=E1743_EMPTY, return_on_level_exit=True),
	RunBackgroundEvent(event_id=E1741_EMPTY, return_on_level_exit=True, bit_6=True),
	SetSyncActionScript(LAYER_1, A0704_BOOSTER_HILL_LAYER_1),
	SetSyncActionScript(LAYER_2, A0655_BOOSTER_HILL_LAYER_2),
	SetSyncActionScript(LAYER_3, A0776_EMPTY),
	SetVarToConst(TIMER_701E, 330),
	RunBackgroundEventWithPauseReturnOnExit(event_id=E1744_EMPTY, timer_var=TIMER_701E, bit_4=True, bit_5=True),
	MoveScriptToBackgroundThread2(),
	Pause(1, identifier="EVENT_1740_pause_19"),
	JmpIfBitSet(TEMP_7043_4, ["EVENT_1740_fade_out_to_black_async_duration_36"], identifier="EVENT_1740_jmp_if_bit_set_20"),
	Pause(1),
	JmpIfBitSet(TEMP_7043_4, ["EVENT_1740_fade_out_to_black_async_duration_36"]),
	JmpIfBitClear(TEMP_7043_5, ["EVENT_1740_pause_19"]),
	CompareVarToConst(SECONDARY_TEMP_7024, 0),
	JmpIfLoadedMemoryIs0(["EVENT_1740_clear_bit_34"]),
	JmpIfLoadedMemoryIsAboveOrEqual0(["EVENT_1740_action_queue_32"]),
	Dec(TEMP_7026),
	JmpIfVarNotEqualsConst(TEMP_7026, 0, ["EVENT_1740_pause_19"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkSoutheastPixels(1),
		A_Dec(SECONDARY_TEMP_7024),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	SetVarToConst(TEMP_7026, 1),
	Jmp(["EVENT_1740_jmp_if_bit_set_20"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(NORMAL),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_WalkNorthwestPixels(1),
		A_Inc(SECONDARY_TEMP_7024),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	], identifier="EVENT_1740_action_queue_32"),
	Jmp(["EVENT_1740_jmp_if_bit_set_20"]),
	ClearBit(TEMP_7043_5, identifier="EVENT_1740_clear_bit_34"),
	Jmp(["EVENT_1740_pause_19"]),
	FadeOutToBlack(sync=False, duration=30, identifier="EVENT_1740_fade_out_to_black_async_duration_36"),
	MoveScriptToMainThread(),
	FreezeAllNPCsUntilReturn(),
	StopAllBackgroundEvents(),
	UnknownCommand(bytearray(b'\xfdD')),
	StopBackgroundEvent(TIMER_701C),
	StopBackgroundEvent(TIMER_701E),
	UnfreezeCamera(),
	JmpToEvent(E1731_EMPTY)
])
