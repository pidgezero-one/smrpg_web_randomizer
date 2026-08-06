# E0005_FREESTANDING_BIG_COIN_ROOM_AWARE
# Wrapper around E3146. Every room except 422 falls straight through to it unchanged.
#
# Room 422's prizes all share gridplane SPR0846, where sequence 2 is the ITEM BAG --
# E3146 sets sequence 2 for its rise-and-vanish collect, so a big coin turned into a
# bag mid-rise. Room 422 therefore gets a vanish-immediately collect with no sequence
# change at all (same shape as the frog coin's).
#
# The room test works because apply.py inserts Set7000ToCurrentLevel() at index 0 of
# every freestanding container (E0227-E0241), which are SHARED ACROSS 19 ROOMS -- so
# this MUST branch on the level rather than being swapped in wholesale.
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
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM, ["r422_big_coin"]),
	JmpToEvent(E3146_FREESTANDING_BIG_COIN),
	DisableObjectTrigger(MEM_70A8, identifier="r422_big_coin"),
	PlaySound(sound=SO013_COIN, channel=4),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
		A_VisibilityOff(),
		A_UnknownCommand(bytearray([0xFD, 0xF2]))
	]),
	AddCoins(10),
	Return()
])
