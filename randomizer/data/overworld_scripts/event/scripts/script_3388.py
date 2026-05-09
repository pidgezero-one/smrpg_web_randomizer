# E3388_SHIP_BOSS_ROOM_PERISCOPE
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
	JmpIfBitSet(JOHNNY_POSITION, ["EVENT_3388_ret_25"]),
	EnterArea(room_id=R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM, face_direction=SOUTH, x=7, y=82, z=0, run_entrance_event=True),
	RemoveObjectFromCurrentLevel(MARIO, identifier="EVENT_3388_remove_from_current_level_15"),
	CircleMaskShrinkToObject(target=MARIO, width=96, speed=8, static=True),
	Pause(180),
	Pause(180),
	CircleMaskShrinkToObject(target=MARIO, width=0, speed=8, static=True),
	JmpIfBitSet(TEMP_7043_7, ["EVENT_3388_enter_area_16"]),
	EnterArea(room_id=R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM, face_direction=NORTHEAST, x=24, y=110, z=0),
	Jmp(["EVENT_3388_run_event_as_subroutine_17"]),
	EnterArea(room_id=R003_POSTGAME_SHIP, face_direction=NORTHEAST, x=24, y=110, z=0, identifier="EVENT_3388_enter_area_16"),
	RunEventAsSubroutine(E0801_SHIP_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER, identifier="EVENT_3388_run_event_as_subroutine_17"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkNortheastPixels(4)
	]),
	FadeInFromBlack(sync=False),
    ClearBit(TEMP_7043_7),
	Return(identifier="EVENT_3388_ret_25")
])
