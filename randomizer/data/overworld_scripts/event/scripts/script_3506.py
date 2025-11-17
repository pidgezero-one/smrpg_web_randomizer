# E3506_BOOSTER_HILL_GET_FLOWER

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
	JmpIfBitClear(TEMP_7044_1, ["EVENT_3506_disable_trigger_2"]),
	Return(),
	DisableObjectTrigger(NPC_8, identifier="EVENT_3506_disable_trigger_2"),
	StopBackgroundEvent(TIMER_701C),
	EnableControlsUntilReturn([]),
	SetSyncActionScript(NPC_9, A0716_BOOSTER_HILL_BUMP_FLOWER),
	SetVarToConst(PRIMARY_TEMP_7000, 1),
	Add7000ToMaxFP(),
	Inc(BOOSTER_HILL_70B1),
	Pause(8),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNorthPixels(4),
		A_SetSpriteSequence(index=4, sprite_offset=2, is_sequence=True, looping=True),
		A_WalkNorthPixels(4),
		A_WalkWestPixels(8),
		A_SetSpriteSequence(index=4, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkWestPixels(8)
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_FixedFCoordOff(),
		A_Pause(4),
		A_FaceSouthwest(),
		A_Pause(4),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_WalkEastPixels(8),
		A_SetSpriteSequence(index=4, sprite_offset=2, is_sequence=True, looping=True),
		A_WalkEastPixels(8),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSouthPixels(8)
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_Pause(4),
		A_FaceSouthwest(),
		A_Pause(4),
		A_FaceNorthwest(),
		A_FixedFCoordOn()
	]),
	JmpIfBitSet(TEMP_7043_7, ["EVENT_3506_action_queue_16"]),
	SetSyncActionScript(NPC_7, A0717_BOOSTER_HILL_BOSS_SHIFT_SIDE_COORD),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
		A_FloatingOff(),
		A_SetAllSpeeds(FAST),
		A_JumpToHeight(height=112, silent=True),
		A_SetSpriteSequence(index=7, sprite_offset=3, is_sequence=True, looping=True),
		A_FloatingOn(),
		A_StartLoopNTimes(15),
		A_VisibilityOff(),
		A_Pause(1),
		A_VisibilityOn(),
		A_WalkSoutheastPixels(1),
		A_Dec(SECONDARY_TEMP_7024),
		A_EndLoop(),
		A_ResetProperties(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	], identifier="EVENT_3506_action_queue_16"),
	JmpIfBitClear(TEMP_7043_7, ["EVENT_3506_set_bit_19"]),
	SetTempSyncActionScript(NPC_7, A0718_BOOSTER_HILL_BOSS_MOVE_FORWARD),
	SetBit(TEMP_7043_7, identifier="EVENT_3506_set_bit_19"),
	EnableControlsUntilReturn([B]),
	ResumeBackgroundEvent(TIMER_701C),
	EnableObjectTrigger(NPC_8),
	Return()
])
