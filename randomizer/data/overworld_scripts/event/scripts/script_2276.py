# E2276_TREASURE_SHOP_SIGNOFF
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
    # All 3 items purchased
    JmpIfBitClear(TREASURE_SHOP_ITEM_1_PURCHASED, ["EVENT_2276_check_availability"]),
    JmpIfBitClear(TREASURE_SHOP_ITEM_2_PURCHASED, ["EVENT_2276_check_availability"]),
    JmpIfBitClear(TREASURE_SHOP_ITEM_3_PURCHASED, ["EVENT_2276_check_availability"]),
	RunDialog(dialog_id=DI2907_TREASURE_SELLER_SOLD_OUT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
    Return(),
    # All 3 items available, but not all have been purchased
    JmpIfBitClear(VOLCANO_LIBERATED, ["EVENT_2276_jmp_if_bit_set_6"], identifier="EVENT_2276_check_availability"),
    JmpIfBitClear(SEASIDE_LIBERATED, ["EVENT_2276_jmp_if_bit_set_6"]),
	RunDialog(dialog_id=DI2902_TREASURE_SELLER_ALL_ITEMS_UNLOCKED, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
    Return(),
    # Suggests to unlock item 2 if haven't already
	RunDialog(dialog_id=DI2909_TREASURE_SELLER_ALL_IVE_GOT_FOR_NOW, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2276_jmp_if_bit_set_6"),
    JmpIfBitSet(SEASIDE_LIBERATED, ["EVENT_2276_jmp_if_bit_set_7"]),
	RunDialog(dialog_id=DI2915_TREASURE_SELLER_2ND_UNLOCK_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
    Return(),
    # Suggests to unlock item 3
	RunDialog(dialog_id=DI2905_TREASURE_SELLER_3RD_UNLOCK_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2276_jmp_if_bit_set_7"),
    Return(),
])
