# E3509_BOOSTER_HILL_BARREL_SUMMONER_WITH_RED
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
    # one barrel
	SetVarToConst(TEMP_70AE, 3),
	StartLoopNTimes(6),
	SetSyncActionScript(NPC_1, A0709_BOOSTER_HILL_BARREL),
	Pause(210),
	EndLoop(),
	JmpIfBitSet(BOOSTER_HILL_CLEARED, ["EVENT_3509_pause_9"]),
	JmpIfBitSet(TEMP_7043_7, ["EVENT_3509_pause_9"]),
	SetBit(TEMP_7043_7),
	SetSyncActionScript(NPC_7, A0717_BOOSTER_HILL_BOSS_SHIFT_SIDE_COORD),
	Pause(30, identifier="EVENT_3509_pause_9"),
    # two barrel
	SetVarToConst(TEMP_70AE, 2),
	StartLoopNTimes(6),
	JmpIfRandom2of3(['EVENT_3509_set_action_script_16', 'EVENT_3509_set_action_script_19']),
	SetSyncActionScript(NPC_0, A0708_BOOSTER_HILL_BARREL),
	SetSyncActionScript(NPC_1, A0709_BOOSTER_HILL_BARREL),
	Jmp(["EVENT_3509_pause_21"]),
	SetSyncActionScript(NPC_1, A0709_BOOSTER_HILL_BARREL, identifier="EVENT_3509_set_action_script_16"),
	SetSyncActionScript(NPC_2, A0710_BOOSTER_HILL_BARREL),
	Jmp(["EVENT_3509_pause_21"]),
	SetSyncActionScript(NPC_2, A0710_BOOSTER_HILL_BARREL, identifier="EVENT_3509_set_action_script_19"),
	SetSyncActionScript(NPC_0, A0708_BOOSTER_HILL_BARREL),
	Pause(210, identifier="EVENT_3509_pause_21"),
	EndLoop(),
	Pause(30),
    # three barrel
	SetVarToConst(TEMP_70AE, 1),
	StartLoopNTimes(6),
	SetSyncActionScript(NPC_0, A0708_BOOSTER_HILL_BARREL),
	SetSyncActionScript(NPC_1, A0709_BOOSTER_HILL_BARREL),
	SetSyncActionScript(NPC_2, A0710_BOOSTER_HILL_BARREL),
	Pause(210),
	EndLoop(),
	Pause(30),
    # one red
	SetVarToConst(TEMP_70AE, 0),
	SetBit(TEMP_7043_3),
	SetTempAsyncActionScript(NPC_4, A0712_BOOSTER_HILL_HENCHMAN_JUMPS_OVER_BARREL),
	SetTempAsyncActionScript(NPC_5, A0712_BOOSTER_HILL_HENCHMAN_JUMPS_OVER_BARREL),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_Walk1StepNortheast()
	]),
	SetTempAsyncActionScript(NPC_3, A0712_BOOSTER_HILL_HENCHMAN_JUMPS_OVER_BARREL),
	StartLoopNTimes(4),
    SetVarToRandom(PRIMARY_TEMP_7000, 3),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["barrel_0_is_red"]),
	SetSyncActionScript(NPC_0, A0708_BOOSTER_HILL_BARREL),
    Jmp(["decide_if_barrel_1_is_red"]),
	SetSyncActionScript(NPC_0, A0763_BOOSTER_HILL_RED_BARREL, identifier="barrel_0_is_red"),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["barrel_1_is_red"], identifier="decide_if_barrel_1_is_red"),
	SetSyncActionScript(NPC_1, A0709_BOOSTER_HILL_BARREL),
    Jmp(["decide_if_barrel_2_is_red"]),
	SetSyncActionScript(NPC_1, A0764_BOOSTER_HILL_RED_BARREL, identifier="barrel_1_is_red"),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["barrel_2_is_red"], identifier="decide_if_barrel_2_is_red"),
	SetSyncActionScript(NPC_2, A0710_BOOSTER_HILL_BARREL),
    Jmp(["EVENT_3509_pause_30"]),
	SetSyncActionScript(NPC_2, A0765_BOOSTER_HILL_RED_BARREL, identifier="barrel_2_is_red"),
	Pause(140, identifier="EVENT_3509_pause_30"),
	EndLoop(),
    # two red
	StartLoopNTimes(4),
    SetVarToRandom(PRIMARY_TEMP_7000, 3),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["barrel_1_normal"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["barrel_2_normal"]),
	SetSyncActionScript(NPC_0, A0708_BOOSTER_HILL_BARREL),
	SetSyncActionScript(NPC_1, A0764_BOOSTER_HILL_RED_BARREL),
	SetSyncActionScript(NPC_2, A0765_BOOSTER_HILL_RED_BARREL),
    Jmp(["EVENT_3509_pause_31"]),
	SetSyncActionScript(NPC_0, A0763_BOOSTER_HILL_RED_BARREL, identifier="barrel_1_normal"),
	SetSyncActionScript(NPC_1, A0709_BOOSTER_HILL_BARREL),
	SetSyncActionScript(NPC_2, A0765_BOOSTER_HILL_RED_BARREL),
    Jmp(["EVENT_3509_pause_31"]),
	SetSyncActionScript(NPC_0, A0763_BOOSTER_HILL_RED_BARREL, identifier="barrel_2_normal"),
	SetSyncActionScript(NPC_1, A0764_BOOSTER_HILL_RED_BARREL),
	SetSyncActionScript(NPC_2, A0710_BOOSTER_HILL_BARREL),
	Pause(140, identifier="EVENT_3509_pause_31"),
	EndLoop(),
    # red barrels only
	StartLoopNTimes(4),
	SetSyncActionScript(NPC_0, A0763_BOOSTER_HILL_RED_BARREL),
	SetSyncActionScript(NPC_1, A0764_BOOSTER_HILL_RED_BARREL),
	SetSyncActionScript(NPC_2, A0765_BOOSTER_HILL_RED_BARREL),
	Pause(140),
	EndLoop(),
	Return()
])

