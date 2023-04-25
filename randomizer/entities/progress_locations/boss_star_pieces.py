"""Progress location definitions for star piece grants from boss fights."""

from typing import Optional, Type, List

from randomizer.entities.items import (
    MimicFightInitiator1,
    MimicFightInitiator2,
    MimicFightInitiator3,
    StarPiece1,
    StarPiece2,
    StarPiece3,
    StarPiece4,
    StarPiece5,
    StarPiece6,
    StarPiece7,
)
from randomizer.types.items import StarPiece
from randomizer.types.overworld_scripts.ids import (
    R018_MUSHROOM_KINGDOM_CASTLE_THRONE_ROOM,
    R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM,
    R103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM,
    R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER,
    R159_STAR_HILL_AREA_04,
    R173_SUNKEN_SHIP_POSTKC_AREA_01_SMALL_ROOM_WTRAMPOLINE,
    R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
    R202_BOOSTER_TOWER_ENTRANCE,
    R205_MUSHROOM_WAY_AREA_03,
    R206_BANDITS_WAY_AREA_05,
    R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD,
    R254_BEAN_VALLEY_SMILAX_AREA,
    R255_MONSTRO_TOWN_JINXS_DOJO,
    R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM,
    R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM,
    R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE,
    R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS,
    R316_SEASIDE_TOWN_BEACH,
    R324_MONSTRO_TOWN_OUTSIDE,
    R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
    R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP,
    R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD,
    R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM,
    R433_SMITHY_FACTORY_AREA_01_____DUMMY,
    R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA,
    R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB,
    R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
    R471_FACTORY_GROUNDS_AREA_02,
    R472_FACTORY_GROUNDS_AREA_03,
)
from randomizer.types.progress_locations import (
    LocationWorldArea,
    BossStarPiecePrize,
    Inventory,
)
from randomizer.types.world.flags import ShuffleLocationSelector
from .helpers.area_access import (
    can_defeat_balcony_boss,
    can_defeat_bandits_way_boss,
    can_defeat_battle_door_boss,
    can_defeat_chapel_boss,
    can_defeat_curtain_boss,
    can_defeat_egg_boss,
    can_defeat_first_dojo_boss,
    can_defeat_first_factory_boss,
    can_defeat_first_mimic,
    can_defeat_first_moleville_boss,
    can_defeat_forest_boss,
    can_defeat_fourth_dojo_boss,
    can_defeat_inner_factory_final_boss,
    can_defeat_inner_factory_first_boss,
    can_defeat_inner_factory_fourth_boss,
    can_defeat_inner_factory_second_boss,
    can_defeat_inner_factory_third_boss,
    can_defeat_keep_chandelier_boss,
    can_defeat_keep_exit_boss,
    can_defeat_lands_end_cloud_boss,
    can_defeat_mushroom_kingdom_boss,
    can_defeat_mushroom_way_boss,
    can_defeat_nimbus_boss,
    can_defeat_post_obstacle_boss,
    can_defeat_sealed_door_boss,
    can_defeat_seaside_boss,
    can_defeat_second_dojo_boss,
    can_defeat_second_factory_boss,
    can_defeat_second_mimic,
    can_defeat_second_moleville_boss,
    can_defeat_sewer_boss,
    can_defeat_ship_boss,
    can_defeat_ship_midboss,
    can_defeat_statue_boss,
    can_defeat_temple_boss,
    can_defeat_third_dojo_boss,
    can_defeat_third_mimic,
    can_defeat_valley_boss,
    can_defeat_volcano_boss,
    can_defeat_volcano_midboss,
)


class MushroomWayBossFightStar(BossStarPiecePrize):
    """MushroomWayBossFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.MUSHROOM_WAY_STAR_PIECE
    )
    _room_ids: List[int] = [R205_MUSHROOM_WAY_AREA_03]
    _world_area: LocationWorldArea = LocationWorldArea.MUSHROOM_WAY

    def can_access(self, inventory: Inventory):
        return can_defeat_mushroom_way_boss(self.world, inventory)


class BanditsWayBossFightStar(BossStarPiecePrize):
    """BanditsWayBossFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BANDITS_WAY_STAR_PIECE
    _room_ids: List[int] = [R206_BANDITS_WAY_AREA_05]
    _world_area: LocationWorldArea = LocationWorldArea.BANDITS_WAY

    def can_access(self, inventory: Inventory):
        return can_defeat_bandits_way_boss(self.world, inventory)


class MushroomKingdomBossFightStar(BossStarPiecePrize):
    """MushroomKingdomBossFightStar progress location class"""

    _original_item: Type[StarPiece] = StarPiece1
    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.INVASION_STAR_PIECE
    _room_ids: List[int] = [R018_MUSHROOM_KINGDOM_CASTLE_THRONE_ROOM]
    _world_area: LocationWorldArea = LocationWorldArea.MUSHROOM_KINGDOM_OCCUPIED_ONLY

    def can_access(self, inventory: Inventory):
        return can_defeat_mushroom_kingdom_boss(self.world, inventory)


class MimicFightLocation1Star(BossStarPiecePrize):
    """MimicFightLocation1Star progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.PANDORITE_BOSS
    _identifier: int = 512

    @property
    def world_area(self) -> Optional[LocationWorldArea]:
        location = next(
            (
                l
                for l in self.world.item_locations
                if l.does_contain(MimicFightInitiator1)
            ),
            None,
        )
        if location is None:
            return None
        return location.world_area

    def can_access(self, inventory: Inventory):
        return can_defeat_first_mimic(self.world, inventory)


class KeroSewersBossFightStar(BossStarPiecePrize):
    """KeroSewersBossFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.KERO_SEWERS_BOSS
    _room_ids: List[int] = [R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS]
    _world_area: LocationWorldArea = LocationWorldArea.KERO_SEWERS

    def can_access(self, inventory: Inventory):
        return can_defeat_sewer_boss(self.world, inventory)


class ForestBossFightStar(BossStarPiecePrize):
    """ForestBossFightStar progress location class"""

    _original_item: Type[StarPiece] = StarPiece2
    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.FOREST_MAZE_BOSS
    _room_ids: List[int] = [R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    _world_area: LocationWorldArea = LocationWorldArea.FOREST_MAZE

    def can_access(self, inventory: Inventory):
        return can_defeat_forest_boss(self.world, inventory)


class MinesMidbossFightStar(BossStarPiecePrize):
    """MinesMidbossFightStar progress location class"""

    _identifier: int = 518
    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_1
    _world_area: LocationWorldArea = LocationWorldArea.MOLEVILLE_MINES

    def can_access(self, inventory: Inventory):
        return can_defeat_first_moleville_boss(self.world, inventory)


class MinesBossFightStar(BossStarPiecePrize):
    """MinesBossFightStar progress location class"""

    _original_item: Type[StarPiece] = StarPiece3
    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_2
    _room_ids: List[int] = [R271_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_AFTER_BATTLE]
    _world_area: LocationWorldArea = LocationWorldArea.MOLEVILLE_MINES

    def can_access(self, inventory: Inventory):
        return can_defeat_second_moleville_boss(self.world, inventory)


class TowerCurtainRoomBossFightStar(BossStarPiecePrize):
    """TowerCurtainRoomBossFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOOSTER_TOWER_STAR_PIECE_1
    )
    _room_ids: List[int] = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _world_area: LocationWorldArea = LocationWorldArea.BOOSTER_TOWER

    def can_access(self, inventory: Inventory):
        return can_defeat_curtain_boss(self.world, inventory)


class TowerBalconyBossFightStar(BossStarPiecePrize):
    """TowerBalconyBossFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOOSTER_TOWER_STAR_PIECE_2
    )
    _room_ids: List[int] = [R202_BOOSTER_TOWER_ENTRANCE]
    _world_area: LocationWorldArea = LocationWorldArea.BOOSTER_TOWER

    def can_access(self, inventory: Inventory):
        return can_defeat_balcony_boss(self.world, inventory)


class ChapelBossFightStar(BossStarPiecePrize):
    """ChapelBossFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.MARRYMORE_STAR_PIECE
    _room_ids: List[int] = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _world_area: LocationWorldArea = LocationWorldArea.MARRYMORE

    def can_access(self, inventory: Inventory):
        return can_defeat_chapel_boss(self.world, inventory)


class StarHillStar(BossStarPiecePrize):
    """StarHillStar progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.STAR_HILL_STAR_PIECE_1
    _original_item: Type[StarPiece] = StarPiece4
    _room_ids: List[int] = [R159_STAR_HILL_AREA_04]
    _world_area: LocationWorldArea = LocationWorldArea.STAR_HILL


class ShipPasswordBossFightStar(BossStarPiecePrize):
    """ShipPasswordBossFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.SUNKEN_SHIP_MIDBOSS
    _room_ids: List[int] = [R173_SUNKEN_SHIP_POSTKC_AREA_01_SMALL_ROOM_WTRAMPOLINE]
    _world_area: LocationWorldArea = LocationWorldArea.SUNKEN_SHIP

    def can_access(self, inventory: Inventory):
        return can_defeat_ship_midboss(self.world, inventory)


class MimicFightLocation2Star(BossStarPiecePrize):
    """MimicFightLocation2Star progress location class"""

    _identifier: int = 513
    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.HIDON_BOSS

    @property
    def world_area(self) -> Optional[LocationWorldArea]:
        location = next(
            (
                l
                for l in self.world.item_locations
                if l.does_contain(MimicFightInitiator2)
            ),
            None,
        )
        if location is None:
            return None
        return location.world_area

    def can_access(self, inventory: Inventory):
        return can_defeat_second_mimic(self.world, inventory)


class ShipFinalBossFightStar(BossStarPiecePrize):
    """ShipFinalBossFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.SUNKEN_SHIP_BOSS
    _room_ids: List[int] = [R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM]
    _world_area: LocationWorldArea = LocationWorldArea.SUNKEN_SHIP

    def can_access(self, inventory: Inventory):
        return can_defeat_ship_boss(self.world, inventory)


class SeasideBeachBossFightStar(BossStarPiecePrize):
    """SeasideBeachBossFightStar progress location class"""

    _original_item: Type[StarPiece] = StarPiece5
    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.SEASIDE_TOWN_BOSS
    _room_ids: List[int] = [R316_SEASIDE_TOWN_BEACH]
    _world_area: LocationWorldArea = LocationWorldArea.SEASIDE_TOWN

    def can_access(self, inventory: Inventory):
        return can_defeat_seaside_boss(self.world, inventory)


class LandsEndCloudBossFightStar(BossStarPiecePrize):
    """LandsEndCloudBossFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.LANDS_END_STAR_PIECE_1
    _identifier: int = 519
    _world_area: LocationWorldArea = (
        LocationWorldArea.LANDS_END
    )  # technically also belome temple, but for simplicity we go with lands end

    def can_access(self, inventory: Inventory):
        return can_defeat_lands_end_cloud_boss(self.world, inventory)


class TempleBossFightStar(BossStarPiecePrize):
    """TempleBossFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BELOME_TEMPLE_BOSS
    _room_ids: List[int] = [R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM]
    _world_area: LocationWorldArea = LocationWorldArea.BELOME_TEMPLE

    def can_access(self, inventory: Inventory):
        return can_defeat_temple_boss(self.world, inventory)


class DojoFirstFightStar(BossStarPiecePrize):
    """DojoFirstFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.DOJO_BOSS_1
    _room_ids: List[int] = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _world_area: LocationWorldArea = LocationWorldArea.MONSTRO_TOWN

    def can_access(self, inventory: Inventory):
        return can_defeat_first_dojo_boss(self.world, inventory)


class DojoSecondFightStar(BossStarPiecePrize):
    """DojoSecondFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.DOJO_BOSS_2
    _identifier: int = 515
    _world_area: LocationWorldArea = LocationWorldArea.MONSTRO_TOWN

    def can_access(self, inventory: Inventory):
        return can_defeat_second_dojo_boss(self.world, inventory)


class DojoThirdFightStar(BossStarPiecePrize):
    """DojoThirdFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.DOJO_BOSS_3
    _identifier: int = 516
    _world_area: LocationWorldArea = LocationWorldArea.MONSTRO_TOWN

    def can_access(self, inventory: Inventory):
        return can_defeat_third_dojo_boss(self.world, inventory)


class DojoFourthFightStar(BossStarPiecePrize):
    """DojoFourthFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.DOJO_BOSS_4
    _identifier: int = 517
    _world_area: LocationWorldArea = LocationWorldArea.MONSTRO_TOWN

    def can_access(self, inventory: Inventory):
        return can_defeat_fourth_dojo_boss(self.world, inventory)


class MonstroSealedDoorBossFightStar(BossStarPiecePrize):
    """MonstroSealedDoorBossFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.CULEX_BOSS
    _room_ids: List[int] = [R324_MONSTRO_TOWN_OUTSIDE]
    _world_area: LocationWorldArea = LocationWorldArea.MONSTRO_TOWN

    def can_access(self, inventory: Inventory):
        return can_defeat_sealed_door_boss(self.world, inventory)


class MimicFightLocation3Star(BossStarPiecePrize):
    """MimicFightLocation3Star progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOX_BOY_BOSS
    _identifier: int = 514

    @property
    def world_area(self) -> Optional[LocationWorldArea]:
        location = next(
            (
                l
                for l in self.world.item_locations
                if l.does_contain(MimicFightInitiator3)
            ),
            None,
        )
        if location is None:
            return None
        return location.world_area

    def can_access(self, inventory: Inventory):
        return can_defeat_third_mimic(self.world, inventory)


class BeanValleyPlanterBossFightStar(BossStarPiecePrize):
    """BeanValleyPlanterBossFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BEAN_VALLEY_BOSS
    _room_ids: List[int] = [R254_BEAN_VALLEY_SMILAX_AREA]
    _world_area: LocationWorldArea = LocationWorldArea.BEAN_VALLEY

    def can_access(self, inventory: Inventory):
        return can_defeat_valley_boss(self.world, inventory)


class StatueRoomBossFightStar(BossStarPiecePrize):
    """StatueRoomBossFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.NIMBUS_LAND_STAR_PIECE_1
    )
    _identifier: int = 520
    _world_area: LocationWorldArea = LocationWorldArea.NIMBUS_CASTLE

    def can_access(self, inventory: Inventory):
        return can_defeat_statue_boss(self.world, inventory)


class GiantEggBossFightStar(BossStarPiecePrize):
    """GiantEggBossFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.NIMBUS_CASTLE_STAR_PIECE_2
    )
    _room_ids: List[int] = [R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM]
    _world_area: LocationWorldArea = LocationWorldArea.NIMBUS_CASTLE

    def can_access(self, inventory: Inventory):
        return can_defeat_egg_boss(self.world, inventory)


class NimbusFinalBossFightStar(BossStarPiecePrize):
    """NimbusFinalBossFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.NIMBUS_CASTLE_STAR_PIECE_3
    )
    _room_ids: List[int] = [R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA]
    _world_area: LocationWorldArea = LocationWorldArea.NIMBUS_CASTLE

    def can_access(self, inventory: Inventory):
        return can_defeat_nimbus_boss(self.world, inventory)


class VolcanoBridgeBossFightStar(BossStarPiecePrize):
    """VolcanoBridgeBossFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BARREL_VOLCANO_BOSS_1
    _room_ids: List[int] = [R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM]
    _world_area: LocationWorldArea = LocationWorldArea.BARREL_VOLCANO

    def can_access(self, inventory: Inventory):
        return can_defeat_volcano_midboss(self.world, inventory)


class VolcanoExitBossFightStar(BossStarPiecePrize):
    """VolcanoExitBossFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BARREL_VOLCANO_BOSS_2
    _room_ids: List[int] = [R393_VOLCANO_POSTCD_AREA_07_WARP_TO_WORLD_MAP]
    _original_item: Type[StarPiece] = StarPiece6
    _world_area: LocationWorldArea = LocationWorldArea.BARREL_VOLCANO

    def can_access(self, inventory: Inventory):
        return can_defeat_volcano_boss(self.world, inventory)


class ObstacleCourseFinalFightStar(BossStarPiecePrize):
    """ObstacleCourseFinalFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.BOWSERS_KEEP_BOSS_CHESTER
    )
    _room_ids: List[int] = [R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB]
    _world_area: LocationWorldArea = LocationWorldArea.BOWSERS_KEEP

    def can_access(self, inventory: Inventory):
        return can_defeat_battle_door_boss(self.world, inventory)


class KeepAfterObstaclesBossFightStar(BossStarPiecePrize):
    """KeepAfterObstaclesBossFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_1
    _room_ids: List[int] = [R266_BOWSERS_KEEP_AREA_10_MAGIKOOPAS_ROOM]
    _world_area: LocationWorldArea = LocationWorldArea.BOWSERS_KEEP

    def can_access(self, inventory: Inventory):
        return can_defeat_post_obstacle_boss(self.world, inventory)


class KeepChandelierBossFightStar(BossStarPiecePrize):
    """KeepChandelierBossFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_2
    _identifier: int = 521
    _world_area: LocationWorldArea = LocationWorldArea.BOWSERS_KEEP

    def can_access(self, inventory: Inventory):
        return can_defeat_keep_chandelier_boss(self.world, inventory)


class KeepFinalBossFightStar(BossStarPiecePrize):
    """KeepFinalBossFightStar progress location class"""

    _identifier: int = 522
    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.BOWSERS_KEEP_BOSS_3
    _world_area: LocationWorldArea = LocationWorldArea.BOWSERS_KEEP

    def can_access(self, inventory: Inventory):
        return can_defeat_keep_exit_boss(self.world, inventory)


class FactoryEntranceBossStar(BossStarPiecePrize):
    """FactoryEntranceBossStar progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.FACTORY_BOSS_1
    _room_ids: List[int] = [R433_SMITHY_FACTORY_AREA_01_____DUMMY]
    _world_area: LocationWorldArea = LocationWorldArea.FACTORY

    def can_access(self, inventory: Inventory):
        return can_defeat_first_factory_boss(self.world, inventory)


class FactoryTransitionBossStar(BossStarPiecePrize):
    """FactoryTransitionBossStar progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.FACTORY_BOSS_2
    _room_ids: List[int] = [R103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM]
    _world_area: LocationWorldArea = LocationWorldArea.FACTORY

    def can_access(self, inventory: Inventory):
        return can_defeat_second_factory_boss(self.world, inventory)


class InnerFactoryFirstFightStar(BossStarPiecePrize):
    """InnerFactoryFirstFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.INNER_FACTORY_BOSS_1
    _room_ids: List[int] = [R406_FACTORY_GROUNDS_AREA_01_WITH_TOAD]
    _world_area: LocationWorldArea = LocationWorldArea.INNER_FACTORY

    def can_access(self, inventory: Inventory):
        return can_defeat_inner_factory_first_boss(self.world, inventory)


class InnerFactorySecondFightStar(BossStarPiecePrize):
    """InnerFactorySecondFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.INNER_FACTORY_BOSS_2
    _room_ids: List[int] = [R471_FACTORY_GROUNDS_AREA_02]
    _world_area: LocationWorldArea = LocationWorldArea.INNER_FACTORY

    def can_access(self, inventory: Inventory):
        return can_defeat_inner_factory_second_boss(self.world, inventory)


class InnerFactoryThirdFightStar(BossStarPiecePrize):
    """InnerFactoryThirdFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.INNER_FACTORY_BOSS_3
    _room_ids: List[int] = [R472_FACTORY_GROUNDS_AREA_03]
    _world_area: LocationWorldArea = LocationWorldArea.INNER_FACTORY

    def can_access(self, inventory: Inventory):
        return can_defeat_inner_factory_third_boss(self.world, inventory)


class InnerFactoryFourthFightStar(BossStarPiecePrize):
    """InnerFactoryFourthFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = ShuffleLocationSelector.INNER_FACTORY_BOSS_4
    _room_ids: List[int] = [R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM]
    _world_area: LocationWorldArea = LocationWorldArea.INNER_FACTORY

    def can_access(self, inventory: Inventory):
        return can_defeat_inner_factory_fourth_boss(self.world, inventory)


class FinalBossFightStar(BossStarPiecePrize):
    """FinalBossFightStar progress location class"""

    _name_enum: ShuffleLocationSelector = (
        ShuffleLocationSelector.INNER_FACTORY_BOSS_FINAL
    )
    _original_item: Type[StarPiece] = StarPiece7
    _room_ids: List[int] = [523]
    _world_area: LocationWorldArea = LocationWorldArea.INNER_FACTORY

    def can_access(self, inventory: Inventory):
        return can_defeat_inner_factory_final_boss(self.world, inventory)
