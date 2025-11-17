# E3511_BOOSTER_HILL_2ND_PASS_BACKGROUND

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
	CopyVarToVar(from_var=BOOSTER_HILL_70B1, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 8),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3511_end_loop_41"]),
	PlaySoundBalance(sound=SO014_FLOWER, balance=40),
	SetSyncActionScript(NPC_8, A0364_BOOSTER_HILL_LEFTOVER_FLOWERS),
	EndLoop(identifier="EVENT_3511_end_loop_41"),
	Return()
])
