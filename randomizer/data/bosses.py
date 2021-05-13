# Boss/star piece randomization data for open mode.

from enum import IntEnum

from randomizer.logic import utils
from randomizer.logic.patch import Patch

from randomizer.data.npcmodels import models
from randomizer.data.roomobjecttables import Rooms


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
    room_objects = []
    model = None
    original_boss = -1
    target_npcs = None

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


# ****************************** Actual location classes
class HammerBros(BossAndStarLocation):
    star_address = 0x1e94ce
    battle_address = 0x1ffd56
    pack_number = 183
    battlefield = Battlefields.MushroomWay
    music = BattleMusic.Boss1
    sprite_width = 40
    sprite_height = 45
    model = {**models[283]}
    target_npcs = [
        {
            "room": Rooms._205_MUSHROOM_WAY_AREA_03,
            "npcs": [7]
        }
    ]
    original_boss = 27


class Croco1(BossAndStarLocation):
    star_address = 0x1e94fa
    battle_address = 0x1f3a54
    pack_number = 163
    battlefield = Battlefields.MushroomWay
    music = BattleMusic.Boss1
    model = {**models[110]}
    target_npcs = [
        {
            "room": Rooms._076_BANDITS_WAY_AREA_01,
            "npcs": [5]
        },
        {
            "room": Rooms._207_BANDITS_WAY_AREA_02,
            "npcs": [8]
        },
        {
            "room": Rooms._077_BANDITS_WAY_AREA_03,
            "npcs": [8]
        },
        {
            "room": Rooms._078_BANDITS_WAY_AREA_04,
            "npcs": [12]
        },
        {
            "room": Rooms._206_BANDITS_WAY_AREA_05,
            "npcs": [8]
        }
    ]
    original_boss = 240


class Mack(BossAndStarLocation):
    star_address = 0x1e9951
    has_star = True
    battle_address = 0x1e2d35
    pack_number = 179
    battlefield = Battlefields.MushroomKingdomThroneRoom
    music = BattleMusic.Boss2
    tall_sprite = True
    sprite_height = 57
    sprite_width = 43
    model = {**models[480]}
    target_npcs = [
        {
            "room": Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
            "optional_sidekicks": [0, 1, 2, 3, 4, 5, 6]
        },
        {
            "room": Rooms._323_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_THRONE_ROOM,
            "optional_sidekicks": [0, 1]
        },
        {
            "room": Rooms._325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
            "optional_sidekicks": [0, 1, 2, 3, 4]
        },
        {
            "room": Rooms._326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM,
            "npcs": [3],
            "optional_sidekicks": [4, 5, 6, 7, 8, 9]
        },
        {
            "room": Rooms._327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM,
            "optional_sidekicks": [0, 1]
        },
        {
            "room": Rooms._329_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_BRANCH_ROOM_TO_VAULTGUEST_ROOM,
            "optional_sidekicks": [0, 1]
        },
        {
            "room": Rooms._332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM,
            "optional_sidekicks": [0, 1]
        },
        {
            "room": Rooms._480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F,
            "optional_sidekicks": [3, 4]
        },
        {
            "room": Rooms._481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F,
            "optional_sidekicks": [1]
        },
    ]
    original_boss = 224


class Pandorite(BossAndStarLocation):
    star_address = 0x1e9517
    battle_address = 0x200a30
    pack_number = 156
    battlefield = Battlefields.KeroSewers
    original_boss = 23
    model = {**models[196]}


class Belome1(BossAndStarLocation):
    star_address = 0x1e952a
    battle_address = 0x200d80
    pack_number = 168
    battlefield = Battlefields.KeroSewers
    music = BattleMusic.Boss1
    sprite_height = 54
    sprite_width = 49
    model = {**models[371]}
    target_npcs = [
        {
            "room": Rooms._302_KERO_SEWERS_AREA_08_BELOMES_ROOM,
            "npcs": [3]
        }
    ]
    original_boss = 199


class Bowyer(BossAndStarLocation):
    star_address = 0x1e953d
    has_star = True
    battle_address = 0x1fc4f3
    pack_number = 181
    battlefield = Battlefields.Bowyer
    music = BattleMusic.Boss2
    tall_sprite = True
    sprite_width = 47
    sprite_height = 52
    model = {**models[486]}
    target_npcs = [
        {
            "room": Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD,
            "npcs": [16],
            "sidekicks": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        }
    ]
    original_boss = 230


class Croco2(BossAndStarLocation):
    star_address = 0x1e95bd
    battle_address = 0x1e9554
    pack_number = 164
    battlefield = Battlefields.MolevilleMines
    music = BattleMusic.Boss1
    model = {**models[367]}
    target_npcs = [
        {
            "room": Rooms._273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE,
            "npcs": [0],
            "optional_sidekicks": [1, 2, 3]
        },
        {
            "room": Rooms._277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM,
            "npcs": [0],
            "optional_sidekicks": [1, 2, 3]
        },
        {
            "room": Rooms._275_MOLEVILLE_MINES_AREA_06_SMALL_ROOM_LEADING_TO_AREA_06,
            "npcs": [0]
        },
        {
            "room": Rooms._281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM,
            "npcs": [0]
        },
        {
            "room": Rooms._279_MOLEVILLE_MINES_AREA_08_CROCOS_BOMBED_ROOM,
            "npcs": [0]
        },
        {
            "room": Rooms._283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM,
            "npcs": [0],
            "optional_sidekicks": [1, 2, 3]
        }
    ]
    original_boss = 241


class Punchinello(BossAndStarLocation):
    star_address = 0x1e96d9
    has_star = True
    battle_address = 0x1e693c
    pack_number = 140
    battlefield = Battlefields.MolevilleMines
    music = BattleMusic.Boss1
    sprite_width = 45
    sprite_height = 45
    model = {**models[464]}
    target_npcs = [
        {
            "room": Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
            "npcs": [0],
            "sidekicks": [2, 3, 4] # this one might need some finessing, hidon only
        }
    ]
    original_boss = 208


class Booster(BossAndStarLocation):
    star_address = 0x1e96ec
    battle_address = [0x1ef4e8, 0x20d7f5]
    pack_number = 161
    battlefield = Battlefields.BoosterTower
    music = BattleMusic.Boss1
    model = {**models[50]}
    target_npcs = [
        {
            "room": Rooms._067_MIDAS_RIVER_BUSINESS_TRANSACTION_AREA,
            "optional_sidekicks": [4]
        },
        {
            "room": Rooms._194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM,
            "optional_sidekicks": [0]
        },
        {
            "room": Rooms._037_BOOSTER_TOWER_4F_3LEVEL_ROOM_WJUMPING_SPOOKUMS,
            "optional_sidekicks": [8]
        },
        {
            "room": Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            "npcs": [0, 7],
            "sidekicks": [1, 2, 3]
        },
        {
            "room": Rooms._154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            "npcs": [12],
            "sidekicks": [0, 1, 2]
        },
        {
            "room": Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            "npcs": [6]
        },
        {
            "room": Rooms._193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS,
            "npcs": [6]
        },
        {
            "room": Rooms._054_BOOSTER_HILL_____DUMMY,
            "npcs": [7],
            "optional_sidekicks": [3, 4, 5]
        },
        {
            "room": Rooms._258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
            "npcs": [3], #formerly 4
            "sidekicks": [0, 1, 2]
        },
        {
            "room": Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            "npcs": [10],
            "sidekicks": [1, 2, 3, 4, 5, 6, 7, 8]
        },
    ]
    original_boss = 246
    dialogs_to_replace = [2504, 2560, 2571, 2572, 3072, 3073]


class ClownBros(BossAndStarLocation):
    star_address = 0x1e9714
    battle_address = 0x1ee82c
    pack_number = 177
    battlefield = Battlefields.ClownBros
    music = BattleMusic.Boss1
    original_boss = 192


class Bundt(BossAndStarLocation):
    star_address = 0x1e9727
    battle_address = 0x1e8a62
    pack_number = 176
    battlefield = Battlefields.Bundt
    music = BattleMusic.Boss1
    model = {**models[470]}
    target_npcs = [
        {
            "room": Rooms._155_MARRYMORE_CHAPEL_KITCHEN,
            "npcs": [0],
            "sidekicks": [1, 2]
        }
    ]
    original_boss = 194
    dialogs_to_replace = [2061, 2062]


class StarHill(StarLocation):
    star_address = 0x14aacb
    has_star = True

    def get_patch(self):
        """Override patch generation because this is an overworld spot that needs special data.

        Returns:
            randomizer.logic.patch.Patch: Patch data

        """
        patch = Patch()

        # Different values needed for this spot.
        val = 0x9c if self.has_star else 0x1c
        patch.add_data(self.star_address, utils.ByteField(val).as_bytes())

        return patch


class KingCalamari(BossAndStarLocation):
    star_address = 0x1e9773
    battle_address = 0x1e974f
    pack_number = 167
    battlefield = Battlefields.SunkenShip
    music = BattleMusic.Boss1
    sprite_width = 48
    model = {**models[168]}
    target_npcs = [
        {
            "room": Rooms._177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM,
            "npcs": [7]
        }
    ]
    original_boss = 216
    dialogs_to_replace = [1660]


class Hidon(BossAndStarLocation):
    star_address = 0x1e97a6
    battle_address = 0x200a37
    pack_number = 157
    battlefield = Battlefields.SunkenShip
    original_boss = 87
    model = {**models[196]}


class Johnny(BossAndStarLocation):
    star_address = 0x1e97b9
    battle_address = 0x20363d
    pack_number = 166
    battlefield = Battlefields.SunkenShip
    music = BattleMusic.Boss1
    model = {**models[52]}
    target_npcs = [
        {
            "room": Rooms._028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM,
            "npcs": [2],
            "sidekicks": [4, 5, 6, 7]
        },
        {
            "room": Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            "npcs": [8],
            "sidekicks": [4, 5]
        },
        {
            "room": Rooms._024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL,
            "optional_sidekicks": [0, 1, 2, 3]
        },
        {
            "room": Rooms._025_SUNKEN_SHIP_POSTKC_AREA_16_ENTRANCE_TO_JOHNNYS_ROOM,
            "optional_sidekicks": [0, 1]
        }
    ]
    original_boss = 249
    dialogs_to_replace = [1694, 1695, 1778, 1780, 1781, 1784, 1785, 1792, 1793]


class Yaridovich(BossAndStarLocation):
    star_address = 0x1e97cc
    has_star = True
    battle_address = 0x1ed255
    pack_number = 180
    battlefield = Battlefields.Yaridovich
    music = BattleMusic.Boss2
    tall_sprite = True
    sprite_width = 32
    sprite_height = 32
    model = {**models[40]}
    target_npcs = [
        {
            "room": Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
            "npcs": [4],
            "sidekicks": [0, 1, 2, 3]
        },
        {
            "room": Rooms._209_SEASIDE_TOWN_DURING_YARIDOVICH_INN_1F,
            "sidekicks": [0]
        },
        {
            "room": Rooms._210_SEASIDE_TOWN_DURING_YARIDOVICH_INN_2F,
            "sidekicks": [0]
        },
        {
            "room": Rooms._211_SEASIDE_TOWN_DURING_YARIDOVICH_ELDERS_HOUSE_1F,
            "npcs": [0],
        },
        {
            "room": Rooms._213_SEASIDE_TOWN_DURING_YARIDOVICH_BEETLES_ARE_USBOMB_SHOP,
            "sidekicks": [0, 1]
        },
        {
            "room": Rooms._214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP,
            "sidekicks": [0, 1]
        },
        {
            "room": Rooms._215_SEASIDE_TOWN_DURING_YARIDOVICH_HEALTH_FOOD_STORE_LEFTMOST,
            "sidekicks": [0]
        },
        {
            "room": Rooms._216_SEASIDE_TOWN_DURING_YARIDOVICH_MUSHROOM_BOY_SHOP_MIDDLE,
            "sidekicks": [0, 1]
        },
        {
            "room": Rooms._217_SEASIDE_TOWN_DURING_YARIDOVICH_ACCESSORY_SHOP_RIGHTMOST,
            "sidekicks": [0]
        },
        {
            "room": Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            "npcs": [7],
            "sidekicks": [0, 1, 2, 3]
        }
    ]
    original_boss = 226
    dialogs_to_replace = [2831, 2832, 2834, 2837, 2838, 2839, 2841, 2842, 2843, 2844, 2845, 2847, 2848]


class Mokura(BossAndStarLocation):
    pack_number = 207
    music = BattleMusic.Boss1
    sprite_height = 38
    sprite_width = 48
    original_boss = 148


class Belome2(BossAndStarLocation):
    star_address = 0x1e9813
    battle_address = 0x1e97dd
    pack_number = 169
    battlefield = Battlefields.BelomeTemple
    music = BattleMusic.Boss1
    sprite_height = 54
    sprite_width = 49
    model = {**models[455]}
    target_npcs = [
        {
            "room": Rooms._268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM,
            "npcs": [4]
        }
    ]
    original_boss = 200


class Jagger(BossAndStarLocation):
    star_address = 0x1e99e2
    battle_address = 0x1f6ca4
    pack_number = 189
    battlefield = Battlefields.JinxDojo
    can_run_away = True
    model = {**models[156]}
    target_npcs = [
        {
            "room": Rooms._255_MONSTRO_TOWN_JINXS_DOJO,
            "npcs": [1]
        }
    ]
    original_boss = 179
    dialogs_to_replace = [3044, 3352]


class Jinx1(BossLocation):
    battle_address = 0x1f6e8f
    pack_number = 178
    battlefield = Battlefields.JinxDojo
    can_run_away = True
    music = BattleMusic.Boss1
    model = {**models[207]}
    target_npcs = [
        {
            "room": Rooms._255_MONSTRO_TOWN_JINXS_DOJO,
            "npcs": [0]
        }
    ]
    original_boss = 195


class Jinx2(BossLocation):
    battle_address = 0x1f6e96
    pack_number = 187
    battlefield = Battlefields.JinxDojo
    can_run_away = True
    music = BattleMusic.Boss1
    model = {**models[415]}
    target_npcs = [
        {
            "room": Rooms._255_MONSTRO_TOWN_JINXS_DOJO,
            "npcs": [2]
        }
    ]
    original_boss = 196


class Jinx3(BossAndStarLocation):
    star_address = 0x1e9834
    battle_address = 0x1f6e9d
    pack_number = 188
    battlefield = Battlefields.JinxDojo
    can_run_away = True
    music = BattleMusic.Boss1
    model = {**models[416]}
    target_npcs = [
        {
            "room": Rooms._255_MONSTRO_TOWN_JINXS_DOJO,
            "npcs": [3]
        }
    ]
    original_boss = 218
    dialogs_to_replace = [3353]


class Culex(BossAndStarLocation):
    star_address = 0x1e98c9
    battle_address = 0x1f6fd7
    pack_number = 216
    battlefield = Battlefields.Culex
    music = BattleMusic.Culex
    original_boss = 255
    target_npcs = [
        {
            "room": Rooms._351_CULEXS_ROOM,
            "npcs": [0]
        }
    ]
    dialogs_to_replace = [3338]

class BoxBoy(BossAndStarLocation):
    star_address = 0x1e99cd
    battle_address = 0x1e999a
    pack_number = 158
    battlefield = Battlefields.KeroSewers
    original_boss = 134


class MegaSmilax(BossAndStarLocation):
    star_address = 0x1e98dc
    battle_address = 0x1fdb4f
    pack_number = 173
    battlefield = Battlefields.BeanValley
    music = BattleMusic.Boss1
    model = {**models[154]}
    target_npcs = [
        {
            "room": Rooms._254_BEAN_VALLEY_SMILAX_AREA,
            "npcs": [0]
        }
    ]
    original_boss = 204


class Dodo(BossAndStarLocation):
    star_address = 0x1e98ef
    battle_address = [0x1f7a1b, 0x209405]
    pack_number = 208
    battlefield = Battlefields.NimbusCastle
    music = BattleMusic.Boss1
    sprite_height = 56
    sprite_width = 46
    model = {**models[131]}
    target_npcs = [
        {
            "room": Rooms._112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT,
            "npcs": [2]
        },
        {
            "room": Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            "npcs": [0]
        },
        {
            "room": Rooms._437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD,
            "npcs": [0]
        }
    ]
    original_boss = 137


class Birdo(BossAndStarLocation):
    star_address = 0x1e9902
    battle_address = 0x20a397
    pack_number = 175
    battlefield = Battlefields.Birdo
    music = BattleMusic.Boss1
    original_boss = 205
    dialogs_to_replace = [49]


class Valentina(BossAndStarLocation):
    star_address = 0x1e9915
    battle_address = 0x1ea5dd
    pack_number = 171
    battlefield = Battlefields.Valentina
    music = BattleMusic.Boss1
    sprite_offset = 0x1db988
    model = {**models[56]}
    statue_index = 63
    # sidekicks?
    target_npcs = [
        {
            "room": Rooms._341_NIMBUS_LAND_GARROS_HOUSE,
            "npcs": [3, 4, 5]
        },
        {
            "room": Rooms._416_NIMBUS_LAND_OUTSIDE_BEFORE_VALENTINA,
            "npcs": [15, 16]
        },
        {
            "room": Rooms._430_NIMBUS_LAND_OUTSIDE_DURING_VALENTINA,
            "npcs": [9]
        },
        {
            "room": Rooms._109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL,
            "npcs": [0, 1, 2, 3, 4, 5]
        },
        {
            "room": Rooms._115_NIMBUS_CASTLE_AREA_03_4WAY_PATH_DURING_VALENTINA,
            "npcs": [0, 1]
        },
        {
            "room": Rooms._122_NIMBUS_CASTLE_AREA_12_ENTRANCE_TO_THRONE_ROOM,
            "npcs": [0, 1]
        },
        {
            "room": Rooms._120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA,
            "npcs": [0, 1]
        },
        {
            "room": Rooms._110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM,
            "npcs": [0, 1, 2]
        },
        {
            "room": Rooms._113_NIMBUS_CASTLE_AREA_16_SMALL_TWODOOR_ROOM_WTREASURE_FROM_AREA_15,
            "npcs": [3]
        },
        {
            "room": Rooms._119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05,
            "npcs": [6, 7]
        },
        {
            "room": Rooms._258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
            "npcs": [4] #formerly 6
        },
        {
            "room": Rooms._408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM_,
            "npcs": [6, 7]
        },
        {
            "room": Rooms._440_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_AFTER_VALENTINA,
            "npcs": [0, 1]
        },
        {
            "room": Rooms._447_NIMBUS_LAND_HOT_SPRINGS,
            "npcs": [1, 2, 3, 4]
        },
        {
            "room": Rooms._497_NIMBUS_CASTLE_AREA_06_____DUMMY,
            "npcs": [0, 1]
        },
        {
            "room": Rooms._499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA,
            "npcs": [1, 2, 3, 4]
        },
        {
            "room": Rooms._501_NIMBUS_CASTLE_AREA_03_4WAY_PATH_AFTER_VALENTINA,
            "npcs": [0, 1]
        },
        {
            "room": Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            "npcs": [9]
        },
        {
            "room": Rooms._411_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_1ST,
            "optional_sidekicks": [0, 1]
        },
        {
            "room": Rooms._121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND,
            "optional_sidekicks": [2, 3, 4, 5]
        },
        {
            "room": Rooms._437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD,
            "optional_sidekicks": [1, 2]
        }
    ]
    original_boss = 251


class CzarDragon(BossAndStarLocation):
    star_address = 0x1e9928
    battle_address = 0x204100
    pack_number = 172
    battlefield = Battlefields.CzarDragon
    music = BattleMusic.Boss1
    tall_sprite = True
    wide_sprite = True
    sprite_width = 59
    sprite_height = 54
    model = {**models[216]}
    target_npcs = [
        {
            "room": Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
            "npcs": [1],
            "sidekicks": [2, 3, 4, 5, 6, 7, 8, 9]
        }
    ]
    original_boss = 220


class AxemRangers(BossAndStarLocation):
    star_address = 0x1e993b
    has_star = True
    battle_address = 0x2046fc
    pack_number = 182
    battlefield = Battlefields.AxemRangers
    music = BattleMusic.Boss2
    model = {**models[208]}
    target_npcs = [
        {
            "room": Rooms._357_VOLCANO_POSTCD_AREA_01,
            "npcs": [2],
            "sidekicks": [3, 4, 5, 6]
        },
        {
            "room": Rooms._388_VOLCANO_POSTCD_AREA_02,
            "npcs": [2],
            "sidekicks": [3, 4, 5, 6]
        },
        {
            "room": Rooms._365_VOLCANO_POSTCD_AREA_03,
            "npcs": [1]
        },
        {
            "room": Rooms._391_VOLCANO_POSTCD_AREA_04,
            "npcs": [0]
        },
        {
            "room": Rooms._394_VOLCANO_POSTCD_AREA_05,
            "npcs": [2],
            "sidekicks": [0, 1]
        },
        {
            "room": Rooms._392_VOLCANO_POSTCD_AREA_06,
            "npcs": [0],
            "sidekicks": [1, 2, 3, 4]
        },
        {
            "room": Rooms._393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
            "npcs": [1],
            "sidekicks": [2, 3, 4, 5]
        },
    ]
    original_boss = 245

class Chester(BowsersKeepLocation):
    pack_number = 235
    battlefield = Battlefields.BowsersKeep
    music = BattleMusic.Normal 
    model = {**models[199]}
    target_npcs = [
        {
            "room": Rooms._461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB,
            "npcs": [4]
        }
    ]
    original_boss = 139


class Magikoopa(BowsersKeepLocation):
    star_address = 0x1e9a1b
    battle_address = 0x1f8847
    pack_number = 209
    battlefield = Battlefields.BowsersKeep
    music = BattleMusic.Boss1
    model = {**models[190]}
    target_npcs = [
        {
            "room": Rooms._266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM,
            "npcs": [2]
        },
        {
            "room": Rooms._376_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2B_1ST_FIGHT_CHEWY,
            "npcs": [0]
        },
        {
            "room": Rooms._377_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2C_1ST_FIGHT_SPARKY,
            "npcs": [0]
        },
        {
            "room": Rooms._459_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1A_1ST_FIGHT_TERRA_COTTA,
            "npcs": [0]
        },
        {
            "room": Rooms._460_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1B_1ST_FIGHT_ALLEY_RAT,
            "npcs": [0]
        },
        {
            "room": Rooms._461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB,
            "npcs": [0]
        },
        {
            "room": Rooms._462_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2A_1ST_FIGHT_GU_GOOMBA,
            "npcs": [0]
        }
    ]
    original_boss = 33


class Boomer(BowsersKeepLocation):
    star_address = 0x1e9a2e
    battle_address = 0x1f8a3a
    pack_number = 210
    battlefield = Battlefields.Boomer
    music = BattleMusic.Boss1
    tall_sprite = True
    sprite_width = 52
    sprite_width = 49
    model = {**models[482]}
    target_npcs = [
        {
            "room": Rooms._400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM,
            "npcs": [0]
        }
    ]
    original_boss = 52


class Exor(BowsersKeepLocation):
    star_address = 0x1e9a41
    battle_address = 0x1f8a58
    pack_number = 186
    battlefield = Battlefields.BowsersKeep
    music = BattleMusic.Boss2
    original_boss = 233



class Countdown(BossLocation):
    battle_address = 0x1fe11d
    pack_number = 174
    battlefield = Battlefields.Gate
    music = BattleMusic.Boss1
    model = {**models[453]}
    target_npcs = [
        {
            "room": Rooms._223_SMITHY_FACTORY_AREA_07_COUNT_DOWNS_ROOM,
            "npcs": [0]
        }
    ]
    original_boss = 197


class CloakerDomino(BossLocation):
    battle_address = 0x1f61d9
    pack_number = 184
    battlefield = Battlefields.Gate
    music = BattleMusic.Boss1
    original_boss = 221


class Clerk(BossLocation):
    battle_address = 0x1fe3ec
    pack_number = 146
    battlefield = Battlefields.Factory
    model = {**models[489]}
    target_npcs = [
        {
            "room": Rooms._469_FACTORY_GROUNDS_AREA_01,
            "npcs": [9],
            "optional_sidekicks": [6, 7]
        }
    ]
    original_boss = 50


class Manager(BossLocation):
    battle_address = 0x1fe819
    pack_number = 147
    battlefield = Battlefields.Factory
    model = {**models[493]}
    target_npcs = [
        {
            "room": Rooms._471_FACTORY_GROUNDS_AREA_02,
            "npcs": [16],
            "sidekicks": [12, 13, 14]
        }
    ]
    original_boss = 76


class Director(BossLocation):
    battle_address = 0x1fea21
    pack_number = 148
    battlefield = Battlefields.Factory
    model = {**models[497]}
    target_npcs = [
        {
            "room": Rooms._471_FACTORY_GROUNDS_AREA_02,
            "npcs": [10],
            "sidekicks": [7, 8, 9]
        }
    ]
    original_boss = 114


class Gunyolk(BossLocation):
    battle_address = 0x1fe247
    pack_number = 149
    battlefield = Battlefields.Factory
    music = BattleMusic.Boss1
    wide_sprite = True
    tall_sprite = True
    sprite_width = 71
    sprite_height = 63
    model = {**models[484]}
    target_npcs = [
        {
            "room": Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
            "npcs": [13],
            "sidekicks": [0, 1, 2, 3, 4, 5, 6] # dont need to use all of these
        }
    ]
    original_boss = 51

    # smithy
    #
    # target_npcs = [
    #     {
    #         "room": Rooms._406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
    #         "sidekicks": [1, 2, 3, 4, 5, 6]
    #     },
    #     {
    #         "room": Rooms._469_FACTORY_GROUNDS_AREA_01,
    #         "sidekicks": [0, 1, 2, 3, 4, 5]
    #     },
    #     {
    #         "room": Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
    #         "sidekicks": [7, 8, 9, 10, 11, 15]
    #     },
    #     {
    #         "room": Rooms._471_FACTORY_GROUNDS_AREA_02,
    #         "sidekicks": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] #6-11 are painted
    #     },
    #     {
    #         "room": Rooms._472_FACTORY_GROUNDS_AREA_03,
    #         "sidekicks": [1, 2, 3, 4, 5, 6]
    #     }
    # ]


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
        StarHill(world),
        KingCalamari(world),
        Hidon(world),
        Johnny(world),
        Yaridovich(world),
        Belome2(world),
        Jagger(world),
        Jinx1(world),
        Jinx2(world),
        Jinx3(world),
        Culex(world),
        BoxBoy(world),
        MegaSmilax(world),
        Dodo(world),
        Birdo(world),
        Valentina(world),
        CzarDragon(world),
        AxemRangers(world),
        Magikoopa(world),
        Boomer(world),
        Exor(world),
        Countdown(world),
        CloakerDomino(world),
        Clerk(world),
        Manager(world),
        Director(world),
        Gunyolk(world),
    ]
