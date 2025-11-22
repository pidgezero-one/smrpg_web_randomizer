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
script = AnimationScriptBlock(expected_size=0x0202, expected_beginning=0x350000, script=[
	DefineObjectQueue(["ally_behaviour_pointers"], identifier="command_0x350000"),
	DefineObjectQueue(["command_0x350402", "command_0x350412", "command_0x350422", "command_0x350432", "command_0x350442", "command_0x350402"], identifier="ally_behaviour_pointers"),
	SetAMEM8BitTo7E5x(amem=0x60, address=0x7E0001, identifier="fix_sprite_after_attack"),
	JmpIfAMEM8BitEqualsConst(amem=0x60, value=0, destinations=["mario_sprite_reset"]),
	JmpIfAMEM8BitEqualsConst(amem=0x60, value=1, destinations=["toadstool_sprite_reset"]),
	JmpIfAMEM8BitEqualsConst(amem=0x60, value=2, destinations=["bowser_sprite_reset"]),
	JmpIfAMEM8BitEqualsConst(amem=0x60, value=3, destinations=["geno_sprite_reset"]),
	JmpIfAMEM8BitEqualsConst(amem=0x60, value=4, destinations=["mallow_sprite_reset"]),
    ReturnSubroutine(),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0002_MARIO_WALKING_UP_RIGHT, sequence=0, store_to_vram=True, overlap_all_sprites=True, bit_4=True, identifier="mario_sprite_reset"),
    ReturnSubroutine(),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0008_TOADSTOOL_WALKING_UP_RIGHT, sequence=0, store_to_vram=True, overlap_all_sprites=True, bit_4=True, identifier="toadstool_sprite_reset"),
    ReturnSubroutine(),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0014_BOWSER_WALKING_UP_RIGHT, sequence=0, store_to_vram=True, overlap_all_sprites=True, bit_4=True, identifier="bowser_sprite_reset"),
    ReturnSubroutine(),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0026_GENO_WALKING_UP_RIGHT, sequence=0, store_to_vram=True, overlap_all_sprites=True, bit_4=True, identifier="geno_sprite_reset"),
    ReturnSubroutine(),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0020_MALLOW_WALKING_UP_RIGHT, sequence=0, store_to_vram=True, overlap_all_sprites=True, bit_4=True, identifier="mallow_sprite_reset"),
    ReturnSubroutine(),
    SetAMEM8BitTo7E5x(amem=0x60, address=0x7E0001, identifier="group_hug_set_caster_sprite"),
    JmpIfAMEM8BitEqualsConst(amem=0x60, value=1, destinations=["peach_uses_group_hug"]),
    SpriteSequence(9, identifier="anyone_else_uses_group_hug"),
    ReturnSubroutine(),
    DrawSpriteAtAMEM32Coords(sprite_id=SPR0012_TOADSTOOL_FALLEN_CRYING, sequence=1, store_to_vram=True, overlap_all_sprites=True, identifier="peach_uses_group_hug"),
    ReturnSubroutine(),
    SetAMEM8BitTo7E5x(amem=0x60, address=0x7E0001, identifier="bowser_crush_cast"),
	JmpIfAMEM8BitEqualsConst(amem=0x60, value=0, destinations=["mario_bowser_crush_cast"]),
	JmpIfAMEM8BitEqualsConst(amem=0x60, value=1, destinations=["toadstool_bowser_crush_cast"]),
	JmpIfAMEM8BitEqualsConst(amem=0x60, value=2, destinations=["bowser_bowser_crush_cast"]),
	JmpIfAMEM8BitEqualsConst(amem=0x60, value=3, destinations=["geno_bowser_crush_cast"]),
	JmpIfAMEM8BitEqualsConst(amem=0x60, value=4, destinations=["mallow_bowser_crush_cast"]),
    ReturnSubroutine(),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0004_MARIO_ATTACK_UP_RIGHT, sequence=0, store_to_vram=True, overlap_all_sprites=True, identifier="mario_bowser_crush_cast"),
    ReturnSubroutine(),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0011_TOADSTOOL_FRYING_PAN_ATTACK, sequence=2, store_to_vram=True, overlap_all_sprites=True, identifier="toadstool_bowser_crush_cast"),
    ReturnSubroutine(),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0018_BOWSER_CAST_SPELL, sequence=0, store_to_vram=True, overlap_all_sprites=True, identifier="bowser_bowser_crush_cast"),
    ReturnSubroutine(),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0029_GENO_FINGER_SHOT, sequence=0, store_to_vram=True, overlap_all_sprites=True, identifier="geno_bowser_crush_cast"),
    ReturnSubroutine(),
	DrawSpriteAtAMEM32Coords(sprite_id=SPR0023_MALLOW_SWING_STICK, sequence=0, store_to_vram=True, overlap_all_sprites=True, identifier="mallow_bowser_crush_cast"),
    ReturnSubroutine(),
])
