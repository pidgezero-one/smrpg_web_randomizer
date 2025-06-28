# Boss/star piece randomization data for open mode.

from enum import IntEnum, Enum, auto

from randomizer.data.npcs import npcs
from randomizer.logic import utils
from randomizer.logic.patch import Patch

from randomizer.data import music
from randomizer.helpers.flag_helpers import SequenceType
from randomizer.data.npcmodels import models
from randomizer.helpers.npcmodeltables import SpriteName, VramStore, ShadowSize
from randomizer.helpers.roomobjecttables import Rooms
from randomizer.helpers.objectsequencetables import SequenceSpeeds, _0x08Flags

from randomizer.data.actionscripts.utils.mimic_rise import subscript as mimic_subscript

EMPTY_DIALOG = auto()


def is_vanilla(boss, location):
    return (
        (
            utils.isclass_or_instance(location, HammerBros)
            and utils.isclass_or_instance(boss, HammerBroBoss)
        )
        or (
            utils.isclass_or_instance(location, Croco1)
            and utils.isclass_or_instance(boss, Croco1Boss)
        )
        or (
            utils.isclass_or_instance(location, Mack)
            and utils.isclass_or_instance(boss, MackBoss)
        )
        or (
            utils.isclass_or_instance(location, Pandorite)
            and utils.isclass_or_instance(boss, PandoriteBoss)
        )
        or (
            (
                utils.isclass_or_instance(location, Belome1)
                or utils.isclass_or_instance(location, Belome2)
            )
            and (
                utils.isclass_or_instance(boss, Belome1Boss)
                or utils.isclass_or_instance(boss, Belome2Boss)
            )
        )
        or (
            utils.isclass_or_instance(location, Bowyer)
            and utils.isclass_or_instance(boss, BowyerBoss)
        )
        or (
            utils.isclass_or_instance(location, Croco2)
            and utils.isclass_or_instance(boss, Croco2Boss)
        )
        or (
            utils.isclass_or_instance(location, Punchinello)
            and utils.isclass_or_instance(boss, PunchinelloBoss)
        )
        or (
            utils.isclass_or_instance(location, Booster)
            and utils.isclass_or_instance(boss, BoosterBoss)
        )
        or (
            utils.isclass_or_instance(location, ClownBros)
            and utils.isclass_or_instance(boss, GrateGuyBoss)
        )
        or (
            utils.isclass_or_instance(location, Bundt)
            and utils.isclass_or_instance(boss, Bundt)
        )
        or (
            utils.isclass_or_instance(location, KingCalamari)
            and utils.isclass_or_instance(boss, KingCalamariBoss)
        )
        or (
            utils.isclass_or_instance(location, Hidon)
            and utils.isclass_or_instance(boss, HidonBoss)
        )
        or (
            utils.isclass_or_instance(location, Johnny)
            and utils.isclass_or_instance(boss, JohnnyBoss)
        )
        or (
            utils.isclass_or_instance(location, Yaridovich)
            and utils.isclass_or_instance(boss, YaridovichBoss)
        )
        or (
            utils.isclass_or_instance(location, Mokura)
            and utils.isclass_or_instance(boss, MokuraBoss)
        )
        or (
            utils.isclass_or_instance(location, Jagger)
            and utils.isclass_or_instance(boss, JaggerBoss)
        )
        or (
            (
                utils.isclass_or_instance(location, Jinx1)
                or utils.isclass_or_instance(location, Jinx2)
                or utils.isclass_or_instance(location, Jinx3)
            )
            and (
                utils.isclass_or_instance(boss, Jinx1Boss)
                or utils.isclass_or_instance(boss, Jinx2Boss)
                or utils.isclass_or_instance(boss, Jinx3Boss)
            )
        )
        or (
            utils.isclass_or_instance(location, Culex)
            and utils.isclass_or_instance(boss, Culex)
        )
        or (
            utils.isclass_or_instance(location, BoxBoy)
            and utils.isclass_or_instance(boss, BoxBoyBoss)
        )
        or (
            utils.isclass_or_instance(location, MegaSmilax)
            and utils.isclass_or_instance(boss, MegaSmilaxBoss)
        )
        or (
            utils.isclass_or_instance(location, Dodo)
            and utils.isclass_or_instance(boss, DodoBoss)
        )
        or (
            utils.isclass_or_instance(location, Birdetta)
            and utils.isclass_or_instance(boss, BirdettaBoss)
        )
        or (
            utils.isclass_or_instance(location, Valentina)
            and utils.isclass_or_instance(boss, ValentinaBoss)
        )
        or (
            utils.isclass_or_instance(location, CzarDragon)
            and utils.isclass_or_instance(boss, CzarBoss)
        )
        or (
            utils.isclass_or_instance(location, AxemRangers)
            and utils.isclass_or_instance(boss, AxemRangersBoss)
        )
        or (
            utils.isclass_or_instance(location, Chester)
            and utils.isclass_or_instance(boss, ChesterBoss)
        )
        or (
            utils.isclass_or_instance(location, Magikoopa)
            and utils.isclass_or_instance(boss, MagikoopaBoss)
        )
        or (
            utils.isclass_or_instance(location, Boomer)
            and utils.isclass_or_instance(boss, BoomerBoss)
        )
        or (
            utils.isclass_or_instance(location, Exor)
            and utils.isclass_or_instance(boss, ExorBoss)
        )
        or (
            utils.isclass_or_instance(location, Countdown)
            and utils.isclass_or_instance(boss, CountdownBoss)
        )
        or (
            utils.isclass_or_instance(location, CloakerDomino)
            and utils.isclass_or_instance(boss, CloakerDominoBoss)
        )
        or (
            utils.isclass_or_instance(location, Clerk)
            and utils.isclass_or_instance(boss, ClerkBoss)
        )
        or (
            utils.isclass_or_instance(location, Manager)
            and utils.isclass_or_instance(boss, ManagerBoss)
        )
        or (
            utils.isclass_or_instance(location, Director)
            and utils.isclass_or_instance(boss, DirectorBoss)
        )
        or (
            utils.isclass_or_instance(location, Gunyolk)
            and utils.isclass_or_instance(boss, GunyolkBoss)
        )
        or (
            utils.isclass_or_instance(location, Smithy)
            and utils.isclass_or_instance(boss, SmithyBoss)
        )
    )


def has_vanilla_henchmen(boss, location):
    return (
        len(location.repeatable_henchmen + location.unique_henchmen) == 0
        or len(boss.repeatable_henchmen + boss.unique_henchmen) == 0
    )


def sanitize_animation_script(boss, boss_location, script, model):
    """Helper function that helps ensure that illegal sequences cannot be performed for substituted sprites in specific slots, but also substitutes specifically chosen sequences where appropriate."""
    # leave script alone if character is vanilla
    if not is_vanilla(boss, boss_location):
        new_script = []
        for _, subscript_command in enumerate(script):
            # Pretty much all of these animations are based around sequence setting
            # if a specific mold or sequence doesn't have an equivalent, just don't include it in the sanitized script
            if subscript_command["command"] == "set_sprite_sequence":
                # molds
                if _0x08Flags.READ_AS_MOLD in subscript_command["args"][2]:
                    # if setting mold to 0, that's ok, just reset to the right default mold for scarecrow or culex
                    if subscript_command["args"][0] == 0:
                        new_script.append(subscript_command)
                    # otherwise, it's subject to animation-specific rules
                    else:
                        if utils.isclass_or_instance(boss_location, Booster):
                            if subscript_command["args"][0] == 12:
                                new_script.append(
                                    {"identifier": "dummy", "command": "face_northeast"}
                                )

                # sequences
                else:
                    # bandit's way distraction
                    if (
                        utils.isclass_or_instance(boss_location, Croco1)
                        and model.animations is not None
                        and model.animations.bandits_way_distracted is not None
                    ):
                        if subscript_command["args"][0] == 5:
                            subscript_command["args"][
                                0
                            ] = model.animations.bandits_way_distracted.sequence_id
                            # no support for sprite offsets, but not necessary with the sprites we're using
                            new_script.append(subscript_command)
                    # ending credits race
                    elif (
                        utils.isclass_or_instance(boss_location, Croco1)
                        and model.animations is not None
                        and model.animations.recoil is not None
                    ):
                        if subscript_command["args"][0] == 2:
                            subscript_command["args"][
                                0
                            ] = model.animations.recoil.sequence_id
                            # no support for sprite offsets, but not necessary with the sprites we're using
                            new_script.append(subscript_command)
                    # moleville mines punch
                    elif utils.isclass_or_instance(boss_location, Punchinello):
                        if (
                            model.animations is not None
                            and model.animations.mines_punch is not None
                        ):
                            if subscript_command["args"][0] == 3:
                                subscript_command["args"][
                                    0
                                ] = model.animations.mines_punch.sequence_id
                                new_script.append(subscript_command)
                    # chapel laughing
                    elif utils.isclass_or_instance(boss_location, Booster):
                        if (
                            model.animations is not None
                            and model.animations.chapel_laugh is not None
                        ):
                            if subscript_command["args"][0] == 2:
                                subscript_command["args"][
                                    0
                                ] = model.animations.chapel_laugh.sequence_id
                                new_script.append(subscript_command)
                    # marrymore kitchen
                    elif utils.isclass_or_instance(boss_location, Bundt):
                        if (
                            model.animations is not None
                            and model.animations.kitchen_prep is not None
                        ):
                            if subscript_command["args"][0] == 3:
                                subscript_command["args"][
                                    0
                                ] = model.animations.kitchen_prep.sequence_id
                                if (
                                    model.animations.kitchen_prep.total_duration
                                    is not None
                                ):
                                    subscript_command["args"][2].append(
                                        _0x08Flags.LOOPING_OFF
                                    )
                                new_script.append(subscript_command)
                    # ship beckon
                    elif utils.isclass_or_instance(boss_location, KingCalamari):
                        if (
                            model.animations is not None
                            and model.animations.ship_beckon is not None
                        ):
                            if subscript_command["args"][0] == 1:
                                subscript_command["args"][
                                    0
                                ] = model.animations.ship_beckon.sequence_id
                                subscript_command["args"][2].append(
                                    _0x08Flags.LOOPING_OFF
                                )
                                new_script.append(subscript_command)
                    # ship chair
                    elif utils.isclass_or_instance(boss_location, Johnny):
                        if (
                            model.animations is not None
                            and model.animations.ship_chair is not None
                        ):
                            if subscript_command["args"][0] == 10:
                                subscript_command["args"][
                                    0
                                ] = model.animations.ship_chair.sequence_id
                                new_script.append(subscript_command)
                    # jagger
                    elif utils.isclass_or_instance(boss_location, Jagger):
                        if (
                            utils.isclass_or_instance(boss, MimicBoss)
                            and subscript_command["args"][0] == 4
                        ):
                            new_script.extend(boss.challenge_script)
                        elif (
                            model.animations is not None
                            and model.animations.dojo_challenge is not None
                        ):
                            if subscript_command["args"][0] == 4:
                                subscript_command["args"][
                                    0
                                ] = model.animations.dojo_challenge.sequence_id
                                new_script.append(subscript_command)
                    # jinx
                    elif (
                        utils.isclass_or_instance(boss_location, Jinx1)
                        or utils.isclass_or_instance(boss_location, Jinx2)
                        or utils.isclass_or_instance(boss_location, Jinx3)
                    ):
                        if (
                            utils.isclass_or_instance(boss, MimicBoss)
                            and subscript_command["args"][0] == 3
                        ):
                            new_script.extend(boss.challenge_script)
                        elif (
                            model.animations is not None
                            and model.animations.dojo_challenge is not None
                        ):
                            if subscript_command["args"][0] == 3:
                                subscript_command["args"][
                                    0
                                ] = model.animations.dojo_challenge.sequence_id
                                new_script.append(subscript_command)
                    # magikoopa - challenge only. sequence #10 also used in battle doors, which will be handled separately
                    elif utils.isclass_or_instance(boss_location, Magikoopa):
                        if (
                            utils.isclass_or_instance(boss, MimicBoss)
                            and subscript_command["args"][0] == 10
                        ):
                            new_script.extend(boss.challenge_script)
                        elif (
                            model.animations is not None
                            and model.animations.keep_challenge is not None
                        ):
                            if subscript_command["args"][0] == 10:
                                subscript_command["args"][
                                    0
                                ] = model.animations.keep_challenge.sequence_id
                                new_script.append(subscript_command)
                    # similar to mold, restore default sequence if appropriate
                    else:
                        if subscript_command["args"][0] == 0:
                            new_script.append(subscript_command)
            else:
                new_script.append(subscript_command)
        return new_script
    else:
        return script


class CrownHeight(Enum):
    Short = auto()
    Mid = auto()
    Tall = auto()


class AvailableBosses(Enum):
    HammerBro = "Hammer Bros"
    Mack = "Mack"
    Croco1 = "Croco 1"
    Pandorite = "Pandorite"
    Belome1 = "Belome 1"
    Bowyer = "Bowyer"
    Croco2 = "Croco 2"
    Punchinello = "Punchinello"
    Booster = "Booster"
    KnifeGuyGrateGuy = "Knife Guy & Grate Guy"
    Bundt = "Bundt"
    KingCalamari = "King Calamari"
    Hidon = "Hidon"
    Johnny = "Johnny"
    Yaridovich = "Yaridovich"
    Mokura = "Mokura"
    Belome2 = "Belome 2"
    Jagger = "Jagger"
    Jinx1 = "Jinx 1"
    Jinx2 = "Jinx 2"
    Jinx3 = "Jinx 3"
    Culex = "Culex"
    BoxBoy = "Box Boy"
    Megasmilax = "Megasmilax"
    Dodo = "Dodo"
    Birdetta = "Birdetta"
    Valentina = "Valentina"
    CzarDragon = "Czar Dragon"
    AxemRangers = "Axem Rangers"
    Chester = "Chester"
    Magikoopa = "Magikoopa"
    Boomer = "Boomer"
    Exor = "Exor"
    CountDown = "Count Down"
    CloakerDomino = "Cloaker & Domino"
    Clerk = "Clerk"
    Manager = "Manager"
    Director = "Director"
    Gunyolk = "Gunyolk & Factory Chief"
    Smithy = "Smithy"


class Battlefields(IntEnum):
    """Enumeration for ID values for battlefields."""

    Forest = 0x00
    Bowyer = 0x01
    Beanstalks = 0x02
    KingCalamari = 0x03
    SunkenShip = 0x04
    MolevilleMines = 0x05
    BowsersKeep = 0x07
    CzarDragon = 0x08
    MushroomWay = 0x09
    Mountains = 0x0A
    House = 0x0B
    BoosterTower = 0x0C
    MushroomKingdom = 0x0D
    Underwater = 0x0E
    MushroomKingdomThroneRoom = 0x0F
    Exor = 0x10
    ClownBros = 0x11
    Countdown = 0x12
    Gate = 0x13
    Volcano = 0x14
    KeroSewers = 0x15
    NimbusCastle = 0x16
    Birdo = 0x17
    Valentina = 0x18
    Underground = 0x19
    MushroomKingdomOutside = 0x1C
    Boomer = 0x1D
    Plateau = 0x21
    SeaEnclave = 0x22
    Bundt = 0x23
    StarHill = 0x24
    Yaridovich = 0x25
    Sea = 0x26
    AxemRangers = 0x27
    CloakerDomino = 0x28
    BeanValley = 0x29
    BelomeTemple = 0x2A
    Desert = 0x2B
    Smithy = 0x2C
    SmithyFinal = 0x2D
    JinxDojo = 0x2E
    Culex = 0x2F
    Factory = 0x30
    BeanValleyUnderground = 0x31


battlefield_room_table = [
    (
        Battlefields.Forest,
        [
            Rooms._224_FOREST_MAZE_AREA_01,
            Rooms._227_FOREST_MAZE_AREA_09_LEADS_TO_4PATH_MAZE,
            Rooms._228_FOREST_MAZE_AREA_04,
        ],
    ),
    (
        Battlefields.Beanstalks,
        [
            Rooms._372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND,
            Rooms._373_NIMBUS_LAND_FALL_FROM_PLATFORM_3RD,
            Rooms._419_LAZY_SHELL_CLOUD,
        ],
    ),
    (
        Battlefields.SunkenShip,
        [
            Rooms._024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL,
            Rooms._167_SUNKEN_SHIP_AREA_05_LONG_STAIRWELL_WITH_RUNNING_ALLEY_RATS,
            Rooms._169_SUNKEN_SHIP_AREA_07_PUZZLE_ROOM_PASSAGEWAY_BRANCH_ROOM_WSHAMAN,
            Rooms._175_SUNKEN_SHIP_POSTKC_AREA_05_WDRY_BONES_LINKED_BY_MARIO_MIRROR_ROOM,
            Rooms._179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM,
            Rooms._183_SUNKEN_SHIP_POSTKC_AREA_08_SECRET_ROOM_WITH_FROG_COIN,
            Rooms._184_SUNKEN_SHIP_POSTKC_AREA_09_HIDONS_ROOM_WSAVE_POINT,
            Rooms._185_SUNKEN_SHIP_POSTKC_AREA_14_SECRET_SAFETY_RING,
            Rooms._379_BEAN_VALLEY_BEANSTALKS_AREA_02,
        ],
    ),
    (
        Battlefields.MushroomKingdom,
        [
            Rooms._017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL,
            Rooms._325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
            Rooms._031_MUSHROOM_KINGDOM_CASTLE_VAULT,
            Rooms._331_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_VAULT,
        ],
    ),
    (
        Battlefields.BowsersKeep,
        [
            Rooms._144_BOWSERS_KEEP_6DOOR_TREASURE_AFTER_EACH_ROOM,
            Rooms._446_BOWSERS_KEEP_6DOOR_EXIT_ROOM_AFTER_FINISHING_4_DOORS,
            Rooms._266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM,
            Rooms._321_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2A_SLOW_ELEVATING_PLATFORMS,
            Rooms._322_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1A_JUMPING_TERRAPIN,
            Rooms._455_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2C_VERY_SLOW_MOVING_CIRCLING_PLATFORMS,
            Rooms._457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING,
            Rooms._458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS,
            Rooms._451_BOWSERS_KEEP_AREA_07_150_COINS_AND_A_MUSHROOM,
            Rooms._453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM,
            Rooms._457_BOWSERS_KEEP_6DOOR_ACTION_ROOM_2B_CANNONBALL_RIDING,
            Rooms._458_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1B_MOVING_PLATFORMS,
            Rooms._451_BOWSERS_KEEP_AREA_07_150_COINS_AND_A_MUSHROOM,
            Rooms._453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM,
        ],
    ),
    (
        Battlefields.MushroomWay,
        [
            Rooms._077_BANDITS_WAY_AREA_03,
            Rooms._078_BANDITS_WAY_AREA_04,
            Rooms._080_ROSE_WAY_TWO_FASTFLOATING_PLATFORMS,
            Rooms._081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA,
            Rooms._203_MUSHROOM_WAY_AREA_01,
            Rooms._204_MUSHROOM_WAY_AREA_02,
            Rooms._206_BANDITS_WAY_AREA_05,
            Rooms._207_BANDITS_WAY_AREA_02,
            Rooms._267_MONSTRO_TOWN_ENTRANCE,
        ],
    ),
    (
        Battlefields.Mountains,
        [
            Rooms._100_BOOSTER_PASS_AREA_01,
            Rooms._137_LANDS_END_AREA_01,
            Rooms._138_LANDS_END_AREA_02,
            Rooms._405_BOOSTER_PASS_SECRET,
        ],
    ),
    (
        Battlefields.House,
        [
            Rooms._009_MARRYMORE_INN_REGULAR_ROOM,
            Rooms._087_ROSE_TOWN_ITEM_SHOP,
            Rooms._093_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_1F,
            Rooms._094_ROSE_TOWN_TREASURE_HOUSE_1F,
            Rooms._097_ROSE_TOWN_DURING_BOWYER_TREASURE_HOUSE_2F,
            Rooms._098_ROSE_TOWN_TREASURE_HOUSE_2F,
            Rooms._492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT,
        ],
    ),
    (
        Battlefields.BoosterTower,
        [
            Rooms._035_BOOSTER_TOWER_7F_3LEVEL_WPARACHUTING_SPOOKUMS,
            Rooms._036_BOOSTER_TOWER_6F_AREA_04_3LEVEL_WTHWOMP_ON_TEETERTOTTER,
            Rooms._048_BOOSTER_TOWER_8F_AREA_02_ZOOM_SHOES_ROOM,
            Rooms._196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS,
            Rooms._199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT,
        ],
    ),
    (
        Battlefields.Volcano,
        [
            Rooms._355_VOLCANO_AREA_03_SECRET_WTWO_FLOWERS,
            Rooms._366_VOLCANO_AREA_13_WSAVE_POINT,
            Rooms._367_VOLCANO_AREA_17_LEADS_TO_HINOPIOS_SHOP,
            Rooms._384_VOLCANO_AREA_05,
            Rooms._385_VOLCANO_AREA_06,
        ],
    ),
    (
        Battlefields.KeroSewers,
        [
            Rooms._059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS,
            Rooms._060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS,
            Rooms._125_PIPE_VAULT_AREA_04_LINE_OF_COINS_2_HIDDEN_TREASURES,
            Rooms._128_PIPE_VAULT_AREA_07_LONG_PATH_WMOVING_PLATFORMS,
            Rooms._301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS,
        ],
    ),
    (
        Battlefields.NimbusCastle,
        [
            Rooms._111_NIMBUS_CASTLE_AREA_04_LEFT_OF_4WAY_PATH_RIGHTANGLE_RED_BRICK_PATH_W_TREASURE,
            Rooms._500_NIMBUS_CASTLE_AREA_04_____DUMMY,
            Rooms._113_NIMBUS_CASTLE_AREA_16_SMALL_TWODOOR_ROOM_WTREASURE_FROM_AREA_15,
            Rooms._114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM,
            Rooms._498_NIMBUS_CASTLE_AREA_10_____DUMMY,
            Rooms._118_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_DURING_VALENTINA,
            Rooms._121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND,
            Rooms._410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE,
            Rooms._499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA,
        ],
    ),
    (Battlefields.Valentina, [Rooms._344_NIMBUS_LAND_ITEM_SHOP]),
    (
        Battlefields.Underground,
        [
            Rooms._262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS,
            Rooms._263_LANDS_END_UNDERGROUND_AREA_01,
            Rooms._270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS,
            Rooms._280_MOLEVILLE_MINES_AREA_15_2LEVEL_ROOM_WSPARKY_AND_10COIN_TC,
            Rooms._285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM,
            Rooms._288_MOLEVILLE_MINES_AREA_16_LARGE_SAVEPOINT_ROOM_WFOUR_BOBOMBS,
            Rooms._401_LANDS_END_SECRET_UNDERGROUND_AREA_02_LEADS_TO_KERO_SEWERS,
            Rooms._234_FOREST_MAZE_SECRET,
            Rooms._242_FOREST_MAZE_ALL_TREE_TRUNK_UNDERGROUND_AREAS,
        ],
    ),
    (
        Battlefields.Plateau,
        [
            Rooms._033_YOSTER_ISLE_ENTRANCE_FROM_PIPE_VAULT,
            Rooms._141_LANDS_END_AREA_04_ROTATING_FLOWERS,
        ],
    ),
    (
        Battlefields.Sea,
        [
            Rooms._132_SEA_AREA_05_FROM_AREA_02_WSAVE_POINT,
            Rooms._133_SEA_AREA_06_WATER_ROOM_WWHIRLPOOLS,
            Rooms._134_SEA_AREA_03_SUPER_STAR_ROOM,
        ],
    ),
    (
        Battlefields.BeanValley,
        [Rooms._251_BEAN_VALLEY_PIRANHA_PIPE_AREA, Rooms._252_BEAN_VALLEY_MAIN_AREA],
    ),
    (
        Battlefields.BelomeTemple,
        [
            Rooms._420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM,
            Rooms._421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE,
            Rooms._425_BELOME_TEMPLE_AREA_05_FROM_FORTUNE_ROOM,
        ],
    ),
    (
        Battlefields.Factory,
        [
            Rooms._237_SMITHY_FACTORY_AREA_05_WSAVE_POINT,
            Rooms._239_SMITHY_FACTORY_AREA_06_ULTRA_HAMMER,
            Rooms._434_SMITHY_FACTORY_AREA_09_FALLING_AXEM_REDS_ON_CONVEYOR_BELTS,
            Rooms._443_SMITHY_FACTORY_AREA_16_SMALL_ROOM_WTWO_TREASURES_AFTER_FALLING_YARIDOVICH_ROOM,
            Rooms._475_SMITHY_FACTORY_AREA_12_LOTS_OF_CONSECUTIVE_CONVEYOR_BELTS_AND_LILXXBOOS,
        ],
    ),
    (
        Battlefields.BeanValleyUnderground,
        [
            Rooms._334_BEAN_VALLEY_PIPE_ROOM_LEFTMOST_PIPE,
            Rooms._335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM,
            Rooms._348_BEAN_VALLEY_PIPE_ROOM_BOTTOM_LEFT,
            Rooms._349_BEAN_VALLEY_PIPE_ROOM_BOTTOM_RIGHT,
        ],
    ),
]


class BattleMusic(Enum):
    """Enumeration for ID values for battle music."""

    Normal = music.NormalBattleMusic
    Boss1 = music.MidbossMusic
    Boss2 = music.BossMusic
    Smithy = music.Smithy1Music
    Culex = music.CulexMusic
    Corn = music.CorndillyMusic


class HenchmanType(Enum):
    Boss = auto()
    Pack = auto()
    Event = auto()
    ExternalEvent = auto()
    NPCOnly = auto()


class SpriteSize(Enum):
    Small = auto()
    Large = auto()
    Attack = auto()


class Henchman:
    npcs = {}
    pack_number = None
    event_id = None
    henchman_type = None
    battle_type = None
    model_id = None
    sprite_offset = 0
    sequence = None


class Boss:
    name = ""
    pack_number = None
    identifier = None
    statue = None
    small_model = None
    big_model = None
    attack_model = None
    forced_background = None
    unique_henchmen = []
    repeatable_henchmen = []
    description = ""
    dialog_replacements = []
    optional_dialog_replacements = []
    eye_height = 17
    crown_height = CrownHeight.Mid
    alt_palette = None

    @property
    def classname(self):
        return self.__class__.__name__


class MimicBoss(Boss):
    challenge_script = mimic_subscript


class ModelFill:
    room_id = None
    fill_type = None
    npc_id = None
    event_id = None
    model_type = None
    minigames_only = False
    repeatable_allowed = True
    remove_if_empty = False
    occupant = None
    preferred_size = SpriteSize.Small
    dialogs = []
    target_scripts = []
    target_action_scripts = []
    sequence_setter = None
    battlefield = None
    can_run_away = False
    prefer_uncloneable = False
    prefer_south_only = False

    def __init__(
        self,
        fill_type,
        room_id,
        npc_id,
        event_id,
        occupant,
        preferred_size,
        minigames_only,
        repeatable_allowed,
        remove_if_empty,
        dialogs=[],
        target_scripts=[],
        target_action_scripts=[],
        sequence_setter=None,
        battlefield=None,
        can_run_away=False,
        prefer_uncloneable=False,
        prefer_south_only=False,
    ):
        self.fill_type = fill_type
        self.room_id = room_id
        self.npc_id = npc_id
        self.event_id = event_id
        self.preferred_size = preferred_size
        self.occupant = occupant
        self.minigames_only = minigames_only
        self.repeatable_allowed = repeatable_allowed
        self.remove_if_empty = remove_if_empty
        self.dialogs = dialogs
        self.target_scripts = target_scripts
        self.target_action_scripts = target_action_scripts
        self.sequence_setter = sequence_setter
        self.battlefield = battlefield
        self.can_run_away = can_run_away
        self.prefer_uncloneable = prefer_uncloneable
        self.prefer_south_only = prefer_south_only


class StatueFill:
    room_id = None
    npc_id = None
    sequence_setter = None

    def __init__(self, room_id, npc_id, sequence_setter):
        self.room_id = room_id
        self.npc_id = npc_id
        self.sequence_setter = sequence_setter


class BossModelFill(ModelFill):
    def __init__(
        self,
        room_id,
        npc_id,
        occupant,
        size,
        minigames_only,
        dialogs=[],
        target_scripts=[],
        target_action_scripts=[],
        sequence_setter=None,
        prefer_uncloneable=False,
        prefer_south_only=False,
    ):
        super().__init__(
            HenchmanType.Boss,
            room_id,
            npc_id,
            None,
            occupant,
            size,
            minigames_only,
            False,
            False,
            dialogs,
            target_scripts,
            target_action_scripts,
            sequence_setter,
            None,
            prefer_uncloneable,
            prefer_south_only,
        )


class UniqueHenchmanFill(ModelFill):
    def __init__(
        self,
        room_id,
        npc_id,
        occupant,
        minigames_only,
        repeatable_allowed,
        remove_if_empty,
        fill_type,
        event_id=None,
        dialogs=[],
        target_scripts=[],
        target_action_scripts=[],
        sequence_setter=None,
        battlefield=None,
        can_run_away=False,
        prefer_uncloneable=False,
        prefer_south_only=False,
    ):
        super().__init__(
            fill_type,
            room_id,
            npc_id,
            event_id,
            occupant,
            SpriteSize.Small,
            minigames_only,
            repeatable_allowed,
            remove_if_empty,
            dialogs,
            target_scripts,
            target_action_scripts,
            sequence_setter,
            battlefield,
            can_run_away,
            prefer_uncloneable,
            prefer_south_only,
        )


class RepeatableHenchmanFill(ModelFill):
    def __init__(
        self,
        room_id,
        npc_id,
        occupant,
        minigames_only,
        remove_if_empty,
        fill_type,
        event_id=None,
        dialogs=[],
        target_scripts=[],
        target_action_scripts=[],
        sequence_setter=None,
        battlefield=None,
        can_run_away=False,
        prefer_uncloneable=False,
        prefer_south_only=False,
    ):
        super().__init__(
            fill_type,
            room_id,
            npc_id,
            event_id,
            occupant,
            SpriteSize.Small,
            minigames_only,
            True,
            remove_if_empty,
            dialogs,
            target_scripts,
            target_action_scripts,
            sequence_setter,
            battlefield,
            can_run_away,
            prefer_uncloneable,
            prefer_south_only,
        )


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
        val = 0xFF if self.has_star else 0x00
        patch.add_data(self.star_address, utils.ByteField(val).as_bytes())

        return patch


class BossLocation:
    """Class for boss fight locations."""

    # Boss fight data
    battle_address = 0x0
    pack_number = 0
    battlefield = None
    can_run_away = False
    music = music.NormalBattleMusic
    wide_sprite = False
    tall_sprite = False
    sprite_width = 32
    sprite_height = 32
    description = ""

    boss = None
    boss_locations = []
    unique_henchmen = []
    repeatable_henchmen = []
    statue_locations = []
    dialogs_to_replace = []

    _identifier = None
    _grant_identifier = None

    def __init__(self, world):
        """

        Args:
            world (randomizer.logic.main.GameWorld):

        """
        self.world = world

        # Get actual pack object based on the pack number.
        self.pack = self.world.get_formation_pack_by_index(self.boss.pack_number)

    def __str__(self):
        return "<{}: music {}, members {}>".format(
            self.name, self.music, [m.enemy for m in self.formation.members]
        )

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
        return self.world.get_formation_pack_by_index(self.boss.pack_number).formations[
            0
        ]

    @property
    def identifier(self):
        return self._identifier

    @property
    def grant_identifier(self):
        if self._grant_identifier is None:
            return self._identifier
        return self._grant_identifier

    def get_patch(self):
        """

        Returns:
            randomizer.logic.patch.Patch: Patch data

        """
        patch = Patch()

        # Add boss data.
        data = bytearray()
        data += utils.ByteField(0x4A).as_bytes()
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
            self.name, self.has_star, self.music, self.boss
        )

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
    name = "Hammer Bro"
    pack_number = 183
    small_model = npcs.HammerBroSmall
    big_model = npcs.HammerBroLarge
    statue = npcs.HammerBroStatue
    dialog_replacements = [
        (49, """HAMMER BRO: Alright already,\n you won, now go away![await]"""),
        (
            1660,
            """ So, you figured it out... But you\n gotta get past my hammer to get\n through![await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n the Hammer Bros' place.[await]""",
        ),
        (
            1695,
            """PIRATE: That's AMAZING!\n No one's EVER whipped\n the HAMMER BROS!![await]""",
        ),
        (
            1778,
            """HAMMER BRO: ...grumble...\n My hammer's embarrassed about\n losing...[await]""",
        ),
        (1780, """HAMMER BRO: What're YOU lookin' at?[await]"""),
        (
            1781,
            """HAMMER BRO: Look buddy, you\n already won, you can get off of my\n hammer now.[await]""",
        ),
        (
            1783,
            """ After getting hammered, [await]\n I always drink Carrot Juice.[await]""",
        ),
        (
            1784,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1785,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1793,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            2061,
            """CHEF TORTE: Zees cake, ve make\n it look like big hammer! It is...\n masterpiece![await]""",
        ),
        (
            2504,
            """HAMMER BRO: You better find [0x7024]\n more of `MARRYMORE_CHARACTER`'s things,\n or my hammer'll be angry![await]""",
        ),
        (
            2560,
            """SNIFIT 1: Hello there.[await]\n The Hammer Bros are busy right\n now, so they can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        ),
        (2572, """SNIFIT 2: Please refrain\n from bothering the Hammer Bros.[await]"""),
        (2831, """HAMMER BRO: What're YOU lookin'\n at?[await]"""),
        (
            2838,
            """ You will find the Hammer Bro...\n in his house. He is...the most\n respected person here.[await]""",
        ),
        (
            3044,
            """HAMMER BRO: The dojo master\n takes on 3 different forms.\n Me, though? I'm just a hammer.[await]""",
        ),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Hammer-this and Hammer-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, """HAMMER BRO: I guess you were\n tougher than I thought![await]"""),
        (3353, """HAMMER BRO: I guess you were\n tougher than I thought![await]"""),
    ]


class Croco1Boss(Boss):
    name = "Croco"
    pack_number = 163
    small_model = npcs.Croco
    statue = npcs.CrocoStatue
    dialog_replacements = [
        (49, """\n CROCO: Get the heck outta here![await]"""),
        (
            1660,
            """ Alright, alright, so ya figured out\n my password! But I ain't goin'\n down without a fight![await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Croco's place.[await]""",
        ),
        (1695, """PIRATE: That's AMAZING!\n No one's EVER whipped CROCO!![await]"""),
        (1778, """CROCO: Enough already, get outta\n here![await]"""),
        (1780, """CROCO: Back already? How 'bout a\n drink?[await]"""),
        (1781, """\n    CROCO: 'Dis some kinda joke?[await]"""),
        (
            1783,
            """ Wanna know how I run so fast?[await]\n Chug some Honey Syrup, chump![await]""",
        ),
        (
            1784,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1785,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1793,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            2061,
            """CHEF TORTE: Zees cake, ve make\n it look like big reptile! It is...\n masterpiece![await]""",
        ),
        (
            2504,
            """CROCO: What's dis?[await][pause] You fools're\n gonna take another 100 years to\n find the last [0x7024] item(s)![await]""",
        ),
        (
            2560,
            """SNIFIT 1: Hello there.[await]\n Croco's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        ),
        (2572, """SNIFIT 2: Please refrain\n from bothering Croco.[await]"""),
        (2831, """CROCO: Whaddya doin' hangin\n 'round here?[await]"""),
        (
            2838,
            """ You will find Croco...\n in his house. He is...the most\n respected person here.[await]""",
        ),
        (
            3044,
            """CROCO: Think ya can beat the dojo\n master, chump? I'd like to see ya\n try![await]""",
        ),
        (
            3057,
            """ Whaddya want, bub?[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        ),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Wallet-this and Coin-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, """CROCO: I hate to say it, but...\n I kinda like this![await]"""),
        (3353, """CROCO: I hate to say it, but...\n I kinda like this![await]"""),
    ]


class MackShyster1(Henchman):
    pack_number = 194
    model = npcs.Shyster


class MackShyster2(Henchman):
    pack_number = 195
    model = npcs.Shyster


class DefaultShyster1(Henchman):
    pack_number = 10
    model = npcs.Shyster


class DefaultShyster2(Henchman):
    pack_number = 11
    model = npcs.Shyster


class MackBoss(Boss):
    name = "Mack"
    pack_number = 179
    small_model = npcs.MackSmall
    big_model = npcs.MackMedium
    attack_model = npcs.MackLarge
    statue = npcs.MackStatue
    unique_henchmen = [MackShyster1, MackShyster2, MackShyster1, MackShyster2]
    repeatable_henchmen = [MackShyster1, MackShyster2]
    dialog_replacements = [
        (49, """MACK: Party's over. I'm going to\n sleep.[await]"""),
        (
            1660,
            """ Listen, bub![await]\n You may have figured out my\n password, but you still gotta get\n past me if you want through![await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Mack's place.[await]""",
        ),
        (1695, """PIRATE: That's AMAZING!\n No one's EVER whipped MACK!![await]"""),
        (1778, """\n   MACK: Guess the party's over.[await]"""),
        (
            1780,
            """MACK: Hey `MAIN_CHARACTER_NAME`!\n Come back to crash our party?[await]""",
        ),
        (1781, """MACK: OK, I get it, you can bounce\n too.[await]"""),
        (
            1783,
            """ I don't care what kinda party it is![await]\n I drink Milk so I can be like Exor!![await]""",
        ),
        (
            1784,
            """BODYGUARD: There's no hard\n feelings. We're all just trying to\n have a good time.[await]""",
        ),
        (
            1793,
            """BODYGUARD: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """BODYGUARD: There's no hard\n feelings. We're all just trying to\n have a good time.[await]""",
        ),
        (
            1785,
            """BODYGUARD: There's no hard\n feelings. We're all just trying to\n have a good time.[await]""",
        ),
        (2061, """BODYGUARD: Doesn't this cake\n look just like Mack?[await]"""),
        (2062, """BODYGUARD: We've gotten REAL\n good with fondant![await]"""),
        (
            2504,
            """MACK: I'm not happy to delay the\n party, but we can't get started\n until you find [0x7024] more item(s)![await]""",
        ),
        (
            2560,
            """BODYGUARD: Welcome![await][pause]\n Our party is invitation-only, so\n please come back another time.[await][page]\n[delay] ...You're here to crash it anyway?[delay]\n Alright, wise guy, let's go![await]""",
        ),
        (2572, """\n   BODYGUARD: Oh, no you don't![await]"""),
        (2831, """\n   MACK: What are you doing here?[await]"""),
        (
            2832,
            """ Yo! You look tired.[delay] How 'bout a\n night on the house?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        ),
        (
            2834,
            """ The two guys in the left building\n have been acting suspicious.[await]""",
        ),
        (
            2837,
            """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        ),
        (2838, """ Have you been to Mack's house\n up on the hill yet?[await]"""),
        (
            2839,
            """ Yo! It's fine if you hang out in\n town, but... [delay]stay away from the\n shed![await]""",
        ),
        (
            2841,
            """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        ),
        (
            2842,
            """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        ),
        (2843, """ Once you get through the Sunken\n Ship, you can... er...[await]"""),
        (
            2844,
            """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        ),
        (2845, """ You trying to snoop on what I'm\n buying here?[await]"""),
        (2847, """\n       What're YOU lookin' at?[await]"""),
        (2848, """\n               Beat it, bub![await]"""),
        (3044, """MACK: Think you're gonna beat the\n dojo master today?[await]"""),
        (
            3057,
            """ You come to crash my party?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        ),
        (
            3072,
            """BODYGUARD: I almost feel bad\n for all those fools out there,\n who can't even bounce...[await]""",
        ),
        (
            3073,
            """BODYGUARD: How 'bout a fat lip to\n go with that ugly moustache?[await]""",
        ),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Bouncing-this and Party-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, """MACK: I guess you CAN bounce\n after all.[await]"""),
        (3353, """MACK: I guess you CAN bounce\n after all.[await]"""),
    ]
    optional_dialog_replacements = [
        (
            1694,
            """BODYGUARD: Think you're tough,\n pal?[await][delay] March that ugly mustache into\n Mack's room, and see what\n happens![await]""",
        ),
        (
            1695,
            """BODYGUARD: You beat Mack?[await]\n This is not good![delay_30]\n I guess you can bounce after all.[await]""",
        ),
    ]


class PandoriteBoss(MimicBoss):
    name = "Pandorite"
    pack_number = 156
    small_model = npcs.PandoriteSmall
    big_model = npcs.PandoriteLarge
    statue = npcs.MimicStatue
    dialog_replacements = [
        (49, """PANDORITE: That thing was making\n me sick...[await]"""),
        (
            1660,
            """ So, you cracked the code. I'm\n warning you though, I hate being\n woken up.[await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Pandorite's place.[await]""",
        ),
        (
            1695,
            """PIRATE: That's AMAZING!\n No one's EVER whipped \nPANDORITE!![await]""",
        ),
        (
            1778,
            """PANDORITE: Whatever... Leave me\n alone so I can go back to sleep.[await]""",
        ),
        (
            1780,
            """PANDORITE: I think I like this place\n more than the sewers. It smells\n marginally better.[await]""",
        ),
        (
            1781,
            """PANDORITE: I can't tell if this is\n better or worse without the\n protection of my box.[await]""",
        ),
        (
            1783,
            """ Here, you can have my...um...[await]\n '21 Redtail Chardonnay.[delay] It's fine.[await]""",
        ),
        (
            1784,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1785,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1793,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            2061,
            """CHEF TORTE: Zees cake, ve make\n it look like mimic! It is...\n masterpiece![await]""",
        ),
        (
            2504,
            """PANDORITE: Sorry, you can't skip\n getting the last [0x7024] item(s).[await]""",
        ),
        (
            2560,
            """SNIFIT 1: Hello there.[await]\n Pandorite's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        ),
        (2572, """SNIFIT 2: Please refrain\n from bothering Pandorite.[await]"""),
        (2831, """PANDORITE: There's not much to do\n around here.[await]"""),
        (
            2838,
            """ You will find Pandorite...\n in his house. He is...the most\n respected person here.[await]""",
        ),
        (
            3044,
            """PANDORITE: Now this should be\n interesting. Can you beat THE\n master, `MAIN_CHARACTER_NAME`?[await]""",
        ),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Treasure-this and Ghost-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, """PANDORITE: ...I'm not sure how\n I'm accomplishing this.[await]"""),
        (3353, """PANDORITE: ...I'm not sure how\n I'm accomplishing this.[await]"""),
    ]


class Belome1Boss(Boss):
    name = "Belome"
    pack_number = 168
    small_model = npcs.Belome1Small
    big_model = npcs.Belome1Large
    statue = npcs.SmallBelomeStatue
    dialog_replacements = [
        (49, """\n        BELOME: Good night~![await]"""),
        (
            1660,
            """ Oh, is it dinner time already?\n Come on in...[delay_60] if you dare~![await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Belome's place.[await]""",
        ),
        (1695, """PIRATE: That's AMAZING!\n No one's EVER whipped BELOME!![await]"""),
        (
            1778,
            """BELOME: You look tasty! If you\n stick around any longer, I might\n just have a snack![await]""",
        ),
        (1780, """BELOME: Oh, you're back![await]\n Did you bring any food?[await]"""),
        (
            1781,
            """BELOME: Say, it's past my bedtime.\n Can you get off of my head?[await]""",
        ),
        (
            1783,
            """ I'm always STARVING~![await]\n...but I hydrate with Filtered Water.[await]""",
        ),
        (
            1784,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1785,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1793,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            2061,
            """CHEF TORTE: Zees cake, ve make\n it look like big dog! It is...\n masterpiece![await]""",
        ),
        (
            2504,
            """BELOME: Oh, no, you're still\n missing [0x7024] item(s).[await][pause] I can't wait any\n longer to see what today's cake\n will be.[await][pause] I'm STARVING![await]""",
        ),
        (
            2560,
            """SNIFIT 1: Hello there.[await]\n Belome's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        ),
        (2572, """SNIFIT 2: Please refrain\n from bothering Belome.[await]"""),
        (2831, """BELOME: It's dreadfully boring\n around here~![await]"""),
        (
            2838,
            """ You will find Belome...\n in his house. He is...the most\n respected person here.[await]""",
        ),
        (
            3044,
            """BELOME: Ooh, how exciting~!\n [delay]The dojo master has challenged\n you![await]""",
        ),
        (
            3057,
            """ Are you the pizza delivery person?[await]\n  [select] (I'm here to fight you)\n  [select] (Sorry, wrong door)[await]""",
        ),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Scarecrow-this and Hungry-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (
            3352,
            """BELOME: This training regimen is\n giving me quite the appetite![await]""",
        ),
        (
            3353,
            """BELOME: This training regimen is\n giving me quite the appetite![await]""",
        ),
    ]


class BowyerAero(Henchman):
    pack_number = 160
    model = npcs.AeroUpright


class BowyerBoss(Boss):
    name = "Bowyer"
    pack_number = 181
    small_model = npcs.BowyerSmall
    big_model = npcs.BowyerOverworld
    attack_model = npcs.BowyerLarge
    statue = npcs.BowyerStatue
    unique_henchmen = [
        BowyerAero,
        BowyerAero,
        BowyerAero,
        BowyerAero,
        BowyerAero,
        BowyerAero,
        BowyerAero,
        BowyerAero,
    ]
    repeatable_henchmen = [BowyerAero]
    dialog_replacements = [
        (49, """BOWYER: Disturb me you must not,\n nya!"""),
        (
            1660,
            """ Nya, NYA?![delay_30] Cracked the code, you\n did! But fight you, I will, nya![await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Bowyer's place.[await]""",
        ),
        (1695, """PIRATE: That's AMAZING!\n No one's EVER whipped BOWYER!![await]"""),
        (1778, """BOWYER: That was nyat fair!\n Scram you must, nya![await]"""),
        (
            1780,
            """BOWYER: Back again, you are,\n nya? I'm nyat as mad as before.[await]""",
        ),
        (1781, """BOWYER: Nya, NYA?! Stop this,\n you must![await]"""),
        (
            1783,
            """ Nya, Nya, NYA!  Make like Locke![await]\n Bring me more Strongbow Cider![await]""",
        ),
        (
            1784,
            """FLUNKIE: Bowyer is easily\n distracted from his missions. But\n we're off the hook today.[await]""",
        ),
        (
            1793,
            """FLUNKIE: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """FLUNKIE: Bowyer is easily\n distracted from his missions. But\n we're off the hook today.[await]""",
        ),
        (
            1785,
            """FLUNKIE: Bowyer is easily\n distracted from his missions. But\n we're off the hook today.[await]""",
        ),
        (2061, """FLUNKIE: Doesn't this cake\n look just like Bowyer?[await]"""),
        (2062, """FLUNKIE: We've gotten REAL\n good with fondant![await]"""),
        (
            2504,
            """BOWYER: Nya, NYA!?[await][pause] Disturb me\n you must not, until [0x7024] more item(s)\n you find, nya![await]""",
        ),
        (
            2560,
            """FLUNKIE: Hello.[await][pause] Bowyer is busy\n now, and he really hates to be\n interrupted.[await][page]\n[delay] ...If you're not going to leave,\n I'll have to kick you out myself![await]""",
        ),
        (
            2572,
            """FLUNKIE: I'm gonna have to ask you\n not to interrupt Bowyer's target\n practice.[await]""",
        ),
        (2831, """\nBOWYER: Nya! Boring here, it is...[await]"""),
        (
            2832,
            """ Since I'm having a good day, you\n can stay here free of charge.\n [delay]How's that sound?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        ),
        (
            2834,
            """ The two guys in the left building\n have been acting suspicious.[await]""",
        ),
        (
            2837,
            """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        ),
        (2838, """ Have you been to Bowyer's house\n up on the hill yet?[await]"""),
        (
            2839,
            """ Don't cause any trouble in our\n town! Stay away from the shed![await]""",
        ),
        (
            2841,
            """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        ),
        (
            2842,
            """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        ),
        (2843, """ Once you get through the Sunken\n Ship, you can... er...[await]"""),
        (
            2844,
            """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        ),
        (2845, """ I'm just a customer![delay] Let me shop\n in peace![await]"""),
        (
            2847,
            """ There's a very uh... [delay]important\n meeting happening inside.\n [delay]You may not enter.[await]""",
        ),
        (
            2848,
            """ What's going on in here?[await][pause] None of\n your business, that's what![await]""",
        ),
        (3044, """\n BOWYER: Interesting, this will be![await]"""),
        (
            3057,
            """ Fight me, you will, nya?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        ),
        (
            3072,
            """FLUNKIE: ...sigh... [delay]Bowyer scolded\n me for interrupting his shooting\n practice.[await][pause] I was just trying to warn\n him that `MAIN_CHARACTER_NAME` is here![await]""",
        ),
        (3073, """FLUNKIE: You look like you'd make\n for a good statue![await]"""),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Arrow-this and Target-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, """BOWYER: 1000 jumps I must do,\n nya![await]"""),
        (3353, """BOWYER: 1000 jumps I must do,\n nya![await]"""),
    ]
    optional_dialog_replacements = [
        (
            1694,
            """FLUNKIE: Whoa! You sure showed\n us! Go on ahead to Bowyer's\n place![await]""",
        ),
        (
            1695,
            """FLUNKIE: Come back and visit\n us sometime. Bowyer won't stay\n mad forever![await]""",
        ),
    ]


class Croco2Crook(Henchman):
    pack_number = 141
    model = npcs.Crook


class DefaultCrook(Henchman):
    pack_number = 199
    model = npcs.Crook


class Croco2Boss(Boss):
    name = "Croco"
    pack_number = 164
    small_model = npcs.Croco2
    statue = npcs.CrocoStatue
    unique_henchmen = [Croco2Crook, Croco2Crook, Croco2Crook]
    repeatable_henchmen = [Croco2Crook]
    dialog_replacements = [
        (49, """\n CROCO: Get the heck outta here![await]"""),
        (
            1660,
            """ Alright, alright, so ya figured out\n my password! But I ain't goin'\n down without a fight![await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Croco's place.[await]""",
        ),
        (1695, """PIRATE: That's AMAZING!\n No one's EVER whipped CROCO!![await]"""),
        (1778, """CROCO: Enough already, get outta\n here![await]"""),
        (1780, """CROCO: Back already? How 'bout a\n drink?[await]"""),
        (1781, """\n    CROCO: 'Dis some kinda joke?[await]"""),
        (
            1783,
            """ I tapped Canada's Maple Syrup[await]\n Reserve. They'll NEVER catch me!![await]""",
        ),
        (
            1784,
            """FLUNKIE: To be honest, Croco's not\n really a bad guy.[await][pause] I guess that's why\n we follow him.[await]""",
        ),
        (
            1793,
            """FLUNKIE: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """FLUNKIE: To be honest, Croco's not\n really a bad guy.[await][pause] I guess that's why\n we follow him.[await]""",
        ),
        (
            1785,
            """FLUNKIE: To be honest, Croco's not\n really a bad guy.[await][pause] I guess that's why\n we follow him.[await]""",
        ),
        (2061, """FLUNKIE: Doesn't this cake\n look just like Croco?[await]"""),
        (2062, """FLUNKIE: We've gotten REAL\n good with fondant![await]"""),
        (
            2560,
            """FLUNKIE: Croco's busy! Scram![await]\n[delay_60] ...Not leaving, huh?\n[delay] Alright buddy, you asked for it![await]""",
        ),
        (2572, """FLUNKIE: Where d'ya think YOU'RE\n going?![await]"""),
        (2831, """CROCO: Whaddya doin' hangin\n 'round here?[await]"""),
        (
            2832,
            """ You tired? You can stay here\n for free.[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        ),
        (
            2834,
            """ The two guys in the left building\n have been acting suspicious.[await]""",
        ),
        (
            2837,
            """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        ),
        (2838, """ Have you been to Croco's house\n up on the hill yet?[await]"""),
        (2839, """ You better not be snooping around\n the shed![await]"""),
        (
            2841,
            """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        ),
        (
            2842,
            """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        ),
        (2843, """ Once you get through the Sunken\n Ship, you can... er...[await]"""),
        (
            2844,
            """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        ),
        (
            2845,
            """ Huh?[delay] What am I doing here?[delay] None\n of your business, that's what![await]""",
        ),
        (2847, """\n           Nothin' to see here.[await]"""),
        (2848, """ Nope, nothing suspicious going on\n in this house![await]"""),
        (
            3044,
            """CROCO: Think ya can beat the dojo\n master, chump? I'd like to see ya\n try![await]""",
        ),
        (
            3057,
            """ Whaddya want, bub?[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        ),
        (3072, """\n  FLUNKIE: I could use a stepstool.[await]"""),
        (3073, """\n      FLUNKIE: A tough guy, eh?[await]"""),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Wallet-this and Coin-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, """CROCO: I hate to say it, but...\n I kinda like this![await]"""),
        (3353, """CROCO: I hate to say it, but...\n I kinda like this![await]"""),
    ]
    optional_dialog_replacements = [
        (
            1694,
            """FLUNKIE: (Sob, sob...)[delay_30]\n You're pretty tough. I guess I'll let\n you through to Croco's place.[await]""",
        ),
        (
            1695,
            """FLUNKIE: You beat Croco!?[delay_30]\n We'll getcha for this![await][page]\n Maybe not today, maybe not\n tomorrow, but someday...[await]""",
        ),
    ]


# loop a few times since no duration


class PunchinelloBobomb(Henchman):
    pack_number = 1
    model = npcs.BobOmb


class DefaultMicrobomb(Henchman):
    pack_number = None
    model = npcs.Microbomb


class DefaultBobomb(Henchman):
    pack_number = 36
    model = npcs.BobOmb


class PunchinelloBoss(Boss):
    name = "Punchinello"
    pack_number = 140
    small_model = npcs.PunchinelloSmall
    big_model = npcs.PunchinelloLarge
    statue = npcs.PunchinelloStatue
    unique_henchmen = [
        PunchinelloBobomb,
        PunchinelloBobomb,
        PunchinelloBobomb,
        PunchinelloBobomb,
    ]
    repeatable_henchmen = [PunchinelloBobomb]
    dialog_replacements = [
        (49, """PUNCHINELLO: Grrr... Leave me\n alone![await]"""),
        (
            1660,
            """ So... You figured out my\n password.[await]\n If you're not here for an\n autograph, I'll have to test you\n once more to let you through![await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Punchinello's place.[await]""",
        ),
        (
            1695,
            """PIRATE: That's AMAZING!\n No one's EVER whipped\n PUNCHINELLO!![await]""",
        ),
        (1778, """PUNCHINELLO: Grrr... I'll never get famous\n at this rate![await]"""),
        (
            1780,
            """PUNCHINELLO: You've come back to\n visit? I truly must be famous![await]""",
        ),
        (
            1781,
            """PUNCHINELLO: They say I'm a hot\n head, so it's a bad idea to stand\n on my head.[await]""",
        ),
        (
            1783,
            """ WATCH ME DRINK THIS TOBASCO![await]\n I'm gonna be youtube-famous![await]""",
        ),
        (1785, """\n      BOB-OMB: I need a break.[await]"""),
        (
            1793,
            """BOB-OMB: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        ),
        (1792, """\n      BOB-OMB: I need a break.[await]"""),
        (1784, """\n      BOB-OMB: I need a break.[await]"""),
        (2061, """BOB-OMB: Doesn't this cake\n look just like Punchinello?[await]"""),
        (2062, """BOB-OMB: We've gotten quite\n good with fondant.[await]"""),
        (
            2504,
            """PUNCHINELLO: Huh?[delay_30] What the hay?[await]\n Where are the other [0x7024] item(s)?[await]""",
        ),
        (
            2560,
            """BOB-OMB: Hello there.[await][pause] If you've\n come for Punchinello's autograph,\n please allow me to buzz you up...[await][page]\n [delay]...You're not here for that?[await]\n [delay]Uh oh, he'll be pretty mad!\n [delay]I'd better do something![await]""",
        ),
        (
            2572,
            """BOB-OMB: There's nothing to see\n back here...[await][pause] I mean that.[await]\n You don't believe me?[await]""",
        ),
        (
            2831,
            """PUNCHINELLO: Hmmm... [delay]Huh?\n [delay]A visitor? [delay]Well, there's not much\n to do around here.[await]""",
        ),
        (
            2832,
            """ Hello there.[await][pause] Today, we've got an\n explosively good deal for you![delay] All\n inn expenses are free of charge.[await]\n Would you like to stay?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        ),
        (
            2834,
            """ The two guys in the left building\n have been acting suspicious.[await]""",
        ),
        (
            2837,
            """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        ),
        (
            2838,
            """ Have you been to Punchinello's\n house up on the hill yet?[await]""",
        ),
        (
            2839,
            """ Hello there.[delay] Welcome to our humble\n town. We have the least suspicious\n shed in all the land.[await]""",
        ),
        (
            2841,
            """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        ),
        (
            2842,
            """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        ),
        (2843, """ Once you get through the Sunken\n Ship, you can... er...[await]"""),
        (
            2844,
            """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        ),
        (
            2845,
            """ I know how this must look, but I'm\n just here to browse the perfectly\n legal goods they're selling.[await]""",
        ),
        (
            2847,
            """ Hello there.[delay] Sorry, but I can't let\n you through this door today.[await]""",
        ),
        (
            2848,
            """ You wouldn't wanna enter this\n house, oh no.[delay] We'll make sure you\n don't enter by accident.[await]""",
        ),
        (
            3044,
            """PUNCHINELLO: A challenge from\n the dojo master, eh? Let's see\n where this goes.[await]""",
        ),
        (
            3057,
            """ Hello. Are you with the press?[await]\n  [select] (I'm here to fight you)\n  [select] (Sorry, wrong number)[await]""",
        ),
        (
            3072,
            """BOB-OMB: I don't look like the\n other bob-ombs here. [delay]That's weird.[await]""",
        ),
        (
            3073,
            """BOB-OMB: You don't think it makes\n sense for a bob-omb to be shooting\n bullets?[await][pause] ...Fight me about it![await]""",
        ),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Bomb-this and Famous-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (
            3352,
            """PUNCHINELLO: Will this training\n montage be my ticket to stardom?[await]""",
        ),
        (
            3353,
            """PUNCHINELLO: Will this training\n montage be my ticket to stardom?[await]""",
        ),
    ]
    optional_dialog_replacements = [
        (
            1694,
            """BOB-OMB: I guess I was a little\n hot-headed, thinking I could win.\n Go on in to Punchinello's room.[await]""",
        ),
        (
            1695,
            """BOB-OMB: Wow, you beat\n Punchinello! He's not very happy\n about that.[await]""",
        ),
    ]


class BoosterSnifit(Henchman):
    pack_number = 0
    model = npcs.Snifit


# Remove sequences from zoom animation if not snifit
class BoosterHillSnifit(Henchman):
    pack_number = None
    model = npcs.BackSnifit


class DefaultSnifit(Henchman):
    pack_number = 142
    model = npcs.Snifit


class BoosterApprentice(Henchman):
    pack_number = 32
    model = npcs.Apprentice


class BoosterBoss(Boss):
    name = "Booster"
    pack_number = 161
    small_model = npcs.Booster
    statue = npcs.BoosterStatue
    unique_henchmen = [BoosterSnifit, BoosterSnifit, BoosterSnifit]
    repeatable_henchmen = [BoosterApprentice]
    dialog_replacements = [
        (
            49,
            """BOOSTER: It's pretty cozy in here.[await][pause]\n No, you can't come in![await]""",
        ),
        (
            1660,
            """ Eh?[delay_30] THAT was my password?![delay_30]\n I'd better fight you, just to be\n sure.[await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Booster's place.[await]""",
        ),
        (1695, """PIRATE: That's AMAZING!\n No one's EVER whipped BOOSTER!![await]"""),
        (
            1778,
            """BOOSTER: I'd love to entertain\n you, but I'm busy watching the\n fish. Come back later.[await]""",
        ),
        (
            1780,
            """BOOSTER: Eh...? My! It's you\n again![await][page]\n  We're having a heated debate over\n what a “party” is, so you can stay\n if you'd like to contribute.[await]""",
        ),
        (1781, """BOOSTER: Hm? How's the view up there?[await]"""),
        (
            1783,
            """ This Dish Detergent is DELICIOUS![await]\n Number 2, (belch) MORE SOAP!!![await]""",
        ),
        (
            1784,
            """SNIFIT 1: There's a 70% chance the\n drink on the table is actually\n punch.[await]""",
        ),
        (
            1785,
            """SNIFIT 2: Booster can't find any\n beetles underwater, but he still\n enjoys watching the fish.[await]""",
        ),
        (
            1792,
            """SNIFIT 3: Uh... Do you know where\n we could get some cake down here?[await]""",
        ),
        (2061, """SNIFIT 2: Doesn't this cake\n look just like Booster?[await]"""),
        (
            2062,
            """SNIFIT 3: Uh... I think we should\n have made his mustache bigger.[await]""",
        ),
        (2831, """\n   BOOSTER: Found our town, eh?[await]"""),
        (
            2832,
            """SNIFIT 1: Welcome![delay] How would you\n like to stay in our fabulous inn\n for free today?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        ),
        (
            2834,
            """ The two guys in the left building\n have been acting suspicious.[await]""",
        ),
        (
            2837,
            """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        ),
        (2838, """ Have you been to Booster's\n house up on the hill yet?[await]"""),
        (2839, """\n You'd better not go near our shed![await]"""),
        (
            2841,
            """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        ),
        (
            2842,
            """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        ),
        (2843, """ Once you get through the Sunken\n Ship, you can... er...[await]"""),
        (
            2844,
            """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        ),
        (
            2845,
            """ I'm facing a promotion. Do they sell\n anything here that'll make me look\n more professional?[await]""",
        ),
        (
            2847,
            """SNIFIT 3: Uh... Don't look in the\n window. [delay]Pretty please.[await]""",
        ),
        (2848, """SNIFIT 2: There is nothing of\n interest to you in here.[await]"""),
        (
            3044,
            """BOOSTER: I wonder if the dojo\n master can shape-shift into a\n Mario doll.[await]""",
        ),
        (
            3057,
            """ Eh? What'd you come here for?[await]\n  [select] (I want a fight)\n  [select] (Uh...)[await]""",
        ),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Beetle-this and Train-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (
            3352,
            """BOOSTER: Eh?[await][pause] ...Training?[delay_15] What training?[await]""",
        ),
        (
            3353,
            """BOOSTER: Eh?[await][pause] ...Training?[delay_15] What training?[await]""",
        ),
    ]
    optional_dialog_replacements = [
        (
            1694,
            """APPRENTICE: Oh, dear![delay] We've\n failed to keep the intruder away\n from Booster![await]""",
        ),
        (
            1695,
            """APPRENTICE: Booster's not happy\n about losing. Please do not jump\n on his head.[await]""",
        ),
    ]


class GrateGuyKnifeGuy(Henchman):
    pack_number = None
    model = npcs.KnifeGuyGridplane


class GrateGuyBoss(Boss):
    name = "Grate Guy"
    pack_number = 177
    small_model = npcs.GrateGuySmall
    big_model = npcs.GrateGuyLarge
    statue = npcs.GrateGuyStatue
    unique_henchmen = [GrateGuyKnifeGuy]
    dialog_replacements = [
        (49, """GRATE GUY: Get lost, buddy, I'm\n busy![await]"""),
        (
            1660,
            """ Oh, a patron![delay_30] Come on in and let's\n get this show on the road![await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Knife Guy and Grate Guy's place.[await]""",
        ),
        (
            1695,
            """PIRATE: That's AMAZING!\n No one's EVER whipped KNIFE GUY\n and GRATE GUY!![await]""",
        ),
        (
            1778,
            """GRATE GUY: Yikes, you're pretty\n tough! I need some time to recover.[await]""",
        ),
        (
            1780,
            """GRATE GUY: It's so boring\n around here... Hey, wanna play\n "Look the other way" with me?[await][page]\n Hah! [delay_30]Just kidding![await]""",
        ),
        (
            1781,
            """GRATE GUY: Sorry, `MAIN_CHARACTER_NAME`,\n but jumping on my head isn't going\n to teach you Blizzard.[await]""",
        ),
        (
            1783,
            """ Of course I didn't shake it up!![await]\n Go on, have a Root Beer!![await]""",
        ),
        (
            1784,
            """KNIFE GUY: No, I'm not giving you the Bright Card down here![await]""",
        ),
        (
            2061,
            """CHEF TORTE: Zees cake, ve make\n it look like big clown! It is...\n masterpiece![await]""",
        ),
        (
            2504,
            """GRATE GUY: Hm?[await][pause] Well, you took all\n the trouble to find [0x7000] item(s),\n so... keep looking for the other [0x7024]![await]\n I can stick around all day.[await]""",
        ),
        (
            2560,
            """SNIFIT 1: Hello there.[await]\n Knife Guy and Grate Guy are busy\n right now, so they can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        ),
        (
            2572,
            """SNIFIT 2: Please refrain\n from bothering Knife Guy and\n Grate Guy.[await]""",
        ),
        (2831, """GRATE GUY: Gee, it sure is boring\n around here![await]"""),
        (
            2838,
            """ You will find Grate Guy...\n in his house. He is...the most\n respected person here.[await]""",
        ),
        (
            3044,
            """GRATE GUY: The dojo master's\n much tougher than I am. Think you\n can win?[await]""",
        ),
        (
            3057,
            """ Welcome! What brings you here?[await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        ),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the people\n next door.[await][page]\n They're always mumbling about\n Knife-this and Casino-that.[await][page]\n Sometimes I'd like to ask them what\n they're babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (
            3352,
            """GRATE GUY: Look, `MAIN_CHARACTER_NAME`!\n I've been training so hard, that my\n ball jumps with me![await]""",
        ),
        (
            3353,
            """GRATE GUY: Look, `MAIN_CHARACTER_NAME`!\n I've been training so hard, that my\n ball jumps with me![await]""",
        ),
    ]


class BundtTorte1(Henchman):
    pack_number = 54
    model = npcs.Torte


class BundtTorte2(Henchman):
    pack_number = 55
    model = npcs.Torte


class BundtBoss(Boss):
    name = "Bundt"
    pack_number = 176
    small_model = npcs.BundtSmall
    big_model = npcs.BundtLarge
    statue = npcs.BundtStatue
    unique_henchmen = [BundtTorte1, BundtTorte2]
    repeatable_henchmen = [BundtTorte1, BundtTorte2]
    dialog_replacements = [
        (49, """\n        (There's no response.)[await]"""),
        (1660, """\n    (The cake beckons you forth.)[await]"""),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Bundt's place.[await]""",
        ),
        (1695, """PIRATE: That's AMAZING!\n No one's EVER whipped BUNDT!![await]"""),
        # Find some way to do an animation instead of posting dialogue
        (
            1784,
            """CHEF TORTE: Ze apprentice, he\n inseests he saw ze cake MOVE!\n Vhy must he still talk of zees?![await]""",
        ),
        (
            1793,
            """APPRENTICE: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """APPRENTICE: You saw it too,\n right? I know I wasn't just\n imagining it![await]""",
        ),
        (
            1783,
            """ Zees ees not sparkling wine,[await]\n philistine!  Ees Champagne!![await]""",
        ),
        (
            1785,
            """APPRENTICE: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        ),
        (
            2504,
            """Wait... Did that cake just move?[await]\n Let's worry about it after finding\n the last [0x7024] item(s).[await]""",
        ),  # do this one with no background
        (
            2560,
            """APPRENTICE: Welcome to our\n world-class culinary school.[await]\n Please come back later to try some\n of our famous Bundt Cake.[await][page]\n [delay]...You want it NOW?\n [delay]How impatient! [delay]I oughtta teach you a lesson![await]""",
        ),
        (
            2572,
            """CHEF TORTE: Ve are busy preparing\n ze batter at ze moment...[await]\n No, you can't have any right zees\n second! [delay]How rude![await]""",
        ),
        (2831, EMPTY_DIALOG),
        (
            2832,
            """ Welcome. Our inn services are free\n tonight.[await][pause] We've unfortunately run\n out of complimentary cake, but\n would you like to stay anyway?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        ),
        (
            2834,
            """ The two guys in the left building\n have been acting suspicious.[await]""",
        ),
        (
            2837,
            """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        ),
        (2838, """ Have you been to Bundt's\n house up on the hill yet?[await]"""),
        (
            2839,
            """ Don't disturb the guards at the\n shed. They're uh... guarding a\n very important bake-off![await]""",
        ),
        (
            2841,
            """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        ),
        (
            2842,
            """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        ),
        (2843, """ Once you get through the Sunken\n Ship, you can... er...[await]"""),
        (
            2844,
            """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        ),
        (
            2845,
            """ I'm just here for kitchen supplies.\n Please leave me alone.[await]""",
        ),
        (2847, """ You can't just barge in here while\n I'm standing guard.[await]"""),
        (
            2848,
            """ Why's the door locked? [delay]Uh... [delay]We're\n uh... [delay]baking a very important\n cake! [delay]Do not disturb! [delay_30](I'm so sly!)[await]""",
        ),
        (3044, EMPTY_DIALOG),
        (
            3057,
            """[delay_60][await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        ),
        (
            3072,
            """APPRENTICE: (Please let this cake\n not be evil... please let this cake\n not be evil...)[await]""",
        ),
        (3073, """APPRENTICE: You again?! Leave\n our cake alone![await]"""),
        (
            3338,
            """ It's really weird.\n I never hear the next door\n neighbour.[await][pause] Maybe they don't move\n around much.[await][page]\n I'd like to go over and introduce\n myself sometime, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, EMPTY_DIALOG),
        (3353, EMPTY_DIALOG),
    ]
    optional_dialog_replacements = [
        (
            1694,
            """APPRENTICE: All right, we'll let\n you through. But don't mess our\n cake up, we spent all day on it.[await]""",
        ),
        (
            1695,
            """APPRENTICE: I thought we asked\n you not to mess our cake up![await]""",
        ),
    ]


class KingCalamariTinyBloober(Henchman):
    pack_number = 204
    model = npcs.TinyBloober


class KingCalamariBloober(Henchman):
    pack_number = 204
    model = npcs.Bloober


class KingCalamariTentacle(Henchman):
    pack_number = None
    model = npcs.TentacleExtending


class KingCalamariBoss(Boss):
    name = "King Calamari"
    pack_number = 167
    forced_background = 35
    small_model = npcs.Bloober
    statue = npcs.BlooberStatue
    repeatable_henchmen = [KingCalamariBloober]
    dialog_replacements = [
        (
            49,
            """KING CALAMARI: My species\n doesn't normally hatch from eggs\n quite this large.[await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n King Calamari's place.[await]""",
        ),
        (
            1695,
            """PIRATE: That's AMAZING!\n No one's EVER whipped\n KING CALAMARI!![await]""",
        ),
        (
            1778,
            """KING CALAMARI: I can't believe I\n was defeated in the ship I sunk\n myself...[await]""",
        ),
        (1780, """KING CALAMARI: Win or lose, I'm\n still king of this ship.[await]"""),
        (
            1781,
            """KING CALAMARI: I'm pretty slimy,\n so this seems like a bad idea.[await]""",
        ),
        (
            1783,
            """ I've found booty in the hold![await]\n Vats of Pearlescent Oyster Juice![await]""",
        ),
        (
            1784,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1785,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1793,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            2061,
            """CHEF TORTE: Zees cake, ve make\n it look like big squid! It is...\n masterpiece![await]""",
        ),
        (
            2504,
            """KING CALAMARI: Sorry, I don't\n have any hint memos for where you\n can find the last [0x7024] item(s).[await]""",
        ),  # do this one with no background
        (
            2560,
            """ Hello there. Welcome to our\n first-ever above-ground treasure\n hoard.[await][page]\n [delay].[delay].[delay].[delay]You're not here to see that?[delay_30]\n Well,[delay] then you must be an intruder!""",
        ),
        (2572, """ There's nothing back here!\n I mean it![await]"""),
        (
            2831,
            """KING CALAMARI: It's not so weird\n for a squid to run a town.[await]""",
        ),
        (
            2838,
            """ You will find King Calamari...\n in his house. He is...the most\n respected person here.[await]""",
        ),
        (3044, """KING CALAMARI: Think you can beat\n the dojo master?[await]"""),
        (
            3057,
            """ What do you want?[await]\n  [select] (Let's fight)\n  [select] (Uh...)[await]""",
        ),
        (
            3072,
            """ I'd just like to go back to\n shooting ink, not bullets...[await]""",
        ),
        (3073, """\n       You looking for a fight?[await]"""),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Ship-this and Tentacle-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (
            3352,
            """KING CALAMARI: My tentacles\n shouldn't be able to do this.[await]""",
        ),
        (
            3353,
            """KING CALAMARI: My tentacles\n shouldn't be able to do this.[await]""",
        ),
    ]


class HidonGoombette(Henchman):
    pack_number = 221
    model = npcs.Goombette


class HidonBoss(MimicBoss):
    name = "Hidon"
    pack_number = 157
    small_model = npcs.HidonSmall
    big_model = npcs.HidonLarge
    statue = npcs.MimicStatue
    unique_henchmen = [HidonGoombette, HidonGoombette, HidonGoombette, HidonGoombette]
    repeatable_henchmen = [HidonGoombette]
    dialog_replacements = [
        (
            49,
            """HIDON: No, I'm not gonna puke up\n another item for you! Go away![await]""",
        ),
        (
            1660,
            """ Ugh... What a rude awakening!\n I'm going to make it a hassle for\n you to pass through here![await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Hidon's place.[await]""",
        ),
        (1695, """PIRATE: That's AMAZING!\n No one's EVER whipped HIDON!![await]"""),
        (1778, """HIDON: Guess I'll have to train the\n Goombettes harder.[await]"""),
        (1780, """HIDON: This is definitely an upgrade\n from my old post.[await]"""),
        (1781, """HIDON: Oh come on, you know I'm\n weak to jumps![await]"""),
        (
            1783,
            """ Goombettes! They're after my[await]\n 1947 Phateu Cetrus Merlot!![await]""",
        ),
        (
            1784,
            """GOOMBETTE: Besides when he\n haphazardly throws us at enemies,\n Hidon is very good to us.[await]""",
        ),
        (
            1793,
            """GOOMBETTE: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """GOOMBETTE: Besides when he\n haphazardly throws us at enemies,\n Hidon is very good to us.[await]""",
        ),
        (
            1785,
            """GOOMBETTE: Besides when he\n haphazardly throws us at enemies,\n Hidon is very good to us.[await]""",
        ),
        (2061, """GOOMBETTE: Doesn't this cake\n look just like Hidon?[await]"""),
        (2062, """GOOMBETTE: We've gotten REAL\n good with fondant![await]"""),
        (
            2504,
            """HIDON: ...I don't know where the\n last [0x7024] item(s) are. Ask the\n Goombettes.[await]""",
        ),
        (
            2560,
            """GOOMBETTE: I need a pen, but I\n can't reach the top drawer of this\n desk. Can you help me out?[await][page]\n [delay]...What?[delay] “How are you going to\n use a pen when you don't have any\n arms”?[await][pause] You makin' fun of me?!\n [delay]That's IT, buddy! Get down here![await]""",
        ),
        (
            2572,
            """GOOMBETTE: Hey! Hidon's trying to\n stay in hidin' over here![delay] Get lost![await]""",
        ),
        (2831, """\n          HIDON: Oh, it's you.[await]"""),
        (
            2832,
            """ Hey! Why don't you crash here for\n the night? It's free! FREE![await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        ),
        (
            2834,
            """ The two guys in the left building\n have been acting suspicious.[await]""",
        ),
        (
            2837,
            """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        ),
        (2838, """ Have you been to Hidon's\n house up on the hill yet?[await]"""),
        (
            2839,
            """ Hey! What are you doing in our\n town? Don't go snooping around![await]""",
        ),
        (
            2841,
            """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        ),
        (
            2842,
            """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        ),
        (2843, """ Once you get through the Sunken\n Ship, you can... er...[await]"""),
        (
            2844,
            """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        ),
        (2845, """ Why don'tcha mind your own\n beeswax?![await]"""),
        (2847, """ Don't even THINK about going\n inside this house![await]"""),
        (
            2848,
            """ Hey, buster![delay] You think you're some\n kinda tough guy, tryin' to step\n over us guards?![await]""",
        ),
        (3044, """HIDON: The dojo master's pretty\n tough.[await]"""),
        (
            3057,
            """ Ugh... What'd you wake me up for?[await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        ),
        (3072, """GOOMBETTE: (I'm too short to see\n out this window.)[await]"""),
        (3073, """GOOMBETTE: Put up your dukes,\n big man![await]"""),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Treasure-this and Piranha-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, """HIDON: I bet this would be even\n harder to do in my box.[await]"""),
        (3353, """HIDON: I bet this would be even\n harder to do in my box.[await]"""),
    ]
    optional_dialog_replacements = [
        (
            1694,
            """GOOMBETTE: You mighta' won\n against us, but Hidon's gonna\n beat you up![await]""",
        ),
        (1695, """GOOMBETTE: You beat Hidon?![await]\n Oh, man...[await]"""),
    ]


class DefaultBandanaRed1(Henchman):
    pack_number = 68
    model = npcs.BandanaRed


class DefaultBandanaRed2(Henchman):
    pack_number = 69
    model = npcs.BandanaRed


class JohnnyBandanaRed(Henchman):
    pack_number = 71
    model = npcs.BandanaRed


class JohnnyBandanaBlue(Henchman):
    pack_number = 70
    model = npcs.BandanaBlue


class JohnnyBoss(Boss):
    name = "Johnny"
    pack_number = 166
    small_model = npcs.JohnnySmall
    big_model = npcs.JohnnyLarge
    statue = npcs.JohnnyStatue
    unique_henchmen = [
        JohnnyBandanaBlue,
        JohnnyBandanaBlue,
        JohnnyBandanaBlue,
        JohnnyBandanaBlue,
    ]
    repeatable_henchmen = [JohnnyBandanaRed]
    dialog_replacements = [
        (
            49,
            """JOHNNY: Matey, it'd be mighty fun\n to spar again, but I'm tryin' to\n sleep now.[await]""",
        ),
        (
            1660,
            """ Good job, matey... But ye gotta\n fight me first if ye wanna be let\n through![await]""",
        ),
        (
            2061,
            """PIRATE: Y'arr, don't ye think\n this cake here be lookin' just like\n Johnny?[await]""",
        ),
        (2062, """PIRATE: Us pirates are pretty\n good with food, arr harr![await]"""),
        (
            2504,
            """JOHNNY: Found [0x7000] item(s), eh? Arr,\n harr, harr...! You gotta find [0x7024]\n more, matey![await]""",
        ),
        (
            2560,
            """PIRATE: Welcome, matey![await][pause] Here to\n spar with Johnny, are ye?[await][page]\n Arr, good fun! Let's have a\n warm-up round![await]""",
        ),
        (
            2572,
            """PIRATE: This ain't the corner you\n want, matey![await][pause] But while you're here,\n let's have a spar, arr harr![await]""",
        ),
        (2831, """\n        JOHNNY: Ahoy, matey![await]"""),
        (
            2832,
            """ Welcome, matey! How'd ya like to\n stay here tonight, on the house?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        ),
        (
            2834,
            """ The two fellas o'er in the left\n building have been actin' weird.[await]""",
        ),
        (
            2837,
            """ It ain't always easy gettin' into\n the Sea.[await][pause] Ya might need to do\n somethin' else, first![await]""",
        ),
        (2838, """ Have ye been to visit Johnny up\n on the hill yet, matey?[await]"""),
        (
            2839,
            """ Arr, what ye be doin' in our town?\n Just stay away from the shed,\n ya hear?[await]""",
        ),
        (2841, """ Out in yonder Sunken Ship, there\n be a... er...[await]"""),
        (
            2842,
            """ A treasure chest, behind a big\n stack o' boxes! Don't forget about\n it, matey![await]""",
        ),
        (
            2843,
            """ If ye can tough it out through the\n ship, you can come back here for\n some... er...[await]""",
        ),
        (
            2844,
            """ Come back here for some FUN,\n arr harr! Ya got that, matey?![await]""",
        ),
        (2845, """\n       I just be shoppin', matey.[await]"""),
        (2847, """ Read my lips... WE AIN'T LETTIN'\n YA THROUGH![await]"""),
        (2848, """\n You ain't gettin in here! It's ours![await]"""),
        (
            3044,
            """JOHNNY: Good luck, matey. The dojo\n master's mighty tough.[await]""",
        ),
        (
            3057,
            """ Arr, what brings ye here?[await]\n  [select] (I want a fight)\n  [select] (Uh...)[await]""",
        ),
        (
            3072,
            """PIRATE: I know there be some fine\n loot in this tower, but it's too far\n 'bove sea level for my liking![await]""",
        ),
        (3073, """PIRATE: I'll make ya see stars,\n arr harr![await]"""),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Arr-this and Matey-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, """JOHNNY: Matey, I've got lots o'\n training to do![await]"""),
        (3353, """JOHNNY: Matey, I've got lots o'\n training to do![await]"""),
    ]


class YaridovichHenchman(Henchman):
    pack_number = 153
    model = npcs.FakeToad


class YaridovichBoss(Boss):
    name = "Yaridovich"
    pack_number = 180
    small_model = npcs.FakeElder
    big_model = npcs.YaridOverworld
    attack_model = npcs.YaridovichLarge
    statue = npcs.YaridovichStatue
    unique_henchmen = [
        YaridovichHenchman,
        YaridovichHenchman,
        YaridovichHenchman,
        YaridovichHenchman,
    ]
    repeatable_henchmen = [YaridovichHenchman]
    dialog_replacements = [
        (
            49,
            """YARIDOVICH: How could I lose to\n those...[delay] Huh? Hey, get lost![await]""",
        ),
        (
            1660,
            """ Eee hee hee! So, you've cracked the\n code... Now, it's time for the\n REAL test![await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Yaridovich's place.[await]""",
        ),
        (
            1695,
            """PIRATE: That's AMAZING!\n No one's EVER whipped\n YARIDOVICH!![await]""",
        ),
        (
            1778,
            """YARIDOVICH: Ridiculous! How could a\n genius like me lose to them...?[await]""",
        ),
        (
            1780,
            """YARIDOVICH: I'm thinking it might\n be time for me to switch careers.[await][page]\n Say, do you happen to know anyone\n who's looking to hire a\n hydrodemolitions expert?[await]""",
        ),
        (1781, """YARIDOVICH: This is just adding\n insult to injury![await]"""),
        (
            1784,
            """TOWNSPERSON: We must.. be\n careful. We could rust.. down here.[await]""",
        ),
        (
            1793,
            """TOWNSPERSON: Hop on... then trampoline... in the next room.\n It'll take you... outside.[await]""",
        ),
        (
            1792,
            """TOWNSPERSON: We must.. be\n careful. We could rust.. down here.[await]""",
        ),
        (
            1783,
            """ My disguise was as see-through[await]\n as this glass of Motor Oil!![await]""",
        ),
        (
            1785,
            """TOWNSPERSON: We must.. be\n careful. We could rust.. down here.[await]""",
        ),
        (
            2061,
            """TOWNSPERSON: We must... make\n this cake... look exactly...\n like Yaridovich.[await]""",
        ),
        (2062, """TOWNSPERSON: We need... more\n fondant.[await]"""),
        (
            2504,
            """YARIDOVICH: Eee hee...! You're\n still missing [0x7024] item(s)! Isn't that\n a shame?[await]""",
        ),
        (
            2560,
            """TOWNSPERSON: I'm just... a\n secretary. Don't bother...\n Yaridovich.[await]""",
        ),
        (2572, """TOWNSPERSON: This is...not...\n the right...way.[await]"""),
        (
            3044,
            """YARIDOVICH: A challenge from the\n dojo master? [delay]Eee hee hee, this\n ought to be interesting![await]""",
        ),
        (
            3057,
            """ Eee hee...! You want to fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        ),
        (3072, """TOWNSPERSON: It's nice...\n outside.[await]"""),
        (3073, """TOWNSPERSON: You want...to\n fight?[await]"""),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Brownie-this and Tickle-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, """YARIDOVICH: I guess I wasn't as\n strong as I thought...[await]"""),
        (3353, """YARIDOVICH: I guess I wasn't as\n strong as I thought...[await]"""),
    ]
    optional_dialog_replacements = [
        (
            1694,
            """TOWNSPERSON: Well done...\n You may go on... to Yaridovich.[await]""",
        ),
        (1695, """TOWNSPERSON: You won...\n Well done...[await]"""),
    ]


class MokuraBoss(Boss):
    name = "Mokura"
    pack_number = 207
    statue = npcs.MokuraStatue
    small_model = npcs.MokuraCloud
    big_model = npcs.MokuraLarge
    dialog_replacements = [
        (49, """\n     MOKURA: Uhh... Go away![await]"""),
        (1660, """\n             Duh, huh, huh...[await]"""),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Mokura's place.[await]""",
        ),
        (1695, """PIRATE: That's AMAZING!\n No one's EVER whipped MOKURA!![await]"""),
        (1778, """\n            MOKURA: Hmm...[await]"""),
        (1780, """MOKURA: What're you doing in my\n secret lair?[await]"""),
        (1781, """MOKURA: I oughta go back to\n being invisible...[await]"""),
        (
            1783,
            """ Mmm...uhhh. Cotton Candy![await]\n ...It's...so...airy...YUM![await]""",
        ),
        (
            1784,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1785,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1793,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            2061,
            """CHEF TORTE: Zees cake, ve make\n it look like big cloud! It is...\n masterpiece![await]""",
        ),
        (2504, """MOKURA: Uhh... You need [0x7024] more\n item(s)...[await]"""),
        (
            2560,
            """SNIFIT 1: Hello there.[await]\n Mokura's busy right now, so he[1] can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        ),
        (2572, """SNIFIT 2: Please refrain\n from bothering Mokura.[await]"""),
        (2831, """\n       MOKURA: Mwa, ha, ha![await]"""),
        (
            2838,
            """ You will find Mokura...\n in his house. He is...the most\n respected person here.[await]""",
        ),
        (3044, """MOKURA: Uhh... Are you... gonna\n beat the Dojo Master?[await]"""),
        (
            3057,
            """ Uhh... Hi there.[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        ),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Secret-this and Gas-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, """\n    MOKURA: A cloud can jump...[await]"""),
        (3353, """\n    MOKURA: A cloud can jump...[await]"""),
    ]


class Belome2MarioClone(Henchman):
    pack_number = 200
    model = npcs.MarioClone


class Belome2MallowClone(Henchman):
    pack_number = 202
    model = npcs.MallowClone


class Belome2GenoClone(Henchman):
    pack_number = 196
    model = npcs.GenoClone


class Belome2BowserClone(Henchman):
    pack_number = 197
    model = npcs.BowserClone


class Belome2PeachClone(Henchman):
    pack_number = 198
    model = npcs.PeachClone


class Belome2Boss(Boss):
    name = "Belome"
    pack_number = 169
    small_model = npcs.Belome2Small
    big_model = npcs.Belome2Large
    statue = npcs.SmallBelomeStatue
    repeatable_henchmen = [
        Belome2MarioClone,
        Belome2MallowClone,
        Belome2GenoClone,
        Belome2BowserClone,
        Belome2PeachClone,
    ]
    dialog_replacements = [
        (49, """\n        BELOME: Good night~![await]"""),
        (
            1660,
            """ Oh, is it dinner time already?\n Come on in...[delay_60] if you dare~![await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Belome's place.[await]""",
        ),
        (1695, """PIRATE: That's AMAZING!\n No one's EVER whipped BELOME!![await]"""),
        (
            1778,
            """BELOME: You look tasty! If you\n stick around any longer, I might\n just have a snack![await]""",
        ),
        (1780, """BELOME: Oh, you're back![await]\n Did you bring any food?[await]"""),
        (
            1781,
            """BELOME: Say, it's past my bedtime.\n Can you get off of my head?[await]""",
        ),
        (
            1783,
            """ Woof, I ate too many Mallows~![await]\n I should wash it down with Tonic~![await]""",
        ),
        (
            1784,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1785,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1793,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            2061,
            """CHEF TORTE: Zees cake, ve make\n it look like big dog! It is...\n masterpiece![await]""",
        ),
        (
            2504,
            """BELOME: Oh, no, you're still\n missing [0x7024] item(s).[await][pause] I can't wait any\n longer to see what today's cake\n will be.[await][pause] I'm STARVING![await]""",
        ),
        (
            2560,
            """SNIFIT 1: Hello there.[await]\n Belome's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        ),
        (2572, """SNIFIT 2: Please refrain\n from bothering Belome.[await]"""),
        (2831, """BELOME: It's dreadfully boring\n around here~![await]"""),
        (
            2838,
            """ You will find Belome...\n in his house. He is...the most\n respected person here.[await]""",
        ),
        (
            3044,
            """BELOME: Ooh, how exciting~!\n [delay]The dojo master has challenged\n you![await]""",
        ),
        (
            3057,
            """ Are you the pizza delivery person?[await]\n  [select] (I'm here to fight you)\n  [select] (Sorry, wrong door)[await]""",
        ),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Scarecrow-this and Hungry-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (
            3352,
            """BELOME: This training regimen is\n giving me quite the appetite![await]""",
        ),
        (
            3353,
            """BELOME: This training regimen is\n giving me quite the appetite![await]""",
        ),
    ]


class JaggerBoss(Boss):
    name = "Jagger"
    pack_number = 189
    small_model = npcs.Terrapin
    statue = npcs.TerrapinStatue
    dialog_replacements = [
        (49, """JAGGER: It'd be fun to fight\n again, but I need a nap.[await]"""),
        (
            1660,
            """ Wow, you figured out the\n password! Come on in and let's\n have a spar![await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Jagger's place.[await]""",
        ),
        (1695, """PIRATE: That's AMAZING!\n No one's EVER whipped JAGGER!![await]"""),
        (
            1778,
            """JAGGER: Wow, what a fight! I\n better think about what I'm gonna\n do to win next time...[await]""",
        ),
        (
            1780,
            """JAGGER: Welcome back! I've been\n training hard for our next fight,\n whenever that may be![await]""",
        ),
        (
            1781,
            """JAGGER: `MAIN_CHARACTER_NAME`, I can't\n jump as high as you. Is this\n really necessary?[await]""",
        ),
        (
            1783,
            """ My Sensei's drink is gross...[await]\n Here, my Black Tea is WAY better.[await]""",
        ),
        (
            1784,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1785,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1793,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            2061,
            """CHEF TORTE: Zees cake, ve make\n it look like big turtle! It is...\n masterpiece![await]""",
        ),
        (
            2504,
            """JAGGER: Oh, wow, you've already\n found [0x7000] item(s)![await][pause] I bet you'll find\n the last [0x7024] in no time.[await]""",
        ),
        (
            2560,
            """SNIFIT 1: Hello there.[await]\n Jagger's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        ),
        (2572, """SNIFIT 2: Please refrain\n from bothering Jagger.[await]"""),
        (2831, """\nJAGGER: Hi, `MAIN_CHARACTER_NAME`![await]"""),
        (
            2838,
            """ You will find Jagger...\n in his house. He is...the most\n respected person here.[await]""",
        ),
        (
            3057,
            """ Hello. May I help you?[await]\n  [select] (Let's fight)\n  [select] (Uh...)[await]""",
        ),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Dojo-this and Sensei-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (
            3353,
            """JAGGER: Sensei, the new regimen\n will strengthen us, right?[await]""",
        ),
    ]


class Jinx1Boss(Boss):
    name = "Jinx"
    pack_number = 178
    small_model = npcs.Jinx1
    statue = npcs.JinxStatue
    dialog_replacements = [
        (49, """JINX: Please do not disturb me.\n I am training in here.[await]"""),
        (
            1660,
            """ So, you've figured out the\n password. But, I'm not letting you\n through just yet![await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Jinx's place.[await]""",
        ),
        (1695, """PIRATE: That's AMAZING!\n No one's EVER whipped JINX!![await]"""),
        (1778, """\n   JINX: I was going easy on you![await]"""),
        (1780, """JINX: I must accept that I have been\n bested. Good work![await]"""),
        (1781, """JINX: Yes, I am short! Show a little\n respect![await]"""),
        (
            1783,
            """ We're warming up `MAIN_CHARACTER_NAME`![await]\n But first, a Green Tea break![await]""",
        ),
        (
            1784,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1785,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1793,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            2061,
            """CHEF TORTE: Zees cake, ve make\n it look like tiny monk! It is...\n masterpiece![await]""",
        ),
        (
            2504,
            """JINX: Hmm.[delay] [0x7000] item(s). Not bad.[await]\n But don't let it get to your head,\n you still have [0x7024] left to find![await]""",
        ),
        (
            2560,
            """SNIFIT 1: Hello there.[await]\n Jinx is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        ),
        (2572, """SNIFIT 2: Please refrain\n from bothering Jinx.[await]"""),
        (2831, """\n               JINX: Hmm...[await]"""),
        (
            2838,
            """ You will find Jinx...\n in his house. He is...the most\n respected person here.[await]""",
        ),
        (
            3044,
            """JINX: The dojo master is quite\n disciplined. Good luck on your\n challenge.[await]""",
        ),
        (
            3057,
            """ You have come to challenge me?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        ),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Dojo-this and Ki-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, """JINX: Master!\n Share your wisdom with us![await]"""),
    ]


class Jinx2Boss(Boss):
    name = "Jinx"
    pack_number = 187
    eye_height = 4
    small_model = npcs.Jinx2
    statue = npcs.JinxStatue
    dialog_replacements = [
        (49, """JINX: Please do not disturb me.\n I am training in here.[await]"""),
        (
            1660,
            """ So, you've figured out the\n password. But, I'm not letting you\n through just yet![await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Jinx's place.[await]""",
        ),
        (1695, """PIRATE: That's AMAZING!\n No one's EVER whipped JINX!![await]"""),
        (1778, """\n   JINX: I was going easy on you![await]"""),
        (1780, """JINX: I must accept that I have been\n bested. Good work![await]"""),
        (1781, """JINX: Yes, I am short! Show a little\n respect![await]"""),
        (
            1783,
            """ Well-fought, `MAIN_CHARACTER_NAME`![await]\n I've some Jasmine Tea for this day![await]""",
        ),
        (
            1784,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1785,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1793,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            2061,
            """CHEF TORTE: Zees cake, ve make\n it look like tiny monk! It is...\n masterpiece![await]""",
        ),
        (
            2504,
            """JINX: Hmm.[delay] [0x7000] item(s). Not bad.[await]\n But don't let it get to your head,\n you still have [0x7024] left to find![await]""",
        ),
        (
            2560,
            """SNIFIT 1: Hello there.[await]\n Jinx is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        ),
        (2572, """SNIFIT 2: Please refrain\n from bothering Jinx.[await]"""),
        (2831, """\n               JINX: Hmm...[await]"""),
        (
            2838,
            """ You will find Jinx...\n in his house. He is...the most\n respected person here.[await]""",
        ),
        (
            3044,
            """JINX: The dojo master is quite\n disciplined. Good luck on your\n challenge.[await]""",
        ),
        (
            3057,
            """ You have come to challenge me?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        ),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Dojo-this and Ki-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, """JINX: Master!\n Share your wisdom with us![await]"""),
    ]


class Jinx3Boss(Boss):
    name = "Jinx"
    pack_number = 188
    small_model = npcs.Jinx3
    statue = npcs.JinxStatue
    dialog_replacements = [
        (49, """JINX: Please do not disturb me.\n I am training in here.[await]"""),
        (
            1660,
            """ So, you've figured out the\n password. But, I'm not letting you\n through just yet![await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Jinx's place.[await]""",
        ),
        (1695, """PIRATE: That's AMAZING!\n No one's EVER whipped JINX!![await]"""),
        (1778, """\n   JINX: I was going easy on you![await]"""),
        (1780, """JINX: I must accept that I have been\n bested. Good work![await]"""),
        (1781, """JINX: Yes, I am short! Show a little\n respect![await]"""),
        (
            1783,
            """ Hail, Master `MAIN_CHARACTER_NAME`![await]\n Let us celebrate with Matcha![await]""",
        ),
        (
            1784,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1785,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1793,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            2061,
            """CHEF TORTE: Zees cake, ve make\n it look like tiny monk! It is...\n masterpiece![await]""",
        ),
        (
            2504,
            """JINX: Hmm.[delay] [0x7000] item(s). Not bad.[await]\n But don't let it get to your head,\n you still have [0x7024] left to find![await]""",
        ),
        (
            2560,
            """SNIFIT 1: Hello there.[await]\n Jinx is busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        ),
        (2572, """SNIFIT 2: Please refrain\n from bothering Jinx.[await]"""),
        (2831, """\n               JINX: Hmm...[await]"""),
        (
            2838,
            """ You will find Jinx...\n in his house. He is...the most\n respected person here.[await]""",
        ),
        (
            3044,
            """JINX: The dojo master is quite\n disciplined. Good luck on your\n challenge.[await]""",
        ),
        (
            3057,
            """ You have come to challenge me?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        ),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Dojo-this and Ki-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, """JINX: Master!\n Share your wisdom with us![await]"""),
    ]


class CulexFireCrystal(Henchman):
    pack_number = 217
    model = npcs.FireCrystal


class CulexWaterCrystal(Henchman):
    pack_number = 218
    model = npcs.WaterCrystal


class CulexEarthCrystal(Henchman):
    pack_number = 219
    model = npcs.EarthCrystal


class CulexWindCrystal(Henchman):
    pack_number = 220
    model = npcs.WindCrystal


class CulexBoss(Boss):
    name = "Culex"
    pack_number = 216
    small_model = npcs.CulexSmall
    big_model = npcs.CulexLarge
    statue = npcs.CulexStatue
    unique_henchmen = [
        CulexFireCrystal,
        CulexWaterCrystal,
        CulexEarthCrystal,
        CulexWindCrystal,
    ]
    dialog_replacements = [
        (
            49,
            """CULEX: Please do not attempt to\n crack this egg again.[await][page]\n It will not give you thousands of\n experience points.[await]""",
        ),
        (
            1660,
            """ You have passed the first test.\n But you're not finished yet!\n Please enter.[await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Culex's place.[await]""",
        ),
        (1695, """PIRATE: That's AMAZING!\n No one's EVER whipped CULEX!![await]"""),
        (
            1778,
            """CULEX: This world truly is\n uninhabitable for me and my kind...[await]""",
        ),
        (
            1780,
            """CULEX: Greetings. It is good to\n make your acquaintance once\n again.[await]""",
        ),
        (
            1781,
            """CULEX: This is not the encounter In expected when I came to visit this\n world.[await]""",
        ),
        (
            1783,
            """ How droll, my crystals shattered.[await]\n I've only Bacchus Wine remaining.[await]""",
        ),
        (
            1785,
            """WATER CRYSTAL: I guess this is as\n close as I'll get to being returned\n to Mysidia.[await]""",
        ),
        (
            1792,
            """EARTH CRYSTAL: I thought the\n Dark Elf was a bit strange, until\n we came to this world.[await]\n You truly have some characters\n here![await]""",
        ),
        (1784, """FIRE CRYSTAL: Of course I'm\n miserable! We're UNDERWATER![await]"""),
        (
            1793,
            """WIND CRYSTAL: Culex is nice and\n all, but I miss Yang sometimes.[await]""",
        ),
        (
            2061,
            """FIRE CRYSTAL: We needed a lot of\n heat to bake a cake of this size.[await]""",
        ),
        (
            2062,
            """WATER CRYSTAL: We must shape\n this confection to resemble Culex.[await]""",
        ),
        (
            2504,
            """CULEX: You must retrieve [0x7024] more\n item(s) before we may proceed.[await]\n Godspeed, champion knight![await]""",
        ),
        (
            2560,
            """FIRE CRYSTAL: Greetings.[await][pause] Culex\n is making preparations to head\n back to his home world.[await][pause] He's\n busy right now.[await][page]\n Please come back later...\n [delay]unless you want to get hurt![await]""",
        ),
        (
            2572,
            """WIND CRYSTAL: You are not going\n to find what you're seeking back\n here.[delay] Stay out.[await]""",
        ),
        (2831, """\n           CULEX: Good day.[await]"""),
        (
            2832,
            """ Welcome to our inn.[await]\n We are offering a competitive price\n of zero coins per night.[await]\n Will you be staying tonight?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        ),
        (
            2834,
            """ The two guys in the left building\n have been acting suspicious.[await]""",
        ),
        (
            2837,
            """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        ),
        (2838, """ Have you been to Culex's\n house up on the hill yet?[await]"""),
        (
            2841,
            """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        ),
        (
            2842,
            """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        ),
        (2843, """ Once you get through the Sunken\n Ship, you can... er...[await]"""),
        (
            2844,
            """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        ),
        (2847, """FIRE CRYSTAL: This area is\n off-limits.[await]"""),
        (
            2848,
            """WATER CRYSTAL: This door is a...\n uh... portal to another dimension!\n We can't let you fall into it.[await]""",
        ),
        (
            3044,
            """CULEX: It will be quite difficult to\n claim victory over the dojo master.\n I wish you luck.[await]""",
        ),
        (
            3072,
            """EARTH CRYSTAL: Wind Crystal\n really should have been the one\n standing guard all the way up here.[await]""",
        ),
        (3073, """EARTH CRYSTAL: Stand back!\n I might know Sandstorm![await]"""),
        (3352, """CULEX: Well met! Thank you for\n the excellent battle.[await]"""),
        (3353, """CULEX: Well met! Thank you for\n the excellent battle.[await]"""),
    ]
    optional_dialog_replacements = [
        (1694, """CRYSTAL: Proceed forth. Culex\n awaits you.[await]"""),
        (
            1695,
            """CRYSTAL: Well met! You have\n satisfied Culex's hunger for a\n true challenge.[await]""",
        ),
    ]


class BoxBoyBoss(MimicBoss):
    name = "Box Boy"
    pack_number = 158
    small_model = npcs.BoxBoySmall
    big_model = npcs.BoxBoyLarge
    statue = npcs.MimicStatue
    dialog_replacements = [
        (
            49,
            """BOX BOY: How many times are you\n gonna wake me up? Get lost![await]""",
        ),
        (1660, """ Oh, you're gonna PAY for waking\n me up like this![await]"""),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Box Boy's place.[await]""",
        ),
        (1695, """PIRATE: That's AMAZING!\n No one's EVER whipped BOX BOY!![await]"""),
        (1778, """\n    BOX BOY: You just got lucky![await]"""),
        (1780, """\n   BOX BOY: This place is boring.[await]"""),
        (
            1781,
            """BOX BOY: You sure you wanna jump\n on me? I counter special attacks.[await]""",
        ),
        (
            1783,
            """ You don't even deserve to LOOK at[await]\n My 1990 Comanee-Ronti Pinot Noir![await]""",
        ),
        (
            1784,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1785,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1793,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            2061,
            """CHEF TORTE: Zees cake, ve make\n it look like mimic! It is...\n masterpiece![await]""",
        ),
        (2504, """BOX BOY: Still missing [0x7024] item(s)?\n Pathetic![await]"""),
        (
            2560,
            """SNIFIT 1: Hello there.[await]\n Box Boy's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        ),
        (2572, """SNIFIT 2: Please refrain\n from bothering Box Boy.[await]"""),
        (2831, """BOX BOY: What'd you come here\n for?[await]"""),
        (
            2838,
            """ You will find Box Boy...\n in his house. He is...the most\n respected person here.[await]""",
        ),
        (3044, """BOX BOY: The dojo master's gonna\n kick your butt![await]"""),
        (
            3057,
            """ This'd BETTER be important![await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        ),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Treasure-this and Ghost-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, """BOX BOY: Ahh, you're not so\n tough![await]"""),
        (3353, """BOX BOY: Ahh, you're not so\n tough![await]"""),
    ]


class MegaSmilaxPiranha(Henchman):
    pack_number = 222
    model = npcs.PiranhaPlant


class MegaSmilaxBoss(Boss):
    name = "Megasmilax"
    pack_number = 173
    small_model = npcs.PiranhaPlant
    big_model = npcs.Megasmilax
    statue = npcs.PiranhaPlantStatue
    repeatable_henchmen = [MegaSmilaxPiranha]
    dialog_replacements = [
        (
            49,
            """MEGASMILAX: I'm thirsty.[await][pause] Can you\n ask Shy Away to come back here,[delay]\n please?[await]""",
        ),
        (
            1660,
            """ Hm?[delay_30] Not often we get visitors\n down here.[delay_30] Come in...[delay_60]\n at your own risk, that is![await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Megasmilax's place.[await]""",
        ),
        (
            1695,
            """PIRATE: That's AMAZING!\n No one's EVER whipped\n MEGASMILAX!![await]""",
        ),
        (1778, """\n      MEGASMILAX: I'm thirsty.[await]"""),
        (
            1780,
            """MEGASMILAX: You'd think it\n wouldn't be so difficult to get\n watered around here, when we're\n literally underwater.[await]""",
        ),
        (1781, """MEGASMILAX: Careful. I have sharp\n teeth.[await]"""),
        (
            1783,
            """ Go ahead, just add Water![await]\n Cha-Cha-Cha-Chia!  La Dee Dah~![await]""",
        ),
        (1784, """SMILAX: I guess salt water\n wouldn't be very good for us.[await]"""),
        (
            1793,
            """SMILAX: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        ),
        (1792, """SMILAX: I guess salt water\n wouldn't be very good for us.[await]"""),
        (1785, """SMILAX: I guess salt water\n wouldn't be very good for us.[await]"""),
        (2061, """SMILAX: We're making this cake\n in honour of Megasmilax.[await]"""),
        (
            2062,
            """SMILAX: I hope the wedding party\n likes it. If they don't...[delay] well,[delay]\n they DID hire plants to bake a cake.[await]""",
        ),
        (
            2504,
            """MEGASMILAX: Hm?[await]\n [0x7024] more item(s)?[await]\n Don't ask me.[delay] I'm just a plant.[await]""",
        ),
        (
            2560,
            """SMILAX: Hello there. Are you the\n gardener?[await][page]\n No?[await][pause] Well, [delay]we didn't call for a\n plumber today... [await][pause]]I better get you\n outta here![await]""",
        ),
        (
            2572,
            """SMILAX: If you didn't come back\n here to water us, you'd better get\n outta here.[await]""",
        ),
        (2831, """\n         MEGASMILAX: Hmm...[await]"""),
        (
            2832,
            """ Hello there. Are you tired?\n We don't charge any fees here,\n if you'd like to stay.[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        ),
        (
            2834,
            """ The two guys in the left building\n have been acting suspicious.[await]""",
        ),
        (
            2837,
            """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        ),
        (2838, """ Have you been to Megasmilax's\n house up on the hill yet?[await]"""),
        (
            2839,
            """ Welcome to our humble little town.\n You're welcome to stick around,\n but keep away from the shed, OK?[await]""",
        ),
        (
            2841,
            """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        ),
        (
            2842,
            """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        ),
        (2843, """ Once you get through the Sunken\n Ship, you can... er...[await]"""),
        (
            2844,
            """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        ),
        (
            2845,
            """ I'm shopping for some fertilizer.[await]\n [delay]...Don't give me that look!\n [delay]I'm just a plant![await]""",
        ),
        (2847, """ There's nothing suspicious going on\n in here.[await]"""),
        (
            2848,
            """ We're just two plants growing in\n front of an abandoned door. ...But\n we're not letting you in.[await]""",
        ),
        (
            3044,
            """MEGASMILAX: I would love to\n watch your match with the dojo\n master.[await]""",
        ),
        (
            3057,
            """ You don't look like the gardener...[await]\n  [select] (I'm here to fight you)\n  [select] (Oops, my mistake)[await]""",
        ),
        (3072, """\n          SMILAX: I'm thirsty.[await]"""),
        (3073, """\n       SMILAX: Careful, I bite.[await]"""),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Water-this and Fertilizer-that.[await]\n ...[delay]Actually, [delay]that doesn't sound\n so bad![await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, """MEGASMILAX: This is harder than it\n looks. I'm a plant.[await]"""),
        (3353, """MEGASMILAX: This is harder than it\n looks. I'm a plant.[await]"""),
    ]
    optional_dialog_replacements = [
        (
            1694,
            """SMILAX: Go on ahead to visit\n Megasmilax. But be warned, he's\n pretty tough when he's hydrated.[await]""",
        ),
        (
            1695,
            """SMILAX: Wow, you won![await][pause] Shy Away\n must have watered you more than\n he watered Megasmilax.[await]""",
        ),
    ]


class DodoBoss(Boss):
    name = "Dodo"
    pack_number = 208
    small_model = npcs.DodoSmall
    big_model = npcs.DodoLarge
    statue = npcs.DodoStatue
    dialog_replacements = [
        # actually, don't use dialogs for dodo, just play sfx... how to handle this?
        # time this according to how long the feather sound effect is
        (49, EMPTY_DIALOG),
        (1660, EMPTY_DIALOG),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Dodo's place.[await]""",
        ),
        (1695, """PIRATE: That's AMAZING!\n No one's EVER whipped DODO!![await]"""),
        (1778, EMPTY_DIALOG),
        (1780, EMPTY_DIALOG),
        (1781, EMPTY_DIALOG),
        (
            1783,
            """ (Dodo stares at a Hot Chocolate)[await]\n ...Please don't tell Valentina.[await]""",
        ),
        (
            1784,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1785,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1793,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            2061,
            """CHEF TORTE: Zees cake, ve make\n it look like big bird! It is...\n masterpiece![await]""",
        ),
        (
            2504,
            """    Dodo is a bird of few words.[await]\n    You still have [0x7024] item(s) left\n                 to find.[await]""",
        ),  # use async for this one too
        (
            2560,
            """SNIFIT 1: Hello there.[await]\n Dodo's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        ),
        (2572, """SNIFIT 2: Please refrain\n from bothering Dodo.[await]"""),
        (2831, EMPTY_DIALOG),
        (
            2838,
            """ You will find Dodo...\n in his house. He is...the most\n respected person here.[await]""",
        ),
        (3044, EMPTY_DIALOG),
        (
            3057,
            """[delay_60][await]\n  [select] (I'm here for a fight)\n  [select] (Uh...)[await]""",
        ),
        (
            3338,
            """ It's really weird.\n I never hear the guy next door.[await]\n Maybe he can't talk.[await][page]\n I'd like to go over and introduce\n myself sometime, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, EMPTY_DIALOG),
        (3353, EMPTY_DIALOG),
    ]


class BirdettaEggbert(Henchman):
    pack_number = 223
    model = npcs.EggbertGridplane


class BirdettaBoss(Boss):
    name = "Birdetta"
    pack_number = 175
    small_model = npcs.BirdettaSmall
    big_model = npcs.BirdettaLarge
    statue = npcs.BirdettaStatue
    unique_henchmen = [BirdettaEggbert, BirdettaEggbert, BirdettaEggbert]
    repeatable_henchmen = [BirdettaEggbert]
    dialog_replacements = [
        (1660, """ Oh, yay, you've come to play!\n Come on in~![await]"""),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Birdetta's place.[await]""",
        ),
        (
            1695,
            """PIRATE: That's AMAZING!\n No one's EVER whipped\n BIRDETTA!![await]""",
        ),
        (1778, """BIRDETTA: Tee hee! Let's play\n again sometime♥![await]"""),
        (
            1780,
            """BIRDETTA: Oh, you didn't forget\n about me! You're so sweet♥![await]""",
        ),
        (
            1781,
            """BIRDETTA: This isn't what I had in\n mind when I said I wanted to play![await]""",
        ),
        (
            1783,
            """ Thanks for playing with me~![await]\n I lost, but I made Yoshi's Eggnog♥![await]""",
        ),
        (
            1784,
            """EGGBERT: You visiting us has\n really made Birdetta happy.\n Thank you![await]""",
        ),
        (
            1793,
            """EGGBERT: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """EGGBERT: You visiting us has\n really made Birdetta happy.\n Thank you![await]""",
        ),
        (
            1785,
            """EGGBERT: You visiting us has\n really made Birdetta happy.\n Thank you![await]""",
        ),
        (2061, """EGGBERT: We're making this cake\n look just like Birdetta![await]"""),
        (2062, """EGGBERT: No eggs were harmed\n in the making of this cake.[await]"""),
        (
            2504,
            """BIRDETTA: Hello♥![await]\n ...Oh, no, you're still missing\n [0x7024] item(s)![await]""",
        ),
        (
            2560,
            """EGGBERT: Birdetta's feeling lonely\n today, so feel free to pay her a\n visit upstairs.[await][pause] I'm sure she'd love\n the company.[await][page]\n Just, let me make sure you'll be\n nice, first![await]""",
        ),
        (
            2572,
            """EGGBERT: Pardon me, Birdetta's\n not back here. Please refrain from\n snooping around.[await]""",
        ),
        (2831, """\n          BIRDETTA: Hello♥![await]"""),
        (
            2832,
            """ Hello! You've been chosen to stay\n here in our lovely inn for FREE!\n Aren't you lucky?[await]\n Will you stay with us?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        ),
        (
            2834,
            """ The two guys in the left building\n have been acting suspicious.[await]""",
        ),
        (
            2837,
            """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        ),
        (2838, """ Have you been to Birdetta's\n house up on the hill yet?[await]"""),
        (
            2839,
            """ Hi![delay] Welcome to our town![delay]\n Stay away from our shed, OK~?[await]""",
        ),
        (
            2841,
            """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        ),
        (
            2842,
            """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        ),
        (2843, """ Once you get through the Sunken\n Ship, you can... er...[await]"""),
        (
            2844,
            """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        ),
        (2845, """ Do you think they sell frying pans\n here?[await]"""),
        (
            2847,
            """ It's perfectly normal for two eggs\n to stand outside a locked house![await]""",
        ),
        (2848, """ There's nothing weird going on\n here![await]"""),
        (3044, """BIRDETTA: Ooh, are you gonna play\n with the dojo master?![await]"""),
        (
            3057,
            """ Hello♥! Did you come to play?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        ),
        (
            3072,
            """EGGBERT: What did Birdetta want\n me to do here, again? I'm just an\n egg![await]""",
        ),
        (3073, """EGGBERT: You're making me so\n mad, I could explode![await]"""),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the lady next\n door.[await][page]\n She's always mumbling about\n Egg-this and Playtime-that.[await][page]\n Sometimes I'd like to ask her what\n she's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, """BIRDETTA: Thanks for playing with\n me~![await]"""),
        (3353, """BIRDETTA: Thanks for playing with\n me~![await]"""),
    ]
    optional_dialog_replacements = [
        (
            1694,
            """EGGBERT: Wow, you sure showed\n us! Don't disappoint Birdetta![await]""",
        ),
        (1695, """EGGBERT: Thanks for playing\n with us today![await]"""),
    ]


class DefaultBluebird1(Henchman):
    pack_number = 94
    model = npcs.Bluebird


class DefaultBluebird2(Henchman):
    pack_number = 95
    model = npcs.Bluebird


class DefaultBirdy1(Henchman):
    pack_number = 92
    model = npcs.Birdy


class DefaultBirdy2(Henchman):
    pack_number = 93
    model = npcs.Birdy


class ValentinaBluebird(Henchman):
    pack_number = 205
    model = npcs.Bluebird


class ValentinaBirdy(Henchman):
    pack_number = 201
    model = npcs.Birdy


class ValentinaBoss(Boss):
    name = "Valentina"
    pack_number = 171
    small_model = npcs.ValentinaSmall
    big_model = npcs.ValentinaLarge
    repeatable_henchmen = [ValentinaBluebird, ValentinaBirdy]
    dialog_replacements = [
        (49, """VALENTINA: ...What? You're STILL\n here?! Go AWAY!!![await]"""),
        (
            1660,
            """ ALRIGHT, already![delay_30] If you're going\n to annoy me like this, get in here\n and finish the job![await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Valentina's place.[await]""",
        ),
        (
            1695,
            """PIRATE: That's AMAZING!\n No one's EVER whipped\n VALENTINA!![await]""",
        ),
        (
            1778,
            """VALENTINA: If you don't stop\n bothering me, I'm going to turn\n your mustache into a\n vegetable scrubber![await]""",
        ),
        (
            1780,
            """VALENTINA: YOU again?! You better\n have brought some margaritas![await]""",
        ),
        (
            1781,
            """VALENTINA: Get OFF of my head\n before I take your shoes and throw\n them in the ocean!!![await]""",
        ),
        (
            1783,
            """ Pfffft!  You call THIS a Martini?[await]\n MAKE IT AGAIN, and I MIGHT tip!![await]""",
        ),
        (
            1784,
            """BLUEBIRD: Valentina's grumpy.\n Booster got her a gold beetle for\n their anniversary.[await][pause] She wanted a\n ladybug.[await][page]\n Married life sounds truly weird.[await]""",
        ),
        (
            1793,
            """BLUEBIRD: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """BLUEBIRD: Valentina's grumpy.\n Booster got her a gold beetle for\n their anniversary.[await][pause] She wanted a\n ladybug.[await][page]\n Married life sounds truly weird.[await]""",
        ),
        (
            1785,
            """BLUEBIRD: Valentina's grumpy.\n Booster got her a gold beetle for\n their anniversary.[await][pause] She wanted a\n ladybug.[await][page]\n Married life sounds truly weird.[await]""",
        ),
        (
            2061,
            """ Why are we making a cake that\n looks like Valentina, again?[await]""",
        ),
        (
            2062,
            """ We're making a cake that looks like\n Valentina.[await][pause] What else are we gonna\n do on our day off?[await]""",
        ),
        (
            2504,
            """VALENTINA: STOP BOTHERING ME![await]\n If you need something to do, go\n look for [0x7024] more item(s)![await]""",
        ),
        (
            2560,
            """BLUEBIRD: I hate being a secretary!\n And... [delay_30]I'm going to make this\n your problem![await]""",
        ),
        (
            2572,
            """BLUEBIRD: Whaddya want?[await][pause] You\n better not be trying to bother\n Valentina, [delay]or I'll be in trouble![await]""",
        ),
        (2831, """\n   VALENTINA: I'm SO frustrated![await]"""),
        (
            2832,
            """ Welcome![delay] I'll let you stay here for\n free, but don't tell Valentina.[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        ),
        (
            2834,
            """ The two guys in the left building\n have been acting suspicious.[await]""",
        ),
        (
            2837,
            """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        ),
        (2838, """ Have you been to Valentina's\n house up on the hill yet?[await]"""),
        (
            2839,
            """ Hmm...[delay] What're you loitering\n around here for?[delay] Uh...[delay] Stay away\n from the shed, OK?[await]""",
        ),
        (
            2841,
            """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        ),
        (
            2842,
            """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        ),
        (2843, """ Once you get through the Sunken\n Ship, you can... er...[await]"""),
        (
            2844,
            """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        ),
        (
            2845,
            """ ...I'm on my break. [delay]Just let me\n shop in peace, OK?[await]""",
        ),
        (2847, """\n     You can't just barge in here![await]"""),
        (2848, """\n         Hey! Who're YOU?!...[await]"""),
        (
            3044,
            """VALENTINA: You? Fighting the dojo\n master? Good luck, chump![await]""",
        ),
        (
            3057,
            """ What? What do you want?![await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        ),
        (
            3072,
            """BLUEBIRD: Valentina only gives us\n the most boring jobs to do...[await]""",
        ),
        (3073, """\nBLUEBIRD: I'm bored. Entertain me![await]"""),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the lady next\n door.[await][page]\n She's always mumbling about\n Queen-this and Dodo-that.[await][page]\n Sometimes I'd like to ask her what\n she's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (
            3352,
            """VALENTINA: Is this REALLY going to\n make me powerful enough to take\n ov...[delay_30] I mean...[await][pause][delay_30] pay a cordial visit\n to Nimbus Land?![await]""",
        ),
        (
            3353,
            """VALENTINA: Is this REALLY going to\n make me powerful enough to take\n ov...[delay_30] I mean...[await][pause][delay_30] pay a cordial visit\n to Nimbus Land?![await]""",
        ),
    ]
    optional_dialog_replacements = [
        (
            1694,
            """BLUEBIRD: Whatever, go on and\n fight Valentina. She doesn't pay\n us enough to keep you out.[await]""",
        ),
        (
            1695,
            """BLUEBIRD: Oh, you won?[await]\n [delay_30](...[delay_30]It's about time!)[await]""",
        ),
    ]


class CzarPyrosphere(Henchman):
    pack_number = 190
    model = npcs.RedFireball


class CzarHelio(Henchman):
    pack_number = 193
    model = npcs.Helio


class CzarBoss(Boss):
    name = "Czar Dragon"
    pack_number = 172
    small_model = npcs.CzarDragonSmall
    big_model = npcs.CzarBody
    attack_model = npcs.CzarDragonLarge
    statue = npcs.CzarStatue
    repeatable_henchmen = [CzarPyrosphere]
    dialog_replacements = [
        (49, """\n    CZAR DRAGON: BLARRGGGG[await]"""),
        (1660, """ BLARRGGGG[await]"""),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n the Czar Dragon's place.[await]""",
        ),
        (
            1695,
            """PIRATE: That's AMAZING!\n No one's EVER whipped\n the CZAR DRAGON!![await]""",
        ),
        (1778, """\n    CZAR DRAGON: BLARRGGGG[await]"""),
        (1780, """\n    CZAR DRAGON: BLARRGGGG[await]"""),
        (1781, """\n    CZAR DRAGON: BLARRGGGG[await]"""),
        (
            1783,
            """ FIIIIIIIRRRRREEEEBAAAALLLLLLLL[await]\n WHISSSSSSSSSKEEEEEEEEEEEEY!!![await]""",
        ),
        (1784, EMPTY_DIALOG),
        (1785, EMPTY_DIALOG),
        (1792, EMPTY_DIALOG),
        (1793, EMPTY_DIALOG),
        (2061, EMPTY_DIALOG),
        (2062, EMPTY_DIALOG),
        (
            2504,
            """CZAR DRAGON: BLARRGGGG[await]""",
        ),  # can we make him say BLARG as many times as you have items remaining?
        (2560, EMPTY_DIALOG),
        (2572, EMPTY_DIALOG),
        (2831, """\n  CZAR DRAGON: BLAAARRRGGGG[await]"""),
        (
            2832,
            """ (Stay in the inn for free?)[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        ),
        (2834, EMPTY_DIALOG),
        (2837, EMPTY_DIALOG),
        (2838, EMPTY_DIALOG),
        (2839, EMPTY_DIALOG),
        (2841, EMPTY_DIALOG),
        (2842, EMPTY_DIALOG),
        (2843, EMPTY_DIALOG),
        (2844, EMPTY_DIALOG),
        (2845, EMPTY_DIALOG),
        (2847, EMPTY_DIALOG),
        (2848, EMPTY_DIALOG),
        (3044, """\n  CZAR DRAGON: BLAAARRRGGGG[await]"""),
        (3057, """[delay_60][await]\n  [select] (Yes)\n  [select] (Uh...)[await]"""),
        (3072, EMPTY_DIALOG),
        (3073, EMPTY_DIALOG),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always yelling about\n BLARRRRG-this and\n BLAHGAHRGGH-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, """\n  CZAR DRAGON: BLAAARRRGGGG[await]"""),
        (3353, """\n  CZAR DRAGON: BLAAARRRGGGG[await]"""),
    ]
    optional_dialog_replacements = [
        (1694, EMPTY_DIALOG),
        (1695, EMPTY_DIALOG),
    ]


class AxemRangersAxemBlack(Henchman):
    pack_number = 248
    model = npcs.AxemBlack


class AxemRangersAxemPink(Henchman):
    pack_number = 249
    model = npcs.AxemPink


class AxemRangersAxemYellow(Henchman):
    pack_number = 250
    model = npcs.AxemYellow


class AxemRangersAxemGreen(Henchman):
    pack_number = 251
    model = npcs.AxemGreen


class AxemRangersMachine1(Henchman):
    pack_number = 203
    model = npcs.MachineAxemRed


class AxemRangersMachine2(Henchman):
    pack_number = 203
    model = npcs.MachineAxemPink


class AxemRangersMachine3(Henchman):
    pack_number = 203
    model = npcs.MachineAxemBlack


class AxemRangersMachine4(Henchman):
    pack_number = 203
    model = npcs.MachineAxemYellow


class AxemRangersMachine5(Henchman):
    pack_number = 203
    model = npcs.MachineAxemGreen


class AxemRangersBoss(Boss):
    name = "Axem Red"
    pack_number = 182
    forced_background = 39
    small_model = npcs.AxemRed
    statue = npcs.AxemRedStatue
    unique_henchmen = [
        AxemRangersAxemBlack,
        AxemRangersAxemPink,
        AxemRangersAxemYellow,
        AxemRangersAxemGreen,
    ]
    repeatable_henchmen = [
        AxemRangersMachine1,
        AxemRangersMachine2,
        AxemRangersMachine3,
        AxemRangersMachine4,
        AxemRangersMachine5,
    ]
    dialog_replacements = [
        (
            49,
            """AXEM RED: We're busy playing Uno\n in here. Go bother someone else![await]""",
        ),
        (
            1660,
            """ Listen up, nerd![delay_30] You may have\n figured out our password, but\n we're not going down without\n a fight![await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n the Axem Rangers' place.[await]""",
        ),
        (
            1695,
            """PIRATE: That's AMAZING!\n No one's EVER whipped\n the AXEM RANGERS!![await]""",
        ),
        (1778, """AXEM RED: How could this happen\n to the Axem Rangers?![await]"""),
        (
            1780,
            """AXEM RED: Yo! Quit wasting your\n time around here, you've got a\n world to save![await]""",
        ),
        (
            1781,
            """AXEM RED: Yo, `MAIN_CHARACTER_NAME`!\n This isn't cool!\n Get off of my head.[await]""",
        ),
        (
            1783,
            """ Yo! This energy drink is preem![await]\n Axem Red Bull gives me wings![await]""",
        ),
        (1784, """AXEM BLACK: Red can be kind of\n a chump when he loses.[await]"""),
        (1792, """AXEM YELLOW: Say, do you have\n anything to eat?[await]"""),
        (
            1785,
            """AXEM PINK: I hate it down here!\n The water makes my makeup run![await]""",
        ),
        (
            1793,
            """AXEM GREEN: The four of them may\n be hot heads, but I truly enjoy\n causing mischief with them.[await]""",
        ),
        (
            2061,
            """AXEM YELLOW: Why the heck do\n I have to bake a cake that I'm\n not going to get to eat?![await]""",
        ),
        (
            2062,
            """AXEM GREEN: Not EVERYTHING\n we do is evil. Today we're baking a\n cake that looks like Axem Red.[await]""",
        ),
        (
            2504,
            """AXEM RED: Listen! You're not\n going anywhere until you find [0x7024]\n more of `MARRYMORE_CHARACTER`'s item(s)![await]""",
        ),
        (
            2560,
            """AXEM BLACK: Green hasn't showed\n up to cover me for lunch yet![await][pause] I'm\n so mad, I could fight somebody![await]""",
        ),
        (2572, """AXEM PINK: Where do you clods\n think you're going?![await]"""),
        (2831, """AXEM RED: Listen up![await]\n Quit snooping around town![await]"""),
        (
            2832,
            """AXEM YELLOW: You tired?[await]\n I'm feeling nice today, so you can\n stay for free.[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        ),
        (
            2834,
            """ The two guys in the left building\n have been acting suspicious.[await]""",
        ),
        (
            2837,
            """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        ),
        (2838, """ Have you been to Axem Red's\n house up on the hill yet?[await]"""),
        (
            2839,
            """ They won't give me a better job\n in this town! I wanted to be one\n of the shed guards![await]\n ...What are they guarding?\n [delay]N-nothing![await]""",
        ),
        (
            2841,
            """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        ),
        (
            2842,
            """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        ),
        (2843, """ Once you get through the Sunken\n Ship, you can... er...[await]"""),
        (
            2844,
            """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        ),
        (2845, """ Why does HE get to be the\n shopkeeper?[await]"""),
        (2847, """\n     AXEM BLACK: Beat it, clod![await]"""),
        (
            2848,
            """AXEM PINK: Get lost, mustache!\n [delay]This shed belongs to the Axem\n Rangers![await]""",
        ),
        (
            3044,
            """AXEM RED: Yo! It won't be enough\n to win just once. The dojo master\n has three forms.[await]""",
        ),
        (
            3057,
            """ Yo! What do you want?![await]\n  [select] (A fight)\n  [select] (Uh...)[await]""",
        ),
        (
            3072,
            """AXEM YELLOW: Man...[delay] I wish\n someone would bring me some food\n up here![await]""",
        ),
        (3073, """\n    AXEM YELLOW: Get lost, bub![await]"""),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the people\n next door.[await][page]\n They're always mumbling about\n Shades-this and Makeup-that.[await][page]\n Sometimes I'd like to ask them what\n they're babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, """\n  AXEM RED: I'm way outta shape![await]"""),
        (3353, """\n  AXEM RED: I'm way outta shape![await]"""),
    ]


class ChesterBoss(MimicBoss):
    name = "Chester"
    pack_number = 235
    small_model = npcs.ChesterSmall
    big_model = npcs.ChesterLarge
    statue = npcs.MimicStatue
    dialog_replacements = [
        (49, """CHESTER: Go on, take it. Just let\n me go back to sleep.[await]"""),
        (1660, """ Quit draggin' your feet! Get in\n here and let's fight![await]"""),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Chester's place.[await]""",
        ),
        (
            1695,
            """PIRATE: That's AMAZING!\n No one's EVER whipped \nCHESTER!![await]""",
        ),
        (1778, """CHESTER: (How embarrassing...)[await]"""),
        (
            1780,
            """CHESTER: You know, I'm kind of a\n big deal over in Bowser's Keep.[await]""",
        ),
        (1781, """CHESTER: This is unnecessary. Get\n off me![await]"""),
        (
            1783,
            """ Leave me alone with my precious[await]\n '92 Napper Cabernet Sauivignon.[await]""",
        ),
        (
            1784,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1785,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1793,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            2061,
            """CHEF TORTE: Zees cake, ve make\n it look like mimic! It is...\n masterpiece![await]""",
        ),
        (
            2504,
            """CHESTER: Don't bother me unless\n you have found [0x7024] more item(s).[await]""",
        ),
        (
            2560,
            """SNIFIT 1: Hello there.[await]\n Chester's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        ),
        (2572, """SNIFIT 2: Please refrain\n from bothering Chester.[await]"""),
        (2831, """CHESTER: This town is pretty\n quiet.[await]"""),
        (
            2838,
            """ You will find Chester...\n in his house. He is...the most\n respected person here.[await]""",
        ),
        (3044, """\n   CHESTER: Now THIS I gotta see.[await]"""),
        (
            3057,
            """ You're interrupting my sleep.[await]\n  [select] (I want to fight)\n  [select] (Uh...)[await]""",
        ),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Treasure-this and Dragon-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, """\n  CHESTER: I don't even have legs![await]"""),
        (3353, """\n  CHESTER: I don't even have legs![await]"""),
    ]


class MagikoopaBoss(Boss):
    name = "Magikoopa"
    pack_number = 209
    small_model = npcs.RedMagikoopa
    big_model = npcs.MagikoopaLarge
    statue = npcs.MagikoopaStatue
    dialog_replacements = [
        (
            49,
            """MAGIKOOPA: Normally,[delay] when I\n summon an egg,[delay] it doesn't\n encapsulate me...[await]""",
        ),
        (1660, """ This..is..my ship!\n Come in..if you dare![await]"""),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Magikoopa's place.[await]""",
        ),
        (
            1695,
            """PIRATE: That's AMAZING!\n No one's EVER whipped\n MAGIKOOPA!![await]""",
        ),
        (1778, """\n  MAGIKOOPA: Huh? ...Where am I?[await]"""),
        (1780, """MAGIKOOPA: Hello! How have you\n been?[await]"""),
        (1781, """MAGIKOOPA: Uh, what are you\n doing?[await]"""),
        (
            1783,
            """ My plans are foiled yet again![await]\n There's Magic Hat in my magic hat![await]""",
        ),
        (
            1784,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1785,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1793,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            2061,
            """CHEF TORTE: Zees cake, ve make\n it look like big wizard! It is...\n masterpiece![await]""",
        ),
        (2504, """MAGIKOOPA: You••need••[0x7024] more\n item(s)![await]"""),
        (
            2560,
            """SNIFIT 1: Hello there.[await]\n Magikoopa's busy right now, so\n he can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        ),
        (2572, """SNIFIT 2: Please refrain\n from bothering Magikoopa.[await]"""),
        (2831, """MAGIKOOPA: There's nothing••to\n see••here![await]"""),
        (
            2838,
            """ You will find Magikoopa...\n in his house. He is...the most\n respected person here.[await]""",
        ),
        (
            3044,
            """MAGIKOOPA: Now this should be\n interesting. Can you beat THE\n master, `MAIN_CHARACTER_NAME`?[await]""",
        ),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Yoshi-this and Bowser-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, """MAGIKOOPA: This is more fun than I\n expected![await]"""),
        (3353, """MAGIKOOPA: This is more fun than I\n expected![await]"""),
    ]


class BoomerShyGuy(Henchman):
    pack_number = 154
    model = npcs.ShyGuy


class BoomerBoss(Boss):
    name = "Boomer"
    pack_number = 210
    small_model = npcs.BoomerSmall
    big_model = npcs.BoomerOverworld
    attack_model = npcs.BoomerLarge
    statue = npcs.BoomerStatue
    unique_henchmen = [BoomerShyGuy, BoomerShyGuy]
    repeatable_henchmen = [BoomerShyGuy]
    dialog_replacements = [
        (
            49,
            """BOOMER: I lost fair and square.[await]\n Now it is time for me to sleep.[await]""",
        ),
        (
            1660,
            """ Ahhhhh... So, it's YOU who solved\n my riddle![delay_30] Now, you've got to deal\n with ME![await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Boomer's place.[await]""",
        ),
        (1695, """PIRATE: That's AMAZING!\n No one's EVER whipped BOOMER!![await]"""),
        (1778, """BOOMER: I don't need your\n sympathy! Go on...[await]"""),
        (
            1780,
            """BOOMER: A true soldier knows\n when to accept defeat. You earned\n your victory.[await]""",
        ),
        (1781, """BOOMER: This is absurd! Get off\n of my head.[await]"""),
        (
            1783,
            """ Great battle deserves great Sake![await]\n Join me, `MAIN_CHARACTER_NAME`.  Kampai![await]""",
        ),
        (
            1784,
            """CHANDELI-HO: There's nowhere for\n Boomer to crash down onto in here!\n Thank goodness![await]""",
        ),
        (
            1793,
            """CHANDELI-HO: Hop on the\n trampoline in the next room. It'll\n take you outside.[await]""",
        ),
        (
            1792,
            """CHANDELI-HO: There's nowhere for\n Boomer to crash down onto in here!\n Thank goodness![await]""",
        ),
        (
            1785,
            """CHANDELI-HO: There's nowhere for\n Boomer to crash down onto in here!\n Thank goodness![await]""",
        ),
        (
            2061,
            """CHANDELI-HO: We're making a cake\n to look just like Boomer![await]""",
        ),
        (2062, """CHANDELI-HO: We've gotten REAL\n good with fondant![await]"""),
        (
            2504,
            """BOOMER: Ha ha ha![delay_30] So, you found\n [0x7000] item(s) already. Impressive.[await][pause] But\n now you've got to find [0x7024] more![await]""",
        ),
        (
            2560,
            """CHANDELI-HO: Welcome! Have you\n come to install the chandelier?[await][page]\n ...No?[delay] Well, you'd better leave\n Boomer alone![await]""",
        ),
        (2572, """CHANDELI-HO: I won't let you\n bother Boomer![await]"""),
        (
            2831,
            """BOOMER: Ha ha ha![await][pause] So, you've\n found our village![await]""",
        ),
        (
            2832,
            """ Hi! Are you tired? You can rest\n up here, and you don't have to\n pay me anything.[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        ),
        (
            2834,
            """ The two guys in the left building\n have been acting suspicious.[await]""",
        ),
        (
            2837,
            """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        ),
        (2838, """ Have you been to Boomer's house\n up on the hill yet?[await]"""),
        (2839, """ ...Stay away from the shed, OK?\n It's scary![await]"""),
        (
            2841,
            """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        ),
        (
            2842,
            """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        ),
        (2843, """ Once you get through the Sunken\n Ship, you can... er...[await]"""),
        (
            2844,
            """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        ),
        (2845, """ I'm upset. There's no candles on\n sale here.[await]"""),
        (2847, """\n      Sorry, we can't let you in![await]"""),
        (
            2848,
            """ This is Boomer's top-secret shed![await]\n ...Oh no, was I supposed to tell\n you it's top secret?[await]""",
        ),
        (
            3044,
            """BOOMER: Ha ha ha! A match\n against the dojo master?!\n This ought to be fun![await]""",
        ),
        (
            3057,
            """ Gahahaha! Is it a fight you seek?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        ),
        (
            3072,
            """CHANDELI-HO: Whew...[delay] It's weird\n for me to say,[delay] but I think I might\n be afraid of heights.[await]""",
        ),
        (3073, """CHANDELI-HO: I won't let anything\n bad happen to Boomer![await]"""),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Soldier-this and Honor-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (
            3352,
            """BOOMER: You won fair and square!\n But I won't make it so easy for you\n next time![await]""",
        ),
        (
            3353,
            """BOOMER: You won fair and square!\n But I won't make it so easy for you\n next time![await]""",
        ),
    ]
    optional_dialog_replacements = [
        (1694, """CHANDELI-HO: Oh, no, I lost!\n Good luck, Boomer![await]"""),
        (1695, """CHANDELI-HO: I hope you didn't\n hurt Boomer too bad![await]"""),
    ]


class ExorBoss(Boss):
    name = "Exor"
    pack_number = 186
    forced_background = 16
    small_model = npcs.ExorSmall
    statue = npcs.ExorStatue
    dialog_replacements = [
        (49, """  EXOR: What do you want? Get\n lost![await]"""),
        (
            1660,
            """ Halt! This ship belongs to ME!\n If you want to get through...\n bring it on![await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Exor's place.[await]""",
        ),
        (1695, """PIRATE: That's AMAZING!\n No one's EVER whipped EXOR!![await]"""),
        (
            1778,
            """EXOR: If it weren't for nosey\n characters like you, I could live in\n this ship undisturbed![await]""",
        ),
        (
            1780,
            """EXOR: Halt! Don't even THINK\n about leaving until you've had\n some of this juice![await]""",
        ),
        (
            1781,
            """EXOR: Look, if you really want to\n humiliate me, why not use\n Geno Whirl too, while you're at it?[await]""",
        ),
        (
            1783,
            """ You think I was MADE this HUGE?![await]\n No, I drank my Milk EVERY DAY!!![await]""",
        ),
        (
            1784,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1785,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1793,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            2061,
            """CHEF TORTE: Zees cake, ve make\n it look like big sword man! It is...\n masterpiece![await]""",
        ),
        (
            2504,
            """EXOR: Halt![await][pause] What do you have\n here?[delay] [0x7000] item(s)?[await]\n No, this won't do.[await][pause] Find [0x7024] more,\n[delay] or I won't let you through![await]""",
        ),
        (
            2560,
            """SNIFIT 1: Hello there.[await]\n Exor's busy right now, so he\n can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        ),
        (2572, """SNIFIT 2: Please refrain\n from bothering Exor.[await]"""),
        (
            2831,
            """EXOR: There isn't much to see in\n this town. Especially not in\n the shed.[await]""",
        ),
        (
            2838,
            """ You will find Exor...\n in his house. He is...the most\n respected person here.[await]""",
        ),
        (
            3044,
            """EXOR: Think you're gonna beat the\n dojo master? Now this I GOTTA\n see![await]""",
        ),
        (
            3057,
            """ Halt! What do you want?[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        ),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Nosey-this and Trespasser-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, """\n        EXOR: How humiliating![await]"""),
        (3353, """\n        EXOR: How humiliating![await]"""),
    ]


class CountdownDingALing(Henchman):
    pack_number = 252
    model = npcs.DingalingGridplane


class CountdownBoss(Boss):
    name = "Count Down"
    pack_number = 174
    forced_background = 18
    small_model = npcs.CountDownGridplane
    statue = npcs.CountDownStatue
    unique_henchmen = [CountdownDingALing, CountdownDingALing]
    repeatable_henchmen = [CountdownDingALing]
    dialog_replacements = [
        (49, """COUNT DOWN: Sometimes, even an\n alarm clock needs to sleep.[await]"""),
        (
            1660,
            """ This is not good![delay_30]\n He figured out the password![delay_30]\n ...We better do something![await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Count Down's place.[await]""",
        ),
        (
            1695,
            """PIRATE: That's AMAZING!\n No one's EVER whipped\n COUNT DOWN!![await]""",
        ),
        (1778, """COUNT DOWN: ...What time is it?\n Time for you to leave![await]"""),
        (
            1780,
            """COUNT DOWN: What are you still\n doing around here? Taking a break,\n huh?[await]""",
        ),
        (1781, """\n   COUNT DOWN: This is not good![await]"""),
        (
            1783,
            """ Ahh, fresh squeezed Orange Juice-[await]\n The second best way to wake up![await]""",
        ),
        (
            1784,
            """DING-A-LING: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        ),
        (
            1785,
            """DING-A-LING: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        ),
        (
            2061,
            """DING-A-LING: I guess it is a little\n weird to make a cake that looks\n like a clock with no body.[await]""",
        ),
        (
            2062,
            """DING-A-LING: Are you impressed by\n how well we can bake without\n having any hands?[await]""",
        ),
        (
            2504,
            """COUNT DOWN: You've only got\n [0x7000] item(s)! You're missing [0x7024]![await]\n You better do something![await]""",
        ),
        (
            2560,
            """DING-A-LING: `MAIN_CHARACTER_NAME`'s HERE![await][pause][delay_30]\n I'd better do something![await]""",
        ),
        (
            2572,
            """DING-A-LING: You won't find\n Count Down back here![await]\n Leave us alone![await]""",
        ),
        (2831, """COUNT DOWN: There's nothing to\n do here![await]"""),
        (
            2832,
            """ Our inn is free![await][pause] Why?[delay_30] Uh...[delay]\n I'm not sure.[delay_30] Anyway,[delay] do you\n want to stay?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        ),
        (
            2834,
            """ The two guys in the left building\n have been acting suspicious.[await]""",
        ),
        (
            2837,
            """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        ),
        (2838, """ Have you been to Count Down's\n house up on the hill yet?[await]"""),
        (
            2841,
            """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        ),
        (
            2842,
            """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        ),
        (2843, """ Once you get through the Sunken\n Ship, you can... er...[await]"""),
        (
            2844,
            """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        ),
        (2847, """\n       This is off-limits! Scram![await]"""),
        (2848, """\n       Get outta here! Beat it![await]"""),
        (3044, """COUNT DOWN: The dojo master will\n be tough to beat![await]"""),
        (
            3072,
            """DING-A-LING: Man...[delay_15] I'm tired.[await]\n Even alarm bells get tired\n sometimes.[await]""",
        ),
        (
            3073,
            """DING-A-LING: Back off![delay_15] I know\n Fear Roulette and I'm not afraid\n to use it![await]""",
        ),
        (
            3057,
            """ Uh-oh! Are you looking for\n trouble?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        ),
        (
            3338,
            """ It's really weird.\n The guy next door never seems\n to shut his alarm clock off.[await][page]\n I'd like to go over and give him a\n piece of my mind, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (
            3352,
            """COUNT DOWN: This is a weird\n training regimen for an alarm\n clock![await]""",
        ),
        (
            3353,
            """COUNT DOWN: This is a weird\n training regimen for an alarm\n clock![await]""",
        ),
    ]
    # unsure if this makes sense to do with countdown. dingalings are kinda terrible to vram
    optional_dialog_replacements = [
        (
            1694,
            """DING-A-LING: We failed to stop\n you. Go ahead into Count Down's\n room![await]""",
        ),
        (
            1695,
            """DING-A-LING: You beat Count Down!\n We didn't see that coming![await]""",
        ),
        # come up with something for booster's other replacement dialogs if it's feasible to have 4 bells in curtain room
    ]


class CloakerDominoBoss(Boss):
    name = "Domino"
    pack_number = 184
    forced_background = 40
    small_model = npcs.DominoSmall
    big_model = npcs.DominoLarge
    statue = npcs.DominoStatue
    dialog_replacements = [
        (
            49,
            """DOMINO: I'm busy wallowing in\n misery at my defeat here.[await][pause] Get lost![await]""",
        ),
        (
            1660,
            """ Uh oh, you cracked the code...\n I don't like where this is going...[await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Cloaker and Domino's place.[await]""",
        ),
        (
            1695,
            """PIRATE: That's AMAZING!\n No one's EVER whipped\n CLOAKER and DOMINO!![await]""",
        ),
        (1778, """DOMINO: Guess you're tougher\n than I thought...[await]"""),
        (1780, """\n DOMINO: So, you've returned...![await]"""),
        (1781, """DOMINO: I don't like where this is\n going...[await]"""),
        (
            1783,
            """ I always enjoy a nice Bubble Tea[await]\n...after CLOBBERING TIME!![await]""",
        ),
        (
            1784,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1785,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1793,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            2061,
            """CHEF TORTE: Zees cake, ve make\n it look like big brick! It is...\n masterpiece![await]""",
        ),
        (
            2504,
            """DOMINO: Hee hee hee... You still\n need to find [0x7024] more item(s)![await]""",
        ),
        (
            2560,
            """SNIFIT 1: Hello there.[await]\n Cloaker and Domino are busy right\n now, so they can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        ),
        (
            2572,
            """SNIFIT 2: Please refrain\n from bothering Cloaker and Domino.[await]""",
        ),
        (
            2831,
            """DOMINO: Hee hee hee... So you've\n found our little town! Boring,\n isn't it?[await]""",
        ),
        (
            2838,
            """ You will find Domino...\n in his house. He is...the most\n respected person here.[await]""",
        ),
        (
            3044,
            """DOMINO: Hee hee hee... So you're\n challenging the dojo master?[await]""",
        ),
        (
            3057,
            """ Hee hee hee... Wanna fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        ),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the people\n next door.[await][page]\n They're always mumbling about\n Weaklings-this and Snake-that.[await][page]\n Sometimes I'd like to ask them what\n they're babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (
            3352,
            """DOMINO: This is exactly the kind\n of training I needed.[await][pause] Fusing myself\n with a snake just hasn't been\n getting me the results I wanted.[await]""",
        ),
        (
            3353,
            """DOMINO: This is exactly the kind\n of training I needed.[await][pause] Fusing myself\n with a snake just hasn't been\n getting me the results I wanted.[await]""",
        ),
    ]


class DefaultMadMallet(Henchman):
    pack_number = 150
    model = npcs.MadMallet


class ClerkMadMallet(Henchman):
    pack_number = 155
    model = npcs.MadMallet


class ClerkBoss(Boss):
    name = "Clerk"
    pack_number = 146
    small_model = npcs.ClerkSmall
    big_model = npcs.ClerkLarge
    statue = npcs.ShovelKnightStatue
    unique_henchmen = [ClerkMadMallet, ClerkMadMallet]
    repeatable_henchmen = [ClerkMadMallet]
    dialog_replacements = [
        (49, """CLERK: I'm going to sleep for 10\n years.[await]"""),
        (
            1660,
            """ Sorry, you may have figured out the\n password, but I can't allow you\n through without a fight.[await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n the Clerk's place.[await]""",
        ),
        (
            1695,
            """PIRATE: That's AMAZING!\n No one's EVER whipped\n the CLERK!![await]""",
        ),
        (
            1778,
            """CLERK: I don't get paid nearly\n enough to get whooped that\n badly...[await]""",
        ),
        (
            1780,
            """CLERK: So, you've come back! I\n hope your journey is staying on\n schedule![await]""",
        ),
        (1781, """CLERK: What do you think you're\n doing?![await]"""),
        (
            1783,
            """ You'll have to take this up with the[await]\n Manager.  I'M having an Espresso.[await]""",
        ),
        (
            1784,
            """MAD MALLET: To be honest, I hate\n fighting alone. I'll run away if I'm\n the last one left in a battle.[await]\n  It sounds cowardly, but this is\n just the way I am.[await]""",
        ),
        (
            1793,
            """MAD MALLET: Hop on the\n trampoline in the next room. It'll\n take you outside.[await]""",
        ),
        (
            1792,
            """MAD MALLET: To be honest, I hate\n fighting alone. I'll run away if I'm\n the last one left in a battle.[await]\n  It sounds cowardly, but this is\n just the way I am.[await]""",
        ),
        (
            1785,
            """MAD MALLET: To be honest, I hate\n fighting alone. I'll run away if I'm\n the last one left in a battle.[await]\n  It sounds cowardly, but this is\n just the way I am.[await]""",
        ),
        (
            2061,
            """MAD MALLET: We're making a cake\n to look just like the Clerk![await]""",
        ),
        (2062, """MAD MALLET: We've gotten REAL\n good with fondant![await]"""),
        (
            2504,
            """CLERK: Whatcha got? [0x7000] item(s)?\n At this rate, you should find the\n last [0x7024] in no time![await]""",
        ),
        (
            2560,
            """MAD MALLET: Welcome.[await][pause] It's the\n Clerk's day off, so he's not taking\n visitors today.[await][page]\n ...But if you insist, I'll have to\n keep you out myself![await]""",
        ),
        (
            2572,
            """MAD MALLET: Listen, the Clerk\n doesn't get paid enough to deal\n with you.[await][page]\n  I certainly don't either, but I'm\n having a bad day![await]""",
        ),
        (
            2831,
            """CLERK: Not much happens in this\n quiet and completely unsuspicious\n town.[await]""",
        ),
        (
            2832,
            """ Welcome.[delay] Would you like to stay\n here for free?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        ),
        (
            2834,
            """ The two guys in the left building\n have been acting suspicious.[await]""",
        ),
        (
            2837,
            """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        ),
        (2838, """ Have you been to the Clerk's\n house up on the hill yet?[await]"""),
        (2839, """\nDon't go snooping around our town![await]"""),
        (
            2841,
            """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        ),
        (
            2842,
            """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        ),
        (2843, """ Once you get through the Sunken\n Ship, you can... er...[await]"""),
        (
            2844,
            """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        ),
        (2845, """\n        I'm just shopping here![await]"""),
        (2847, """\n                 Get lost![await]"""),
        (
            2848,
            """ Hey buddy, why don't you go snoop\n around some other houses instead?[await]""",
        ),
        (
            3044,
            """CLERK: Now this should be\n interesting. Can you beat THE\n master, `MAIN_CHARACTER_NAME`?[await]""",
        ),
        (
            3057,
            """ Are you here for a fight?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        ),
        (3072, """MAD MALLET: Wow! I can see\n Nimbus Land from here![await]"""),
        (3073, """MAD MALLET: I'm gonna THRASH\n ya![await]"""),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Hammer-this and Puffball-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, """CLERK: If anyone asks, I'm on\n break![await]"""),
        (3353, """CLERK: If anyone asks, I'm on\n break![await]"""),
    ]
    optional_dialog_replacements = [
        (1694, """MAD MALLET: You trashed us!\n Go on to the Clerk's place.[await]"""),
        (
            1695,
            """MAD MALLET: Whoa... No one's\n beaten the Clerk in 10 years![await]""",
        ),
    ]


class ManagerPounder(Henchman):
    pack_number = 126
    model = npcs.Pounder


class ManagerBoss(Boss):
    name = "Manager"
    pack_number = 147
    small_model = npcs.ManagerSmall
    big_model = npcs.ManagerLarge
    statue = npcs.ShovelKnightStatue
    unique_henchmen = [ManagerPounder, ManagerPounder, ManagerPounder]
    repeatable_henchmen = [ManagerPounder]
    dialog_replacements = [
        (49, """MANAGER: I'm going to sleep for 25\n years.[await]"""),
        (1660, """ Who gave you the password?!\n You're gonna pay for this![await]"""),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n the Manager's place.[await]""",
        ),
        (
            1695,
            """PIRATE: That's AMAZING!\n No one's EVER whipped\n the MANAGER!![await]""",
        ),
        (1778, """MANAGER: Why don't you just jump\n on out of here?![await]"""),
        (1780, """MANAGER: Oh, you've returned.\n Good work so far.[await]"""),
        (
            1781,
            """MANAGER: Get off of my head\n before I make you take the longest\n jump of your life![await]""",
        ),
        (
            1783,
            """ DON'T bother the Director with this.[await]\n Just, drink my Cappuccino. Happy?[await]""",
        ),
        (
            1784,
            """POUNDER: This is way more fun\n than working in the factory was.[await]""",
        ),
        (
            1793,
            """POUNDER: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """POUNDER: This is way more fun\n than working in the factory was.[await]""",
        ),
        (
            1785,
            """POUNDER: This is way more fun\n than working in the factory was.[await]""",
        ),
        (
            2061,
            """POUNDER: We're making a cake\n to look just like the Manager![await]""",
        ),
        (2062, """POUNDER: We've gotten REAL\n good with fondant![await]"""),
        (
            2504,
            """MANAGER: Heh heh heh.[delay] Good work.[await]\n You just need [0x7024] more item(s).[await]""",
        ),
        (
            2560,
            """POUNDER: Good day.[await][pause] The Manager\n is busy today and will not be\n seeing any guests.[await][pause]\n If you try to force your way in,\n I'll have to deal with you![await]""",
        ),
        (
            2572,
            """POUNDER: Stay outta our hair![await]\n [delay]...Huh? [delay]“You don't have hair”?[await][pause]\n That's it, you're asking for it![await]""",
        ),
        (
            2831,
            """MANAGER: Come to invade our\n town, have you?[await][pause] No need, there's\n nothing of interest here, I swear![await]""",
        ),
        (
            2832,
            """ Good day.[delay] We're offering free\n reservations today. Would you like\n to stay?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        ),
        (
            2834,
            """ The two guys in the left building\n have been acting suspicious.[await]""",
        ),
        (
            2837,
            """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        ),
        (
            2838,
            """ Have you been to the Manager's\n house up on the hill yet?[await]""",
        ),
        (
            2839,
            """ If you're gonna snoop around,\n [delay]just don't do it near the shed![await]""",
        ),
        (
            2841,
            """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        ),
        (
            2842,
            """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        ),
        (2843, """ Once you get through the Sunken\n Ship, you can... er...[await]"""),
        (
            2844,
            """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        ),
        (
            2845,
            """ Hey buddy, I'm just trying to shop\n here. Why don't you mind your own\n business?[await]""",
        ),
        (2847, """\n             Don't bother us![await]"""),
        (2848, """\n      Can't you see we're busy?[await]"""),
        (3044, """MANAGER: You think you can beat\n the dojo master?![await]"""),
        (
            3057,
            """ Yes?[await][pause] What do you want?[await]\n  [select] (Fight me!)\n  [select] (Uh...)[await]""",
        ),
        (3072, """POUNDER: Man, I need a break. This\n job is tiring.[await]"""),
        (
            3073,
            """POUNDER: Bullet Bill production is\n on schedule! Don't get in my way![await]""",
        ),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Hammer-this and Schedule-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, """MANAGER: Don't interrupt me while\n I'm training![await]"""),
        (3353, """MANAGER: Don't interrupt me while\n I'm training![await]"""),
    ]
    optional_dialog_replacements = [
        (1694, """POUNDER: We lost, but we made\n the Manager proud![await]"""),
        (
            1695,
            """POUNDER: Wow! The Manager's\n been here 25 years, and you just\n dethroned him![await]""",
        ),
    ]


class DirectorPoundette(Henchman):
    pack_number = 128
    model = npcs.Poundette


class DirectorBoss(Boss):
    name = "Director"
    pack_number = 148
    small_model = npcs.DirectorSmall
    big_model = npcs.DirectorLarge
    statue = npcs.ShovelKnightStatue
    unique_henchmen = [
        DirectorPoundette,
        DirectorPoundette,
        DirectorPoundette,
        DirectorPoundette,
    ]
    repeatable_henchmen = [DirectorPoundette]
    dialog_replacements = [
        (49, """DIRECTOR: (Could this day get any\n worse?)[await]"""),
        (
            1660,
            """ Figured out the password, did you?[delay_30]\n Don't get too cocky![delay_30]\n Intruders will be eliminated![await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n the Director's place.[await]""",
        ),
        (
            1695,
            """PIRATE: That's AMAZING!\n No one's EVER whipped\n the DIRECTOR!![await]""",
        ),
        (
            1778,
            """DIRECTOR: I'm afraid I have more\n pressing matters to attend to.\n Depart at once.[await]""",
        ),
        (
            1780,
            """DIRECTOR: Do not waste too much\n time here. Your quest must\n continue.[await]""",
        ),
        (
            1781,
            """DIRECTOR: Any tomfoolery will be\n dealt with by immediate meltdown.\n Get off of my head.[await]""",
        ),
        (
            1783,
            """ Only the Chief can help you, now.[await]\n I have a Latte with my name on it.[await]""",
        ),
        (
            1784,
            """POUNDETTE: I don't feel like I'm\n being used to my full potentia\n down here, but I don't mind\n having a break.[await]""",
        ),
        (
            1793,
            """POUNDETTE: Hop on the trampoline\n in the next room. It'll take you\n outside. Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """POUNDETTE: I don't feel like I'm\n being used to my full potentia\n down here, but I don't mind\n having a break.[await]""",
        ),
        (
            1785,
            """POUNDETTE: I don't feel like I'm\n being used to my full potentia\n down here, but I don't mind\n having a break.[await]""",
        ),
        (
            2061,
            """POUNDETTE: We're making a cake\n to look just like the Director![await]""",
        ),
        (2062, """POUNDETTE: We've gotten REAL\n good with fondant![await]"""),
        (
            2504,
            """DIRECTOR: I'm afraid you must\n continue searching.[delay] There are\n [0x7024] item(s) remaining.[await]""",
        ),
        (
            2560,
            """POUNDETTE: Salutations.[await][pause] Would you\n like to book an appointment with\n the Director?[await][pause]\n ...You want to just barge right\n in?![delay] No way![await]\n Time to teach you some manners![await]""",
        ),
        (
            2572,
            """POUNDETTE: The Director doesn't\n want anyone coming back here.[await]\n So I'm going to have to ask you\n to leave.[await]""",
        ),
        (
            2831,
            """DIRECTOR: I'm afraid there is\n nothing of concern to you in\n this town.[await]""",
        ),
        (
            2832,
            """ Salutations. How would you like to\n stay in our inn for free today?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        ),
        (
            2834,
            """ The two guys in the left building\n have been acting suspicious.[await]""",
        ),
        (
            2837,
            """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        ),
        (
            2838,
            """ Have you been to the Director's\n house up on the hill yet?[await]""",
        ),
        (
            2839,
            """ There's nothing suspicious going on\n in our town! [delay]Now go on, go to the\n next town![await]""",
        ),
        (
            2841,
            """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        ),
        (
            2842,
            """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        ),
        (2843, """ Once you get through the Sunken\n Ship, you can... er...[await]"""),
        (
            2844,
            """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        ),
        (2845, """ No, you can't see what I'm buying!\n [delay]How rude![await]"""),
        (2847, """\n                   Scram![await]"""),
        (
            2848,
            """ There's some important business\n happening in this shed, so get lost\n and quit trying to interrupt us![await]""",
        ),
        (
            3044,
            """DIRECTOR: I'm afraid the dojo\n master will be quite a challenge for\n you to beat.[await]""",
        ),
        (
            3057,
            """ State your business.[await]\n  [select] (Fight me)\n  [select] (Uh...)[await]""",
        ),
        (3072, """POUNDETTE: Finally, some time to\n rest![await]"""),
        (3073, """\nPOUNDETTE: Let's see whatcha got![await]"""),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Hammer-this and Meltdown-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (
            3352,
            """DIRECTOR: This is quite the\n difficult regimen for a white-collar\n fellow like me.[await]""",
        ),
        (
            3353,
            """DIRECTOR: This is quite the\n difficult regimen for a white-collar\n fellow like me.[await]""",
        ),
    ]
    optional_dialog_replacements = [
        (1694, """POUNDETTE: Well, we lost.\n Time for a break.[await]"""),
        (1695, """POUNDETTE: You beat the Director!\n Impressive![await]"""),
    ]


class DefaultUnpaintedDrillBit(Henchman):
    pack_number = None
    model = npcs.MachineDrillBit


class DefaultPaintedDrillBit(Henchman):
    pack_number = None
    model = npcs.Jabit


class GunyolkPiece(Henchman):
    pack_number = None
    model = npcs.GunyolkTop


class GunyolkBoss(Boss):
    name = "Factory Chief"
    pack_number = 149
    small_model = npcs.FactoryChief
    statue = npcs.FactoryChiefStatue
    dialog_replacements = [
        (49, """FACTORY CHIEF: Grrr... Leave me\n alone![await]"""),
        (
            1660,
            """ So, you solved it?[delay_30]\n Too bad, this is the end of the line\n for you! I won't let you through![await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n the Gunyolk's place.[await]""",
        ),
        (
            1695,
            """PIRATE: That's AMAZING!\n No one's EVER whipped\n the GUNYOLK!![await]""",
        ),
        (
            1778,
            """FACTORY CHIEF: Harrumph! Get out\n of here before I invent something\n even stronger![await]""",
        ),
        (
            1780,
            """FACTORY CHIEF: I'm surprised to\n see you back here! I don't have any\n new inventions to show yet.[await]""",
        ),
        (
            1781,
            """FACTORY CHIEF: Harrumph! I should\n invent myself a spiky hat![await]""",
        ),
        (
            1783,
            """ Who do I have to Breaker Beam[await]\n to get a cuppa Coffee 'round here?[await]""",
        ),
        (
            1784,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1785,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1792,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            1793,
            """ Hop on the trampoline in the next\n room. It'll take ya outside.\n Go on, now. Give it a try![await]""",
        ),
        (
            2061,
            """CHEF TORTE: Zees cake, ve make\n it look like big ninja! It is...\n masterpiece![await]""",
        ),
        (
            2504,
            """FACTORY CHIEF: Harrumph! You're\n still missing [0x7024] more item(s)![await]""",
        ),
        (
            2560,
            """SNIFIT 1: Hello there.[await]\n The Gunyolk is busy right now, so\n it can't play.[await][page]\n Come back some other time, or you\n can try to force your way in...[await]""",
        ),
        (2572, """SNIFIT 2: Please refrain\n from bothering the Gunyolk.[await]"""),
        (2831, """FACTORY CHIEF: Harrumph! What're\n you doing here?[await]"""),
        (
            2838,
            """ You will find the Factory Chief...\n in his house. He is...the most\n respected person here.[await]""",
        ),
        (
            3044,
            """FACTORY CHIEF: Harrumph! Just\n because you beat me, doesn't mean\n you can beat the dojo master![await]""",
        ),
        (
            3057,
            """ Did you come here to fight me?[await]\n  [select] (Yes)\n  [select] (Uh...)[await]""",
        ),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Ninja-this and Invention-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (
            3352,
            """FACTORY CHIEF: I'll out-jump you\n if it's the last thing I do![await]""",
        ),
        (
            3353,
            """FACTORY CHIEF: I'll out-jump you\n if it's the last thing I do![await]""",
        ),
    ]


class SmithyDrillBit(Henchman):
    pack_number = 253
    model = npcs.DrillBit


class SmithyShyster(Henchman):
    pack_number = 254
    model = npcs.Shyster


class SmithyAero(Henchman):
    pack_number = 255
    model = npcs.AeroUpright


class SmithyBoss(Boss):
    name = "Smithy"
    pack_number = 185
    small_model = npcs.SmithySmall
    big_model = npcs.SmithyLarge
    statue = npcs.SmithyStatue
    unique_henchmen = [SmithyDrillBit, SmithyShyster, SmithyAero]
    repeatable_henchmen = [SmithyDrillBit, SmithyShyster, SmithyAero]
    dialog_replacements = [
        (49, """SMITHY: How utterly annoying!\n Leave me alone![await]"""),
        (
            1660,
            """ Gufaw, haw, haw![delay_30] You really think\n I'm going to let you through with\n just a password?![await]""",
        ),
        (
            1694,
            """PIRATE: You're pretty tough, `MAIN_CHARACTER_MOLE_GREETING`.\n All right. I'll let you through to\n Smithy's place.[await]""",
        ),
        (1695, """PIRATE: That's AMAZING!\n No one's EVER whipped\n SMITHY!![await]"""),
        (
            1778,
            """SMITHY: How utterly annoying!\n Get out of here before I crush\n you all![await]""",
        ),
        (
            1780,
            """SMITHY: Gufaw, haw, haw...\n Not quite as impressive as my\n factory, eh?[await]""",
        ),
        (1781, """SMITHY: Never have I been so\n wronged![await]"""),
        (
            1783,
            """ This isn't even my final form![await]\n Barkeep!  Bring me more Ale!![await]""",
        ),
        (
            1784,
            """ The foundation in this old haunted\n ship looks pretty weak. So we try\n not to make Smithy too mad.[await]""",
        ),
        (
            1793,
            """ Hop on the trampoline in the next\n room. It'll take you outside.[await]""",
        ),
        (
            1792,
            """ The foundation in this old haunted\n ship looks pretty weak. So we try\n not to make Smithy too mad.[await]""",
        ),
        (
            1785,
            """ The foundation in this old haunted\n ship looks pretty weak. So we try\n not to make Smithy too mad.[await]""",
        ),
        (
            2061,
            """MACHINE MADE: We're making a cake\n to look just like Smithy![await]""",
        ),
        (2062, """MACHINE MADE: We've gotten REAL\n good with fondant![await]"""),
        (
            2504,
            """SMITHY: How utterly annoying![await]\n Give me [0x7024] more item(s)![await]""",
        ),
        (
            2560,
            """MACHINE MADE: Yo![await][pause] Smithy's busy,\n so come back another time! [await][page]\n [delay]...You sure you wanna just barge\n in like that?[await][pause] Alright buddy, don't\n say I didn't warn you![await]""",
        ),
        (
            2572,
            """MACHINE MADE: Man, what's your\n deal?[await][pause] Quit snooping around!\n Smithy'll have a fit![await]""",
        ),
        (
            2831,
            """SMITHY: So, it's YOU![await]\n Unfortunately for you, there's\n nothing evil in this town that\n demands your attention.[await]""",
        ),
        (
            2832,
            """ Yo. This inn doesn't charge\n anything for our services.\n Wanna stay?[await]\n  [select] (Thanks)\n  [select] (I'll pass)[await]""",
        ),
        (
            2834,
            """ The two guys in the left building\n have been acting suspicious.[await]""",
        ),
        (
            2837,
            """ If you can't get into the Sunken\n Ship, you might have to check it\n out later.[await]""",
        ),
        (2838, """ Have you been to Smithy's house\n up on the hill yet?[await]"""),
        (
            2839,
            """ The shed...?[delay] No, there's nothing in\n there! Take my word for it.[await]""",
        ),
        (
            2841,
            """ Have you found the Sunken Ship\n yet? There's something about it I\n was supposed to tell you...[await]""",
        ),
        (
            2842,
            """ Oh, yeah, there's a wall of boxes\n hiding a treasure chest. It's pretty\n easy to miss it.[await]""",
        ),
        (2843, """ Once you get through the Sunken\n Ship, you can... er...[await]"""),
        (
            2844,
            """ You can come back here. We'll have\n something good waiting for you...\n heh heh...[await]""",
        ),
        (
            2845,
            """ What am I doing with this stuff?\n ...None of your business![await]""",
        ),
        (2847, """\n             Get out of here![await]"""),
        (2848, """ No visitors allowed in the shed!\n Scram![await]"""),
        (
            3057,
            """ Grr... What do you want?[await]\n  [select] (Fight me!)\n  [select] (Uh...)[await]""",
        ),
        (3044, """\n   SMITHY: Grr... Leave me alone![await]"""),
        (3072, """MACHINE MADE: It's pretty drafty\n in here![await]"""),
        (3073, """\n MACHINE MADE: Oh, no you don't![await]"""),
        (
            3338,
            """ It's really weird.\n Sometimes I hear the guy next door.[await][page]\n He's always mumbling about\n Factory-this and Weapon-that.[await][page]\n Sometimes I'd like to ask him what\n he's babbling about, but the door\n won't open without a Shiny Stone.[await][page]\n `FIREWORKS_CLAUSE`[await]""",
        ),
        (3352, """SMITHY: Grr... [delay]You're stronger\n than I thought...[await]"""),
        (3353, """SMITHY: Grr... [delay]You're stronger\n than I thought...[await]"""),
    ]
    optional_dialog_replacements = [
        (1694, """ You're pretty tough, but are you\n ready to fight Smithy?[await]"""),
        (1695, """ Oh, wow, you did it![delay] No wonder we\n lost to you...[await]"""),
    ]


# ****************************** Actual location classes
class HammerBros(BossAndStarLocation):
    _identifier = 205
    description = AvailableBosses.HammerBro.value
    name = "Hammer Bro"
    battlefield = Battlefields.MushroomWay
    music = music.MidbossMusic

    boss = HammerBroBoss
    boss_locations = [
        BossModelFill(
            Rooms._205_MUSHROOM_WAY_AREA_03,
            7,
            HammerBroBoss,
            SpriteSize.Large,
            False,
            target_scripts=[2809],
            sequence_setter=755,
        )
    ]


class Croco1(BossAndStarLocation):
    _identifier = 206
    description = AvailableBosses.Croco1.value
    name = "Croco"
    battlefield = Battlefields.MushroomWay
    music = music.MidbossMusic
    boss = Croco1Boss
    boss_locations = [
        BossModelFill(
            Rooms._076_BANDITS_WAY_AREA_01,
            5,
            Croco1Boss,
            SpriteSize.Small,
            False,
            target_scripts=[1714],
            sequence_setter=757,
        ),
        BossModelFill(
            Rooms._207_BANDITS_WAY_AREA_02,
            8,
            Croco1Boss,
            SpriteSize.Small,
            False,
            target_scripts=[1702],
            sequence_setter=756,
        ),
        BossModelFill(
            Rooms._077_BANDITS_WAY_AREA_03,
            8,
            Croco1Boss,
            SpriteSize.Small,
            False,
            target_scripts=[1713],
            target_action_scripts=[162],
            sequence_setter=758,
        ),
        BossModelFill(
            Rooms._078_BANDITS_WAY_AREA_04,
            12,
            Croco1Boss,
            SpriteSize.Small,
            False,
            target_scripts=[1698],
            sequence_setter=759,
        ),
        BossModelFill(
            Rooms._206_BANDITS_WAY_AREA_05,
            8,
            Croco1Boss,
            SpriteSize.Small,
            False,
            target_scripts=[1707, 1708, 1709, 1710],
            target_action_scripts=[469],
            sequence_setter=760,
        ),
        BossModelFill(
            Rooms._505_ENDING_CREDITS_YOSTER_ISLE_CROCO_RACING_YOSHI,
            10,
            Croco1Boss,
            SpriteSize.Small,
            False,
            target_scripts=[3806],
            target_action_scripts=[239],
            sequence_setter=1193,
        ),
    ]


class Mack(BossAndStarLocation):
    _identifier = 326
    _grant_identifier = 18
    description = AvailableBosses.Mack.value
    name = "Mack"
    battlefield = Battlefields.MushroomKingdomThroneRoom
    music = music.BossMusic
    statue_palette = [
        "F8E870",
        "D0A000",
        "F8E870",
        "906010",
        "906010",
        "D0A000",
        "C08020",
        "E0C000",
        "683808",
        "301830",
        "C08020",
        "301830",
        "906010",
        "482818",
        "181818",
    ]
    boss = MackBoss
    boss_locations = [
        BossModelFill(
            Rooms._326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM,
            3,
            MackBoss,
            SpriteSize.Large,
            False,
            target_scripts=[368, 373],
            target_action_scripts=[636],
            sequence_setter=761,
            prefer_south_only=True,
        ),
    ]
    unique_henchmen = [
        [
            UniqueHenchmanFill(
                Rooms._326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM,
                4,
                DefaultShyster1,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[368, 372, 373],
                target_action_scripts=[103, 102],
                sequence_setter=761,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM,
                5,
                DefaultShyster1,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[368, 372, 373],
                target_action_scripts=[103, 101],
                sequence_setter=761,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM,
                6,
                DefaultShyster1,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[368, 372, 373],
                target_action_scripts=[103, 102],
                sequence_setter=761,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM,
                7,
                DefaultShyster1,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[368, 372, 373],
                target_action_scripts=[103, 101],
                sequence_setter=761,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM,
                8,
                DefaultShyster1,
                True,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[368, 372, 373],
                target_action_scripts=[103, 102],
                sequence_setter=761,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM,
                9,
                DefaultShyster1,
                True,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[368, 372, 373],
                target_action_scripts=[103, 101],
                sequence_setter=761,
            ),
        ],
    ]
    repeatable_henchmen = [
        [
            RepeatableHenchmanFill(
                Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                3,
                DefaultShyster1,
                False,
                False,
                HenchmanType.PACK,
                target_scripts=[376],
                target_action_scripts=[132],
                sequence_setter=762,
            ),
            RepeatableHenchmanFill(
                Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                5,
                DefaultShyster1,
                False,
                False,
                HenchmanType.EVENT,
                1189,
                target_scripts=[376],
                target_action_scripts=[130, 107, 106, 105, 104],
                sequence_setter=762,
                battlefield=Battlefields.MushroomKingdomOutside,
            ),
            RepeatableHenchmanFill(
                Rooms._323_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_THRONE_ROOM,
                0,
                DefaultShyster1,
                False,
                False,
                HenchmanType.PACK,
                target_scripts=[764],
                target_action_scripts=[115, 107, 106, 105, 104],
                sequence_setter=763,
            ),
            RepeatableHenchmanFill(
                Rooms._325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
                0,
                DefaultShyster1,
                False,
                False,
                HenchmanType.EVENT,
                1186,
                target_scripts=[371, 377],
                target_action_scripts=[110],
                sequence_setter=765,
                battlefield=Battlefields.MushroomKingdomThroneRoom,
            ),
            RepeatableHenchmanFill(
                Rooms._325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
                1,
                DefaultShyster1,
                False,
                False,
                HenchmanType.EVENT,
                1187,
                target_scripts=[371, 377],
                target_action_scripts=[110],
                sequence_setter=765,
                battlefield=Battlefields.MushroomKingdomThroneRoom,
            ),
            RepeatableHenchmanFill(
                Rooms._325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
                2,
                DefaultShyster1,
                False,
                False,
                HenchmanType.EVENT,
                1188,
                target_scripts=[371, 377],
                target_action_scripts=[108],
                sequence_setter=765,
                battlefield=Battlefields.MushroomKingdomThroneRoom,
            ),
            RepeatableHenchmanFill(
                Rooms._325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
                3,
                DefaultShyster1,
                False,
                False,
                HenchmanType.PACK,
                target_scripts=[371, 377],
                target_action_scripts=[109],
                sequence_setter=765,
            ),
            RepeatableHenchmanFill(
                Rooms._325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
                4,
                DefaultShyster1,
                False,
                False,
                HenchmanType.EVENT,
                1189,
                target_scripts=[371, 377],
                target_action_scripts=[111],
                sequence_setter=765,
                battlefield=Battlefields.MushroomKingdomThroneRoom,
            ),
            RepeatableHenchmanFill(
                Rooms._327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM,
                0,
                DefaultShyster1,
                False,
                False,
                HenchmanType.PACK,
                target_scripts=[391],
                target_action_scripts=[125],
                sequence_setter=766,
            ),
            RepeatableHenchmanFill(
                Rooms._329_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_BRANCH_ROOM_TO_VAULTGUEST_ROOM,
                1,
                DefaultShyster1,
                False,
                False,
                HenchmanType.PACK,
                target_scripts=[767],
                target_action_scripts=[123],
                sequence_setter=768,
            ),
            RepeatableHenchmanFill(
                Rooms._480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F,
                4,
                DefaultShyster1,
                False,
                False,
                HenchmanType.EVENT,
                1187,
                target_scripts=[393, 407, 405],
                target_action_scripts=[103],
                sequence_setter=770,
                battlefield=Battlefields.House,
            ),
        ],
        [
            RepeatableHenchmanFill(
                Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                0,
                DefaultShyster2,
                False,
                False,
                HenchmanType.EVENT,
                1186,
                target_scripts=[376],
                target_action_scripts=[133],
                sequence_setter=762,
                battlefield=Battlefields.MushroomKingdomOutside,
            ),
            RepeatableHenchmanFill(
                Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                1,
                DefaultShyster2,
                False,
                False,
                HenchmanType.EVENT,
                1187,
                target_scripts=[376],
                target_action_scripts=[133],
                sequence_setter=762,
                battlefield=Battlefields.MushroomKingdomOutside,
            ),
            RepeatableHenchmanFill(
                Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                2,
                DefaultShyster2,
                False,
                False,
                HenchmanType.EVENT,
                1188,
                target_scripts=[376],
                target_action_scripts=[136],
                sequence_setter=762,
                battlefield=Battlefields.MushroomKingdomOutside,
            ),
            RepeatableHenchmanFill(
                Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                4,
                DefaultShyster2,
                False,
                False,
                HenchmanType.PACK,
                target_scripts=[376],
                target_action_scripts=[135],
                sequence_setter=762,
            ),
            RepeatableHenchmanFill(
                Rooms._190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                6,
                DefaultShyster2,
                False,
                False,
                HenchmanType.EVENT,
                1190,
                target_scripts=[376],
                target_action_scripts=[134, 107, 106, 105, 104],
                sequence_setter=762,
                battlefield=Battlefields.MushroomKingdomOutside,
            ),
            RepeatableHenchmanFill(
                Rooms._323_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_THRONE_ROOM,
                1,
                DefaultShyster2,
                False,
                False,
                HenchmanType.PACK,
                target_scripts=[764],
                target_action_scripts=[116, 107, 106, 105, 104],
                sequence_setter=763,
            ),
            RepeatableHenchmanFill(
                Rooms._327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM,
                1,
                DefaultShyster2,
                False,
                False,
                HenchmanType.EVENT,
                1186,
                target_scripts=[391],
                target_action_scripts=[124],
                sequence_setter=766,
                battlefield=Battlefields.MushroomKingdom,
            ),
            RepeatableHenchmanFill(
                Rooms._329_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_BRANCH_ROOM_TO_VAULTGUEST_ROOM,
                0,
                DefaultShyster2,
                False,
                False,
                HenchmanType.PACK,
                target_scripts=[767],
                target_action_scripts=[122],
                sequence_setter=768,
            ),
            RepeatableHenchmanFill(
                Rooms._332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM,
                0,
                DefaultShyster2,
                False,
                False,
                HenchmanType.EXTERNAL_EVENT,
                1186,
                target_scripts=[384, 381],
                target_action_scripts=[103],
                sequence_setter=769,
                battlefield=Battlefields.MushroomKingdom,
            ),
            RepeatableHenchmanFill(
                Rooms._332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM,
                1,
                DefaultShyster2,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[384, 381],
                target_action_scripts=[103],
                sequence_setter=769,
                battlefield=Battlefields.MushroomKingdom,
            ),
            RepeatableHenchmanFill(
                Rooms._480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F,
                3,
                DefaultShyster2,
                False,
                False,
                HenchmanType.EVENT,
                1186,
                target_scripts=[393, 407, 405],
                target_action_scripts=[103],
                sequence_setter=770,
                battlefield=Battlefields.House,
            ),
            RepeatableHenchmanFill(
                Rooms._481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F,
                1,
                DefaultShyster2,
                False,
                False,
                HenchmanType.EVENT,
                1186,
                target_scripts=[409, 410],
                target_action_scripts=[103],
                sequence_setter=771,
                battlefield=Battlefields.House,
            ),
        ],
    ]


class Pandorite(BossAndStarLocation):
    _identifier = 512
    description = AvailableBosses.Pandorite.value
    name = "Pandorite"
    battlefield = Battlefields.KeroSewers
    boss = PandoriteBoss


class Belome1(BossAndStarLocation):
    _identifier = 302
    _grant_identifier = 301
    battlefield = Battlefields.KeroSewers
    music = music.MidbossMusic
    description = AvailableBosses.Belome1.value
    name = "Belome"
    boss = Belome1Boss
    boss_locations = [
        BossModelFill(
            Rooms._302_KERO_SEWERS_AREA_08_BELOMES_ROOM,
            1,
            Belome1Boss,
            SpriteSize.Attack,
            False,
            target_scripts=[773, 3135],
            sequence_setter=772,
        ),
    ]


class Bowyer(BossAndStarLocation):
    _identifier = 232
    description = AvailableBosses.Bowyer.value
    name = "Bowyer"
    battlefield = Battlefields.BOWYER
    music = music.BossMusic
    boss = BowyerBoss
    boss_locations = [
        BossModelFill(
            Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD,
            11,
            BowyerBoss,
            SpriteSize.Large,
            False,
            target_scripts=[774, 2448],
            sequence_setter=775,
            prefer_uncloneable=True,
            prefer_south_only=True,
        ),
    ]
    unique_henchmen = [
        [
            UniqueHenchmanFill(
                Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD,
                1,
                BowyerAero,
                False,
                False,
                True,
                HenchmanType.NPC_ONLY,
                target_scripts=[774, 2448],
                target_action_scripts=[486, 487],
                sequence_setter=775,
                prefer_south_only=True,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD,
                7,
                BowyerAero,
                False,
                False,
                True,
                HenchmanType.NPC_ONLY,
                target_scripts=[774, 2448],
                target_action_scripts=[486, 487],
                sequence_setter=775,
                prefer_south_only=True,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD,
                3,
                BowyerAero,
                False,
                False,
                True,
                HenchmanType.NPC_ONLY,
                target_scripts=[774, 2448],
                target_action_scripts=[486, 487],
                sequence_setter=775,
                prefer_south_only=True,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD,
                9,
                BowyerAero,
                False,
                False,
                True,
                HenchmanType.NPC_ONLY,
                target_scripts=[774, 2448],
                target_action_scripts=[486, 487],
                sequence_setter=775,
                prefer_south_only=True,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD,
                4,
                BowyerAero,
                False,
                False,
                True,
                HenchmanType.NPC_ONLY,
                target_scripts=[774, 2448],
                target_action_scripts=[486, 487],
                sequence_setter=775,
                prefer_south_only=True,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD,
                5,
                BowyerAero,
                False,
                False,
                True,
                HenchmanType.NPC_ONLY,
                target_scripts=[774, 2448],
                target_action_scripts=[486, 487],
                sequence_setter=775,
                prefer_south_only=True,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD,
                2,
                BowyerAero,
                False,
                False,
                True,
                HenchmanType.NPC_ONLY,
                target_scripts=[774, 2448],
                target_action_scripts=[486, 487],
                sequence_setter=775,
                prefer_south_only=True,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD,
                8,
                BowyerAero,
                False,
                False,
                True,
                HenchmanType.NPC_ONLY,
                target_scripts=[774, 2448],
                target_action_scripts=[486, 487],
                sequence_setter=775,
                prefer_south_only=True,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD,
                0,
                BowyerAero,
                False,
                False,
                True,
                HenchmanType.NPC_ONLY,
                target_scripts=[774, 2448],
                target_action_scripts=[486, 487],
                sequence_setter=775,
                prefer_south_only=True,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._232_FOREST_MAZE_BOWYERS_PRACTICE_PAD,
                6,
                BowyerAero,
                False,
                False,
                True,
                HenchmanType.NPC_ONLY,
                target_scripts=[774, 2448],
                target_action_scripts=[486, 487],
                sequence_setter=775,
                prefer_south_only=True,
            ),
        ],
    ]


class Croco2(BossAndStarLocation):
    _identifier = 518
    description = AvailableBosses.Croco2.value
    name = "Croco"
    battlefield = Battlefields.MOLEVILLE_MINES
    music = music.MidbossMusic
    boss = Croco2Boss
    boss_locations = [
        BossModelFill(
            Rooms._273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE,
            0,
            Croco2Boss,
            SpriteSize.Small,
            False,
            target_scripts=[776],
            target_action_scripts=[730],
            sequence_setter=777,
        ),
        BossModelFill(
            Rooms._277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM,
            0,
            Croco2Boss,
            SpriteSize.Small,
            False,
            target_scripts=[778],
            target_action_scripts=[735],
            sequence_setter=779,
        ),
        BossModelFill(
            Rooms._275_MOLEVILLE_MINES_AREA_06_SMALL_ROOM_LEADING_TO_AREA_06,
            0,
            Croco2Boss,
            SpriteSize.Small,
            False,
            target_scripts=[780],
            target_action_scripts=[734],
            sequence_setter=781,
        ),
        BossModelFill(
            Rooms._281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM,
            0,
            Croco2Boss,
            SpriteSize.Small,
            False,
            target_scripts=[782],
            target_action_scripts=[733],
            sequence_setter=783,
        ),
        BossModelFill(
            Rooms._279_MOLEVILLE_MINES_AREA_08_CROCOS_BOMBED_ROOM,
            0,
            Croco2Boss,
            SpriteSize.Small,
            False,
            target_scripts=[784],
            target_action_scripts=[732],
            sequence_setter=785,
        ),
        BossModelFill(
            Rooms._283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM,
            0,
            Croco2Boss,
            SpriteSize.Small,
            False,
            target_scripts=[786],
            target_action_scripts=[731],
            sequence_setter=787,
        ),
    ]
    unique_henchmen = [
        [
            UniqueHenchmanFill(
                Rooms._273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE,
                1,
                DefaultCrook,
                False,
                True,
                False,
                HenchmanType.EVENT,
                1186,
                target_scripts=[776],
                target_action_scripts=[619],
                sequence_setter=777,
                battlefield=Battlefields.MOLEVILLE_MINES,
                can_run_away=True,
            )
        ],
        [
            UniqueHenchmanFill(
                Rooms._277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM,
                1,
                DefaultCrook,
                False,
                True,
                False,
                HenchmanType.EVENT,
                1186,
                target_scripts=[778],
                target_action_scripts=[617],
                sequence_setter=779,
                battlefield=Battlefields.MOLEVILLE_MINES,
                can_run_away=True,
            )
        ],
        [
            UniqueHenchmanFill(
                Rooms._283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM,
                1,
                DefaultCrook,
                False,
                True,
                False,
                HenchmanType.EVENT,
                1186,
                target_scripts=[786],
                target_action_scripts=[618],
                sequence_setter=787,
                battlefield=Battlefields.MOLEVILLE_MINES,
                can_run_away=True,
            )
        ],
    ]


class Punchinello(BossAndStarLocation):
    _identifier = 271
    description = AvailableBosses.Punchinello.value
    name = "Punchinello"
    battlefield = Battlefields.MOLEVILLE_MINES
    music = music.MidbossMusic
    boss = PunchinelloBoss
    boss_locations = [
        BossModelFill(
            Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
            0,
            PunchinelloBoss,
            SpriteSize.Attack,
            False,
            target_scripts=[592, 596, 594, 860],
            sequence_setter=788,
        ),
    ]
    # should the bobombs be unique henchmen?
    repeatable_henchmen = [
        [  # needs special considerations for only tiny sprites
            RepeatableHenchmanFill(
                Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
                1,
                DefaultMicrobomb,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[592, 596],
                target_action_scripts=[299, 302],
                sequence_setter=788,
            ),
            RepeatableHenchmanFill(
                Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
                2,
                DefaultMicrobomb,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[592, 596],
                target_action_scripts=[299, 302],
                sequence_setter=788,
            ),
            RepeatableHenchmanFill(
                Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
                3,
                DefaultMicrobomb,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[592, 596],
                target_action_scripts=[299, 302],
                sequence_setter=788,
            ),
        ],
        [  # check and see if cloning causes vram issues
            RepeatableHenchmanFill(
                Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
                4,
                DefaultBobomb,
                False,
                False,
                HenchmanType.PACK,
                target_scripts=[592, 596],
                target_action_scripts=[290, 293],
                sequence_setter=788,
                can_run_away=True,
            ),
            RepeatableHenchmanFill(
                Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
                5,
                DefaultBobomb,
                False,
                False,
                HenchmanType.PACK,
                target_scripts=[592, 596],
                target_action_scripts=[292, 293],
                sequence_setter=788,
                can_run_away=True,
            ),
            RepeatableHenchmanFill(
                Rooms._289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
                6,
                DefaultBobomb,
                False,
                False,
                HenchmanType.PACK,
                target_scripts=[592, 596],
                target_action_scripts=[291, 293],
                sequence_setter=788,
                can_run_away=True,
            ),
        ],
        [  # booster tower masher room because lol
            RepeatableHenchmanFill(
                197,
                1,
                DefaultBobomb,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[2340, 2342],
                target_action_scripts=[],
                sequence_setter=881,
            )
        ],
    ]


class Booster(BossAndStarLocation):
    _identifier = 192
    description = AvailableBosses.Booster.value
    name = "Booster"
    battlefield = Battlefields.BoosterTower
    music = music.MidbossMusic
    boss = BoosterBoss
    boss_locations = [
        BossModelFill(
            Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
            0,
            BoosterBoss,
            SpriteSize.Small,
            False,
            target_scripts=[1359, 1358, 1364, 1365, 1366, 1367, 1368, 1369, 1370],
            sequence_setter=789,
        ),
        BossModelFill(
            Rooms._154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            7,
            BoosterBoss,
            SpriteSize.Small,
            False,
            dialogs=[2504],
            target_scripts=[3809, 3930],
            sequence_setter=790,
        ),
        BossModelFill(
            Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            6,
            BoosterBoss,
            SpriteSize.Small,
            False,
            target_scripts=[1339, 1335],
            target_action_scripts=[],
            sequence_setter=791,
        ),
        BossModelFill(
            Rooms._193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS,
            6,
            BoosterBoss,
            SpriteSize.Small,
            False,
            target_action_scripts=[702],
            sequence_setter=792,
        ),
        BossModelFill(
            Rooms._054_BOOSTER_HILL_____DUMMY,
            7,
            BoosterBoss,
            SpriteSize.Small,
            False,
            target_scripts=[3499, 3502, 3500, 3503, 3506],
            target_action_scripts=[717, 718],
            sequence_setter=200,
        ),
        BossModelFill(
            Rooms._202_BOOSTER_TOWER_ENTRANCE,
            1,
            BoosterBoss,
            SpriteSize.Small,
            False,
            target_scripts=[1328],
            target_action_scripts=[519],
            sequence_setter=878,
        ),
        BossModelFill(
            Rooms._043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM,
            3,
            BoosterBoss,
            SpriteSize.Small,
            False,
            target_scripts=[1312],
            target_action_scripts=[518],
            sequence_setter=797,
        ),
        BossModelFill(
            Rooms._258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
            3,
            BoosterBoss,
            SpriteSize.Small,
            False,
            target_scripts=[1282, 2278],
            target_action_scripts=[],
            sequence_setter=794,
        ),
        BossModelFill(
            Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            10,
            BoosterBoss,
            SpriteSize.Small,
            False,
            target_scripts=[2295],
            target_action_scripts=[],
            sequence_setter=795,
        ),
    ]
    unique_henchmen = [
        [
            UniqueHenchmanFill(
                Rooms._043_BOOSTER_TOWER_1F_AREA_01_MAIN_ROOM,
                4,
                DefaultSnifit,
                False,
                True,
                False,
                HenchmanType.EVENT,
                1186,
                dialogs=[2560],
                target_scripts=[1312],
                target_action_scripts=[],
                sequence_setter=797,
                battlefield=Battlefields.BoosterTower,
            ),
            UniqueHenchmanFill(
                Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
                1,
                DefaultSnifit,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[1359, 1358, 1364, 1365, 1366, 1367, 1368, 1369, 1370],
                target_action_scripts=[576, 577, 579],
                sequence_setter=789,
            ),
            UniqueHenchmanFill(
                Rooms._154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
                0,
                DefaultSnifit,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[3809, 600, 3930],
                target_action_scripts=[376, 372],
                sequence_setter=790,
            ),
            UniqueHenchmanFill(
                Rooms._054_BOOSTER_HILL_____DUMMY,
                3,
                BoosterHillSnifit,
                True,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[3499, 3502, 3500, 3503],
                target_action_scripts=[707, 712, 711],
                sequence_setter=200,
            ),
            UniqueHenchmanFill(
                Rooms._258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
                0,
                DefaultSnifit,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[1282, 2278],
                target_action_scripts=[],
                sequence_setter=794,
            ),
            UniqueHenchmanFill(
                Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
                2,
                DefaultSnifit,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[2295],
                target_action_scripts=[],
                sequence_setter=795,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._194_BOOSTER_TOWER_2F_AREA_02_BOOSTERS_RAILWAY_ROOM,
                0,
                DefaultSnifit,
                False,
                True,
                False,
                HenchmanType.EXTERNAL_EVENT,
                1186,
                dialogs=[2572],
                target_scripts=[1344, 1346],
                target_action_scripts=[],
                sequence_setter=798,
                battlefield=Battlefields.BoosterTower,
            ),
            UniqueHenchmanFill(
                Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
                2,
                DefaultSnifit,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[1359, 1358, 1364, 1365, 1366, 1367, 1368, 1369, 1370],
                target_action_scripts=[576, 577, 580],
                sequence_setter=789,
                battlefield=Battlefields.BoosterTower,
            ),
            UniqueHenchmanFill(
                Rooms._154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
                1,
                DefaultSnifit,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[3809, 600, 3930],
                target_action_scripts=[373],
                sequence_setter=790,
            ),
            UniqueHenchmanFill(
                Rooms._054_BOOSTER_HILL_____DUMMY,
                4,
                BoosterHillSnifit,
                True,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[3499, 3502, 3500, 3503],
                target_action_scripts=[707, 712, 711],
                sequence_setter=200,
            ),
            UniqueHenchmanFill(
                Rooms._258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
                1,
                DefaultSnifit,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[1282, 2278],
                target_action_scripts=[],
                sequence_setter=794,
            ),
            UniqueHenchmanFill(
                Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
                1,
                DefaultSnifit,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[2295],
                target_action_scripts=[],
                sequence_setter=795,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._037_BOOSTER_TOWER_4F_3LEVEL_ROOM_WJUMPING_SPOOKUMS,
                8,
                DefaultSnifit,
                False,
                True,
                False,
                HenchmanType.EVENT,
                1186,
                dialogs=[3072, 3073],
                target_scripts=[2348, 2352, 2351],
                target_action_scripts=[386],
                sequence_setter=799,
                battlefield=Battlefields.BoosterTower,
            ),
            UniqueHenchmanFill(
                Rooms._192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
                3,
                DefaultSnifit,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[1359, 1358, 1364, 1365, 1366, 1367, 1368, 1369, 1370],
                target_action_scripts=[576, 577, 578],
                sequence_setter=789,
            ),
            UniqueHenchmanFill(
                Rooms._154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
                2,
                DefaultSnifit,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[3809, 600, 3930],
                target_action_scripts=[376, 374],
                sequence_setter=790,
            ),
            UniqueHenchmanFill(
                Rooms._054_BOOSTER_HILL_____DUMMY,
                5,
                BoosterHillSnifit,
                True,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[3499, 3502, 3500, 3503],
                target_action_scripts=[707, 712, 711],
                sequence_setter=200,
            ),
            UniqueHenchmanFill(
                Rooms._258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
                2,
                DefaultSnifit,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[1282, 2278],
                target_action_scripts=[],
                sequence_setter=794,
            ),
            UniqueHenchmanFill(
                Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
                3,
                DefaultSnifit,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[2295],
                target_action_scripts=[],
                sequence_setter=795,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
                4,
                DefaultSnifit,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[2295],
                target_action_scripts=[],
                sequence_setter=795,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
                5,
                DefaultSnifit,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[2295],
                target_action_scripts=[],
                sequence_setter=795,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
                6,
                DefaultSnifit,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[2295],
                target_action_scripts=[],
                sequence_setter=795,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
                7,
                DefaultSnifit,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[2295],
                target_action_scripts=[],
                sequence_setter=795,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
                8,
                DefaultSnifit,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[2295],
                target_action_scripts=[],
                sequence_setter=795,
            ),
        ],
    ]
    repeatable_henchmen = [
        [
            RepeatableHenchmanFill(
                Rooms._405_BOOSTER_PASS_SECRET,
                9,
                BoosterApprentice,
                False,
                False,
                HenchmanType.EXTERNAL_EVENT,
                1186,
                target_scripts=[2586],
                target_action_scripts=[851],
                sequence_setter=880,
                battlefield=Battlefields.Mountains,
            ),
        ],
    ]


class ClownBros(BossAndStarLocation):
    _identifier = 258
    _grant_identifier = 202
    battlefield = Battlefields.ClownBros
    music = music.MidbossMusic
    description = AvailableBosses.KnifeGuyGrateGuy.value
    name = "Grate Guy"
    boss = GrateGuyBoss


class Bundt(BossAndStarLocation):
    _identifier = 154
    battlefield = Battlefields.Bundt
    music = music.MidbossMusic
    description = AvailableBosses.Bundt.value
    name = "Bundt"
    boss = BundtBoss
    boss_locations = [
        BossModelFill(
            Rooms._155_MARRYMORE_CHAPEL_KITCHEN,
            0,
            BundtBoss,
            SpriteSize.Small,
            False,
            target_scripts=[628],
            target_action_scripts=[],
            sequence_setter=796,
            prefer_south_only=True,
            prefer_uncloneable=True,
        ),
        BossModelFill(
            Rooms._154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
            11,
            BundtBoss,
            SpriteSize.Small,
            False,
            target_scripts=[668],
            target_action_scripts=[],
            sequence_setter=790,
        ),
    ]
    unique_henchmen = [
        [
            UniqueHenchmanFill(
                Rooms._155_MARRYMORE_CHAPEL_KITCHEN,
                1,
                BundtTorte1,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                dialogs=[2061],
                target_scripts=[628],
                target_action_scripts=[330],
                sequence_setter=796,
                prefer_uncloneable=True,
            ),
            UniqueHenchmanFill(
                Rooms._154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
                9,
                BundtTorte1,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[668],
                target_action_scripts=[636],
                sequence_setter=790,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._155_MARRYMORE_CHAPEL_KITCHEN,
                2,
                BundtTorte2,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                dialogs=[2062],
                target_scripts=[628],
                target_action_scripts=[331],
                sequence_setter=796,
                prefer_uncloneable=True,
            ),
            UniqueHenchmanFill(
                Rooms._154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
                10,
                BundtTorte2,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[668],
                target_action_scripts=[636],
                sequence_setter=790,
            ),
        ],
    ]


class KingCalamari(BossAndStarLocation):
    _identifier = 177
    _grant_identifier = 173
    battlefield = Battlefields.SunkenShip
    music = music.MidbossMusic
    description = AvailableBosses.KingCalamari.value
    name = "King Calamari"
    boss = KingCalamariBoss
    boss_locations = [
        BossModelFill(
            Rooms._177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM,
            7,
            KingCalamariTentacle,
            SpriteSize.Small,
            False,
            dialogs=[1660],
            target_scripts=[3224, 3218],
            target_action_scripts=[203],
            sequence_setter=800,
        ),
    ]


class Hidon(BossAndStarLocation):
    _identifier = 513
    battlefield = Battlefields.SunkenShip
    description = AvailableBosses.Hidon.value
    name = "Hidon"
    boss = HidonBoss


class Johnny(BossAndStarLocation):
    _identifier = 28
    battlefield = Battlefields.SunkenShip
    music = music.MidbossMusic
    description = AvailableBosses.Johnny.value
    name = "Johnny"
    boss = JohnnyBoss
    boss_locations = [
        BossModelFill(
            Rooms._028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM,
            0,
            JohnnyBoss,
            SpriteSize.Small,
            False,
            dialogs=[1778, 1780, 1781, 1783],
            target_scripts=[3282],
            target_action_scripts=[348],
            sequence_setter=801,
        ),
        BossModelFill(
            Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            8,
            JohnnyBoss,
            SpriteSize.Small,
            False,
            dialogs=[1787],
            target_scripts=[1146, 1147],
            target_action_scripts=[],
            sequence_setter=802,
        ),
        BossModelFill(
            Rooms._432_ENDING_CREDITS_JOHNNY_LOOKING_OUT_AT_SUNSET_ON_BEACH_SHORE,
            0,
            JohnnyBoss,
            SpriteSize.Small,
            False,
            target_scripts=[2619],
            target_action_scripts=[],
            sequence_setter=1191,
        ),
    ]
    unique_henchmen = [
        [
            UniqueHenchmanFill(
                Rooms._028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM,
                1,
                JohnnyBandanaBlue,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                dialogs=[1784],
                target_scripts=[3282],
                target_action_scripts=[],
                sequence_setter=801,
            ),
            UniqueHenchmanFill(
                Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
                4,
                JohnnyBandanaBlue,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[1146, 1147],
                target_action_scripts=[],
                sequence_setter=802,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM,
                2,
                JohnnyBandanaBlue,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                dialogs=[1785],
                target_scripts=[3282],
                target_action_scripts=[],
                sequence_setter=801,
            ),
            UniqueHenchmanFill(
                Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
                5,
                JohnnyBandanaBlue,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[1146, 1147],
                target_action_scripts=[],
                sequence_setter=802,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM,
                3,
                JohnnyBandanaBlue,
                False,
                False,
                True,
                HenchmanType.NPC_ONLY,
                dialogs=[1792],
                target_scripts=[3282],
                target_action_scripts=[],
                sequence_setter=801,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM,
                4,
                JohnnyBandanaBlue,
                False,
                False,
                True,
                HenchmanType.NPC_ONLY,
                dialogs=[1793],
                target_scripts=[3282],
                target_action_scripts=[],
                sequence_setter=801,
            ),
        ],
    ]
    repeatable_henchmen = [
        [
            RepeatableHenchmanFill(
                Rooms._024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL,
                0,
                DefaultBandanaRed1,
                True,
                False,
                HenchmanType.EXTERNAL_EVENT,
                1186,
                target_scripts=[3280],
                target_action_scripts=[],
                sequence_setter=803,
                battlefield=Battlefields.SunkenShip,
            ),
            RepeatableHenchmanFill(
                Rooms._024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL,
                1,
                DefaultBandanaRed1,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[3280],
                target_action_scripts=[],
                sequence_setter=803,
            ),
            RepeatableHenchmanFill(
                Rooms._024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL,
                2,
                DefaultBandanaRed1,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[3280],
                target_action_scripts=[],
                sequence_setter=803,
            ),
            RepeatableHenchmanFill(
                Rooms._024_SUNKEN_SHIP_POSTKC_AREA_15_BANDANA_RED_ROOM_WLONG_STAIRWELL,
                3,
                DefaultBandanaRed1,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[3280],
                target_action_scripts=[],
                sequence_setter=803,
            ),
        ],
        [
            RepeatableHenchmanFill(
                Rooms._025_SUNKEN_SHIP_POSTKC_AREA_16_ENTRANCE_TO_JOHNNYS_ROOM,
                0,
                DefaultBandanaRed2,
                True,
                False,
                HenchmanType.EXTERNAL_EVENT,
                1186,
                dialogs=[1694, 1695],
                target_scripts=[3281],
                target_action_scripts=[],
                sequence_setter=804,
                battlefield=Battlefields.SunkenShip,
            ),
            RepeatableHenchmanFill(
                Rooms._025_SUNKEN_SHIP_POSTKC_AREA_16_ENTRANCE_TO_JOHNNYS_ROOM,
                1,
                DefaultBandanaRed2,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[3281],
                target_action_scripts=[],
                sequence_setter=804,
            ),
        ],
    ]


class Yaridovich(BossAndStarLocation):
    _identifier = 315
    _grant_identifier = 316
    description = AvailableBosses.Yaridovich.value
    name = "Yaridovich"
    battlefield = Battlefields.Yaridovich
    music = music.BossMusic
    boss = YaridovichBoss
    boss_locations = [
        BossModelFill(
            Rooms._211_SEASIDE_TOWN_DURING_YARIDOVICH_ELDERS_HOUSE_1F,
            0,
            YaridovichBoss,
            SpriteSize.Small,
            False,
            dialogs=[2831],
            target_scripts=[],
            target_action_scripts=[],
            sequence_setter=805,
        ),
        BossModelFill(
            Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
            4,
            YaridovichBoss,
            SpriteSize.Small,
            False,
            target_scripts=[1119],
            target_action_scripts=[],
            sequence_setter=806,
        ),
        BossModelFill(
            Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            6,
            YaridovichBoss,
            SpriteSize.Small,
            False,
            target_scripts=[1146, 1147],
            target_action_scripts=[527],
            sequence_setter=802,
        ),
        BossModelFill(
            Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
            7,
            YaridovichBoss,
            SpriteSize.Large,
            False,
            target_scripts=[1146, 1147],
            target_action_scripts=[527],
            sequence_setter=802,
        ),
    ]
    unique_henchmen = [
        [
            UniqueHenchmanFill(
                Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
                0,
                YaridovichHenchman,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                dialogs=[2847],
                target_scripts=[1119],
                target_action_scripts=[],
                sequence_setter=806,
            ),
            UniqueHenchmanFill(
                Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
                0,
                YaridovichHenchman,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[1146, 1147],
                target_action_scripts=[],
                sequence_setter=802,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
                1,
                YaridovichHenchman,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                dialogs=[2848],
                target_scripts=[1119],
                target_action_scripts=[],
                sequence_setter=806,
            ),
            UniqueHenchmanFill(
                Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
                1,
                YaridovichHenchman,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[1146, 1147],
                target_action_scripts=[],
                sequence_setter=802,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
                2,
                YaridovichHenchman,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[1119],
                target_action_scripts=[],
                sequence_setter=806,
            ),
            UniqueHenchmanFill(
                Rooms._209_SEASIDE_TOWN_DURING_YARIDOVICH_INN_1F,
                0,
                YaridovichHenchman,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                dialogs=[2832],
                target_scripts=[1121],
                target_action_scripts=[],
                sequence_setter=807,
            ),
            UniqueHenchmanFill(
                Rooms._210_SEASIDE_TOWN_DURING_YARIDOVICH_INN_2F,
                0,
                YaridovichHenchman,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[1122],
                target_action_scripts=[],
                sequence_setter=808,
            ),
            UniqueHenchmanFill(
                Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
                2,
                YaridovichHenchman,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[1146, 1147],
                target_action_scripts=[],
                sequence_setter=802,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
                3,
                YaridovichHenchman,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[1119],
                target_action_scripts=[],
                sequence_setter=806,
            ),
            UniqueHenchmanFill(
                Rooms._213_SEASIDE_TOWN_DURING_YARIDOVICH_BEETLES_ARE_USBOMB_SHOP,
                0,
                YaridovichHenchman,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[1125],
                target_action_scripts=[585],
                sequence_setter=809,
            ),
            UniqueHenchmanFill(
                Rooms._315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
                3,
                YaridovichHenchman,
                False,
                True,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[1146, 1147],
                target_action_scripts=[],
                sequence_setter=802,
            ),
        ],
    ]
    repeatable_henchmen = [
        [
            RepeatableHenchmanFill(
                Rooms._213_SEASIDE_TOWN_DURING_YARIDOVICH_BEETLES_ARE_USBOMB_SHOP,
                1,
                YaridovichHenchman,
                False,
                False,
                HenchmanType.NPC_ONLY,
                dialogs=[2845],
                target_scripts=[1125],
                target_action_scripts=[586],
                sequence_setter=809,
            ),
        ],
        [
            RepeatableHenchmanFill(
                Rooms._214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP,
                0,
                YaridovichHenchman,
                False,
                False,
                HenchmanType.NPC_ONLY,
                dialogs=[2841, 2842],
                target_scripts=[1126, 1138, 1139],
                target_action_scripts=[],
                sequence_setter=810,
            ),
        ],
        [
            RepeatableHenchmanFill(
                Rooms._214_SEASIDE_TOWN_DURING_YARIDOVICH_WEAPONS_AND_ARMOR_SHOP,
                1,
                YaridovichHenchman,
                False,
                False,
                HenchmanType.NPC_ONLY,
                dialogs=[2843, 2844],
                target_scripts=[1126, 1138, 1139],
                target_action_scripts=[],
                sequence_setter=810,
            ),
        ],
        [
            RepeatableHenchmanFill(
                Rooms._215_SEASIDE_TOWN_DURING_YARIDOVICH_HEALTH_FOOD_STORE_LEFTMOST,
                0,
                YaridovichHenchman,
                False,
                False,
                HenchmanType.NPC_ONLY,
                dialogs=[2839],
                target_scripts=[1127],
                target_action_scripts=[],
                sequence_setter=811,
            ),
        ],
        [
            RepeatableHenchmanFill(
                Rooms._216_SEASIDE_TOWN_DURING_YARIDOVICH_MUSHROOM_BOY_SHOP_MIDDLE,
                0,
                YaridovichHenchman,
                False,
                False,
                HenchmanType.NPC_ONLY,
                dialogs=[2837],
                target_scripts=[1128],
                target_action_scripts=[],
                sequence_setter=812,
            ),
        ],
        [
            RepeatableHenchmanFill(
                Rooms._216_SEASIDE_TOWN_DURING_YARIDOVICH_MUSHROOM_BOY_SHOP_MIDDLE,
                1,
                YaridovichHenchman,
                False,
                False,
                HenchmanType.NPC_ONLY,
                dialogs=[2838],
                target_scripts=[1128],
                target_action_scripts=[],
                sequence_setter=812,
            ),
        ],
        [
            RepeatableHenchmanFill(
                Rooms._217_SEASIDE_TOWN_DURING_YARIDOVICH_ACCESSORY_SHOP_RIGHTMOST,
                0,
                YaridovichHenchman,
                False,
                False,
                HenchmanType.NPC_ONLY,
                dialogs=[2834],
                target_scripts=[1129],
                target_action_scripts=[],
                sequence_setter=813,
            ),
        ],
    ]


class Mokura(BossAndStarLocation):
    _identifier = 519
    music = music.MidbossMusic
    description = AvailableBosses.Mokura.value
    name = "Mokura"
    boss = MokuraBoss


class Belome2(BossAndStarLocation):
    _identifier = 268
    description = AvailableBosses.Belome2.value
    name = "Belome"
    battlefield = Battlefields.BelomeTemple
    music = music.MidbossMusic
    boss = Belome2Boss
    boss_locations = [
        BossModelFill(
            Rooms._268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM,
            4,
            Belome2Boss,
            SpriteSize.Large,
            False,
            target_scripts=[1771],
            target_action_scripts=[],
            sequence_setter=814,
        ),
    ]


class Jagger(BossAndStarLocation):
    _identifier = 255
    description = AvailableBosses.Jagger.value
    name = "Jagger"
    battlefield = Battlefields.JinxDojo
    can_run_away = True
    boss = JaggerBoss
    boss_locations = [
        BossModelFill(
            Rooms._255_MONSTRO_TOWN_JINXS_DOJO,
            1,
            JaggerBoss,
            SpriteSize.Small,
            False,
            dialogs=[3044, 3352],
            target_scripts=[861, 2064, 2066, 2067, 2077],
            target_action_scripts=[1006],
            sequence_setter=815,
        ),
    ]


class Jinx1(BossAndStarLocation):
    _identifier = 515
    description = AvailableBosses.Jinx1.value
    name = "Jinx"
    battlefield = Battlefields.JinxDojo
    can_run_away = True
    music = music.MidbossMusic
    boss = Jinx1Boss
    boss_locations = [
        BossModelFill(
            Rooms._255_MONSTRO_TOWN_JINXS_DOJO,
            0,
            Jinx1Boss,
            SpriteSize.Small,
            False,
            target_scripts=[862, 2064, 2066, 2067, 2068],
            target_action_scripts=[],
            sequence_setter=815,
        ),
    ]


class Jinx2(BossAndStarLocation):
    _identifier = 516
    description = AvailableBosses.Jinx2.value
    name = "Jinx"
    battlefield = Battlefields.JinxDojo
    can_run_away = True
    music = music.MidbossMusic
    boss = Jinx2Boss
    boss_locations = [
        BossModelFill(
            Rooms._255_MONSTRO_TOWN_JINXS_DOJO,
            2,
            Jinx2Boss,
            SpriteSize.Small,
            False,
            target_scripts=[863, 864, 2064, 2068, 2076],
            target_action_scripts=[],
            sequence_setter=815,
        ),
    ]


class Jinx3(BossAndStarLocation):
    _identifier = 517
    description = AvailableBosses.Jinx3.value
    name = "Jinx"
    battlefield = Battlefields.JinxDojo
    can_run_away = True
    music = music.MidbossMusic
    boss = Jinx3Boss
    boss_locations = [
        BossModelFill(
            Rooms._255_MONSTRO_TOWN_JINXS_DOJO,
            3,
            Jinx3Boss,
            SpriteSize.Small,
            False,
            dialogs=[3353],
            target_scripts=[865, 866, 2064, 2076, 2077],
            target_action_scripts=[1006],
            sequence_setter=815,
        ),
    ]


class Culex(BossAndStarLocation):
    _identifier = 351
    _grant_identifier = 324
    description = AvailableBosses.Culex.value
    name = "Culex"
    battlefield = Battlefields.Culex
    music = music.CulexMusic
    boss = CulexBoss
    boss_locations = [
        BossModelFill(
            Rooms._351_CULEXS_ROOM,
            0,
            CulexBoss,
            SpriteSize.Small,
            False,
            dialogs=[3338, 3057],
            target_scripts=[2074],
            target_action_scripts=[],
            sequence_setter=816,
        ),
    ]


class BoxBoy(BossAndStarLocation):
    _identifier = 514
    battlefield = Battlefields.KeroSewers
    description = AvailableBosses.BoxBoy.value
    name = "Box Boy"
    boss = BoxBoyBoss


class MegaSmilax(BossAndStarLocation):
    _identifier = 254
    description = AvailableBosses.Megasmilax.value
    name = "Megasmilax"
    battlefield = Battlefields.BeanValley
    music = music.MidbossMusic
    boss = MegaSmilaxBoss
    boss_locations = [
        BossModelFill(
            Rooms._254_BEAN_VALLEY_SMILAX_AREA,
            1,
            MegaSmilaxBoss,
            SpriteSize.Small,
            False,
            target_scripts=[2555, 2557],
            target_action_scripts=[845],
            sequence_setter=817,
        ),  # despawn NPC 0 and move NPC 1 down one Z coordinate
    ]


class Dodo(BossAndStarLocation):
    _identifier = 520
    description = AvailableBosses.Dodo.value
    name = "Dodo"
    battlefield = Battlefields.NimbusCastle
    music = music.MidbossMusic
    boss = DodoBoss
    boss_locations = [
        BossModelFill(
            Rooms._112_NIMBUS_CASTLE_AREA_17_RIGHT_OF_4WAY_PATH_SAVE_POINT,
            1,
            DodoBoss,
            SpriteSize.Large,
            False,
            target_scripts=[2108],
            target_action_scripts=[],
            sequence_setter=818,
        ),
        BossModelFill(
            Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            0,
            DodoBoss,
            SpriteSize.Large,
            False,
            target_scripts=[2295],
            target_action_scripts=[],
            sequence_setter=795,
        ),
        BossModelFill(
            Rooms._110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM,
            3,
            DodoBoss,
            SpriteSize.Attack,
            True,
            target_scripts=[3640, 936, 937, 938, 939, 940],
            target_action_scripts=[],
            sequence_setter=819,
        ),
        BossModelFill(
            Rooms._437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD,
            0,
            DodoBoss,
            SpriteSize.Large,
            False,
            target_scripts=[3736],
            target_action_scripts=[],
            sequence_setter=820,
        ),
    ]


class Birdetta(BossAndStarLocation):
    _identifier = 409
    description = AvailableBosses.Birdetta.value
    name = "Birdetta"
    battlefield = Battlefields.Birdo
    music = music.MidbossMusic
    dialogs_to_replace = [49]
    boss = BirdettaBoss


class Valentina(BossAndStarLocation):
    _identifier = 430
    _grant_identifier = 438
    description = AvailableBosses.Valentina.value
    name = "Valentina"
    battlefield = Battlefields.Valentina
    music = music.MidbossMusic
    boss = ValentinaBoss
    boss_locations = [
        BossModelFill(
            Rooms._430_NIMBUS_LAND_OUTSIDE_DURING_VALENTINA,
            9,
            ValentinaBoss,
            SpriteSize.Small,
            False,
            target_scripts=[738],
            target_action_scripts=[],
            sequence_setter=822,
        ),
        BossModelFill(
            Rooms._258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
            4,
            ValentinaBoss,
            SpriteSize.Small,
            False,
            target_scripts=[1282, 2278],
            target_action_scripts=[],
            sequence_setter=794,
        ),
        BossModelFill(
            Rooms._506_ENDING_CREDITS_MARRYMORE_CHAPEL_BOOSTER_WEDDING_VALENTINA,
            9,
            ValentinaBoss,
            SpriteSize.Small,
            False,
            target_scripts=[2295],
            target_action_scripts=[],
            sequence_setter=795,
        ),
    ]
    statue_locations = [
        StatueFill(Rooms._341_NIMBUS_LAND_GARROS_HOUSE, 1, sequence_setter=821),
        StatueFill(Rooms._341_NIMBUS_LAND_GARROS_HOUSE, 2, sequence_setter=821),
        StatueFill(Rooms._341_NIMBUS_LAND_GARROS_HOUSE, 3, sequence_setter=821),
        StatueFill(
            Rooms._109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL, 0, sequence_setter=823
        ),
        StatueFill(
            Rooms._109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL, 1, sequence_setter=823
        ),
        StatueFill(
            Rooms._109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL, 2, sequence_setter=823
        ),
        StatueFill(
            Rooms._109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL, 3, sequence_setter=823
        ),
        StatueFill(
            Rooms._109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL, 4, sequence_setter=823
        ),
        StatueFill(
            Rooms._109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL, 5, sequence_setter=823
        ),
        StatueFill(
            Rooms._115_NIMBUS_CASTLE_AREA_03_4WAY_PATH_DURING_VALENTINA,
            0,
            sequence_setter=824,
        ),
        StatueFill(
            Rooms._115_NIMBUS_CASTLE_AREA_03_4WAY_PATH_DURING_VALENTINA,
            1,
            sequence_setter=824,
        ),
        StatueFill(
            Rooms._122_NIMBUS_CASTLE_AREA_12_ENTRANCE_TO_THRONE_ROOM,
            0,
            sequence_setter=825,
        ),
        StatueFill(
            Rooms._122_NIMBUS_CASTLE_AREA_12_ENTRANCE_TO_THRONE_ROOM,
            1,
            sequence_setter=825,
        ),
        StatueFill(
            Rooms._120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA,
            0,
            sequence_setter=826,
        ),
        StatueFill(
            Rooms._120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA,
            1,
            sequence_setter=826,
        ),
        StatueFill(
            Rooms._110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM,
            0,
            sequence_setter=819,
        ),
        StatueFill(
            Rooms._110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM,
            1,
            sequence_setter=819,
        ),
        StatueFill(
            Rooms._110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM,
            2,
            sequence_setter=819,
        ),
        StatueFill(
            Rooms._113_NIMBUS_CASTLE_AREA_16_SMALL_TWODOOR_ROOM_WTREASURE_FROM_AREA_15,
            3,
            sequence_setter=827,
        ),
        StatueFill(
            Rooms._119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05,
            6,
            sequence_setter=829,
        ),
        StatueFill(
            Rooms._119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05,
            7,
            sequence_setter=829,
        ),
        StatueFill(
            Rooms._408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM_,
            6,
            sequence_setter=830,
        ),
        StatueFill(
            Rooms._408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM_,
            7,
            sequence_setter=830,
        ),
        StatueFill(
            Rooms._440_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_AFTER_VALENTINA,
            0,
            sequence_setter=831,
        ),
        StatueFill(
            Rooms._440_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_AFTER_VALENTINA,
            1,
            sequence_setter=831,
        ),
        StatueFill(Rooms._447_NIMBUS_LAND_HOT_SPRINGS, 1, sequence_setter=832),
        StatueFill(Rooms._447_NIMBUS_LAND_HOT_SPRINGS, 2, sequence_setter=832),
        StatueFill(Rooms._447_NIMBUS_LAND_HOT_SPRINGS, 3, sequence_setter=832),
        StatueFill(Rooms._447_NIMBUS_LAND_HOT_SPRINGS, 4, sequence_setter=832),
        StatueFill(Rooms._497_NIMBUS_CASTLE_AREA_06_____DUMMY, 0, sequence_setter=834),
        StatueFill(Rooms._497_NIMBUS_CASTLE_AREA_06_____DUMMY, 1, sequence_setter=834),
        StatueFill(
            Rooms._499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA,
            1,
            sequence_setter=835,
        ),
        StatueFill(
            Rooms._499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA,
            2,
            sequence_setter=835,
        ),
        StatueFill(
            Rooms._499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA,
            3,
            sequence_setter=835,
        ),
        StatueFill(
            Rooms._499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA,
            4,
            sequence_setter=835,
        ),
        StatueFill(
            Rooms._501_NIMBUS_CASTLE_AREA_03_4WAY_PATH_AFTER_VALENTINA,
            0,
            sequence_setter=836,
        ),
        StatueFill(
            Rooms._501_NIMBUS_CASTLE_AREA_03_4WAY_PATH_AFTER_VALENTINA,
            1,
            sequence_setter=836,
        ),
    ]
    repeatable_henchmen = [
        [
            RepeatableHenchmanFill(
                Rooms._411_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_1ST,
                0,
                DefaultBluebird2,
                False,
                False,
                HenchmanType.PACK,
                95,
                target_scripts=[],
                target_action_scripts=[29],
                sequence_setter=838,
                can_run_away=True,
            ),
        ],
        [
            RepeatableHenchmanFill(
                Rooms._411_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_1ST,
                1,
                DefaultBluebird2,
                False,
                False,
                HenchmanType.PACK,
                95,
                target_scripts=[],
                target_action_scripts=[458],
                sequence_setter=838,
                can_run_away=True,
            ),
            RepeatableHenchmanFill(
                Rooms._121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND,
                2,
                DefaultBluebird2,
                False,
                False,
                HenchmanType.PACK,
                95,
                target_scripts=[],
                target_action_scripts=[458],
                sequence_setter=839,
                can_run_away=True,
            ),
        ],
        [
            RepeatableHenchmanFill(
                Rooms._121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND,
                3,
                DefaultBluebird2,
                False,
                False,
                HenchmanType.PACK,
                95,
                target_scripts=[],
                target_action_scripts=[30],
                sequence_setter=839,
                can_run_away=True,
            ),
            RepeatableHenchmanFill(
                Rooms._121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND,
                4,
                DefaultBluebird2,
                False,
                False,
                HenchmanType.PACK,
                95,
                target_scripts=[],
                target_action_scripts=[30],
                sequence_setter=839,
                can_run_away=True,
            ),
            RepeatableHenchmanFill(
                Rooms._121_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_2ND,
                5,
                DefaultBluebird2,
                False,
                False,
                HenchmanType.PACK,
                95,
                target_scripts=[],
                target_action_scripts=[30],
                sequence_setter=839,
                can_run_away=True,
            ),
            RepeatableHenchmanFill(
                Rooms._437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD,
                1,
                DefaultBluebird2,
                False,
                False,
                HenchmanType.PACK,
                95,
                target_scripts=[],
                target_action_scripts=[30],
                sequence_setter=820,
                can_run_away=True,
            ),
            RepeatableHenchmanFill(
                Rooms._437_NIMBUS_CASTLE_PATH_AFTER_THRONE_ROOM_3RD,
                2,
                DefaultBluebird2,
                False,
                False,
                HenchmanType.PACK,
                95,
                target_scripts=[],
                target_action_scripts=[30],
                sequence_setter=820,
                can_run_away=True,
            ),
        ],
    ]


class CzarDragon(BossAndStarLocation):
    _identifier = 352
    description = AvailableBosses.CzarDragon.value
    name = "Czar Dragon"
    battlefield = Battlefields.CzarDragon
    music = music.MidbossMusic
    boss = CzarBoss
    boss_locations = [
        BossModelFill(
            Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
            1,
            CzarBoss,
            SpriteSize.Large,
            False,
            target_scripts=[3330, 3331],
            target_action_scripts=[941],
            sequence_setter=840,
        ),
    ]
    repeatable_henchmen = [
        [
            RepeatableHenchmanFill(
                Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                2,
                CzarPyrosphere,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[3330, 3331],
                target_action_scripts=[936],
                sequence_setter=840,
            ),
            RepeatableHenchmanFill(
                Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                3,
                CzarPyrosphere,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[3330, 3331],
                target_action_scripts=[936],
                sequence_setter=840,
            ),
            RepeatableHenchmanFill(
                Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                4,
                CzarPyrosphere,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[3330, 3331],
                target_action_scripts=[936],
                sequence_setter=840,
            ),
            RepeatableHenchmanFill(
                Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                5,
                CzarPyrosphere,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[3330, 3331],
                target_action_scripts=[936],
                sequence_setter=840,
            ),
            RepeatableHenchmanFill(
                Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                6,
                CzarPyrosphere,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[3330, 3331],
                target_action_scripts=[937],
                sequence_setter=840,
            ),
            RepeatableHenchmanFill(
                Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                7,
                CzarPyrosphere,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[3330, 3331],
                target_action_scripts=[937],
                sequence_setter=840,
            ),
            RepeatableHenchmanFill(
                Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                8,
                CzarPyrosphere,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[3330, 3331],
                target_action_scripts=[937],
                sequence_setter=840,
            ),
            RepeatableHenchmanFill(
                Rooms._352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                9,
                CzarPyrosphere,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[3330, 3331],
                target_action_scripts=[937],
                sequence_setter=840,
            ),
        ]
    ]


class AxemRangers(BossAndStarLocation):
    _identifier = 393
    description = AvailableBosses.AxemRangers.value
    name = "Axem Red"
    battlefield = Battlefields.AxemRangers
    music = music.BossMusic
    boss = AxemRangersBoss
    boss_locations = [
        BossModelFill(
            Rooms._392_VOLCANO_POSTCD_AREA_06,
            0,
            AxemRangersBoss,
            SpriteSize.Small,
            False,
            target_scripts=[3343],
            target_action_scripts=[],
            sequence_setter=842,
        ),
        BossModelFill(
            Rooms._394_VOLCANO_POSTCD_AREA_05,
            2,
            AxemRangersBoss,
            SpriteSize.Small,
            False,
            target_scripts=[3345],
            target_action_scripts=[],
            sequence_setter=843,
        ),  # NPCs missing from 394 may need to have every command related to them removed from 3345
        BossModelFill(
            Rooms._393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
            1,
            AxemRangersBoss,
            SpriteSize.Small,
            False,
            target_scripts=[3344],
            target_action_scripts=[],
            sequence_setter=844,
        ),  # NPCs missing from room 393 should have their embedded scripts removed and the trampoline bounces reduced
    ]
    unique_henchmen = [
        [
            UniqueHenchmanFill(
                Rooms._392_VOLCANO_POSTCD_AREA_06,
                1,
                AxemRangersAxemGreen,
                False,
                False,
                True,
                HenchmanType.NPC_ONLY,
                target_scripts=[3343],
                target_action_scripts=[],
                sequence_setter=842,
            ),
            UniqueHenchmanFill(
                Rooms._391_VOLCANO_POSTCD_AREA_04,
                0,
                AxemRangersAxemGreen,
                False,
                False,
                True,
                HenchmanType.NPC_ONLY,
                target_scripts=[3341],
                target_action_scripts=[],
                sequence_setter=845,
            ),
            UniqueHenchmanFill(
                Rooms._393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
                2,
                AxemRangersAxemGreen,
                False,
                False,
                True,
                HenchmanType.NPC_ONLY,
                target_scripts=[3344],
                target_action_scripts=[],
                sequence_setter=844,
            ),  # NPCs missing from room 393 should have their embedded scripts removed and the trampoline bounces reduced
        ],
        [
            UniqueHenchmanFill(
                Rooms._392_VOLCANO_POSTCD_AREA_06,
                2,
                AxemRangersAxemYellow,
                False,
                False,
                True,
                HenchmanType.NPC_ONLY,
                target_scripts=[3343],
                target_action_scripts=[],
                sequence_setter=842,
            ),
            UniqueHenchmanFill(
                Rooms._393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
                3,
                AxemRangersAxemYellow,
                False,
                False,
                True,
                HenchmanType.NPC_ONLY,
                target_scripts=[3344],
                target_action_scripts=[],
                sequence_setter=844,
            ),  # NPCs missing from room 393 should have their embedded scripts removed and the trampoline bounces reduced
        ],
        [
            UniqueHenchmanFill(
                Rooms._392_VOLCANO_POSTCD_AREA_06,
                3,
                AxemRangersAxemPink,
                False,
                False,
                True,
                HenchmanType.NPC_ONLY,
                target_scripts=[3343],
                target_action_scripts=[],
                sequence_setter=842,
            ),
            UniqueHenchmanFill(
                Rooms._394_VOLCANO_POSTCD_AREA_05,
                1,
                AxemRangersAxemPink,
                False,
                False,
                True,
                HenchmanType.NPC_ONLY,
                target_scripts=[3345],
                target_action_scripts=[],
                sequence_setter=843,
            ),
            UniqueHenchmanFill(
                Rooms._393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
                4,
                AxemRangersAxemPink,
                False,
                False,
                True,
                HenchmanType.NPC_ONLY,
                target_scripts=[3344],
                target_action_scripts=[],
                sequence_setter=844,
            ),  # NPCs missing from room 393 should have their embedded scripts removed and the trampoline bounces reduced
        ],
        [
            UniqueHenchmanFill(
                Rooms._392_VOLCANO_POSTCD_AREA_06,
                4,
                AxemRangersAxemBlack,
                False,
                False,
                True,
                HenchmanType.NPC_ONLY,
                target_scripts=[3343],
                target_action_scripts=[],
                sequence_setter=842,
            ),
            UniqueHenchmanFill(
                Rooms._394_VOLCANO_POSTCD_AREA_05,
                0,
                AxemRangersAxemBlack,
                False,
                False,
                True,
                HenchmanType.NPC_ONLY,
                target_scripts=[3345],
                target_action_scripts=[],
                sequence_setter=843,
            ),
            UniqueHenchmanFill(
                Rooms._393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
                5,
                AxemRangersAxemBlack,
                False,
                False,
                True,
                HenchmanType.NPC_ONLY,
                target_scripts=[3344],
                target_action_scripts=[],
                sequence_setter=844,
            ),  # NPCs missing from room 393 should have their embedded scripts removed and the trampoline bounces reduced
        ],
    ]


class Chester(BossAndStarLocation):
    _identifier = 461
    description = AvailableBosses.Chester.value
    name = "Chester"
    battlefield = Battlefields.BowsersKeep
    music = music.NormalBattleMusic
    boss = ChesterBoss
    boss_locations = [
        BossModelFill(
            Rooms._461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB,
            4,
            ChesterBoss,
            SpriteSize.Small,
            False,
            target_scripts=[2174, 2190],
            target_action_scripts=[],
            sequence_setter=846,
        ),  # remove sequence set from 2174
    ]


class Magikoopa(BowsersKeepLocation):
    _identifier = 266
    description = AvailableBosses.Magikoopa.value
    name = "Magikoopa"
    battlefield = Battlefields.BowsersKeep
    music = music.MidbossMusic
    boss = MagikoopaBoss
    boss_locations = [
        BossModelFill(
            Rooms._266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM,
            1,
            MagikoopaBoss,
            SpriteSize.Small,
            False,
            target_scripts=[2208, 2209, 942],
            target_action_scripts=[],
            sequence_setter=847,
        ),  # may need to remove palette setter if not magikoopa, may need special animation when summoning
        BossModelFill(
            Rooms._376_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2B_1ST_FIGHT_CHEWY,
            0,
            MagikoopaBoss,
            SpriteSize.Small,
            False,
            target_scripts=[2181, 2182, 2183, 2184, 941],
            target_action_scripts=[1004, 1005],
            sequence_setter=848,
        ),  # may need special animation when summoning
        BossModelFill(
            Rooms._377_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2C_1ST_FIGHT_SPARKY,
            0,
            MagikoopaBoss,
            SpriteSize.Small,
            False,
            target_scripts=[2186, 2187, 2188, 2189, 941],
            target_action_scripts=[1004, 1005],
            sequence_setter=849,
        ),  # may need special animation when summoning
        BossModelFill(
            Rooms._459_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1A_1ST_FIGHT_TERRA_COTTA,
            0,
            MagikoopaBoss,
            SpriteSize.Small,
            False,
            target_scripts=[2161, 2162, 2163, 2164, 941],
            target_action_scripts=[1004, 1005],
            sequence_setter=850,
        ),  # may need special animation when summoning
        BossModelFill(
            Rooms._460_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1B_1ST_FIGHT_ALLEY_RAT,
            0,
            MagikoopaBoss,
            SpriteSize.Small,
            False,
            target_scripts=[2166, 2167, 2168, 2169, 941],
            target_action_scripts=[1004, 1005],
            sequence_setter=851,
        ),  # may need special animation when summoning
        BossModelFill(
            Rooms._461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB,
            0,
            MagikoopaBoss,
            SpriteSize.Small,
            False,
            target_scripts=[2171, 2172, 2173, 2174, 941],
            target_action_scripts=[1004, 1005],
            sequence_setter=846,
        ),  # may need special animation when summoning
        BossModelFill(
            Rooms._462_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2A_1ST_FIGHT_GU_GOOMBA,
            0,
            MagikoopaBoss,
            SpriteSize.Small,
            False,
            target_scripts=[2176, 2177, 2178, 2179, 941],
            target_action_scripts=[1004, 1005],
            sequence_setter=852,
        ),  # may need special animation when summoning
        BossModelFill(
            Rooms._435_ENDING_CREDITS_BOWSERS_KEEP_BOWSER__TROOPS_REPAIR,
            6,
            MagikoopaBoss,
            SpriteSize.Small,
            False,
            target_scripts=[2622],
            target_action_scripts=[],
            sequence_setter=1192,
        ),
    ]


class Boomer(BowsersKeepLocation):
    _identifier = 521
    description = AvailableBosses.Boomer.value
    name = "Boomer"
    battlefield = Battlefields.Boomer
    music = music.MidbossMusic
    boss = BoomerBoss
    boss_locations = [
        BossModelFill(
            Rooms._400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM,
            0,
            BoomerBoss,
            SpriteSize.Large,
            False,
            target_scripts=[2224, 2225, 943],
            target_action_scripts=[],
            sequence_setter=853,
        ),  # 2225 may need a sequence switch
    ]


class Exor(BowsersKeepLocation):
    _identifier = 522
    description = AvailableBosses.Exor.value
    name = "Exor"
    battlefield = Battlefields.BowsersKeep
    music = music.BossMusic
    boss = ExorBoss


class Countdown(BossLocation):
    _identifier = 223
    _grant_identifier = 433
    description = AvailableBosses.CountDown.value
    name = "Count Down"
    battlefield = Battlefields.Gate
    music = music.MidbossMusic
    boss = CountdownBoss
    boss_locations = [
        BossModelFill(
            Rooms._223_SMITHY_FACTORY_AREA_07_COUNT_DOWNS_ROOM,
            0,
            CountdownBoss,
            SpriteSize.Small,
            False,
            target_scripts=[2363],
            target_action_scripts=[],
            sequence_setter=854,
        ),
    ]
    repeatable_henchmen = [
        [
            RepeatableHenchmanFill(
                Rooms._223_SMITHY_FACTORY_AREA_07_COUNT_DOWNS_ROOM,
                1,
                CountdownDingALing,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[2363],
                target_action_scripts=[],
                sequence_setter=854,
            ),
            RepeatableHenchmanFill(
                Rooms._223_SMITHY_FACTORY_AREA_07_COUNT_DOWNS_ROOM,
                2,
                CountdownDingALing,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[2363],
                target_action_scripts=[],
                sequence_setter=854,
            ),
        ]
    ]


class CloakerDomino(BossLocation):
    _identifier = 103
    description = AvailableBosses.CloakerDomino.value
    name = "Domino"
    battlefield = Battlefields.Gate
    music = music.MidbossMusic
    boss = CloakerDominoBoss


class Clerk(BossLocation):
    _identifier = 469
    _grant_identifier = 406
    description = AvailableBosses.Clerk.value
    name = "Clerk"
    battlefield = Battlefields.Factory
    boss = ClerkBoss
    boss_locations = [
        BossModelFill(
            Rooms._469_FACTORY_GROUNDS_AREA_01,
            8,
            ClerkBoss,
            SpriteSize.Small,
            False,
            target_scripts=[2606],
            target_action_scripts=[],
            sequence_setter=855,
        ),
    ]
    repeatable_henchmen = [
        [
            RepeatableHenchmanFill(
                Rooms._469_FACTORY_GROUNDS_AREA_01,
                6,
                DefaultMadMallet,
                False,
                False,
                HenchmanType.EXTERNAL_EVENT,
                1186,
                target_scripts=[2606],
                target_action_scripts=[],
                sequence_setter=855,
                battlefield=Battlefields.Factory,
            ),
            RepeatableHenchmanFill(
                Rooms._469_FACTORY_GROUNDS_AREA_01,
                7,
                DefaultMadMallet,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[2606],
                target_action_scripts=[],
                sequence_setter=855,
            ),
        ]
    ]


class Manager(BossLocation):
    _identifier = 471
    description = AvailableBosses.Manager.value
    name = "Manager"
    battlefield = Battlefields.Factory
    boss = ManagerBoss
    boss_locations = [
        BossModelFill(
            Rooms._471_FACTORY_GROUNDS_AREA_02,
            15,
            ManagerBoss,
            SpriteSize.Small,
            False,
            target_scripts=[2617, 2618],
            target_action_scripts=[],
            sequence_setter=856,
        ),
    ]
    unique_henchmen = [
        [
            UniqueHenchmanFill(
                Rooms._471_FACTORY_GROUNDS_AREA_02,
                12,
                ManagerPounder,
                False,
                True,
                True,
                HenchmanType.NPC_ONLY,
                target_scripts=[2617, 2618],
                target_action_scripts=[960, 961],
                sequence_setter=856,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._471_FACTORY_GROUNDS_AREA_02,
                13,
                ManagerPounder,
                False,
                True,
                True,
                HenchmanType.NPC_ONLY,
                target_scripts=[2617, 2618],
                target_action_scripts=[960, 961],
                sequence_setter=856,
            ),
        ],
        [
            # For NPCs that need to walk X steps, maybe fix F -coord if it otherwise forces a direction change.
            UniqueHenchmanFill(
                Rooms._471_FACTORY_GROUNDS_AREA_02,
                14,
                ManagerPounder,
                False,
                True,
                True,
                HenchmanType.NPC_ONLY,
                target_scripts=[2617, 2618],
                target_action_scripts=[960, 961],
                sequence_setter=856,
            ),
        ],
    ]


class Director(BossLocation):
    _identifier = 472
    description = AvailableBosses.Director.value
    name = "Director"
    battlefield = Battlefields.Factory
    boss = DirectorBoss
    boss_locations = [
        BossModelFill(
            Rooms._472_FACTORY_GROUNDS_AREA_03,
            10,
            DirectorBoss,
            SpriteSize.Small,
            False,
            target_scripts=[2621, 2627],
            target_action_scripts=[],
            sequence_setter=857,
        ),
    ]
    unique_henchmen = [
        [
            UniqueHenchmanFill(
                Rooms._472_FACTORY_GROUNDS_AREA_03,
                7,
                DirectorPoundette,
                True,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[2621],
                target_action_scripts=[962],
                sequence_setter=857,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._472_FACTORY_GROUNDS_AREA_03,
                8,
                DirectorPoundette,
                True,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[2621],
                target_action_scripts=[963],
                sequence_setter=857,
            ),
        ],
        [
            UniqueHenchmanFill(
                Rooms._472_FACTORY_GROUNDS_AREA_03,
                9,
                DirectorPoundette,
                True,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[2621],
                target_action_scripts=[964],
                sequence_setter=857,
            ),
        ],
    ]


class Gunyolk(BossLocation):
    _identifier = 470
    description = AvailableBosses.Gunyolk.value
    name = "Factory Chief"
    battlefield = Battlefields.Factory
    music = music.MidbossMusic
    boss = GunyolkBoss
    boss_locations = [
        BossModelFill(
            Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
            12,
            GunyolkBoss,
            SpriteSize.Small,
            False,
            target_scripts=[2601, 2603],
            target_action_scripts=[],
            sequence_setter=858,
        ),
    ]
    unique_henchmen = [
        [
            UniqueHenchmanFill(
                Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                0,
                GunyolkPiece,
                False,
                True,
                True,
                HenchmanType.NPC_ONLY,
                target_scripts=[2601],
                target_action_scripts=[],
                sequence_setter=858,
            ),  # hide a lot of clones if not vanilla
        ],
    ]


class Smithy(BossLocation):
    _identifier = 496
    _grant_identifier = 523
    description = AvailableBosses.Smithy.value
    name = "Smithy"
    battlefield = Battlefields.Smithy
    music = music.Smithy1Music
    boss = SmithyBoss
    # hide all other parts of smithy if shuffled
    boss_locations = [
        BossModelFill(
            Rooms._509_FACTORY_GROUNDS_SMITHYS_PAD,
            4,
            SmithyBoss,
            SpriteSize.Large,
            False,
            target_scripts=[3792, 3794],
            target_action_scripts=[],
            sequence_setter=859,
        ),  # hide a lot of clones if not vanilla
    ]
    repeatable_henchmen = [
        [
            RepeatableHenchmanFill(
                Rooms._406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                1,
                DefaultPaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[945],
                sequence_setter=859,
            ),
            RepeatableHenchmanFill(
                Rooms._406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                2,
                DefaultPaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[945],
                sequence_setter=859,
            ),
            RepeatableHenchmanFill(
                Rooms._406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                3,
                DefaultPaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[945],
                sequence_setter=859,
            ),
            RepeatableHenchmanFill(
                Rooms._406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                4,
                DefaultPaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[945],
                sequence_setter=859,
            ),
            RepeatableHenchmanFill(
                Rooms._406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                5,
                DefaultPaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[945],
                sequence_setter=859,
            ),
            RepeatableHenchmanFill(
                Rooms._406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
                6,
                DefaultPaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[945],
                sequence_setter=859,
            ),
            RepeatableHenchmanFill(
                Rooms._469_FACTORY_GROUNDS_AREA_01,
                0,
                DefaultPaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[945],
                sequence_setter=855,
            ),
            RepeatableHenchmanFill(
                Rooms._469_FACTORY_GROUNDS_AREA_01,
                1,
                DefaultPaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[945],
                sequence_setter=855,
            ),
            RepeatableHenchmanFill(
                Rooms._469_FACTORY_GROUNDS_AREA_01,
                2,
                DefaultPaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[945],
                sequence_setter=855,
            ),
            RepeatableHenchmanFill(
                Rooms._469_FACTORY_GROUNDS_AREA_01,
                3,
                DefaultPaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[945],
                sequence_setter=855,
            ),
            RepeatableHenchmanFill(
                Rooms._469_FACTORY_GROUNDS_AREA_01,
                4,
                DefaultPaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[945],
                sequence_setter=855,
            ),
            RepeatableHenchmanFill(
                Rooms._469_FACTORY_GROUNDS_AREA_01,
                5,
                DefaultPaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[945],
                sequence_setter=855,
            ),
            RepeatableHenchmanFill(
                Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                7,
                DefaultUnpaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[955],
                sequence_setter=858,
            ),
            RepeatableHenchmanFill(
                Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                8,
                DefaultUnpaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[954],
                sequence_setter=858,
            ),
            RepeatableHenchmanFill(
                Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                9,
                DefaultUnpaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[954],
                sequence_setter=858,
            ),
            RepeatableHenchmanFill(
                Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                10,
                DefaultUnpaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[954],
                sequence_setter=858,
            ),
            RepeatableHenchmanFill(
                Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                11,
                DefaultUnpaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[956],
                sequence_setter=858,
            ),
            RepeatableHenchmanFill(
                Rooms._470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
                15,
                DefaultUnpaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[959],
                sequence_setter=858,
            ),
            RepeatableHenchmanFill(
                Rooms._471_FACTORY_GROUNDS_AREA_02,
                0,
                DefaultUnpaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[949],
                sequence_setter=856,
            ),
            RepeatableHenchmanFill(
                Rooms._471_FACTORY_GROUNDS_AREA_02,
                1,
                DefaultUnpaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[949],
                sequence_setter=856,
            ),
            RepeatableHenchmanFill(
                Rooms._471_FACTORY_GROUNDS_AREA_02,
                2,
                DefaultUnpaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[949],
                sequence_setter=856,
            ),
            RepeatableHenchmanFill(
                Rooms._471_FACTORY_GROUNDS_AREA_02,
                3,
                DefaultUnpaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[948],
                sequence_setter=856,
            ),
            RepeatableHenchmanFill(
                Rooms._471_FACTORY_GROUNDS_AREA_02,
                4,
                DefaultUnpaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[948],
                sequence_setter=856,
            ),
            RepeatableHenchmanFill(
                Rooms._471_FACTORY_GROUNDS_AREA_02,
                5,
                DefaultUnpaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[948],
                sequence_setter=856,
            ),
            RepeatableHenchmanFill(
                Rooms._471_FACTORY_GROUNDS_AREA_02,
                6,
                DefaultPaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[951],
                sequence_setter=856,
            ),
            RepeatableHenchmanFill(
                Rooms._471_FACTORY_GROUNDS_AREA_02,
                7,
                DefaultPaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[951],
                sequence_setter=856,
            ),
            RepeatableHenchmanFill(
                Rooms._471_FACTORY_GROUNDS_AREA_02,
                8,
                DefaultPaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[951],
                sequence_setter=856,
            ),
            RepeatableHenchmanFill(
                Rooms._471_FACTORY_GROUNDS_AREA_02,
                9,
                DefaultPaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[950],
                sequence_setter=856,
            ),
            RepeatableHenchmanFill(
                Rooms._471_FACTORY_GROUNDS_AREA_02,
                10,
                DefaultPaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[950],
                sequence_setter=856,
            ),
            RepeatableHenchmanFill(
                Rooms._471_FACTORY_GROUNDS_AREA_02,
                11,
                DefaultPaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[950],
                sequence_setter=856,
            ),
            RepeatableHenchmanFill(
                Rooms._472_FACTORY_GROUNDS_AREA_03,
                1,
                DefaultUnpaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[968],
                sequence_setter=857,
            ),
            RepeatableHenchmanFill(
                Rooms._472_FACTORY_GROUNDS_AREA_03,
                2,
                DefaultUnpaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[968],
                sequence_setter=857,
            ),
            RepeatableHenchmanFill(
                Rooms._472_FACTORY_GROUNDS_AREA_03,
                3,
                DefaultUnpaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[967],
                sequence_setter=857,
            ),
            RepeatableHenchmanFill(
                Rooms._472_FACTORY_GROUNDS_AREA_03,
                4,
                DefaultUnpaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[966],
                sequence_setter=857,
            ),
            RepeatableHenchmanFill(
                Rooms._472_FACTORY_GROUNDS_AREA_03,
                5,
                DefaultUnpaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[966],
                sequence_setter=857,
            ),
            RepeatableHenchmanFill(
                Rooms._472_FACTORY_GROUNDS_AREA_03,
                6,
                DefaultUnpaintedDrillBit,
                False,
                False,
                HenchmanType.NPC_ONLY,
                target_scripts=[],
                target_action_scripts=[965],
                sequence_setter=857,
            ),
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
