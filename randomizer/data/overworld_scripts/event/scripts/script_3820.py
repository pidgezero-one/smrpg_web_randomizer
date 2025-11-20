# E3820_FORCED_TOWER_BOSS_1_FIGHT
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
	EnableControlsUntilReturn([]),
	StartBattleAtBattlefield(PACK161_BOOSTER_FIGHT_STATIC, BF12_BOOSTER_TOWER),
	JmpIfBitClear(GAME_OVER, ["EVENT_3820_remove_from_level_4"]),
	ResetAndChooseGame(),
	RemoveObjectFromSpecificLevel(NPC_7, R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, identifier="EVENT_3820_remove_from_level_4"),
	RemoveObjectFromCurrentLevel(NPC_7),
	FadeInFromBlack(sync=False),
	JmpIfBitSet(TOWER_BOSS_1_STAR_PIECE, ["EVENT_3820_ret_10"]),
	SetBit(TOWER_BOSS_1_STAR_PIECE),
	JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
	Return(identifier="EVENT_3820_ret_10")
])
