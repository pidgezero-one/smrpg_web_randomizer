# E2365_EMPTY
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
	ActionQueueSync(target=NPC_0, subscript=[
		A_WalkWestPixels(12),
		A_ShiftZDownPixels(6),
		A_FaceSoutheast()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_WalkNorthSteps(8),
		A_ShadowOn()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_WalkNorthSteps(8),
		A_ShadowOn()
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_WalkNorthSteps(8),
		A_ShiftZUpPixels(16),
		A_ShadowOn()
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_WalkNorthSteps(8),
		A_WalkEastPixels(4),
		A_FaceSoutheast(),
		A_ShadowOn()
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_WalkNorthSteps(8),
		A_FaceSouthwest(),
		A_ShadowOn()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_WalkNorthSteps(8),
		A_FaceSouthwest(),
		A_ShadowOn()
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_WalkSouthPixels(10),
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_TransferToXYZF(x=5, y=53, z=4, direction=EAST)
	]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkToXYCoords(x=0, y=1)
	]),
	FreezeCamera(),
	SetSyncActionScript(NPC_1, A0763_EMPTY),
	SetSyncActionScript(NPC_2, A0763_EMPTY),
	SetSyncActionScript(NPC_3, A0763_EMPTY),
	SetSyncActionScript(NPC_4, A0763_EMPTY),
	SetSyncActionScript(NPC_5, A0763_EMPTY),
	SetSyncActionScript(NPC_6, A0763_EMPTY),
	FadeInFromBlack(sync=False),
	Pause(16),
	SetSyncActionScript(MARIO, A0764_EMPTY),
	Pause(24),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_UnknownCommand(bytearray(b' \x02')),
		A_EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x1d\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")),
		A_Pause(64),
		A_BPL262728()
	]),
	Pause(1, identifier="EVENT_2365_pause_22"),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_2365_set_action_script_25"]),
	Jmp(["EVENT_2365_pause_22"]),
	SetSyncActionScript(NPC_7, A0765_EMPTY, identifier="EVENT_2365_set_action_script_25"),
	ActionQueueSync(target=NPC_0, subscript=[
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\xc0\x06\x80\xff')),
		A_Pause(30),
		A_BPL262728()
	]),
	Pause(24),
	UnfreezeCamera(),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FASTEST),
		A_WalkNorthSteps(4)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetPriority(3),
		A_OverwriteSolidity(),
		A_ShadowOn(),
		A_SetSpriteSequence(index=4, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_FloatingOff(),
		A_UnknownCommand(bytearray(b' \x07')),
		A_UnknownCommand(bytearray(b'$P\x01\xb0\xfe')),
		A_UnknownCommand(bytearray(b'%\x00\x0c\xa0\xff')),
		A_Pause(255),
		A_BPL262728()
	]),
	Pause(18),
	FadeOutToBlack(sync=False, duration=30),
	JmpToEvent(E0142_EMPTY),
	Return()
])
