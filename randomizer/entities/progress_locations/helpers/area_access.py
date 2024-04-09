"""Helper methods that calculate if the player can access a given area based on their inventory
and settings."""

from typing import Callable, List, Type, Union

from randomizer.entities.bosses import (
    AxemRangersBoss,
    Belome2Boss,
    BowyerBoss,
    BundtBoss,
    ExorBoss,
    GrateGuyBoss,
    HammerBroBoss,
    JohnnyBoss,
    PunchinelloBoss,
    ValentinaBoss,
    YaridovichBoss,
)
from randomizer.entities.items import (
    BambinoBomb,
    BrightCard,
    Brooch,
    CastleKey1,
    CastleKey2,
    Crown,
    Fireworks,
    MimicFightInitiator1,
    MimicFightInitiator2,
    MimicFightInitiator3,
    ProgressiveFireworks,
    Ring,
    Shoes,
)
from randomizer.entities.items.items import CricketPie
from randomizer.entities.progress_locations import (
    BanditsWayBossFight,
    BeanValleyPlanterBossFight,
    ChapelBossFight,
    DojoFirstFight,
    DojoFourthFight,
    DojoSecondFight,
    DojoThirdFight,
    FactoryEntranceBoss,
    FactoryTransitionBoss,
    FinalBossFight,
    ForestBossFight,
    GiantEggBossFight,
    InnerFactoryFirstFight,
    InnerFactoryFourthFight,
    InnerFactorySecondFight,
    InnerFactoryThirdFight,
    KeepAfterObstaclesBossFight,
    KeepChandelierBossFight,
    KeepFinalBossFight,
    KeroSewersBossFight,
    LandsEndCloudBossFight,
    MinesBossFight,
    MinesMidbossFight,
    MushroomKingdomBossFight,
    MushroomWayBossFight,
    NimbusFinalBossFight,
    ObstacleCourseFinalFight,
    SeasideBeachBossFight,
    ShipFinalBossFight,
    ShipPasswordBossFight,
    StatueRoomBossFight,
    TempleBossFight,
    TowerBalconyBossFight,
    TowerCurtainRoomBossFight,
    VolcanoBridgeBossFight,
    VolcanoExitBossFight,
)
from randomizer.entities.characters import (
    Geno,
    Mallow,
    Mario,
    Toadstool,
    Bowser,
)


from randomizer.types.items import StarPiece
from randomizer.types.progress_locations import BossFightLocation, Inventory
from randomizer.types.world import GameWorld
from randomizer.types.world.flags import (
    BanditsWayGating,
    BarrelVolcanoGating,
    BelomeTempleGating,
    BoosterTowerGating,
    BossScaleOptions,
    BowsersKeepGating,
    FactoryGating,
    FireworksOptions,
    ForestMazeGating,
    MarrymoreGating,
    Moleville1Gating,
    MonstroTownGating,
    PipeVaultGating,
    SeaGating,
    YaridovichGating,
    BanditsWayGate,
    BarrelVolcanoGate,
    BelomeTempleGate,
    BoosterTowerGate,
    BossShuffleScaleStats,
    BowsersKeepGate,
    BucketWarp,
    CasinoWarp,
    FactoryGate,
    FireworksSetting,
    ForestMazeGate,
    MarrymoreGate,
    Moleville1Gate,
    MonstroTownGate,
    PipeVaultGate,
    SafeLogicProgression,
    SeaGate,
    ShuffleWeddingGear,
    SkipMustyFearsSequence,
    StarPiecesRequired,
    YaridovichGate,
)


def progression_safety(world: GameWorld) -> bool:
    """IF true, it means the player has chosen some settings that
    should prevent having to fight unusually difficult boss fights
    in unexpected world areas or too early in the seed logic."""
    return world.settings.is_boolean_flag_enabled(
        SafeLogicProgression
    ) and world.settings.is_flag_value(BossShuffleScaleStats, BossScaleOptions.MATCH)


def can_defeat_some_of(
    world: GameWorld,
    inventory: Inventory,
    conditions: List[Callable],
    amount: int = 1,
):
    """If true, the player is expected to be able to defeat at least some of
    the provided bosses.
    If progression safety is turned off, this will always return true."""
    if not progression_safety(world):
        return True
    bosses: List[bool] = [cond(world, inventory) for cond in conditions]
    completable: List[bool] = [cond for cond in bosses if cond]
    return len(completable) >= amount


def can_defeat_boss(
    world: GameWorld, inventory: Inventory, location: Type[BossFightLocation]
) -> bool:
    """If true, the player is expected to be able to defeat the boss location."""
    inst = world.get_location_instance(location)
    if inst.contents is None:
        return False
    return inventory.has_item(type(inst.contents))


def can_defeat_mushroom_way_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the boss at Mushroom Way."""
    return can_defeat_boss(world, inventory, MushroomWayBossFight)


def can_access_bandits_way(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Bandit's Way."""
    if world.settings.is_flag_value(BanditsWayGate, BanditsWayGating.MALLOW):
        return inventory.has_item(Mallow)
    if world.settings.is_flag_value(BanditsWayGate, BanditsWayGating.HAMMER_BRO):
        return inventory.has_item(HammerBroBoss)
    return True


def can_defeat_bandits_way_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the boss at Bandit's Way."""
    return can_access_bandits_way(world, inventory) and can_defeat_boss(
        world, inventory, BanditsWayBossFight
    )


def can_defeat_mushroom_kingdom_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the boss at Mushroom Kingdom."""
    return can_defeat_bandits_way_boss(world, inventory) and can_defeat_boss(
        world, inventory, MushroomKingdomBossFight
    )


def can_defeat_mimic(
    world: GameWorld,
    inventory: Inventory,
    mimic: Union[
        Type[MimicFightInitiator1],
        Type[MimicFightInitiator2],
        Type[MimicFightInitiator3],
    ],
) -> bool:
    """If true, the player is expected to be able to defeat the specified mimic chest fight."""
    location = next((l for l in world.item_locations if l.does_contain(mimic)), None)
    if location is None:
        return False
    return location.can_access(inventory)


def can_access_first_mimic(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the first mimic chest fight."""
    return can_defeat_mimic(world, inventory, MimicFightInitiator1)


def can_defeat_first_mimic(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the first mimic chest fight."""
    return can_access_first_mimic(world, inventory) and can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_mushroom_way_boss,
            can_defeat_bandits_way_boss,
            can_defeat_mushroom_kingdom_boss,
        ],
    )


def can_access_sewer_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the boss at Kero Sewers."""
    return can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_mushroom_way_boss,
            can_defeat_bandits_way_boss,
            can_defeat_mushroom_kingdom_boss,
        ],
    )


def can_defeat_sewer_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the boss at Kero Sewers."""
    return can_access_sewer_boss(world, inventory) and can_defeat_boss(
        world, inventory, KeroSewersBossFight
    )


def can_access_forest(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Forest Maze."""
    if world.settings.is_flag_value(ForestMazeGate, ForestMazeGating.GENO):
        return inventory.has_item(Geno)
    if world.settings.is_flag_value(ForestMazeGate, ForestMazeGating.PIE):
        return inventory.has_item(CricketPie)
    return True


def can_access_forest_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the boss at Forest Maze."""
    return can_access_forest(world, inventory) and can_defeat_some_of(
        world,
        inventory,
        [can_defeat_mushroom_kingdom_boss, can_defeat_sewer_boss],
    )


def can_defeat_forest_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the boss at Forest Maze."""
    return can_defeat_boss(
        world, inventory, ForestBossFight
    ) and can_access_forest_boss(world, inventory)


def can_access_moleville_entrance(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the uper entrance to the mines."""
    if world.settings.is_flag_value(Moleville1Gate, Moleville1Gating.GENO):
        return inventory.has_item(Geno)
    if world.settings.is_flag_value(Moleville1Gate, Moleville1Gating.FOREST):
        return can_defeat_forest_boss(world, inventory)
    if world.settings.is_flag_value(Moleville1Gate, Moleville1Gating.BOWYER):
        return inventory.has_item(BowyerBoss)
    return True


def can_access_first_moleville_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 1st boss at Moleville."""
    return can_access_moleville_entrance(world, inventory) and (
        can_defeat_some_of(
            world,
            inventory,
            [can_defeat_mushroom_kingdom_boss, can_defeat_sewer_boss],
            2,
        )
        or can_defeat_some_of(
            world,
            inventory,
            [can_defeat_forest_boss],
        )
    )


def can_access_second_mimic(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the second mimic chest fight."""
    return can_defeat_mimic(world, inventory, MimicFightInitiator2)


def can_defeat_second_mimic(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the second mimic chest fight."""
    return can_access_second_mimic(world, inventory) and (
        can_defeat_some_of(
            world,
            inventory,
            [can_defeat_mushroom_kingdom_boss, can_defeat_sewer_boss],
            2,
        )
        or can_defeat_some_of(
            world,
            inventory,
            [can_defeat_forest_boss],
        )
    )


def can_defeat_first_moleville_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 1st boss at Moleville."""
    return can_access_first_moleville_boss(world, inventory) and can_defeat_boss(
        world, inventory, MinesMidbossFight
    )


def can_access_inner_mines(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the inner half
    of Moleville Mines (beyond the exploding wall)."""
    return can_access_moleville_entrance(world, inventory) and inventory.has_item(
        BambinoBomb
    )


def can_access_second_moleville_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 2nd boss at Moleville."""
    return can_access_inner_mines(world, inventory) and (
        can_defeat_some_of(
            world,
            inventory,
            [
                can_defeat_forest_boss,
                can_defeat_sewer_boss,
                can_defeat_first_moleville_boss,
            ],
        )
    )


def can_defeat_second_moleville_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 2nd boss at Moleville."""
    return can_access_second_moleville_boss(world, inventory) and can_defeat_boss(
        world, inventory, MinesBossFight
    )


def can_access_tower(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to enter Booster Tower."""
    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.MARIO):
        return inventory.has_item(Mario)
    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.MALLOW):
        return inventory.has_item(Mallow)
    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.GENO):
        return inventory.has_item(Geno)
    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.BOWSER):
        return inventory.has_item(Bowser)
    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.TOADSTOOL):
        return inventory.has_item(Toadstool)
    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.MINES):
        return can_defeat_second_moleville_boss(world, inventory)
    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.PUNCHINELLO):
        return inventory.has_item(PunchinelloBoss)
    return True


def can_access_curtain_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 1st boss of Booster Tower."""
    return can_access_tower(world, inventory) and (
        can_defeat_some_of(
            world,
            inventory,
            [
                can_defeat_forest_boss,
                can_defeat_second_moleville_boss,
                can_defeat_first_moleville_boss,
            ],
        )
    )


def can_defeat_curtain_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 1st boss of Booster Tower."""
    return can_access_curtain_boss(world, inventory) and can_defeat_boss(
        world, inventory, TowerCurtainRoomBossFight
    )


def can_access_balcony_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 2nd boss of Booster Tower."""
    return can_access_tower(world, inventory) and (
        can_defeat_some_of(
            world,
            inventory,
            [
                can_defeat_forest_boss,
                can_defeat_second_moleville_boss,
                can_defeat_first_moleville_boss,
                can_defeat_curtain_boss,
            ],
        )
    )


def can_defeat_balcony_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 2nd boss of Booster Tower."""
    return can_access_balcony_boss(world, inventory) and can_defeat_boss(
        world, inventory, TowerBalconyBossFight
    )


def can_access_chapel(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to enter the Marrymore chapel."""
    if world.settings.is_flag_value(MarrymoreGate, MarrymoreGating.TOWER):
        return can_defeat_balcony_boss(world, inventory)
    if world.settings.is_flag_value(MarrymoreGate, MarrymoreGating.KGGG):
        return inventory.has_item(GrateGuyBoss)
    return True


def can_access_chapel_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the boss of Marrymore."""
    has_gear = True
    if world.settings.is_boolean_flag_enabled(ShuffleWeddingGear):
        has_gear = (
            inventory.has_item(Shoes)
            and inventory.has_item(Ring)
            and inventory.has_item(Brooch)
            and inventory.has_item(Crown)
        )
    return (
        has_gear
        and can_access_chapel(world, inventory)
        and can_defeat_some_of(
            world,
            inventory,
            [
                can_defeat_forest_boss,
                can_defeat_second_moleville_boss,
                can_defeat_first_moleville_boss,
                can_defeat_curtain_boss,
                can_defeat_balcony_boss,
            ],
        )
    )


def can_defeat_chapel_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the boss of Marrymore."""
    return can_access_chapel_boss(world, inventory) and can_defeat_boss(
        world, inventory, ChapelBossFight
    )


def can_access_sea(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the Sea."""
    if world.settings.is_flag_value(SeaGate, SeaGating.TOADSTOOL):
        return inventory.has_item(Toadstool)
    if world.settings.is_flag_value(SeaGate, SeaGating.STAR_4):
        return inventory.has_item_count(StarPiece, 4)
    if world.settings.is_flag_value(SeaGate, SeaGating.BUNDT):
        return inventory.has_item(BundtBoss)
    return True


def can_access_ship_midboss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 1st ship boss."""
    return can_access_sea(world, inventory) and (
        can_defeat_some_of(
            world,
            inventory,
            [
                can_defeat_second_moleville_boss,
                can_defeat_first_moleville_boss,
                can_defeat_curtain_boss,
                can_defeat_balcony_boss,
                can_defeat_chapel_boss,
            ],
        )
    )


def can_defeat_ship_midboss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 1st ship boss."""
    return can_access_ship_midboss(world, inventory) and can_defeat_boss(
        world, inventory, ShipPasswordBossFight
    )


def can_access_ship_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 2nd ship boss."""
    return can_defeat_ship_midboss(world, inventory)


def can_defeat_ship_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 2nd ship boss."""
    return can_access_ship_boss(world, inventory) and can_defeat_boss(
        world, inventory, ShipFinalBossFight
    )


def can_access_seaside_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the Seaside Town boss."""
    sufficient_bosses = can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_second_moleville_boss,
            can_defeat_first_moleville_boss,
            can_defeat_curtain_boss,
            can_defeat_balcony_boss,
            can_defeat_chapel_boss,
            can_defeat_ship_midboss,
            can_defeat_ship_boss,
        ],
        2,
    )
    if world.settings.is_flag_value(YaridovichGate, YaridovichGating.SHIP):
        return can_defeat_ship_boss(world, inventory) and sufficient_bosses
    if world.settings.is_flag_value(YaridovichGate, YaridovichGating.JOHNNY):
        return inventory.has_item(JohnnyBoss) and sufficient_bosses
    return sufficient_bosses


def can_defeat_seaside_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the Seaside Town boss."""
    return can_access_seaside_boss(world, inventory) and can_defeat_boss(
        world, inventory, SeasideBeachBossFight
    )


def can_access_lands_end_cloud(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the random cloud spawn
    in Land's End."""
    return can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_curtain_boss,
            can_defeat_balcony_boss,
            can_defeat_chapel_boss,
            can_defeat_ship_midboss,
            can_defeat_ship_boss,
            can_defeat_seaside_boss,
        ],
        2,
    )


def can_defeat_lands_end_cloud_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the Land's End cloud spawn boss."""
    return can_access_lands_end_cloud(world, inventory) and can_defeat_boss(
        world, inventory, LandsEndCloudBossFight
    )


def can_access_temple(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Belome Temple."""
    if world.settings.is_flag_value(BelomeTempleGate, BelomeTempleGating.SEASIDE):
        return can_defeat_seaside_boss(world, inventory)
    if world.settings.is_flag_value(BelomeTempleGate, BelomeTempleGating.YARID):
        return inventory.has_item(YaridovichBoss)
    return True


def can_access_temple_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the Belome Temple boss."""
    return can_access_temple(world, inventory) and can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_curtain_boss,
            can_defeat_balcony_boss,
            can_defeat_chapel_boss,
            can_defeat_ship_midboss,
            can_defeat_ship_boss,
            can_defeat_seaside_boss,
            can_defeat_lands_end_cloud_boss,
        ],
        2,
    )


def can_access_third_mimic(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the third mimic chest fight."""
    return can_defeat_mimic(world, inventory, MimicFightInitiator3)


def can_defeat_third_mimic(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the third mimic chest fight."""
    return can_access_third_mimic(world, inventory) and can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_curtain_boss,
            can_defeat_balcony_boss,
            can_defeat_chapel_boss,
            can_defeat_ship_midboss,
            can_defeat_ship_boss,
            can_defeat_seaside_boss,
            can_defeat_lands_end_cloud_boss,
        ],
    )


def can_defeat_temple_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the Belome Temple boss."""
    return can_access_temple_boss(world, inventory) and can_defeat_boss(
        world, inventory, TempleBossFight
    )


def can_access_monstro_town(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Monstro Town."""
    if world.settings.is_flag_value(MonstroTownGate, MonstroTownGating.LANDS_END):
        return can_defeat_temple_boss(world, inventory)
    if world.settings.is_flag_value(MonstroTownGate, MonstroTownGating.BELOME_2):
        return inventory.has_item(Belome2Boss)
    return True


def can_access_first_dojo_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 1st Monstro dojo boss."""
    return can_access_monstro_town(world, inventory) and can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_ship_midboss,
            can_defeat_ship_boss,
            can_defeat_seaside_boss,
            can_defeat_lands_end_cloud_boss,
            can_defeat_temple_boss,
        ],
    )


def can_defeat_first_dojo_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 1st Monstro dojo boss."""
    return can_access_first_dojo_boss(world, inventory) and can_defeat_boss(
        world, inventory, DojoFirstFight
    )


def can_access_second_dojo_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 2nd Monstro dojo boss."""
    return can_defeat_first_dojo_boss(world, inventory)


def can_defeat_second_dojo_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 2nd Monstro dojo boss."""
    return can_access_second_dojo_boss(world, inventory) and can_defeat_boss(
        world, inventory, DojoSecondFight
    )


def can_access_third_dojo_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 3rd Monstro dojo boss."""
    return can_defeat_second_dojo_boss(world, inventory)


def can_defeat_third_dojo_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 3rd Monstro dojo boss."""
    return can_access_third_dojo_boss(world, inventory) and can_defeat_boss(
        world, inventory, DojoThirdFight
    )


def can_access_fourth_dojo_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 4th Monstro dojo boss."""
    return can_defeat_third_dojo_boss(world, inventory)


def can_defeat_fourth_dojo_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 4th Monstro dojo boss."""
    return can_access_third_dojo_boss(world, inventory) and can_defeat_boss(
        world, inventory, DojoFourthFight
    )


def can_access_valley_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the Bean Valley boss."""
    return can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_ship_midboss,
            can_defeat_ship_boss,
            can_defeat_seaside_boss,
            can_defeat_lands_end_cloud_boss,
            can_defeat_temple_boss,
            can_defeat_first_dojo_boss,
            can_defeat_second_dojo_boss,
            can_defeat_third_dojo_boss,
            can_defeat_fourth_dojo_boss,
        ],
    )


def can_defeat_valley_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the Bean Valley boss."""
    return can_access_valley_boss(world, inventory) and can_defeat_boss(
        world, inventory, BeanValleyPlanterBossFight
    )


def can_access_statue_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 1st Nimbus boss."""
    return can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_ship_midboss,
            can_defeat_ship_boss,
            can_defeat_seaside_boss,
            can_defeat_lands_end_cloud_boss,
            can_defeat_temple_boss,
            can_defeat_first_dojo_boss,
            can_defeat_second_dojo_boss,
            can_defeat_third_dojo_boss,
            can_defeat_fourth_dojo_boss,
            can_defeat_valley_boss,
        ],
    )


def can_defeat_statue_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 1st Nimbus boss."""
    return can_access_statue_boss(world, inventory) and can_defeat_boss(
        world, inventory, StatueRoomBossFight
    )


# pylint: disable=W0613
def can_access_inner_nimbus(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to get past the Castle Key 1 door."""
    return inventory.has_item(CastleKey1)


def can_access_egg_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 2nd Nimbus boss."""
    return can_access_inner_nimbus(world, inventory) and can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_ship_midboss,
            can_defeat_ship_boss,
            can_defeat_seaside_boss,
            can_defeat_temple_boss,
            can_defeat_first_dojo_boss,
            can_defeat_second_dojo_boss,
            can_defeat_third_dojo_boss,
            can_defeat_fourth_dojo_boss,
            can_defeat_valley_boss,
            can_defeat_statue_boss,
        ],
    )


def can_defeat_egg_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 2nd Nimbus boss."""
    return can_access_egg_boss(world, inventory) and can_defeat_boss(
        world, inventory, GiantEggBossFight
    )


def can_access_late_nimbus(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to get past the Castle Key 2 door."""
    return can_access_inner_nimbus(world, inventory) and inventory.has_item(CastleKey2)


def can_access_nimbus_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 3rd Nimbus boss."""
    return can_access_late_nimbus(world, inventory) and can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_ship_boss,
            can_defeat_seaside_boss,
            can_defeat_lands_end_cloud_boss,
            can_defeat_temple_boss,
            can_defeat_second_dojo_boss,
            can_defeat_third_dojo_boss,
            can_defeat_fourth_dojo_boss,
            can_defeat_valley_boss,
            can_defeat_statue_boss,
            can_defeat_egg_boss,
        ],
    )


def can_defeat_nimbus_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 3rd Nimbus boss."""
    return can_access_nimbus_boss(world, inventory) and can_defeat_boss(
        world, inventory, NimbusFinalBossFight
    )


def can_access_volcano(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Barrel Volcano."""
    if world.settings.is_flag_value(BarrelVolcanoGate, BarrelVolcanoGating.NIMBUS):
        return can_defeat_nimbus_boss(world, inventory)
    if world.settings.is_flag_value(BarrelVolcanoGate, BarrelVolcanoGating.VALENTINA):
        return inventory.has_item(ValentinaBoss)
    return True


def can_access_volcano_midboss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 1st volcano boss."""
    return can_access_volcano(world, inventory) and can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_seaside_boss,
            can_defeat_temple_boss,
            can_defeat_third_dojo_boss,
            can_defeat_fourth_dojo_boss,
            can_defeat_valley_boss,
            can_defeat_statue_boss,
            can_defeat_egg_boss,
            can_defeat_nimbus_boss,
        ],
    )


def can_defeat_volcano_midboss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 1st volcano boss."""
    return can_access_volcano_midboss(world, inventory) and can_defeat_boss(
        world, inventory, VolcanoBridgeBossFight
    )


def can_access_volcano_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 2nd volcano boss."""
    return can_defeat_volcano_midboss(world, inventory)


def can_defeat_volcano_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 2nd volcano boss."""
    return can_access_volcano_boss(world, inventory) and can_defeat_boss(
        world, inventory, VolcanoExitBossFight
    )


def can_take_lategame_bosses(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to reasonably have progressed enough in the seed
    to fight lategame bosses."""
    return can_defeat_some_of(
        world,
        inventory,
        [
            can_defeat_fourth_dojo_boss,
            can_defeat_egg_boss,
            can_access_nimbus_boss,
            can_defeat_volcano_midboss,
            can_defeat_volcano_boss,
        ],
    )


def can_access_keep(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Bowser's Keep."""
    if world.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.VOLCANO):
        return can_defeat_volcano_boss(world, inventory)
    if world.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.STAR_6):
        return inventory.has_item_count(StarPiece, 6)
    if world.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.AXEM):
        return inventory.has_item(AxemRangersBoss)
    return True


def can_access_battle_door_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the battle door
    that normally contains the Chester fight."""
    return can_access_keep(world, inventory) and can_take_lategame_bosses(
        world, inventory
    )


def can_defeat_battle_door_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the battle door
    that normally contains the Chester fight."""
    return can_access_battle_door_boss(world, inventory) and can_defeat_boss(
        world, inventory, ObstacleCourseFinalFight
    )


def can_access_post_obstacle_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the boss fight
    after completing the Bowser's Keep red doors."""
    return can_access_keep(world, inventory) and can_take_lategame_bosses(
        world, inventory
    )


def can_defeat_post_obstacle_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the boss fight
    after completing the Bowser's Keep red doors."""
    return can_access_post_obstacle_boss(world, inventory) and can_defeat_boss(
        world, inventory, KeepAfterObstaclesBossFight
    )


def can_access_keep_chandelier_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the first back-to-back Keep boss."""
    return can_defeat_post_obstacle_boss(world, inventory) and can_take_lategame_bosses(
        world, inventory
    )


def can_defeat_keep_chandelier_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the first back-to-back Keep boss."""
    return can_access_keep_chandelier_boss(world, inventory) and can_defeat_boss(
        world, inventory, KeepChandelierBossFight
    )


def can_access_keep_exit_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the second back-to-back Keep boss."""
    return can_defeat_keep_chandelier_boss(
        world, inventory
    ) and can_take_lategame_bosses(world, inventory)


def can_defeat_keep_exit_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the second back-to-back Keep boss."""
    return can_access_keep_exit_boss(world, inventory) and can_defeat_boss(
        world, inventory, KeepFinalBossFight
    )


def can_access_factory(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the Outer Factory."""
    if world.settings.is_flag_value(FactoryGate, FactoryGating.STAR_6):
        return inventory.has_item_count(StarPiece, 6) and can_defeat_keep_exit_boss(
            world, inventory
        )
    if world.settings.is_flag_value(FactoryGate, FactoryGating.EXOR):
        return inventory.has_item(ExorBoss) and can_defeat_keep_exit_boss(
            world, inventory
        )
    return can_defeat_keep_exit_boss(world, inventory)


def can_access_first_factory_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 1st Outer Factory boss."""
    return can_access_factory(world, inventory) and can_take_lategame_bosses(
        world, inventory
    )


def can_defeat_first_factory_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 1st Outer Factory boss."""
    return can_access_first_factory_boss(world, inventory) and can_defeat_boss(
        world, inventory, FactoryEntranceBoss
    )


def can_access_second_factory_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 2nd Outer Factory boss."""
    return can_defeat_first_factory_boss(world, inventory) and can_take_lategame_bosses(
        world, inventory
    )


def can_defeat_second_factory_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 2nd Outer Factory boss."""
    return can_access_second_factory_boss(world, inventory) and can_defeat_boss(
        world, inventory, FactoryTransitionBoss
    )


def can_access_inner_factory_first_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 1st Inner Factory boss."""
    return can_defeat_second_factory_boss(
        world, inventory
    ) and can_take_lategame_bosses(world, inventory)


def can_defeat_inner_factory_first_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 1st Inner Factory boss."""
    return can_access_inner_factory_first_boss(world, inventory) and can_defeat_boss(
        world, inventory, InnerFactoryFirstFight
    )


def can_access_inner_factory_second_boss(
    world: GameWorld, inventory: Inventory
) -> bool:
    """If true, the player is expected to be able to access the 2nd Inner Factory boss."""
    return can_defeat_first_factory_boss(world, inventory) and can_take_lategame_bosses(
        world, inventory
    )


def can_defeat_inner_factory_second_boss(
    world: GameWorld, inventory: Inventory
) -> bool:
    """If true, the player is expected to be able to defeat the 2nd Inner Factory boss."""
    return can_access_inner_factory_second_boss(world, inventory) and can_defeat_boss(
        world, inventory, InnerFactorySecondFight
    )


def can_access_inner_factory_third_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the 3rd Inner Factory boss."""
    return can_defeat_inner_factory_second_boss(
        world, inventory
    ) and can_take_lategame_bosses(world, inventory)


def can_defeat_inner_factory_third_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the 3rd Inner Factory boss."""
    return can_access_inner_factory_third_boss(world, inventory) and can_defeat_boss(
        world, inventory, InnerFactoryThirdFight
    )


def can_access_inner_factory_fourth_boss(
    world: GameWorld, inventory: Inventory
) -> bool:
    """If true, the player is expected to be able to access the 4th Inner Factory boss."""
    return can_defeat_inner_factory_third_boss(
        world, inventory
    ) and can_take_lategame_bosses(world, inventory)


def can_defeat_inner_factory_fourth_boss(
    world: GameWorld, inventory: Inventory
) -> bool:
    """If true, the player is expected to be able to defeat the 4th Inner Factory boss."""
    return can_access_inner_factory_fourth_boss(world, inventory) and can_defeat_boss(
        world, inventory, InnerFactoryFourthFight
    )


def can_access_inner_factory_final_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the final Factory boss."""
    value = world.settings.get_flag(StarPiecesRequired).value
    has_stars = inventory.has_item_count(StarPiece, value)
    if world.settings.is_flag_value(FireworksSetting, FireworksOptions.SHUFFLE_ONE):
        fireworks_access = inventory.has_item(Fireworks)
    elif world.settings.is_flag_value(FireworksSetting, FireworksOptions.PROGRESSIVE):
        fireworks_access = inventory.has_item_count(ProgressiveFireworks, 3)
    else:
        fireworks_access = True
    can_access_bucket = (
        fireworks_access
        and can_defeat_second_moleville_boss(world, inventory)
        and world.settings.is_boolean_flag_enabled(BucketWarp)
    )
    can_access_casino = world.settings.is_boolean_flag_enabled(
        CasinoWarp
    ) and inventory.has_item(BrightCard)
    return (
        has_stars
        and (
            can_access_bucket
            or can_access_casino
            or can_defeat_inner_factory_fourth_boss(world, inventory)
        )
        and can_take_lategame_bosses(world, inventory)
    )


def can_defeat_inner_factory_final_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the final Factory boss."""
    return can_access_inner_factory_final_boss(world, inventory) and can_defeat_boss(
        world, inventory, FinalBossFight
    )


def can_access_sealed_door_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access the sealed door boss."""
    boss_reqs = can_access_monstro_town(world, inventory) and can_take_lategame_bosses(
        world, inventory
    )
    item_reqs: bool = False
    if world.settings.is_flag_value(FireworksSetting, FireworksOptions.SHUFFLE_ONE):
        item_reqs = inventory.has_item(Fireworks) and can_defeat_second_moleville_boss(
            world, inventory
        )
    elif world.settings.is_flag_value(FireworksSetting, FireworksOptions.PROGRESSIVE):
        item_reqs = inventory.has_item_count(ProgressiveFireworks, 2)
    else:
        item_reqs = can_defeat_second_moleville_boss(world, inventory)
    return can_access_monstro_town(world, inventory) and item_reqs and boss_reqs


def can_defeat_sealed_door_boss(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to defeat the sealed door boss."""
    return can_access_sealed_door_boss(world, inventory) and can_defeat_boss(
        world, inventory, FinalBossFight
    )


def can_access_invisible_flags(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the invisible item checks have been activated."""
    return world.settings.is_boolean_flag_enabled(
        SkipMustyFearsSequence
    ) or can_access_monstro_town(world, inventory)


def can_access_pipe_vault(world: GameWorld, inventory: Inventory) -> bool:
    """If true, the player is expected to be able to access Pipe Vault."""
    if world.settings.is_flag_value(PipeVaultGate, PipeVaultGating.GENO):
        return inventory.has_item(Geno)
    if world.settings.is_flag_value(PipeVaultGate, PipeVaultGating.FOREST):
        return can_defeat_forest_boss(world, inventory)
    if world.settings.is_flag_value(PipeVaultGate, PipeVaultGating.BOWYER):
        return inventory.has_item(BowyerBoss)
    return True
