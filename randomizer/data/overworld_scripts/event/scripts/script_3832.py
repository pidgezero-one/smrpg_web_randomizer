# E3832_EMPTY

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
	JmpIfObjectInCurrentLevel(NPC_0, ["EVENT_3832_play_sound_7"]),
	SetVarToConst(ITEM_ID, SonicCymbalItem),
	RunEventAsSubroutine(E0032_NON_COIN_CHEST_CONTAINER),
	Inc(HIDDEN_CHEST_COUNTER),
	DisableObjectTriggerInSpecificLevel(NPC_0, R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT),
	DisableObjectTriggerInSpecificLevel(NPC_0, R484_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_BASEMENT),
	JmpToEvent(E3837_EMPTY),
	PlaySound(sound=SO014_FLOWER, channel=6, identifier="EVENT_3832_play_sound_7"),
	SummonObjectToCurrentLevel(NPC_0),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 492, ["EVENT_3832_apply_tile_mod_13"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R484_MUSHROOM_KINGDOM_DURING_MACK_ITEM_SHOP_BASEMENT, mod_id=0),
	Jmp(["EVENT_3832_set_action_script_14"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT, mod_id=0, identifier="EVENT_3832_apply_tile_mod_13"),
	SetSyncActionScript(NPC_0, A0014_FLOATING_CHEST, identifier="EVENT_3832_set_action_script_14"),
	Return()
])
