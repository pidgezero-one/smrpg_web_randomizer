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
	Set700CToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 395, ["ACTION_943_set_sprite_sequence_23"]),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 13, ["ACTION_943_set_sprite_sequence_4"]),
	SetVRAMPriority(PRIORITY_3),
	SetSpriteSequence(index=1, is_sequence=True, identifier="ACTION_943_set_sprite_sequence_4"),
	JmpIfRandom1of2(["ACTION_943_shift_xy_pixels_9"]),
	JmpIfRandom1of2(["ACTION_943_jmp_if_random_above_128_11"]),
	ShiftXYPixels(x=252, y=2),
	Jmp(["ACTION_943_pause_15"]),
	ShiftXYPixels(x=4, y=2, identifier="ACTION_943_shift_xy_pixels_9"),
	Jmp(["ACTION_943_pause_15"]),
	JmpIfRandom1of2(["ACTION_943_shift_xy_pixels_14"], identifier="ACTION_943_jmp_if_random_above_128_11"),
	ShiftXYPixels(x=4, y=254),
	Jmp(["ACTION_943_pause_15"]),
	ShiftXYPixels(x=252, y=254, identifier="ACTION_943_shift_xy_pixels_14"),
	Pause(6, identifier="ACTION_943_pause_15"),
	JmpIfBitSet(TEMP_7044_4, ["ACTION_943_visibility_off_21"]),
	CreatePacketAtNPCCoords(packet_id=P047_BLUE_FIRE_TRAIL, object=MARIO, destinations=["ACTION_943_pause_18"]),
	Pause(6, identifier="ACTION_943_pause_18"),
	JmpIfBitSet(TEMP_7044_4, ["ACTION_943_visibility_off_21"]),
	CreatePacketAtNPCCoords(packet_id=P047_BLUE_FIRE_TRAIL, object=MARIO, destinations=["ACTION_943_visibility_off_21"]),
	VisibilityOff(identifier="ACTION_943_visibility_off_21"),
	Return(),
	SetSpriteSequence(index=1, is_sequence=True, identifier="ACTION_943_set_sprite_sequence_23"),
	Inc(TEMP_70AE),
	JmpIfVarEqualsConst(TEMP_70AE, 1, ["ACTION_943_pause_28"]),
	JmpIfVarEqualsConst(TEMP_70AE, 2, ["ACTION_943_pause_36"]),
	JmpIfVarEqualsConst(TEMP_70AE, 3, ["ACTION_943_set_44"]),
	Pause(6, identifier="ACTION_943_pause_28"),
	JmpIfBitSet(TEMP_7043_0, ["ACTION_943_visibility_off_21"]),
	CreatePacketAtNPCCoords(packet_id=P047_BLUE_FIRE_TRAIL, object=NPC_2, destinations=["ACTION_943_pause_31"]),
	Pause(6, identifier="ACTION_943_pause_31"),
	JmpIfBitSet(TEMP_7043_0, ["ACTION_943_visibility_off_21"]),
	CreatePacketAtNPCCoords(packet_id=P047_BLUE_FIRE_TRAIL, object=NPC_2, destinations=["ACTION_943_visibility_off_34"]),
	VisibilityOff(identifier="ACTION_943_visibility_off_34"),
	Return(),
	Pause(6, identifier="ACTION_943_pause_36"),
	JmpIfBitSet(TEMP_7043_0, ["ACTION_943_visibility_off_21"]),
	CreatePacketAtNPCCoords(packet_id=P047_BLUE_FIRE_TRAIL, object=NPC_3, destinations=["ACTION_943_pause_39"]),
	Pause(6, identifier="ACTION_943_pause_39"),
	JmpIfBitSet(TEMP_7043_0, ["ACTION_943_visibility_off_21"]),
	CreatePacketAtNPCCoords(packet_id=P047_BLUE_FIRE_TRAIL, object=NPC_3, destinations=["ACTION_943_visibility_off_42"]),
	VisibilityOff(identifier="ACTION_943_visibility_off_42"),
	Return(),
	SetVarToConst(TEMP_70AE, 0, identifier="ACTION_943_set_44"),
	Pause(6),
	JmpIfBitSet(TEMP_7043_0, ["ACTION_943_visibility_off_21"]),
	CreatePacketAtNPCCoords(packet_id=P047_BLUE_FIRE_TRAIL, object=NPC_4, destinations=["ACTION_943_pause_48"]),
	Pause(6, identifier="ACTION_943_pause_48"),
	JmpIfBitSet(TEMP_7043_0, ["ACTION_943_visibility_off_21"]),
	CreatePacketAtNPCCoords(packet_id=P047_BLUE_FIRE_TRAIL, object=NPC_4, destinations=["ACTION_943_visibility_off_51"]),
	VisibilityOff(identifier="ACTION_943_visibility_off_51"),
	Return()
])
