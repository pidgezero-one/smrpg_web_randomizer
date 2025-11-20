
from smrpgpatchbuilder.datatypes.battle_animation_scripts import *
from ....variables.sprite_names import *
from ....variables.music_names import *
from ....variables.battle_sfx_names import *
from ....variables.battle_effect_names import *
from ....variables.battle_event_names import *
from ....variables.screen_effect_names import *
from ....spells.spells import *
from ....items.items import *
from ....enemies.enemies import *
from ....enemy_attacks.attacks import *

script = AnimationScriptBlock(expected_size=183, expected_beginning=0x3580B4, script=[
	SpriteSequence(sequence=0, looping_off=True, identifier="command_0x3580B4"),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=112, y=155, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1792, arch_height=96),
	PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
	ResetObjectMappingMemory(),
	ResetTargetMappingMemory(),
	ReturnSubroutine(),
	SpriteSequence(sequence=0, looping_off=True, identifier="command_0x3580CB"),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=96, y=163, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1792, arch_height=96),
	PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
	ResetObjectMappingMemory(),
	ResetTargetMappingMemory(),
	ReturnSubroutine(),
	SpriteSequence(sequence=0, looping_off=True, identifier="command_0x3580E2"),
	ResetTargetMappingMemory(),
	SetAMEM60ToCurrentTarget(),
	UnknownCommand(bytearray(b'Dh')),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1792, arch_height=96),
	PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
	ResetObjectMappingMemory(),
	ResetTargetMappingMemory(),
	ReturnSubroutine(),
	SpriteSequence(sequence=0, looping_off=True, identifier="command_0x3580F5"),
	ResetTargetMappingMemory(),
	SetAMEM60ToCurrentTarget(),
	SetAMEM40ToXYZCoords(origin=TARGET_CURRENT_POSITION, x=-52, y=26, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1792, arch_height=96),
	PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
	ResetObjectMappingMemory(),
	ResetTargetMappingMemory(),
	ReturnSubroutine(),
	SpriteSequence(sequence=0, looping_off=True, identifier="command_0x35810E"),
	ResetTargetMappingMemory(),
	SetAMEM60ToCurrentTarget(),
	SetAMEM40ToXYZCoords(origin=ABSOLUTE_POSITION, x=44, y=199, z=0, set_x=True, set_y=True, set_z=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1792, arch_height=96),
	PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
	ResetObjectMappingMemory(),
	ResetTargetMappingMemory(),
	ReturnSubroutine(),
	SpriteSequence(sequence=4, identifier="command_0x358127"),
	PauseScriptUntilSpriteSequenceDone(),
	ReturnSubroutine(),
	SetAMEMToRandomShort(amem=0x60, upper_bound=8, identifier="command_0x35812B"),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x358133"]),
	ReturnSubroutine(),
	DefineObjectQueue(["command_0x358143", "command_0x358148", "command_0x35814D", "command_0x358152", "command_0x358157", "command_0x35815C", "command_0x358161", "command_0x358166"], identifier="command_0x358133"),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=3, identifier="command_0x358143"),
	ReturnSubroutine(),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=6, identifier="command_0x358148"),
	ReturnSubroutine(),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=9, identifier="command_0x35814D"),
	ReturnSubroutine(),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=12, identifier="command_0x358152"),
	ReturnSubroutine(),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=15, identifier="command_0x358157"),
	ReturnSubroutine(),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=18, identifier="command_0x35815C"),
	ReturnSubroutine(),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=21, identifier="command_0x358161"),
	ReturnSubroutine(),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=24, identifier="command_0x358166"),
	ReturnSubroutine()
])
