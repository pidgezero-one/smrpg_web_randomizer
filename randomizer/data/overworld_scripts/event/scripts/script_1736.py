# E1736_EMPTY

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
	Inc(TEMP_7030),
	JmpIfVarNotEqualsConst(TEMP_7030, 4, ["EVENT_1736_pause_action_script_7"]),
	SetBit(EXP_STAR_BIT_6, identifier="EVENT_1736_set_bit_2"),
	Pause(3),
	CreatePacketAtObjectCoords(packet=P031_LEVELUP_TEXT, target_npc=MARIO, destinations=["EVENT_1736_set_bit_2"]),
	SetVarToConst(TIMER_7020, 64),
	RunBackgroundEventWithPauseReturnOnExit(event_id=E0254_EXP_STAR_HIT_SUBROUTINE, timer_var=TIMER_7020, bit_4=True, bit_5=True),
	PauseActionScript(MEM_70A8, identifier="EVENT_1736_pause_action_script_7"),
	ActionQueueSync(target=MEM_70A8, subscript=[
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_SetVRAMPriority(PRIORITY_3),
		A_SetPriority(3),
		A_OverwriteSolidity(),
		A_ObjectMemoryClearBit(arg_1=0x08, bits=[3, 4]),
		A_FloatingOff(),
		A_FixedFCoordOn(),
		A_UnknownCommand(bytearray(b' \x07')),
		A_EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x00\x00\x05\x00\x01\x00\x00\x00\x00\x00')),
		A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\x00\x00\x05\x00\x01\x00\x00\x00\x00\x00")),
		A_UnknownCommand(bytearray(b'\xfd$\x00\x07')),
		A_JmpIfRandom1of2(["EVENT_1736_action_queue_8_SUBSCRIPT_db_16"]),
		A_JmpIfRandom1of2(["EVENT_1736_action_queue_8_SUBSCRIPT_add_15"]),
		A_AddConstToVar(PRIMARY_TEMP_700C, 24),
		A_Jmp(["EVENT_1736_action_queue_8_SUBSCRIPT_db_16"]),
		A_AddConstToVar(PRIMARY_TEMP_700C, 232, identifier="EVENT_1736_action_queue_8_SUBSCRIPT_add_15"),
		A_UnknownCommand(bytearray(b'\xfd%'), identifier="EVENT_1736_action_queue_8_SUBSCRIPT_db_16"),
		A_UnknownCommand(bytearray(b'%\xa0\x08\x80\xff')),
		A_JmpIfBitClear(UNKNOWN_7076_1, ["EVENT_1736_action_queue_8_SUBSCRIPT_pause_20"]),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=False),
		A_Pause(88, identifier="EVENT_1736_action_queue_8_SUBSCRIPT_pause_20"),
		A_BPL262728(),
		A_VisibilityOff()
	]),
	Pause(1),
	Return()
])
