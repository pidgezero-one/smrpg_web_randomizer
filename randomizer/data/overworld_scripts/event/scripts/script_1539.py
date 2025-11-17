# E1539_EMPTY

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
	DisableObjectTrigger(MEM_70A8),
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AE),
	FreezeAllNPCsUntilReturn(),
	ResumeActionScript(NPC_6),
	ResumeActionScript(NPC_7),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	SetSyncActionScript(MEM_70A8, A0470_COLLECT_MIDAS_COIN),
	Pause(7),
	MoveScriptToBackgroundThread2(),
	SetVarToConst(PRIMARY_TEMP_7000, 1),
	AddCoins(PRIMARY_TEMP_7000),
	Pause(12),
	UnfreezeAllNPCs(),
	MoveScriptToMainThread(),
	CopyVarToVar(from_var=TEMP_70AE, to_var=PRIMARY_TEMP_7000),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 23, ["EVENT_1539_jmp_if_var_not_equals_short_19"]),
	SetSyncActionScript(NPC_4, A0468_EMPTY),
	SetBit(GAMEBOY_KID_PURCHASE_COMPLETE),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 24, ["EVENT_1539_ret_22"], identifier="EVENT_1539_jmp_if_var_not_equals_short_19"),
	SetSyncActionScript(NPC_5, A0468_EMPTY),
	SetBit(STAR_PIECE_GRANT_DIRECTIONAL_BIT),
	Return(identifier="EVENT_1539_ret_22")
])
