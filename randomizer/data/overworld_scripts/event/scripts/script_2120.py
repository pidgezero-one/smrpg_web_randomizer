# E2120_EMPTY

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
	StopMusic(identifier="EVENT_2120_stop_music_0"),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSpriteSequence(index=0, is_mold=True, is_sequence=True, looping=True),
		A_Pause(20),
		A_SetSequenceSpeed(NORMAL),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True),
		A_Pause(45)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SequenceLoopingOn(),
		A_SequencePlaybackOn(),
		A_SetAllSpeeds(VERY_FAST),
		A_SetSpriteSequence(index=1, looping=True, mirror_sprite=True),
		A_WalkNorthwestSteps(9),
		A_WalkNorthwestSteps(2),
		A_VisibilityOff(),
		A_SequenceLoopingOff(),
		A_Pause(40)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Pause(60),
		A_SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	Pause(60),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	Pause(60),
	JmpIfBitSet(TEMP_7044_2, ["EVENT_2130_run_dialog_0"]),
	RunDialog(dialog_id=DI3348_EMPTY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	ClearBit(TEMP_7043_0),
	ClearBit(TEMP_7043_1),
	SetBit(TEMP_7044_2),
	Pause(30),
	Jmp(["EVENT_2131_pause_0"]),
	Return()
])
