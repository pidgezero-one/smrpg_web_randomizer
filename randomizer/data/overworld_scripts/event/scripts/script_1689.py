# E1689_TEMPLE_PIPE_TO_BOSS_FIGHT
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
	SetVarToConst(UNKNOWN_70AD, 0),
	SetVarToConst(X_COORD_2, 7440),
	RunEventAsSubroutine(E0066_PIPE_DOWN_SUBROUTINE),
    SetBit(DIRECTIONAL_7049_0),
	EnableControls([]),
	JmpIfBitSet(TEMPLE_POSTGAME_BOSS_DEFEATED, ["enter_boss_room"]),
    JmpIfBitClear(TEMPLE_BOSS_DEFEATED, ["enter_boss_room"]),
    JmpIfBitClear(STAY_VOUCHER_USED, ["enter_boss_room"]),
	EnterArea(room_id=R293_BELOME_3_ROOM, face_direction=SOUTH, x=4, y=43, z=9, identifier="enter_boss_room_2"),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(height=0, silent=True)
	]),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	EnterArea(room_id=R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM, face_direction=SOUTH, x=4, y=43, z=9, identifier="enter_boss_room"),
    SetBit(DIRECTIONAL_7049_0),
	ActionQueueSync(target=MARIO, subscript=[
		A_JumpToHeight(height=0, silent=True)
	]),
	JmpToEvent(E1771_TEMPLE_BOSS_ROOM_LOADER),
])
