# E0293_WALLET_TOAD_1

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
	JmpIfBitSet(WALLET_SOLD, ["EVENT_395_run_dialog_35"]),
	JmpIfBitSet(WALLET_RETURNED, ["EVENT_293_run_dialog_18"]),
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_293_jmp_if_bit_clear_14"]),
	JmpIfBitSet(MUSHROOM_KINGDOM_OCCUPIED, ["EVENT_395_jmp_if_bit_set_0"]),
	PauseActionScript(MEM_70A8, identifier="EVENT_293_pause_action_script_4"),
	SetSyncActionScript(MEM_70A8, A0099_LOOPED_JUMPING),
	RunDialog(dialog_id=DI0578_WALLET_GUY_INTRO, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	PauseActionScript(MEM_70A8),
	Pause(1, identifier="EVENT_293_pause_8"),
	JmpIfObjectInAir(MEM_70A8, ["EVENT_293_pause_8"]),
	RunDialog(dialog_id=DI0579_WALLET_GUY_PROMISE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	StartAsyncEmbeddedActionScript(target=MEM_70A8, prefix=0xF1, subscript=[
		A_SetSolidityBits(cant_pass_walls=True),
		A_FloatingOn(),
		A_SetSolidityBits(cant_walk_through=True)
	]),
	SetSyncActionScript(MEM_70A8, A0021_STAND_STILL_AND_MOVE_RANDOM_DIRECTIONS),
	Return(),
	JmpIfBitClear(REFUSED_TO_RETURN_WALLET, ["EVENT_395_jmp_if_bit_set_0"], identifier="EVENT_293_jmp_if_bit_clear_14"),
	SetBit(WALLET_RETURNED),
	RunEventAsSubroutine(E0180_NPC_QUEST_3_CONTAINER),
	Return(),
	RunDialog(dialog_id=DI2242_TROOPA_CLIFF_HINT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_293_run_dialog_18"),
	Return()
])
