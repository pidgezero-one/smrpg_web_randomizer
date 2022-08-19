#classes
from randomizer.types.actionscripts.commands import *
from randomizer.types.actionscripts.classes import ActionScript
#ids
from randomizer.types.eventscripts.constants.script_ids import *
from randomizer.types.actionscripts.constants.script_ids import *
from randomizer.types.packets.constants.packet_ids import *
from randomizer.types.constants.sound_names import *
from randomizer.types.constants.directions import *
#types
from randomizer.types.constants.area_objects import *
from randomizer.types.constants.coords import *
from randomizer.types.actionscripts.constants.sequence_speeds import *
from randomizer.types.actionscripts.constants.vram_priority import *
from randomizer.types.variables.variables import *

script = ActionScript([
	SetPriority(3),
	Set700CToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 455, ["ACTION_653_set_700C_to_pressed_button_6"]),
	Set700CToPressedButton(),
	CompareVarToConst(PRIMARY_TEMP_700C, 30),
	JmpIfComparisonResultIsGreaterOrEqual(["ACTION_653_set_vram_priority_11"]),
	Set700CToPressedButton(identifier="ACTION_653_set_700C_to_pressed_button_6"),
	AddConstToVar(PRIMARY_TEMP_700C, 65534),
	CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=ACTIVE_NPC),
	Db(bytearray(b'\x97\x10')),
	Jmp(["ACTION_653_set_700C_to_pressed_button_6"]),
	SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES, identifier="ACTION_653_set_vram_priority_11"),
	Set700CToPressedButton(identifier="ACTION_653_set_700C_to_pressed_button_12"),
	AddConstToVar(PRIMARY_TEMP_700C, 65534),
	CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=ACTIVE_NPC),
	TransferToObjectXY(MEM_70A8),
	Jmp(["ACTION_653_set_700C_to_pressed_button_12"])
])
