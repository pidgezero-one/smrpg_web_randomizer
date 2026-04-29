# E2563_REVEAL_BEAN_VALLEY_BEANSTALK
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
	FreezeCamera(identifier="EVENT_2563_freeze_camera_28"),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetVRAMPriority(NORMAL_PRIORITY)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetVRAMPriority(NORMAL_PRIORITY)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetPriority(3),
		A_WalkToXYCoords(x=26, y=30),
		A_FaceNortheast(),
		A_Pause(16),
		A_SetSpriteSequence(index=0, sprite_offset=6, is_sequence=True, looping=True),
		A_Pause(24),
		A_SetSpriteSequence(index=4, sprite_offset=1, is_sequence=True, looping=True, mirror_sprite=True),
		A_OverwriteSolidity(),
		A_FloatingOff(),
		A_PlaySound(sound=SO004_JUMP, channel=4),
		A_ShadowOn(),
		A_ToggleSubroutineSlots(mask=0x07),
		A_SetSubroutineXTargets(slot_26_x=0x0180, slot_27_x=0x0180),
		A_UnknownCommand(bytearray([0x25, 0x00, 0x0C, 0x80, 0xFF])),
		A_Pause(31),
		A_KillAllSubroutineSlots(),
		A_ShadowOn(),
		A_SetSpriteSequence(index=13, sprite_offset=6, is_mold=True, is_sequence=True, looping=True),
		A_Pause(24)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkNorthSteps(6)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=7, sprite_offset=6, is_sequence=True, looping=True),
		A_ToggleSubroutineSlots(mask=0x01),
		A_SetSubroutineXTargets(slot_26_x=0x0020, slot_27_x=0x0000),
		A_WalkNorthSteps(10),
		A_KillAllSubroutineSlots()
	]),
	FadeOutToBlack(sync=False),
	JmpToEvent(E3615_CLIMB_UP_VALLEY_BEANSTALK_INTO_VINE_CLOUDS),
	Return(identifier="EVENT_2563_ret_37")
])
