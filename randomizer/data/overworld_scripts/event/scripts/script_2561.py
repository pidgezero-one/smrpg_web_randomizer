# E2561_EMPTY

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
	JmpIfBitSet(TEMP_7044_7, ["EVENT_2304_ret_0"]),
	EnableControls([]),
	FreezeCamera(),
	UnfreezeAllNPCs(),
	PlaySound(sound=SO004_JUMP, channel=6),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_SequencePlaybackOff(),
		A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_F),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["EVENT_2561_action_queue_5_SUBSCRIPT_set_sprite_sequence_12"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["EVENT_2561_action_queue_5_SUBSCRIPT_set_sprite_sequence_14"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["EVENT_2561_action_queue_5_SUBSCRIPT_set_sprite_sequence_16"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["EVENT_2561_action_queue_5_SUBSCRIPT_set_sprite_sequence_18"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["EVENT_2561_action_queue_5_SUBSCRIPT_set_sprite_sequence_20"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["EVENT_2561_action_queue_5_SUBSCRIPT_set_sprite_sequence_22"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 6, ["EVENT_2561_action_queue_5_SUBSCRIPT_set_sprite_sequence_24"]),
		A_SetSpriteSequence(index=4, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
		A_Jmp(["EVENT_2561_action_queue_5_SUBSCRIPT_clear_solidity_bits_25"]),
		A_SetSpriteSequence(index=2, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="EVENT_2561_action_queue_5_SUBSCRIPT_set_sprite_sequence_12"),
		A_Jmp(["EVENT_2561_action_queue_5_SUBSCRIPT_clear_solidity_bits_25"]),
		A_SetSpriteSequence(index=3, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="EVENT_2561_action_queue_5_SUBSCRIPT_set_sprite_sequence_14"),
		A_Jmp(["EVENT_2561_action_queue_5_SUBSCRIPT_clear_solidity_bits_25"]),
		A_SetSpriteSequence(index=0, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, identifier="EVENT_2561_action_queue_5_SUBSCRIPT_set_sprite_sequence_16"),
		A_Jmp(["EVENT_2561_action_queue_5_SUBSCRIPT_clear_solidity_bits_25"]),
		A_SetSpriteSequence(index=3, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, identifier="EVENT_2561_action_queue_5_SUBSCRIPT_set_sprite_sequence_18"),
		A_Jmp(["EVENT_2561_action_queue_5_SUBSCRIPT_clear_solidity_bits_25"]),
		A_SetSpriteSequence(index=2, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, identifier="EVENT_2561_action_queue_5_SUBSCRIPT_set_sprite_sequence_20"),
		A_Jmp(["EVENT_2561_action_queue_5_SUBSCRIPT_clear_solidity_bits_25"]),
		A_SetSpriteSequence(index=4, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, identifier="EVENT_2561_action_queue_5_SUBSCRIPT_set_sprite_sequence_22"),
		A_Jmp(["EVENT_2561_action_queue_5_SUBSCRIPT_clear_solidity_bits_25"]),
		A_SetSpriteSequence(index=1, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, identifier="EVENT_2561_action_queue_5_SUBSCRIPT_set_sprite_sequence_24"),
		A_ClearSolidityBits(cant_pass_walls=True, identifier="EVENT_2561_action_queue_5_SUBSCRIPT_clear_solidity_bits_25"),
		A_SetPriority(3),
		A_SetWalkingSpeed(FASTEST),
		A_ShiftZUpSteps(16),
		A_RunAwayShift(),
		A_FaceSouth(),
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	FadeOutToBlack(sync=False),
	OpenSaveMenu()
])
