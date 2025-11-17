# E2498_EMPTY

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
	SetVarToConst(GAME_OVER_COUNTER_MAYBE, 2),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ShadowOn(),
		A_WalkSoutheastPixels(6),
		A_FaceSouthwest(),
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_ShadowOn(),
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_ShadowOn(),
		A_WalkNorthwestPixels(5),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_ShadowOn(),
		A_WalkSoutheastPixels(5),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_ShadowOn(),
		A_WalkSoutheastPixels(5),
		A_FaceNorthwest()
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_ShadowOn(),
		A_WalkNorthwestPixels(5),
		A_FaceSoutheast()
	]),
	SetSyncActionScript(NPC_4, A0547_KEEP_CROSSING_TERRA_COTTAS),
	SetSyncActionScript(NPC_5, A0548_KEEP_CROSSING_TERRA_COTTAS),
	SetSyncActionScript(NPC_6, A0548_KEEP_CROSSING_TERRA_COTTAS),
	SetSyncActionScript(NPC_7, A0547_KEEP_CROSSING_TERRA_COTTAS),
	FadeInFromBlack(sync=False),
	Return()
])
