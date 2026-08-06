# E1688_TEMPLE_FORTUNE_HEADS_ROOM_LOADER

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
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_rows import *
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
	ClearBit(TEMP_7043_0),
	ClearBit(TEMP_7043_1),
	ClearBit(TEMP_7043_2),
	JmpIfBitClear(BELOME_FORTUNE_1, ["EVENT_1688_copy_var_to_var_2"]),
	RemoveObjectFromCurrentLevel(NPC_3),
	CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000, identifier="EVENT_1688_copy_var_to_var_2"),
	Mem7000AndConst(0x0003),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
	CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
	Mem7000AndConst(0x000C),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7026),
	CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
	JmpIf7000AllBitsClear(bits=[4], destinations=["EVENT_1688_jmp_if_7000_all_bits_clear_12"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM, mod_id=32),
	SetBit(TEMP_7043_0),
	JmpIf7000AllBitsClear(bits=[5], destinations=["EVENT_1688_jmp_if_7000_all_bits_clear_15"], identifier="EVENT_1688_jmp_if_7000_all_bits_clear_12"),
	ApplyTileModToLevel(use_alternate=True, room_id=R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM, mod_id=33),
	SetBit(TEMP_7043_1),
	JmpIf7000AllBitsClear(bits=[6], destinations=["EVENT_1688_jmp_if_bit_clear_18"], identifier="EVENT_1688_jmp_if_7000_all_bits_clear_15"),
	ApplyTileModToLevel(use_alternate=True, room_id=R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM, mod_id=34),
	SetBit(TEMP_7043_2),
	JmpIfBitClear(UNKNOWN_BELOME_FORTUNE, ["EVENT_1688_jmp_to_event_23"], identifier="EVENT_1688_jmp_if_bit_clear_18"),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_FixedFCoordOff(),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_FixedFCoordOn(),
		A_WalkSouthPixels(4),
		A_FloatingOn(),
		A_JumpToHeight(0),
		A_Pause(1, identifier="EVENT_1688_action_queue_19_SUBSCRIPT_pause_8"),
		A_JmpIfObjectInAir(NPC_0, ["EVENT_1688_action_queue_19_SUBSCRIPT_pause_8"]),
		A_WalkNorthPixels(8)
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_FixedFCoordOff(),
		A_FaceSouthwest(),
		A_VisibilityOn(),
		A_FixedFCoordOn(),
		A_WalkSouthPixels(4),
		A_FloatingOn(),
		A_JumpToHeight(0),
		A_Pause(1, identifier="EVENT_1688_action_queue_20_SUBSCRIPT_pause_8"),
		A_JmpIfObjectInAir(NPC_1, ["EVENT_1688_action_queue_20_SUBSCRIPT_pause_8"]),
		A_WalkNorthPixels(8)
	]),
	JmpIfBitClear(UNKNOWN_BELOME_TEMPLE, ["EVENT_1688_jmp_to_event_23"]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_IncPaletteRowBy(1),
		A_VisibilityOn(),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_WalkSouthPixels(4),
		A_FloatingOn(),
		A_JumpToHeight(0),
		A_Pause(10)
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_1688_jmp_to_event_23")
])
