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
script = AnimationScriptBlock(expected_size=151, expected_beginning=0x3589D5, script=[
	ResetTargetMappingMemory(identifier="toadstool_weapon_wrapper"),
	ResetObjectMappingMemory(),
	SetAMEM60ToCurrentTarget(),
	UnknownCommand(bytearray([0x44, 0x55])),
	SpriteSequence(sequence=0, looping_off=True),
	MoveSpriteToCoords(shift_type=SHIFT_TYPE_TRANSFER, speed=1792, arch_height=96),
	PauseScriptUntil(condition=SPRITE_SHIFT_COMPLETE),
	ResetObjectMappingMemory(),
	SetAMEM8BitTo7E5x(0x60, 0x7E002E),
	ClearAMEM16Bit(0x61),
	ClearAMEM16Bit(0x63),
	ClearAMEM8Bit(0x65),
	SetAMEM8BitTo7E5x(0x6A, 0x7E002E),
	ClearAMEM8Bit(0x6B),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35ECA2"]),
	JmpIfTimedHitSuccess(destinations=["command_0x358A56"]),
	ClearAMEM16Bit(0x60),
	ClearAMEM8Bit(0x6F),
	UnknownCommand(bytearray([0xDB, 0x6B])),
	UnknownCommand(bytearray([0x81])),
	Pause1Frame(),
	Jmp(["command_0x358A10"]),
	ClearAMEM16Bit(0x60, identifier="command_0x358A08"),
	ClearAMEM8Bit(0x6F),
	UnknownCommand(bytearray([0xDB, 0x6F])),
	UnknownCommand(bytearray([0x82])),
	Pause1Frame(),
	AttackTimerBegins(identifier="command_0x358A10"),
	PauseScriptUntilAMEMBitsSet(0x6F, [0]),
	UnknownCommand(bytearray([0x3C, 0x00, 0x08])),
	SetAMEM8BitToConst(0x63, 1),
	SetAMEM8BitToConst(0x65, 1),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0008_TOADSTOOL_NONPROTAGONIST_2, sequence=0, store_to_vram=True, overlap_all_sprites=True, bit_4=True),
	RunSubroutine(["fix_sprite_after_attack"]),
    RunSubroutine(["command_0x358072"]),
	UnknownCommand(bytearray([0x6D])),
	ReturnSubroutine(),
	ResetTargetMappingMemory(identifier="command_0x358A37"),
	ResetObjectMappingMemory(),
	RunSubroutine(["ally_spell_common_subroutine_1"]),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0012_TOADSTOOL_NONPROTAGONIST_6, sequence=3, store_to_vram=True, overlap_all_sprites=True),
	PauseScriptUntilSpriteSequenceDone(),
	SetOMEM60To072C(),
	DecAMEM16BitByConst(0x60, 96),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35C761"]),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0008_TOADSTOOL_NONPROTAGONIST_2, sequence=0, store_to_vram=True, overlap_all_sprites=True, bit_4=True),
	RunSubroutine(["command_0x358072"]),
	UnknownCommand(bytearray([0x6D])),
	ReturnSubroutine(),
	PlaySound(sound=S0172_WEAPON_TIMING, channel=4, identifier="command_0x358A56"),
	SetAMEM8BitToConst(0x63, 1),
	SetAMEM8BitTo7E5x(0x60, 0x7E002E),
	ClearAMEM8Bit(0x61),
	SetAMEM8BitToConst(0x62, 1),
	UseObjectQueueAtOffsetWithAMEM60Index(destinations=["command_0x35ECA2"]),
	Jmp(["command_0x358A08"]),
	VisibilityOff(unknown_byte=0x01, identifier="command_0x350790"),
	UnknownCommand(bytearray([0x4F])),
	Jmp(["command_0x3505C9"]),
])
