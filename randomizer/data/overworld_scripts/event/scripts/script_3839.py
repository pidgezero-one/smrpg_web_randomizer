# E3839_EMPTY

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
	SetBit(UNKNOWN_7080_7),
	EnterArea(room_id=R219_GAME_INTRO_SEA_SHORE_WITH_SUNKEN_SHIP, face_direction=SOUTHWEST, x=12, y=29, z=6),
	FadeInFromBlack(sync=False),
	ActionQueueSync(target=MARIO, subscript=[
		A_Walk1StepSouthwest(),
		A_JumpToHeight(height=108, silent=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_Walk1StepSouthwest()
	]),
	Pause(1, identifier="EVENT_3839_pause_4"),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True),
	CompareVarToConst(PRIMARY_TEMP_7000, 1296),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3839_pause_4"]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_ShadowOn(),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetSpriteSequence(index=5, sprite_offset=3, is_sequence=True, looping=True),
		A_TransferToObjectXY(MARIO),
		A_ShiftXYPixels(x=0, y=8),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[2, 3]),
		A_VisibilityOn(),
		A_Pause(12),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_ShadowOn(),
		A_FloatingOff(),
		A_SetSpriteSequence(index=13, sprite_offset=1, is_sequence=True, looping=True),
		A_Pause(20),
		A_SetSpriteSequence(index=10, sprite_offset=1, is_sequence=True, looping=True),
		A_Walk1StepSouth(),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetSpriteSequence(index=10, sprite_offset=1, is_sequence=True, looping=True),
		A_Walk1StepSouth(),
		A_SetSpriteSequence(index=13, sprite_offset=1, is_sequence=True, looping=True),
		A_ShiftZDownPixels(2),
		A_SetSpriteSequence(index=12, sprite_offset=1, is_sequence=True, looping=True),
		A_ShiftZDownPixels(2),
		A_SetSpriteSequence(index=14, sprite_offset=1, is_sequence=True, looping=True),
		A_ShiftZDownPixels(2),
		A_SetSpriteSequence(index=11, sprite_offset=1, is_sequence=True, looping=True),
		A_ShiftZDownPixels(2),
		A_ResetProperties(),
		A_IncPaletteRowBy(4),
		A_ObjectMemoryModifyBits(arg_1=0x0C, set_bits=[4], clear_bits=[3, 5]),
		A_FaceNorth(),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_StartLoopNTimes(35),
		A_TurnClockwise45DegreesNTimes(1),
		A_ShiftZDownPixels(2),
		A_EndLoop(),
		A_FloatingOn(),
		A_SetAllSpeeds(SLOW),
		A_Walk1StepSouthwest(),
		A_JumpToHeight(height=34, silent=True),
		A_WalkSouthwestSteps(2),
		A_SetBit(TEMP_7044_7),
		A_WalkSouthwestSteps(2),
		A_SetAllSpeeds(NORMAL)
	]),
	Pause(1, identifier="EVENT_3839_pause_10"),
	JmpIfBitClear(TEMP_7044_7, ["EVENT_3839_pause_10"]),
	FadeOutToBlack(sync=False, duration=30),
	ClearBit(UNKNOWN_7080_7),
	JmpToEvent(E0145_EMPTY)
])
