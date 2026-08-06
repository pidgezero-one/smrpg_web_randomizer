# E1055_VAULT_LOADER
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
    # Need to force-start action scripts for 3, 4, and 5
    JmpIfBitClear(MUSHROOM_KINGDOM_OCCUPIED, ["pre_occupied"]),
    JmpIfObjectTriggerDisabledInSpecificLevel(NPC_0, R031_MUSHROOM_KINGDOM_CASTLE_VAULT, ["left_flipped"]),
	SummonObjectToCurrentLevel(NPC_0),
	RemoveObjectFromCurrentLevel(NPC_3),
    Jmp(["is_right_flipped"]),
	RemoveObjectFromCurrentLevel(NPC_0, identifier="left_flipped"),
	SummonObjectToCurrentLevel(NPC_3),
    JmpIfObjectTriggerDisabledInSpecificLevel(NPC_3, R031_MUSHROOM_KINGDOM_CASTLE_VAULT, ["is_right_flipped"]),
    ResumeActionScript(NPC_3),
    JmpIfObjectTriggerDisabledInSpecificLevel(NPC_1, R031_MUSHROOM_KINGDOM_CASTLE_VAULT, ["right_flipped"], identifier="is_right_flipped"),
	SummonObjectToCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_4),
    Jmp(["is_middle_flipped"]),
	RemoveObjectFromCurrentLevel(NPC_1, identifier="right_flipped"),
	SummonObjectToCurrentLevel(NPC_4),
    JmpIfObjectTriggerDisabledInSpecificLevel(NPC_4, R031_MUSHROOM_KINGDOM_CASTLE_VAULT, ["is_middle_flipped"]),
    ResumeActionScript(NPC_4),
    JmpIfObjectTriggerDisabledInSpecificLevel(NPC_2, R031_MUSHROOM_KINGDOM_CASTLE_VAULT, ["middle_flipped"], identifier="is_middle_flipped"),
	SummonObjectToCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_5),
    JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	RemoveObjectFromCurrentLevel(NPC_2, identifier="middle_flipped"),
    SummonObjectToCurrentLevel(NPC_5),
    JmpIfObjectTriggerDisabledInSpecificLevel(NPC_5, R031_MUSHROOM_KINGDOM_CASTLE_VAULT, ["1055_exit"]),
    ResumeActionScript(NPC_5),
    JmpToEvent(E0015_STANDARD_ROOM_LOADER, identifier="1055_exit"),
	SummonObjectToCurrentLevel(NPC_0, identifier="pre_occupied"),
	SummonObjectToCurrentLevel(NPC_1),
	SummonObjectToCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_4),
	RemoveObjectFromCurrentLevel(NPC_5),
    JmpToEvent(E0015_STANDARD_ROOM_LOADER),
])
