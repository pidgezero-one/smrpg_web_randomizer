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
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 13, ["ACTION_63_sequence_looping_on_3"]),
	SetVRAMPriority(PRIORITY_3),
	SequenceLoopingOn(identifier="ACTION_63_sequence_looping_on_3"),
	SequencePlaybackOn(),
	ClearSolidityBits(cant_pass_walls=True),
	SetSpriteSequence(index=0, looping_off=True),
	JmpIfBitSet(TEMP_7042_7, ["ACTION_63_play_sound_13"]),
	Set700CToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 457, ["ACTION_63_play_sound_11"]),
	JmpIfVarEqualsConst(CURRENT_OVERWORLD_MARKER_ID, 4, ["ACTION_63_play_sound_17"]),
	PlaySound(sound=S060_DYNAMITE_BOMB_EXPLOSION, channel=4, identifier="ACTION_63_play_sound_11"),
	Jmp(["ACTION_63_shift_z_up_pixels_14"]),
	PlaySound(sound=S113_OPEN_CHAMBER_DOOR, channel=4, identifier="ACTION_63_play_sound_13"),
	ShiftZUpPixels(18, identifier="ACTION_63_shift_z_up_pixels_14"),
	VisibilityOff(),
	Return(),
	PlaySound(sound=S052_DEEP_BOUNCE, channel=4, identifier="ACTION_63_play_sound_17"),
	Jmp(["ACTION_63_shift_z_up_pixels_14"])
])
