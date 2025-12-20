# E3511_BOOSTER_HILL_2ND_PASS_BACKGROUND
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
	SetVarToConst(TEMP_70AE, 3),
	StartLoopNTimes(6),
	JmpIfRandom2of3(['EVENT_3511_set_action_script_5', 'EVENT_3511_set_action_script_7']),
	SetSyncActionScript(NPC_0, A0708_BOOSTER_HILL_BARREL),
	Jmp(["EVENT_3511_pause_8"]),
	SetSyncActionScript(NPC_1, A0709_BOOSTER_HILL_BARREL, identifier="EVENT_3511_set_action_script_5"),
	Jmp(["EVENT_3511_pause_8"]),
	SetSyncActionScript(NPC_2, A0710_BOOSTER_HILL_BARREL, identifier="EVENT_3511_set_action_script_7"),
	Pause(210, identifier="EVENT_3511_pause_8"),
	EndLoop(),
	Pause(30),
	StartLoopNTimes(6),
	JmpIfRandom2of3(['EVENT_3511_set_action_script_16', 'EVENT_3511_set_action_script_19']),
	SetSyncActionScript(NPC_0, A0708_BOOSTER_HILL_BARREL),
	SetSyncActionScript(NPC_1, A0709_BOOSTER_HILL_BARREL),
	Jmp(["EVENT_3511_pause_21"]),
	SetSyncActionScript(NPC_1, A0709_BOOSTER_HILL_BARREL, identifier="EVENT_3511_set_action_script_16"),
	SetSyncActionScript(NPC_2, A0710_BOOSTER_HILL_BARREL),
	Jmp(["EVENT_3511_pause_21"]),
	SetSyncActionScript(NPC_2, A0710_BOOSTER_HILL_BARREL, identifier="EVENT_3511_set_action_script_19"),
	SetSyncActionScript(NPC_0, A0708_BOOSTER_HILL_BARREL),
	Pause(210, identifier="EVENT_3511_pause_21"),
	EndLoop(),
	Pause(30),
	StartLoopNTimes(6),
	SetSyncActionScript(NPC_0, A0708_BOOSTER_HILL_BARREL),
	SetSyncActionScript(NPC_1, A0709_BOOSTER_HILL_BARREL),
	SetSyncActionScript(NPC_2, A0710_BOOSTER_HILL_BARREL),
	Pause(210),
	EndLoop(),
	Pause(30),
	Pause(210),
	Pause(210),
	StartLoopNTimes(1),
	Pause(210),
	Pause(210),
    JmpIfBitSet(BOOSTER_HILL_CLOSED, ["EVENT_3511_end_loop_41"]),
	
	CopyVarToVar(from_var=BOOSTER_HILL_FLOWER_COUNTER, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 16),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3511_end_loop_41"]),
	PlaySoundBalance(sound=SO014_FLOWER, balance=40),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["summon_flower_1"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["summon_flower_2"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["summon_flower_3"]),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["summon_flower_4"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["summon_flower_5"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["summon_flower_6"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["summon_flower_7"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["summon_flower_8"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["summon_flower_9"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["summon_flower_10"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 10, ["summon_flower_11"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 11, ["summon_flower_12"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 12, ["summon_flower_13"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 13, ["summon_flower_14"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 14, ["summon_flower_15"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 15, ["summon_flower_16"]),
    Jmp(["EVENT_3511_end_loop_41"]),
	SetSyncActionScript(NPC_9, A0364_BOOSTER_HILL_LEFTOVER_FLOWERS, identifier="summon_flower_1"),
    RunEventAsSubroutine(E3512_BOOSTER_HILL_FLOWER_PICKUP),
    Jmp(["increment_70B1_final"]),
	SetSyncActionScript(NPC_10, A0364_BOOSTER_HILL_LEFTOVER_FLOWERS, identifier="summon_flower_2"),
    RunEventAsSubroutine(E3512_BOOSTER_HILL_FLOWER_PICKUP),
    Jmp(["increment_70B1_final"]),
	SetSyncActionScript(NPC_11, A0364_BOOSTER_HILL_LEFTOVER_FLOWERS, identifier="summon_flower_3"),
    RunEventAsSubroutine(E3512_BOOSTER_HILL_FLOWER_PICKUP),
    Jmp(["increment_70B1_final"]),
	SetSyncActionScript(NPC_12, A0364_BOOSTER_HILL_LEFTOVER_FLOWERS, identifier="summon_flower_4"),
    RunEventAsSubroutine(E3512_BOOSTER_HILL_FLOWER_PICKUP),
    Jmp(["increment_70B1_final"]),
	SetSyncActionScript(NPC_13, A0364_BOOSTER_HILL_LEFTOVER_FLOWERS, identifier="summon_flower_5"),
    RunEventAsSubroutine(E3512_BOOSTER_HILL_FLOWER_PICKUP),
    Jmp(["increment_70B1_final"]),
	SetSyncActionScript(NPC_14, A0364_BOOSTER_HILL_LEFTOVER_FLOWERS, identifier="summon_flower_6"),
    RunEventAsSubroutine(E3512_BOOSTER_HILL_FLOWER_PICKUP),
    Jmp(["increment_70B1_final"]),
	SetSyncActionScript(NPC_15, A0364_BOOSTER_HILL_LEFTOVER_FLOWERS, identifier="summon_flower_7"),
    RunEventAsSubroutine(E3512_BOOSTER_HILL_FLOWER_PICKUP),
    Jmp(["increment_70B1_final"]),
	SetSyncActionScript(NPC_16, A0364_BOOSTER_HILL_LEFTOVER_FLOWERS, identifier="summon_flower_8"),
    RunEventAsSubroutine(E3512_BOOSTER_HILL_FLOWER_PICKUP),
    Jmp(["increment_70B1_final"]),
	SetSyncActionScript(NPC_17, A0364_BOOSTER_HILL_LEFTOVER_FLOWERS, identifier="summon_flower_9"),
    RunEventAsSubroutine(E3512_BOOSTER_HILL_FLOWER_PICKUP),
    Jmp(["increment_70B1_final"]),
	SetSyncActionScript(NPC_18, A0364_BOOSTER_HILL_LEFTOVER_FLOWERS, identifier="summon_flower_10"),
    RunEventAsSubroutine(E3512_BOOSTER_HILL_FLOWER_PICKUP),
    Jmp(["increment_70B1_final"]),
	SetSyncActionScript(NPC_19, A0364_BOOSTER_HILL_LEFTOVER_FLOWERS, identifier="summon_flower_11"),
    RunEventAsSubroutine(E3512_BOOSTER_HILL_FLOWER_PICKUP),
    Jmp(["increment_70B1_final"]),
	SetSyncActionScript(NPC_20, A0364_BOOSTER_HILL_LEFTOVER_FLOWERS, identifier="summon_flower_12"),
    RunEventAsSubroutine(E3512_BOOSTER_HILL_FLOWER_PICKUP),
    Jmp(["increment_70B1_final"]),
	SetSyncActionScript(NPC_21, A0364_BOOSTER_HILL_LEFTOVER_FLOWERS, identifier="summon_flower_13"),
    RunEventAsSubroutine(E3512_BOOSTER_HILL_FLOWER_PICKUP),
    Jmp(["increment_70B1_final"]),
	SetSyncActionScript(NPC_22, A0364_BOOSTER_HILL_LEFTOVER_FLOWERS, identifier="summon_flower_14"),
    RunEventAsSubroutine(E3512_BOOSTER_HILL_FLOWER_PICKUP),
    Jmp(["increment_70B1_final"]),
	SetSyncActionScript(NPC_23, A0364_BOOSTER_HILL_LEFTOVER_FLOWERS, identifier="summon_flower_15"),
    RunEventAsSubroutine(E3512_BOOSTER_HILL_FLOWER_PICKUP),
    Jmp(["increment_70B1_final"]),
	SetSyncActionScript(NPC_24, A0364_BOOSTER_HILL_LEFTOVER_FLOWERS, identifier="summon_flower_16"),
    RunEventAsSubroutine(E3512_BOOSTER_HILL_FLOWER_PICKUP),
    Inc(BOOSTER_HILL_FLOWER_COUNTER, identifier="increment_70B1_final"),
	EnableControlsUntilReturn([B]),
	SetBit(UNKNOWN_704E_2),
	EndLoop(identifier="EVENT_3511_end_loop_41"),
	Return()
])
