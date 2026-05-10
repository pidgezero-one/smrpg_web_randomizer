# E1750_TEMPLE_BOSS_POSTGAME
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
	SetVarToConst(PRIMARY_TEMP_7000, 523),
	SetBit(TEMPLE_POSTGAME_BOSS_DEFEATED),
	RunEventAsSubroutine(E0353_BOSS_BATTLE),
	RemoveObjectFromCurrentLevel(NPC_1),
	JmpIfBitSet(RUN_AWAY, ["EVENT_1750_set_temp_action_script_18"]),
	JmpIfBitSet(GAME_OVER, ["EVENT_1750_reset_and_choose_game_17"]),
	RestoreAllHP(),
	RestoreAllFP(),
	FadeInFromBlack(sync=False),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	RunEventAsSubroutine(E1212_POSTGAME_TEMPLE_BOSS_UNLOCKS),
	SetVarToConst(PRIMARY_TEMP_7000, 523),
	JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE),
	FadeInFromBlack(sync=False, identifier="EVENT_1750_set_temp_action_script_18"),
    Return(),
	ResetAndChooseGame(identifier="EVENT_1750_reset_and_choose_game_17"),
])
