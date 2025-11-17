# E2124_CHOOSE_MARRYMORE_SANCTUARY_STATE

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
	JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_2124_enter_area_3"], identifier="EVENT_2124_jmp_if_bit_set_0"),
	JmpIfBitSet(CHAPEL_ITEM_RETRIEVAL_STARTED, ["EVENT_2124_enter_area_5"]),
	JmpToEvent(E3809_MARRYMORE_SANCTUARY_BEGIN_WEDDING_GEAR_SEQUENCE),
	EnterArea(room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, face_direction=NORTHEAST, x=9, y=98, z=0, run_entrance_event=True, identifier="EVENT_2124_enter_area_3"),
	Return(),
	EnterArea(room_id=R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER, face_direction=NORTHEAST, x=9, y=98, z=0, run_entrance_event=True, identifier="EVENT_2124_enter_area_5"),
	Return()
])
