# E4083_PACKET_OF_E3111 (auto: E3111 minus FD F2 presence-commit, jumps repointed)
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
	DisableObjectTrigger(MEM_70A8),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_VisibilityOff(),
	]),
	StoreItemAmountTo7000(MysteryEggItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_4083L_3111_set_var_to_const_15"]),
	StoreItemAmountTo7000(LambsLureItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_4083L_3111_set_var_to_const_12"]),
	StoreItemAmountTo7000(SheepAttackItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_4083L_3111_set_var_to_const_8"]),
	SetVarToConst(ITEM_ID, MysteryEggItem),
	JmpToEvent(E4077_PACKET_OF_E0165),
	SetVarToConst(ITEM_ID, SheepAttackItem, identifier="EVENT_4083L_3111_set_var_to_const_8"),
	JmpToEvent(E4077_PACKET_OF_E0165),
	SetVarToConst(ITEM_ID, SheepAttackItem, identifier="EVENT_4083L_3111_set_var_to_const_12"),
	RemoveOneOfItemFromInventory(LambsLureItem),
	JmpToEvent(E4077_PACKET_OF_E0165),
	SetVarToConst(ITEM_ID, LambsLureItem, identifier="EVENT_4083L_3111_set_var_to_const_15"),
	RemoveOneOfItemFromInventory(MysteryEggItem),
	JmpToEvent(E4077_PACKET_OF_E0165)
])