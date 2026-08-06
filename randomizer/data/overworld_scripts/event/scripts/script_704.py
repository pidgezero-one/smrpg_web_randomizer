# E0704_BOOSTER_TOWER_POSTGAME_LOADER
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
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(2, is_sequence=True, looping=True, identifier="EVENT_704_set_sprite_sequence_0"),
        A_SequenceLoopingOn(),
        A_FixedFCoordOn(),
		A_WalkNorthPixels(8),
		A_WalkWestPixels(8),
        A_FixedFCoordOff(),
	], identifier="EVENT_704_action_queue_sync_0"),
	ActionQueueAsync(target=LAYER_1, subscript=[
		A_WalkEastPixels(8),
		A_WalkNorthPixels(8)
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_WalkSouthPixels(22),
		A_WalkEastPixels(7),
		A_SetPriority(2),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	RunEventAsSubroutine(E1090_BOOSTER_TOWER_POSTGAME_SHUFFLED_NPC_ANIMATION_LOADER),
    FadeInFromBlack(sync=False),
	Return()
])
