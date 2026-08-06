# E0703_BOOSTER_TOWER_ENTER_CURTAIN_ROOM
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
	JmpIfBitSet(POSTGAME_TOWER_COMPLETED, ["EVENT_703_enter_default_curtain_room"]),

    JmpIfBitClear(MARIO_DOLL_SHUFFLE_ENABLED, ["EVENT_703_jmp_if_bit_clear_26"]),
    JmpIfBitClear(RETURNED_MARIO_DOLL, ["EVENT_703_enter_default_curtain_room"]),


    
	JmpIfBitClear(TOWER_BOSS_1_STAR_PIECE, ["EVENT_703_enter_default_curtain_room"], identifier="EVENT_703_jmp_if_bit_clear_26"),
	JmpIfBitClear(STAY_VOUCHER_USED, ["EVENT_703_enter_default_curtain_room"]),
    
            
            
    EnterArea(room_id=R004_POSTGAME_TOWER, face_direction=SOUTHWEST, x=7,
            y=19,
            z=0, run_entrance_event=True, identifier="EVENT_703_enter_postgame_curtain_room"),
    Return(),


    EnterArea(room_id=R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, face_direction=SOUTHWEST, x=7,
            y=19,
            z=0, run_entrance_event=True, identifier="EVENT_703_enter_default_curtain_room"),
    Return(),
            
	
])
