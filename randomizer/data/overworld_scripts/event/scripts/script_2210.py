# E2210_KEEP_1ST_BOSS_HEALS_YOU
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
    ActionQueueSync(NPC_2, [
        A_FaceSoutheast(),
	]),
    ActionQueueAsync(MARIO, [
        A_SetAllSpeeds(FAST),
        A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
        A_WalkToXYCoords(25, 100),
        A_FaceNorthwest(),
	]),
    EnableControlsUntilReturn([]),
    Pause(30),
    ActionQueueSync(NPC_2, [
        A_SetSequenceSpeed(NORMAL),
        A_SetSpriteSequence(index=10, looping=False, mirror_sprite=True, is_sequence=True, identifier="keep_boss_1_heal"),
		A_Pause(80, identifier="keep_boss_1_heal_length"),
        A_ResetProperties(),
	], identifier="keep_boss_1_heal_aq"),
    ActionQueueSync(MARIO, [
        A_SetSequenceSpeed(NORMAL),
        A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
        A_Pause(55, identifier="keep_heal_arms_go_up"),
        A_SetSpriteSequence(index=15, sprite_offset=2, is_mold=True, looping=True, mirror_sprite=True, is_sequence=True, identifier="keep_heal_arms_raised"),
        A_Pause(30, identifier="keep_heal_arms_go_down"),
        A_ResetProperties(),
	], identifier="keep_heal_arms_raised_aq"),
    Pause(60, identifier="keep_heal_animation_starts"),
	PlaySound(sound=SO071_MUSHROOM_CURE, channel=6),
	TintLayers(layers=[LAYER_L1, LAYER_L2, LAYER_L3, LAYER_L4, NPC_SPRITES, BACKGROUND], red=64, green=160, blue=64, speed=3, bit_15=True),
	TintLayers(layers=[LAYER_L1, LAYER_L2, LAYER_L3, LAYER_L4, NPC_SPRITES, BACKGROUND], red=0, green=0, blue=0, speed=3, bit_15=True),
	ResetPrioritySet(),
	RestoreAllHP(),
	RestoreAllFP(),
    Pause(20, identifier="keep_heal_animation_ends"),
    EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, B, X, Y]),
	Return()
])
