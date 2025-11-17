# E1565_EMPTY

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
	JmpIfBitSet(TEMP_7042_3, ["EVENT_1565_action_queue_14"]),
	ClearBit(FLOWER_TOWER_ASCENDED),
	ClearBit(SKY_BRIDGE_TUTORIAL_BIT),
	SummonObjectToSpecificLevel(NPC_5, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL),
	SummonObjectToSpecificLevel(NPC_6, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL),
	SummonObjectToSpecificLevel(NPC_7, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL),
	SummonObjectToSpecificLevel(NPC_8, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL),
	SummonObjectToSpecificLevel(NPC_9, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL),
	SummonObjectToSpecificLevel(NPC_10, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL),
	SummonObjectToSpecificLevel(NPC_11, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL),
	SummonObjectToSpecificLevel(NPC_12, R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL),
	CopyVarToVar(from_var=LAST_OVERWORLD_MARKER_ID, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 39, ["EVENT_1565_enter_area_28"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 45, ["EVENT_1565_enter_area_28"]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_WalkNortheastPixels(8)
	], identifier="EVENT_1565_action_queue_14"),
	ActionQueueSync(target=NPC_0, subscript=[
		A_WalkWestPixels(4)
	]),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_WalkNortheastPixels(8),
		A_ShiftZUpPixels(4)
	]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_4, R137_LANDS_END_AREA_01, ["EVENT_1565_jmp_if_bit_set_19"]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_VisibilityOff()
	]),
	JmpIfBitSet(TEMP_7044_7, ["EVENT_1565_run_event_as_subroutine_21"], identifier="EVENT_1565_jmp_if_bit_set_19"),
	RunEventAsSubroutine(E1844_SUMMON_CLOUD_BOSS),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_1565_run_event_as_subroutine_21"),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1565_clear_bit_26"]),
	JmpIfObjectTriggerDisabledInSpecificLevel(NPC_4, R137_LANDS_END_AREA_01, ["EVENT_1565_clear_bit_26"]),
	PlaySound(sound=SO149_CASINO_SECRET_PASSAGE, channel=6),
	ClearBit(SIGNAL_RING_BIT, identifier="EVENT_1565_clear_bit_26"),
	Return(),
	EnterArea(room_id=R407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS, face_direction=SOUTHWEST, x=26, y=103, z=22, identifier="EVENT_1565_enter_area_28"),
	SummonObjectToSpecificLevel(NPC_2, R319_LANDS_END_DESERT_AREA_06),
	SummonObjectToSpecificLevel(NPC_6, R402_LANDS_END_DESERT_AREA_03),
	SummonObjectToSpecificLevel(NPC_2, R403_LANDS_END_DESERT_AREA_05),
	SummonObjectToSpecificLevel(NPC_3, R404_LANDS_END_DESERT_AREA_04),
	SummonObjectToSpecificLevel(NPC_6, R318_LANDS_END_DESERT_AREA_02),
	SetBit(TEMP_7044_7),
	FadeInFromBlack(sync=False),
	Return()
])
