# Boss/star piece randomization data for open mode.

from enum import IntEnum, Enum, auto

from randomizer.logic import utils
from randomizer.logic.patch import Patch

from randomizer.data.npcmodels import models
from randomizer.data.npcmodeltables import SpriteName, VramStore, ShadowSize
from randomizer.data.roomobjecttables import Rooms

from randomizer.logic.flags import AvailableBosses


class Battlefields(IntEnum):
    """Enumeration for ID values for battlefields."""
    Bowyer = 0x01
    KingCalamari = 0x03
    SunkenShip = 0x04
    MolevilleMines = 0x05
    BowsersKeep = 0x07
    CzarDragon = 0x08
    MushroomWay = 0x09
    BoosterTower = 0x0c
    MushroomKingdomThroneRoom = 0x0f
    Exor = 0x10
    ClownBros = 0x11
    Countdown = 0x12
    Gate = 0x13
    KeroSewers = 0x15
    NimbusCastle = 0x16
    Birdo = 0x17
    Valentina = 0x18
    Boomer = 0x1d
    Bundt = 0x23
    Yaridovich = 0x25
    AxemRangers = 0x27
    CloakerDomino = 0x28
    BeanValley = 0x29
    BelomeTemple = 0x2a
    Smithy = 0x2c
    JinxDojo = 0x2e
    Culex = 0x2f
    Factory = 0x30


class BattleMusic(IntEnum):
    """Enumeration for ID values for battle music."""
    Normal = 0x01
    Boss1 = 0x04
    Boss2 = 0x08
    Smithy = 0x0c
    Culex = 0x1c
    Corn = 0x10


class HenchmanType(Enum):
    Boss = auto()
    Pack = auto()
    Event = auto()
    ExternalEvent = auto()
    NPCOnly = auto()


class SpriteSize(Enum):
    Statue = auto()
    Small = auto()
    Large = auto()
    Attack = auto()


class Henchman:
    npcs = {}
    pack = None
    event_id = None
    henchman_type = None
    battle_type = None
    model_id = None
    sprite_offset = None
    sequence = None
    invert_directions = False


class Boss:
    pack = None
    identifier = None
    small_model_id = None
    small_model_sequence = 0
    small_model_sprite_offset = 0
    small_model_invert_directions = False
    big_model_details = None
    big_model_sequence = 0
    big_model_sprite_offset = 0
    attack_model_details = None
    forced_background = None
    unique_henchmen = []
    repeatable_henchmen = []


class ModelFill:
    room = None
    fill_type = None
    npc_id = None
    event_id = None 
    model_type = None
    minigames_only = False
    repeatable_allowed = True
    remove_if_empty = False
    occupant = None
    preferred_size = SpriteSize.Small

    def __init(self, fill_type, room_id, npc_id, event_id, occupant, preferred_size, minigames_only, repeatable_allowed, remove_if_empty):
        self.fill_type = fill_type
        self.room_id = room_id
        self.npc_id = npc_id
        self.event_id = event_id
        self.preferred_size = preferred_size
        self.occupant = occupant
        self.minigames_only = minigames_only
        self.repeatable_allowed = repeatable_allowed
        self.remove_if_empty = remove_if_empty

class BossModelFill(ModelFill):
    def __init__(self, room_id, npc_id, occupant, size, minigames_only):
        super().__init__(HenchmanType.Boss, room_id, npc_id, None, occupant, size, minigames_only, False, False)

class UniqueHenchmanFill(ModelFill):
    def __init__(self, room_id, npc_id, occupant, minigames_only, repeatable_allowed, remove_if_empty, fill_type, event_id=None):
        super().__init__(fill_type, room_id, npc_id, event_id, occupant, SpriteSize.Small, minigames_only, repeatable_allowed, remove_if_empty)

class RepeatableHenchmanFill(ModelFill):
    def __init__(self, room_id, npc_id, occupant, minigames_only, remove_if_empty, fill_type, event_id=None):
        super().__init__(fill_type, room_id, npc_id, event_id, occupant, SpriteSize.Small, minigames_only, True, remove_if_empty)


class StarLocation:
    """Class representing a star location."""

    # Star piece data
    star_address = 0x0
    has_star = False

    def __init__(self, world):
        """

        Args:
            world (randomizer.logic.main.GameWorld):

        """
        self.world = world

    def __str__(self):
        return "<{}: has_star {}>".format(self.name, self.has_star)

    def __repr__(self):
        return str(self)

    @property
    def name(self):
        return self.__class__.__name__

    def get_patch(self):
        """

        Returns:
            randomizer.logic.patch.Patch: Patch data

        """
        patch = Patch()

        # Zero for no star, or 255 if this boss has a star.
        val = 0xff if self.has_star else 0x00
        patch.add_data(self.star_address, utils.ByteField(val).as_bytes())

        return patch


class BossLocation:
    """Class for boss fight locations."""

    # Boss fight data
    battle_address = 0x0
    pack_number = 0
    battlefield = None
    can_run_away = False
    music = BattleMusic.Normal
    wide_sprite = False
    tall_sprite = False
    sprite_width = 32
    sprite_height = 32
    description = ""

    boss = None
    boss_locations = []
    unique_henchmen = []
    repeatable_henchmen_locations = []

    def __init__(self, world):
        """

        Args:
            world (randomizer.logic.main.GameWorld):

        """
        self.world = world

        # Get actual pack object based on the pack number.
        self.pack = self.world.get_formation_pack_by_index(self.pack_number)

    def __str__(self):
        return "<{}: music {}, members {}>".format(self.name, self.music, [m.enemy for m in self.formation.members])

    def __repr__(self):
        return str(self)

    @property
    def name(self):
        return self.__class__.__name__

    @property
    def formation(self):
        """Pack should be all the same formation for bosses, so get the object from the first item.

        Returns:
            randomizer.data.formations.EnemyFormation: Formation for this location.

        """
        return self.pack.formations[0]

    def get_patch(self):
        """

        Returns:
            randomizer.logic.patch.Patch: Patch data

        """
        patch = Patch()

        # Add boss data.
        data = bytearray()
        data += utils.ByteField(0x4a).as_bytes()
        data += utils.ByteField(self.pack.index).as_bytes()
        data += utils.ByteField(0x00).as_bytes()

        # If boss formation requires a specific battlefield, use that.  Otherwise use the location battlefield.
        if self.formation.required_battlefield is not None:
            data += utils.ByteField(self.formation.required_battlefield).as_bytes()
        else:
            data += utils.ByteField(self.battlefield).as_bytes()

        # Check for list of addresses if spot has multiple addresses that need to be set.
        if isinstance(self.battle_address, (list, tuple)):
            addrs = self.battle_address
        else:
            addrs = [self.battle_address]

        for addr in addrs:
            patch.add_data(addr, data)

        return patch


class BossAndStarLocation(StarLocation, BossLocation):
    """Subclass for star piece locations that are also boss fights."""

    def __init__(self, world):
        """

        Args:
            world (randomizer.logic.main.GameWorld):

        """
        StarLocation.__init__(self, world)
        BossLocation.__init__(self, world)

    def __str__(self):
        return "<{}: has_star {}, music {}, members {}>".format(
            self.name, self.has_star, self.music, [m.enemy for m in self.formation.members])

    def __repr__(self):
        return str(self)

    def get_patch(self):
        """

        Returns:
            randomizer.logic.patch.Patch: Patch data

        """
        patch = StarLocation.get_patch(self)
        patch += BossLocation.get_patch(self)
        return patch


class BowsersKeepLocation(BossAndStarLocation):
    """Container subclass for Bowser's Keep locations."""
    pass


class HammerBroBoss(Boss):
    pack = 183
    small_model_id = 488
    big_model_details = {
        "sprite": SpriteName._283_HAMMER_BRO,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": True,
        "shadow": ShadowSize._01_OVAL_MED,
        "y_pixel_shift": 1,
        "acute_axis": 8,
        "obtuse_axis": 7,
        "height": 19,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 3,
        "cannot_clone": True,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }
    big_sprite_width = 40
    big_sprite_height = 45


class Croco1Boss(Boss):
    pack = 163
    small_model_id = 48  # could be 42, 110, 367


class MackShyster1(Henchman):
    pack = 194
    model_id = 414


class MackShyster2(Henchman):
    pack = 195
    model_id = 414


class DefaultShyster1(Henchman):
    pack = 10
    model_id = 414


class DefaultShyster2(Henchman):
    pack = 11
    model_id = 414


class MackBoss(Boss):
    pack = 179
    small_model_id = 414
    big_model_details = {
        "sprite": SpriteName._480_MACK,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": True,
        "shadow": ShadowSize._02_OVAL_BIG,
        "y_pixel_shift": 1,
        "acute_axis": 13,
        "obtuse_axis": 13,
        "height": 23,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 3,
        "cannot_clone": True,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }
    big_model_sequence = 7  # note: remove from event 368
    big_sprite_height = 57
    big_sprite_width = 43
    unique_henchmen = [MackShyster1, MackShyster2, MackShyster1, MackShyster2]
    repeatable_henchmen = [MackShyster1, MackShyster2]


class PandoriteBoss(Boss):
    pack = 156
    small_model_id = 199  # could be 196 or 111
    small_model_sequence = 4
    big_model_details = {
        "sprite": SpriteName._279_PANDORITE,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": True,
        "shadow": ShadowSize._01_OVAL_MED,
        "y_pixel_shift": 3,
        "acute_axis": 7,
        "obtuse_axis": 7,
        "height": 12,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 1,
        "cannot_clone": False,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }
    original_boss = 199


class Belome1Boss(Boss):
    pack = 168
    small_model_id = 385
    small_model_invert_directions = True
    big_model_details = {
        "sprite": SpriteName._455_BELOME_1ST_TIME,
        "priority_0": True,
        "priority_1": True,
        "priority_2": False,
        "show_shadow": False,
        "shadow": ShadowSize._00_OVAL_SMALL,
        "y_pixel_shift": 2,
        "acute_axis": 10,
        "obtuse_axis": 10,
        "height": 18,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 5,
        "cannot_clone": False,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }
    big_sprite_height = 54
    big_sprite_width = 49


class BowyerAero(Henchman):
    pack = 205
    model_id = 487
    sequence = 1


class BowyerBoss(Boss):
    pack = 181
    small_model_id = 487
    small_model_sequence = 1
    big_model_details = {
        "sprite": SpriteName._241_BOWYER,
        "priority_0": False,
        "priority_1": False,
        "priority_2": False,
        "show_shadow": False,
        "shadow": ShadowSize._00_OVAL_SMALL,
        "y_pixel_shift": 0,
        "acute_axis": 0,
        "obtuse_axis": 0,
        "height": 0,
        "vram_store": VramStore._00_SWSE_NWNE,
        "vram_size": 0,
        "cannot_clone": False,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }
    big_sprite_height = 52
    big_sprite_width = 47
    attack_model_details = {
        "sprite": SpriteName._486_BOWYER,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": False,
        "shadow": ShadowSize._00_OVAL_SMALL,
        "y_pixel_shift": 1,
        "acute_axis": 6,
        "obtuse_axis": 8,
        "height": 16,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 3,
        "cannot_clone": True,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }
    unique_henchmen = [BowyerAero, BowyerAero, BowyerAero,
                       BowyerAero, BowyerAero, BowyerAero, BowyerAero, BowyerAero]
    repeatable_henchmen = [BowyerAero]


class Croco2Crook(Henchman):
    pack = 141
    model_id = 261


class DefaultCrook(Henchman):
    pack = 199
    model_id = 261


class Croco2Boss(Boss):
    pack = 164
    small_model_id = 48  # could be 42, 110, 367
    unique_henchmen = [Croco2Crook, Croco2Crook, Croco2Crook]
    repeatable_henchmen = [Croco2Crook]


class PunchinelloBobomb(Henchman):
    pack = 1
    model_id = 145  # maybe 281



class DefaultMicrobomb(Henchman):
    pack = None
    model_id = 37  # maybe 440

class DefaultBobomb(Henchman):
    pack = 36
    model_id = 145  # maybe 281


class PunchinelloBoss(Boss):
    pack = 140
    small_model_id = 145  # maybe 281
    big_model_details = {
        "sprite": SpriteName._464_PUNCHINELLO,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": False,
        "shadow": ShadowSize._00_OVAL_SMALL,
        "y_pixel_shift": 1,
        "acute_axis": 11,
        "obtuse_axis": 8,
        "height": 19,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 2,
        "cannot_clone": True,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }
    big_sprite_height = 45
    big_sprite_width = 45
    unique_henchmen = [PunchinelloBobomb, PunchinelloBobomb,
                       PunchinelloBobomb, PunchinelloBobomb]
    repeatable_henchmen = [PunchinelloBobomb]


class BoosterSnifit(Henchman):
    pack = 0
    model_id = 36  # maybe 504 or 505; or 38 or 224 for back-facing


class DefaultSnifit(Henchman):
    pack = 142
    model_id = 36  # maybe 504 or 505; or 38 or 224 for back-facing


class BoosterApprentice(Henchman):
    pack = 32
    model_id = 384  # maybe 282


class BoosterBoss(Boss):
    pack = 161
    small_model_id = 50
    unique_henchmen = [BoosterSnifit, BoosterSnifit, BoosterSnifit]
    repeatable_henchmen = [BoosterApprentice]


class GrateGuyKnifeGuy(Henchman):  # What to do with this? Can't have a pack
    pack = None
    small_model_id = 134


class GrateGuyBoss(Boss):
    pack = 177
    small_model_id = 452
    big_model_details = {
        "sprite": SpriteName._449_GRATE_GUY,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": False,
        "shadow": ShadowSize._00_OVAL_SMALL,
        "y_pixel_shift": 1,
        "acute_axis": 11,
        "obtuse_axis": 11,
        "height": 13,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 3,
        "cannot_clone": False,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }
    unique_henchmen = [GrateGuyKnifeGuy]


class BundtTorte1(Henchman):
    pack = 54
    small_model_id = 398  # maybe 397


class BundtTorte2(Henchman):
    pack = 55
    small_model_id = 398  # maybe 397


class BundtBoss(Boss):
    pack = 176
    small_model_id = 470
    big_model_details = {
        "sprite": SpriteName._450_BUNDT,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": True,
        "shadow": ShadowSize._02_OVAL_BIG,
        "y_pixel_shift": 1,
        "acute_axis": 13,
        "obtuse_axis": 13,
        "height": 23,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 3,
        "cannot_clone": True,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }
    unique_henchmen = [BundtTorte1, BundtTorte2]
    repeatable_henchmen = [BundtTorte1, BundtTorte2]


class KingCalamariBloober(Henchman):
    pack = 204
    model_id = 266  # maybe 172 or 173


class KingCalamariBoss(Boss):
    pack = 167
    forced_background = 35
    small_model_id = 266
    repeatable_henchmen = [KingCalamariBloober]


class HidonGoombette(Henchman):
    pack = 221
    model_id = 349
    small = True


class HidonBoss(Boss):
    pack = 157
    small_model_id = 199  # could be 196 or 111
    small_model_sequence = 4
    big_model_details = {
        "sprite": SpriteName._343_HIDON,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": True,
        "shadow": ShadowSize._01_OVAL_MED,
        "y_pixel_shift": 3,
        "acute_axis": 7,
        "obtuse_axis": 7,
        "height": 12,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 1,
        "cannot_clone": False,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }
    unique_henchmen = [HidonGoombette, HidonGoombette,
                       HidonGoombette, HidonGoombette]
    repeatable_henchmen = [HidonGoombette]


class DefaultBandanaRed1(Henchman):
    pack = 68
    model_id = 267


class DefaultBandanaRed2(Henchman):
    pack = 69
    model_id = 267


class JohnnyBandanaRed(Henchman):
    pack = 71
    model_id = 267


class JohnnyBandanaBlue(Henchman):
    pack = 70
    model_id = 331


class JohnnyBoss(Boss):
    pack = 166
    small_model_id = 55  # maybe 52
    big_model_details = {
        "sprite": SpriteName._505_JOHNNY,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": True,
        "shadow": ShadowSize._02_OVAL_BIG,
        "y_pixel_shift": 1,
        "acute_axis": 13,
        "obtuse_axis": 13,
        "height": 23,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 3,
        "cannot_clone": True,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }
    unique_henchmen = [JohnnyBandanaBlue, JohnnyBandanaBlue,
                       JohnnyBandanaBlue, JohnnyBandanaBlue]
    repeatable_henchmen = [JohnnyBandanaRed]


class YaridovichHenchman(Henchman):
    pack = 153
    model_id = 39


class YaridovichBoss(Boss):
    pack = 180
    small_model_id = 40
    big_model_details = {
        "sprite": SpriteName._482_YARIDOVICH,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": True,
        "shadow": ShadowSize._02_OVAL_BIG,
        "y_pixel_shift": 1,
        "acute_axis": 13,
        "obtuse_axis": 13,
        "height": 23,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 3,
        "cannot_clone": True,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }
    unique_henchmen = [YaridovichHenchman, YaridovichHenchman,
                       YaridovichHenchman, YaridovichHenchman]
    repeatable_henchmen = [YaridovichHenchman]


class MokuraBoss(Boss):
    pack = 207
    small_model_id = 201
    big_model_details = {
        "sprite": SpriteName._573_MOKURA,
        "priority_0": True,
        "priority_1": True,
        "priority_2": False,
        "show_shadow": False,
        "shadow": ShadowSize._00_OVAL_SMALL,
        "y_pixel_shift": 2,
        "acute_axis": 10,
        "obtuse_axis": 10,
        "height": 18,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 5,
        "cannot_clone": False,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }
    big_sprite_height = 38
    big_sprite_width = 48


class Belome2Boss(Boss):
    pack = 169
    small_model_id = 385
    small_model_invert_directions = True
    big_model_details = {
        "sprite": SpriteName._455_BELOME_1ST_TIME,
        "priority_0": True,
        "priority_1": True,
        "priority_2": False,
        "show_shadow": False,
        "shadow": ShadowSize._00_OVAL_SMALL,
        "y_pixel_shift": 2,
        "acute_axis": 10,
        "obtuse_axis": 10,
        "height": 18,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 5,
        "cannot_clone": False,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }
    big_sprite_height = 54
    big_sprite_width = 49


class JaggerBoss(Boss):
    pack = 189
    small_model_id = 237  # could be 156 or 256, or maybe 206 but prob not


class Jinx1Boss(Boss):
    pack = 178
    small_model_id = 207  # could be 415 or 416


class Jinx2Boss(Boss):
    pack = 187
    small_model_id = 415  # could be 207 or 416


class Jinx3Boss(Boss):
    pack = 188
    small_model_id = 416  # could be 207 or 415


class CulexFireCrystal(Henchman):
    pack = 217
    model_id = 386
    sequence = 1


class CulexWaterCrystal(Henchman):
    pack = 218
    model_id = 435


class CulexEarthCrystal(Henchman):
    pack = 219
    model_id = 435
    sequence = 1


class CulexWindCrystal(Henchman):
    pack = 220
    model_id = 386


class CulexBoss(Boss):
    pack = 216
    small_model_id = 511
    small_model_sequence = 8
    big_model_details = {
        "sprite": SpriteName._511_CULEX,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": True,
        "shadow": ShadowSize._01_OVAL_MED,
        "y_pixel_shift": 1,
        "acute_axis": 16,
        "obtuse_axis": 16,
        "height": 31,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 0,
        "cannot_clone": True,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }
    unique_henchmen = [CulexFireCrystal, CulexWaterCrystal,
                       CulexEarthCrystal, CulexWindCrystal]


class BoxBoyBoss(Boss):
    pack = 158
    small_model_id = 199  # could be 196 or 111
    small_model_sequence = 4
    big_model_details = {
        "sprite": SpriteName._390_BOX_BOY,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": True,
        "shadow": ShadowSize._01_OVAL_MED,
        "y_pixel_shift": 3,
        "acute_axis": 7,
        "obtuse_axis": 7,
        "height": 12,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 1,
        "cannot_clone": False,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }


class MegaSmilaxPiranha(Henchman):
    pack = 222
    model_id = 263  # could be 138


class MegaSmilaxBoss(Boss):
    pack = 173
    small_model_id = 263  # could be 138
    big_model_details = {
        "sprite": SpriteName._460_MEGASMILAX,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": False,
        "shadow": ShadowSize._00_OVAL_SMALL,
        "y_pixel_shift": 1,
        "acute_axis": 11,
        "obtuse_axis": 11,
        "height": 13,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 3,
        "cannot_clone": False,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }
    repeatable_henchmen = [MegaSmilaxPiranha]


class DodoBoss(Boss):
    pack = 208
    small_model_id = 131
    small_model_sequence = 2
    big_model_details = {
        "sprite": SpriteName._393_DODO,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": False,
        "shadow": ShadowSize._00_OVAL_SMALL,
        "y_pixel_shift": 1,
        "acute_axis": 7,
        "obtuse_axis": 7,
        "height": 13,
        "vram_store": VramStore._00_SWSE_NWNE,
        "vram_size": 0,
        "cannot_clone": False,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": True,
        "byte5_bit7": True,
        "byte6_bit2": True
    }  # could be 21 or 312
    big_sprite_height = 56
    big_sprite_width = 46


class BirdettaEggbert(Henchman):
    pack = 223
    model_id = 462


class BirdettaBoss(Boss):
    pack = 175
    small_model_id = 462
    big_model_details = {
        "sprite": SpriteName._461_BIRDO,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": True,
        "shadow": ShadowSize._02_OVAL_BIG,
        "y_pixel_shift": 1,
        "acute_axis": 9,
        "obtuse_axis": 11,
        "height": 23,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 4,
        "cannot_clone": False,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }
    repeatable_henchmen = [BirdettaEggbert]


class DefaultBluebird1(Henchman):
    pack = 94
    model_id = 333  # maybe 334


class DefaultBluebird2(Henchman):
    pack = 95
    model_id = 333  # maybe 334


class DefaultBirdy1(Henchman):
    pack = 92
    model_id = 183  # maybe 269 or 279


class DefaultBirdy2(Henchman):
    pack = 93
    model_id = 183  # maybe 269 or 279


class ValentinaBluebird(Henchman):
    pack = 160
    model_id = 333  # maybe 334


class ValentinaBirdy(Henchman):
    pack = 201
    model_id = 183  # maybe 269 or 279


class ValentinaBoss(Boss):
    pack = 171
    small_model_id = 56
    statue_model_id = 63
    big_model_details = {
        "sprite": SpriteName._507_VALENTINA,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": True,
        "shadow": ShadowSize._02_OVAL_BIG,
        "y_pixel_shift": 1,
        "acute_axis": 13,
        "obtuse_axis": 13,
        "height": 23,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 3,
        "cannot_clone": True,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }
    repeatable_henchmen = [ValentinaBluebird, ValentinaBirdy]


class CzarPyrosphere(Henchman):
    pack = 190
    model_id = 155  # maybe 277. these are the exact same, could free one up


class CzarBoss(Boss):
    pack = 172
    small_model_id = 56
    big_model_details = {
        "sprite": SpriteName._476_CZAR_DRAGON,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": False,
        "shadow": ShadowSize._00_OVAL_SMALL,
        "y_pixel_shift": 0,
        "acute_axis": 1,
        "obtuse_axis": 1,
        "height": 1,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 3,
        "cannot_clone": True,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }
    large_sprite_width = 59
    large_sprite_height = 54
    repeatable_henchmen = [CzarPyrosphere]


class AxemRangersAxemBlack(Henchman):
    pack = 248
    model_id = 209


class AxemRangersAxemPink(Henchman):
    pack = 249
    model_id = 210


class AxemRangersAxemYellow(Henchman):
    pack = 250
    model_id = 211  # 463 is a clone, could free up


class AxemRangersAxemGreen(Henchman):
    pack = 251
    model_id = 212  # 467 is a clone, could free up


class AxemRangersMachine1(Henchman):
    pack = 203
    model_id = 185


class AxemRangersMachine2(Henchman):
    pack = 203
    model_id = 422

# Maybe add models for the other three


class AxemRangersBoss(Boss):
    pack = 188
    small_model_id = 208  # could be 466
    unique_henchmen = [AxemRangersAxemBlack, AxemRangersAxemPink,
                       AxemRangersAxemYellow, AxemRangersAxemGreen]
    repeatable_henchmen = [AxemRangersMachine1, AxemRangersMachine2]


class ChesterBoss(Boss):
    pack = 235
    small_model_id = 199  # could be 196 or 111
    small_model_sequence = 4
    big_model_details = {
        "sprite": SpriteName._395_CHESTER,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": True,
        "shadow": ShadowSize._01_OVAL_MED,
        "y_pixel_shift": 3,
        "acute_axis": 7,
        "obtuse_axis": 7,
        "height": 12,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 1,
        "cannot_clone": False,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }


class MagikoopaBoss(Boss):
    pack = 209
    small_model_id = 190
    big_model_details = {
        "sprite": SpriteName._353_MERLIN,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": True,
        "shadow": ShadowSize._02_OVAL_BIG,
        "y_pixel_shift": 1,
        "acute_axis": 7,
        "obtuse_axis": 7,
        "height": 13,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 2,
        "cannot_clone": True,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }


class BoomerShyGuy(Henchman):
    pack = 200
    model_id = 159  # maybe 346


class BoomerBoss(Boss):
    pack = 210
    small_model_id = 159  # maybe 346
    big_model_details = {
        "sprite": SpriteName._169_BOOMER_RED,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": True,
        "shadow": ShadowSize._02_OVAL_BIG,
        "y_pixel_shift": 1,
        "acute_axis": 8,
        "obtuse_axis": 8,
        "height": 17,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 3,
        "cannot_clone": False,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }
    attack_model_details = {
        "sprite": SpriteName._308_BOOMER,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": True,
        "shadow": ShadowSize._02_OVAL_BIG,
        "y_pixel_shift": 2,
        "acute_axis": 9,
        "obtuse_axis": 9,
        "height": 22,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 3,
        "cannot_clone": True,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }
    big_sprite_width = 52
    big_sprite_width = 49
    unique_henchmen = [BoomerShyGuy, BoomerShyGuy]
    repeatable_henchmen = [BoomerShyGuy]


class ExorBoss(Boss):
    pack = 186
    forced_background = 16
    small_model_id = 0
    small_model_sprite_offset = 3
    small_model_sequence = 10
    # potentially, put sprite #3 on an unused NPC and don't worry about the sprite offset


class CountdownDingALing(Henchman):
    pack = 419
    model_id = 454


class CountdownBoss(Boss):
    pack = 174
    forced_background = 18
    small_model_id = 454
    unique_henchmen = [CountdownDingALing, CountdownDingALing]
    repeatable_henchmen = [CountdownDingALing]


class CloakerDominoBoss(Boss):
    pack = 184
    forced_background = 40
    small_model_id = 429  # maybe 249
    big_model_details = {
        "sprite": SpriteName._477_CLOAKER_1ST_TIME,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": True,
        "shadow": ShadowSize._02_OVAL_BIG,
        "y_pixel_shift": 1,
        "acute_axis": 8,
        "obtuse_axis": 8,
        "height": 17,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 3,
        "cannot_clone": False,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }


class DefaultMadMallet(Henchman):
    pack = 150
    model_id = 259


class ClerkMadMallet(Henchman):
    pack = 202
    model_id = 259


class ClerkBoss(Boss):
    pack = 146
    small_model_id = 446
    big_model_details = {
        "sprite": SpriteName._306_CLERK,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": False,
        "shadow": ShadowSize._00_OVAL_SMALL,
        "y_pixel_shift": 1,
        "acute_axis": 7,
        "obtuse_axis": 7,
        "height": 13,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 7,
        "cannot_clone": True,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }
    unique_henchmen = [ClerkMadMallet, ClerkMadMallet]
    repeatable_henchmen = [ClerkMadMallet]


class ManagerPounder(Henchman):
    pack = 126
    model_id = 323


class ManagerBoss(Boss):
    pack = 147
    small_model_id = 493
    big_model_details = {
        "sprite": SpriteName._332_MANAGER,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": False,
        "shadow": ShadowSize._00_OVAL_SMALL,
        "y_pixel_shift": 1,
        "acute_axis": 7,
        "obtuse_axis": 7,
        "height": 13,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 7,
        "cannot_clone": True,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }
    unique_henchmen = [ManagerPounder, ManagerPounder,
                       ManagerPounder, ManagerPounder]
    repeatable_henchmen = [ManagerPounder]


class DirectorPoundette(Henchman):
    pack = 128
    model_id = 324  # maybe 477


class DirectorBoss(Boss):
    pack = 148
    small_model_id = 497
    big_model_details = {
        "sprite": SpriteName._332_MANAGER,
        "priority_0": False,
        "priority_1": False,
        "priority_2": True,
        "show_shadow": False,
        "shadow": ShadowSize._00_OVAL_SMALL,
        "y_pixel_shift": 1,
        "acute_axis": 7,
        "obtuse_axis": 7,
        "height": 13,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 7,
        "cannot_clone": True,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }
    unique_henchmen = [DirectorPoundette, DirectorPoundette,
                       DirectorPoundette, DirectorPoundette]
    repeatable_henchmen = [DirectorPoundette]

class DefaultUnpaintedDrillBit(Henchman):
    pack = None
    model_id = 402

class DefaultPaintedDrillBit(Henchman):
    pack = None
    model_id = 351

class GunyolkBoss(Boss):
    pack = 149
    small_model_id = 484


class SmithyDrillBit(Henchman):
    pack = 253
    model_id = 483


class SmithyShyster(Henchman):
    pack = 254
    model_id = 401


class SmithyAero(Henchman):
    pack = 255
    model_id = 487
    sequence = 1


class SmithyBoss(Boss):
    pack = 185
    small_model_id = 351
    big_model_details = {
        "sprite": SpriteName._947_SMITHY,
        "priority_0": True,
        "priority_1": True,
        "priority_2": False,
        "show_shadow": False,
        "shadow": ShadowSize._00_OVAL_SMALL,
        "y_pixel_shift": 2,
        "acute_axis": 10,
        "obtuse_axis": 10,
        "height": 18,
        "vram_store": VramStore._02_SWSE,
        "vram_size": 5,
        "cannot_clone": False,
        "byte2_bit0": False,
        "byte2_bit1": False,
        "byte2_bit2": False,
        "byte2_bit3": False,
        "byte2_bit4": False,
        "byte5_bit6": False,
        "byte5_bit7": False,
        "byte6_bit2": False
    }
    unique_henchmen = [SmithyDrillBit, SmithyShyster, SmithyAero]
    repeatable_henchmen = [SmithyDrillBit, SmithyShyster, SmithyAero]


# ****************************** Actual location classes
class HammerBros(BossAndStarLocation):
    identifier = 205
    description = AvailableBosses.HammerBro
    name = "Hammer Bro"
    battlefield = Battlefields.MushroomWay
    music = BattleMusic.Boss1

    boss = HammerBroBoss
    boss_locations = [
        BossModelFill(Rooms._205_MUSHROOM_WAY_AREA_03, 7, HammerBroBoss, SpriteSize.Large, False)
    ]


class Croco1(BossAndStarLocation):
    identifier = 326
    description = AvailableBosses.Croco1
    name = "Croco"
    battlefield = Battlefields.MushroomWay
    music = BattleMusic.Boss1
    boss = Croco1Boss
    boss_locations = [
        BossModelFill(Rooms._076_BANDITS_WAY_AREA_01, 5, Croco1Boss, SpriteSize.Small, False),
        BossModelFill(Rooms._207_BANDITS_WAY_AREA_02, 8, Croco1Boss, SpriteSize.Small, False),
        BossModelFill(Rooms._077_BANDITS_WAY_AREA_03, 8, Croco1Boss, SpriteSize.Small, False),
        BossModelFill(Rooms._078_BANDITS_WAY_AREA_04, 12, Croco1Boss, SpriteSize.Small, False),
        BossModelFill(Rooms._206_BANDITS_WAY_AREA_05, 8, Croco1Boss, SpriteSize.Small, False)
    ]


class Mack(BossAndStarLocation):
    identifier = 326
    description = AvailableBosses.Mack
    name = "Mack"
    battlefield = Battlefields.MushroomKingdomThroneRoom
    music = BattleMusic.Boss2
    boss = MackBoss
    boss_locations = [
        BossModelFill(Rooms._326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM, 3, MackBoss, SpriteSize.Large, False)
    ]
    unique_henchmen = [
        [
            UniqueHenchmanFill(Rooms._326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM, 4, DefaultShyster1, False, True, False, HenchmanType.NPCOnly)
        ],
        [
            UniqueHenchmanFill(Rooms._326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM, 5, DefaultShyster1, False, True, False, HenchmanType.NPCOnly)
        ],
        [
            UniqueHenchmanFill(Rooms._326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM, 6, DefaultShyster1, False, True, False, HenchmanType.NPCOnly)
        ],
        [
            UniqueHenchmanFill(Rooms._326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM, 7, DefaultShyster1, False, True, False, HenchmanType.NPCOnly)
        ],
        [
            UniqueHenchmanFill(Rooms._326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM, 8, DefaultShyster1, True, True, False, HenchmanType.NPCOnly)
        ],
        [
            UniqueHenchmanFill(Rooms._326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM, 9, DefaultShyster1, True, True, False, HenchmanType.NPCOnly)
        ]
    ]
    repeatable_henchmen = [
        [
            RepeatableHenchmanFill(Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, 3, DefaultShyster1, False, False, HenchmanType.Pack),
            RepeatableHenchmanFill(Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, 5, DefaultShyster1, False, False, HenchmanType.Event, 1189),
            RepeatableHenchmanFill(Rooms._323_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_THRONE_ROOM, 0, DefaultShyster1, False, False, HenchmanType.Pack),
            RepeatableHenchmanFill(Rooms._325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL, 0, DefaultShyster1, False, False, HenchmanType.Event, 1186),
            RepeatableHenchmanFill(Rooms._325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL, 1, DefaultShyster1, False, False, HenchmanType.Event, 1187),
            RepeatableHenchmanFill(Rooms._325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL, 2, DefaultShyster1, False, False, HenchmanType.Event, 1188),
            RepeatableHenchmanFill(Rooms._325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL, 3, DefaultShyster1, False, False, HenchmanType.Pack),
            RepeatableHenchmanFill(Rooms._325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL, 4, DefaultShyster1, False, False, HenchmanType.Event, 1189),
            RepeatableHenchmanFill(Rooms._327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM, 0, DefaultShyster1, False, False, HenchmanType.Pack),
            RepeatableHenchmanFill(Rooms._329_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_BRANCH_ROOM_TO_VAULTGUEST_ROOM, 1, DefaultShyster1, False, False, HenchmanType.Pack),
            RepeatableHenchmanFill(Rooms._480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F, 4, DefaultShyster1, False, False, HenchmanType.Event, 1187),
        ],
        [
            RepeatableHenchmanFill(Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, 0, DefaultShyster2, False, False, HenchmanType.Event, 1186),
            RepeatableHenchmanFill(Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, 1, DefaultShyster2, False, False, HenchmanType.Event, 1187),
            RepeatableHenchmanFill(Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, 2, DefaultShyster2, False, False, HenchmanType.Event, 1188),
            RepeatableHenchmanFill(Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, 4, DefaultShyster2, False, False, HenchmanType.Pack),
            RepeatableHenchmanFill(Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, 6, DefaultShyster2, False, False, HenchmanType.Event, 1190),
            RepeatableHenchmanFill(Rooms._323_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_THRONE_ROOM, 1, DefaultShyster2, False, False, HenchmanType.Pack),
            RepeatableHenchmanFill(Rooms._327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM, 1, DefaultShyster2, False, False, HenchmanType.Event, 1186),
            RepeatableHenchmanFill(Rooms._329_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_BRANCH_ROOM_TO_VAULTGUEST_ROOM, 0, DefaultShyster2, False, False, HenchmanType.Pack),
            RepeatableHenchmanFill(Rooms._332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM, 0, DefaultShyster2, False, False, HenchmanType.ExternalEvent, 1186),
            RepeatableHenchmanFill(Rooms._332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM, 1, DefaultShyster2, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F, 3, DefaultShyster2, False, False, HenchmanType.Event, 1186),
            RepeatableHenchmanFill(Rooms._481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F, 1, DefaultShyster2, False, False, HenchmanType.Event, 1186),
        ]
    ]


class Pandorite(BossAndStarLocation):
    identifier = 512
    description = AvailableBosses.Pandorite
    name = "Pandorite"
    battlefield = Battlefields.KeroSewers
    boss = PandoriteBoss


class Belome1(BossAndStarLocation):
    identifier = 302
    battlefield = Battlefields.KeroSewers
    music = BattleMusic.Boss1
    description = AvailableBosses.Belome1
    name = "Belome"
    boss = Belome1Boss
    boss_locations = [
        BossModelFill(Rooms._302_KERO_SEWERS_AREA_08_BELOMES_ROOM, 3, Belome1Boss, SpriteSize.Large, False)
    ]


class Bowyer(BossAndStarLocation):
    identifier = 353
    description = AvailableBosses.Bowyer
    name = "Bowyer"
    battlefield = Battlefields.Bowyer
    music = BattleMusic.Boss2
    boss = BowyerBoss
    boss_locations = [
        BossModelFill(Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD, 11, BowyerBoss, SpriteSize.Large, False)
    ]
    unique_henchmen = [
        [
            UniqueHenchmanFill(Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD, 1, BowyerAero, False, False, True, HenchmanType.NPCOnly)
        ],
        [
            UniqueHenchmanFill(Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD, 7, BowyerAero, False, False, True, HenchmanType.NPCOnly)
        ],
        [
            UniqueHenchmanFill(Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD, 2, BowyerAero, False, False, True, HenchmanType.NPCOnly)
        ],
        [
            UniqueHenchmanFill(Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD, 8, BowyerAero, False, False, True, HenchmanType.NPCOnly)
        ],
        [
            UniqueHenchmanFill(Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD, 0, BowyerAero, False, False, True, HenchmanType.NPCOnly)
        ],
        [
            UniqueHenchmanFill(Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD, 6, BowyerAero, False, False, True, HenchmanType.NPCOnly)
        ],
        [
            UniqueHenchmanFill(Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD, 3, BowyerAero, False, False, True, HenchmanType.NPCOnly)
        ],
        [
            UniqueHenchmanFill(Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD, 9, BowyerAero, False, False, True, HenchmanType.NPCOnly)
        ],
        [
            UniqueHenchmanFill(Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD, 4, BowyerAero, False, False, True, HenchmanType.NPCOnly)
        ],
        [
            UniqueHenchmanFill(Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD, 5, BowyerAero, False, False, True, HenchmanType.NPCOnly)
        ]
    ]


class Croco2(BossAndStarLocation):
    identifier = 518
    description = AvailableBosses.Croco2
    name = "Croco"
    battlefield = Battlefields.MolevilleMines
    music = BattleMusic.Boss1
    boss = Croco2Boss
    boss_locations = [
        BossModelFill(Rooms._273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE, 0, Croco2Boss, SpriteSize.Small, False),
        BossModelFill(Rooms._277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM, 0, Croco2Boss, SpriteSize.Small, False),
        BossModelFill(Rooms._275_MOLEVILLE_MINES_AREA_06_SMALL_ROOM_LEADING_TO_AREA_06, 0, Croco2Boss, SpriteSize.Small, False),
        BossModelFill(Rooms._281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM, 0, Croco2Boss, SpriteSize.Small, False),
        BossModelFill(Rooms._279_MOLEVILLE_MINES_AREA_08_CROCOS_BOMBED_ROOM, 0, Croco2Boss, SpriteSize.Small, False),
        BossModelFill(Rooms._283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM, 0, Croco2Boss, SpriteSize.Small, False)
    ]
    unique_henchmen = [
        [
            UniqueHenchmanFill(Rooms._273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE, 1, DefaultCrook, False, True, False, HenchmanType.Event, 1186),
            UniqueHenchmanFill(Rooms._273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE, 2, DefaultCrook, False, True, False, HenchmanType.Event, 1186),
            UniqueHenchmanFill(Rooms._273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE, 3, DefaultCrook, False, True, False, HenchmanType.Event, 1186)
        ],
        [
            UniqueHenchmanFill(Rooms._277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM, 1, DefaultCrook, False, True, False, HenchmanType.Event, 1186),
            UniqueHenchmanFill(Rooms._277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM, 2, DefaultCrook, False, True, False, HenchmanType.Event, 1186),
            UniqueHenchmanFill(Rooms._277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM, 3, DefaultCrook, False, True, False, HenchmanType.Event, 1186)
        ],
        [
            UniqueHenchmanFill(Rooms._283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM, 1, DefaultCrook, False, True, False, HenchmanType.Event, 1186),
            UniqueHenchmanFill(Rooms._283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM, 2, DefaultCrook, False, True, False, HenchmanType.Event, 1186),
            UniqueHenchmanFill(Rooms._283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM, 3, DefaultCrook, False, True, False, HenchmanType.Event, 1186)
        ]
    ]


class Punchinello(BossAndStarLocation):
    identifier = 271
    description = AvailableBosses.Punchinello
    name = "Punchinello"
    battlefield = Battlefields.MolevilleMines
    music = BattleMusic.Boss1
    boss = PunchinelloBoss
    boss_locations = [
        BossModelFill(Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE, 0, PunchinelloBoss, SpriteSize.Attack, False)
    ]
    repeatable_henchmen = [
        [ # needs special considerations for only tiny sprites
            RepeatableHenchmanFill(Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE, 1, DefaultMicrobomb, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE, 2, DefaultMicrobomb, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE, 3, DefaultMicrobomb, False, False, HenchmanType.NPCOnly),
        ],
        [ # check and see if cloning causes vram issues
            RepeatableHenchmanFill(Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE, 4, DefaultBobomb, False, False, HenchmanType.Pack),
            RepeatableHenchmanFill(Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE, 5, DefaultBobomb, False, False, HenchmanType.Pack),
            RepeatableHenchmanFill(Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE, 6, DefaultBobomb, False, False, HenchmanType.Pack),
        ]
    ]


class Booster(BossAndStarLocation):
    identifier = 192
    description = AvailableBosses.Booster
    name = "Booster"
    battlefield = Battlefields.BoosterTower
    music = BattleMusic.Boss1
    dialogs_to_replace = [2504, 2560, 2571, 2572, 3072, 3073]
    boss = BoosterBoss
    boss_locations = [
        BossModelFill(Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 0, BoosterBoss, SpriteSize.Small, False),
        BossModelFill(Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 7, BoosterBoss, SpriteSize.Small, False),
        BossModelFill(Rooms._154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER, 12, BoosterBoss, SpriteSize.Small, False),
        BossModelFill(Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM, 6, BoosterBoss, SpriteSize.Small, False),
        BossModelFill(Rooms._193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS, 6, BoosterBoss, SpriteSize.Small, False),
        BossModelFill(Rooms._054_BOOSTER_HILL_____DUMMY, 7, BoosterBoss, SpriteSize.Small, False),
        BossModelFill(Rooms._258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR, 3, BoosterBoss, SpriteSize.Small, False),
        BossModelFill(Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA, 10, BoosterBoss, SpriteSize.Small, False)
    ]
    unique_henchmen = [
        [
            UniqueHenchmanFill(Rooms._043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM, 4, DefaultSnifit, False, True, False, HenchmanType.Event, 1186),
            UniqueHenchmanFill(Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 1, DefaultSnifit, False, True, False, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER, 0, DefaultSnifit, False, True, False, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._054_BOOSTER_HILL_____DUMMY, 3, DefaultSnifit, True, True, False, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR, 0, DefaultSnifit, False, True, False, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA, 1, DefaultSnifit, False, True, False, HenchmanType.NPCOnly)
        ],
        [
            UniqueHenchmanFill(Rooms._194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM, 0, DefaultSnifit, False, True, False, HenchmanType.ExternalEvent, 1186),
            UniqueHenchmanFill(Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 2, DefaultSnifit, False, True, False, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER, 1, DefaultSnifit, False, True, False, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._054_BOOSTER_HILL_____DUMMY, 4, DefaultSnifit, True, True, False, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR, 1, DefaultSnifit, False, True, False, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA, 2, DefaultSnifit, False, True, False, HenchmanType.NPCOnly)
        ],
        [
            UniqueHenchmanFill(Rooms._037_BOOSTER_TOWER_4F_3LEVEL_ROOM_WJUMPING_SPOOKUMS, 8, DefaultSnifit, False, True, False, HenchmanType.Event, 1186),
            UniqueHenchmanFill(Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM, 3, DefaultSnifit, False, True, False, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER, 2, DefaultSnifit, False, True, False, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._054_BOOSTER_HILL_____DUMMY, 5, DefaultSnifit, True, True, False, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR, 2, DefaultSnifit, False, True, False, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA, 3, DefaultSnifit, False, True, False, HenchmanType.NPCOnly)
        ],
        [
            UniqueHenchmanFill(Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA, 4, DefaultSnifit, False, True, False, HenchmanType.NPCOnly)
        ],
        [
            UniqueHenchmanFill(Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA, 5, DefaultSnifit, False, True, False, HenchmanType.NPCOnly)
        ],
        [
            UniqueHenchmanFill(Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA, 6, DefaultSnifit, False, True, False, HenchmanType.NPCOnly)
        ],
        [
            UniqueHenchmanFill(Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA, 7, DefaultSnifit, False, True, False, HenchmanType.NPCOnly)
        ],
        [
            UniqueHenchmanFill(Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA, 8, DefaultSnifit, False, True, False, HenchmanType.NPCOnly)
        ],
    ]


class ClownBros(BossAndStarLocation):
    identifier = 353
    battlefield = Battlefields.ClownBros
    music = BattleMusic.Boss1
    description = AvailableBosses.KnifeGuyGrateGuy
    name = "Grate Guy"
    boss = GrateGuyBoss


class Bundt(BossAndStarLocation):
    identifier = 154
    battlefield = Battlefields.Bundt
    music = BattleMusic.Boss1
    description = AvailableBosses.Bundt
    name = "Bundt"
    dialogs_to_replace = [2061, 2062]
    boss = BundtBoss
    boss_locations = [
        BossModelFill(Rooms._155_MARRYMORE_CHAPEL_KITCHEN, 0, BundtBoss, SpriteSize.Small, False)
    ]
    unique_henchmen = [
        [
            UniqueHenchmanFill(Rooms._155_MARRYMORE_CHAPEL_KITCHEN, 1, BundtTorte1, False, True, False, HenchmanType.NPCOnly)
        ],
        [
            UniqueHenchmanFill(Rooms._155_MARRYMORE_CHAPEL_KITCHEN, 2, BundtTorte2, False, True, False, HenchmanType.NPCOnly)
        ]
    ]

class KingCalamari(BossAndStarLocation):
    identifier = 177
    battlefield = Battlefields.SunkenShip
    music = BattleMusic.Boss1
    description = AvailableBosses.KingCalamari
    name = "King Calamari"
    dialogs_to_replace = [1660]
    boss = KingCalamariBoss
    boss_locations = [
        BossModelFill(Rooms._177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM, 7, KingCalamariBoss, SpriteSize.Small, False)
    ]


class Hidon(BossAndStarLocation):
    identifier = 513
    battlefield = Battlefields.SunkenShip
    description = AvailableBosses.Hidon
    name = "Hidon"
    boss = HidonBoss


class Johnny(BossAndStarLocation):
    identifier = 28
    battlefield = Battlefields.SunkenShip
    music = BattleMusic.Boss1
    description = AvailableBosses.Johnny
    name = "Johnny"
    dialogs_to_replace = [1694, 1695, 1778, 1780, 1781, 1784, 1785, 1792, 1793]
    boss = JohnnyBoss
    boss_locations = [
        BossModelFill(Rooms._028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM, 2, JohnnyBoss, SpriteSize.Small, False),
        BossModelFill(Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH, 8, JohnnyBoss, SpriteSize.Small, False)
    ]
    unique_henchmen = [
        [
            UniqueHenchmanFill(Rooms._028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM, 4, JohnnyBandanaBlue, False, True, False, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH, 4, JohnnyBandanaBlue, False, True, False, HenchmanType.NPCOnly)
        ],
        [
            UniqueHenchmanFill(Rooms._028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM, 5, JohnnyBandanaBlue, False, True, False, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH, 5, JohnnyBandanaBlue, False, True, False, HenchmanType.NPCOnly)
        ],
        [
            UniqueHenchmanFill(Rooms._028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM, 6, JohnnyBandanaBlue, False, False, True, HenchmanType.NPCOnly)
        ],
        [
            UniqueHenchmanFill(Rooms._028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM, 7, JohnnyBandanaBlue, False, False, True, HenchmanType.NPCOnly)
        ],
    ]
    repeatable_henchmen = [
        [
            RepeatableHenchmanFill(Rooms._024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL, 0, DefaultBandanaRed1, True, False, HenchmanType.ExternalEvent, 1186),
            RepeatableHenchmanFill(Rooms._024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL, 1, DefaultBandanaRed1, True, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL, 2, DefaultBandanaRed1, True, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL, 3, DefaultBandanaRed1, True, False, HenchmanType.NPCOnly)
        ],
        [
            RepeatableHenchmanFill(Rooms._025_SUNKEN_SHIP_POSTKC_AREA_16_ENTRANCE_TO_JOHNNYS_ROOM, 0, DefaultBandanaRed2, True, False, HenchmanType.ExternalEvent, 1186),
            RepeatableHenchmanFill(Rooms._025_SUNKEN_SHIP_POSTKC_AREA_16_ENTRANCE_TO_JOHNNYS_ROOM, 1, DefaultBandanaRed2, True, False, HenchmanType.NPCOnly),
        ]
    ]


class Yaridovich(BossAndStarLocation):
    identifier = 315
    description = AvailableBosses.Yaridovich
    name = "Yaridovich"
    battlefield = Battlefields.Yaridovich
    music = BattleMusic.Boss2
    dialogs_to_replace = [2831, 2832, 2834, 2837, 2838,
                          2839, 2841, 2842, 2843, 2844, 2845, 2847, 2848]
    boss = YaridovichBoss
    boss_locations = [
        BossModelFill(Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, 4, YaridovichBoss, SpriteSize.Small, False),
        BossModelFill(Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH, 6, YaridovichBoss, SpriteSize.Small, False),
        BossModelFill(Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH, 7, YaridovichBoss, SpriteSize.Large, False)
    ]
    unique_henchmen = [
        [
            UniqueHenchmanFill(Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, 0, YaridovichHenchman, False, True, False, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH, 0, YaridovichHenchman, False, True, False, HenchmanType.NPCOnly),
        ],
        [
            UniqueHenchmanFill(Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, 1, YaridovichHenchman, False, True, False, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH, 1, YaridovichHenchman, False, True, False, HenchmanType.NPCOnly),
        ],
        [
            UniqueHenchmanFill(Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, 2, YaridovichHenchman, False, True, False, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._209_SEASIDE_TOWN_DURING_YARIDOVICH_INN_1F, 0, YaridovichHenchman, False, True, False, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._210_SEASIDE_TOWN_DURING_YARIDOVICH_INN_2F, 0, YaridovichHenchman, False, True, False, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH, 2, YaridovichHenchman, False, True, False, HenchmanType.NPCOnly),
        ],
        [
            UniqueHenchmanFill(Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE, 3, YaridovichHenchman, False, True, False, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._213_SEASIDE_TOWN_DURING_YARIDOVICH_BEETLES_ARE_USBOMB_SHOP, 0, YaridovichHenchman, False, True, False, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH, 3, YaridovichHenchman, False, True, False, HenchmanType.NPCOnly),
        ],
    ]
    repeatable_henchmen = [
        [
            RepeatableHenchmanFill(Rooms._213_SEASIDE_TOWN_DURING_YARIDOVICH_BEETLES_ARE_USBOMB_SHOP, 1, YaridovichHenchman, False, False, HenchmanType.NPCOnly),
        ],
        [
            RepeatableHenchmanFill(Rooms._214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP, 0, YaridovichHenchman, False, False, HenchmanType.NPCOnly),
        ],
        [
            RepeatableHenchmanFill(Rooms._214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP, 1, YaridovichHenchman, False, False, HenchmanType.NPCOnly),
        ],
        [
            RepeatableHenchmanFill(Rooms._215_SEASIDE_TOWN_DURING_YARIDOVICH_HEALTH_FOOD_STORE_LEFTMOST, 0, YaridovichHenchman, False, False, HenchmanType.NPCOnly),
        ],
        [
            RepeatableHenchmanFill(Rooms._216_SEASIDE_TOWN_DURING_YARIDOVICH_MUSHROOM_BOY_SHOP_MIDDLE, 0, YaridovichHenchman, False, False, HenchmanType.NPCOnly),
        ],
        [
            RepeatableHenchmanFill(Rooms._216_SEASIDE_TOWN_DURING_YARIDOVICH_MUSHROOM_BOY_SHOP_MIDDLE, 1, YaridovichHenchman, False, False, HenchmanType.NPCOnly),
        ],
        [
            RepeatableHenchmanFill(Rooms._217_SEASIDE_TOWN_DURING_YARIDOVICH_ACCESSORY_SHOP_RIGHTMOST, 0, YaridovichHenchman, False, False, HenchmanType.NPCOnly),
        ],
    ]


class Mokura(BossAndStarLocation):
    identifier = 519
    music = BattleMusic.Boss1
    description = AvailableBosses.Mokura
    name = "Mokura"
    boss = MokuraBoss


class Belome2(BossAndStarLocation):
    identifier = 268
    description = AvailableBosses.Belome2
    name = "Belome"
    battlefield = Battlefields.BelomeTemple
    music = BattleMusic.Boss1
    boss = Belome2Boss
    boss_locations = [
        BossModelFill(Rooms._268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM, 4, Belome2Boss, SpriteSize.Large, False)
    ]


class Jagger(BossAndStarLocation):
    identifier = 255
    description = AvailableBosses.Jagger
    name = "Jagger"
    battlefield = Battlefields.JinxDojo
    can_run_away = True
    dialogs_to_replace = [3044, 3352]
    boss = JaggerBoss
    boss_locations = [
        BossModelFill(Rooms._255_MONSTRO_TOWN_JINXS_DOJO, 1, JaggerBoss, SpriteSize.Small, False)
    ]


class Jinx1(BossAndStarLocation):
    identifier = 515
    description = AvailableBosses.Jinx1
    name = "Jinx"
    battlefield = Battlefields.JinxDojo
    can_run_away = True
    music = BattleMusic.Boss1
    boss = Jinx1Boss
    boss_locations = [
        BossModelFill(Rooms._255_MONSTRO_TOWN_JINXS_DOJO, 0, Jinx1Boss, SpriteSize.Small, False)
    ]


class Jinx2(BossAndStarLocation):
    identifier = 516
    description = AvailableBosses.Jinx2
    name = "Jinx"
    battlefield = Battlefields.JinxDojo
    can_run_away = True
    music = BattleMusic.Boss1
    boss = Jinx2Boss
    boss_locations = [
        BossModelFill(Rooms._255_MONSTRO_TOWN_JINXS_DOJO, 2, Jinx2Boss, SpriteSize.Small, False)
    ]


class Jinx3(BossAndStarLocation):
    identifier = 517
    description = AvailableBosses.Jinx3
    name = "Jinx"
    battlefield = Battlefields.JinxDojo
    can_run_away = True
    music = BattleMusic.Boss1
    dialogs_to_replace = [3353]
    boss = Jinx3Boss
    boss_locations = [
        BossModelFill(Rooms._255_MONSTRO_TOWN_JINXS_DOJO, 3, Jinx3Boss, SpriteSize.Small, False)
    ]


class Culex(BossAndStarLocation):
    identifier = 351
    description = AvailableBosses.Culex
    name = "Culex"
    battlefield = Battlefields.Culex
    music = BattleMusic.Culex
    dialogs_to_replace = [3338]
    boss = CulexBoss
    boss_locations = [
        BossModelFill(Rooms._351_CULEXS_ROOM, 0, CulexBoss, SpriteSize.Small, False)
    ]


class BoxBoy(BossAndStarLocation):
    identifier = 514
    battlefield = Battlefields.KeroSewers
    description = AvailableBosses.BoxBoy
    name = "Box Boy"
    boss = BoxBoyBoss


class MegaSmilax(BossAndStarLocation):
    identifier = 254
    description = AvailableBosses.Megasmilax
    name = "Megasmilax"
    battlefield = Battlefields.BeanValley
    music = BattleMusic.Boss1
    boss = MegaSmilaxBoss
    boss_locations = [
        BossModelFill(Rooms._254_BEAN_VALLEY_SMILAX_AREA, 0, MegaSmilaxBoss, SpriteSize.Small, False)
    ]


class Dodo(BossAndStarLocation):
    identifier = 520
    description = AvailableBosses.Dodo
    name = "Dodo"
    battlefield = Battlefields.NimbusCastle
    music = BattleMusic.Boss1
    boss = DodoBoss
    boss_locations = [
        BossModelFill(Rooms._112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT, 2, DodoBoss, SpriteSize.Large, False),
        BossModelFill(Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA, 0, DodoBoss, SpriteSize.Large, False),
        BossModelFill(Rooms._110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM, 3, DodoBoss, SpriteSize.Attack, True),
        BossModelFill(Rooms._437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD, 0, DodoBoss, SpriteSize.Large, False),
    ]


class Birdetta(BossAndStarLocation):
    identifier = 409
    description = AvailableBosses.Birdetta
    name = "Birdetta"
    battlefield = Battlefields.Birdo
    music = BattleMusic.Boss1
    dialogs_to_replace = [49]
    boss = BirdettaBoss


class Valentina(BossAndStarLocation):
    identifier = 430
    description = AvailableBosses.Valentina
    name = "Valentina"
    battlefield = Battlefields.Valentina
    music = BattleMusic.Boss1
    boss = ValentinaBoss
    boss_locations = [
        BossModelFill(Rooms._341_NIMBUS_LAND_GARROS_HOUSE, 3, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._341_NIMBUS_LAND_GARROS_HOUSE, 4, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._341_NIMBUS_LAND_GARROS_HOUSE, 5, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._430_NIMBUS_LAND_OUTSIDE_DURING_VALENTINA, 9, ValentinaBoss, SpriteSize.Small, False),
        BossModelFill(Rooms._109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL, 0, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL, 1, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL, 2, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL, 3, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL, 4, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL, 5, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._115_NIMBUS_CASTLE_AREA_03_4WAY_PATH_DURING_VALENTINA, 0, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._115_NIMBUS_CASTLE_AREA_03_4WAY_PATH_DURING_VALENTINA, 1, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._122_NIMBUS_CASTLE_AREA_12_ENTRANCE_TO_THRONE_ROOM, 0, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._122_NIMBUS_CASTLE_AREA_12_ENTRANCE_TO_THRONE_ROOM, 1, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA, 0, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA, 1, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM, 0, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM, 1, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM, 2, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._113_NIMBUS_CASTLE_AREA_16_SMALL_TWODOOR_ROOM_WTREASURE_FROM_AREA_15, 3, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05, 6, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05, 7, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR, 4, ValentinaBoss, SpriteSize.Small, False),
        BossModelFill(Rooms._408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM_, 6, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM_, 7, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._440_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_AFTER_VALENTINA, 0, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._440_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_AFTER_VALENTINA, 1, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._447_NIMBUS_LAND_HOT_SPRINGS, 1, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._447_NIMBUS_LAND_HOT_SPRINGS, 2, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._447_NIMBUS_LAND_HOT_SPRINGS, 3, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._447_NIMBUS_LAND_HOT_SPRINGS, 4, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._497_NIMBUS_CASTLE_AREA_06_____DUMMY, 0, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._497_NIMBUS_CASTLE_AREA_06_____DUMMY, 1, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA, 1, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA, 2, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA, 3, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA, 4, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._501_NIMBUS_CASTLE_AREA_03_4WAY_PATH_AFTER_VALENTINA, 0, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._501_NIMBUS_CASTLE_AREA_03_4WAY_PATH_AFTER_VALENTINA, 1, ValentinaBoss, SpriteSize.Statue, False),
        BossModelFill(Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA, 9, ValentinaBoss, SpriteSize.Small, False),
    ]
    repeatable_henchmen = [
        [
            RepeatableHenchmanFill(Rooms._411_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_1ST, 0, DefaultBluebird2, False, False, HenchmanType.Pack, 95),
        ],
        [
            RepeatableHenchmanFill(Rooms._411_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_1ST, 1, DefaultBluebird2, False, False, HenchmanType.Pack, 95),
        ],
        [
            RepeatableHenchmanFill(Rooms._121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND, 2, DefaultBluebird2, False, False, HenchmanType.Pack, 95),
        ],
        [
            RepeatableHenchmanFill(Rooms._121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND, 3, DefaultBluebird2, False, False, HenchmanType.Pack, 95),
        ],
        [
            RepeatableHenchmanFill(Rooms._121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND, 4, DefaultBluebird2, False, False, HenchmanType.Pack, 95),
        ],
        [
            RepeatableHenchmanFill(Rooms._121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND, 5, DefaultBluebird2, False, False, HenchmanType.Pack, 95),
        ],
        [
            RepeatableHenchmanFill(Rooms._437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD, 1, DefaultBluebird2, False, False, HenchmanType.Pack, 95),
        ],
        [
            RepeatableHenchmanFill(Rooms._437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD, 2, DefaultBluebird2, False, False, HenchmanType.Pack, 95),
        ],
    ]


class CzarDragon(BossAndStarLocation):
    identifier = 352
    description = AvailableBosses.CzarDragon
    name = "Czar Dragon"
    battlefield = Battlefields.CzarDragon
    music = BattleMusic.Boss1
    boss = CzarBoss
    boss_locations = [
        BossModelFill(Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM, 1, CzarBoss, SpriteSize.Large, False),
    ]
    repeatable_henchmen = [
        [
            RepeatableHenchmanFill(Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM, 2, CzarPyrosphere, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM, 3, CzarPyrosphere, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM, 4, CzarPyrosphere, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM, 5, CzarPyrosphere, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM, 6, CzarPyrosphere, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM, 7, CzarPyrosphere, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM, 8, CzarPyrosphere, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM, 9, CzarPyrosphere, False, False, HenchmanType.NPCOnly),
        ]
    ]


class AxemRangers(BossAndStarLocation):
    identifier = 393
    description = AvailableBosses.AxemRangers
    name = "Axem Red"
    battlefield = Battlefields.AxemRangers
    music = BattleMusic.Boss2
    boss = AxemRangersBoss
    boss_locations = [
        BossModelFill(Rooms._392_VOLCANO_POSTCD_AREA_06, 0, AxemRangersBoss, SpriteSize.Small, False),
        BossModelFill(Rooms._394_VOLCANO_POSTCD_AREA_05, 2, AxemRangersBoss, SpriteSize.Small, False),
        BossModelFill(Rooms._393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP, 1, AxemRangersBoss, SpriteSize.Small, False),
    ]
    unique_henchmen = [
        [
            UniqueHenchmanFill(Rooms._392_VOLCANO_POSTCD_AREA_06, 1, AxemRangersAxemGreen, False, False, True, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._391_VOLCANO_POSTCD_AREA_04, 0, AxemRangersAxemGreen, False, False, True, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP, 2, AxemRangersAxemGreen, False, False, True, HenchmanType.NPCOnly),
        ],
        [
            UniqueHenchmanFill(Rooms._392_VOLCANO_POSTCD_AREA_06, 2, AxemRangersAxemYellow, False, False, True, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP, 3, AxemRangersAxemYellow, False, False, True, HenchmanType.NPCOnly),
        ],
        [
            UniqueHenchmanFill(Rooms._392_VOLCANO_POSTCD_AREA_06, 3, AxemRangersAxemPink, False, False, True, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._394_VOLCANO_POSTCD_AREA_05, 1, AxemRangersAxemPink, False, False, True, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP, 4, AxemRangersAxemPink, False, False, True, HenchmanType.NPCOnly),
        ],
        [
            UniqueHenchmanFill(Rooms._392_VOLCANO_POSTCD_AREA_06, 4, AxemRangersAxemBlack, False, False, True, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._394_VOLCANO_POSTCD_AREA_05, 0, AxemRangersAxemBlack, False, False, True, HenchmanType.NPCOnly),
            UniqueHenchmanFill(Rooms._393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP, 5, AxemRangersAxemBlack, False, False, True, HenchmanType.NPCOnly),
        ],
    ]


class Chester(BossAndStarLocation):
    identifier = 461
    description = AvailableBosses.Chester
    name = "Chester"
    battlefield = Battlefields.BowsersKeep
    music = BattleMusic.Normal
    boss = ChesterBoss
    boss_locations = [
        BossModelFill(Rooms._461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB, 4, ChesterBoss, SpriteSize.Small, False),
    ]


class Magikoopa(BowsersKeepLocation):
    identifier = 266
    description = AvailableBosses.Magikoopa
    name = "Magikoopa"
    battlefield = Battlefields.BowsersKeep
    music = BattleMusic.Boss1
    boss = MagikoopaBoss
    boss_locations = [
        BossModelFill(Rooms._266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM, 2, MagikoopaBoss, SpriteSize.Small, False),
        BossModelFill(Rooms._376_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2B_1ST_FIGHT_CHEWY, 0, MagikoopaBoss, SpriteSize.Small, False),
        BossModelFill(Rooms._377_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2C_1ST_FIGHT_SPARKY, 0, MagikoopaBoss, SpriteSize.Small, False),
        BossModelFill(Rooms._459_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1A_1ST_FIGHT_TERRA_COTTA, 0, MagikoopaBoss, SpriteSize.Small, False),
        BossModelFill(Rooms._460_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1B_1ST_FIGHT_ALLEY_RAT, 0, MagikoopaBoss, SpriteSize.Small, False),
        BossModelFill(Rooms._461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB, 0, MagikoopaBoss, SpriteSize.Small, False),
        BossModelFill(Rooms._462_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2A_1ST_FIGHT_GU_GOOMBA, 0, MagikoopaBoss, SpriteSize.Small, False),
    ]


class Boomer(BowsersKeepLocation):
    identifier = 521
    description = AvailableBosses.Boomer
    name = "Boomer"
    battlefield = Battlefields.Boomer
    music = BattleMusic.Boss1
    boss = BoomerBoss
    boss_locations = [
        BossModelFill(Rooms._400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM, 0, BoomerBoss, SpriteSize.Large, False),
    ]


class Exor(BowsersKeepLocation):
    identifier = 522
    description = AvailableBosses.Exor
    name = "Exor"
    battlefield = Battlefields.BowsersKeep
    music = BattleMusic.Boss2
    boss = ExorBoss


class Countdown(BossLocation):
    identifier = 223
    description = AvailableBosses.CountDown
    name = "Count Down"
    battlefield = Battlefields.Gate
    music = BattleMusic.Boss1
    boss = CountdownBoss
    boss_locations = [
        BossModelFill(Rooms._223_SMITHY_FACTORY_AREA_07_COUNT_DOWNS_ROOM, 0, CountdownBoss, SpriteSize.Small, False),
    ]
    repeatable_henchmen = [
        [
            RepeatableHenchmanFill(Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM, 2, CzarPyrosphere, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM, 3, CzarPyrosphere, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM, 4, CzarPyrosphere, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM, 5, CzarPyrosphere, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM, 6, CzarPyrosphere, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM, 7, CzarPyrosphere, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM, 8, CzarPyrosphere, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM, 9, CzarPyrosphere, False, False, HenchmanType.NPCOnly),
        ]
    ]


class CloakerDomino(BossLocation):
    identifier = 103
    description = AvailableBosses.CloakerDomino
    name = "Cloaker"
    battlefield = Battlefields.Gate
    music = BattleMusic.Boss1
    boss = CloakerDominoBoss


class Clerk(BossLocation):
    identifier = 469
    description = AvailableBosses.Clerk
    name = "Clerk"
    battlefield = Battlefields.Factory
    boss = ClerkBoss
    boss_locations = [
        BossModelFill(Rooms._469_FACTORY_GROUNDS_AREA_01, 9, ClerkBoss, SpriteSize.Small, False),
    ]
    repeatable_henchmen = [
        [
            RepeatableHenchmanFill(Rooms._469_FACTORY_GROUNDS_AREA_01, 6, DefaultMadMallet, False, False, HenchmanType.ExternalEvent, 1186),
            RepeatableHenchmanFill(Rooms._469_FACTORY_GROUNDS_AREA_01, 7, DefaultMadMallet, False, False, HenchmanType.NPCOnly),
        ]
    ]


class Manager(BossLocation):
    identifier = 471
    description = AvailableBosses.Manager
    name = "Manager"
    battlefield = Battlefields.Factory
    boss = ManagerBoss
    boss_locations = [
        BossModelFill(Rooms._471_FACTORY_GROUNDS_AREA_02, 16, ManagerBoss, SpriteSize.Small, False),
    ]
    repeatable_henchmen = [
        [
            RepeatableHenchmanFill(Rooms._471_FACTORY_GROUNDS_AREA_02, 12, ManagerPounder, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._471_FACTORY_GROUNDS_AREA_02, 13, ManagerPounder, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._471_FACTORY_GROUNDS_AREA_02, 14, ManagerPounder, False, False, HenchmanType.NPCOnly),
        ]
    ]


class Director(BossLocation):
    identifier = 472
    description = AvailableBosses.Director
    name = "Director"
    battlefield = Battlefields.Factory
    boss = DirectorBoss
    boss_locations = [
        BossModelFill(Rooms._472_FACTORY_GROUNDS_AREA_03, 10, DirectorBoss, SpriteSize.Small, False),
    ]
    repeatable_henchmen = [
        [
            RepeatableHenchmanFill(Rooms._472_FACTORY_GROUNDS_AREA_03, 7, DirectorPoundette, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._472_FACTORY_GROUNDS_AREA_03, 8, DirectorPoundette, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._472_FACTORY_GROUNDS_AREA_03, 9, DirectorPoundette, False, False, HenchmanType.NPCOnly),
        ]
    ]


class Gunyolk(BossLocation):
    identifier = 470
    description = AvailableBosses.Gunyolk
    name = "Factory Chief"
    battlefield = Battlefields.Factory
    music = BattleMusic.Boss1
    boss = GunyolkBoss
    boss_locations = [
        BossModelFill(Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM, 13, GunyolkBoss, SpriteSize.Small, False),
    ]


class Smithy(BossLocation):
    identifier = 496
    description = AvailableBosses.Smithy
    name = "Smithy"
    battlefield = Battlefields.Smithy
    music = BattleMusic.Smithy
    boss = SmithyBoss
    # hide all other parts of smithy if shuffled
    boss_locations = [
        BossModelFill(Rooms._509_FACTORY_GROUNDS_SMITHYS_PAD, 6, SmithyBoss, SpriteSize.Large, False),
    ]
    repeatable_henchmen = [
        [
            RepeatableHenchmanFill(Rooms._406_FACTORY_GROUNDS_AREA_01_WITH_TOAD, 1, DefaultPaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._406_FACTORY_GROUNDS_AREA_01_WITH_TOAD, 2, DefaultPaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._406_FACTORY_GROUNDS_AREA_01_WITH_TOAD, 3, DefaultPaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._406_FACTORY_GROUNDS_AREA_01_WITH_TOAD, 4, DefaultPaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._406_FACTORY_GROUNDS_AREA_01_WITH_TOAD, 5, DefaultPaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._406_FACTORY_GROUNDS_AREA_01_WITH_TOAD, 6, DefaultPaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._469_FACTORY_GROUNDS_AREA_01, 0, DefaultPaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._469_FACTORY_GROUNDS_AREA_01, 1, DefaultPaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._469_FACTORY_GROUNDS_AREA_01, 2, DefaultPaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._469_FACTORY_GROUNDS_AREA_01, 3, DefaultPaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._469_FACTORY_GROUNDS_AREA_01, 4, DefaultPaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._469_FACTORY_GROUNDS_AREA_01, 5, DefaultPaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM, 7, DefaultUnpaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM, 8, DefaultUnpaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM, 9, DefaultUnpaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM, 10, DefaultUnpaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM, 11, DefaultUnpaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM, 15, DefaultUnpaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._406_FACTORY_GROUNDS_AREA_01_WITH_TOAD, 6, DefaultPaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._471_FACTORY_GROUNDS_AREA_02, 0, DefaultUnpaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._471_FACTORY_GROUNDS_AREA_02, 1, DefaultUnpaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._471_FACTORY_GROUNDS_AREA_02, 2, DefaultUnpaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._471_FACTORY_GROUNDS_AREA_02, 3, DefaultUnpaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._471_FACTORY_GROUNDS_AREA_02, 4, DefaultUnpaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._471_FACTORY_GROUNDS_AREA_02, 5, DefaultUnpaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._471_FACTORY_GROUNDS_AREA_02, 6, DefaultPaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._471_FACTORY_GROUNDS_AREA_02, 7, DefaultPaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._471_FACTORY_GROUNDS_AREA_02, 8, DefaultPaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._471_FACTORY_GROUNDS_AREA_02, 9, DefaultPaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._471_FACTORY_GROUNDS_AREA_02, 10, DefaultPaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._471_FACTORY_GROUNDS_AREA_02, 11, DefaultPaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._472_FACTORY_GROUNDS_AREA_03, 1, DefaultUnpaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._472_FACTORY_GROUNDS_AREA_03, 2, DefaultUnpaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._472_FACTORY_GROUNDS_AREA_03, 3, DefaultUnpaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._472_FACTORY_GROUNDS_AREA_03, 4, DefaultUnpaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._472_FACTORY_GROUNDS_AREA_03, 5, DefaultUnpaintedDrillBit, False, False, HenchmanType.NPCOnly),
            RepeatableHenchmanFill(Rooms._472_FACTORY_GROUNDS_AREA_03, 6, DefaultUnpaintedDrillBit, False, False, HenchmanType.NPCOnly),
        ]
    ]


# ********************* Default lists for the world.

def get_default_boss_locations(world):
    """Get default boss locations.

    Args:
        world (randomizer.logic.main.GameWorld):

    Returns:
        list[BossAndStarLocation]: List of default boss locations.

    """
    return [
        HammerBros(world),
        Croco1(world),
        Mack(world),
        Pandorite(world),
        Belome1(world),
        Bowyer(world),
        Croco2(world),
        Punchinello(world),
        Booster(world),
        ClownBros(world),
        Bundt(world),
        KingCalamari(world),
        Hidon(world),
        Johnny(world),
        Yaridovich(world),
        Mokura(world),
        Belome2(world),
        Jagger(world),
        Jinx1(world),
        Jinx2(world),
        Jinx3(world),
        Culex(world),
        BoxBoy(world),
        MegaSmilax(world),
        Dodo(world),
        Birdetta(world),
        Valentina(world),
        CzarDragon(world),
        AxemRangers(world),
        Chester(world),
        Magikoopa(world),
        Boomer(world),
        Exor(world),
        Countdown(world),
        CloakerDomino(world),
        Clerk(world),
        Manager(world),
        Director(world),
        Gunyolk(world),
        Smithy(world),
    ]
