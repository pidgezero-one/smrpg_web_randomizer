# Data module for character data.

from randomizer.logic import utils, flags
from randomizer.logic.patch import Patch
from randomizer.helpers.flag_helpers import PlayableCharacters

from . import spells
from .utils import color_to_bytes, palette_to_bytes


classic_palette_offset = 0x2567E6
minecart_palette_offset = 0x256DFE
map_palette_offset = 0x3E99C1

class StatGrowth:
    """Container class for a stat growth/bonus for a certain level + character."""

    def __init__(self, max_hp, attack, defense, magic_attack, magic_defense):
        self.max_hp = max_hp
        self.attack = attack
        self.defense = defense
        self.magic_attack = magic_attack
        self.magic_defense = magic_defense

    @property
    def best_choices(self):
        """Best choice of attributes for a levelup bonus based on the numbers.  For HP, it must be twice the total of
        the attack + defense options to be considered "better".  This is arbitrary, but HP is less useful.

        :return: Tuple of attributes to select for best choice.
        :rtype: tuple[str]
        """
        options = [
            (self.max_hp / 2, ("max_hp", )),
            (self.attack + self.defense, ("attack", "defense")),
            (self.magic_attack + self.magic_defense, ("magic_attack", "magic_defense")),
        ]
        a, b = max(options)
        options = [(c, d) for (c, d) in options if c == a]
        a, b = options[0]
        return b

    def as_bytes(self):
        """Return byte representation of this stat growth object for the patch.

        :rtype: bytearray
        """
        data = bytearray()

        # HP is one byte on its own.  Attack/defense stats are 4 bits each combined into a single byte together.
        data += utils.ByteField(self.max_hp).as_bytes()

        physical = self.attack << 4
        physical |= self.defense
        data += utils.ByteField(physical).as_bytes()

        magical = self.magic_attack << 4
        magical |= self.magic_defense
        data += utils.ByteField(magical).as_bytes()

        return data


class LevelUpExps:
    """Class for amounts of exp required for each levelup."""
    BASE_ADDRESS = 0x3a1aff

    def __init__(self):
        self.levels = [
            0,
            16,
            48,
            84,
            130,
            200,
            290,
            402,
            538,
            700,
            890,
            1110,
            1360,
            1640,
            1950,
            2290,
            2660,
            3060,
            3490,
            3950,
            4440,
            4960,
            5510,
            6088,
            6692,
            7320,
            7968,
            8634,
            9315,
            9999,
        ]

    def get_xp_for_level(self, level):
        """
        :type level: int
        :return: XP required to reach this level.
        :rtype: int
        """
        if level < 1 or level > 30:
            raise ValueError("Level must be between 1 and 30")
        return self.levels[level - 1]

    def get_patch(self):
        """Get patch for exp required for each level up.

        :return: Patch data.
        :rtype: randomizer.logic.patch.Patch
        """
        # Data is 29 blocks (starting at level 2), 2 bytes each block.
        data = bytearray()
        for level in range(2, 31):
            data += utils.ByteField(self.get_xp_for_level(level), num_bytes=2).as_bytes()

        patch = Patch()
        patch.add_data(self.BASE_ADDRESS, data)
        return patch


class Character:
    """Class for handling a character."""
    BASE_ADDRESS = 0x3a002c
    BASE_STAT_GROWTH_ADDRESS = 0x3a1b39
    BASE_STAT_BONUS_ADDRESS = 0x3a1cec
    BASE_LEARNED_SPELLS_ADDRESS = 0x3a42f5

    # Stats used during levelups.
    LEVEL_STATS = ["max_hp", "attack", "defense", "magic_attack", "magic_defense"]

    # Base stats.
    original_name = ''
    index = 0
    starting_level = 1
    max_hp = 1
    speed = 1
    attack = 1
    defense = 1
    magic_attack = 1
    magic_defense = 1
    xp = 0
    learned_spells = {}
    palette = None
    forest_maze_sprite_id = 0x0
    mway_3_npc_id = []
    mway_2_npc_id = []
    mway_1_npc_id = []
    moleville_sprite_id = 0x0
    ending_palettes = []
    default_palette_bytes = []
    default_underwater_palette_bytes = []

    # Placeholders for vanilla starting levelup growth and bonus numbers.
    starting_growths = ()
    starting_bonuses = ()

    standard_sprite_addresses = []
    original_weapon_sprite_ids = []
    sprite_ids_as_main_character = []
    sprite_addresses = [[], [], []] # not building an assembler for this in this version

    battle_sprite_offset = None
    battle_sprite_id = 0
    menu_sprite_offset = None
    menu_sprite_id = 0
    abxy_coord_offset = None
    abxy_coord = 0
    cursor_coord_offset = None
    cursor_coord = 0
    portrait_sprite_offset = None
    portrait_id = 0

    def __init__(self, world):
        """

        Args:
            world (randomizer.logic.main.GameWorld):

        """
        self.world = world
        self.starting_spells = set()

        # Level-up stat growth and bonuses.
        self.levelup_growths = []
        for max_hp, attack, defense, magic_attack, magic_defense in self.starting_growths:
            self.levelup_growths.append(StatGrowth(max_hp, attack, defense, magic_attack, magic_defense))

        self.levelup_bonuses = []
        for max_hp, attack, defense, magic_attack, magic_defense in self.starting_bonuses:
            self.levelup_bonuses.append(StatGrowth(max_hp, attack, defense, magic_attack, magic_defense))

        self.palette = None

    def __str__(self):
        return "<{}>".format(self.name)

    def __repr__(self):
        return str(self)

    @property
    def name(self):
        return self.__class__.__name__

    def get_stat_at_level(self, attr, level):
        """Get natural value of the given stat at the given level using just the levelup growths.

        :type attr: str
        :type level: int
        :rtype: int
        """
        if level < 1 or level > 30:
            raise ValueError("Level must be between 1 and 30")

        value = getattr(self, attr)
        for g in self.levelup_growths[:level - 1]:
            value += getattr(g, attr)
        return value

    def get_optimal_stat_at_level(self, attr, level):
        """Get optimal value of the given stat at the given level using the levelup growths and best choice bonuses.

        :type attr: str
        :type level: int
        :rtype: int
        """
        if level < 1 or level > 30:
            raise ValueError("Level must be between 1 and 30")

        value = self.get_stat_at_level(attr, level)
        for b in self.levelup_bonuses[:level - 1]:
            if attr in b.best_choices:
                value += getattr(b, attr)
        return value

    def get_max_stat_at_level(self, attr, level):
        """Get max value of the given stat at the given level using the levelup growths and bonuses.

        :type attr: str
        :type level: int
        :rtype: int
        """
        if level < 1 or level > 30:
            raise ValueError("Level must be between 1 and 30")

        value = self.get_stat_at_level(attr, level)
        for b in self.levelup_bonuses[:level - 1]:
            value += getattr(b, attr)
        return value
        

    def special_palette(self, colours, address, patch):
        for j in range(0, len(colours)):
            i = colours[j]
            if i is not None:
                colour = self.palette.colours[i]
                patch.add_data(address + j*2, color_to_bytes(colour))
        return patch

    def get_patch(self):
        """Build patch data for this character.

        :return: Patch data for this character.
        :rtype: randomizer.logic.patch.Patch
        """
        patch = Patch()

        # Build character patch data.
        char_data = bytearray()
        char_data += utils.ByteField(self.starting_level).as_bytes()
        char_data += utils.ByteField(self.max_hp, num_bytes=2).as_bytes()  # Current HP
        char_data += utils.ByteField(self.max_hp, num_bytes=2).as_bytes()  # Max HP
        char_data += utils.ByteField(self.speed).as_bytes()
        char_data += utils.ByteField(self.attack).as_bytes()
        char_data += utils.ByteField(self.defense).as_bytes()
        char_data += utils.ByteField(self.magic_attack).as_bytes()
        char_data += utils.ByteField(self.magic_defense).as_bytes()
        char_data += utils.ByteField(self.xp, num_bytes=2).as_bytes()
        # Set starting weapon/armor/accessory as blank for all characters.
        char_data += utils.ByteField(0xff).as_bytes()
        char_data += utils.ByteField(0xff).as_bytes()
        char_data += utils.ByteField(0xff).as_bytes()
        char_data.append(0x00)  # Unused byte
        char_data += utils.BitMapSet(4, [spell.index for spell in self.starting_spells]).as_bytes()

        # Base address plus offset based on character index.
        addr = self.BASE_ADDRESS + (self.index * 20)
        patch.add_data(addr, char_data)

        # Add levelup stat growth and bonuses to the patch data for this character.  Offset is 15 bytes for each stat
        # object, 3 bytes per character.
        for i, stat in enumerate(self.levelup_growths):
            addr = self.BASE_STAT_GROWTH_ADDRESS + (i * 15) + (self.index * 3)
            patch.add_data(addr, stat.as_bytes())

        for i, stat in enumerate(self.levelup_bonuses):
            addr = self.BASE_STAT_BONUS_ADDRESS + (i * 15) + (self.index * 3)
            patch.add_data(addr, stat.as_bytes())

        # Add learned spells data.
        # Data is 29 blocks (starting at level 2), 5 bytes each block (1 byte per character in order)
        base_addr = self.BASE_LEARNED_SPELLS_ADDRESS + self.index
        for level in range(2, 31):
            level_addr = base_addr + ((level - 2) * 5)
            # If we have a spell for this level, add the index.  Otherwise it should be 0xff for no spell learned.
            if self.learned_spells.get(level):
                patch.add_data(level_addr, utils.ByteField(self.learned_spells[level].index).as_bytes())
            else:
                patch.add_data(level_addr, utils.ByteField(0xff).as_bytes())

        if self.palette:
            colourbytes = palette_to_bytes(self.palette.colours)
            poisonbytes = palette_to_bytes(self.palette.poison_colours)
            underwaterbytes = palette_to_bytes(self.palette.underwater_colours)
            for address in self.palette.starting_addresses:
                patch.add_data(address, colourbytes)
            for address in self.palette.poison_addresses:
                patch.add_data(address, poisonbytes)
            for address in self.palette.underwater_addresses:
                patch.add_data(address, underwaterbytes)

            if self.palette.rename_character and self.world.settings.is_flag_enabled(flags.ChangeNames):
                name = self.palette.name
                clone_name = self.palette.name.upper()
                while len(name) < 10:
                    name += " "
                if len(clone_name) < 8:
                    clone_name = clone_name + " CLONE"
                else:
                    clone_name = clone_name + " 2"
                while len(clone_name) < 13:
                    clone_name += " "
                patch.add_data(self.palette.name_address, name)
                patch.add_data(self.palette.clone_name_address, clone_name)
        else:
            colourbytes = self.default_palette_bytes
            underwaterbytes = self.default_underwater_palette_bytes

        patch.add_data(self.ending_palettes[0], colourbytes)
        #if self.index not in [2, 3]:
        patch.add_data(self.ending_palettes[1], underwaterbytes)


            
        

        return patch


# ******************* Actual character data classes.
class Mario(Character):
    original_name = PlayableCharacters.mario
    placeholder = "`MARIO_NAME`"
    index = 0
    starting_level = 1
    max_hp = 20
    speed = 20
    attack = 20
    defense = 0
    magic_attack = 10
    magic_defense = 2
    learned_spells = {
        1: spells.Jump,
        3: spells.FireOrb,
        6: spells.SuperJump,
        10: spells.SuperFlame,
        14: spells.UltraJump,
        18: spells.UltraFlame,
    }

    # Vanilla levelup stat growths
    # (hp, attack, defense, m.attack, m.defense)
    starting_growths = (
        (5, 3, 2, 2, 2),
        (5, 3, 2, 2, 2),
        (5, 3, 3, 2, 2),
        (5, 3, 3, 2, 2),
        (5, 4, 3, 3, 2),
        (6, 4, 3, 3, 2),
        (6, 4, 3, 3, 2),
        (7, 4, 3, 3, 2),
        (7, 4, 3, 3, 2),
        (7, 5, 4, 3, 3),
        (8, 5, 4, 4, 3),
        (8, 5, 4, 4, 3),
        (8, 5, 4, 4, 3),
        (9, 5, 4, 4, 3),
        (9, 6, 4, 4, 3),
        (9, 6, 4, 4, 3),
        (10, 6, 4, 4, 3),
        (10, 6, 4, 5, 3),
        (10, 6, 4, 5, 3),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
    )

    # Vanilla levelup stat bonus options
    # (hp, attack, defense, m.attack, m.defense)
    starting_bonuses = (
        (3, 1, 1, 3, 1),
        (3, 2, 1, 1, 1),
        (4, 1, 1, 1, 1),
        (3, 1, 1, 3, 1),
        (3, 2, 1, 1, 1),
        (4, 1, 1, 1, 1),
        (3, 1, 1, 3, 1),
        (3, 2, 1, 1, 1),
        (4, 1, 1, 1, 1),
        (3, 1, 1, 3, 1),
        (3, 2, 1, 1, 1),
        (4, 1, 1, 1, 1),
        (3, 1, 1, 3, 1),
        (3, 2, 1, 1, 1),
        (4, 1, 1, 1, 1),
        (3, 1, 1, 3, 1),
        (3, 2, 1, 1, 1),
        (4, 1, 1, 1, 1),
        (3, 1, 1, 3, 1),
        (1, 2, 1, 1, 1),
        (2, 1, 1, 1, 1),
        (1, 1, 1, 3, 1),
        (1, 2, 1, 1, 1),
        (2, 1, 1, 1, 1),
        (1, 1, 1, 3, 1),
        (1, 2, 1, 1, 1),
        (2, 1, 1, 1, 1),
        (1, 1, 1, 3, 1),
        (1, 2, 1, 1, 1),
    )
    forest_maze_sprite_id = 0x03
    mway_3_npc_id = [0x03, 0xB0]
    mway_2_npc_id = [0x03, 0x70]
    mway_1_npc_id = [0x03, 0x40]
    moleville_sprite_id = 0x02
    ending_palettes = (0x37A9D8, 0x37B31A)
    default_palette_bytes = bytearray([0xFF, 0x7F, 0x3F, 0x43, 0x38, 0x26, 0xB5, 0x25, 0xEF, 0x18, 0x1D, 0x1D, 0x3F, 0x00, 0x36, 0x00, 0x0C, 0x00, 0xE7, 0x70, 0x00, 0x6C, 0x00, 0x30, 0x7C, 0x6F, 0x33, 0x46, 0x63, 0x0C])
    default_underwater_palette_bytes = bytearray([0xB5, 0x7A, 0x35, 0x52, 0x70, 0x3D, 0x2C, 0x39, 0xA8, 0x30, 0x35, 0x24, 0x0C, 0x24, 0x07, 0x24, 0x03, 0x24, 0x00, 0x6C, 0x00, 0x3C, 0x00, 0x14, 0x53, 0x6E, 0x6D, 0x51, 0x63, 0x0C])
    
    dialog_replacements = [
        (659,''' You can't get inside Booster's
 Tower very easily. You'll need
 a pretty good jumper for that.[await]'''), # conditional based on booster's tower flag
    ]


    original_weapon_sprite_ids = [0, 1, 2, 3, 4, 5, 6]
    sprite_ids_as_main_character = [0, 1, 2, 3, 4, 5, 6]
    sprite_addresses = [[], [], [0x35F119, 0x35FF13, 0x35CD9F], [], [0x35eCF9, 0x35ECF0, 0x35EDC4, 0x35EDDF, 0x35EDD4, 0x35EEF9, 0x35EFAC, 0x35EFB5, 0x35F0d2, 0x358Ce7, 0x358D79, 0x358E0B, 0x35FF6D, 0x35ECF0, 0x35ECF9], [0x35ED8C, 0x35ED7D, 0x35EE58, 0x35EE49, 0x35EE99, 0x35EE8A, 0x35F032, 0x35F023, 0x35F10B], []] # not building an assembler for this in this version
    
    battle_sprite_offset = 0x020225
    battle_sprite_id = 0x02
    menu_sprite_offset = 0x0318A3
    menu_sprite_id = 0x02
    abxy_coord_offset = 0x023685
    abxy_coord = 0xBF
    cursor_coord_offset = 0x029752
    cursor_coord = 0x13
    portrait_sprite_offset = 0x24123
    portrait_id = 0x28
    item_use_offset = 0x3589A5
    item_use_bytes = bytearray([0x03, 0x81, 0x00, 0x06, 0x00, 0x01])
    runaway_offset = 0x350547
    runaway_bytes = bytearray([0x03, 0x81, 0x08, 0x00, 0x00, 0x00])

    def get_patch(self):
        patch = super().get_patch()

        if self.palette is not None:
            patch = self.special_palette([0, 1, 2, 3, 4, 6, 7, 8, 8, 10, 11, 11, 12, 13, 14], self.palette.doll_addresses[0], patch)
            if self.world.starting_character == self.index or not self.world.settings.is_flag_enabled(flags.PlayAsStarter):
                patch = self.special_palette([10, 6, 1, None, None, None, None, None, None, None, None, None, None, None, None], classic_palette_offset, patch)
                patch = self.special_palette([None, 13, 1, 2, None, 5, 3, 6, 7, 9, 4, 9, 8, 10, 11], minecart_palette_offset, patch)
                patch = self.special_palette([0, 1, 2, 3, 4, 6, 7, 8, 8, 10, 11, 11, 12, 13, 14], map_palette_offset, patch)

        if self.world.starting_character == self.index or not self.world.settings.is_flag_enabled(flags.PlayAsStarter):
            if self.palette is not None:
                patch.add_data(0x37B0A4, palette_to_bytes(self.palette.colours))
                patch.add_data(0x37B0A6, bytearray([0x5F, 0x19, 0xD8, 0x1C, 0x35]))

        return patch


class Peach(Character):
    index = 1
    original_name = PlayableCharacters.toadstool
    placeholder = "`PEACH_NAME`"
    starting_level = 9
    max_hp = 15
    speed = 24
    attack = 15
    defense = 0
    magic_attack = 14
    magic_defense = 14
    learned_spells = {
        3: spells.Therapy,
        7: spells.GroupHug,
        11: spells.SleepyTime,
        13: spells.ComeBack,
        15: spells.Mute,
        18: spells.PsychBomb,
    }

    # Vanilla levelup stat growths
    # (hp, attack, defense, m.attack, m.defense)
    starting_growths = (
        (2, 2, 2, 1, 1),
        (2, 2, 2, 1, 1),
        (2, 2, 2, 2, 1),
        (2, 2, 3, 2, 1),
        (2, 2, 3, 2, 1),
        (2, 2, 3, 3, 2),
        (2, 2, 3, 3, 2),
        (3, 2, 3, 3, 2),
        # Vanilla growths
        (4, 1, 3, 4, 2),
        (5, 2, 3, 4, 3),
        (6, 3, 3, 4, 3),
        (7, 4, 3, 4, 3),
        (8, 5, 3, 4, 3),
        (9, 6, 3, 4, 3),
        (10, 7, 3, 4, 4),
        (11, 8, 4, 4, 4),
        (12, 9, 4, 4, 4),
        (13, 10, 4, 4, 4),
        (14, 10, 4, 4, 4),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
    )

    # Vanilla levelup stat bonus options
    # (hp, attack, defense, m.attack, m.defense)
    starting_bonuses = (
        (5, 1, 1, 3, 1),
        (5, 3, 1, 1, 1),
        (9, 1, 1, 1, 1),
        (5, 1, 1, 3, 1),
        (5, 3, 1, 1, 1),
        (9, 1, 1, 1, 1),
        (5, 1, 1, 3, 1),
        (5, 3, 1, 1, 1),
        (9, 1, 1, 1, 1),
        (5, 1, 1, 3, 1),
        (5, 3, 1, 1, 1),
        (9, 1, 1, 1, 1),
        (5, 1, 1, 3, 1),
        (5, 3, 1, 1, 1),
        (9, 1, 1, 1, 1),
        (5, 1, 1, 3, 1),
        (5, 3, 1, 1, 1),
        (9, 1, 1, 1, 1),
        (5, 1, 1, 3, 1),
        (3, 3, 1, 1, 1),
        (2, 1, 1, 1, 1),
        (1, 1, 1, 3, 1),
        (1, 3, 1, 1, 1),
        (2, 1, 1, 1, 1),
        (1, 1, 1, 3, 1),
        (1, 3, 1, 1, 1),
        (2, 1, 1, 1, 1),
        (1, 1, 1, 3, 1),
        (1, 3, 1, 1, 1),
    )
    forest_maze_sprite_id = 0x07
    mway_3_npc_id = [0x07, 0xB0]
    mway_2_npc_id = [0x07, 0x70]
    mway_1_npc_id = [0x07, 0x40]
    moleville_sprite_id = 0x06
    ending_palettes = (0x37B086, 0x37B338)
    default_palette_bytes = bytearray([0xFF, 0x7F, 0xBF, 0x5B, 0x7C, 0x3A, 0x53, 0x09, 0xAA, 0x0C, 0x7F, 0x7E, 0x3D, 0x59, 0x96, 0x40, 0x0E, 0x00, 0x5F, 0x1F, 0x3F, 0x12, 0xE7, 0x68, 0x3A, 0x67, 0xAF, 0x31, 0x63, 0x0C])
    default_underwater_palette_bytes = bytearray([0xD6, 0x6A, 0xB6, 0x52, 0xD4, 0x39, 0x0E, 0x19, 0xA8, 0x14, 0x56, 0x69, 0xD5, 0x50, 0x90, 0x40, 0x4B, 0x14, 0x76, 0x2A, 0xB6, 0x21, 0xC6, 0x58, 0x53, 0x5A, 0x4C, 0x35, 0x63, 0x0C])
    
    dialog_replacements = [
        (659,''' You can't get inside Booster's
 Tower very easily. You'll need
 a persuasive princess for that.[await]'''),
        (270, ''' Good day, Princess![await][pause]
 Did you forget something in your
 room?[await]''')
    ]

    original_weapon_sprite_ids = [7, None, 8, 9, 10, 11, 12]
    sprite_ids_as_main_character = [0, 1, 2, 3, 4, 5, 634]
    sprite_addresses = [[], None, [0x35FF1A, 0x35A9FD, 0x35CDA8], [], [0x35ED1A, 0x35ED0B, 0x35EEE5, 0x35EED6, 0x35EFDE, 0x35EFCD, 0x35F049, 0x35F058, 0x35FF74], [0x35EF1D, 0x35EF0E, 0x35F0F6, 0x35F0E7], [0x35A9A0]] # not building an assembler for this in this version

    battle_sprite_offset = 0x020226
    battle_sprite_id = 0x08
    menu_sprite_offset = 0x0318A4
    menu_sprite_id = 0x08
    abxy_coord_offset = 0x023687
    abxy_coord = 0xBE
    cursor_coord_offset = 0x029753
    cursor_coord = 0x13
    portrait_sprite_offset = 0x24124
    portrait_id = 0x29
    item_use_offset = 0x358A3c
    item_use_bytes = bytearray([0x03, 0x81, 0x00, 0x0C, 0x00, 0x03])
    runaway_offset = 0x35054E
    runaway_bytes = bytearray([0x03, 0x81, 0x08, 0x07, 0x00, 0x00])

    # print([hex(i) for i in palette_to_bytes(["EFAD31", "DE9421", "B57B21", "946318", "6B5218", "6B5218", "212110", "DE9421", "946318", "4A3910", "DE9421", "9C6B18", "523910", "101008", "181818"])])

    def get_patch(self):
        patch = super().get_patch()

        if self.world.starting_character == self.index and self.world.settings.is_flag_enabled(flags.PlayAsStarter):
            if self.palette is None:
                classicbytes = palette_to_bytes(["E050E0", "A82828", "F8D860", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000"])
                patch.add_data(classic_palette_offset, classicbytes)
                mapbytes = palette_to_bytes(["F8F8F8", "F8E8B0", "E09870", "985010", "502818", "F898F8", "E848B0", "B02080", "700000", "F8D038", "F88820", "3838D0", "D0C8C8", "786860", "181818"])
                patch.add_data(map_palette_offset, mapbytes)
                patch.add_data(0x37B0A4, self.default_palette_bytes)
            else:
                patch = self.special_palette([6, 3, 1, None, None, None, None, None, None, None, None, None, None, None, None], classic_palette_offset, patch)
                patch = self.special_palette([i for i in range(0,15)], map_palette_offset, patch)
                patch.add_data(0x37B0A4, palette_to_bytes(self.palette.colours))

            # group hug
            #patch.add_data(0x35FF3E, 0x00)
            patch.add_data(0x35FF43, bytearray([0x03, 0x81, 0x00, 0x05, 0x00, 0x04]))
            #patch.add_data(0x35FF98, 0x00)
            patch.add_data(0x35FF9D, bytearray([0x03, 0x81, 0x10, 0x02, 0x00, 0x01]))

        return patch



class Bowser(Character):
    index = 2
    original_name = PlayableCharacters.bowser
    placeholder = "`BOWSER_NAME`"
    starting_level = 8
    max_hp = 25
    speed = 15
    attack = 39
    defense = 15
    magic_attack = 1
    magic_defense = 6
    learned_spells = {
        8: spells.Terrorize,
        12: spells.PoisonGas,
        15: spells.Crusher,
        18: spells.BowserCrush,
    }

    # Vanilla levelup stat growths
    # (hp, attack, defense, m.attack, m.defense)
    starting_growths = (
        (6, 6, 5, 1, 3),
        (6, 6, 5, 1, 3),
        (7, 6, 5, 1, 3),
        (7, 6, 5, 1, 3),
        (7, 6, 5, 2, 3),
        (8, 6, 5, 2, 3),
        (8, 6, 5, 2, 3),
        # Vanilla growths
        (8, 3, 3, 4, 2),
        (8, 3, 3, 4, 2),
        (8, 4, 3, 4, 2),
        (8, 4, 3, 4, 2),
        (8, 4, 3, 4, 2),
        (8, 4, 3, 4, 2),
        (8, 4, 3, 4, 2),
        (8, 5, 4, 4, 2),
        (8, 5, 4, 4, 2),
        (9, 5, 4, 4, 2),
        (9, 6, 4, 4, 2),
        (9, 6, 4, 4, 2),
        (4, 2, 2, 2, 2),
        (4, 2, 2, 2, 2),
        (4, 2, 2, 2, 2),
        (4, 2, 2, 2, 2),
        (4, 2, 2, 2, 2),
        (4, 2, 2, 2, 2),
        (4, 2, 2, 2, 2),
        (4, 2, 2, 2, 2),
        (4, 2, 2, 2, 2),
        (4, 2, 2, 2, 2),
    )

    # Vanilla levelup stat bonus options
    # (hp, attack, defense, m.attack, m.defense)
    starting_bonuses = (
        (1, 1, 1, 3, 1),
        (1, 2, 1, 1, 1),
        (3, 1, 1, 1, 1),
        (1, 1, 1, 3, 1),
        (1, 2, 1, 1, 1),
        (3, 1, 1, 1, 1),
        (1, 1, 1, 3, 1),
        (1, 2, 1, 1, 1),
        (3, 1, 1, 1, 1),
        (1, 1, 1, 3, 1),
        (1, 2, 1, 1, 1),
        (3, 1, 1, 1, 1),
        (1, 1, 1, 3, 1),
        (1, 2, 1, 1, 1),
        (3, 1, 1, 1, 1),
        (1, 1, 1, 3, 1),
        (1, 2, 1, 1, 1),
        (3, 1, 1, 1, 1),
        (1, 1, 1, 3, 1),
        (1, 2, 1, 1, 1),
        (3, 1, 1, 1, 1),
        (1, 1, 1, 3, 1),
        (1, 2, 1, 1, 1),
        (3, 1, 1, 1, 1),
        (1, 1, 1, 3, 1),
        (1, 2, 1, 1, 1),
        (3, 1, 1, 1, 1),
        (1, 1, 1, 3, 1),
        (1, 2, 1, 1, 1),
    )
    forest_maze_sprite_id = 0x0B
    mway_3_npc_id = [0x0B, 0xB0]
    mway_2_npc_id = [0x0B, 0x70]
    mway_1_npc_id = [0x0B, 0x40]
    moleville_sprite_id = 0x0A
    ending_palettes = (0x37B068, 0x37B356)
    default_palette_bytes = bytearray([0xFF, 0x7F, 0xFF, 0x2B, 0x3E, 0x1B, 0xF7, 0x08, 0xEA, 0x0C, 0xA7, 0x1A, 0xE4, 0x11, 0x23, 0x09, 0xA4, 0x0C, 0x19, 0x12, 0x31, 0x11, 0x44, 0x04, 0x52, 0x42, 0x8C, 0x21, 0x63, 0x0C])
    default_underwater_palette_bytes = bytearray([0xD6, 0x6A, 0xD6, 0x32, 0x56, 0x26, 0xD1, 0x18, 0xC8, 0x1C, 0x06, 0x26, 0x64, 0x25, 0x04, 0x19, 0xA4, 0x1C, 0x92, 0x21, 0x0D, 0x21, 0x64, 0x18, 0xCE, 0x41, 0x4A, 0x29, 0x63, 0x0C])
    
    dialog_replacements = [
        (659,''' You can't get inside Booster's
 Tower very easily. You'll need
 a REALLY strong person for that.[await]''')
    ]

    original_weapon_sprite_ids = [13, None, 14, 15, 16, 17, 18]
    sprite_ids_as_main_character = [0, 1, 2, 3, 4, 5, 634]
    sprite_addresses = [[], None, [0x35FF21, 0x35CDB1], [], [0x35ED2A, 0x35ED35, 0x35F074, 0x35F069, 0x35FF7B], [0x35EE2B, 0x35EE6C, 0x35EF31, 0x35EF95], []] # not building an assembler for this in this version

    battle_sprite_offset = 0x020227
    battle_sprite_id = 0x0E
    menu_sprite_offset = 0x0318A5
    menu_sprite_id = 0x0E
    abxy_coord_offset = 0x023689
    abxy_coord = 0xBA
    cursor_coord_offset = 0x029754
    cursor_coord = 0x24
    portrait_sprite_offset = 0x24125
    portrait_id = 0x2A
    item_use_offset = 0x358B27
    item_use_bytes = bytearray([0x03, 0x81, 0x00, 0x12, 0x00, 0x01])
    runaway_offset = 0x350555
    runaway_bytes = bytearray([0x03, 0x81, 0x08, 0x0D, 0x00, 0x00])

    def get_patch(self):
        patch = super().get_patch()

        if self.world.starting_character == self.index and self.world.settings.is_flag_enabled(flags.PlayAsStarter):
            if self.palette is None:
                mapbytes = palette_to_bytes(["F8F8F8", "F8F850", "F0C830", "B83810", "503818", "38A830", "207820", "184810", "202818", "C88020", "884820", "201008", "909080", "606040", "181818"])
                patch.add_data(map_palette_offset, mapbytes)
                patch.add_data(0x37B0A4, self.default_palette_bytes)
            else:
                patch = self.special_palette([i for i in range(0,15)], map_palette_offset, patch)
                patch.add_data(0x37B0A4, palette_to_bytes(self.palette.colours))


        return patch

class Geno(Character):
    index = 3
    original_name = PlayableCharacters.geno
    placeholder = "`GENO_NAME`"
    starting_level = 6
    max_hp = 20
    speed = 30
    attack = 24
    defense = 6
    magic_attack = 3
    magic_defense = 5
    learned_spells = {
        6: spells.GenoBeam,
        8: spells.GenoBoost,
        11: spells.GenoWhirl,
        14: spells.GenoBlast,
        17: spells.GenoFlash,
    }

    # Vanilla levelup stat growths
    # (hp, attack, defense, m.attack, m.defense)
    starting_growths = (
        (3, 6, 3, 3, 2),
        (4, 6, 3, 3, 2),
        (4, 6, 3, 3, 2),
        (4, 6, 3, 3, 2),
        (4, 6, 3, 4, 2),
        # Vanilla growths
        (8, 5, 3, 4, 2),
        (8, 5, 3, 4, 2),
        (8, 5, 3, 4, 2),
        (8, 5, 3, 4, 2),
        (8, 5, 4, 4, 3),
        (8, 5, 4, 4, 3),
        (8, 5, 4, 4, 3),
        (8, 5, 4, 4, 3),
        (8, 5, 4, 4, 3),
        (8, 5, 4, 5, 3),
        (8, 5, 4, 5, 3),
        (8, 6, 4, 5, 3),
        (8, 6, 4, 5, 3),
        (8, 6, 4, 5, 3),
        (1, 2, 3, 2, 2),
        (1, 2, 3, 2, 2),
        (1, 2, 3, 2, 2),
        (1, 2, 3, 2, 2),
        (1, 2, 3, 2, 2),
        (1, 2, 3, 2, 2),
        (1, 2, 3, 2, 2),
        (1, 2, 3, 2, 2),
        (1, 2, 3, 2, 2),
        (1, 2, 3, 2, 2),
    )

    # Vanilla levelup stat bonus options
    # (hp, attack, defense, m.attack, m.defense)
    starting_bonuses = (
        (5, 1, 1, 3, 1),
        (5, 3, 1, 1, 1),
        (6, 1, 1, 1, 1),
        (5, 1, 1, 3, 1),
        (5, 3, 1, 1, 1),
        (6, 1, 1, 1, 1),
        (5, 1, 1, 3, 1),
        (5, 3, 1, 1, 1),
        (6, 1, 1, 1, 1),
        (5, 1, 1, 3, 1),
        (5, 3, 1, 1, 1),
        (6, 1, 1, 1, 1),
        (5, 1, 1, 3, 1),
        (5, 3, 1, 1, 1),
        (6, 1, 1, 1, 1),
        (5, 1, 1, 3, 1),
        (5, 3, 1, 1, 1),
        (6, 1, 1, 1, 1),
        (5, 1, 1, 3, 1),
        (1, 3, 1, 1, 1),
        (2, 1, 1, 1, 1),
        (1, 1, 1, 3, 1),
        (1, 3, 1, 1, 1),
        (2, 1, 1, 1, 1),
        (1, 1, 1, 3, 1),
        (1, 3, 1, 1, 1),
        (2, 1, 1, 1, 1),
        (1, 1, 1, 3, 1),
        (1, 3, 1, 1, 1),
    )
    forest_maze_sprite_id = 0x13
    mway_3_npc_id = [0x13, 0xB0]
    mway_2_npc_id = [0x13, 0x70]
    mway_1_npc_id = [0x13, 0x40]
    moleville_sprite_id = 0x12
    ending_palettes = (0x37AA14, 0x37B392)
    default_palette_bytes = bytearray([0xFF, 0x7F, 0x7E, 0x33, 0x18, 0x1A, 0x30, 0x0D, 0xA8, 0x08, 0x00, 0x7F, 0x40, 0x72, 0xC0, 0x69, 0x20, 0x3D, 0x1F, 0x03, 0x5F, 0x01, 0x8D, 0x0C, 0x96, 0x4A, 0x8D, 0x39, 0x63, 0x0C])
    default_underwater_palette_bytes = bytearray([0xD6, 0x66, 0x95, 0x36, 0x91, 0x25, 0x0C, 0x1D, 0xA6, 0x18, 0xE1, 0x65, 0x61, 0x5D, 0x01, 0x59, 0xA1, 0x34, 0x56, 0x16, 0x16, 0x15, 0x8A, 0x1C, 0xF0, 0x45, 0x4A, 0x39, 0x63, 0x0C])
    
    dialog_replacements = [
        (659,''' You can't get inside Booster's
 Tower very easily. You'll need
 a pretty strong gun for that.[await]''')
    ]

    original_weapon_sprite_ids = [25, None, 26, 27, 28, 29, 30]
    sprite_ids_as_main_character = [0, 1, 2, 3, 4, 5, 634]
    sprite_addresses = [[], None, [0x35FF28, 0x35BC59, 0x35CDBA], [], [0x35F93C, 0x35ED4F, 0x35F976, 0x35EF58], [0x35FF82, 0x35EDF3, 0x35EEAD, 0x35EFF5, 0x35F09A, 0x35B4F5, 0x35BAAD], [0x35BC4A, 0x35911C]] # not building an assembler for this in this version

    battle_sprite_offset = 0x020228
    battle_sprite_id = 0x1A
    menu_sprite_offset = 0x0318A6
    menu_sprite_id = 0x1A
    abxy_coord_offset = 0x02368B
    abxy_coord = 0xC0
    cursor_coord_offset = 0x029755
    cursor_coord = 0x13
    portrait_sprite_offset = 0x24126
    portrait_id = 0x2C
    item_use_offset = 0x358BBC
    item_use_bytes = bytearray([0x03, 0x81, 0x00, 0x1E, 0x00, 0x01])
    runaway_offset = 0x35055C
    runaway_bytes = bytearray([0x03, 0x81, 0x08, 0x19, 0x00, 0x00])

    def get_patch(self):
        patch = super().get_patch()

        if self.world.starting_character == self.index and self.world.settings.is_flag_enabled(flags.PlayAsStarter):
            if self.palette is None:
                classicbytes = palette_to_bytes(["804818", "0090E0", "F0D860", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000", "000000"])
                patch.add_data(classic_palette_offset, classicbytes)
                mapbytes = palette_to_bytes(["F8F8F8", "F0D860", "C08030", "804818", "402810", "00C0F8", "0090E0", "0070D0", "004878", "F8C000", "F85000", "682018", "B0A090", "686070", "181818"])
                patch.add_data(map_palette_offset, mapbytes)
                patch.add_data(0x37B0A4, self.default_palette_bytes)
            else:
                patch = self.special_palette([3, 6, 1, None, None, None, None, None, None, None, None, None, None, None, None], classic_palette_offset, patch)
                patch = self.special_palette([i for i in range(0,15)], map_palette_offset, patch)
                patch.add_data(0x37B0A4, palette_to_bytes(self.palette.colours))


        return patch

class Mallow(Character):
    index = 4
    original_name = PlayableCharacters.mallow
    placeholder = "`MALLOW_NAME`"
    starting_level = 2
    max_hp = 16
    speed = 18
    attack = 20
    defense = 0
    magic_attack = 11
    magic_defense = 7
    learned_spells = {
        2: spells.Thunderbolt,
        3: spells.HPRain,
        6: spells.Psychopath,
        10: spells.Shocker,
        14: spells.Snowy,
        18: spells.StarRain,
    }

    # Vanilla levelup stat growths
    # (hp, attack, defense, m.attack, m.defense)
    starting_growths = (
        (4, 2, 3, 2, 2),
        # Vanilla growths
        (4, 2, 3, 2, 2),
        (4, 2, 3, 2, 2),
        (4, 2, 3, 3, 2),
        (5, 2, 3, 3, 2),
        (5, 3, 3, 3, 2),
        (5, 3, 3, 4, 2),
        (6, 3, 3, 4, 3),
        (6, 3, 3, 4, 3),
        (6, 4, 3, 4, 3),
        (7, 4, 3, 5, 3),
        (7, 4, 3, 5, 3),
        (7, 4, 3, 5, 3),
        (8, 5, 3, 5, 3),
        (8, 5, 3, 5, 3),
        (8, 5, 3, 5, 3),
        (9, 5, 3, 5, 4),
        (9, 6, 3, 5, 4),
        (9, 6, 3, 5, 4),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
        (2, 2, 2, 2, 2),
    )

    # Vanilla levelup stat bonus options
    # (hp, attack, defense, m.attack, m.defense)
    starting_bonuses = (
        (4, 1, 1, 2, 1),
        (4, 3, 1, 1, 1),
        (6, 1, 1, 1, 1),
        (4, 1, 1, 2, 1),
        (4, 3, 1, 1, 1),
        (6, 1, 1, 1, 1),
        (4, 1, 1, 2, 1),
        (4, 3, 1, 1, 1),
        (6, 1, 1, 1, 1),
        (4, 1, 1, 2, 1),
        (4, 3, 1, 1, 1),
        (6, 1, 1, 1, 1),
        (4, 1, 1, 2, 1),
        (4, 3, 1, 1, 1),
        (6, 1, 1, 1, 1),
        (4, 1, 1, 2, 1),
        (4, 3, 1, 1, 1),
        (6, 1, 1, 1, 1),
        (4, 1, 1, 2, 1),
        (1, 3, 1, 1, 1),
        (2, 1, 1, 1, 1),
        (1, 1, 1, 2, 1),
        (1, 3, 1, 1, 1),
        (2, 1, 1, 1, 1),
        (1, 1, 1, 2, 1),
        (1, 3, 1, 1, 1),
        (2, 1, 1, 1, 1),
        (1, 1, 1, 2, 1),
        (1, 3, 1, 1, 1),
    )
    forest_maze_sprite_id = 0x0F
    mway_3_npc_id = [0x0F, 0xB0]
    mway_2_npc_id = [0x0F, 0x70]
    mway_1_npc_id = [0x0F, 0x40]
    moleville_sprite_id = 0x0E
    ending_palettes = (0x37A9F6, 0x37B374)
    default_palette_bytes = bytearray([0xFF, 0x7F, 0xDE, 0x4B, 0x7B, 0x3F, 0x94, 0x2E, 0xE8, 0x14, 0xBF, 0x69, 0xB2, 0x24, 0x8B, 0x1C, 0x26, 0x08, 0xA5, 0x7F, 0x43, 0x5E, 0x42, 0x31, 0x34, 0x46, 0xAD, 0x25, 0x63, 0x0C])
    default_underwater_palette_bytes = bytearray([0xB5, 0x7A, 0x94, 0x56, 0x52, 0x4E, 0xAD, 0x41, 0xA5, 0x30, 0x35, 0x69, 0x6C, 0x3C, 0x67, 0x38, 0x24, 0x28, 0x63, 0x7A, 0x82, 0x61, 0xE1, 0x44, 0x6D, 0x51, 0x29, 0x3D, 0x63, 0x0C])
    

    dialog_replacements = [
        (659,''' You can't get inside Booster's
 Tower very easily. You'll need
 some pretty magical fluff for that.[await]''')
    ]

    original_weapon_sprite_ids = [19, None, 20, 21, 22, 23, 24]
    sprite_ids_as_main_character = [0, 1, 2, 3, 4, 5, 6]
    sprite_addresses = [[], None, [0x35FF2F, 0x35CDC3], [], [0x35ED66, 0x35ED5D, 0x35EEC4, 0x35EEBB, 0x35F003, 0x35F00C, 0x35FF89], [0x35EDB0, 0x35EDA1, 0x35EE17, 0x35EE08, 0x35EF7E, 0x35EF6D, 0x35F0BE, 0x35F0AF], []] # not building an assembler for this in this version
    standard_sprite_addresses = [0x35FF2F]

    battle_sprite_offset = 0x020229
    battle_sprite_id = 0x14
    menu_sprite_offset = 0x0318A7
    menu_sprite_id = 0x14
    abxy_coord_offset = 0x02368D
    abxy_coord = 0xC4
    cursor_coord_offset = 0x029756
    cursor_coord = 0x12
    portrait_sprite_offset = 0x24127
    portrait_id = 0x2B
    item_use_offset = 0x358C5F
    item_use_bytes = bytearray([0x03, 0x81, 0x00, 0x18, 0x00, 0x02])
    runaway_offset = 0x350563
    runaway_bytes = bytearray([0x03, 0x81, 0x08, 0x13, 0x00, 0x00])

    def get_patch(self):
        patch = super().get_patch()

        if self.world.starting_character == self.index and self.world.settings.is_flag_enabled(flags.PlayAsStarter):
            if self.palette is None:
                mapbytes = palette_to_bytes(["F8F8F8", "F0F090", "D8D878", "A0A058", "403828", "F868D0", "902848", "582038", "300810", "28E8F8", "1890B8", "105060", "A08888", "686848", "181818"])
                patch.add_data(map_palette_offset, mapbytes)
                patch.add_data(0x37B0A4, self.default_palette_bytes)
            else:
                patch = self.special_palette([i for i in range(0,15)], map_palette_offset, patch)
                patch.add_data(0x37B0A4, palette_to_bytes(self.palette.colours))

        return patch

def get_default_characters(world):
    """Get default vanilla character list for the world.

    Args:
        world (randomizer.logic.main.GameWorld):

    Returns:
        list[Character]: List of default character objects.

    """
    return [
        Mario(world),
        Mallow(world),
        Geno(world),
        Bowser(world),
        Peach(world),
    ]
