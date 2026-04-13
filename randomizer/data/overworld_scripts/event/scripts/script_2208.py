# E2208_KEEP_1ST_BOSS_ROOM_LOADER
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
	JmpIfBitSet(KEEP_BOSS_1_DEFEATED, ["kamek_palette_2"]),
	RunEventAsSubroutine(E0847_KEEP_FIRST_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	JmpToEvent(E2209_KEEP_1ST_BOSS_FIGHT),
	Return(),
	PaletteSet(palette_set_starts_at=EPAL0138_KAMEK_BLUE, from_row=NPC_PALETTE_ROW_2, identifier="kamek_palette_2"),
	PaletteSet(palette_set_starts_at=EPAL0139_GOLD_CHEST, from_row=NPC_PALETTE_ROW_1, identifier="infinite_coin_chest_palette_2"),
    JmpIfObjectTriggerDisabledInSpecificLevel(NPC_0, R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM, ["move_magikoopa_to_defeated_position"]),
	SetSyncActionScript(NPC_0, A0014_FLOATING_CHEST),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShiftToXYCoords(x=24, y=98),
		A_VisibilityOn(),
		A_FaceSoutheast(),
		A_SequenceLoopingOn()
	], identifier="move_magikoopa_to_defeated_position"),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=27, y=104, z=7, direction=EAST),
		A_VisibilityOn()
	]),
	RunEventAsSubroutine(E0847_KEEP_FIRST_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	Return()
])
