# E2336_TOWER_FIRST_STAIRCASE_SPOOKUM_DIRECTION_1
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
	JmpIfObjectNotInSpecificLevel(NPC_0, R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, ["EVENT_2336_summon_to_level_9"], identifier="EVENT_2336_jmp_if_object_not_in_level_0"),
	JmpIfObjectNotInSpecificLevel(NPC_1, R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, ["EVENT_2336_summon_to_level_14"]),
	JmpIfObjectNotInSpecificLevel(NPC_2, R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, ["EVENT_2336_summon_to_level_19"]),
	JmpIfObjectNotInSpecificLevel(NPC_3, R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, ["EVENT_2336_summon_to_level_24"]),
	JmpIfObjectNotInSpecificLevel(NPC_4, R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, ["EVENT_2336_summon_to_level_29"]),
	JmpIfObjectNotInSpecificLevel(NPC_5, R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, ["EVENT_2336_summon_to_level_34"]),
	JmpIfObjectNotInSpecificLevel(NPC_5, R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, ["EVENT_2336_summon_to_level_34"]),
	Pause(16),
	Jmp(["EVENT_2336_jmp_if_object_not_in_level_0"]),
	SummonObjectToSpecificLevel(NPC_0, R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, identifier="EVENT_2336_summon_to_level_9"),
    ActionQueueSync(NPC_0, [
        A_ResetProperties(),
        A_SetObjectMemoryBits(0x0B, []),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetPriority(2),
		A_OverwriteSolidity(False, False, True, False, True, False, True, False),
        A_ObjectMemorySetBit(0x08, [4]),
		A_FixedFCoordOff(),
	]),
	ResetCoords(NPC_0),
    EnableObjectTrigger(NPC_0),
	SetSyncActionScript(NPC_0, A0696_TOWER_FIRST_STAIRCASE_SPOOKUM_DIRECTION_1),
	Pause(112),
	Jmp(["EVENT_2336_jmp_if_object_not_in_level_0"]),
	SummonObjectToSpecificLevel(NPC_1, R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, identifier="EVENT_2336_summon_to_level_14"),
    ActionQueueSync(NPC_1, [
        A_ResetProperties(),
        A_SetObjectMemoryBits(0x0B, []),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetPriority(2),
		A_OverwriteSolidity(False, False, True, False, True, False, True, False),
        A_ObjectMemorySetBit(0x08, [4]),
		A_FixedFCoordOff(),
	]),
	ResetCoords(NPC_1),
    EnableObjectTrigger(NPC_1),
	SetSyncActionScript(NPC_1, A0696_TOWER_FIRST_STAIRCASE_SPOOKUM_DIRECTION_1),
	Pause(112),
	Jmp(["EVENT_2336_jmp_if_object_not_in_level_0"]),
	SummonObjectToSpecificLevel(NPC_2, R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, identifier="EVENT_2336_summon_to_level_19"),
    ActionQueueSync(NPC_2, [
        A_ResetProperties(),
        A_SetObjectMemoryBits(0x0B, []),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetPriority(2),
		A_OverwriteSolidity(False, False, True, False, True, False, True, False),
        A_ObjectMemorySetBit(0x08, [4]),
		A_FixedFCoordOff(),
	]),
	ResetCoords(NPC_2),
    EnableObjectTrigger(NPC_2),
	SetSyncActionScript(NPC_2, A0696_TOWER_FIRST_STAIRCASE_SPOOKUM_DIRECTION_1),
	Pause(112),
	Jmp(["EVENT_2336_jmp_if_object_not_in_level_0"]),
	SummonObjectToSpecificLevel(NPC_3, R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, identifier="EVENT_2336_summon_to_level_24"),
    ActionQueueSync(NPC_3, [
        A_ResetProperties(),
        A_SetObjectMemoryBits(0x0B, []),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetPriority(2),
		A_OverwriteSolidity(False, False, True, False, True, False, True, False),
        A_ObjectMemorySetBit(0x08, [4]),
		A_FixedFCoordOff(),
	]),
	ResetCoords(NPC_3),
    EnableObjectTrigger(NPC_3),
	SetSyncActionScript(NPC_3, A0696_TOWER_FIRST_STAIRCASE_SPOOKUM_DIRECTION_1),
	Pause(112),
	Jmp(["EVENT_2336_jmp_if_object_not_in_level_0"]),
	SummonObjectToSpecificLevel(NPC_4, R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, identifier="EVENT_2336_summon_to_level_29"),
    ActionQueueSync(NPC_4, [
        A_ResetProperties(),
        A_SetObjectMemoryBits(0x0B, []),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetPriority(2),
		A_OverwriteSolidity(False, False, True, False, True, False, True, False),
        A_ObjectMemorySetBit(0x08, [4]),
		A_FixedFCoordOff(),
	]),
	ResetCoords(NPC_4),
    EnableObjectTrigger(NPC_4),
	SetSyncActionScript(NPC_4, A0696_TOWER_FIRST_STAIRCASE_SPOOKUM_DIRECTION_1),
	Pause(112),
	Jmp(["EVENT_2336_jmp_if_object_not_in_level_0"]),
	SummonObjectToSpecificLevel(NPC_5, R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS, identifier="EVENT_2336_summon_to_level_34"),
    ActionQueueSync(NPC_5, [
        A_ResetProperties(),
        A_SetObjectMemoryBits(0x0B, []),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetPriority(2),
		A_OverwriteSolidity(False, False, True, False, True, False, True, False),
        A_ObjectMemorySetBit(0x08, [4]),
		A_FixedFCoordOff(),
	]),
	ResetCoords(NPC_5),
    EnableObjectTrigger(NPC_5),
	SetSyncActionScript(NPC_5, A0696_TOWER_FIRST_STAIRCASE_SPOOKUM_DIRECTION_1),
	Pause(112),
	Jmp(["EVENT_2336_jmp_if_object_not_in_level_0"])
])
