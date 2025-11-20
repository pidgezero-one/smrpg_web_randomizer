# E3080_COIN_CHEST_QUICK_HIT
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
	CopyVarToVar(from_var=ITEM_ID, to_var=PRIMARY_TEMP_7000),
	Mem7000AndConst(0x00F0),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 240, ["EVENT_3080_set_var_to_const_6"]),
	CopyVarToVar(from_var=ITEM_ID, to_var=PRIMARY_TEMP_7000),
	Mem7000AndConst(0x000F),
	Jmp(["EVENT_3080_add_coins_21"]),
	SetVarToConst(PRIMARY_TEMP_7000, 0, identifier="EVENT_3080_set_var_to_const_6"),
	JmpIfVarEqualsConst(COIN_CHEST_MULTIPLIER, 0, ["EVENT_3080_copy_var_to_var_11"], identifier="EVENT_3080_jmp_if_var_equals_const_7"),
	AddConstToVar(PRIMARY_TEMP_7000, 15),
	Dec(COIN_CHEST_MULTIPLIER),
	Jmp(["EVENT_3080_jmp_if_var_equals_const_7"]),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=COIN_CHEST_MULTIPLIER, identifier="EVENT_3080_copy_var_to_var_11"),
	CopyVarToVar(from_var=ITEM_ID, to_var=PRIMARY_TEMP_7000),
	Mem7000AndConst(0x000F),
	AddVarTo7000(COIN_CHEST_MULTIPLIER),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=COIN_CHEST_MULTIPLIER),
	SetVarToConst(PRIMARY_TEMP_7000, 0),
	JmpIfVarEqualsConst(COIN_CHEST_MULTIPLIER, 0, ["EVENT_3080_add_coins_21"], identifier="EVENT_3080_jmp_if_var_equals_const_17"),
	AddConstToVar(PRIMARY_TEMP_7000, 10),
	Dec(COIN_CHEST_MULTIPLIER),
	Jmp(["EVENT_3080_jmp_if_var_equals_const_17"]),
	AddCoins(PRIMARY_TEMP_7000, identifier="EVENT_3080_add_coins_21"),
	SummonObjectToCurrentLevel(MEM_70A8),
	RunDialog(dialog_id=DI0515_GOT_X_COINS, above_object=MARIO, closable=False, sync=True, multiline=False, use_background=False, bit_6=True),
	DisableObjectTrigger(MEM_70A8),
	PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
	DisableTriggerOfObjectAt70A8InCurrentLevel(),
	SetSyncActionScript(MEM_70A8, A0007_HIT_TREASURE_CHEST_CONTENTS_DEPLETED),
	Set70107015ToObjectXYZ(target=MEM_70A8),
	CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_7000),
	AddConstToVar(PRIMARY_TEMP_7000, 608),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Z_COORD_1),
	JmpIfBitSet(UNKNOWN_704A_3, ["EVENT_3080_clear_bit_34"]),
	PlaySound(sound=SO013_COIN, channel=6),
	ClearBit(UNKNOWN_704A_3, identifier="EVENT_3080_clear_bit_34"),
	CreatePacketAt7010(packet=P016_BIG_COIN_BEING_COLLECTED, destinations=["EVENT_3080_ret_36"]),
	Return(identifier="EVENT_3080_ret_36")
])
