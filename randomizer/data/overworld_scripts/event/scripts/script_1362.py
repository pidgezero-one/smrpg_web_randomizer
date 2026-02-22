# E1362_CURTAIN_3
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
from ....spells.spells import *

script = EventScript([
	SetBit(TEMP_7043_2),
    JmpIfBitClear(TOWER_BOSS_1_STAR_PIECE, ["EVENT_1362_bg_thread"]),
    JmpIfObjectNotInSpecificLevel(NPC_5, R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, ["EVENT_1362_bg_thread"]),
    Set7016701BToObjectXYZ(NPC_5),
    JmpIfVarEqualsConst(Z_COORD_1, 0, ["EVENT_1362_bg_thread"]),
    JmpIfBitClear(TEMP_7043_2, ["EVENT_1362_ret_6"], identifier="EVENT_1362_jump_check_loop"),
	Set7000ToTappedButton(),
    Pause(1),
	Mem7000AndConst(0x0080),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_1362_action_queue_54"]),
	Jmp(["EVENT_1362_jump_check_loop"]),
	EnableControlsUntilReturn([], identifier="EVENT_1362_action_queue_54"),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(112),
		A_Pause(60),
		A_SetSequenceSpeed(NORMAL),
	], identifier="EVENT_1368_action_queue_54"),
	ActionQueueSync(target=NPC_5, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_Pause(8),
		A_SetWalkingSpeed(FAST),
		A_FloatingOn(),
		A_ShadowOff(),
		A_JumpToHeight(height=64, silent=True),
		A_WalkSoutheastSteps(3)
	]),
    Return(),
    
	MoveScriptToBackgroundThread2(identifier="EVENT_1362_bg_thread"),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_1362_ret_6"]),
	ClearBit(TEMP_7043_0),
	ClearBit(TEMP_7043_1),
	ClearBit(TEMP_7043_3),
	Return(identifier="EVENT_1362_ret_6")
])
