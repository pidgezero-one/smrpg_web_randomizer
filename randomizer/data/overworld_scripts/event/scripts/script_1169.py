# E1169_EMPTY

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
	ActionQueueAsync(target=NPC_16, subscript=[
		A_ShadowOn()
	]),
	ActionQueueAsync(target=NPC_15, subscript=[
		A_ShadowOn()
	]),
	ActionQueueAsync(target=NPC_14, subscript=[
		A_ShadowOn()
	]),
	ActionQueueAsync(target=NPC_13, subscript=[
		A_ShadowOn()
	]),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_ShadowOn()
	]),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_ShadowOn()
	]),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_ShadowOn()
	]),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_ShadowOn()
	]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_ShadowOn()
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_ShadowOn()
	]),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_ShadowOn()
	]),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_ShadowOn()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_ShadowOn()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_ShadowOn()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_ShadowOn()
	]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ShadowOn()
	]),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_ShadowOn()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ShadowOn()
	]),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 192, ["EVENT_1364_set_var_to_const_2"]),
	Return(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	Return()
])
