# E2428_EMPTY

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
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(UNUSED_7091_2, ["EVENT_2428_jmp_if_bit_clear_3"]),
	SetSyncActionScript(NPC_2, A0690_OPENING_CHEST),
	JmpIfBitClear(DIRECTIONAL_7047_0, ["EVENT_2428_fade_in_from_black_async_14"], identifier="EVENT_2428_jmp_if_bit_clear_3"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_VisibilityOff()
	]),
	FadeInFromBlack(sync=False),
	FreezeCamera(),
	SetAsyncActionScript(MARIO, A0482_FOREST_PLAYER_FALLS_TO_UNDERGROUND),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2428_unfreeze_camera_12"]),
	JmpIfBitSet(UNUSED_7091_2, ["EVENT_2428_unfreeze_camera_12"]),
	Pause(24),
	UnfreezeCamera(identifier="EVENT_2428_unfreeze_camera_12"),
	Jmp(["EVENT_2428_jmp_if_bit_clear_15"]),
	FadeInFromBlack(sync=False, identifier="EVENT_2428_fade_in_from_black_async_14"),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2428_clear_bit_19"], identifier="EVENT_2428_jmp_if_bit_clear_15"),
	JmpIfBitSet(UNUSED_7091_2, ["EVENT_2428_clear_bit_19"]),
	ClearBit(SIGNAL_RING_BIT),
	PlaySound(sound=SO149_CASINO_SECRET_PASSAGE, channel=6),
	ClearBit(SIGNAL_RING_BIT, identifier="EVENT_2428_clear_bit_19"),
	Return()
])
