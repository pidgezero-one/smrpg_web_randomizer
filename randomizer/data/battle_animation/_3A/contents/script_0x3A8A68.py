# pyright: reportWildcardImportFromLibrary=false
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
from smrpgpatchbuilder.datatypes.battle_animation_scripts.arguments.battle_targets import *
script = AnimationScriptBlock(expected_size=89, expected_beginning=0x3A8A68, script=[
	ReturnObjectQueue(),  # LAZYSHELL break point
	DefineObjectQueue(["command_0x3A8A6A"], identifier="command_0x3A8A68"),
	SetAMEM32ToXYZCoords(origin=CASTER_CURRENT_POSITION, x=-16, y=-240, z=0, set_x=True, set_y=True, set_z=True, identifier="command_0x3A8A6A"),
	UnknownCommand(bytearray(b'\x83\x83')),
	RunSubroutine(["command_0x3A781B"]),
	RunSubroutine(["command_0x3A88D2"]),
	DefineObjectQueue(["command_0x3A8A7E", "command_0x3A8A9F"], identifier="command_0x3A8A7A"),
	SetAMEM32ToXYZCoords(origin=CASTER_CURRENT_POSITION, x=-8, y=-256, z=0, set_x=True, set_y=True, set_z=True, identifier="command_0x3A8A7E"),
	UnknownCommand(bytearray(b'\x83\x83')),
	MoveObject(speed=65, start_position=-513, end_position=768, apply_to_y=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	MoveObject(speed=17, start_position=0, end_position=-257, apply_to_x=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=20),
	RunSubroutine(["command_0x3A88D2"]),
	SetAMEM32ToXYZCoords(origin=CASTER_CURRENT_POSITION, x=8, y=-256, z=0, set_x=True, set_y=True, set_z=True, identifier="command_0x3A8A9F"),
	UnknownCommand(bytearray(b'\x83\x83')),
	MoveObject(speed=65, start_position=-513, end_position=768, apply_to_y=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	MoveObject(speed=17, start_position=0, end_position=256, apply_to_x=True, should_set_start_position=True, should_set_end_position=True, should_set_speed=True),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=20),
	RunSubroutine(["command_0x3A88D2"]),
])
