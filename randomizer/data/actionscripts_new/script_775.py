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
	Set700CToPressedButton(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 20, ["ACTION_775_set_short_11"]),
	PlaySound(sound=S105_SURPRISE, channel=4),
	SetAllSpeeds(speed=VERY_FAST),
	SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True),
	JumpToHeight(height=112, silent=True, identifier="ACTION_775_jump_to_height_silent_5"),
	ShiftSouthwestPixels(1),
	ShiftWestPixels(4, identifier="ACTION_775_shift_west_pixels_7"),
	JmpIfMarioInAir(["ACTION_775_shift_west_pixels_7"]),
	PlaySound(sound=S084_SMOKED, channel=4),
	Jmp(["ACTION_775_jump_to_height_silent_5"]),
	SetVarToConst(TEMP_7034, 65535, identifier="ACTION_775_set_short_11"),
	Db(bytearray(b'\xc7\x00')),
	CreatePacketAtNPCCoords(packet_id=P032_BLUE_CLOUD, destinations=["ACTION_775_pause_14"]),
	Pause(6, identifier="ACTION_775_pause_14"),
	Jmp(["ACTION_775_set_short_11"])
])
