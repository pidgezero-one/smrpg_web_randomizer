# E2080_MUSTY_FEARS_ROOM_LOADER

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
	JmpIfBitClear(INVISIBLE_ITEMS_ANYWHERE, ["EVENT_2080_action_queue_6"]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_VisibilityOn(),
		A_SequenceLoopingOn()
	]),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_VisibilityOn(),
		A_SequenceLoopingOn()
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_VisibilityOn(),
		A_SequenceLoopingOn()
	]),
	Jmp(["EVENT_2080_fade_in_from_black_async_7"]),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_WalkNorthwestPixels(4),
		A_WalkNorthPixels(9),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_SetVRAMPriority(NORMAL_PRIORITY)
	], identifier="EVENT_2080_action_queue_6"),
	FadeInFromBlack(sync=False, identifier="EVENT_2080_fade_in_from_black_async_7"),
	RunEventAsSubroutine(E0091_INVISIBLE_ITEM_SUMMONER),
	Return()
])
