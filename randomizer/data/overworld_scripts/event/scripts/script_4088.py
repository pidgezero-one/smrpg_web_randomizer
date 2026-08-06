# E4088_PACKET_OF_E3937 (auto: E3937 minus FD F2 presence-commit, jumps repointed)
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
	DisableObjectTrigger(MEM_70A8),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_VisibilityOff(),
	]),
	PlaySound(sound=SO085_FLOWER, channel=6),
	JmpIfBitClear(SHIP_PACKET_AUTOTERM_DIALOG, ["e4088_await"]),
	RunDialog(dialog_id=DI3061_RING_AUTOTERM, above_object=BOWSER, closable=False, sync=True, multiline=False, use_background=False),
	Jmp(["e4088_tail"]),
	RunDialog(dialog_id=DI2097_GOT_RING, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False, identifier="e4088_await"),
	Inc(WEDDING_GEAR_COUNTER, identifier="e4088_tail"),
	AddToInventory(RingItem),
	Return()
])