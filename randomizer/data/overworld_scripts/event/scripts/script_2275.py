# E2275_TREASURE_SHOP_ITEM_3
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
    JmpIfBitClear(VOLCANO_LIBERATED, ["EVENT_2275_end"]),
	JmpIfBitSet(TREASURE_SHOP_ITEM_3_PURCHASED, ["EVENT_2275_end"]),
	RunDialog(dialog_id=DI2914_TREASURE_SELLER_ITEM_3, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_2275_end"]),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 300),
	JmpIfComparisonResultIsLesser(["EVENT_2275_run_dialog_19"]),
	SetVarToConst(PRIMARY_TEMP_7000, 300),
	Dec7000FromCoins(),
	SetBit(TREASURE_SHOP_ITEM_3_PURCHASED),
	RunDialog(dialog_id=DI2912_TREASURE_SELLER_SUCCESSFUL_SALE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RunEventAsSubroutine(E0180_NPC_QUEST_3_CONTAINER),
    Return(),
	RunDialog(dialog_id=DI2910_TREASURE_SELLER_INSUFFICIENT_COINS, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2275_run_dialog_19"),
    Return(identifier="EVENT_2275_end"),
])
