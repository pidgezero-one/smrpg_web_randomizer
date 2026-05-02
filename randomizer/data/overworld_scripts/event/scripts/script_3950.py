# E3950_POST_FINAL_BOSS_INIT
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

PLAYER = MARIO
DEFAULT_PROTAGONIST_CHARACTER = NPC_0
DEFAULT_MARRYMORE_CHARACTER = NPC_1
DEFAULT_MWAY_CHARACTER = NPC_3
# Forest character defaults to the Geno-ending NPC slot at R088 object index 5
# (immediately after the doll at NPC_4 — anchors palette row 4 for the doll).
DEFAULT_FOREST_CHARACTER = NPC_5
# Bowser is moved to the last object slot (index 8) so the layout reads
# Mario/Peach/Sparkle/Mallow/Doll/Geno/Empty/GenoRedemption/Bowser.
DEFAULT_MINES_CHARACTER = NPC_8
DOLL = NPC_4


def build_contents(
	protagonist=DEFAULT_PROTAGONIST_CHARACTER,
	marrymore=DEFAULT_MARRYMORE_CHARACTER,
	mway=DEFAULT_MWAY_CHARACTER,
	forest=DEFAULT_FOREST_CHARACTER,
	mines=DEFAULT_MINES_CHARACTER,
):
	"""Build the contents list for E3950_POST_FINAL_BOSS_INIT.

	The forest character is removed before the fade-in: in R088 the cutscene
	doesn't feature a forest role visually (Geno is the doll), so whoever's
	been assigned to the forest role just needs to be cleared from the level.
	"""
	PROTAGONIST_CHARACTER = protagonist
	MARRYMORE_CHARACTER = marrymore
	MWAY_CHARACTER = mway
	FOREST_CHARACTER = forest
	MINES_CHARACTER = mines
	return [
		EnterArea(room_id=R088_SMITHYS_FINAL_FORM_DEFEAT_GENOS_REDEMPTION, face_direction=SOUTHWEST, x=4, y=51, z=0),
		FreezeCamera(),
		RemoveObjectFromCurrentLevel(PLAYER, identifier="hide_player_avatar2"),
		RemoveObjectFromCurrentLevel(FOREST_CHARACTER, identifier="hide_forest_character_3950"),
		ActionQueueSync(target=MWAY_CHARACTER, subscript=[
			A_TransferToXYZF(x=3, y=50, z=0, direction=EAST),
			A_TransferXYZFPixels(x=248, y=0, z=0, direction=EAST),
			A_FaceSoutheast()
		]),
		ActionQueueSync(target=MARRYMORE_CHARACTER, subscript=[
			A_TransferToXYZF(x=6, y=57, z=0, direction=EAST),
			A_TransferXYZFPixels(x=240, y=0, z=0, direction=EAST),
			A_SetSpriteSequence(index=23, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="ending_mmr_character_lean_far"),
			A_Pause(2),
			A_ResetProperties(),
			A_FaceNorthwest()
		], identifier="ending_mmr_character_lean_far_aq"),
		ActionQueueSync(target=MINES_CHARACTER, subscript=[
			A_TransferToXYZF(x=3, y=56, z=0, direction=SOUTHWEST),
			A_TransferXYZFPixels(x=240, y=0, z=0, direction=SOUTHWEST),
			A_FaceNortheast(),
			A_SetSpriteSequence(index=3, is_mold=True, looping=True, mirror_sprite=True),
		]),
		ActionQueueSync(target=DOLL, subscript=[
			A_TransferToXYZF(x=4, y=53, z=0, direction=EAST),
			A_TransferXYZFPixels(x=242, y=252, z=0, direction=EAST),
			A_SetSpriteSequence(index=6, is_sequence=True, looping=True, identifier="ending_doll_"),
		], identifier="ending_doll_aq_a"),
		ActionQueueAsync(target=PROTAGONIST_CHARACTER, subscript=[
			A_TransferToXYZF(x=6, y=50, z=0, direction=EAST),
			A_TransferXYZFPixels(x=240, y=254, z=0, direction=EAST),
			A_FaceSouthwest(),
		]),
		FadeInFromColour(duration=40, colour=WHITE),
		PauseScriptUntilEffectDone(),
		ActionQueueAsync(target=PROTAGONIST_CHARACTER, subscript=[
			A_SetWalkingSpeed(SLOW),
			A_SetSequenceSpeed(FAST),
			A_Walk1StepSouthwest(),
			A_WalkSouthwestPixels(12),
			A_SetSpriteSequence(index=12, sprite_offset=6, is_sequence=True, looping=True, identifier="ending_protag_look_at_doll")
		], identifier="ending_protag_look_at_doll_aq"),
		Pause(30),
		ActionQueueSync(target=MARRYMORE_CHARACTER, subscript=[
			A_SetWalkingSpeed(NORMAL),
			A_SetSequenceSpeed(FAST),
			A_Walk1StepNorthwest(),
			A_SetWalkingSpeed(SLOW),
			A_Walk1StepNorthwest(),
			A_WalkNorthwestPixels(8),
			A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, identifier="ending_marrymore_char_look_down_2")
		], identifier="ending_marrymore_char_look_down_2_aq"),
		ActionQueueSync(target=MWAY_CHARACTER, subscript=[
			A_Pause(16),
			A_SetWalkingSpeed(SLOW),
			A_SetSequenceSpeed(FAST),
			A_Walk1StepSoutheast(),
			A_WalkSoutheastPixels(8),
			A_SetSpriteSequence(index=14, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="ending_mway_character_look_down_2")
		], identifier="ending_mway_character_look_down_2_aq"),
		ActionQueueSync(target=MINES_CHARACTER, subscript=[
			A_Pause(16),
			A_SetWalkingSpeed(SLOW),
			A_SetSequenceSpeed(FAST),
			A_SetSpriteSequence(index=1, is_sequence=True, looping=True, mirror_sprite=True),
			A_Walk1StepNortheast(),
			A_WalkNortheastPixels(6),
			A_SetSpriteSequence(index=15, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="ending_mines_character_look_down_2")
		], identifier="ending_mines_character_look_down_2_aq"),
		RememberLastObject(),
		Pause(120),
		ActionQueueSync(target=NPC_7, subscript=[
			A_VisibilityOff(),
			A_TransferToXYZF(x=4, y=56, z=0, direction=EAST),
			A_TransferXYZFPixels(x=2, y=220, z=0, direction=EAST),
			A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
			A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
			A_VisibilityOn(),
			A_SequenceLoopingOn(),
			A_SetWalkingSpeed(VERY_FAST),
			A_StartLoopNTimes(1),
			A_Pause(60),
			A_ShiftZUpPixels(12),
			A_ShiftZDownPixels(12),
			A_EndLoop(),
			A_Pause(60),
			A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
			A_Pause(56),
			A_VisibilityOff(),
			A_SetPriority(0),
			A_TransferXYZFPixels(x=0, y=216, z=0, direction=EAST),
			A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
			A_VisibilityOn(),
			A_SetPriority(2),
			A_SetVRAMPriority(NORMAL_PRIORITY)
		]),
		ActionQueueSync(target=PROTAGONIST_CHARACTER, subscript=[
			A_Pause(90),
			A_ResetProperties(),
			A_Pause(150),
			A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True)
		]),
		ActionQueueSync(target=MWAY_CHARACTER, subscript=[
			A_Pause(120),
			A_ResetProperties(),
			A_Pause(90),
			A_SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="ending_mway_character_sees_geno"),
		], identifier="ending_mway_character_sees_geno_aq"),
		ActionQueueSync(target=MINES_CHARACTER, subscript=[
			A_Pause(90),
			A_ResetProperties(),
			A_Pause(120),
			A_SetSpriteSequence(index=24, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, identifier="ending_mines_character_lean_2_1"),
			A_Pause(2),
			A_SetSpriteSequence(index=25, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, identifier="ending_mines_character_lean_2_2")
		], identifier="ending_mines_character_lean_2_aq"),
		ActionQueueSync(target=MARRYMORE_CHARACTER, subscript=[
			A_Pause(90),
			A_ResetProperties(),
			A_Pause(120),
			A_SetSpriteSequence(index=22, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="ending_mmr_character_lean_far_2_partial"),
			A_Pause(2),
			A_SetSpriteSequence(index=23, sprite_offset=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="ending_mmr_character_lean_far_2_full")
		], identifier="ending_mmr_character_lean_2_aq"),
		RememberLastObject(),
		SetSyncActionScript(NPC_7, A0120_EMBEDDED_ROUTINE),
		Pause(90),
		PauseActionScript(NPC_7),
		StartAsyncEmbeddedActionScript(target=NPC_7, prefix=0xF1, subscript=[
			A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
			A_KillAllSubroutineSlots(),
			A_ToggleSubroutineSlots(mask=0x07),
			A_UnknownCommand(bytearray([0x25, 0x00, 0x07, 0x80, 0xFF])),
			A_SetSubroutineXTargets(slot_26_x=0xFF98, slot_27_x=0xFFC8),
			A_Pause(30),
			A_KillAllSubroutineSlots()
		]),
		SetSyncActionScript(NPC_7, A0120_EMBEDDED_ROUTINE),
		ActionQueueSync(target=MINES_CHARACTER, subscript=[
			A_SetSpriteSequence(index=18, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="ending_mines_character_looks_upward"),
		], identifier="ending_mines_character_looks_upward_aq"),
		ActionQueueSync(target=MARRYMORE_CHARACTER, subscript=[
			A_ResetProperties()
		]),
		ActionQueueSync(target=MWAY_CHARACTER, subscript=[
			A_SetSpriteSequence(index=9, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True, identifier="ending_mway_character_geno_joy"),
		], identifier="ending_mway_character_geno_joy_aq"),
		ActionQueueAsync(target=PROTAGONIST_CHARACTER, subscript=[
			A_SetSpriteSequence(index=8, is_mold=True, is_sequence=True, looping=True)
		]),
		Pause(60),
		PauseActionScript(NPC_7),
		StartAsyncEmbeddedActionScript(target=NPC_7, prefix=0xF1, subscript=[
			A_KillAllSubroutineSlots(),
			A_ToggleSubroutineSlots(mask=0x07),
			A_UnknownCommand(bytearray([0x25, 0x80, 0x06, 0xA0, 0xFF])),
			A_SetSubroutineXTargets(slot_26_x=0xFF90, slot_27_x=0x0100),
			A_Pause(30)
		]),
		SetSyncActionScript(NPC_7, A0120_EMBEDDED_ROUTINE),
		ActionQueueSync(target=MARRYMORE_CHARACTER, subscript=[
			A_SetSpriteSequence(index=19, is_mold=True, is_sequence=True, looping=True, identifier="ending_marrymore_char_look_left")
		], identifier="ending_marrymore_char_look_left_aq"),
		ActionQueueSync(target=PROTAGONIST_CHARACTER, subscript=[
			A_ResetProperties()
		]),
		ActionQueueAsync(target=MINES_CHARACTER, subscript=[
			A_SetSpriteSequence(index=12, sprite_offset=0, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True, identifier="ending_mines_character_raised_arms"),
		], identifier="ending_mines_character_raised_arms_aq"),
		Pause(60),
		PauseActionScript(NPC_7),
		StartAsyncEmbeddedActionScript(target=NPC_7, prefix=0xF1, subscript=[
			A_KillAllSubroutineSlots(),
			A_ToggleSubroutineSlots(mask=0x07),
			A_UnknownCommand(bytearray([0x25, 0xC0, 0x06, 0x88, 0xFF])),
			A_SetSubroutineXTargets(slot_26_x=0x0178, slot_27_x=0x0000),
			A_Pause(28)
		]),
		SetSyncActionScript(NPC_7, A0120_EMBEDDED_ROUTINE),
		ActionQueueSync(target=PROTAGONIST_CHARACTER, subscript=[
			A_SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True)
		]),
		ActionQueueAsync(target=MARRYMORE_CHARACTER, subscript=[
			A_SetSpriteSequence(index=5, sprite_offset=2, is_sequence=True, looping=True, identifier="ending_marrymore_char_joy_jump_1"),
			A_JumpToHeight(height=48, silent=True),
			A_Pause(1, identifier="EVENT_3950_action_queue_43_SUBSCRIPT_pause_2"),
			A_JmpIfObjectInAir(MARRYMORE_CHARACTER, ["EVENT_3950_action_queue_43_SUBSCRIPT_pause_2"]),
			A_SetSpriteSequence(index=2, sprite_offset=2, is_sequence=True, looping=True, identifier="ending_marrymore_char_joy_jump_2"),
		], identifier="ending_marrymore_char_joy_jump_aq"),
		Pause(60),
		PauseActionScript(NPC_7),
		StartAsyncEmbeddedActionScript(target=NPC_7, prefix=0xF1, subscript=[
			A_KillAllSubroutineSlots(),
			A_ToggleSubroutineSlots(mask=0x07),
			A_UnknownCommand(bytearray([0x25, 0x80, 0x06, 0x90, 0xFF])),
			A_SetSubroutineXTargets(slot_26_x=0x0020, slot_27_x=0xFF30),
			A_Pause(30)
		]),
		SetSyncActionScript(NPC_7, A0120_EMBEDDED_ROUTINE),
		ActionQueueAsync(target=PROTAGONIST_CHARACTER, subscript=[
			A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True)
		]),
		Pause(60),
		ActionQueueAsync(target=NPC_6, subscript=[
			A_TransferToXYZF(x=4, y=52, z=0, direction=EAST),
			A_TransferXYZFPixels(x=242, y=252, z=0, direction=EAST)
		]),
		SetSyncActionScript(NPC_6, A0228_ENDING_CUTSCENE_EFFECT),
		Pause(2),
		PauseActionScript(NPC_7),
		ActionQueueAsync(target=NPC_7, subscript=[
			A_KillAllSubroutineSlots(),
			A_SetObjectMemoryBits(arg_1=0x0E, bits=[0])
		]),
		Pause(230),
		ActionQueueSync(target=SCREEN_FOCUS, subscript=[
			A_SetWalkingSpeed(VERY_SLOW),
			A_WalkNorthSteps(3),
			A_WalkNorthPixels(8),
			A_Pause(2),
			A_SetWalkingSpeed(VERY_FAST),
			A_WalkNorthSteps(6)
		]),
		Pause(240),
		JmpToEvent(E3951_STAR_PIECE_CREDITS_INIT)
	]


script = EventScript(build_contents())
