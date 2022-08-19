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
	Db(bytearray(b'\xfd\x12')),
	FloatingOff(),
	SetSpriteSequence(index=5, is_sequence=True),
	Pause(32),
	SetSequenceSpeed(speed=SLOW),
	Db(bytearray(b' \x07')),
	Db(bytearray(b'$`\x00\x10\x01')),
	Db(bytearray(b'%\x00\x08\x80\xff')),
	Pause(32),
	BPL262728(),
	SetSequenceSpeed(speed=NORMAL),
	SetSpriteSequence(index=0, is_sequence=True, mirror_sprite=True),
	Pause(96),
	SetSpriteSequence(index=5, is_sequence=True),
	SetSequenceSpeed(speed=SLOW),
	Db(bytearray(b' \x07')),
	Db(bytearray(b'$\xa0\xff\xf0\xfe')),
	Db(bytearray(b'%\xc0\x06\x80\xff')),
	Pause(32),
	BPL262728(),
	FaceSouthwest(),
	ResetProperties(),
	SetSequenceSpeed(speed=NORMAL),
	SequenceLoopingOn(),
	Pause(32),
	Set700CToPressedButton(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 20, ["ACTION_693_set_700C_to_object_coord_31"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 21, ["ACTION_693_set_700C_to_object_coord_38"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 22, ["ACTION_693_set_700C_to_object_coord_45"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 23, ["ACTION_693_set_700C_to_object_coord_52"]),
	Return(),
	Set700CToObjectCoord(object=NPC_0, coord=Z, pixel=True, bit_7=True, identifier="ACTION_693_set_700C_to_object_coord_31"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_693_clear_bit_35"]),
	WalkToXYCoords(x=7, y=115),
	FaceSouthwest(),
	ClearBit(TEMP_7043_0, identifier="ACTION_693_clear_bit_35"),
	TransferToXYZF(x=7, y=115, z=4, direction=EAST),
	Return(),
	Set700CToObjectCoord(object=NPC_1, coord=Z, pixel=True, bit_7=True, identifier="ACTION_693_set_700C_to_object_coord_38"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_693_clear_bit_42"]),
	WalkToXYCoords(x=8, y=107),
	FaceSouthwest(),
	ClearBit(TEMP_7043_1, identifier="ACTION_693_clear_bit_42"),
	TransferToXYZF(x=8, y=107, z=4, direction=EAST),
	Return(),
	Set700CToObjectCoord(object=NPC_2, coord=Z, pixel=True, bit_7=True, identifier="ACTION_693_set_700C_to_object_coord_45"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_693_clear_bit_49"]),
	WalkToXYCoords(x=12, y=107),
	FaceSouthwest(),
	ClearBit(TEMP_7043_2, identifier="ACTION_693_clear_bit_49"),
	TransferToXYZF(x=12, y=107, z=4, direction=EAST),
	Return(),
	Set700CToObjectCoord(object=NPC_3, coord=Z, pixel=True, bit_7=True, identifier="ACTION_693_set_700C_to_object_coord_52"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 8, ["ACTION_693_clear_bit_56"]),
	WalkToXYCoords(x=11, y=95),
	FaceSouthwest(),
	ClearBit(TEMP_7043_3, identifier="ACTION_693_clear_bit_56"),
	TransferToXYZF(x=11, y=95, z=8, direction=EAST),
	Return()
])
