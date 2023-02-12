from typing import List, Optional, Type

from randomizer.entities.bosses.bosses import (
    AxemRangersBoss,
    Belome1Boss,
    Belome2Boss,
    BirdettaBoss,
    BoomerBoss,
    BoosterBoss,
    BowyerBoss,
    BoxBoyBoss,
    BundtBoss,
    ChesterBoss,
    ClerkBoss,
    CloakerDominoBoss,
    CountdownBoss,
    Croco1Boss,
    Croco2Boss,
    CulexBoss,
    CzarBoss,
    DirectorBoss,
    DodoBoss,
    ExorBoss,
    GrateGuyBoss,
    GunyolkBoss,
    HammerBroBoss,
    HidonBoss,
    JaggerBoss,
    Jinx1Boss,
    Jinx2Boss,
    Jinx3Boss,
    JohnnyBoss,
    KamekBoss,
    KingCalamariBoss,
    MackBoss,
    ManagerBoss,
    MegaSmilaxBoss,
    MokuraBoss,
    PandoriteBoss,
    PunchinelloBoss,
    SmithyBoss,
    ValentinaBoss,
    YaridovichBoss,
)
from randomizer.entities.dialogs.overworld_dialogs.constants.dialog_ids import (
    DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING,
)
from randomizer.entities.enemies.enemies import Shelly
from randomizer.entities.progress_locations.helpers.area_access import (
    can_access_balcony_boss,
    can_access_bandits_way,
    can_access_battle_door_boss,
    can_access_chapel_boss,
    can_access_curtain_boss,
    can_access_egg_boss,
    can_access_first_dojo_boss,
    can_access_first_mimic,
    can_access_first_moleville_boss,
    can_access_forest_boss,
    can_access_fourth_dojo_boss,
    can_access_inner_factory_final_boss,
    can_access_inner_factory_first_boss,
    can_access_inner_factory_fourth_boss,
    can_access_inner_factory_second_boss,
    can_access_inner_factory_third_boss,
    can_access_keep_chandelier_boss,
    can_access_keep_exit_boss,
    can_access_lands_end_cloud,
    can_access_nimbus_boss,
    can_access_post_obstacle_boss,
    can_access_sealed_door_boss,
    can_access_seaside_boss,
    can_access_second_dojo_boss,
    can_access_second_factory_boss,
    can_access_second_mimic,
    can_access_second_moleville_boss,
    can_access_sewer_boss,
    can_access_ship_midboss,
    can_access_statue_boss,
    can_access_temple_boss,
    can_access_third_dojo_boss,
    can_access_third_mimic,
    can_access_valley_boss,
    can_access_volcano_midboss,
    can_defeat_bandits_way_boss,
    can_defeat_first_factory_boss,
    can_defeat_ship_midboss,
    can_defeat_volcano_boss,
)
from randomizer.entities.progress_locations.helpers.model_fills import (
    BANDITS_WAY_1_BOSS_FILL,
    BANDITS_WAY_2_BOSS_FILL,
    BANDITS_WAY_3_BOSS_FILL,
    BANDITS_WAY_4_BOSS_FILL,
    BANDITS_WAY_5_BOSS_FILL,
    BEAN_VALLEY_BOSS_FILL,
    BOOSTER_HILL_LEFT_HENCHMAN_FILL,
    BOOSTER_HILL_MIDDLE_HENCHMAN_FILL,
    BOOSTER_HILL_RIGHT_HENCHMAN_FILL,
    BOOSTER_PASS_APPRENTICE_FILL,
    CHAPEL_HENCHMAN_1_FILL,
    CHAPEL_HENCHMAN_2_FILL,
    CHAPEL_HENCHMAN_3_FILL,
    CHAPEL_KITCHEN_BOSS_FILL,
    CHAPEL_KITCHEN_HENCHMAN_1_FILL,
    CHAPEL_KITCHEN_HENCHMAN_2_FILL,
    CHAPEL_SANCTUARY_BOSS_FILL,
    CHAPEL_SANCTUARY_HENCHMAN_1_FILL,
    CHAPEL_SANCTUARY_HENCHMAN_2_FILL,
    DOJO_FIRST_BOSS_FILL,
    DOJO_FOURTH_BOSS_FILL,
    DOJO_SECOND_BOSS_FILL,
    DOJO_THIRD_BOSS_FILL,
    END_OF_NIMBUS_HALLWAY_BOSS_FILL,
    ENDING_CREDITS_CHAPEL_HENCHMAN_1_FILL,
    ENDING_CREDITS_CHAPEL_HENCHMAN_2_FILL,
    ENDING_CREDITS_CHAPEL_HENCHMAN_3_FILL,
    ENDING_CREDITS_CHAPEL_HENCHMAN_4_FILL,
    ENDING_CREDITS_CHAPEL_HENCHMAN_5_FILL,
    ENDING_CREDITS_CHAPEL_HENCHMAN_6_FILL,
    ENDING_CREDITS_CHAPEL_HENCHMAN_7_FILL,
    ENDING_CREDITS_CHAPEL_HENCHMAN_8_FILL,
    ENDING_CREDITS_CHAPEL_NIMBUS_BOSS_FILL,
    ENDING_CREDITS_CHAPEL_PASTOR_FILL,
    ENDING_CREDITS_KEEP_BOSS_CASTLE_REPAIR,
    ENDING_CREDITS_RACER,
    ENDING_CREDITS_SHIP_BOSS_ON_CLIFF_FILL,
    FACTORY_CLOCK_BOSS_FILL,
    FACTORY_CLOCK_LEFT_HENCHMAN_FILL,
    FACTORY_CLOCK_RIGHT_HENCHMAN_FILL,
    FINAL_FACTORY_BOSS_FILL,
    FOREST_BOSS_AREA_BOSS_FILL,
    FOREST_BOTTOM_LEFT_HENCHMAN_FILL,
    FOREST_BOTTOM_MID_LEFT_HENCHMAN_FILL,
    FOREST_BOTTOM_MID_RIGHT_HENCHMAN_FILL,
    FOREST_BOTTOM_RIGHT_HENCHMAN_FILL,
    FOREST_MID_LEFT_HENCHMAN_FILL,
    FOREST_MID_RIGHT_HENCHMAN_FILL,
    FOREST_TOP_LEFT_HENCHMAN_FILL,
    FOREST_TOP_MID_LEFT_HENCHMAN_FILL,
    FOREST_TOP_MID_RIGHT_HENCHMAN_FILL,
    FOREST_TOP_RIGHT_HENCHMAN_FILL,
    GARRO_LEFT_STATUE_FILL,
    GARRO_MID_STATUE_FILL,
    GARRO_RIGHT_STATUE_FILL,
    HOT_SPRINGS_LEFT_NORTHFACING_STATUE,
    HOT_SPRINGS_LEFT_SOUTHFACING_STATUE,
    HOT_SPRINGS_RIGHT_NORTHFACING_STATUE,
    HOT_SPRINGS_RIGHT_SOUTHFACING_STATUE,
    INNER_FACTORY_1_CONVEYOR_HENCHMAN_1_FILL,
    INNER_FACTORY_1_CONVEYOR_HENCHMAN_2_FILL,
    INNER_FACTORY_1_CONVEYOR_HENCHMAN_3_FILL,
    INNER_FACTORY_1_CONVEYOR_HENCHMAN_4_FILL,
    INNER_FACTORY_1_CONVEYOR_HENCHMAN_5_FILL,
    INNER_FACTORY_1_CONVEYOR_HENCHMAN_6_FILL,
    INNER_FACTORY_1_POST_DEFEAT_CONVEYOR_HENCHMAN_1_FILL,
    INNER_FACTORY_1_POST_DEFEAT_CONVEYOR_HENCHMAN_2_FILL,
    INNER_FACTORY_1_POST_DEFEAT_CONVEYOR_HENCHMAN_3_FILL,
    INNER_FACTORY_1_POST_DEFEAT_CONVEYOR_HENCHMAN_4_FILL,
    INNER_FACTORY_1_POST_DEFEAT_CONVEYOR_HENCHMAN_5_FILL,
    INNER_FACTORY_1_POST_DEFEAT_CONVEYOR_HENCHMAN_6_FILL,
    INNER_FACTORY_2_CONVEYOR_HENCHMAN_1_FILL,
    INNER_FACTORY_2_CONVEYOR_HENCHMAN_2_FILL,
    INNER_FACTORY_2_CONVEYOR_HENCHMAN_3_FILL,
    INNER_FACTORY_2_CONVEYOR_HENCHMAN_4_FILL,
    INNER_FACTORY_2_CONVEYOR_HENCHMAN_5_FILL,
    INNER_FACTORY_2_CONVEYOR_HENCHMAN_6_FILL,
    INNER_FACTORY_2_CONVEYOR_HENCHMAN_7_FILL,
    INNER_FACTORY_2_CONVEYOR_HENCHMAN_8_FILL,
    INNER_FACTORY_2_CONVEYOR_HENCHMAN_9_FILL,
    INNER_FACTORY_2_CONVEYOR_HENCHMAN_10_FILL,
    INNER_FACTORY_2_CONVEYOR_HENCHMAN_11_FILL,
    INNER_FACTORY_2_CONVEYOR_HENCHMAN_12_FILL,
    INNER_FACTORY_3_CONVEYOR_HENCHMAN_1_FILL,
    INNER_FACTORY_3_CONVEYOR_HENCHMAN_2_FILL,
    INNER_FACTORY_3_CONVEYOR_HENCHMAN_3_FILL,
    INNER_FACTORY_3_CONVEYOR_HENCHMAN_4_FILL,
    INNER_FACTORY_3_CONVEYOR_HENCHMAN_5_FILL,
    INNER_FACTORY_3_CONVEYOR_HENCHMAN_6_FILL,
    INNER_FACTORY_4_CONVEYOR_HENCHMAN_1_FILL,
    INNER_FACTORY_4_CONVEYOR_HENCHMAN_2_FILL,
    INNER_FACTORY_4_CONVEYOR_HENCHMAN_3_FILL,
    INNER_FACTORY_4_CONVEYOR_HENCHMAN_4_FILL,
    INNER_FACTORY_4_CONVEYOR_HENCHMAN_5_FILL,
    INNER_FACTORY_4_CONVEYOR_HENCHMAN_6_FILL,
    INNER_FACTORY_FIRST_BOSS_FILL,
    INNER_FACTORY_FIRST_BOSS_LEFT_HENCHMAN,
    INNER_FACTORY_FIRST_BOSS_RIGHT_HENCHMAN,
    INNER_FACTORY_FOURTH_BOSS_FILL,
    INNER_FACTORY_FOURTH_BOSS_HENCHMAN_FILL,
    INNER_FACTORY_LEFT_ASSEMBLER,
    INNER_FACTORY_MID_ASSEMBLER,
    INNER_FACTORY_RIGHT_ASSEMBLER,
    INNER_FACTORY_SECOND_BOSS_FILL,
    INNER_FACTORY_SECOND_BOSS_LEFT_HENCHMAN,
    INNER_FACTORY_SECOND_BOSS_MID_HENCHMAN,
    INNER_FACTORY_SECOND_BOSS_RIGHT_HENCHMAN,
    INNER_FACTORY_THIRD_BOSS_FILL,
    KEEP_BATTLE_ROOM_1_END_BOSS_FILL,
    KEEP_BATTLE_ROOM_2_END_BOSS_FILL,
    KEEP_BATTLE_ROOM_3_END_BOSS_FILL,
    KEEP_BATTLE_ROOM_4_END_BOSS_FILL,
    KEEP_BATTLE_ROOM_5_END_BOSS_FILL,
    KEEP_BATTLE_ROON_6_END_BOSS_FILL,
    KEEP_CHANDELIER_BOSS_FILL,
    KEEP_MIDBOSS_LAIR_FILL,
    KEEP_OBSTACLE_ROOM_FINAL_FIGHT_FILL,
    KINGDOM_ANTECHAMBER_LEFT_HENCHMAN_FILL,
    KINGDOM_ANTECHAMBER_RIGHT_HENCHMAN_FILL,
    KINGDOM_BEDROOM_ANTECHAMBER_LEFT_HENCHMAN_FILL,
    KINGDOM_BEDROOM_ANTECHAMBER_RIGHT_HENCHMAN_FILL,
    KINGDOM_EXTERIOR_GRASS_HENCHMAN_FILL,
    KINGDOM_EXTERIOR_NPC_HITTING_HOUSE_HENCHMAN_FILL,
    KINGDOM_EXTERIOR_NPC_TERRORIZING_GUARD_HENCHMAN_FILL,
    KINGDOM_EXTERIOR_RESPAWNING_HENCHMAN_1,
    KINGDOM_EXTERIOR_RESPAWNING_HENCHMAN_2,
    KINGDOM_EXTERIOR_RESPAWNING_HENCHMAN_3,
    KINGDOM_EXTERIOR_STANDING_HENCHMAN_FILL,
    KINGDOM_HOUSE_BED_HENCHMAN_FILL,
    KINGDOM_HOUSE_SINK_HENCHMAN_FILL,
    KINGDOM_HOUSE_TABLE_HENCHMAN_FILL,
    KINGDOM_MAIN_HALL_DOOR_GUARD_HENCHMAN_FILL,
    KINGDOM_MAIN_HALL_REPEATING_HENCHMAN_FILL_1,
    KINGDOM_MAIN_HALL_REPEATING_HENCHMAN_FILL_2,
    KINGDOM_MAIN_HALL_REPEATING_HENCHMAN_FILL_3,
    KINGDOM_MAIN_HALL_TERRORIZING_TOAD_HENCHMAN_FILL,
    KINGDOM_RIGHT_HALL_LEFT_HENCHMAN_FILL,
    KINGDOM_RIGHT_HALL_RIGHT_HENCHMAN_FILL,
    KINGDOM_STAIRCASE_LEFT_HENCHMAN_FILL,
    KINGDOM_STAIRCASE_RIGHT_HENCHMAN_FILL,
    MINES_BOSS_BATTLE_HENCHMAN_FILL_1,
    MINES_BOSS_BATTLE_HENCHMAN_FILL_2,
    MINES_BOSS_BATTLE_HENCHMAN_FILL_3,
    MINES_BOSS_TINY_HENCHMAN_FILL_1,
    MINES_BOSS_TINY_HENCHMAN_FILL_2,
    MINES_BOSS_TINY_HENCHMAN_FILL_3,
    MINES_CIRCLE_EXIT_ROOM_BOSS_FILL,
    MINES_CIRCLE_EXPLODED_ROOM,
    MINES_CIRCLE_LEFT_OF_TRAMPOLINE_ROOM_BOSS_FILL,
    MINES_CIRCLE_PRE_EXPLODED_ROOM,
    MINES_CIRCLE_SMALL_ROOM_BOSS_FILL,
    MINES_CIRCLE_TRAMPOLINE_ROOM_BOSS_FILL,
    MINES_FINAL_BOSS_FILL,
    MINES_LEFT_HENCHMAN_FILL,
    MINES_RIGHT_HENCHMAN_FILL,
    MINES_TRAMPOLINE_HENCHMAN_FILL,
    MONSTRO_SEALED_DOOR_BOSS_FILL,
    MUSHROOM_WAY_2_BOSS_FILL,
    NIMBUS_ANTECHAMBER_NORTHFACING_STATUE,
    NIMBUS_ANTECHAMBER_SOUTHFACING_STATUE,
    NIMBUS_BACKDOOR_HALLWAY_1_LEFT_HENCHMAN_FILL,
    NIMBUS_BACKDOOR_HALLWAY_1_RIGHT_HENCHMAN_FILL,
    NIMBUS_BACKDOOR_HALLWAY_2_FIRST_HENCHMAN_FILL,
    NIMBUS_BACKDOOR_HALLWAY_2_FOURTH_HENCHMAN_FILL,
    NIMBUS_BACKDOOR_HALLWAY_2_SECOND_HENCHMAN_FILL,
    NIMBUS_BACKDOOR_HALLWAY_2_THIRD_HENCHMAN_FILL,
    NIMBUS_BACKDOOR_HALLWAY_3_FIRST_HENCHMAN_FILL,
    NIMBUS_BACKDOOR_HALLWAY_3_SECOND_HENCHMAN_FILL,
    NIMBUS_BOSS_ON_BALCONY_FILL,
    NIMBUS_CELLAR_HALLWAY_LEFT_STATUE,
    NIMBUS_CELLAR_HALLWAY_RIGHT_STATUE,
    NIMBUS_CONFRONTATION_BOSS_FILL,
    NIMBUS_FIVEDOOR_HALLWAY_LEFT_NORTHFACING_STATUE,
    NIMBUS_FIVEDOOR_HALLWAY_LEFT_SOUTHFACING_STATUE,
    NIMBUS_FIVEDOOR_HALLWAY_RIGHT_NORTHFACING_STATUE,
    NIMBUS_FIVEDOOR_HALLWAY_RIGHT_SOUTHFACING_STATUE,
    NIMBUS_LEFT_SHAMAN_HALL_NORTHFACING_STATUE,
    NIMBUS_LEFT_SHAMAN_HALL_SOUTHFACING_STATUE,
    NIMBUS_LIBERATED_4PATH_NORTHFACING_STATUE,
    NIMBUS_LIBERATED_4PATH_SOUTHFACING_STATUE,
    NIMBUS_LIBERATED_THRONE_ROOM_NORTHFACING_STATUE,
    NIMBUS_LIBERATED_THRONE_ROOM_SOUTHFACING_STATUE,
    NIMBUS_LONE_STATUE,
    NIMBUS_MAIN_HALL_LEFT_NORTHFACING_STATUE_FILL,
    NIMBUS_MAIN_HALL_LEFT_SOUTHFACING_STATUE_FILL,
    NIMBUS_MAIN_HALL_MID_NORTHFACING_STATUE_FILL,
    NIMBUS_MAIN_HALL_MID_SOUTHFACING_STATUE_FILL,
    NIMBUS_MAIN_HALL_RIGHT_NORTHFACING_STATUE_FILL,
    NIMBUS_MAIN_HALL_RIGHT_SOUTHFACING_STATUE_FILL,
    NIMBUS_OCCUPIED_4PATH_NORTHFACING_STATUE,
    NIMBUS_OCCUPIED_4PATH_SOUTHFACING_STATUE,
    NIMBUS_OCCUPIED_THRONE_ROOM_NORTHFACING_STATUE,
    NIMBUS_OCCUPIED_THRONE_ROOM_SOUTHFACING_STATUE,
    NIMBUS_POLISHING_ROOM_LEFT_STATUE,
    NIMBUS_POLISHING_ROOM_MID_STATUE,
    NIMBUS_POLISHING_ROOM_RIGHT_STATUE,
    NIMBUS_RIGHT_SHAMAN_HALL_NORTHFACING_STATUE,
    NIMBUS_RIGHT_SHAMAN_HALL_SOUTHFACING_STATUE,
    PASSWORD_ROOM_BECKON_BOSS_FILL,
    SEASIDE_BEACH_BOSS_FILL_SMALL,
    SEASIDE_BEACH_HENCHMAN_1_FILL,
    SEASIDE_BEACH_HENCHMAN_2_FILL,
    SEASIDE_BEACH_HENCHMAN_3_FILL,
    SEASIDE_BEACH_HENCHMAN_4_FILL,
    SEASIDE_BOSS_TRANSFORMED_FILL,
    SEASIDE_CONFRONTATION_BOSS_FILL,
    SEASIDE_CONFRONTATION_HENCHMAN_3_FILL,
    SEASIDE_CONFRONTATION_HENCHMAN_4_FILL,
    SEASIDE_CUSTOMER_HENCHMAN_FILL,
    SEASIDE_HOUSE_BOSS_FILL,
    SEASIDE_INNKEEPER_1F_HENCHMAN_FILL,
    SEASIDE_INNKEEPER_2F_HENCHMAN_FILL,
    SEASIDE_LONG_SHOP_LEFT_HENCHMAN_FILL,
    SEASIDE_LONG_SHOP_RIGHT_HENCHMAN_FILL,
    SEASIDE_OUTSIDE_LEFT_GUARD,
    SEASIDE_OUTSIDE_RIGHT_GUARD,
    SEASIDE_RIGHT_BUILDING_LEFT_DOOR_HENCHMAN_FILL,
    SEASIDE_RIGHT_BUILDING_MIDDLE_DOOR_HENCHMAN_LOWER_FILL,
    SEASIDE_RIGHT_BUILDING_MIDDLE_DOOR_HENCHMAN_UPPER_FILL,
    SEASIDE_RIGHT_BUILDING_RIGHT_DOOR_HENCHMAN_FILL,
    SEASIDE_SHOPKEEPER_HENCHMAN_FILL,
    SEWER_BOSS_ROOM_FILL,
    SHIP_BOSS_ON_BEACH_FILL,
    SHIP_FINAL_ROOM_BOSS_FILL,
    SHIP_FIRST_FORCED_HENCHMAN_FIGHT_FILL_1,
    SHIP_FIRST_FORCED_HENCHMAN_FIGHT_FILL_2,
    SHIP_FIRST_FORCED_HENCHMAN_FIGHT_FILL_3,
    SHIP_FIRST_FORCED_HENCHMAN_FIGHT_FILL_4,
    SHIP_MAIN_HENCHMAN_1_BEACH_FILL,
    SHIP_MAIN_HENCHMAN_1_BOSS_ROOM_FILL,
    SHIP_MAIN_HENCHMAN_2_BEACH_FILL,
    SHIP_MAIN_HENCHMAN_2_BOSS_ROOM_FILL,
    SHIP_MAIN_HENCHMAN_3_BOSS_ROOM_FILL,
    SHIP_MAIN_HENCHMAN_4_BOSS_ROOM_FILL,
    SHIP_SECOND_FORCED_HENCHMAN_FIGHT_FILL_1,
    SHIP_SECOND_FORCED_HENCHMAN_FIGHT_FILL_2,
    STATUE_POLISHER_FILL,
    STATUE_ROOM_BOSS_FILL,
    TEMPLE_BOSS_FILL,
    THRONE_ROOM_BOSS_FILL,
    THRONE_ROOM_BOTTOM_LEFT_HENCHMAN_FILL,
    THRONE_ROOM_BOTTOM_RIGHT_HENCHMAN_FILL,
    THRONE_ROOM_MID_LEFT_HENCHMAN_FILL,
    THRONE_ROOM_MID_RIGHT_HENCHMAN_FILL,
    THRONE_ROOM_TOP_LEFT_HENCHMAN_FILL,
    THRONE_ROOM_TOP_RIGHT_HENCHMAN_FILL,
    TOWER_ANCESTOR_GAME_MASTER_NPC_FILL,
    TOWER_BALCONY_HENCHMAN_1_FILL,
    TOWER_BALCONY_HENCHMAN_2_FILL,
    TOWER_BALCONY_HENCHMAN_3_FILL,
    TOWER_BEHIND_BOBOMB_CURTAINS_BOSS_FILL,
    TOWER_BOSS_BOOSTER_HILL_FILL,
    TOWER_BOSS_ENDING_CREDITS_WEDDING_FILL,
    TOWER_BOSS_FIRST_ROOM_BEHIND_DOORWAY_FILL,
    TOWER_BOSS_FRONT_DOOR_FILL,
    TOWER_BOSS_ON_BALCONY_FILL,
    TOWER_BOSS_SANCTUARY_NPC_FILL,
    TOWER_BULLET_ROOM_HENCHMAN_FILL,
    TOWER_CURTAIN_GAME_ROOM_BOSS_FILL,
    TOWER_CURTAIN_GAME_ROOM_HENCHMAN_1_FILL,
    TOWER_CURTAIN_GAME_ROOM_HENCHMAN_2_FILL,
    TOWER_CURTAIN_GAME_ROOM_HENCHMAN_3_FILL,
    TOWER_LOBBY_HENCHMAN_FILL,
    TOWER_SEESAW_CHEST_NPC_FILL,
    TOWER_TRAIN_ROOM_HENCHMAN_FILL,
    VOLCANO_BOSS_FINAL_STAIRCASE_FILL,
    VOLCANO_BOSS_TELEPORT_FILL,
    VOLCANO_BOSS_TRAMPOLINE_FILL,
    VOLCANO_BRIDGE_ASSEMBLER_HENCHMAN_1_FILL,
    VOLCANO_BRIDGE_ASSEMBLER_HENCHMAN_2_FILL,
    VOLCANO_BRIDGE_ASSEMBLER_HENCHMAN_3_FILL,
    VOLCANO_BRIDGE_ASSEMBLER_HENCHMAN_4_FILL,
    VOLCANO_BRIDGE_ASSEMBLER_HENCHMAN_5_FILL,
    VOLCANO_BRIDGE_ASSEMBLER_HENCHMAN_6_FILL,
    VOLCANO_BRIDGE_ASSEMBLER_HENCHMAN_7_FILL,
    VOLCANO_BRIDGE_ASSEMBLER_HENCHMAN_8_FILL,
    VOLCANO_BRIDGE_BOSS_FILL,
    VOLCANO_FIRST_HENCHMAN_FINAL_STAIRCASE_FILL,
    VOLCANO_FIRST_HENCHMAN_TINY_ROOM_FILL,
    VOLCANO_FIRST_HENCHMAN_TRAMPOLINE_FILL,
    VOLCANO_FOURTH_HENCHMAN_FINAL_STAIRCASE_FILL,
    VOLCANO_FOURTH_HENCHMAN_TELEPORT_FILL,
    VOLCANO_FOURTH_HENCHMAN_TRAMPOLINE_FILL,
    VOLCANO_SECOND_HENCHMAN_FINAL_STAIRCASE_FILL,
    VOLCANO_SECOND_HENCHMAN_TRAMPOLINE_FILL,
    VOLCANO_THIRD_HENCHMAN_FINAL_STAIRCASE_FILL,
    VOLCANO_THIRD_HENCHMAN_TELEPORT_FILL,
    VOLCANO_THIRD_HENCHMAN_TRAMPOLINE_FILL,
)
from randomizer.types.battle_animation_scripts.classes import AnimationScriptBank
from randomizer.types.battle_animation_scripts.commands import Jmp, Pause1Frame
from randomizer.types.battle_animation_scripts.constants.script_ids.bank_names import (
    SUBROUTINES_0X3A8BE4,
)
from randomizer.types.battles.formations.classes import FormationMember
from randomizer.types.battles.formations.constants.formation_ids import (
    FORM0297_BIRDETTA_BOSS_FIGHT,
)
from randomizer.types.bosses.classes import Boss
from randomizer.types.bosses.enums import Battlefields, BattleMusic, BossLocations
from randomizer.types.monster_scripts.commands import CallTarget, RunBattleEvent
from randomizer.types.monster_scripts.constants.targets import (
    MONSTER_1_CALL,
    MONSTER_2_CALL,
    MONSTER_3_CALL,
    MONSTER_4_CALL,
    MONSTER_5_CALL,
    MONSTER_6_CALL,
    MONSTER_7_CALL,
    MONSTER_8_CALL,
)
from randomizer.types.npcs.fills.classes import (
    BossModelFill,
    RepeatableHenchmanFill,
    StatueFill,
    UniqueHenchmanFill,
)
from randomizer.types.overworld_scripts.constants.room_names import (
    R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM,
    R103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM,
    R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
    R177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM,
    R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
    R205_MUSHROOM_WAY_AREA_03,
    R206_BANDITS_WAY_AREA_05,
    R223_SMITHY_FACTORY_AREA_07_COUNT_DOWNS_ROOM,
    R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD,
    R254_BEAN_VALLEY_SMILAX_AREA,
    R255_MONSTRO_TOWN_JINXS_DOJO,
    R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR,
    R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM,
    R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM,
    R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE,
    R302_KERO_SEWERS_AREA_08_BELOMES_ROOM,
    R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH,
    R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM,
    R351_CULEXS_ROOM,
    R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
    R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
    R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM,
    R430_NIMBUS_LAND_OUTSIDE_DURING_VALENTINA,
    R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB,
    R469_FACTORY_GROUNDS_AREA_01,
    R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
    R471_FACTORY_GROUNDS_AREA_02,
    R472_FACTORY_GROUNDS_AREA_03,
    R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE,
)
from randomizer.types.progress_locations.classes import BossFightLocation, Inventory
from randomizer.types.progress_locations.enums import LocationWorldArea


class MushroomWayBossFight(BossFightLocation):
    _room_ids: List[int] = [R205_MUSHROOM_WAY_AREA_03]
    _name_enum: BossLocations = BossLocations.MushroomWay
    _battlefield = Battlefields.MushroomWay
    _music = BattleMusic.Boss1
    _world_area: LocationWorldArea = LocationWorldArea.MushroomWay

    _original_item: Type[Boss] = HammerBroBoss
    _overworld_boss_npc_fills: List[BossModelFill] = [MUSHROOM_WAY_2_BOSS_FILL]


class BanditsWayBossFight(BossFightLocation):
    _room_ids: List[int] = [R206_BANDITS_WAY_AREA_05]
    _name_enum: BossLocations = BossLocations.BanditsWay
    _battlefield = Battlefields.MushroomWay
    _music = BattleMusic.Boss1
    _world_area: LocationWorldArea = LocationWorldArea.BanditsWay

    _original_item: Type[Boss] = Croco1Boss
    _overworld_boss_npc_fills = [
        BANDITS_WAY_1_BOSS_FILL,
        BANDITS_WAY_2_BOSS_FILL,
        BANDITS_WAY_3_BOSS_FILL,
        BANDITS_WAY_4_BOSS_FILL,
        BANDITS_WAY_5_BOSS_FILL,
        ENDING_CREDITS_RACER,
    ]

    def is_vanilla(self) -> bool:
        return super().is_vanilla() or isinstance(self.contents, Croco2Boss)

    def can_access(self, inventory: Inventory):
        return can_access_bandits_way(self.world, inventory)


class MushroomKingdomBossFight(BossFightLocation):
    _room_ids: List[int] = [R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM]
    _name_enum: BossLocations = BossLocations.MushroomKingdom
    _battlefield = Battlefields.MushroomKingdomThroneRoom
    _music = BattleMusic.Boss2
    _world_area: LocationWorldArea = LocationWorldArea.MushroomKingdomOccupiedOnly

    _original_item: Type[Boss] = MackBoss
    _overworld_boss_npc_fills: List[BossModelFill] = [THRONE_ROOM_BOSS_FILL]
    _overworld_unique_henchmen_npc_fills: List[list[UniqueHenchmanFill]] = [
        [THRONE_ROOM_TOP_LEFT_HENCHMAN_FILL],
        [THRONE_ROOM_MID_LEFT_HENCHMAN_FILL],
        [THRONE_ROOM_MID_RIGHT_HENCHMAN_FILL],
        [THRONE_ROOM_TOP_RIGHT_HENCHMAN_FILL],
        [THRONE_ROOM_BOTTOM_LEFT_HENCHMAN_FILL],
        [THRONE_ROOM_BOTTOM_RIGHT_HENCHMAN_FILL],
    ]
    _overworld_generic_henchmen_npc_fills: List[list[RepeatableHenchmanFill]] = [
        [
            KINGDOM_EXTERIOR_NPC_HITTING_HOUSE_HENCHMAN_FILL,
            KINGDOM_EXTERIOR_NPC_TERRORIZING_GUARD_HENCHMAN_FILL,
            KINGDOM_ANTECHAMBER_LEFT_HENCHMAN_FILL,
            KINGDOM_MAIN_HALL_REPEATING_HENCHMAN_FILL_1,
            KINGDOM_MAIN_HALL_REPEATING_HENCHMAN_FILL_2,
            KINGDOM_MAIN_HALL_REPEATING_HENCHMAN_FILL_3,
            KINGDOM_MAIN_HALL_DOOR_GUARD_HENCHMAN_FILL,
            KINGDOM_MAIN_HALL_TERRORIZING_TOAD_HENCHMAN_FILL,
            KINGDOM_STAIRCASE_RIGHT_HENCHMAN_FILL,
            KINGDOM_RIGHT_HALL_RIGHT_HENCHMAN_FILL,
            KINGDOM_HOUSE_TABLE_HENCHMAN_FILL,
        ],
        [
            KINGDOM_EXTERIOR_RESPAWNING_HENCHMAN_1,
            KINGDOM_EXTERIOR_RESPAWNING_HENCHMAN_2,
            KINGDOM_EXTERIOR_RESPAWNING_HENCHMAN_3,
            KINGDOM_EXTERIOR_STANDING_HENCHMAN_FILL,
            KINGDOM_EXTERIOR_GRASS_HENCHMAN_FILL,
            KINGDOM_ANTECHAMBER_RIGHT_HENCHMAN_FILL,
            KINGDOM_STAIRCASE_LEFT_HENCHMAN_FILL,
            KINGDOM_RIGHT_HALL_LEFT_HENCHMAN_FILL,
            KINGDOM_BEDROOM_ANTECHAMBER_LEFT_HENCHMAN_FILL,
            KINGDOM_BEDROOM_ANTECHAMBER_RIGHT_HENCHMAN_FILL,
            KINGDOM_HOUSE_SINK_HENCHMAN_FILL,
            KINGDOM_HOUSE_BED_HENCHMAN_FILL,
        ],
    ]

    def can_access(self, inventory: Inventory):
        return can_defeat_bandits_way_boss(self.world, inventory)


class MimicFightLocation1(BossFightLocation):
    _identifier: int = 512
    _name_enum: BossLocations = BossLocations.Mimic1
    _original_item: Type[Boss] = PandoriteBoss

    def can_access(self, inventory: Inventory):
        return can_access_first_mimic(self.world, inventory)


class KeroSewersBossFight(BossFightLocation):
    _room_ids: List[int] = [R302_KERO_SEWERS_AREA_08_BELOMES_ROOM]
    _battlefield = Battlefields.KeroSewers
    _music = BattleMusic.Boss1
    _name_enum: BossLocations = BossLocations.KeroSewers
    _original_item: Type[Boss] = Belome1Boss
    _world_area: LocationWorldArea = LocationWorldArea.KeroSewers
    _overworld_boss_npc_fills: List[BossModelFill] = [SEWER_BOSS_ROOM_FILL]

    def is_vanilla(self) -> bool:
        return super().is_vanilla() or isinstance(self.contents, Belome2Boss)

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_sewer_boss(self.world, inventory)


class ForestBossFight(BossFightLocation):
    _room_ids: List[int] = [R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    _name_enum: BossLocations = BossLocations.ForestMaze
    _battlefield = Battlefields.Bowyer
    _music = BattleMusic.Boss2
    _original_item: Type[Boss] = BowyerBoss
    _world_area: LocationWorldArea = LocationWorldArea.ForestMaze
    _overworld_boss_npc_fills: List[BossModelFill] = [FOREST_BOSS_AREA_BOSS_FILL]
    _overworld_unique_henchmen_npc_fills: List[list[UniqueHenchmanFill]] = [
        [FOREST_MID_LEFT_HENCHMAN_FILL],
        [FOREST_MID_RIGHT_HENCHMAN_FILL],
        [FOREST_BOTTOM_LEFT_HENCHMAN_FILL],
        [FOREST_BOTTOM_RIGHT_HENCHMAN_FILL],
        [FOREST_TOP_LEFT_HENCHMAN_FILL],
        [FOREST_TOP_RIGHT_HENCHMAN_FILL],
        [FOREST_BOTTOM_MID_LEFT_HENCHMAN_FILL],
        [FOREST_BOTTOM_MID_RIGHT_HENCHMAN_FILL],
        [FOREST_TOP_MID_LEFT_HENCHMAN_FILL],
        [FOREST_TOP_MID_RIGHT_HENCHMAN_FILL],
    ]

    def can_access(self, inventory: Inventory):
        return can_access_forest_boss(self.world, inventory)


class MinesMidbossFight(BossFightLocation):
    _identifier: int = 518
    _name_enum: BossLocations = BossLocations.MinesMidboss
    _battlefield = Battlefields.MolevilleMines
    _music = BattleMusic.Boss1
    _original_item: Type[Boss] = Croco2Boss
    _world_area: LocationWorldArea = LocationWorldArea.MolevilleMines
    _overworld_boss_npc_fills: List[BossModelFill] = [
        MINES_CIRCLE_TRAMPOLINE_ROOM_BOSS_FILL,
        MINES_CIRCLE_LEFT_OF_TRAMPOLINE_ROOM_BOSS_FILL,
        MINES_CIRCLE_SMALL_ROOM_BOSS_FILL,
        MINES_CIRCLE_EXIT_ROOM_BOSS_FILL,
        MINES_CIRCLE_EXPLODED_ROOM,
        MINES_CIRCLE_PRE_EXPLODED_ROOM,
    ]
    _overworld_unique_henchmen_npc_fills: List[list[UniqueHenchmanFill]] = [
        [MINES_TRAMPOLINE_HENCHMAN_FILL],
        [MINES_LEFT_HENCHMAN_FILL],
        [MINES_RIGHT_HENCHMAN_FILL],
    ]

    def is_vanilla(self) -> bool:
        return super().is_vanilla() or isinstance(self.contents, Croco1Boss)

    def can_access(self, inventory: Inventory):
        return can_access_first_moleville_boss(self.world, inventory)


class MinesBossFight(BossFightLocation):
    _room_ids: List[int] = [R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    _name_enum: BossLocations = BossLocations.MinesEnd
    _battlefield = Battlefields.MolevilleMines
    _music = BattleMusic.Boss1
    _original_item: Type[Boss] = PunchinelloBoss
    _world_area: LocationWorldArea = LocationWorldArea.MolevilleMines
    _overworld_boss_npc_fills: List[BossModelFill] = [
        MINES_FINAL_BOSS_FILL,
    ]
    # should the bobombs be unique henchmen?
    _overworld_generic_henchmen_npc_fills: List[list[RepeatableHenchmanFill]] = [
        [  # needs special considerations for only tiny sprites
            MINES_BOSS_TINY_HENCHMAN_FILL_1,
            MINES_BOSS_TINY_HENCHMAN_FILL_2,
            MINES_BOSS_TINY_HENCHMAN_FILL_3,
        ],
        [  # check and see if cloning causes vram issues
            MINES_BOSS_BATTLE_HENCHMAN_FILL_1,
            MINES_BOSS_BATTLE_HENCHMAN_FILL_2,
            MINES_BOSS_BATTLE_HENCHMAN_FILL_3,
        ],
        [TOWER_SEESAW_CHEST_NPC_FILL],  # booster tower masher room because lol
    ]

    def can_access(self, inventory: Inventory):
        return can_access_second_moleville_boss(self.world, inventory)


class TowerCurtainRoomBossFight(BossFightLocation):
    _room_ids: List[int] = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _name_enum: BossLocations = BossLocations.TowerCurtain
    _battlefield = Battlefields.BoosterTower
    _music = BattleMusic.Boss1
    _original_item: Type[Boss] = BoosterBoss
    _world_area: LocationWorldArea = LocationWorldArea.BoosterTower
    _overworld_boss_npc_fills: List[BossModelFill] = [
        TOWER_CURTAIN_GAME_ROOM_BOSS_FILL,
        TOWER_BOSS_SANCTUARY_NPC_FILL,
        TOWER_ANCESTOR_GAME_MASTER_NPC_FILL,
        TOWER_BEHIND_BOBOMB_CURTAINS_BOSS_FILL,
        TOWER_BOSS_BOOSTER_HILL_FILL,
        TOWER_BOSS_FRONT_DOOR_FILL,
        TOWER_BOSS_FIRST_ROOM_BEHIND_DOORWAY_FILL,
        TOWER_BOSS_ON_BALCONY_FILL,
        TOWER_BOSS_ENDING_CREDITS_WEDDING_FILL,
    ]
    _overworld_unique_henchmen_npc_fills: List[list[UniqueHenchmanFill]] = [
        [
            TOWER_LOBBY_HENCHMAN_FILL,
            TOWER_CURTAIN_GAME_ROOM_HENCHMAN_1_FILL,
            CHAPEL_HENCHMAN_1_FILL,
            BOOSTER_HILL_LEFT_HENCHMAN_FILL,
            TOWER_BALCONY_HENCHMAN_1_FILL,
            ENDING_CREDITS_CHAPEL_HENCHMAN_1_FILL,
        ],
        [
            TOWER_TRAIN_ROOM_HENCHMAN_FILL,
            TOWER_CURTAIN_GAME_ROOM_HENCHMAN_2_FILL,
            CHAPEL_HENCHMAN_2_FILL,
            BOOSTER_HILL_MIDDLE_HENCHMAN_FILL,
            TOWER_BALCONY_HENCHMAN_2_FILL,
            ENDING_CREDITS_CHAPEL_HENCHMAN_2_FILL,
        ],
        [
            TOWER_BULLET_ROOM_HENCHMAN_FILL,
            TOWER_CURTAIN_GAME_ROOM_HENCHMAN_3_FILL,
            CHAPEL_HENCHMAN_3_FILL,
            BOOSTER_HILL_RIGHT_HENCHMAN_FILL,
            TOWER_BALCONY_HENCHMAN_3_FILL,
            ENDING_CREDITS_CHAPEL_HENCHMAN_3_FILL,
        ],
        [ENDING_CREDITS_CHAPEL_HENCHMAN_4_FILL],
        [ENDING_CREDITS_CHAPEL_HENCHMAN_5_FILL],
        [ENDING_CREDITS_CHAPEL_HENCHMAN_6_FILL],
        [ENDING_CREDITS_CHAPEL_HENCHMAN_7_FILL],
        [ENDING_CREDITS_CHAPEL_HENCHMAN_8_FILL],
    ]
    _overworld_generic_henchmen_npc_fills: List[list[RepeatableHenchmanFill]] = [
        [BOOSTER_PASS_APPRENTICE_FILL],
    ]

    def can_access(self, inventory: Inventory):
        return can_access_curtain_boss(self.world, inventory)


class TowerBalconyBossFight(BossFightLocation):
    _room_ids: List[int] = [R258_BOOSTER_TOWER_BALCONY_AT_TOP_FLOOR]
    _battlefield = Battlefields.ClownBros
    _music = BattleMusic.Boss1
    _name_enum: BossLocations = BossLocations.TowerBalcony
    _original_item: Type[Boss] = GrateGuyBoss
    _world_area: LocationWorldArea = LocationWorldArea.BoosterTower

    def can_access(self, inventory: Inventory):
        return can_access_balcony_boss(self.world, inventory)


class ChapelBossFight(BossFightLocation):
    _room_ids: List[int] = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _name_enum: BossLocations = BossLocations.Marrymore
    _battlefield = Battlefields.Bundt
    _music = BattleMusic.Boss1
    _original_item: Type[Boss] = BundtBoss
    _world_area: LocationWorldArea = LocationWorldArea.Marrymore
    _overworld_boss_npc_fills: List[BossModelFill] = [
        CHAPEL_KITCHEN_BOSS_FILL,
        CHAPEL_SANCTUARY_BOSS_FILL,
    ]
    _overworld_unique_henchmen_npc_fills: List[list[UniqueHenchmanFill]] = [
        [
            CHAPEL_KITCHEN_HENCHMAN_1_FILL,
            CHAPEL_SANCTUARY_HENCHMAN_1_FILL,
        ],
        [
            CHAPEL_KITCHEN_HENCHMAN_2_FILL,
            CHAPEL_SANCTUARY_HENCHMAN_2_FILL,
        ],
    ]

    def can_access(self, inventory: Inventory):
        return can_access_chapel_boss(self.world, inventory)


class ShipPasswordBossFight(BossFightLocation):
    _room_ids: List[int] = [R177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM]
    _battlefield = Battlefields.SunkenShip
    _music = BattleMusic.Boss1
    _name_enum: BossLocations = BossLocations.SunkenShipMidboss
    _world_area: LocationWorldArea = LocationWorldArea.SunkenShip
    _original_item: Type[Boss] = KingCalamariBoss
    _overworld_boss_npc_fills: List[BossModelFill] = [PASSWORD_ROOM_BECKON_BOSS_FILL]

    def can_access(self, inventory: Inventory):
        return can_access_ship_midboss(self.world, inventory)


class MimicFightLocation2(BossFightLocation):
    _identifier: int = 513
    _name_enum: BossLocations = BossLocations.Mimic2
    _original_item: Type[Boss] = HidonBoss

    def can_access(self, inventory: Inventory):
        return can_access_second_mimic(self.world, inventory)


class ShipFinalBossFight(BossFightLocation):
    _room_ids: List[int] = [R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM]
    _battlefield = Battlefields.SunkenShip
    _music = BattleMusic.Boss1
    _name_enum: BossLocations = BossLocations.SunkenShipEnd
    _original_item: Type[Boss] = JohnnyBoss
    _world_area: LocationWorldArea = LocationWorldArea.SunkenShip
    _overworld_boss_npc_fills: List[BossModelFill] = [
        SHIP_FINAL_ROOM_BOSS_FILL,
        SHIP_BOSS_ON_BEACH_FILL,
        ENDING_CREDITS_SHIP_BOSS_ON_CLIFF_FILL,
    ]
    _overworld_unique_henchmen_npc_fills: List[list[UniqueHenchmanFill]] = [
        [
            SHIP_MAIN_HENCHMAN_1_BOSS_ROOM_FILL,
            SHIP_MAIN_HENCHMAN_1_BEACH_FILL,
        ],
        [SHIP_MAIN_HENCHMAN_2_BOSS_ROOM_FILL, SHIP_MAIN_HENCHMAN_2_BEACH_FILL],
        [SHIP_MAIN_HENCHMAN_3_BOSS_ROOM_FILL],
        [SHIP_MAIN_HENCHMAN_4_BOSS_ROOM_FILL],
    ]
    _overworld_generic_henchmen_npc_fills: List[list[RepeatableHenchmanFill]] = [
        [
            SHIP_FIRST_FORCED_HENCHMAN_FIGHT_FILL_1,
            SHIP_FIRST_FORCED_HENCHMAN_FIGHT_FILL_2,
            SHIP_FIRST_FORCED_HENCHMAN_FIGHT_FILL_3,
            SHIP_FIRST_FORCED_HENCHMAN_FIGHT_FILL_4,
        ],
        [
            SHIP_SECOND_FORCED_HENCHMAN_FIGHT_FILL_1,
            SHIP_SECOND_FORCED_HENCHMAN_FIGHT_FILL_2,
        ],
    ]

    def can_access(self, inventory: Inventory):
        return can_defeat_ship_midboss(self.world, inventory)


class SeasideBeachBossFight(BossFightLocation):
    _room_ids: List[int] = [R315_SEASIDE_TOWN_DURING_YARIDOVICH_BEACH]
    _name_enum: BossLocations = BossLocations.SeasideTown
    _battlefield = Battlefields.Yaridovich
    _music = BattleMusic.Boss2
    _world_area: LocationWorldArea = LocationWorldArea.SeasideTown
    _original_item: Type[Boss] = YaridovichBoss
    _overworld_boss_npc_fills: List[BossModelFill] = [
        SEASIDE_HOUSE_BOSS_FILL,
        SEASIDE_CONFRONTATION_BOSS_FILL,
        SEASIDE_BEACH_BOSS_FILL_SMALL,
        SEASIDE_BOSS_TRANSFORMED_FILL,
    ]
    _overworld_unique_henchmen_npc_fills: List[list[UniqueHenchmanFill]] = [
        [
            SEASIDE_OUTSIDE_LEFT_GUARD,
            SEASIDE_BEACH_HENCHMAN_1_FILL,
        ],
        [
            SEASIDE_OUTSIDE_RIGHT_GUARD,
            SEASIDE_BEACH_HENCHMAN_2_FILL,
        ],
        [
            SEASIDE_CONFRONTATION_HENCHMAN_3_FILL,
            SEASIDE_INNKEEPER_1F_HENCHMAN_FILL,
            SEASIDE_INNKEEPER_2F_HENCHMAN_FILL,
            SEASIDE_BEACH_HENCHMAN_3_FILL,
        ],
        [
            SEASIDE_CONFRONTATION_HENCHMAN_4_FILL,
            SEASIDE_SHOPKEEPER_HENCHMAN_FILL,
            SEASIDE_BEACH_HENCHMAN_4_FILL,
        ],
    ]
    _overworld_generic_henchmen_npc_fills: List[list[RepeatableHenchmanFill]] = [
        [SEASIDE_CUSTOMER_HENCHMAN_FILL],
        [SEASIDE_LONG_SHOP_LEFT_HENCHMAN_FILL],
        [SEASIDE_LONG_SHOP_RIGHT_HENCHMAN_FILL],
        [SEASIDE_RIGHT_BUILDING_LEFT_DOOR_HENCHMAN_FILL],
        [SEASIDE_RIGHT_BUILDING_MIDDLE_DOOR_HENCHMAN_LOWER_FILL],
        [SEASIDE_RIGHT_BUILDING_MIDDLE_DOOR_HENCHMAN_UPPER_FILL],
        [SEASIDE_RIGHT_BUILDING_RIGHT_DOOR_HENCHMAN_FILL],
    ]

    def can_access(self, inventory: Inventory):
        return can_access_seaside_boss(self.world, inventory)


class LandsEndCloudBossFight(BossFightLocation):
    _identifier: int = 519
    _music = BattleMusic.Boss1
    _name_enum: BossLocations = BossLocations.LandsEndCloud
    _world_area: LocationWorldArea = LocationWorldArea.LandsEnd
    _original_item: Type[Boss] = MokuraBoss

    def can_access(self, inventory: Inventory):
        return can_access_lands_end_cloud(self.world, inventory)


class TempleBossFight(BossFightLocation):
    _room_ids: List[int] = [R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM]
    _name_enum: BossLocations = BossLocations.BelomeTemple
    _battlefield = Battlefields.BelomeTemple
    _music = BattleMusic.Boss1
    _original_item: Type[Boss] = Belome2Boss
    _world_area: LocationWorldArea = LocationWorldArea.BelomeTemple
    _overworld_boss_npc_fills: List[BossModelFill] = [TEMPLE_BOSS_FILL]

    def is_vanilla(self) -> bool:
        return super().is_vanilla() or isinstance(self.contents, Belome1Boss)

    def can_access(self, inventory: Inventory):
        return can_access_temple_boss(self.world, inventory)


class DojoFirstFight(BossFightLocation):
    _room_ids: List[int] = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _name_enum: BossLocations = BossLocations.Dojo1
    _battlefield = Battlefields.JinxDojo
    _can_run_away: bool = True
    _original_item: Type[Boss] = JaggerBoss
    _world_area: LocationWorldArea = LocationWorldArea.MonstroTown
    _overworld_boss_npc_fills: List[BossModelFill] = [DOJO_FIRST_BOSS_FILL]

    def can_access(self, inventory: Inventory):
        return can_access_first_dojo_boss(self.world, inventory)


class DojoSecondFight(BossFightLocation):
    _identifier: int = 515
    _name_enum: BossLocations = BossLocations.Dojo2
    _battlefield = Battlefields.JinxDojo
    _can_run_away: bool = True
    _music = BattleMusic.Boss1
    _world_area: LocationWorldArea = LocationWorldArea.MonstroTown
    _original_item: Type[Boss] = Jinx1Boss
    _overworld_boss_npc_fills: List[BossModelFill] = [DOJO_SECOND_BOSS_FILL]

    def is_vanilla(self) -> bool:
        return (
            super().is_vanilla()
            or isinstance(self.contents, Jinx2Boss)
            or isinstance(self.contents, Jinx3Boss)
        )

    def can_access(self, inventory: Inventory):
        return can_access_second_dojo_boss(self.world, inventory)


class DojoThirdFight(BossFightLocation):
    _identifier: int = 516
    _name_enum: BossLocations = BossLocations.Dojo3
    _battlefield = Battlefields.JinxDojo
    _can_run_away: bool = True
    _music = BattleMusic.Boss1
    _world_area: LocationWorldArea = LocationWorldArea.MonstroTown
    _original_item: Type[Boss] = Jinx2Boss
    _overworld_boss_npc_fills: List[BossModelFill] = [DOJO_THIRD_BOSS_FILL]

    def is_vanilla(self) -> bool:
        return (
            super().is_vanilla()
            or isinstance(self.contents, Jinx1Boss)
            or isinstance(self.contents, Jinx3Boss)
        )

    def can_access(self, inventory: Inventory):
        return can_access_third_dojo_boss(self.world, inventory)


class DojoFourthFight(BossFightLocation):
    _identifier: int = 517
    _name_enum: BossLocations = BossLocations.Dojo4
    _battlefield = Battlefields.JinxDojo
    _can_run_away: bool = True
    _music = BattleMusic.Boss1
    _world_area: LocationWorldArea = LocationWorldArea.MonstroTown
    _original_item: Type[Boss] = Jinx3Boss
    _overworld_boss_npc_fills: List[BossModelFill] = [DOJO_FOURTH_BOSS_FILL]

    def is_vanilla(self) -> bool:
        return (
            super().is_vanilla()
            or isinstance(self.contents, Jinx2Boss)
            or isinstance(self.contents, Jinx2Boss)
        )

    def can_access(self, inventory: Inventory):
        return can_access_fourth_dojo_boss(self.world, inventory)


class MonstroSealedDoorBossFight(BossFightLocation):
    _room_ids: List[int] = [R351_CULEXS_ROOM]
    _name_enum: BossLocations = BossLocations.MonstroDoor
    _battlefield = Battlefields.Culex
    _music = BattleMusic.Culex
    _original_item: Type[Boss] = CulexBoss
    _world_area: LocationWorldArea = LocationWorldArea.MonstroTown
    _overworld_boss_npc_fills: List[BossModelFill] = [MONSTRO_SEALED_DOOR_BOSS_FILL]

    def can_access(self, inventory: Inventory):
        return can_access_sealed_door_boss(self.world, inventory)


class MimicFightLocation3(BossFightLocation):
    _identifier: int = 514
    _name_enum: BossLocations = BossLocations.Mimic3
    _original_item: Type[Boss] = BoxBoyBoss

    def can_access(self, inventory: Inventory):
        return can_access_third_mimic(self.world, inventory)


class BeanValleyPlanterBossFight(BossFightLocation):
    _room_ids: List[int] = [R254_BEAN_VALLEY_SMILAX_AREA]
    _name_enum: BossLocations = BossLocations.BeanValley
    _battlefield = Battlefields.BeanValley
    _music = BattleMusic.Boss1
    _original_item: Type[Boss] = MegaSmilaxBoss
    _world_area: LocationWorldArea = LocationWorldArea.BeanValley
    _overworld_boss_npc_fills: List[BossModelFill] = [BEAN_VALLEY_BOSS_FILL]

    def can_access(self, inventory: Inventory):
        return can_access_valley_boss(self.world, inventory)


class StatueRoomBossFight(BossFightLocation):
    _name_enum: BossLocations = BossLocations.NimbusStatues
    _identifier: int = 520
    _battlefield = Battlefields.NimbusCastle
    _music = BattleMusic.Boss1
    _original_item: Type[Boss] = DodoBoss
    _world_area: LocationWorldArea = LocationWorldArea.NimbusCastle
    _overworld_boss_npc_fills: List[BossModelFill] = [
        STATUE_ROOM_BOSS_FILL,
        ENDING_CREDITS_CHAPEL_PASTOR_FILL,
        STATUE_POLISHER_FILL,
        END_OF_NIMBUS_HALLWAY_BOSS_FILL,
    ]

    def can_access(self, inventory: Inventory):
        return can_access_statue_boss(self.world, inventory)


class GiantEggBossFight(BossFightLocation):
    _room_ids: List[int] = [R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM]
    _name_enum: BossLocations = BossLocations.GiantEgg
    _battlefield = Battlefields.Birdetta
    _music = BattleMusic.Boss1
    _world_area: LocationWorldArea = LocationWorldArea.NimbusCastle
    _affected_dialog_ids: List[int] = [DI0049_NIMBUS_EGG_BOSS_TALK_AFTER_WINNING]
    _original_item: Type[Boss] = BirdettaBoss

    def can_access(self, inventory: Inventory):
        return can_access_egg_boss(self.world, inventory)

    def can_accept(self, item: Boss, inventory: Optional[Inventory] = None) -> bool:
        return (
            super().can_accept(item, inventory)
            and item.forced_background is None
            and item
            not in [
                MackBoss,
                Belome1Boss,
                BowyerBoss,
                GrateGuyBoss,
                JohnnyBoss,
                YaridovichBoss,
                Belome2Boss,
                CulexBoss,
                BoxBoyBoss,
                DodoBoss,
                ValentinaBoss,
                CzarBoss,
                ChesterBoss,
                KamekBoss,
                BoomerBoss,
                ClerkBoss,
                ManagerBoss,
                DirectorBoss,
                GunyolkBoss,
            ]
        )

    def set_contents(self, contents: Boss) -> None:
        super().set_contents(contents)

        if not self.is_vanilla():
            # Don't show the egg fragment in front if not vanilla.
            bank: AnimationScriptBank = (
                self.world.monsters_attacks_and_items_animation_scripts.get_bank(
                    SUBROUTINES_0X3A8BE4
                )
            )
            jump_command = Jmp(["after_shelly_egg"], identifier="queuestart_0x3a8c05")
            bank.replace_command_by_name("queuestart_0x3a8c05", jump_command)
            # fill space to make sure no subroutine addresses shift
            for _ in range(0, 5):
                bank.scripts[0].insert_after_identifier(
                    "queuestart_0x3a8c05", Pause1Frame()
                )

            # Add Shelly to the formation.

            assert contents.pack_number is not None
            pack = self.world.packs[contents.pack_number]
            assert pack is not None
            formation = self.world.formations[pack.formation_id]
            assert formation is not None

            visible_at_start_ids = [
                i
                for (i, member) in enumerate(formation.members)
                if member is not None and not member.hidden_at_start
            ]
            for member in formation.members:
                if member is not None:
                    member.set_hidden_at_start(True)
            event_to_run = formation.run_event_at_load
            formation.set_run_event_at_load(None)

            index_for_shelly = formation.members.index(None)
            formation.members[index_for_shelly] = FormationMember(
                Shelly, x_pos=171, y_pos=103, include_in_stat_totaling=False
            )

            script = self.world.monster_scripts.scripts[Shelly().monster_id]
            call_options = [
                MONSTER_1_CALL,
                MONSTER_2_CALL,
                MONSTER_3_CALL,
                MONSTER_4_CALL,
                MONSTER_5_CALL,
                MONSTER_6_CALL,
                MONSTER_7_CALL,
                MONSTER_8_CALL,
            ]

            new_summon_command = CallTarget(
                call_options[visible_at_start_ids[0]], identifier="shelly_summon"
            )
            script.replace_by_name("shelly_summon", new_summon_command)
            for num, monster in enumerate(visible_at_start_ids):
                if num == 0:
                    continue
                new_summon_command = CallTarget(call_options[monster])
                script.insert_after_identifier("shelly_summon", new_summon_command)
            if event_to_run is not None:
                script.insert_before_identifier(
                    "shelly_summon", RunBattleEvent(event_to_run)
                )

            # Remove eggshell from Birdetta if she's not in the vanilla location.
            birdetta_formation = self.world.formations[FORM0297_BIRDETTA_BOSS_FIGHT]
            assert birdetta_formation is not None
            assert birdetta_formation.members[0] is not None
            birdetta_formation.members[0].set_hidden_at_start(False)
            birdetta_formation.members[1] = None


class NimbusFinalBossFight(BossFightLocation):
    _room_ids: List[int] = [R430_NIMBUS_LAND_OUTSIDE_DURING_VALENTINA]
    _name_enum: BossLocations = BossLocations.NimbusEnd
    _battlefield = Battlefields.Valentina
    _music = BattleMusic.Boss1
    _original_item: Type[Boss] = ValentinaBoss
    _world_area: LocationWorldArea = LocationWorldArea.NimbusCastle
    _overworld_boss_npc_fills: List[BossModelFill] = [
        NIMBUS_CONFRONTATION_BOSS_FILL,
        NIMBUS_BOSS_ON_BALCONY_FILL,
        ENDING_CREDITS_CHAPEL_NIMBUS_BOSS_FILL,
    ]
    _statue_fills: List[StatueFill] = [
        GARRO_LEFT_STATUE_FILL,
        GARRO_MID_STATUE_FILL,
        GARRO_RIGHT_STATUE_FILL,
        NIMBUS_MAIN_HALL_LEFT_SOUTHFACING_STATUE_FILL,
        NIMBUS_MAIN_HALL_MID_SOUTHFACING_STATUE_FILL,
        NIMBUS_MAIN_HALL_RIGHT_SOUTHFACING_STATUE_FILL,
        NIMBUS_MAIN_HALL_LEFT_NORTHFACING_STATUE_FILL,
        NIMBUS_MAIN_HALL_MID_NORTHFACING_STATUE_FILL,
        NIMBUS_MAIN_HALL_RIGHT_NORTHFACING_STATUE_FILL,
        NIMBUS_OCCUPIED_4PATH_SOUTHFACING_STATUE,
        NIMBUS_OCCUPIED_4PATH_NORTHFACING_STATUE,
        NIMBUS_ANTECHAMBER_SOUTHFACING_STATUE,
        NIMBUS_ANTECHAMBER_NORTHFACING_STATUE,
        NIMBUS_OCCUPIED_THRONE_ROOM_SOUTHFACING_STATUE,
        NIMBUS_OCCUPIED_THRONE_ROOM_NORTHFACING_STATUE,
        NIMBUS_POLISHING_ROOM_LEFT_STATUE,
        NIMBUS_POLISHING_ROOM_MID_STATUE,
        NIMBUS_POLISHING_ROOM_RIGHT_STATUE,
        NIMBUS_LONE_STATUE,
        NIMBUS_LEFT_SHAMAN_HALL_SOUTHFACING_STATUE,
        NIMBUS_LEFT_SHAMAN_HALL_NORTHFACING_STATUE,
        NIMBUS_RIGHT_SHAMAN_HALL_SOUTHFACING_STATUE,
        NIMBUS_RIGHT_SHAMAN_HALL_NORTHFACING_STATUE,
        NIMBUS_LIBERATED_THRONE_ROOM_SOUTHFACING_STATUE,
        NIMBUS_LIBERATED_THRONE_ROOM_NORTHFACING_STATUE,
        HOT_SPRINGS_LEFT_SOUTHFACING_STATUE,
        HOT_SPRINGS_RIGHT_SOUTHFACING_STATUE,
        HOT_SPRINGS_RIGHT_NORTHFACING_STATUE,
        HOT_SPRINGS_LEFT_NORTHFACING_STATUE,
        NIMBUS_CELLAR_HALLWAY_LEFT_STATUE,
        NIMBUS_CELLAR_HALLWAY_RIGHT_STATUE,
        NIMBUS_FIVEDOOR_HALLWAY_LEFT_SOUTHFACING_STATUE,
        NIMBUS_FIVEDOOR_HALLWAY_RIGHT_NORTHFACING_STATUE,
        NIMBUS_FIVEDOOR_HALLWAY_LEFT_NORTHFACING_STATUE,
        NIMBUS_FIVEDOOR_HALLWAY_RIGHT_SOUTHFACING_STATUE,
        NIMBUS_LIBERATED_4PATH_SOUTHFACING_STATUE,
        NIMBUS_LIBERATED_4PATH_NORTHFACING_STATUE,
    ]
    _overworld_generic_henchmen_npc_fills: List[list[RepeatableHenchmanFill]] = [
        [
            NIMBUS_BACKDOOR_HALLWAY_1_LEFT_HENCHMAN_FILL,
        ],
        [
            NIMBUS_BACKDOOR_HALLWAY_1_RIGHT_HENCHMAN_FILL,
            NIMBUS_BACKDOOR_HALLWAY_2_FIRST_HENCHMAN_FILL,
        ],
        [
            NIMBUS_BACKDOOR_HALLWAY_2_SECOND_HENCHMAN_FILL,
            NIMBUS_BACKDOOR_HALLWAY_2_FOURTH_HENCHMAN_FILL,
            NIMBUS_BACKDOOR_HALLWAY_2_THIRD_HENCHMAN_FILL,
            NIMBUS_BACKDOOR_HALLWAY_3_FIRST_HENCHMAN_FILL,
            NIMBUS_BACKDOOR_HALLWAY_3_SECOND_HENCHMAN_FILL,
        ],
    ]

    def can_access(self, inventory: Inventory):
        return can_access_nimbus_boss(self.world, inventory)


class VolcanoBridgeBossFight(BossFightLocation):
    _room_ids: List[int] = [R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM]
    _name_enum: BossLocations = BossLocations.BarrelVolcanoMidboss
    _battlefield = Battlefields.CzarDragon
    _music = BattleMusic.Boss1
    _world_area: LocationWorldArea = LocationWorldArea.BarrelVolcano
    _original_item: Type[Boss] = CzarBoss
    _overworld_boss_npc_fills: List[BossModelFill] = [VOLCANO_BRIDGE_BOSS_FILL]
    _overworld_generic_henchmen_npc_fills: List[list[RepeatableHenchmanFill]] = [
        [
            VOLCANO_BRIDGE_ASSEMBLER_HENCHMAN_1_FILL,
            VOLCANO_BRIDGE_ASSEMBLER_HENCHMAN_2_FILL,
            VOLCANO_BRIDGE_ASSEMBLER_HENCHMAN_3_FILL,
            VOLCANO_BRIDGE_ASSEMBLER_HENCHMAN_4_FILL,
            VOLCANO_BRIDGE_ASSEMBLER_HENCHMAN_5_FILL,
            VOLCANO_BRIDGE_ASSEMBLER_HENCHMAN_6_FILL,
            VOLCANO_BRIDGE_ASSEMBLER_HENCHMAN_7_FILL,
            VOLCANO_BRIDGE_ASSEMBLER_HENCHMAN_8_FILL,
        ]
    ]

    def can_access(self, inventory: Inventory):
        return can_access_volcano_midboss(self.world, inventory)


class VolcanoExitBossFight(BossFightLocation):
    _room_ids: List[int] = [R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP]
    _name_enum: BossLocations = BossLocations.BarrelVolcanoEnd
    _battlefield = Battlefields.AxemRangers
    _music = BattleMusic.Boss2
    _world_area: LocationWorldArea = LocationWorldArea.BarrelVolcano
    _original_item: Type[Boss] = AxemRangersBoss
    _overworld_boss_npc_fills: List[BossModelFill] = [
        VOLCANO_BOSS_FINAL_STAIRCASE_FILL,
        VOLCANO_BOSS_TELEPORT_FILL,
        VOLCANO_BOSS_TRAMPOLINE_FILL,
    ]
    _overworld_unique_henchmen_npc_fills: List[list[UniqueHenchmanFill]] = [
        [
            VOLCANO_FIRST_HENCHMAN_FINAL_STAIRCASE_FILL,
            VOLCANO_FIRST_HENCHMAN_TINY_ROOM_FILL,
            VOLCANO_FIRST_HENCHMAN_TRAMPOLINE_FILL,
        ],
        [
            VOLCANO_SECOND_HENCHMAN_FINAL_STAIRCASE_FILL,
            VOLCANO_SECOND_HENCHMAN_TRAMPOLINE_FILL,
        ],
        [
            VOLCANO_THIRD_HENCHMAN_FINAL_STAIRCASE_FILL,
            VOLCANO_THIRD_HENCHMAN_TRAMPOLINE_FILL,
            VOLCANO_THIRD_HENCHMAN_TELEPORT_FILL,
        ],
        [
            VOLCANO_FOURTH_HENCHMAN_FINAL_STAIRCASE_FILL,
            VOLCANO_FOURTH_HENCHMAN_TELEPORT_FILL,
            VOLCANO_FOURTH_HENCHMAN_TRAMPOLINE_FILL,
        ],
    ]

    def can_access(self, inventory: Inventory):
        return can_defeat_volcano_boss(self.world, inventory)


class ObstacleCourseFinalFight(BossFightLocation):
    _room_ids: List[int] = [R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB]
    _name_enum: BossLocations = BossLocations.BowsersKeepObstacles
    _battlefield = Battlefields.BowsersKeep
    _original_item: Type[Boss] = ChesterBoss
    _world_area: LocationWorldArea = LocationWorldArea.BowsersKeep
    _overworld_boss_npc_fills: List[BossModelFill] = [
        KEEP_OBSTACLE_ROOM_FINAL_FIGHT_FILL
    ]

    def can_access(self, inventory: Inventory):
        return can_access_battle_door_boss(self.world, inventory)


class KeepAfterObstaclesBossFight(BossFightLocation):
    _room_ids: List[int] = [R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM]
    _name_enum: BossLocations = BossLocations.BowsersKeepMidboss
    _battlefield = Battlefields.BowsersKeep
    _music = BattleMusic.Boss1
    _world_area: LocationWorldArea = LocationWorldArea.BowsersKeep
    _original_item: Type[Boss] = KamekBoss
    _overworld_boss_npc_fills: List[BossModelFill] = [
        KEEP_MIDBOSS_LAIR_FILL,  # may need to remove palette setter if not magikoopa, may need special animation when summoning
        KEEP_BATTLE_ROOM_1_END_BOSS_FILL,
        KEEP_BATTLE_ROOM_2_END_BOSS_FILL,
        KEEP_BATTLE_ROOM_3_END_BOSS_FILL,
        KEEP_BATTLE_ROOM_4_END_BOSS_FILL,
        KEEP_BATTLE_ROOM_5_END_BOSS_FILL,
        KEEP_BATTLE_ROON_6_END_BOSS_FILL,
        ENDING_CREDITS_KEEP_BOSS_CASTLE_REPAIR,
    ]

    def can_access(self, inventory: Inventory):
        return can_access_post_obstacle_boss(self.world, inventory)


class KeepChandelierBossFight(BossFightLocation):
    _identifier: int = 521
    _name_enum: BossLocations = BossLocations.BowsersKeepEnd1
    _battlefield = Battlefields.Boomer
    _music = BattleMusic.Boss1
    _world_area: LocationWorldArea = LocationWorldArea.BowsersKeep
    _original_item: Type[Boss] = BoomerBoss
    _overworld_boss_npc_fills: List[BossModelFill] = [KEEP_CHANDELIER_BOSS_FILL]

    def can_access(self, inventory: Inventory):
        return can_access_keep_chandelier_boss(self.world, inventory)


class KeepFinalBossFight(BossFightLocation):
    _identifier: int = 522
    _name_enum: BossLocations = BossLocations.BowsersKeepEnd2
    _battlefield = Battlefields.BowsersKeep
    _music = BattleMusic.Boss2
    _world_area: LocationWorldArea = LocationWorldArea.BowsersKeep
    _original_item: Type[Boss] = ExorBoss

    def can_access(self, inventory: Inventory):
        return can_access_keep_exit_boss(self.world, inventory)


class FactoryEntranceBoss(BossFightLocation):
    _room_ids: List[int] = [R223_SMITHY_FACTORY_AREA_07_COUNT_DOWNS_ROOM]
    _name_enum: BossLocations = BossLocations.FactoryMidboss
    _battlefield = Battlefields.Gate
    _music = BattleMusic.Boss1
    _world_area: LocationWorldArea = LocationWorldArea.Factory
    _original_item: Type[Boss] = CountdownBoss
    _overworld_boss_npc_fills: List[BossModelFill] = [FACTORY_CLOCK_BOSS_FILL]
    _overworld_generic_henchmen_npc_fills: List[list[RepeatableHenchmanFill]] = [
        [
            FACTORY_CLOCK_LEFT_HENCHMAN_FILL,
            FACTORY_CLOCK_RIGHT_HENCHMAN_FILL,
        ]
    ]

    def can_access(self, inventory: Inventory):
        return can_defeat_first_factory_boss(self.world, inventory)


class FactoryTransitionBoss(BossFightLocation):
    _room_ids: List[int] = [R103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM]
    _name_enum: BossLocations = BossLocations.FactoryEnd
    _battlefield = Battlefields.Gate
    _music = BattleMusic.Boss1
    _original_item: Type[Boss] = CloakerDominoBoss
    _world_area: LocationWorldArea = LocationWorldArea.Factory

    def can_access(self, inventory: Inventory):
        return can_access_second_factory_boss(self.world, inventory)


class InnerFactoryFirstFight(BossFightLocation):
    _room_ids: List[int] = [R469_FACTORY_GROUNDS_AREA_01]
    _name_enum: BossLocations = BossLocations.InnerFactory1
    _battlefield = Battlefields.Factory
    _world_area: LocationWorldArea = LocationWorldArea.InnerFactory
    _original_item: Type[Boss] = ClerkBoss
    _overworld_boss_npc_fills: List[BossModelFill] = [INNER_FACTORY_FIRST_BOSS_FILL]
    _overworld_generic_henchmen_npc_fills: List[list[RepeatableHenchmanFill]] = [
        [
            INNER_FACTORY_FIRST_BOSS_RIGHT_HENCHMAN,
            INNER_FACTORY_FIRST_BOSS_LEFT_HENCHMAN,
        ]
    ]

    def can_access(self, inventory: Inventory):
        return can_access_inner_factory_first_boss(self.world, inventory)


class InnerFactorySecondFight(BossFightLocation):
    _room_ids: List[int] = [R471_FACTORY_GROUNDS_AREA_02]
    _name_enum: BossLocations = BossLocations.InnerFactory2
    _battlefield = Battlefields.Factory
    _world_area: LocationWorldArea = LocationWorldArea.InnerFactory
    _original_item: Type[Boss] = ManagerBoss
    _overworld_boss_npc_fills: List[BossModelFill] = [INNER_FACTORY_SECOND_BOSS_FILL]
    _overworld_unique_henchmen_npc_fills: List[list[UniqueHenchmanFill]] = [
        [INNER_FACTORY_SECOND_BOSS_LEFT_HENCHMAN],
        [
            INNER_FACTORY_SECOND_BOSS_MID_HENCHMAN,
        ],
        [INNER_FACTORY_SECOND_BOSS_RIGHT_HENCHMAN],
    ]

    def can_access(self, inventory: Inventory):
        return can_access_inner_factory_second_boss(self.world, inventory)


class InnerFactoryThirdFight(BossFightLocation):
    _room_ids: List[int] = [R472_FACTORY_GROUNDS_AREA_03]
    _name_enum: BossLocations = BossLocations.InnerFactory3
    _battlefield = Battlefields.Factory
    _world_area: LocationWorldArea = LocationWorldArea.InnerFactory
    _original_item: Type[Boss] = DirectorBoss
    _overworld_boss_npc_fills: List[BossModelFill] = [INNER_FACTORY_THIRD_BOSS_FILL]
    _overworld_unique_henchmen_npc_fills: List[list[UniqueHenchmanFill]] = [
        [INNER_FACTORY_LEFT_ASSEMBLER],
        [INNER_FACTORY_MID_ASSEMBLER],
        [INNER_FACTORY_RIGHT_ASSEMBLER],
    ]

    def can_access(self, inventory: Inventory):
        return can_access_inner_factory_third_boss(self.world, inventory)


class InnerFactoryFourthFight(BossFightLocation):
    _room_ids: List[int] = [R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM]
    _name_enum: BossLocations = BossLocations.InnerFactory4
    _battlefield = Battlefields.Factory
    _world_area: LocationWorldArea = LocationWorldArea.InnerFactory
    _music = BattleMusic.Boss1
    _original_item: Type[Boss] = GunyolkBoss
    _overworld_boss_npc_fills: List[BossModelFill] = [INNER_FACTORY_FOURTH_BOSS_FILL]
    _overworld_unique_henchmen_npc_fills: List[list[UniqueHenchmanFill]] = [
        [INNER_FACTORY_FOURTH_BOSS_HENCHMAN_FILL],
    ]

    def can_access(self, inventory: Inventory):
        return can_access_inner_factory_fourth_boss(self.world, inventory)


class FinalBossFight(BossFightLocation):
    _room_ids: List[int] = [R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE]
    _name_enum: BossLocations = BossLocations.InnerFactoryLair
    _battlefield = Battlefields.Smithy
    _world_area: LocationWorldArea = LocationWorldArea.InnerFactory
    _music = BattleMusic.Smithy
    _original_item: Type[Boss] = SmithyBoss
    # hide all other parts of smithy if shuffled
    _overworld_boss_npc_fills: List[BossModelFill] = [FINAL_FACTORY_BOSS_FILL]
    _overworld_generic_henchmen_npc_fills: List[list[RepeatableHenchmanFill]] = [
        [
            INNER_FACTORY_1_POST_DEFEAT_CONVEYOR_HENCHMAN_1_FILL,
            INNER_FACTORY_1_POST_DEFEAT_CONVEYOR_HENCHMAN_2_FILL,
            INNER_FACTORY_1_POST_DEFEAT_CONVEYOR_HENCHMAN_3_FILL,
            INNER_FACTORY_1_POST_DEFEAT_CONVEYOR_HENCHMAN_4_FILL,
            INNER_FACTORY_1_POST_DEFEAT_CONVEYOR_HENCHMAN_5_FILL,
            INNER_FACTORY_1_POST_DEFEAT_CONVEYOR_HENCHMAN_6_FILL,
            INNER_FACTORY_1_CONVEYOR_HENCHMAN_1_FILL,
            INNER_FACTORY_1_CONVEYOR_HENCHMAN_2_FILL,
            INNER_FACTORY_1_CONVEYOR_HENCHMAN_3_FILL,
            INNER_FACTORY_1_CONVEYOR_HENCHMAN_4_FILL,
            INNER_FACTORY_1_CONVEYOR_HENCHMAN_5_FILL,
            INNER_FACTORY_1_CONVEYOR_HENCHMAN_6_FILL,
            INNER_FACTORY_4_CONVEYOR_HENCHMAN_1_FILL,
            INNER_FACTORY_4_CONVEYOR_HENCHMAN_2_FILL,
            INNER_FACTORY_4_CONVEYOR_HENCHMAN_3_FILL,
            INNER_FACTORY_4_CONVEYOR_HENCHMAN_4_FILL,
            INNER_FACTORY_4_CONVEYOR_HENCHMAN_5_FILL,
            INNER_FACTORY_4_CONVEYOR_HENCHMAN_6_FILL,
            INNER_FACTORY_2_CONVEYOR_HENCHMAN_1_FILL,
            INNER_FACTORY_2_CONVEYOR_HENCHMAN_2_FILL,
            INNER_FACTORY_2_CONVEYOR_HENCHMAN_3_FILL,
            INNER_FACTORY_2_CONVEYOR_HENCHMAN_4_FILL,
            INNER_FACTORY_2_CONVEYOR_HENCHMAN_5_FILL,
            INNER_FACTORY_2_CONVEYOR_HENCHMAN_6_FILL,
            INNER_FACTORY_2_CONVEYOR_HENCHMAN_7_FILL,
            INNER_FACTORY_2_CONVEYOR_HENCHMAN_8_FILL,
            INNER_FACTORY_2_CONVEYOR_HENCHMAN_9_FILL,
            INNER_FACTORY_2_CONVEYOR_HENCHMAN_10_FILL,
            INNER_FACTORY_2_CONVEYOR_HENCHMAN_11_FILL,
            INNER_FACTORY_2_CONVEYOR_HENCHMAN_12_FILL,
            INNER_FACTORY_3_CONVEYOR_HENCHMAN_1_FILL,
            INNER_FACTORY_3_CONVEYOR_HENCHMAN_2_FILL,
            INNER_FACTORY_3_CONVEYOR_HENCHMAN_3_FILL,
            INNER_FACTORY_3_CONVEYOR_HENCHMAN_4_FILL,
            INNER_FACTORY_3_CONVEYOR_HENCHMAN_5_FILL,
            INNER_FACTORY_3_CONVEYOR_HENCHMAN_6_FILL,
        ]
    ]

    def can_access(self, inventory: Inventory):
        return can_access_inner_factory_final_boss(self.world, inventory)


# ********************* Default lists for the world.


def get_default_overworld_boss_npc_fills(world):
    """Get default boss locations.

    Args:
        world (randomizer.logic.main.GameWorld):

    Returns:
        list[BossAndStarLocation]: List of default boss locations.

    """
    return [
        MushroomWayBossFight(world),
        BanditsWayBossFight(world),
        MushroomKingdomBossFight(world),
        MimicFightLocation1(world),
        KeroSewersBossFight(world),
        ForestBossFight(world),
        MinesMidbossFight(world),
        MinesBossFight(world),
        TowerCurtainRoomBossFight(world),
        TowerBalconyBossFight(world),
        ChapelBossFight(world),
        ShipPasswordBossFight(world),
        MimicFightLocation2(world),
        ShipFinalBossFight(world),
        SeasideBeachBossFight(world),
        LandsEndCloudBossFight(world),
        TempleBossFight(world),
        DojoFirstFight(world),
        DojoSecondFight(world),
        DojoThirdFight(world),
        DojoFourthFight(world),
        MonstroSealedDoorBossFight(world),
        MimicFightLocation3(world),
        BeanValleyPlanterBossFight(world),
        StatueRoomBossFight(world),
        GiantEggBossFight(world),
        NimbusFinalBossFight(world),
        VolcanoBridgeBossFight(world),
        VolcanoExitBossFight(world),
        ObstacleCourseFinalFight(world),
        KeepAfterObstaclesBossFight(world),
        KeepChandelierBossFight(world),
        KeepFinalBossFight(world),
        FactoryEntranceBoss(world),
        FactoryTransitionBoss(world),
        InnerFactoryFirstFight(world),
        InnerFactorySecondFight(world),
        InnerFactoryThirdFight(world),
        InnerFactoryFourthFight(world),
        FinalBossFight(world),
    ]
