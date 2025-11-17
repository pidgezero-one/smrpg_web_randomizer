# E0395_WALLET_TOAD_2

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
	JmpIfBitSet(WALLET_SOLD, ["EVENT_395_run_dialog_35"], identifier="EVENT_395_jmp_if_bit_set_0"),
	JmpIfBitSet(WALLET_GUY_UNKNOWN_7083_3, ["EVENT_395_run_event_as_subroutine_25"]),
	JmpIfBitSet(REFUSED_TO_RETURN_WALLET, ["EVENT_395_run_dialog_30"]),
	StoreItemAmountTo7000(WalletItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_293_pause_action_script_4"]),
	RunEventAsSubroutine(E3587_SET_70AE_TO_70A8),
	RunDialog(dialog_id=DI0669_ASKS_FOR_WALLET_BACK, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_395_set_action_script_19"], identifier="EVENT_395_jmp_if_dialog_option_b_7"),
	Pause(10),
	RunEventAsSubroutine(E3587_SET_70AE_TO_70A8),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	RunDialog(dialog_id=DI0671_THANKS_FOR_RETURNING_WALLET, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	RunEventAsSubroutine(E0179_NPC_QUEST_2_CONTAINER),
	RemoveOneOfItemFromInventory(WalletItem),
	SetBit(REFUSED_TO_RETURN_WALLET),
	ClearBit(WALLET_GUY_UNKNOWN_7083_3),
	SetSyncActionScript(MEM_70A8, A0978_RANDOMLY_FACE_SOUTHWEST),
	Return(),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO, identifier="EVENT_395_set_action_script_19"),
	RememberLastObject(),
	Pause(10),
	RunDialog(dialog_id=DI0670_YOURE_TERRIBLE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(WALLET_GUY_UNKNOWN_7083_3),
	Return(),
	RunEventAsSubroutine(E3587_SET_70AE_TO_70A8, identifier="EVENT_395_run_event_as_subroutine_25"),
	RunDialog(dialog_id=DI0672_DEMANDS_WALLET_BACK_AGAIN, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	StoreItemAmountTo7000(WalletItem),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_395_run_dialog_34"]),
	Jmp(["EVENT_395_jmp_if_dialog_option_b_7"]),
	RunDialog(dialog_id=DI0668_THAT_WAS_TOO_DARN_CLOSE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_395_run_dialog_30"),
	Return(),
	SetBit(TEMP_7043_6),
	Jmp(["EVENT_293_pause_action_script_4"]),
	RunDialog(dialog_id=DI0889_WALLET_THREAT, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True, identifier="EVENT_395_run_dialog_34"),
	RunDialog(dialog_id=DI0890_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_395_run_dialog_35"),
	SetBit(WALLET_SOLD),
	Return()
])
