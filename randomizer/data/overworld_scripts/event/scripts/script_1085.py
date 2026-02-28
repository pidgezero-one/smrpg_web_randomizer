# E1085_MELODY_BAY_JUMP_ANIMATION
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
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1085_pause_action_script_13"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1085_pause_action_script_16"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_1085_pause_action_script_19"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_1085_pause_action_script_22"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_1085_pause_action_script_25"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_1085_pause_action_script_28"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_1085_pause_action_script_31"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65535, ["EVENT_1085_pause_action_script_34"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65534, ["EVENT_1085_pause_action_script_37"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65533, ["EVENT_1085_pause_action_script_40"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65532, ["EVENT_1085_pause_action_script_43"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65531, ["EVENT_1085_pause_action_script_46"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 65530, ["EVENT_1085_pause_action_script_49"]),
	PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_13"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_JumpToHeight(height=64, silent=True),
		A_UnknownCommand(bytearray([0x20, 0x03])),
		A_UnknownCommand(bytearray([0x24, 0x00, 0x02, 0x00, 0xFF])),
		A_Pause(16),
		A_BPL262728()
	]),
	Return(),
	PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_16"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_JumpToHeight(height=64, silent=True),
		A_UnknownCommand(bytearray([0x20, 0x03])),
		A_UnknownCommand(bytearray([0x24, 0x00, 0x01, 0x80, 0xFE])),
		A_Pause(16),
		A_BPL262728()
	]),
	Return(),
	PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_19"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorth(),
		A_JumpToHeight(height=96, silent=True),
		A_UnknownCommand(bytearray([0x20, 0x03])),
		A_UnknownCommand(bytearray([0x24, 0x00, 0x00, 0xAB, 0xFE])),
		A_Pause(24),
		A_BPL262728()
	]),
	Return(),
	PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_22"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorth(),
		A_JumpToHeight(height=96, silent=True),
		A_UnknownCommand(bytearray([0x20, 0x03])),
		A_UnknownCommand(bytearray([0x24, 0x56, 0xFF, 0x56, 0xFE])),
		A_Pause(24),
		A_BPL262728()
	]),
	Return(),
	PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_25"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest(),
		A_JumpToHeight(height=96, silent=True),
		A_UnknownCommand(bytearray([0x20, 0x03])),
		A_UnknownCommand(bytearray([0x24, 0xAB, 0xFE, 0x00, 0xFE])),
		A_Pause(24),
		A_BPL262728()
	]),
	Return(),
	PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_28"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest(),
		A_JumpToHeight(height=128, silent=True),
		A_UnknownCommand(bytearray([0x20, 0x03])),
		A_UnknownCommand(bytearray([0x24, 0x80, 0xFE, 0x40, 0xFE])),
		A_Pause(32),
		A_BPL262728()
	]),
	Return(),
	PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_31"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest(),
		A_JumpToHeight(height=128, silent=True),
		A_UnknownCommand(bytearray([0x20, 0x03])),
		A_UnknownCommand(bytearray([0x24, 0x00, 0xFE, 0x00, 0xFE])),
		A_Pause(32),
		A_BPL262728()
	]),
	Return(),
	PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_34"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNortheast(),
		A_JumpToHeight(height=96, silent=True),
		A_UnknownCommand(bytearray([0x20, 0x03])),
		A_UnknownCommand(bytearray([0x24, 0x00, 0x02, 0xAB, 0xFF])),
		A_Pause(24),
		A_BPL262728()
	]),
	Return(),
	PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_37"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceEast(),
		A_JumpToHeight(height=96, silent=True),
		A_UnknownCommand(bytearray([0x20, 0x03])),
		A_UnknownCommand(bytearray([0x24, 0xAA, 0x02, 0x00, 0x00])),
		A_Pause(24),
		A_BPL262728()
	]),
	Return(),
	PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_40"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceEast(),
		A_JumpToHeight(height=96, silent=True),
		A_UnknownCommand(bytearray([0x20, 0x03])),
		A_UnknownCommand(bytearray([0x24, 0x55, 0x03, 0x55, 0x00])),
		A_Pause(24),
		A_BPL262728()
	]),
	Return(),
	PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_43"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSoutheast(),
		A_JumpToHeight(height=96, silent=True),
		A_UnknownCommand(bytearray([0x20, 0x03])),
		A_UnknownCommand(bytearray([0x24, 0x00, 0x04, 0xAA, 0x00])),
		A_Pause(24),
		A_BPL262728()
	]),
	Return(),
	PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_46"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSoutheast(),
		A_JumpToHeight(height=128, silent=True),
		A_UnknownCommand(bytearray([0x20, 0x03])),
		A_UnknownCommand(bytearray([0x24, 0x80, 0x03, 0xC0, 0x00])),
		A_Pause(32),
		A_BPL262728()
	]),
	Return(),
	PauseActionScript(MARIO, identifier="EVENT_1085_pause_action_script_49"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSoutheast(),
		A_JumpToHeight(height=128, silent=True),
		A_UnknownCommand(bytearray([0x20, 0x03])),
		A_UnknownCommand(bytearray([0x24, 0x00, 0x04, 0x00, 0x01])),
		A_Pause(32),
		A_BPL262728()
	]),
	Return()
])
