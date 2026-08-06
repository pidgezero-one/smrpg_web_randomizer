# pyright: reportWildcardImportFromLibrary=false
from smrpgpatchbuilder.datatypes.battle_animation_scripts import *
from ....variables.sprite_names import *
from ....variables.music_names import *
from ....variables.battle_sfx_names import *
from ....variables.battle_effect_names import *
from ....variables.battle_event_names import *
from ....variables.screen_effect_names import *
from ....variables.battle_animation_variable_names import *
from ....variables.battle_variable_names import *
from ....spells.spells import *
from ....items.items import *
from ....enemies.enemies import *
from ....enemy_attacks.attacks import *
from smrpgpatchbuilder.datatypes.battle_animation_scripts.arguments.battle_targets import *
script = AnimationScriptBlock(expected_size=149, expected_beginning=0x358B57, script=[
	ResetTargetMappingMemory(identifier="geno_weapon_wrapper"),
	ResetObjectMappingMemory(),
	SetAMEM60ToCurrentTarget(),
    RunSubroutine(["geno_wrapper_parent_subroutine"]),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1792, arch_height=96),
	PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
	ResetObjectMappingMemory(),
	SetAMEM8BitToRAMRelative7E(0x60, 0x7E002E),
	ClearAMEM16Bit(0x61),
	ClearAMEM8Bit(0x63),
	ClearAMEM8Bit(0x66),
	SetAMEM8BitToRAMRelative7E(0x6A, 0x7E002E),
	ClearAMEM8Bit(0x6B),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35ECA2"]),
	JmpIfTimedHitSuccess(destinations=["command_0x358BD6"]),
	ClearAMEM8Bit(0x6F),
	PauseScriptUntilAMEMBitsSet(0x66, [0]),
	ClearAMEM16Bit(0x60),
	UnknownCommand(bytearray([0xDB, 0x6B])),
	UnknownCommand(bytearray([0x81])),
	Pause1Frame(),
	Jmp(["command_0x358B98"]),
	ClearAMEM8Bit(0x6F, identifier="command_0x358B8D"),
	PauseScriptUntilAMEMBitsSet(0x66, [0]),
	ClearAMEM16Bit(0x60),
	UnknownCommand(bytearray([0xDB, 0x6F])),
	UnknownCommand(bytearray([0x82])),
	Pause1Frame(),
	AttackTimerBegins(identifier="command_0x358B98"),
	PauseScriptUntilAMEMBitsSet(0x6F, [0]),
	UnknownCommand(bytearray([0x3C, 0x00, 0x08])),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0026_GENO_NONPROTAGONIST_2, sequence=0, store_to_vram=True, overlap_all_sprites=True, bit_4=True),
	RunSubroutine(["fix_sprite_after_attack"]),
    RunSubroutine(["command_0x358072"]),
	UnknownCommand(bytearray([0x6D])),
	ReturnSubroutine(),
	ResetTargetMappingMemory(identifier="command_0x358BAA"),
	ResetObjectMappingMemory(),
	SetOMEM60To072C(),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35C992"]),
	SpriteSequence(sequence=0, looping_off=True),
	RunSubroutine(["command_0x358072"]),
	UnknownCommand(bytearray([0x6D])),
	ReturnSubroutine(),
	ResetTargetMappingMemory(identifier="command_0x358BB7"),
	ResetObjectMappingMemory(),
	RunSubroutine(["ally_spell_common_subroutine_1"]),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0030_GENO_NONPROTAGONIST_6, sequence=1, store_to_vram=True, overlap_all_sprites=True),
	PauseScriptUntilSpriteSequenceDone(),
	SetOMEM60To072C(),
	DecAMEM16BitByConst(0x60, 96),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35C761"]),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0026_GENO_NONPROTAGONIST_2, sequence=0, store_to_vram=True, overlap_all_sprites=True, bit_4=True),
	RunSubroutine(["command_0x358072"]),
	UnknownCommand(bytearray([0x6D])),
	ReturnSubroutine(),	
	SetAMEM16BitToOMEMMain(amem=0x60, omem=0x64, identifier="command_0x35A076"),
	SetAMEM32ToXYZCoords(origin=TARGET_CURRENT_POSITION, x=-10, y=-3, z=0, set_x=True, set_y=True, set_z=True),
	RunSubroutine(["command_0x35A096"]),
	ReturnObjectQueue(),
])
