# E0994_EMPTY
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
	EnterArea(room_id=R244_GAME_INTRO_YOSTER_ISLE_TALK_TO_YOSHI_RUN_AROUND, face_direction=SOUTHWEST, x=16, y=64, z=0),
	FadeInFromBlack(sync=True),
	SetBit(TEMP_7044_4),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Pause(10),
	ActionQueueAsync(target=NPC_12, subscript=[
		A_FaceSouthwest()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_JumpToHeight(height=110, silent=True),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetWalkingSpeed(SLOW),
		A_WalkSouthwestPixels(13),
		A_FloatingOff(),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_WalkSouthwestPixels(3),
		A_SetSpriteSequence(index=5, sprite_offset=6, is_sequence=True, looping=True),
		A_SetWalkingSpeed(FASTEST),
		A_DecZCoord1Step(),
		A_Pause(30)
	]),
	MoveScriptToMainThread(),
	UnknownCommand(bytearray(b'\xfdE')),
	PauseActionScript(NPC_12),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_SetSpriteSequence(index=2, sprite_offset=6, is_sequence=True, looping=True),
		A_WalkSouthSteps(2),
		A_SetSpriteSequence(index=5, sprite_offset=6, is_sequence=True, looping=True),
		A_WalkSouthwestSteps(9),
		A_SetSpriteSequence(index=5, sprite_offset=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkSoutheastSteps(5),
		A_SetSpriteSequence(index=6, sprite_offset=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_WalkNortheastSteps(12)
	]),
	ActionQueueSync(target=NPC_12, subscript=[
		A_FixedFCoordOff(),
		A_SetObjectMemoryBits(arg_1=0x0E, bits=[]),
		A_SetAllSpeeds(FAST),
		A_WalkSouthSteps(2),
		A_WalkSouthwestSteps(9),
		A_WalkSoutheastSteps(5),
		A_WalkNortheastSteps(12)
	]),
	Pause(190),
	FadeOutToBlack(sync=True, duration=30),
	PauseScriptUntilEffectDone(),
	JmpToEvent(E0139_EMPTY)
])
