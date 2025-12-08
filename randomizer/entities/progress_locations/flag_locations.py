# pylint: disable=C0301

"""Progress location definition pool for invisible items."""

from randomizer.entities.items import (
    BigBooFlag,
    DryBonesFlag,
    GreaperFlag,
    ShedKey)

from randomizer.types.items import (
    Item)
from randomizer.types.overworld_scripts.ids import (
    R005_MARRYMORE_OUTSIDE_DURING_BOOSTER,
    R012_MARRYMORE_INN_SUITE_ROOM,
    R016_MARIOS_PAD,
    R018_MUSHROOM_KINGDOM_CASTLE_THRONE_ROOM,
    R034_YOSTER_ISLE,
    R036_BOOSTER_TOWER_6F_AREA_04_3LEVEL_WTHWOMP_ON_TEETERTOTTER,
    R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS,
    R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM,
    R055_PIPE_VAULT_ENTRANCE,
    R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS,
    R062_KERO_SEWERS_AREA_01_WATER_ROOM_WSAVE,
    R064_MARRYMORE_OUTSIDE,
    R065_MARRYMORE_CHAPEL_SANCTUARY,
    R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED,
    R067_MIDAS_RIVER_BUSINESS_TRANSACTION_AREA,
    R075_TADPOLE_POND_AREA_01,
    R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE,
    R084_ROSE_TOWN_OUTSIDE,
    R085_ROSE_TOWN_DURING_BOWYER_INN_1F,
    R086_ROSE_TOWN_INN_1F,
    R092_GRATE_GUYS_CASINO_INSIDE_CASINO,
    R101_BOOSTER_PASS_AREA_02,
    R102_MOLEVILLE_OUTSIDE_AT_EXIT_FROM_MINES,
    R108_MOLEVILLE_OUTSIDE,
    R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT,
    R129_PIPE_VAULT_AREA_05,
    R130_SEA_AREA_02_LARGE_ROOM_WITH_SHOP,
    R133_SEA_AREA_06_WATER_ROOM_WWHIRLPOOLS,
    R137_LANDS_END_AREA_01,
    R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL,
    R152_MARRYMORE_CHAPEL_MAIN_HALL,
    R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
    R155_MARRYMORE_CHAPEL_KITCHEN,
    R158_STAR_HILL_AREA_02,
    R162_SUNKEN_SHIP_AREA_04_GREAPERS__DRY_BONES,
    R165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY,
    R166_SUNKEN_SHIP_PUZZLE_ROOM_1,
    R174_SEA_AREA_08_SHORE_WITH_SUNKEN_SHIP,
    R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM,
    R189_MARIOS_PIPEHOUSE,
    R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
    R191_MUSHROOM_KINGDOM_OUTSIDE,
    R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
    R193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS,
    R197_BOOSTER_TOWER_1F_AREA_02_HIGH_MASHER_ROOM_WTEETERTOTTER,
    R202_BOOSTER_TOWER_ENTRANCE,
    R204_MUSHROOM_WAY_AREA_02,
    R207_BANDITS_WAY_AREA_02,
    R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
    R217_SEASIDE_TOWN_DURING_YARIDOVICH_ACCESSORY_SHOP_RIGHTMOST,
    R231_FOREST_MAZE_SECRET_ENTRANCE,
    R235_FOREST_MAZE_AREA_08_UNDERGROUND,
    R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER,
    R252_BEAN_VALLEY_MAIN_AREA,
    R253_BEAN_VALLEY_MAGIC_BRICK_TO_BEANSTALK_AREA,
    R255_MONSTRO_TOWN_JINXS_DOJO,
    R265_LANDS_END_UNDERGROUND_AREA_03,
    R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM,
    R267_MONSTRO_TOWN_ENTRANCE,
    R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE,
    R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM,
    R290_MOLEVILLE_MINES_AREA_19_FROM_OUTSIDE_AFTER_PAYING,
    R313_SEASIDE_TOWN_ACCESSORY_SHOP,
    R314_SEASIDE_TOWN_SHED,
    R324_MONSTRO_TOWN_OUTSIDE,
    R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM,
    R337_MOLEVILLE_INN,
    R341_NIMBUS_LAND_GARROS_HOUSE,
    R343_NIMBUS_LAND_INN,
    R353_VOLCANO_AREA_18_HINO_MART,
    R395_MONSTRO_TOWN_MONSTERMAMAS_HOUSE_1F,
    R398_MONSTRO_TOWN_WEAPON_AND_ARMOR_SHOP,
    R401_LANDS_END_SECRET_UNDERGROUND_AREA_02_LEADS_TO_KERO_SEWERS,
    R404_LANDS_END_DESERT_AREA_04,
    R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
    R407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS,
    R413_NIMBUS_CASTLE_KINGS_LOCKED_CELLAR,
    R417_GARDENERS_HOUSE_OUTSIDE,
    R419_LAZY_SHELL_CLOUD,
    R447_NIMBUS_LAND_HOT_SPRINGS,
    R449_BOWSERS_KEEP_AREA_11_THWOMPBULLET_ROOM_AFTER_MAGIKOOPAS_ROOM,
    R482_MUSHROOM_KINGDOM_DURING_MACK_RAZ_AND_RAINIS_HOUSE,
    R490_MUSHROOM_KINGDOM_RAZ_AND_RAINIS_HOUSE)
from randomizer.types.overworld_scripts.event_scripts.ids import (
    E0252_NPC_QUEST_2_GRANT)
from randomizer.types.progress_locations import (
    Inventory,
    InvisibleItemCandidate)
from randomizer.types.world.flags import ShuffleLocationSelector, BowserDoorRequirements


from .helpers.area_access import (
    can_access_volcano,
    can_defeat_battle_door_boss,
    can_defeat_chapel_boss,
    can_defeat_forest_boss,
    can_defeat_inner_factory_first_boss,
    can_defeat_post_obstacle_boss,
    can_defeat_seaside_boss,
    can_defeat_second_moleville_boss,
    can_defeat_temple_boss)
from .helpers.classes import (
    BanditsWayLocation,
    BeanValleyLocation,
    BoosterPassLocation,
    BoosterTowerExteriorLocation,
    BoosterTowerLocation,
    BowsersKeepObstacleLocation,
    CasinoLocation,
    ForestLocation,
    InnerSunkenShipLocation,
    KeroSewersLocation,
    LandsEndLocation,
    MariosPadLocation,
    MarrymoreChapelLocation,
    MarrymoreLocation,
    MidasRiverLocation,
    MinesLocation,
    MolevilleLocation,
    MonstroTownLocation,
    NimbusTownLocation,
    NimbusCastleLocation,
    NimbusDeepCastleLocation,
    BarrelVolcanoLocation,
    InnerFactoryLocation,
    MushroomKingdomLocation,
    MushroomWayLocation,
    PipeVaultLocation,
    RoseTownLocation,
    RoseWayLocation,
    SeaLocation,
    SeasideTownLocation,
    StarHillLocation,
    SunkenShipLocation,
    TadpolePondLocation,
    YosterIsleLocation)


class MariosPadBed(MariosPadLocation, InvisibleItemCandidate):
    """MariosPadBed invisible progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MARIOS_PAD_BED
    _original_item: type[Item] = DryBonesFlag
    _room_ids: list[int] = [R189_MARIOS_PIPEHOUSE]
    _x_coord: int = 3
    _y_coord: int = 11

    _clue_text: str = """\n My flag's underneath a green bed.[await]"""

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, MariosPadLocation, inventory)


class RoseTownSign(RoseTownLocation, InvisibleItemCandidate):
    """RoseTownSign invisible progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.ROSE_TOWN_FLAG
    _original_item: type[Item] = GreaperFlag
    _room_ids: list[int] = [
        R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE,
        R084_ROSE_TOWN_OUTSIDE,
    ]
    _x_coord: int = 10
    _y_coord: int = 47
    _clue_text: str = """\n My flag's behind a wooden flower.[await]"""

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, RoseTownLocation, inventory)


class YosterIsleGoal(YosterIsleLocation, InvisibleItemCandidate):
    """YosterIsleGoal invisible progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.YOSTER_ISLE_FLAG
    _original_item: type[Item] = BigBooFlag
    _room_ids: list[int] = [R034_YOSTER_ISLE]
    _container_event: int = E0252_NPC_QUEST_2_GRANT
    _x_coord: int = 21
    _y_coord: int = 62
    _y_shift: int = -4
    _clue_text: str = """\n My flag's between “O” and “A”.[await]"""

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, YosterIsleLocation, inventory)


class MariosPadSteamwhistle(MariosPadLocation, InvisibleItemCandidate):
    """MariosPadSteamwhistle invisible progress location class"""

    _room_ids: list[int] = [R016_MARIOS_PAD]
    _x_coord: int = 11
    _y_coord: int = 34
    _z_coord: int = 1
    _clue_text: str = "\n  Mine is underneath a steamwhistle.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, MariosPadLocation, inventory)


class MariosPadLantern(MariosPadLocation, InvisibleItemCandidate):
    """MariosPadLantern invisible progress location class"""

    _room_ids: list[int] = [R016_MARIOS_PAD]
    _x_coord: int = 13
    _y_coord: int = 35
    _x_shift: int = 8
    _y_shift: int = -8
    _clue_text: str = "\n    Mine is under a white lantern.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, MariosPadLocation, inventory)


class MushroomWayTree(MushroomWayLocation, InvisibleItemCandidate):
    """MushroomWayTree invisible progress location class"""

    _room_ids: list[int] = [R204_MUSHROOM_WAY_AREA_02]
    _x_coord: int = 11
    _y_coord: int = 16
    _z_coord: int = 3
    _x_shift: int = -16
    _clue_text: str = " Mine's under a tree, up on a ledge\n by itself.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, MushroomWayLocation, inventory)


class MushroomKingdomSign(MushroomKingdomLocation, InvisibleItemCandidate):
    """MushroomKingdomSign invisible progress location class"""

    _room_ids: list[int] = [
        R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
        R191_MUSHROOM_KINGDOM_OUTSIDE,
    ]
    _x_coord: int = 22
    _y_coord: int = 116
    _z_coord: int = 2
    _y_shift: int = -8
    _clue_text: str = "\n  Mine's behind a wooden mushroom.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(
            self, MushroomKingdomLocation, inventory
        )


class MushroomKingdomEmptyHouse(MushroomKingdomLocation, InvisibleItemCandidate):
    """MushroomKingdomEmptyHouse invisible progress location class"""

    _room_ids: list[int] = [
        R482_MUSHROOM_KINGDOM_DURING_MACK_RAZ_AND_RAINIS_HOUSE,
        R490_MUSHROOM_KINGDOM_RAZ_AND_RAINIS_HOUSE,
    ]
    _x_coord: int = 14
    _y_coord: int = 61
    _y_shift: int = 8
    _clue_text: str = " Mine is under the bed in an empty\n house.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(
            self, MushroomKingdomLocation, inventory
        )


class ChancellorThrone(MushroomKingdomLocation, InvisibleItemCandidate):
    """ChancellorThrone invisible progress location class"""

    _room_ids: list[int] = [
        R018_MUSHROOM_KINGDOM_CASTLE_THRONE_ROOM,
        R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM,
    ]
    _x_coord: int = 19
    _y_coord: int = 24
    _z_coord: int = 3
    _clue_text: str = "\n       Mine's under a blue chair.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(
            self, MushroomKingdomLocation, inventory
        )


class BanditsWayFlower(BanditsWayLocation, InvisibleItemCandidate):
    """BanditsWayFlower invisible progress location class"""

    _room_ids: list[int] = [R207_BANDITS_WAY_AREA_02]
    _x_coord: int = 25
    _y_coord: int = 89
    _x_shift: int = 16
    _clue_text: str = "\n      Mine's on a landing flower.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, BanditsWayLocation, inventory)


class KeroGate(KeroSewersLocation, InvisibleItemCandidate):
    """KeroGate invisible progress location class"""

    _room_ids: list[int] = [
        R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS
    ]
    _x_coord: int = 5
    _y_coord: int = 41
    _z_coord: int = 4
    _y_shift: int = 8
    _clue_text: str = " Mine's in a corner, nearby lots of\n dank stairs.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, KeroSewersLocation, inventory)


class KeroStairs(KeroSewersLocation, InvisibleItemCandidate):
    """KeroStairs invisible progress location class"""

    _room_ids: list[int] = [R062_KERO_SEWERS_AREA_01_WATER_ROOM_WSAVE]
    _x_coord: int = 4
    _y_coord: int = 88
    _z_coord: int = 4
    _x_shift: int = -16
    _clue_text: str = "\n Mine is by a lone metal spike fence.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, KeroSewersLocation, inventory)


class MidasTrees(MidasRiverLocation, InvisibleItemCandidate):
    """MidasTrees invisible progress location class"""

    _room_ids: list[int] = [R067_MIDAS_RIVER_BUSINESS_TRANSACTION_AREA]
    _x_coord: int = 24
    _y_coord: int = 26
    _x_shift: int = -8
    _clue_text: str = " Mine's between a lone pair of\n palm trees.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, MidasRiverLocation, inventory)


class TadpoleCabinet(TadpolePondLocation, InvisibleItemCandidate):
    """TadpoleCabinet invisible progress location class"""

    _room_ids: list[int] = [R075_TADPOLE_POND_AREA_01]
    _x_coord: int = 25
    _y_coord: int = 29
    _z_coord: int = 2
    _x_shift: int = 8
    _y_shift: int = 8
    _clue_text: str = "\n       Mine is in a frog cabinet.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, TadpolePondLocation, inventory)


class RoseWayDirtPatch(RoseWayLocation, InvisibleItemCandidate):
    """RoseWayDirtPatch invisible progress location class"""

    _room_ids: list[int] = [R066_ROSE_WAY_EXIT_AREA_WHERE_BOWSERS_TROOPS_GATHERED]
    _x_coord: int = 25
    _y_coord: int = 88
    _clue_text: str = " Mine is in the middle of a HUGE\n patch of dirt.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, RoseWayLocation, inventory)


class RoseTownHydrant(RoseTownLocation, InvisibleItemCandidate):
    """RoseTownHydrant invisible progress location class"""

    _room_ids: list[int] = [
        R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE,
        R084_ROSE_TOWN_OUTSIDE,
    ]
    _x_coord: int = 15
    _y_coord: int = 63
    _y_shift: int = -8
    _clue_text: str = "\n  Mine is under a low steel hydrant.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, RoseTownLocation, inventory)


class RoseTownBowser(RoseTownLocation, InvisibleItemCandidate):
    """RoseTownBowser invisible progress location class"""

    _room_ids: list[int] = [
        R085_ROSE_TOWN_DURING_BOWYER_INN_1F,
        R086_ROSE_TOWN_INN_1F,
    ]
    _x_coord: int = 7
    _y_coord: int = 21
    _clue_text: str = "\n   Mine's under a miniature turtle.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, RoseTownLocation, inventory)


class RoseTownGardenerHydrant(RoseTownLocation, InvisibleItemCandidate):
    """RoseTownGardenerHydrant invisible progress location class"""

    _room_ids: list[int] = [R417_GARDENERS_HOUSE_OUTSIDE]
    _x_coord: int = 2
    _y_coord: int = 85
    _y_shift: int = -8
    _clue_text: str = "\n   Mine is under a private hydrant.[await]"

    def can_access(self, inventory: Inventory):
        return (
            InvisibleItemCandidate.can_access(self, RoseTownLocation, inventory)
            and can_defeat_forest_boss(self.world, inventory)
            and can_defeat_chapel_boss(self.world, inventory)
        )


class RoseTownGardenerBucket(RoseTownLocation, InvisibleItemCandidate):
    """RoseTownGardenerBucket invisible progress location class"""

    _room_ids: list[int] = [R417_GARDENERS_HOUSE_OUTSIDE]
    _x_coord: int = 5
    _y_coord: int = 87
    _clue_text: str = "\n   Mine is under a private bucket.[await]"

    def can_access(self, inventory: Inventory):
        return (
            InvisibleItemCandidate.can_access(self, RoseTownLocation, inventory)
            and can_defeat_forest_boss(self.world, inventory)
            and can_defeat_chapel_boss(self.world, inventory)
        )


class RoseTownGardenerLeaf(RoseTownLocation, InvisibleItemCandidate):
    """RoseTownGardenerLeaf invisible progress location class"""

    _room_ids: list[int] = [R419_LAZY_SHELL_CLOUD]
    _x_coord: int = 4
    _y_coord: int = 111
    _z_coord: int = 10
    _clue_text: str = "\n Mine's on a big leaf between\n two chests.[await]"

    def can_access(self, inventory: Inventory):
        return (
            InvisibleItemCandidate.can_access(self, RoseTownLocation, inventory)
            and can_defeat_forest_boss(self.world, inventory)
            and can_defeat_chapel_boss(self.world, inventory)
        )


class ForestMazeSecretStump(ForestLocation, InvisibleItemCandidate):
    """ForestMazeSecretStump invisible progress location class"""

    _room_ids: list[int] = [R231_FOREST_MAZE_SECRET_ENTRANCE]
    _x_coord: int = 18
    _y_coord: int = 72
    _x_shift: int = 16
    _clue_text: str = " Mine is behind a brightly\n illuminated tree stump.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, ForestLocation, inventory)


class ForestMazeSecretMushrooms(ForestLocation, InvisibleItemCandidate):
    """ForestMazeSecretMushrooms invisible progress location class"""

    _room_ids: list[int] = [R235_FOREST_MAZE_AREA_08_UNDERGROUND]
    _x_coord: int = 25
    _y_coord: int = 93
    _x_shift: int = -8
    _y_shift: int = 8
    _clue_text: str = " Mine is on an illuminated pack of\n 5 mushrooms.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, ForestLocation, inventory)


class ForestMazeSecretWiggler(ForestLocation, InvisibleItemCandidate):
    """ForestMazeSecretWiggler invisible progress location class"""

    _room_ids: list[int] = [R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER]
    _x_coord: int = 2
    _y_coord: int = 39
    _clue_text: str = "\n        Mine is on a sleepy bug.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, ForestLocation, inventory)


class PipeVaultExterior(PipeVaultLocation, InvisibleItemCandidate):
    """PipeVaultExterior invisible progress location class"""

    _room_ids: list[int] = [R055_PIPE_VAULT_ENTRANCE]
    _x_coord: int = 17
    _y_coord: int = 19
    _x_shift: int = -8
    _y_shift: int = 8
    _clue_text: str = " Mine is by a pipe in the middle of\n the road.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, PipeVaultLocation, inventory)


class PipeVaultRedPipe(PipeVaultLocation, InvisibleItemCandidate):
    """PipeVaultRedPipe invisible progress location class"""

    _room_ids: list[int] = [R129_PIPE_VAULT_AREA_05]
    _x_coord: int = 21
    _y_coord: int = 107
    _x_shift: int = -8
    _y_shift: int = -8
    _clue_text: str = "\n     Mine is behind a low red pipe.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, PipeVaultLocation, inventory)


class YosterIsleHut(YosterIsleLocation, InvisibleItemCandidate):
    """YosterIsleHut invisible progress location class"""

    _room_ids: list[int] = [R034_YOSTER_ISLE]
    _x_coord: int = 11
    _y_coord: int = 70
    _clue_text: str = "\n         Mine's in a fruity hut.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, YosterIsleLocation, inventory)


class MolevilleHydrant(MolevilleLocation, InvisibleItemCandidate):
    """MolevilleHydrant invisible progress location class"""

    _room_ids: list[int] = [
        R102_MOLEVILLE_OUTSIDE_AT_EXIT_FROM_MINES,
        R108_MOLEVILLE_OUTSIDE,
    ]
    _x_coord: int = 6
    _y_coord: int = 63
    _y_shift: int = -8
    _clue_text: str = "\n     Mine's under a gold hydrant.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, MolevilleLocation, inventory)


class MolevilleMountainBush(MolevilleLocation, InvisibleItemCandidate):
    """MolevilleMountainBush invisible progress location class"""

    _room_ids: list[int] = [
        R102_MOLEVILLE_OUTSIDE_AT_EXIT_FROM_MINES,
        R108_MOLEVILLE_OUTSIDE,
    ]
    _x_coord: int = 19
    _y_coord: int = 31
    _z_coord: int = 12
    _clue_text: str = " Mine's in a bush at the top of\n a mountain.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, MolevilleLocation, inventory)


class MolevilleBed(MolevilleLocation, InvisibleItemCandidate):
    """MolevilleBed invisible progress location class"""

    _room_ids: list[int] = [
        R337_MOLEVILLE_INN,
    ]
    _x_coord: int = 6
    _y_coord: int = 12
    _x_shift: int = 16
    _clue_text: str = "\n       Mine's under a middle bed.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, MolevilleLocation, inventory)


class MolevilleMinesArrows(MinesLocation, InvisibleItemCandidate):
    """MolevilleMinesArrows invisible progress location class"""

    _room_ids: list[int] = [
        R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE,
    ]
    _x_coord: int = 5
    _y_coord: int = 51
    _clue_text: str = (
        " Mine's between two arrows,\n pointing away from each other.[await]"
    )

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, MinesLocation, inventory)


class MolevilleMinesCeiling(MinesLocation, InvisibleItemCandidate):
    """MolevilleMinesCeiling invisible progress location class"""

    _room_ids: list[int] = [
        R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM,
    ]
    _x_coord: int = 8
    _y_coord: int = 13
    _z_coord: int = 4
    _clue_text: str = " Mine's in a zig-zag room, up\n on the ceiling.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, MinesLocation, inventory)


class MolevilleMinesEntry(MinesLocation, InvisibleItemCandidate):
    """MolevilleMinesEntry invisible progress location class"""

    _room_ids: list[int] = [
        R290_MOLEVILLE_MINES_AREA_19_FROM_OUTSIDE_AFTER_PAYING,
    ]
    _x_coord: int = 22
    _y_coord: int = 23
    _z_coord: int = 3
    _x_shift: int = 16
    _clue_text: str = "\n My flag?[delay]\n ...[delay]It's on the word “IN”,\n [delay]above a big hole.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(
            self, MinesLocation, inventory
        ) and can_defeat_second_moleville_boss(self.world, inventory)


class BoosterPassCornerBush(BoosterPassLocation, InvisibleItemCandidate):
    """BoosterPassCornerBush invisible progress location class"""

    _room_ids: list[int] = [
        R101_BOOSTER_PASS_AREA_02,
    ]
    _x_coord: int = 17
    _y_coord: int = 112
    _x_shift: int = -8
    _y_shift: int = 8
    _clue_text: str = "\n        Mine's in a corner bush.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, BoosterPassLocation, inventory)


class BoosterTowerExteriorSign(BoosterTowerExteriorLocation, InvisibleItemCandidate):
    """BoosterTowerExteriorSign invisible progress location class"""

    _room_ids: list[int] = [R202_BOOSTER_TOWER_ENTRANCE]
    _x_coord: int = 4
    _y_coord: int = 110
    _x_shift: int = 16
    _clue_text: str = " Mine's behind a sign with Japanese\n letters.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(
            self, BoosterTowerExteriorLocation, inventory
        )


class BoosterTowerDesk(BoosterTowerLocation, InvisibleItemCandidate):
    """BoosterTowerDesk invisible progress location class"""

    _room_ids: list[int] = [R043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM]
    _x_coord: int = 24
    _y_coord: int = 113
    _x_shift: int = 16
    _clue_text: str = "\n      Mine's under “B” and “K”.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, BoosterTowerLocation, inventory)


class BoosterTowerMasherRoom(BoosterTowerLocation, InvisibleItemCandidate):
    """BoosterTowerMasherRoom invisible progress location class"""

    _room_ids: list[int] = [
        R197_BOOSTER_TOWER_1F_AREA_02_HIGH_MASHER_ROOM_WTEETERTOTTER
    ]
    _x_coord: int = 19
    _y_coord: int = 122
    _y_shift: int = 8
    _clue_text: str = "\n Mine's on a lightly-loaded see-saw.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, BoosterTowerLocation, inventory)


class BoosterTowerCurtain(BoosterTowerLocation, InvisibleItemCandidate):
    """BoosterTowerCurtain invisible progress location class"""

    _room_ids: list[int] = [R193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS]
    _x_coord: int = 7
    _y_coord: int = 64
    _z_coord: int = 9
    _y_shift: int = 8
    _clue_text: str = (
        " Mine's in a corner, between a\n window and a red curtain.[await]"
    )

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, BoosterTowerLocation, inventory)


class BoosterTowerThwompInvisible(BoosterTowerLocation, InvisibleItemCandidate):
    """BoosterTowerThwompInvisible invisible progress location class"""

    _room_ids: list[int] = [
        R036_BOOSTER_TOWER_6F_AREA_04_3LEVEL_WTHWOMP_ON_TEETERTOTTER
    ]
    _x_coord: int = 5
    _y_coord: int = 114
    _z_coord: int = 12
    _clue_text: str = "\n     Mine is near a lonely thwomp.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, BoosterTowerLocation, inventory)


class BoosterTowerBrokenFrame(BoosterTowerLocation, InvisibleItemCandidate):
    """BoosterTowerBrokenFrame invisible progress location class"""

    _room_ids: list[int] = [
        R038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS
    ]
    _x_coord: int = 15
    _y_coord: int = 83
    _x_shift: int = -8
    _y_shift: int = -9
    _clue_text: str = "\n       Mine is in a broken frame.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, BoosterTowerLocation, inventory)


class BoosterTowerBeetleCage(BoosterTowerLocation, InvisibleItemCandidate):
    """BoosterTowerBeetleCage invisible progress location class"""

    _room_ids: list[int] = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _x_coord: int = 7
    _y_coord: int = 18
    _clue_text: str = "\n     Mine is on an insect cage.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, BoosterTowerLocation, inventory)


class BoosterTowerToyBox(BoosterTowerLocation, InvisibleItemCandidate):
    """BoosterTowerToyBox invisible progress location class"""

    _room_ids: list[int] = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _x_coord: int = 7
    _y_coord: int = 24
    _x_shift: int = 16
    _clue_text: str = "\n       Mine is behind a toy box.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, BoosterTowerLocation, inventory)


class MarrymoreOutsideCrate(MarrymoreLocation, InvisibleItemCandidate):
    """MarrymoreOutsideCrate invisible progress location class"""

    _room_ids: list[int] = [
        R005_MARRYMORE_OUTSIDE_DURING_BOOSTER,
        R064_MARRYMORE_OUTSIDE,
    ]
    _x_coord: int = 23
    _y_coord: int = 60
    _z_coord: int = 6
    _x_shift: int = -8
    _y_shift: int = -8
    _clue_text: str = "\n  Mine is under a lone backyard box.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, MarrymoreLocation, inventory)


class MarrymoreSuiteBed(MarrymoreLocation, InvisibleItemCandidate):
    """MarrymoreSuiteBed invisible progress location class"""

    _room_ids: list[int] = [R012_MARRYMORE_INN_SUITE_ROOM]
    _x_coord: int = 7
    _y_coord: int = 13
    _z_coord: int = 6
    _x_shift: int = -16
    _clue_text: str = " Mine's beneath two adjoined\n red beds.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, MarrymoreLocation, inventory)


class MarrymoreKitchen(MarrymoreChapelLocation, InvisibleItemCandidate):
    """MarrymoreKitchen invisible progress location class"""

    _room_ids: list[int] = [R155_MARRYMORE_CHAPEL_KITCHEN]
    _x_coord: int = 2
    _y_coord: int = 20
    _x_shift: int = -8
    _y_shift: int = 8
    _clue_text: str = " Mine is in a big cabinet full of\n dishes.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(
            self, MarrymoreChapelLocation, inventory
        )


class MarrymoreFireplace(MarrymoreChapelLocation, InvisibleItemCandidate):
    """MarrymoreFireplace invisible progress location class"""

    _room_ids: list[int] = [R152_MARRYMORE_CHAPEL_MAIN_HALL]
    _x_coord: int = 9
    _y_coord: int = 33
    _z_coord: int = 2
    _y_shift: int = -8
    _clue_text: str = "\n    Mine is in an empty fireplace.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(
            self, MarrymoreChapelLocation, inventory
        )


class MarrymoreOrgan(MarrymoreChapelLocation, InvisibleItemCandidate):
    """MarrymoreOrgan invisible progress location class"""

    _room_ids: list[int] = [
        R065_MARRYMORE_CHAPEL_SANCTUARY,
        R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
    ]
    _x_coord: int = 23
    _y_coord: int = 65
    _z_coord: int = 1
    _x_shift: int = -16
    _clue_text: str = " Mine is behind a big musical\n instrument.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(
            self, MarrymoreChapelLocation, inventory
        )


class MarrymoreAltar(MarrymoreChapelLocation, InvisibleItemCandidate):
    """MarrymoreAltar invisible progress location class"""

    _room_ids: list[int] = [
        R065_MARRYMORE_CHAPEL_SANCTUARY,
        R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
    ]
    _x_coord: int = 23
    _y_coord: int = 70
    _z_coord: int = 1
    _clue_text: str = "\n        Mine's behind an altar.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(
            self, MarrymoreChapelLocation, inventory
        )


class StarHillNorthStar(StarHillLocation, InvisibleItemCandidate):
    """StarHillNorthStar invisible progress location class"""

    _room_ids: list[int] = [R158_STAR_HILL_AREA_02]
    _x_coord: int = 8
    _y_coord: int = 69
    _z_coord: int = 2
    _x_shift: int = -10
    _clue_text: str = "\n     Mine is atop the North Star.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, StarHillLocation, inventory)


class SeasideTownAnchor(SeasideTownLocation, InvisibleItemCandidate):
    """SeasideTownAnchor invisible progress location class"""

    _room_ids: list[int] = [R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE]
    _x_coord: int = 14
    _y_coord: int = 57
    _x_shift: int = 16
    _clue_text: str = "\n       Mine is behind an anchor.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, SeasideTownLocation, inventory)


class SeasideTownHydrant(SeasideTownLocation, InvisibleItemCandidate):
    """SeasideTownHydrant invisible progress location class"""

    _room_ids: list[int] = [R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE]
    _x_coord: int = 16
    _y_coord: int = 25
    _z_coord: int = 5
    _x_shift: int = 0
    _y_shift: int = -8
    _clue_text: str = "\n  Mine is under a high steel hydrant.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, SeasideTownLocation, inventory)


class SeasideTownBucket(SeasideTownLocation, InvisibleItemCandidate):
    """SeasideTownBucket invisible progress location class"""

    _room_ids: list[int] = [R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE]
    _x_coord: int = 20
    _y_coord: int = 31
    _z_coord: int = 3
    _clue_text: str = "\n  Mine is under a high steel hydrant.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, SeasideTownLocation, inventory)


class SeasideTownFlowers(SeasideTownLocation, InvisibleItemCandidate):
    """SeasideTownFlowers invisible progress location class"""

    _room_ids: list[int] = [
        R217_SEASIDE_TOWN_DURING_YARIDOVICH_ACCESSORY_SHOP_RIGHTMOST,
        R313_SEASIDE_TOWN_ACCESSORY_SHOP,
    ]
    _x_coord: int = 26
    _y_coord: int = 60
    _y_shift: int = 8
    _clue_text: str = " Mine's in the middle of three\n pink flowers.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, SeasideTownLocation, inventory)


class SeasideTownShedBox(SeasideTownLocation, InvisibleItemCandidate):
    """SeasideTownShedBox invisible progress location class"""

    _room_ids: list[int] = [R314_SEASIDE_TOWN_SHED]
    _x_coord: int = 5
    _y_coord: int = 23
    _y_shift: int = 8
    _clue_text: str = " Mine's under a lone crate in an\n empty house.[await]"

    def can_access(self, inventory: Inventory):
        return (
            InvisibleItemCandidate.can_access(self, SeasideTownLocation, inventory)
            and can_defeat_seaside_boss(self.world, inventory)
            and inventory.has_item(ShedKey)
        )


class SeaArrow(SeaLocation, InvisibleItemCandidate):
    """SeaArrow invisible progress location class"""

    _room_ids: list[int] = [R130_SEA_AREA_02_LARGE_ROOM_WITH_SHOP]
    _x_coord: int = 8
    _y_coord: int = 21
    _x_shift: int = -8
    _y_shift: int = -8
    _clue_text: str = "\n   Mine is beside a mossy up-arrow.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, SeaLocation, inventory)


class SeaBoxes(SeaLocation, InvisibleItemCandidate):
    """SeaBoxes invisible progress location class"""

    _room_ids: list[int] = [R130_SEA_AREA_02_LARGE_ROOM_WITH_SHOP]
    _x_coord: int = 9
    _y_coord: int = 36
    _y_shift: int = -8
    _clue_text: str = "\n    Mine's in some V-shaped boxes.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, SeaLocation, inventory)


class SeaStalagnate(SeaLocation, InvisibleItemCandidate):
    """SeaStalagnate invisible progress location class"""

    _room_ids: list[int] = [R133_SEA_AREA_06_WATER_ROOM_WWHIRLPOOLS]
    _x_coord: int = 18
    _y_coord: int = 43
    _z_coord: int = 6
    _x_shift: int = -8
    _y_shift: int = -8
    _clue_text: str = " Mine is behind a big gray\n stalagnate.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, SeaLocation, inventory)


class SeaUnderwaterSail(SeaLocation, InvisibleItemCandidate):
    """SeaUnderwaterSail invisible progress location class"""

    _room_ids: list[int] = [R174_SEA_AREA_08_SHORE_WITH_SUNKEN_SHIP]
    _x_coord: int = 4
    _y_coord: int = 41
    _clue_text: str = "\n        Mine's behind a big sail.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, SeaLocation, inventory)


class ShipBarrelPile(SunkenShipLocation, InvisibleItemCandidate):
    """ShipBarrelPile invisible progress location class"""

    _room_ids: list[int] = [R162_SUNKEN_SHIP_AREA_04_GREAPERS__DRY_BONES]
    _x_coord: int = 7
    _y_coord: int = 66
    _z_coord: int = 3
    _clue_text: str = "\n  Mine is atop a big pile of barrels.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, SunkenShipLocation, inventory)


class ShipDoorMarker(SunkenShipLocation, InvisibleItemCandidate):
    """ShipDoorMarker invisible progress location class"""

    _room_ids: list[int] = [R165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY]
    _x_coord: int = 18
    _y_coord: int = 82
    _z_coord: int = 1
    _y_shift: int = 8
    _clue_text: str = " Mine is on a stack of boxes.[await][pause]\n[delay] Hm?[delay] Is that not specific enough?[await][page]\n Well,[delay] the boxes act as a door\n marker.[delay] They represent the\n number “4”.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, SunkenShipLocation, inventory)


class ShipButton(SunkenShipLocation, InvisibleItemCandidate):
    """ShipButton invisible progress location class"""

    _room_ids: list[int] = [R166_SUNKEN_SHIP_PUZZLE_ROOM_1]
    _x_coord: int = 16
    _y_coord: int = 133
    _clue_text: str = "\n   Mine is under a floating button.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, SunkenShipLocation, inventory)


class ShipSwitch(InnerSunkenShipLocation, InvisibleItemCandidate):
    """ShipSwitch invisible progress location class"""

    _room_ids: list[int] = [R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM]
    _x_coord: int = 17
    _y_coord: int = 121
    _clue_text: str = "\n  Mine is underneath a floating “J”.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(
            self, InnerSunkenShipLocation, inventory
        )


class LandsEndPlatform(LandsEndLocation, InvisibleItemCandidate):
    """LandsEndPlatform invisible progress location class"""

    _room_ids: list[int] = [R137_LANDS_END_AREA_01]
    _x_coord: int = 6
    _y_coord: int = 29
    _clue_text: str = "\n   Mine is under a rising platform.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, LandsEndLocation, inventory)


class LandsEndCannon(LandsEndLocation, InvisibleItemCandidate):
    """LandsEndCannon invisible progress location class"""

    _room_ids: list[int] = [R139_LANDS_END_AREA_03_GECKITS_PLAYING_CANNONBALL]
    _x_coord: int = 11
    _y_coord: int = 115
    _y_shift: int = -8
    _clue_text: str = " Mine's under a big and quiet\n cannon.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, LandsEndLocation, inventory)


class LandsEndArrow(LandsEndLocation, InvisibleItemCandidate):
    """LandsEndArrow invisible progress location class"""

    _room_ids: list[int] = [
        R401_LANDS_END_SECRET_UNDERGROUND_AREA_02_LEADS_TO_KERO_SEWERS
    ]
    _x_coord: int = 28
    _y_coord: int = 29
    _x_shift: int = 16
    _clue_text: str = "\n Mine is beside an orange up-arrow.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, LandsEndLocation, inventory)


class LandsEndHill(LandsEndLocation, InvisibleItemCandidate):
    """LandsEndHill invisible progress location class"""

    _room_ids: list[int] = [R404_LANDS_END_DESERT_AREA_04]
    _x_coord: int = 23
    _y_coord: int = 96
    _x_shift: int = 8
    _y_shift: int = 8
    _clue_text: str = " Mine is on a short, red hill in a\n remote area.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, LandsEndLocation, inventory)


class LandsEndStalagmite(LandsEndLocation, InvisibleItemCandidate):
    """LandsEndStalagmite invisible progress location class"""

    _room_ids: list[int] = [R265_LANDS_END_UNDERGROUND_AREA_03]
    _x_coord: int = 22
    _y_coord: int = 80
    _x_shift: int = 8
    _y_shift: int = 8
    _clue_text: str = (
        " Mine's on a big stalagmite\n formation, in an underground cave.[await]"
    )

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, LandsEndLocation, inventory)


class LandsEndCliffBush(LandsEndLocation, InvisibleItemCandidate):
    """LandsEndCliffBush invisible progress location class"""

    _room_ids: list[int] = [R407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS]
    _x_coord: int = 23
    _y_coord: int = 103
    _z_coord: int = 22
    _clue_text: str = " Mine is on a bush, way up high on\n a cliff.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(
            self, LandsEndLocation, inventory
        ) and can_defeat_temple_boss(self.world, inventory)


class DojoBonsai(MonstroTownLocation, InvisibleItemCandidate):
    """DojoBonsai invisible progress location class"""

    _room_ids: list[int] = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _x_coord: int = 6
    _y_coord: int = 9
    _y_shift: int = 8
    _clue_text: str = "\n   Mine's underneath a bonsai tree.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, MonstroTownLocation, inventory)


class MonstroEntranceSign(MonstroTownLocation, InvisibleItemCandidate):
    """MonstroEntranceSign invisible progress location class"""

    _room_ids: list[int] = [R267_MONSTRO_TOWN_ENTRANCE]
    _x_coord: int = 9
    _y_coord: int = 102
    _clue_text: str = "\n     Mine's in a lone flowery bush.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, MonstroTownLocation, inventory)


class MonstroBat(MonstroTownLocation, InvisibleItemCandidate):
    """MonstroBat invisible progress location class"""

    _room_ids: list[int] = [R324_MONSTRO_TOWN_OUTSIDE]
    _x_coord: int = 5
    _y_coord: int = 51
    _z_coord: int = 4
    _y_shift: int = 8
    _clue_text: str = "\n     Mine's behind a wooden bat.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, MonstroTownLocation, inventory)


class MonstroFan(MonstroTownLocation, InvisibleItemCandidate):
    """MonstroFan invisible progress location class"""

    _room_ids: list[int] = [R395_MONSTRO_TOWN_MONSTERMAMAS_HOUSE_1F]
    _x_coord: int = 12
    _y_coord: int = 80
    _z_coord: int = 1
    _x_shift: int = -16
    _clue_text: str = "\n       Mine's beside a room fan.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, MonstroTownLocation, inventory)


class MonstroShell(MonstroTownLocation, InvisibleItemCandidate):
    """MonstroShell invisible progress location class"""

    _room_ids: list[int] = [R398_MONSTRO_TOWN_WEAPON_AND_ARMOR_SHOP]
    _x_coord: int = 16
    _y_coord: int = 15
    _z_coord: int = 1
    _y_shift: int = 8
    _clue_text: str = "\n   Mine's beneath a spinning shell.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, MonstroTownLocation, inventory)


class BeanValleyPipe(BeanValleyLocation, InvisibleItemCandidate):
    """BeanValleyPipe invisible progress location class"""

    _room_ids: list[int] = [R252_BEAN_VALLEY_MAIN_AREA]
    _x_coord: int = 17
    _y_coord: int = 85
    _z_coord: int = 1
    _x_shift: int = -16
    _clue_text: str = " Mine's on an isolated, dead-end\n pipe.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, BeanValleyLocation, inventory)


class BeanValleyBeanstalkBlock(BeanValleyLocation, InvisibleItemCandidate):
    """BeanValleyBeanstalkBlock invisible progress location class"""

    _room_ids: list[int] = [R253_BEAN_VALLEY_MAGIC_BRICK_TO_BEANSTALK_AREA]
    _x_coord: int = 27
    _y_coord: int = 27
    _clue_text: str = "\n  Mine's underneath a big beanstalk.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, BeanValleyLocation, inventory)


class CasinoBell(CasinoLocation, InvisibleItemCandidate):
    """CasinoBell invisible progress location class"""

    _room_ids: list[int] = [R092_GRATE_GUYS_CASINO_INSIDE_CASINO]
    _x_coord: int = 14
    _y_coord: int = 19
    _x_shift: int = 8
    _y_shift: int = 8
    _clue_text: str = "\n       Mine is beside a tiny bell.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, CasinoLocation, inventory)


class NimbusGoldGoomba(NimbusTownLocation, InvisibleItemCandidate):
    """NimbusGoldGoomba invisible progress location class"""

    _room_ids: list[int] = [R341_NIMBUS_LAND_GARROS_HOUSE]
    _x_coord: int = 5
    _y_coord: int = 14
    _z_coord: int = 1
    _clue_text: str = "\n     Mine is on a golden Goomba.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, NimbusTownLocation, inventory)


class NimbusInnLobby(NimbusTownLocation, InvisibleItemCandidate):
    """NimbusInnLobby invisible progress location class"""

    _room_ids: list[int] = [R343_NIMBUS_LAND_INN]
    _x_coord: int = 6
    _y_coord: int = 84
    _z_coord: int = 2
    _x_shift: int = -8
    _y_shift: int = -8
    _clue_text: str = " Mine is under a stove, between\n two pots.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, NimbusTownLocation, inventory)


class NimbusPlant(NimbusCastleLocation, InvisibleItemCandidate):
    """NimbusPlant invisible progress location class"""

    _room_ids: list[int] = [
        R117_NIMBUS_CASTLE_AREA_15_FRONT_OF_4WAY_PATH_LARGE_RIGHTANGLE_ROOM_W_PLANT
    ]
    _x_coord: int = 27
    _y_coord: int = 74
    _z_coord: int = 1
    _clue_text: str = " Mine is behind a big potted plant\n in a corner.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, NimbusCastleLocation, inventory)


class NimbusBird(NimbusDeepCastleLocation, InvisibleItemCandidate):
    """NimbusBird invisible progress location class"""

    _room_ids: list[int] = [R413_NIMBUS_CASTLE_KINGS_LOCKED_CELLAR]
    _x_coord: int = 28
    _y_coord: int = 48
    _y_shift: int = -8
    _clue_text: str = (
        " Mine is under a birdcage, in a\n restricted dead-end area.[await]"
    )

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(
            self, NimbusDeepCastleLocation, inventory
        )


class NimbusHotSprings(NimbusTownLocation, InvisibleItemCandidate):
    """NimbusHotSprings invisible progress location class"""

    _room_ids: list[int] = [R447_NIMBUS_LAND_HOT_SPRINGS]
    _x_coord: int = 19
    _y_coord: int = 114
    _z_coord: int = 5
    _clue_text: str = " Mine's on the right side of a\n hot pool.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(
            self, NimbusTownLocation, inventory
        ) and can_access_volcano(self.world, inventory)


class VolcanoShips(BarrelVolcanoLocation, InvisibleItemCandidate):
    """VolcanoShips invisible progress location class"""

    _room_ids: list[int] = [R353_VOLCANO_AREA_18_HINO_MART]
    _x_coord: int = 11
    _y_coord: int = 61
    _z_coord: int = 2
    _clue_text: str = "\n    Mine is between two vehicles.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(self, BarrelVolcanoLocation, inventory)


class KeepPostObstacleBossRoom(BowsersKeepObstacleLocation, InvisibleItemCandidate):
    """KeepPostObstacleBossRoom invisible progress location class"""

    _room_ids: list[int] = [R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM]
    _x_coord: int = 26
    _y_coord: int = 97
    _x_shift: int = 8
    _y_shift: int = 8
    _clue_text: str = "\n  Mine is between two big red doors.[await]"

    def can_access(self, inventory: Inventory) -> bool:
        general_access = InvisibleItemCandidate.can_access(
            self, BowsersKeepObstacleLocation, inventory
        ) and can_defeat_post_obstacle_boss(self.world, inventory)
        needs_chester_defeat = self.world.settings.is_flag_value(
            BowserDoorRequirements, 6
        )
        if needs_chester_defeat:
            general_access &= can_defeat_battle_door_boss(self.world, inventory)
        return general_access and super().can_access(inventory)


class KeepThwomp(BowsersKeepObstacleLocation, InvisibleItemCandidate):
    """KeepThwomp invisible progress location class"""

    _room_ids: list[int] = [
        R449_BOWSERS_KEEP_AREA_11_THWOMPBULLET_ROOM_AFTER_MAGIKOOPAS_ROOM
    ]
    _x_coord: int = 19
    _y_coord: int = 47
    _clue_text: str = "\n      Mine is under a big thwomp.[await]"

    def can_access(self, inventory: Inventory) -> bool:
        general_access = InvisibleItemCandidate.can_access(
            self, BowsersKeepObstacleLocation, inventory
        ) and can_defeat_post_obstacle_boss(self.world, inventory)
        needs_chester_defeat = self.world.settings.is_flag_value(
            BowserDoorRequirements, 6
        )
        if needs_chester_defeat:
            general_access &= can_defeat_battle_door_boss(self.world, inventory)
        return general_access and super().can_access(inventory)


class FactoryButton(InnerFactoryLocation, InvisibleItemCandidate):
    """FactoryButton invisible progress location class"""

    _room_ids: list[int] = [R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD]
    _x_coord: int = 4
    _y_coord: int = 36
    _z_coord: int = 5
    _clue_text: str = " Mine is on a jammed machine\n button.[await]"

    def can_access(self, inventory: Inventory):
        return InvisibleItemCandidate.can_access(
            self, InnerFactoryLocation, inventory
        ) and can_defeat_inner_factory_first_boss(self.world, inventory)
