# E2109_EMPTY

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
	JmpIfBitSet(UNKNOWN_TOWER_BOSS_2_FIGHT_7092_5, ["EVENT_2109_ret_38"]),
	JmpIfBitSet(UNKNOWN_TOWER_BOSS_2_FIGHT_7092_6, ["EVENT_2109_ret_38"]),
	FadeOutMusicToVolume(duration=0, volume=0),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(cant_pass_walls=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(30),
		A_ResetProperties(),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkToXYCoords(x=17, y=15),
		A_Pause(2),
		A_FaceSoutheast()
	]),
	Pause(40),
	Pause(10),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=8, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(30),
	Pause(80),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ResetProperties(),
		A_SequenceLoopingOff(),
		A_Pause(30),
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(SLOW),
		A_WalkSouthwestPixels(6),
		A_Pause(15)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=0, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True),
		A_JumpToHeight(48),
		A_Pause(30),
		A_ResetProperties(),
		A_FixedFCoordOff(),
		A_SetAllSpeeds(VERY_FAST),
		A_WalkNortheastSteps(1),
		A_WalkSoutheastSteps(7),
		A_SetSolidityBits(cant_pass_walls=True),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_VisibilityOff()
	]),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	StopSound(),
	EnterArea(room_id=R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM, face_direction=SOUTHEAST, x=2, y=56, z=0),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkToXYCoords(x=1, y=49),
		A_WalkNorthwestSteps(1),
		A_WalkEastPixels(13)
	]),
	PaletteSet(palette_set=111, row=1, bit_3=True),
	ActionQueueSync(target=NPC_0, subscript=[
		A_WalkSouthwestPixels(3),
		A_WalkNorthwestPixels(3),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_WalkSouthwestPixels(3),
		A_WalkNorthwestPixels(3),
		A_FaceNortheast()
	]),
	ActionQueueAsync(target=NPC_2, subscript=[
		A_WalkSouthwestPixels(3),
		A_WalkNorthwestPixels(3),
		A_FaceNortheast()
	]),
	FadeInFromBlack(sync=False),
	FreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_WalkSoutheastSteps(10),
		A_JumpToHeight(80),
		A_WalkSouthwestSteps(2),
		A_FaceNortheast(),
		A_SetAllSpeeds(NORMAL)
	]),
	Pause(60),
	Jmp(["EVENT_2114_fade_out_music_to_volume_0"]),
	Return(identifier="EVENT_2109_ret_38")
])
