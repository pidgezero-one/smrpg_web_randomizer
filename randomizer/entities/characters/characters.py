"""Playable character classes."""

from typing import List, Type, Union
from randomizer.entities.progress_locations.characters_recruited import (
    StartingCharacter1,
)
from randomizer.entities.spells.spells import (
    BowserCrush,
    ComeBack,
    Crusher,
    FireOrb,
    GenoBeam,
    GenoBlast,
    GenoBoost,
    GenoFlash,
    GenoWhirl,
    GroupHug,
    HPRain,
    Jump,
    Mute,
    PoisonGas,
    PsychBomb,
    Psychopath,
    Shocker,
    SleepyTime,
    Snowy,
    StarRain,
    SuperFlame,
    SuperJump,
    Terrorize,
    Therapy,
    Thunderbolt,
    UltraFlame,
    UltraJump,
)
from randomizer.types.palettes.classes import (
    BowserPaletteSet,
    GenoPaletteSet,
    MallowPaletteSet,
    MarioPaletteSet,
    ToadstoolPaletteSet,
)
from randomizer.types.items.classes import SpottedCharacter
from randomizer.types.spells.classes import CharacterSpell
from randomizer.types.numbers.classes import UInt16, UInt8
from randomizer.types.characters.classes import Character, StatGrowth
from randomizer.entities.characters.palettes.bowser import (
    Default as DefaultBowserPalette,
)
from randomizer.entities.characters.palettes.geno import Default as DefaultGenoPalette
from randomizer.entities.characters.palettes.mario import Default as DefaultMarioPalette
from randomizer.entities.characters.palettes.mallow import (
    Default as DefaultMallowPalette,
)
from randomizer.entities.characters.palettes.toadstool import (
    Default as DefaultToadstoolPalette,
)

from randomizer.types.npcs.objects.classes import NPC
from randomizer.types.npcs.objects.npcs import (
    BowserDoll,
    GenoDoll,
    MallowDoll,
    MarioDoll,
    Mario as MarioNPC,
    Mallow as MallowNPC,
    Geno as GenoNPC,
    Bowser as BowserNPC,
    Toadstool as ToadstoolNPC,
    ToadstoolDoll,
)
from randomizer.types.world.flags.enums import PlayableCharacters


from randomizer.types.world.flags.flags import PlayAsStarter


class MarioSpotted(SpottedCharacter):
    """Placeholder instance representing the event of seeing Mario in the overworld
    (without recruiting him)."""

    _item_id: int = 225


class ToadstoolSpotted(SpottedCharacter):
    """Placeholder instance representing the event of seeing Toadstool in the overworld
    (without recruiting her)."""

    _item_id: int = 226


class MallowSpotted(SpottedCharacter):
    """Placeholder instance representing the event of seeing Mallow in the overworld
    (without recruiting him)."""

    _item_id: int = 227


class GenoSpotted(SpottedCharacter):
    """Placeholder instance representing the event of seeing Geno in the overworld
    (without recruiting him)."""

    _item_id: int = 228


class BowserSpotted(SpottedCharacter):
    """Placeholder instance representing the event of seeing Bowser in the overworld
    (without recruiting him)."""

    _item_id: int = 229


# ******************* Actual character data classes.
class Mario(Character):
    """Playable character instance of Mario."""

    _original_name: str = PlayableCharacters.MARIO
    _character_id: int = 0
    _starting_level: int = 1
    _max_hp: UInt16 = UInt16(20)
    _speed: UInt8 = UInt8(20)
    _attack: UInt8 = UInt8(20)
    _defense: UInt8 = UInt8(0)
    _magic_attack: UInt8 = UInt8(10)
    _magic_defense: UInt8 = UInt8(2)
    _learned_spells: "dict[int, Type[CharacterSpell]]" = {
        1: Jump,
        3: FireOrb,
        6: SuperJump,
        10: SuperFlame,
        14: UltraJump,
        18: UltraFlame,
    }
    _palette: MarioPaletteSet = DefaultMarioPalette()

    @property
    def palette(self) -> "MarioPaletteSet":
        return self._palette

    # Vanilla levelup stat growths
    # (hp, attack, defense, m.attack, m.defense)
    _starting_growths: List[StatGrowth] = [
        StatGrowth(5, 3, 2, 2, 2),
        StatGrowth(5, 3, 2, 2, 2),
        StatGrowth(5, 3, 3, 2, 2),
        StatGrowth(5, 3, 3, 2, 2),
        StatGrowth(5, 4, 3, 3, 2),
        StatGrowth(6, 4, 3, 3, 2),
        StatGrowth(6, 4, 3, 3, 2),
        StatGrowth(7, 4, 3, 3, 2),
        StatGrowth(7, 4, 3, 3, 2),
        StatGrowth(7, 5, 4, 3, 3),
        StatGrowth(8, 5, 4, 4, 3),
        StatGrowth(8, 5, 4, 4, 3),
        StatGrowth(8, 5, 4, 4, 3),
        StatGrowth(9, 5, 4, 4, 3),
        StatGrowth(9, 6, 4, 4, 3),
        StatGrowth(9, 6, 4, 4, 3),
        StatGrowth(10, 6, 4, 4, 3),
        StatGrowth(10, 6, 4, 5, 3),
        StatGrowth(10, 6, 4, 5, 3),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
    ]

    # Vanilla levelup stat bonus options
    # (hp, attack, defense, m.attack, m.defense)
    _levelup_bonuses: List[StatGrowth] = [
        StatGrowth(3, 1, 1, 3, 1),
        StatGrowth(3, 2, 1, 1, 1),
        StatGrowth(4, 1, 1, 1, 1),
        StatGrowth(3, 1, 1, 3, 1),
        StatGrowth(3, 2, 1, 1, 1),
        StatGrowth(4, 1, 1, 1, 1),
        StatGrowth(3, 1, 1, 3, 1),
        StatGrowth(3, 2, 1, 1, 1),
        StatGrowth(4, 1, 1, 1, 1),
        StatGrowth(3, 1, 1, 3, 1),
        StatGrowth(3, 2, 1, 1, 1),
        StatGrowth(4, 1, 1, 1, 1),
        StatGrowth(3, 1, 1, 3, 1),
        StatGrowth(3, 2, 1, 1, 1),
        StatGrowth(4, 1, 1, 1, 1),
        StatGrowth(3, 1, 1, 3, 1),
        StatGrowth(3, 2, 1, 1, 1),
        StatGrowth(4, 1, 1, 1, 1),
        StatGrowth(3, 1, 1, 3, 1),
        StatGrowth(1, 2, 1, 1, 1),
        StatGrowth(2, 1, 1, 1, 1),
        StatGrowth(1, 1, 1, 3, 1),
        StatGrowth(1, 2, 1, 1, 1),
        StatGrowth(2, 1, 1, 1, 1),
        StatGrowth(1, 1, 1, 3, 1),
        StatGrowth(1, 2, 1, 1, 1),
        StatGrowth(2, 1, 1, 1, 1),
        StatGrowth(1, 1, 1, 3, 1),
        StatGrowth(1, 2, 1, 1, 1),
    ]

    _ending_palettes: List[int] = [0x37A9D8, 0x37B31A]

    _original_weapon_sprite_ids: List[Union[int, None]] = [0, 1, 2, 3, 4, 5, 6]
    _sprite_ids_as_main_character: List[int] = [0, 1, 2, 3, 4, 5, 6]
    _sprite_addresses: List[Union[list[int], None]] = [
        [],
        [],
        [0x35F119, 0x35FF13, 0x35CD9F],
        [],
        [
            0x35ECF9,
            0x35ECF0,
            0x35EDC4,
            0x35EDDF,
            0x35EDD4,
            0x35EEF9,
            0x35EFAC,
            0x35EFB5,
            0x35F0D2,
            0x358CE7,
            0x358D79,
            0x358E0B,
            0x35FF6D,
            0x35ECF0,
            0x35ECF9,
        ],
        [
            0x35ED8C,
            0x35ED7D,
            0x35EE58,
            0x35EE49,
            0x35EE99,
            0x35EE8A,
            0x35F032,
            0x35F023,
            0x35F10B,
        ],
        [],
    ]  # not building an assembler for this in this version

    _battle_sprite_offset: int = 0x020225
    _battle_sprite_id: int = 0x02
    _menu_sprite_offset: int = 0x0318A3
    _menu_sprite_id: int = 0x02
    _abxy_coord_offset: int = 0x023685
    _abxy_coord: int = 0xBF
    _cursor_coord_offset: int = 0x029752
    _cursor_coord: int = 0x13
    _portrait_sprite_offset: int = 0x24123
    _portrait_id: int = 0x28
    _item_use_offset: int = 0x3589A5
    _item_use_bytes: bytearray = bytearray([0x03, 0x81, 0x00, 0x06, 0x00, 0x01])
    _runaway_offset: int = 0x350547
    _runaway_bytes: bytearray = bytearray([0x03, 0x81, 0x08, 0x00, 0x00, 0x00])

    _item_id: int = 220
    _description: str = PlayableCharacters.MARIO.value
    _placeholder: str = "`MARIO_NAME`"
    _starter_script: int = 187
    _container_script: int = 193
    _model: Type[NPC] = MarioNPC
    _doll: Type[NPC] = MarioDoll
    _sprites_primary: "dict[str, tuple[int, int, bool]]" = {
        "south": (0, 12, True),
        "defend": (2, 16, True),
        "face_north": (0, 1, False),
        "face_south": (0, 0, False),
        "shocked_loop": (3, 8, False),
        "shocked_loop_backwards": (3, 9, False),
        "shocked_backwards_sequence": (2, 3, False),
        "shocked_shadow": (3, 0, False),
        "shocked_shadow_backwards": (2, 8, True),
        "crying": (3, 3, False),
        "crying_backwards": (3, 4, False),
        "looking_down_static": (0, 6, True),
        "looking_down": (0, 6, False),
        "looking_down_away": (0, 7, False),
        "floored": (3, 1, True),
        "hurt": (0, 6, True),
        "shaking_head": (0, 8, False),
        "shaking_head_backward": (0, 9, False),
        "sleeping": (2, 6, False),
        "salute": (2, 9, False),
        "joy": (2, 9, False),
        "joy_behind": (3, 2, False),
        "joy_jump": (3, 2, False),
        "distracted": (0, 10, True),
        "displeased": (3, 4, False),
        "challenge": (4, 2, False),
        "look_to_side": (0, 8, True),
        "look_to_down": (0, 9, True),
        "look_to_side_behind": (0, 11, True),
        "cast_frame_1": (2, 12, True),
        "cast_frame_2": (2, 13, True),
        "cast_frame_3": (2, 14, True),
        "cast_frame_4": (2, 15, True),
        "look_up_slightly": (2, 23, True),
        "look_way_up": (2, 24, True),
        "victory_pose": (2, 10, True),
        "prince_neutral": (0, 0, True),
        "prince_down": (0, 9, True),
        "prince_left": (0, 8, True),
        "hammer": (2, 3, True),
        "hammer_static": (2, 3, True),
    }
    _sprites_secondary: "dict[str, tuple[int, int, bool]]" = {
        "south": (0, 20, True),
        "defend": (1, 16, True),
        "face_north": (0, 1, False),
        "face_south": (0, 0, False),
        "shocked_loop": (2, 8, False),
        "shocked_loop_backwards": (2, 9, False),
        "shocked_backwards_sequence": (1, 3, False),
        "shocked_shadow": (2, 0, False),
        "shocked_shadow_backwards": (1, 8, True),
        "crying": (0, 4, False),
        "crying_backwards": (0, 5, False),
        "looking_down_static": (0, 14, True),
        "looking_down": (0, 6, False),
        "looking_down_away": (0, 7, False),
        "floored": (2, 1, True),
        "hurt": (0, 14, True),
        "shaking_head": (0, 8, False),
        "shaking_head_backward": (0, 9, False),
        "sleeping": (1, 6, False),
        "salute": (1, 9, False),
        "joy": (1, 9, False),
        "joy_behind": (2, 2, False),
        "joy_jump": (2, 2, False),
        "distracted": (0, 18, True),
        "displeased": (0, 5, False),
        "challenge": (3, 2, False),
        "look_to_side": (0, 16, True),
        "look_to_down": (0, 17, True),
        "look_to_side_behind": (0, 19, True),
        "cast_frame_1": (1, 12, True),
        "cast_frame_2": (1, 13, True),
        "cast_frame_3": (1, 14, True),
        "cast_frame_4": (1, 15, True),
        "look_up_slightly": (1, 23, True),
        "look_way_up": (1, 24, True),
        "victory_pose": (1, 10, True),
        "prince_neutral": (0, 0, True),
        "prince_down": (0, 17, True),
        "prince_left": (0, 16, True),
        "hammer": (1, 3, True),
        "hammer_static": (1, 3, True),
    }

    _associated_spotted_class: Type[SpottedCharacter] = MarioSpotted

    def get_patch(self):
        patch = super().get_patch()

        starting_char = self.world.get_location_instance(StartingCharacter1).contents
        is_main_character = isinstance(
            starting_char, type(self)
        ) and self.world.settings.is_boolean_flag_enabled(PlayAsStarter)
        if is_main_character:  # don't remember what this does
            patch.add_data(0x37B0A6, bytearray([0x5F, 0x19, 0xD8, 0x1C, 0x35]))

        return patch


class Toadstool(Character):
    """Playable character instance of Toadstool."""

    _original_name: str = PlayableCharacters.TOADSTOOL
    _character_id: int = 1
    _placeholder: str = "`PEACH_NAME`"
    _starting_level: int = 9
    _max_hp: UInt16 = UInt16(15)
    _speed: UInt8 = UInt8(24)
    _attack: UInt8 = UInt8(15)
    _defense: UInt8 = UInt8(0)
    _magic_attack: UInt8 = UInt8(14)
    _magic_defense: UInt8 = UInt8(14)
    _learned_spells: "dict[int, Type[CharacterSpell]]" = {
        3: Therapy,
        7: GroupHug,
        11: SleepyTime,
        13: ComeBack,
        15: Mute,
        18: PsychBomb,
    }
    _palette: ToadstoolPaletteSet = DefaultToadstoolPalette()

    @property
    def palette(self) -> "ToadstoolPaletteSet":
        return self._palette

    # Vanilla levelup stat growths
    # (hp, attack, defense, m.attack, m.defense)
    _starting_growths: List[StatGrowth] = [
        StatGrowth(2, 2, 2, 1, 1),
        StatGrowth(2, 2, 2, 1, 1),
        StatGrowth(2, 2, 2, 2, 1),
        StatGrowth(2, 2, 3, 2, 1),
        StatGrowth(2, 2, 3, 2, 1),
        StatGrowth(2, 2, 3, 3, 2),
        StatGrowth(2, 2, 3, 3, 2),
        StatGrowth(3, 2, 3, 3, 2),
        # Vanilla growths
        StatGrowth(4, 1, 3, 4, 2),
        StatGrowth(5, 2, 3, 4, 3),
        StatGrowth(6, 3, 3, 4, 3),
        StatGrowth(7, 4, 3, 4, 3),
        StatGrowth(8, 5, 3, 4, 3),
        StatGrowth(9, 6, 3, 4, 3),
        StatGrowth(10, 7, 3, 4, 4),
        StatGrowth(11, 8, 4, 4, 4),
        StatGrowth(12, 9, 4, 4, 4),
        StatGrowth(13, 10, 4, 4, 4),
        StatGrowth(14, 10, 4, 4, 4),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
    ]

    # Vanilla levelup stat bonus options
    # (hp, attack, defense, m.attack, m.defense)
    _levelup_bonuses: List[StatGrowth] = [
        StatGrowth(5, 1, 1, 3, 1),
        StatGrowth(5, 3, 1, 1, 1),
        StatGrowth(9, 1, 1, 1, 1),
        StatGrowth(5, 1, 1, 3, 1),
        StatGrowth(5, 3, 1, 1, 1),
        StatGrowth(9, 1, 1, 1, 1),
        StatGrowth(5, 1, 1, 3, 1),
        StatGrowth(5, 3, 1, 1, 1),
        StatGrowth(9, 1, 1, 1, 1),
        StatGrowth(5, 1, 1, 3, 1),
        StatGrowth(5, 3, 1, 1, 1),
        StatGrowth(9, 1, 1, 1, 1),
        StatGrowth(5, 1, 1, 3, 1),
        StatGrowth(5, 3, 1, 1, 1),
        StatGrowth(9, 1, 1, 1, 1),
        StatGrowth(5, 1, 1, 3, 1),
        StatGrowth(5, 3, 1, 1, 1),
        StatGrowth(9, 1, 1, 1, 1),
        StatGrowth(5, 1, 1, 3, 1),
        StatGrowth(3, 3, 1, 1, 1),
        StatGrowth(2, 1, 1, 1, 1),
        StatGrowth(1, 1, 1, 3, 1),
        StatGrowth(1, 3, 1, 1, 1),
        StatGrowth(2, 1, 1, 1, 1),
        StatGrowth(1, 1, 1, 3, 1),
        StatGrowth(1, 3, 1, 1, 1),
        StatGrowth(2, 1, 1, 1, 1),
        StatGrowth(1, 1, 1, 3, 1),
        StatGrowth(1, 3, 1, 1, 1),
    ]
    _ending_palettes: List[int] = [0x37B086, 0x37B338]

    _original_weapon_sprite_ids: List[Union[int, None]] = [7, None, 8, 9, 10, 11, 12]
    _sprite_ids_as_main_character: List[int] = [0, 1, 2, 3, 4, 5, 634]
    _sprite_addresses: List[Union[list[int], None]] = [
        [],
        None,
        [0x35FF1A, 0x35A9FD, 0x35CDA8],
        [],
        [
            0x35ED1A,
            0x35ED0B,
            0x35EEE5,
            0x35EED6,
            0x35EFDE,
            0x35EFCD,
            0x35F049,
            0x35F058,
            0x35FF74,
        ],
        [0x35EF1D, 0x35EF0E, 0x35F0F6, 0x35F0E7],
        [0x35A9A0],
    ]  # not building an assembler for this in this version

    _battle_sprite_offset: int = 0x020226
    _battle_sprite_id: int = 0x08
    _menu_sprite_offset: int = 0x0318A4
    _menu_sprite_id: int = 0x08
    _abxy_coord_offset: int = 0x023687
    _abxy_coord: int = 0xBE
    _cursor_coord_offset: int = 0x029753
    _cursor_coord: int = 0x13
    _portrait_sprite_offset: int = 0x24124
    _portrait_id: int = 0x29
    _item_use_offset: int = 0x358A3C
    _item_use_bytes: bytearray = bytearray([0x03, 0x81, 0x00, 0x0C, 0x00, 0x03])
    _runaway_offset: int = 0x35054E
    _runaway_bytes: bytearray = bytearray([0x03, 0x81, 0x08, 0x07, 0x00, 0x00])

    _item_id: int = 221
    _description: str = PlayableCharacters.TOADSTOOL.value
    _placeholder: str = "`PEACH_NAME`"
    _gender: str = "woman"
    _gender_casual: str = "gal"
    _honorific: str = "ma'am"
    _title: str = "miss"
    _title_short: str = "Ms"
    _mole_greeting: str = "mate"
    _mboy_greeting: str = ""
    _starter_script: int = 191
    _container_script: int = 197
    _doll: Type[NPC] = ToadstoolDoll
    _model: Type[NPC] = ToadstoolNPC
    _sprites_primary: "dict[str, tuple[int, int, bool]]" = {
        "south": (0, 12, True),
        "defend": (2, 15, True),
        "face_north": (0, 1, False),
        "face_south": (0, 0, False),
        "shocked_loop": (3, 8, False),
        "shocked_loop_backwards": (3, 9, False),
        "shocked_backwards_sequence": (2, 3, False),
        "shocked_shadow": (3, 0, False),
        "shocked_shadow_backwards": (2, 8, True),
        "crying": (3, 3, False),
        "crying_backwards": (3, 4, False),
        "looking_down_static": (0, 6, True),
        "looking_down": (0, 6, False),
        "looking_down_away": (0, 7, False),
        "floored": (3, 1, True),
        "hurt": (0, 6, True),
        "shaking_head": (0, 8, False),
        "shaking_head_backward": (0, 9, False),
        "sleeping": (2, 6, False),
        "salute": (2, 9, False),
        "joy": (2, 9, False),
        "joy_jump": (3, 2, False),
        "joy_behind": (3, 2, False),
        "distracted": (0, 18, True),
        "displeased": (0, 5, False),
        "challenge": (4, 5, False),
        "look_to_side": (0, 8, True),
        "look_to_down": (0, 9, True),
        "look_to_side_behind": (0, 11, True),
        "cast_frame_1": (2, 10, True),
        "cast_frame_2": (2, 11, True),
        "cast_frame_3": (2, 12, True),
        "cast_frame_4": (2, 14, True),
        "look_up_slightly": (2, 22, True),
        "look_way_up": (2, 23, True),
        "victory_pose": (2, 10, True),
        "prince_neutral": (0, 0, True),
        "prince_down": (0, 9, True),
        "prince_left": (0, 8, True),
        "hammer": (2, 3, True),
        "hammer_static": (2, 3, True),
    }
    _sprites_secondary: "dict[str, tuple[int, int, bool]]" = {
        "south": (0, 20, True),
        "defend": (1, 15, True),
        "face_north": (0, 1, False),
        "face_south": (0, 0, False),
        "shocked_loop": (2, 3, False),
        "shocked_loop_backwards": (2, 4, False),
        "shocked_backwards_sequence": (1, 3, False),
        "shocked_shadow": (2, 0, False),
        "shocked_shadow_backwards": (1, 8, True),
        "crying": (0, 13, False),
        "crying_backwards": (0, 14, False),
        "looking_down_static": (0, 14, True),
        "looking_down": (0, 6, False),
        "looking_down_away": (0, 7, False),
        "floored": (2, 1, True),
        "hurt": (5, 0, True),
        "shaking_head": (0, 8, False),
        "shaking_head_backward": (0, 9, False),
        "sleeping": (1, 6, False),
        "salute": (1, 9, False),
        "joy": (1, 9, False),
        "joy_behind": (2, 2, False),
        "joy_jump": (2, 5, False),
        "distracted": (0, 18, True),
        "displeased": (0, 5, False),
        "challenge": (3, 5, False),
        "look_to_side": (0, 16, True),
        "look_to_down": (0, 17, True),
        "look_to_side_behind": (0, 19, True),
        "cast_frame_1": (1, 10, True),
        "cast_frame_2": (1, 11, True),
        "cast_frame_3": (1, 12, True),
        "cast_frame_4": (1, 14, True),
        "look_up_slightly": (1, 22, True),
        "look_way_up": (1, 23, True),
        "victory_pose": (1, 10, True),
        "prince_neutral": (0, 0, True),
        "prince_down": (0, 17, True),
        "prince_left": (0, 16, True),
        "hammer": (1, 3, True),
        "hammer_static": (1, 3, True),
    }

    _associated_spotted_class: Type[SpottedCharacter] = ToadstoolSpotted
    # print([hex(i) for i in palette_to_bytes(["EFAD31", "DE9421", "B57B21", "946318", "6B5218", "6B5218", "212110", "DE9421", "946318", "4A3910", "DE9421", "9C6B18", "523910", "101008", "181818"])])

    def get_patch(self):
        patch = super().get_patch()

        starting_char = self.world.get_location_instance(StartingCharacter1).contents
        is_main_character = isinstance(
            starting_char, type(self)
        ) and self.world.settings.is_boolean_flag_enabled(PlayAsStarter)
        if is_main_character:  # don't remember what this does
            patch.add_data(0x35FF43, bytearray([0x03, 0x81, 0x00, 0x05, 0x00, 0x04]))
            # patch.add_data(0x35FF98, 0x00)
            patch.add_data(0x35FF9D, bytearray([0x03, 0x81, 0x10, 0x02, 0x00, 0x01]))

        return patch


class Bowser(Character):
    """Playable character instance of Bowser."""

    _original_name: str = PlayableCharacters.BOWSER
    _character_id: int = 2
    _starting_level: int = 8
    _max_hp: UInt16 = UInt16(25)
    _speed: UInt8 = UInt8(15)
    _attack: UInt8 = UInt8(39)
    _defense: UInt8 = UInt8(15)
    _magic_attack: UInt8 = UInt8(1)
    _magic_defense: UInt8 = UInt8(6)
    _learned_spells: "dict[int, Type[CharacterSpell]]" = {
        8: Terrorize,
        12: PoisonGas,
        15: Crusher,
        18: BowserCrush,
    }
    _palette: BowserPaletteSet = DefaultBowserPalette()

    @property
    def palette(self) -> "BowserPaletteSet":
        return self._palette

    # Vanilla levelup stat growths
    # (hp, attack, defense, m.attack, m.defense)
    _starting_growths: List[StatGrowth] = [
        StatGrowth(6, 6, 5, 1, 3),
        StatGrowth(6, 6, 5, 1, 3),
        StatGrowth(7, 6, 5, 1, 3),
        StatGrowth(7, 6, 5, 1, 3),
        StatGrowth(7, 6, 5, 2, 3),
        StatGrowth(8, 6, 5, 2, 3),
        StatGrowth(8, 6, 5, 2, 3),
        # Vanilla growths
        StatGrowth(8, 3, 3, 4, 2),
        StatGrowth(8, 3, 3, 4, 2),
        StatGrowth(8, 4, 3, 4, 2),
        StatGrowth(8, 4, 3, 4, 2),
        StatGrowth(8, 4, 3, 4, 2),
        StatGrowth(8, 4, 3, 4, 2),
        StatGrowth(8, 4, 3, 4, 2),
        StatGrowth(8, 5, 4, 4, 2),
        StatGrowth(8, 5, 4, 4, 2),
        StatGrowth(9, 5, 4, 4, 2),
        StatGrowth(9, 6, 4, 4, 2),
        StatGrowth(9, 6, 4, 4, 2),
        StatGrowth(4, 2, 2, 2, 2),
        StatGrowth(4, 2, 2, 2, 2),
        StatGrowth(4, 2, 2, 2, 2),
        StatGrowth(4, 2, 2, 2, 2),
        StatGrowth(4, 2, 2, 2, 2),
        StatGrowth(4, 2, 2, 2, 2),
        StatGrowth(4, 2, 2, 2, 2),
        StatGrowth(4, 2, 2, 2, 2),
        StatGrowth(4, 2, 2, 2, 2),
        StatGrowth(4, 2, 2, 2, 2),
    ]

    # Vanilla levelup stat bonus options
    # (hp, attack, defense, m.attack, m.defense)
    _levelup_bonuses: List[StatGrowth] = [
        StatGrowth(1, 1, 1, 3, 1),
        StatGrowth(1, 2, 1, 1, 1),
        StatGrowth(3, 1, 1, 1, 1),
        StatGrowth(1, 1, 1, 3, 1),
        StatGrowth(1, 2, 1, 1, 1),
        StatGrowth(3, 1, 1, 1, 1),
        StatGrowth(1, 1, 1, 3, 1),
        StatGrowth(1, 2, 1, 1, 1),
        StatGrowth(3, 1, 1, 1, 1),
        StatGrowth(1, 1, 1, 3, 1),
        StatGrowth(1, 2, 1, 1, 1),
        StatGrowth(3, 1, 1, 1, 1),
        StatGrowth(1, 1, 1, 3, 1),
        StatGrowth(1, 2, 1, 1, 1),
        StatGrowth(3, 1, 1, 1, 1),
        StatGrowth(1, 1, 1, 3, 1),
        StatGrowth(1, 2, 1, 1, 1),
        StatGrowth(3, 1, 1, 1, 1),
        StatGrowth(1, 1, 1, 3, 1),
        StatGrowth(1, 2, 1, 1, 1),
        StatGrowth(3, 1, 1, 1, 1),
        StatGrowth(1, 1, 1, 3, 1),
        StatGrowth(1, 2, 1, 1, 1),
        StatGrowth(3, 1, 1, 1, 1),
        StatGrowth(1, 1, 1, 3, 1),
        StatGrowth(1, 2, 1, 1, 1),
        StatGrowth(3, 1, 1, 1, 1),
        StatGrowth(1, 1, 1, 3, 1),
        StatGrowth(1, 2, 1, 1, 1),
    ]

    _ending_palettes: List[int] = [0x37B068, 0x37B356]

    _original_weapon_sprite_ids: List[Union[int, None]] = [
        13,
        None,
        14,
        15,
        16,
        17,
        18,
    ]
    _sprite_ids_as_main_character: List[int] = [0, 1, 2, 3, 4, 5, 634]
    _sprite_addresses: List[Union[list[int], None]] = [
        [],
        None,
        [0x35FF21, 0x35CDB1],
        [],
        [0x35ED2A, 0x35ED35, 0x35F074, 0x35F069, 0x35FF7B],
        [0x35EE2B, 0x35EE6C, 0x35EF31, 0x35EF95],
        [],
    ]  # not building an assembler for this in this version

    _battle_sprite_offset: int = 0x020227
    _battle_sprite_id: int = 0x0E
    _menu_sprite_offset: int = 0x0318A5
    _menu_sprite_id: int = 0x0E
    _abxy_coord_offset: int = 0x023689
    _abxy_coord: int = 0xBA
    _cursor_coord_offset: int = 0x029754
    _cursor_coord: int = 0x24
    _portrait_sprite_offset: int = 0x24125
    _portrait_id: int = 0x2A
    _item_use_offset: int = 0x358B27
    _item_use_bytes: bytearray = bytearray([0x03, 0x81, 0x00, 0x12, 0x00, 0x01])
    _runaway_offset: int = 0x350555
    _runaway_bytes: bytearray = bytearray([0x03, 0x81, 0x08, 0x0D, 0x00, 0x00])

    _item_id: int = 224
    _model: Type[NPC] = BowserNPC
    _description: str = PlayableCharacters.BOWSER.value
    _placeholder: str = "`BOWSER_NAME`"
    _starter_script: int = 190
    _container_script: int = 196
    _doll: Type[NPC] = BowserDoll
    _sprites_primary: "dict[str, tuple[int, int, bool]]" = {
        "south": (0, 12, True),
        "defend": (2, 17, True),
        "face_north": (0, 1, False),
        "face_south": (0, 0, False),
        "shocked_loop": (3, 8, False),
        "shocked_loop_backwards": (3, 9, False),
        "shocked_backwards_sequence": (2, 3, False),
        "shocked_shadow": (3, 0, False),
        "shocked_shadow_backwards": (2, 8, True),
        "crying": (3, 3, False),
        "crying_backwards": (3, 4, False),
        "looking_down_static": (0, 6, True),
        "looking_down": (0, 6, False),
        "looking_down_away": (0, 7, False),
        "floored": (3, 1, True),
        "hurt": (0, 6, True),
        "shaking_head": (0, 8, False),
        "shaking_head_backward": (0, 9, False),
        "sleeping": (2, 6, False),
        "salute": (2, 9, False),
        "joy": (2, 9, False),
        "joy_behind": (3, 2, False),
        "joy_jump": (3, 2, False),
        "distracted": (0, 10, True),
        "displeased": (3, 4, False),
        "challenge": (4, 4, False),
        "look_to_side": (0, 8, True),
        "look_to_down": (0, 9, True),
        "look_to_side_behind": (0, 11, True),
        "cast_frame_1": (2, 10, True),
        "cast_frame_2": (2, 11, True),
        "cast_frame_3": (2, 12, True),
        "cast_frame_4": (2, 13, True),
        "look_up_slightly": (2, 24, True),
        "look_way_up": (2, 25, True),
        "victory_pose": (2, 10, True),
        "prince_neutral": (0, 0, True),
        "prince_down": (0, 9, True),
        "prince_left": (0, 8, True),
        "hammer": (2, 3, True),
        "hammer_static": (2, 3, True),
    }
    _sprites_secondary: "dict[str, tuple[int, int, bool]]" = {
        "south": (0, 20, True),
        "defend": (1, 17, True),
        "face_north": (0, 1, False),
        "face_south": (0, 0, False),
        "shocked_loop": (2, 8, False),
        "shocked_loop_backwards": (2, 9, False),
        "shocked_backwards_sequence": (1, 3, False),
        "shocked_shadow": (2, 0, False),
        "shocked_shadow_backwards": (1, 8, True),
        "crying": (0, 13, False),
        "crying_backwards": (0, 14, False),
        "looking_down_static": (0, 14, True),
        "looking_down": (0, 6, False),
        "looking_down_away": (0, 7, False),
        "floored": (2, 1, True),
        "hurt": (0, 6, False),
        "shaking_head": (0, 8, False),
        "shaking_head_backward": (0, 9, False),
        "sleeping": (1, 6, False),
        "salute": (1, 9, False),
        "joy": (1, 9, False),
        "joy_behind": (2, 2, False),
        "joy_jump": (2, 2, False),
        "distracted": (0, 18, True),
        "displeased": (0, 5, False),
        "challenge": (3, 4, False),
        "look_to_side": (0, 16, True),
        "look_to_down": (0, 17, True),
        "look_to_side_behind": (0, 19, True),
        "cast_frame_1": (1, 10, True),
        "cast_frame_2": (1, 11, True),
        "cast_frame_3": (1, 12, True),
        "cast_frame_4": (1, 13, True),
        "look_up_slightly": (1, 24, True),
        "look_way_up": (1, 25, True),
        "victory_pose": (1, 10, True),
        "prince_neutral": (0, 0, True),
        "prince_down": (0, 17, True),
        "prince_left": (0, 16, True),
        "hammer": (2, 4, False),
        "hammer_static": (2, 13, True),
    }

    _associated_spotted_class: Type[SpottedCharacter] = BowserSpotted


class Geno(Character):
    """Playable character instance of Geno."""

    _original_name: str = PlayableCharacters.GENO
    _character_id: int = 3
    _starting_level: int = 6
    _max_hp: UInt16 = UInt16(20)
    _speed: UInt8 = UInt8(30)
    _attack: UInt8 = UInt8(24)
    _defense: UInt8 = UInt8(6)
    _magic_attack: UInt8 = UInt8(3)
    _magic_defense: UInt8 = UInt8(5)
    _learned_spells: "dict[int, Type[CharacterSpell]]" = {
        6: GenoBeam,
        8: GenoBoost,
        11: GenoWhirl,
        14: GenoBlast,
        17: GenoFlash,
    }
    _palette: GenoPaletteSet = DefaultGenoPalette()

    @property
    def palette(self) -> "GenoPaletteSet":
        return self._palette

    # Vanilla levelup stat growths
    # (hp, attack, defense, m.attack, m.defense)
    _starting_growths: List[StatGrowth] = [
        StatGrowth(3, 6, 3, 3, 2),
        StatGrowth(4, 6, 3, 3, 2),
        StatGrowth(4, 6, 3, 3, 2),
        StatGrowth(4, 6, 3, 3, 2),
        StatGrowth(4, 6, 3, 4, 2),
        # Vanilla growths
        StatGrowth(8, 5, 3, 4, 2),
        StatGrowth(8, 5, 3, 4, 2),
        StatGrowth(8, 5, 3, 4, 2),
        StatGrowth(8, 5, 3, 4, 2),
        StatGrowth(8, 5, 4, 4, 3),
        StatGrowth(8, 5, 4, 4, 3),
        StatGrowth(8, 5, 4, 4, 3),
        StatGrowth(8, 5, 4, 4, 3),
        StatGrowth(8, 5, 4, 4, 3),
        StatGrowth(8, 5, 4, 5, 3),
        StatGrowth(8, 5, 4, 5, 3),
        StatGrowth(8, 6, 4, 5, 3),
        StatGrowth(8, 6, 4, 5, 3),
        StatGrowth(8, 6, 4, 5, 3),
        StatGrowth(1, 2, 3, 2, 2),
        StatGrowth(1, 2, 3, 2, 2),
        StatGrowth(1, 2, 3, 2, 2),
        StatGrowth(1, 2, 3, 2, 2),
        StatGrowth(1, 2, 3, 2, 2),
        StatGrowth(1, 2, 3, 2, 2),
        StatGrowth(1, 2, 3, 2, 2),
        StatGrowth(1, 2, 3, 2, 2),
        StatGrowth(1, 2, 3, 2, 2),
        StatGrowth(1, 2, 3, 2, 2),
    ]

    # Vanilla levelup stat bonus options
    # (hp, attack, defense, m.attack, m.defense)
    _levelup_bonuses: List[StatGrowth] = [
        StatGrowth(5, 1, 1, 3, 1),
        StatGrowth(5, 3, 1, 1, 1),
        StatGrowth(6, 1, 1, 1, 1),
        StatGrowth(5, 1, 1, 3, 1),
        StatGrowth(5, 3, 1, 1, 1),
        StatGrowth(6, 1, 1, 1, 1),
        StatGrowth(5, 1, 1, 3, 1),
        StatGrowth(5, 3, 1, 1, 1),
        StatGrowth(6, 1, 1, 1, 1),
        StatGrowth(5, 1, 1, 3, 1),
        StatGrowth(5, 3, 1, 1, 1),
        StatGrowth(6, 1, 1, 1, 1),
        StatGrowth(5, 1, 1, 3, 1),
        StatGrowth(5, 3, 1, 1, 1),
        StatGrowth(6, 1, 1, 1, 1),
        StatGrowth(5, 1, 1, 3, 1),
        StatGrowth(5, 3, 1, 1, 1),
        StatGrowth(6, 1, 1, 1, 1),
        StatGrowth(5, 1, 1, 3, 1),
        StatGrowth(1, 3, 1, 1, 1),
        StatGrowth(2, 1, 1, 1, 1),
        StatGrowth(1, 1, 1, 3, 1),
        StatGrowth(1, 3, 1, 1, 1),
        StatGrowth(2, 1, 1, 1, 1),
        StatGrowth(1, 1, 1, 3, 1),
        StatGrowth(1, 3, 1, 1, 1),
        StatGrowth(2, 1, 1, 1, 1),
        StatGrowth(1, 1, 1, 3, 1),
        StatGrowth(1, 3, 1, 1, 1),
    ]

    _ending_palettes: List[int] = [0x37AA14, 0x37B392]

    _original_weapon_sprite_ids: List[Union[int, None]] = [
        25,
        None,
        26,
        27,
        28,
        29,
        30,
    ]
    _sprite_ids_as_main_character: List[int] = [0, 1, 2, 3, 4, 5, 634]
    _sprite_addresses: List[Union[list[int], None]] = [
        [],
        None,
        [0x35FF28, 0x35BC59, 0x35CDBA],
        [],
        [0x35F93C, 0x35ED4F, 0x35F976, 0x35EF58],
        [0x35FF82, 0x35EDF3, 0x35EEAD, 0x35EFF5, 0x35F09A, 0x35B4F5, 0x35BAAD],
        [0x35BC4A, 0x35911C],
    ]  # not building an assembler for this in this version

    _battle_sprite_offset: int = 0x020228
    _battle_sprite_id: int = 0x1A
    _menu_sprite_offset: int = 0x0318A6
    _menu_sprite_id: int = 0x1A
    _abxy_coord_offset: int = 0x02368B
    _abxy_coord: int = 0xC0
    _cursor_coord_offset: int = 0x029755
    _cursor_coord: int = 0x13
    _portrait_sprite_offset: int = 0x24126
    _portrait_id: int = 0x2C
    _item_use_offset: int = 0x358BBC
    _item_use_bytes: bytearray = bytearray([0x03, 0x81, 0x00, 0x1E, 0x00, 0x01])
    _runaway_offset: int = 0x35055C
    _runaway_bytes: bytearray = bytearray([0x03, 0x81, 0x08, 0x19, 0x00, 0x00])

    _item_id: int = 223
    _description: str = PlayableCharacters.GENO.value
    _placeholder: str = "`GENO_NAME`"
    _starter_script: int = 189
    _container_script: int = 195
    _doll: Type[NPC] = GenoDoll
    _model: Type[NPC] = GenoNPC
    _sprites_primary: "dict[str, tuple[int, int, bool]]" = {
        "south": (0, 12, True),
        "defend": (2, 16, True),
        "face_north": (0, 1, False),
        "face_south": (0, 0, False),
        "shocked_loop": (3, 8, False),
        "shocked_loop_backwards": (3, 9, False),
        "shocked_backwards_sequence": (2, 3, False),
        "shocked_shadow": (3, 0, False),
        "shocked_shadow_backwards": (2, 8, True),
        "crying": (3, 3, False),
        "crying_backwards": (3, 4, False),
        "looking_down_static": (0, 6, True),
        "looking_down": (0, 6, False),
        "looking_down_away": (0, 7, False),
        "floored": (3, 1, True),
        "hurt": (0, 6, True),
        "shaking_head": (0, 8, False),
        "shaking_head_backward": (0, 9, False),
        "sleeping": (2, 6, False),
        "salute": (2, 9, False),
        "joy": (2, 9, False),
        "joy_behind": (3, 2, False),
        "joy_jump": (3, 2, False),
        "distracted": (0, 10, True),
        "displeased": (3, 4, False),
        "challenge": (4, 0, False),
        "look_to_side": (0, 8, True),
        "look_to_down": (0, 9, True),
        "look_to_side_behind": (0, 11, True),
        "cast_frame_1": (2, 12, True),
        "cast_frame_2": (2, 13, True),
        "cast_frame_3": (2, 14, True),
        "cast_frame_4": (2, 15, True),
        "look_up_slightly": (2, 23, True),
        "look_way_up": (2, 24, True),
        "victory_pose": (2, 10, True),
        "prince_neutral": (0, 0, True),
        "prince_down": (0, 9, True),
        "prince_left": (0, 8, True),
        "hammer": (2, 3, True),
        "hammer_static": (2, 3, True),
    }
    _sprites_secondary: "dict[str, tuple[int, int, bool]]" = {
        "south": (0, 20, True),
        "defend": (1, 16, True),
        "face_north": (0, 1, False),
        "face_south": (0, 0, False),
        "shocked_loop": (2, 8, False),
        "shocked_loop_backwards": (2, 9, False),
        "shocked_backwards_sequence": (1, 3, False),
        "shocked_shadow": (2, 0, False),
        "shocked_shadow_backwards": (1, 8, True),
        "crying": (0, 11, False),
        "crying_backwards": (0, 12, False),
        "looking_down_static": (0, 14, True),
        "looking_down": (0, 6, False),
        "looking_down_away": (0, 7, False),
        "floored": (2, 1, True),
        "hurt": (0, 22, True),
        "shaking_head": (0, 8, False),
        "shaking_head_backward": (0, 9, False),
        "sleeping": (1, 6, False),
        "salute": (1, 9, False),
        "joy": (1, 9, False),
        "joy_behind": (2, 2, False),
        "joy_jump": (2, 2, False),
        "distracted": (0, 19, True),
        "displeased": (0, 5, False),
        "challenge": (3, 0, False),
        "look_to_side": (0, 16, True),
        "look_to_down": (0, 17, True),
        "look_to_side_behind": (0, 19, True),
        "cast_frame_1": (1, 12, True),
        "cast_frame_2": (1, 13, True),
        "cast_frame_3": (1, 14, True),
        "cast_frame_4": (1, 15, True),
        "look_up_slightly": (1, 23, True),
        "look_way_up": (1, 24, True),
        "victory_pose": (1, 10, True),
        "prince_neutral": (0, 0, True),
        "prince_down": (0, 17, True),
        "prince_left": (0, 16, True),
        "hammer": (1, 3, True),
        "hammer_static": (1, 3, True),
    }

    _associated_spotted_class: Type[SpottedCharacter] = GenoSpotted


class Mallow(Character):
    """Playable character instance of Mallow."""

    _original_name: str = PlayableCharacters.MALLOW
    _character_id: int = 4
    _starting_level: int = 2
    _max_hp: UInt16 = UInt16(6)
    _speed: UInt8 = UInt8(18)
    _attack: UInt8 = UInt8(20)
    _defense: UInt8 = UInt8(0)
    _magic_attack: UInt8 = UInt8(11)
    _magic_defense: UInt8 = UInt8(7)
    _learned_spells: "dict[int, Type[CharacterSpell]]" = {
        2: Thunderbolt,
        3: HPRain,
        6: Psychopath,
        10: Shocker,
        14: Snowy,
        18: StarRain,
    }
    _palette: MallowPaletteSet = DefaultMallowPalette()

    @property
    def palette(self) -> "MallowPaletteSet":
        return self._palette

    # Vanilla levelup stat growths
    # (hp, attack, defense, m.attack, m.defense)
    _starting_growths: List[StatGrowth] = [
        StatGrowth(4, 2, 3, 2, 2),
        # Vanilla growths
        StatGrowth(4, 2, 3, 2, 2),
        StatGrowth(4, 2, 3, 2, 2),
        StatGrowth(4, 2, 3, 3, 2),
        StatGrowth(5, 2, 3, 3, 2),
        StatGrowth(5, 3, 3, 3, 2),
        StatGrowth(5, 3, 3, 4, 2),
        StatGrowth(6, 3, 3, 4, 3),
        StatGrowth(6, 3, 3, 4, 3),
        StatGrowth(6, 4, 3, 4, 3),
        StatGrowth(7, 4, 3, 5, 3),
        StatGrowth(7, 4, 3, 5, 3),
        StatGrowth(7, 4, 3, 5, 3),
        StatGrowth(8, 5, 3, 5, 3),
        StatGrowth(8, 5, 3, 5, 3),
        StatGrowth(8, 5, 3, 5, 3),
        StatGrowth(9, 5, 3, 5, 4),
        StatGrowth(9, 6, 3, 5, 4),
        StatGrowth(9, 6, 3, 5, 4),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
        StatGrowth(2, 2, 2, 2, 2),
    ]

    # Vanilla levelup stat bonus options
    # (hp, attack, defense, m.attack, m.defense)
    _levelup_bonuses: List[StatGrowth] = [
        StatGrowth(4, 1, 1, 2, 1),
        StatGrowth(4, 3, 1, 1, 1),
        StatGrowth(6, 1, 1, 1, 1),
        StatGrowth(4, 1, 1, 2, 1),
        StatGrowth(4, 3, 1, 1, 1),
        StatGrowth(6, 1, 1, 1, 1),
        StatGrowth(4, 1, 1, 2, 1),
        StatGrowth(4, 3, 1, 1, 1),
        StatGrowth(6, 1, 1, 1, 1),
        StatGrowth(4, 1, 1, 2, 1),
        StatGrowth(4, 3, 1, 1, 1),
        StatGrowth(6, 1, 1, 1, 1),
        StatGrowth(4, 1, 1, 2, 1),
        StatGrowth(4, 3, 1, 1, 1),
        StatGrowth(6, 1, 1, 1, 1),
        StatGrowth(4, 1, 1, 2, 1),
        StatGrowth(4, 3, 1, 1, 1),
        StatGrowth(6, 1, 1, 1, 1),
        StatGrowth(4, 1, 1, 2, 1),
        StatGrowth(1, 3, 1, 1, 1),
        StatGrowth(2, 1, 1, 1, 1),
        StatGrowth(1, 1, 1, 2, 1),
        StatGrowth(1, 3, 1, 1, 1),
        StatGrowth(2, 1, 1, 1, 1),
        StatGrowth(1, 1, 1, 2, 1),
        StatGrowth(1, 3, 1, 1, 1),
        StatGrowth(2, 1, 1, 1, 1),
        StatGrowth(1, 1, 1, 2, 1),
        StatGrowth(1, 3, 1, 1, 1),
    ]
    _ending_palettes: List[int] = [0x37A9F6, 0x37B374]

    _standard_sprite_addresses: List[int] = [0x35FF2F]
    _original_weapon_sprite_ids: List[Union[int, None]] = [
        19,
        None,
        20,
        21,
        22,
        23,
        24,
    ]
    _sprite_ids_as_main_character: List[int] = [0, 1, 2, 3, 4, 5, 6]
    _sprite_addresses: List[Union[list[int], None]] = [
        [],
        None,
        [0x35FF2F, 0x35CDC3],
        [],
        [0x35ED66, 0x35ED5D, 0x35EEC4, 0x35EEBB, 0x35F003, 0x35F00C, 0x35FF89],
        [
            0x35EDB0,
            0x35EDA1,
            0x35EE17,
            0x35EE08,
            0x35EF7E,
            0x35EF6D,
            0x35F0BE,
            0x35F0AF,
        ],
        [],
    ]  # not building an assembler for this in this version

    _battle_sprite_offset: int = 0x020229
    _battle_sprite_id: int = 0x14
    _menu_sprite_offset: int = 0x0318A7
    _menu_sprite_id: int = 0x14
    _abxy_coord_offset: int = 0x02368D
    _abxy_coord: int = 0xC4
    _cursor_coord_offset: int = 0x029756
    _cursor_coord: int = 0x12
    _portrait_sprite_offset: int = 0x24127
    _portrait_id: int = 0x2B
    _item_use_offset: int = 0x358C5F
    _item_use_bytes = bytearray([0x03, 0x81, 0x00, 0x18, 0x00, 0x02])
    _runaway_offset: int = 0x350563
    _runaway_bytes = bytearray([0x03, 0x81, 0x08, 0x13, 0x00, 0x00])

    _item_id: int = 222
    _description: str = PlayableCharacters.MALLOW.value
    _placeholder: str = "`MALLOW_NAME`"
    _starter_script: int = 188
    _container_script: int = 194
    _doll: Type[NPC] = MallowDoll
    _model: Type[NPC] = MallowNPC
    _sprites_primary: "dict[str, tuple[int, int, bool]]" = {
        "south": (0, 12, True),
        "defend": (2, 15, True),
        "face_north": (0, 1, False),
        "face_south": (0, 0, False),
        "shocked_loop": (3, 8, False),
        "shocked_loop_backwards": (3, 9, False),
        "shocked_backwards_sequence": (2, 3, False),
        "shocked_shadow": (3, 0, False),
        "shocked_shadow_backwards": (2, 8, True),
        "crying": (3, 3, False),
        "crying_backwards": (3, 4, False),
        "looking_down_static": (0, 6, True),
        "looking_down": (0, 6, False),
        "looking_down_away": (0, 7, False),
        "floored": (3, 1, True),
        "hurt": (0, 6, True),
        "shaking_head": (0, 8, False),
        "shaking_head_backward": (0, 9, False),
        "sleeping": (2, 6, False),
        "salute": (2, 9, False),
        "joy": (2, 9, False),
        "joy_behind": (3, 2, False),
        "joy_jump": (3, 2, False),
        "distracted": (0, 10, True),
        "displeased": (3, 4, False),
        "challenge": (4, 5, False),
        "look_to_side": (0, 8, True),
        "look_to_down": (0, 9, True),
        "look_to_side_behind": (0, 11, True),
        "cast_frame_1": (2, 11, True),
        "cast_frame_2": (2, 12, True),
        "cast_frame_3": (2, 13, True),
        "cast_frame_4": (2, 10, True),
        "look_up_slightly": (2, 22, True),
        "look_way_up": (2, 23, True),
        "victory_pose": (2, 10, True),
        "prince_neutral": (0, 0, True),
        "prince_down": (0, 9, True),
        "prince_left": (0, 8, True),
        "hammer": (2, 3, True),
        "hammer_static": (2, 3, True),
    }
    _sprites_secondary: "dict[str, tuple[int, int, bool]]" = {
        "south": (0, 20, True),
        "defend": (1, 15, True),
        "face_north": (0, 1, False),
        "face_south": (0, 0, False),
        "shocked_loop": (2, 8, False),
        "shocked_loop_backwards": (2, 9, False),
        "shocked_backwards_sequence": (1, 3, False),
        "shocked_shadow": (2, 0, False),
        "shocked_shadow_backwards": (1, 8, True),
        "crying": (0, 13, False),
        "crying_backwards": (0, 14, False),
        "looking_down_static": (0, 14, True),
        "looking_down": (0, 6, False),
        "looking_down_away": (0, 7, False),
        "floored": (2, 1, True),
        "hurt": (0, 14, True),
        "shaking_head": (0, 8, False),
        "shaking_head_backward": (0, 9, False),
        "sleeping": (1, 6, False),
        "salute": (2, 17, True),
        "joy": (1, 9, False),
        "joy_behind": (2, 2, False),
        "joy_jump": (2, 2, False),
        "distracted": (0, 18, True),
        "displeased": (0, 5, False),
        "challenge": (3, 5, False),
        "look_to_side": (0, 16, True),
        "look_to_down": (0, 17, True),
        "look_to_side_behind": (0, 19, True),
        "cast_frame_1": (1, 11, True),
        "cast_frame_2": (1, 12, True),
        "cast_frame_3": (1, 13, True),
        "cast_frame_4": (1, 10, True),
        "look_up_slightly": (1, 22, True),
        "look_way_up": (1, 23, True),
        "victory_pose": (1, 10, True),
        "prince_neutral": (2, 14, True),
        "prince_down": (2, 15, True),
        "prince_left": (2, 16, True),
        "hammer": (1, 3, True),
        "hammer_static": (1, 3, True),
    }

    _associated_spotted_class: Type[SpottedCharacter] = MallowSpotted


def initiate_items(world) -> List[Character]:
    """Instantiate each character for use in the game world."""
    return [
        Mario(world),
        Mallow(world),
        Geno(world),
        Bowser(world),
        Toadstool(world),
    ]
