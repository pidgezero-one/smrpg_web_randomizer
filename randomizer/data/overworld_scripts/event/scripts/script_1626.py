# E1626_MOLEVILLE_CARBO_COOKIE_TRADER

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
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AE),
	JmpIfBitSet(BUCKET_PRIZE_GRANT_NO_WARP, ["EVENT_1626_store_item_amount_7000_21"]),
	JmpIfBitSet(SHUFFLE_ONE_FIREWORKS_ENABLED, ["EVENT_1626_run_dialog_8"]),
	JmpIfBitClear(PROGRESSIVE_FIREWORKS_ENABLED, ["EVENT_1626_store_item_amount_7000_6"]),
	JmpIfBitSet(FIRST_CARBO_COOKIE_GIVEN, ["EVENT_1626_store_item_amount_7000_21"]),
	StoreItemAmountTo7000(ShinyStoneItem, identifier="EVENT_1626_store_item_amount_7000_6"),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1626_run_dialog_10"]),
	RunDialog(dialog_id=DI1156_BEAN_VALLEY_PLATFORM_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1626_run_dialog_8"),
	Return(),
	RunDialog(dialog_id=DI1159_ASK_TO_TRADE_COOKIE_FOR_STONE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1626_run_dialog_10"),
	JmpIfDialogOptionBSelected(["EVENT_1626_pause_18"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	RemoveOneOfItemFromInventory(ShinyStoneItem),
	SetVarToConst(ITEM_ID, CarboCookieItem),
	RunEventAsSubroutine(E0160_NPC_QUEST_GRANT_ITEM),
	Return(),
	Pause(10, identifier="EVENT_1626_pause_18"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Return(),
	StoreItemAmountTo7000(ShinyStoneItem, identifier="EVENT_1626_store_item_amount_7000_21"),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1626_run_dialog_8"]),
	RunDialog(dialog_id=DI1158_OFFER_TO_RETURN_SHINY_STONE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_1626_pause_18"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	SetVarToConst(ITEM_ID, ShinyStoneItem),
	RunEventAsSubroutine(E0160_NPC_QUEST_GRANT_ITEM),
	Return()
])
