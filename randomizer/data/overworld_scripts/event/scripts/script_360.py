# E0360_TREASURY_PRIZE
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
	JmpIfVarEqualsConst(ACTIVE_NPC, NPC_0, ["EVENT_360_jmp_to_event_5"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, NPC_1, ["EVENT_360_jmp_to_event_6"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, NPC_2, ["EVENT_360_jmp_to_event_7"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, NPC_3, ["EVENT_360_jmp_to_event_8"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, NPC_4, ["EVENT_360_jmp_to_event_9"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, NPC_5, ["EVENT_360_jmp_to_event_10"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, NPC_6, ["EVENT_360_jmp_to_event_11"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, NPC_7, ["EVENT_360_jmp_to_event_12"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, NPC_8, ["EVENT_360_jmp_to_event_13"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, NPC_9, ["EVENT_360_jmp_to_event_14"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, NPC_10, ["EVENT_360_jmp_to_event_15"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, NPC_11, ["EVENT_360_jmp_to_event_16"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, NPC_12, ["EVENT_360_jmp_to_event_17"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, NPC_13, ["EVENT_360_jmp_to_event_18"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, NPC_14, ["EVENT_360_jmp_to_event_19"]),
	Return(),
	JmpToEvent(E0241_FREESTANDING_1_GRANT, identifier="EVENT_360_jmp_to_event_5"),
	JmpToEvent(E0240_FREESTANDING_2_GRANT, identifier="EVENT_360_jmp_to_event_6"),
	JmpToEvent(E0239_FREESTANDING_3_GRANT, identifier="EVENT_360_jmp_to_event_7"),
	JmpToEvent(E0238_FREESTANDING_4_GRANT, identifier="EVENT_360_jmp_to_event_8"),
	JmpToEvent(E0237_FREESTANDING_5_GRANT, identifier="EVENT_360_jmp_to_event_9"),
	JmpToEvent(E0236_FREESTANDING_6_GRANT, identifier="EVENT_360_jmp_to_event_10"),
	JmpToEvent(E0235_FREESTANDING_7_GRANT, identifier="EVENT_360_jmp_to_event_11"),
	JmpToEvent(E0234_FREESTANDING_8_GRANT, identifier="EVENT_360_jmp_to_event_12"),
	JmpToEvent(E0233_FREESTANDING_9_GRANT, identifier="EVENT_360_jmp_to_event_13"),
	JmpToEvent(E0232_FREESTANDING_10_GRANT, identifier="EVENT_360_jmp_to_event_14"),
	JmpToEvent(E0231_FREESTANDING_11_GRANT, identifier="EVENT_360_jmp_to_event_15"),
	JmpToEvent(E0230_FREESTANDING_12_GRANT, identifier="EVENT_360_jmp_to_event_16"),
	JmpToEvent(E0229_FREESTANDING_13_GRANT, identifier="EVENT_360_jmp_to_event_17"),
	JmpToEvent(E0228_FREESTANDING_14_GRANT, identifier="EVENT_360_jmp_to_event_18"),
	JmpToEvent(E0227_FREESTANDING_15_GRANT, identifier="EVENT_360_jmp_to_event_19")
])
