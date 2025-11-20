# E2081_MUSTY_FEARS_LAMP
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
	SetVarToConst(TIMER_7022, 8),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_Pause(2),
		A_SetSpriteSequence(index=12, is_mold=True, is_sequence=True, looping=True),
		A_Pause(4),
		A_SetSpriteSequence(index=13, is_mold=True, is_sequence=True, looping=True)
	]),
	SetVarToConst(ITEM_ID, BigBooFlagItem),
	StoreItemAt70A7QuantityTo7000(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2081_run_background_event_with_pause_16"]),
	SetVarToConst(ITEM_ID, DryBonesFlagItem),
	StoreItemAt70A7QuantityTo7000(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2081_run_background_event_with_pause_16"]),
	SetVarToConst(ITEM_ID, GreaperFlagItem),
	StoreItemAt70A7QuantityTo7000(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2081_run_background_event_with_pause_16"]),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	RemoveOneOfItemFromInventory(BigBooFlagItem),
	RemoveOneOfItemFromInventory(DryBonesFlagItem),
	RemoveOneOfItemFromInventory(GreaperFlagItem),
	Jmp(["EVENT_2081_action_queue_21"]),
	RunBackgroundEventWithPause(event_id=E3075_HEAL_FLASH, timer_var=TIMER_7022, bit_4=True, bit_5=True, identifier="EVENT_2081_run_background_event_with_pause_16"),
	PlaySound(sound=SO071_MUSHROOM_CURE, channel=6),
	RestoreAllHP(),
	RestoreAllFP(),
	Pause(60),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_ResetProperties()
	], identifier="EVENT_2081_action_queue_21"),
	Return()
])
