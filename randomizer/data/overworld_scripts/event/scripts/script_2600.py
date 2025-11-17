# E2600_EMPTY

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
	JmpIfBitSet(UNUSED_708F_4, ["EVENT_2600_ret_15"]),
	PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
	SetSyncActionScript(MEM_70A8, A0007_HIT_TREASURE_CHEST_CONTENTS_DEPLETED),
	Set70107015ToObjectXYZ(target=NPC_4),
	PlaySound(sound=SO014_FLOWER, channel=6),
	CreatePacketAt7010(packet=P001_FLASHING_POOF_MUSHROOM, destinations=["EVENT_2600_ret_15"]),
	RestoreAllHP(),
	RestoreAllFP(),
	SetVarToConst(TIMER_7020, 8),
	RunBackgroundEventWithPause(event_id=E3075_HEAL_FLASH, timer_var=TIMER_7020, bit_4=True, bit_5=True),
	SetBit(UNUSED_708F_4),
	Inc(HIDDEN_CHEST_COUNTER),
	SummonObjectToSpecificLevel(NPC_1, R237_SMITHY_FACTORY_AREA_05_WSAVE_POINT),
	SummonObjectToSpecificLevel(NPC_3, R237_SMITHY_FACTORY_AREA_05_WSAVE_POINT),
	RemoveObjectFromSpecificLevel(NPC_2, R237_SMITHY_FACTORY_AREA_05_WSAVE_POINT),
	Return(identifier="EVENT_2600_ret_15")
])
