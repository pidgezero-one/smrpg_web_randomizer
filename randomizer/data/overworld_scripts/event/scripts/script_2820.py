# E2820_ASYNC_NO_ANIMATION_ITEM
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

script = EventScript([
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	JmpIfVarEqualsConst(ITEM_ID, UltraHammerItem, ["EVENT_2820_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, AmuletItem, ["EVENT_2820_run_dialog_16"], identifier="EVENT_2820_delete_vowel_1"),
	JmpIfVarEqualsConst(ITEM_ID, AttackScarfItem, ["EVENT_2820_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, ExpBoosterItem, ["EVENT_2820_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, AntidotePinItem, ["EVENT_2820_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, AbleJuiceItem, ["EVENT_2820_run_dialog_16"], identifier="EVENT_2820_delete_vowel_2"),
	JmpIfVarEqualsConst(ITEM_ID, EnergizerItem, ["EVENT_2820_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, IceBombItem, ["EVENT_2820_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, ElixirItem, ["EVENT_2820_run_dialog_16"], identifier="EVENT_2820_delete_vowel_3"),
	JmpIfVarEqualsConst(ITEM_ID, EarlierTimesItem, ["EVENT_2820_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, ElderKeyItem, ["EVENT_2820_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, AltoCardItem, ["EVENT_2820_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, EnduringBroochItem, ["EVENT_2820_run_dialog_16"]),
	JmpIfVarEqualsConst(ITEM_ID, ExtraShinyStoneItem, ["EVENT_2820_run_dialog_16"]),
	RunDialog(dialog_id=DI0066_GOT_A_70A7_AUTO_TERMINATE, above_object=BOWSER, closable=False, sync=True, multiline=False, use_background=False),
	AddToInventory(ITEM_ID),
	Return(),
	RunDialog(dialog_id=DI0064_GOT_AN_70A7_AUTO_TERMINATE, above_object=BOWSER, closable=False, sync=True, multiline=False, use_background=False, identifier="EVENT_2820_run_dialog_16"),
	AddToInventory(ITEM_ID),
	Return()
])
