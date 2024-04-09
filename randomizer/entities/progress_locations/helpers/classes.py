"""Generic location classes belonging to world areas, with associated access logic."""

from typing import Type
from randomizer.entities.items import BrightCard, TempleKey
from randomizer.entities.progress_locations.helpers.area_access import (
    can_access_bandits_way,
    can_access_chapel,
    can_access_factory,
    can_access_forest,
    can_access_inner_mines,
    can_access_inner_nimbus,
    can_access_keep,
    can_access_late_nimbus,
    can_access_moleville_entrance,
    can_access_monstro_town,
    can_access_pipe_vault,
    can_access_sea,
    can_access_temple,
    can_access_tower,
    can_access_volcano,
    can_defeat_bandits_way_boss,
    can_defeat_battle_door_boss,
    can_defeat_first_factory_boss,
    can_defeat_second_factory_boss,
    can_defeat_ship_midboss,
)
from randomizer.types.items import Item
from randomizer.types.items.classes import StarPiece

from randomizer.types.progress_locations import (
    Inventory,
    ProgressLocation,
    LocationWorldArea,
)
from randomizer.types.world import GameWorld
from randomizer.types.world.flags import BowserDoorShuffle, StarPiecesRestrictedByArea
from randomizer.types.world.flags.enums import (
    BanditsWayGating,
    BarrelVolcanoGating,
    BelomeTempleGating,
    BoosterTowerGating,
    BowsersKeepGating,
    FactoryGating,
    ForestMazeGating,
    MarrymoreGating,
    Moleville1Gating,
    PipeVaultGating,
    SeaGating,
)
from randomizer.types.world.flags.flags import (
    BanditsWayGate,
    BarrelVolcanoGate,
    BelomeTempleGate,
    BoosterTowerGate,
    BowsersKeepGate,
    FactoryGate,
    ForestMazeGate,
    MarrymoreGate,
    Moleville1Gate,
    PipeVaultGate,
    SeaGate,
)


def _should_forbid_star_piece(world: GameWorld, *class_matches: Type[ProgressLocation]):
    if not world.settings.is_boolean_flag_enabled(StarPiecesRestrictedByArea):
        return False
    comparative_locations = [
        l
        for l in world.boss_star_pieces + world.item_locations
        if isinstance(l, class_matches)
    ]
    for location in comparative_locations:
        if isinstance(location.contents, StarPiece):
            return True
    return False


def _area_1_should_forbid_star_piece(world: GameWorld, item: Item) -> bool:
    """Returns true if a nearby area already has a star piece."""
    if not isinstance(item, StarPiece):
        return False
    return _should_forbid_star_piece(
        world,
        MariosPadLocation,
        MushroomWayLocation,
        MushroomKingdomLocation,
        BanditsWayLocation,
        MushroomKingdomOccupiedLocation,
    )


def _area_2_should_forbid_star_piece(world: GameWorld, item: Item) -> bool:
    """Returns true if a nearby area already has a star piece."""
    if not isinstance(item, StarPiece):
        return False
    return _should_forbid_star_piece(
        world,
        KeroSewersLocation,
        MidasRiverLocation,
        TadpolePondLocation,
        RoseWayLocation,
        RoseTownLocation,
        ForestLocation,
        PipeVaultLocation,
        YosterIsleLocation,
    )


def _area_3_should_forbid_star_piece(world: GameWorld, item: Item) -> bool:
    """Returns true if a nearby area already has a star piece."""
    if not isinstance(item, StarPiece):
        return False
    return _should_forbid_star_piece(
        world,
        MolevilleLocation,
        MinesLocation,
        InnerMinesLocation,
        BoosterPassLocation,
        BoosterTowerExteriorLocation,
        BoosterTowerLocation,
        MarrymoreLocation,
    )


def _area_4_should_forbid_star_piece(world: GameWorld, item: Item) -> bool:
    """Returns true if a nearby area already has a star piece."""
    if not isinstance(item, StarPiece):
        return False
    return _should_forbid_star_piece(
        world,
        StarHillLocation,
        SeasideTownLocation,
        SeaLocation,
        SunkenShipLocation,
        InnerSunkenShipLocation,
    )


def _area_5_should_forbid_star_piece(world: GameWorld, item: Item) -> bool:
    """Returns true if a nearby area already has a star piece."""
    if not isinstance(item, StarPiece):
        return False
    return _should_forbid_star_piece(
        world,
        LandsEndLocation,
        TempleLocation,
        InnerTempleLocation,
        TreasuryLocation,
        MonstroTownLocation,
        BeanValleyLocation,
        CasinoLocation,
    )


def _area_6_should_forbid_star_piece(world: GameWorld, item: Item) -> bool:
    """Returns true if a nearby area already has a star piece."""
    if not isinstance(item, StarPiece):
        return False
    return _should_forbid_star_piece(
        world,
        NimbusTownLocation,
        NimbusCastleLocation,
        NimbusMidCastleLocation,
        NimbusDeepCastleLocation,
        BarrelVolcanoLocation,
    )


def _area_7_should_forbid_star_piece(world: GameWorld, item: Item) -> bool:
    """Returns true if a nearby area already has a star piece."""
    if not isinstance(item, StarPiece):
        return False
    return _should_forbid_star_piece(
        world,
        BowsersKeepLocation,
        BowsersKeepObstacleLocation,
        OuterFactoryLocation,
        MidFactoryLocation,
        InnerFactoryLocation,
    )


class _Area1Location(ProgressLocation):
    def can_accept(self, item: Item, inventory: Inventory | None = None) -> bool:
        return (
            super().can_accept(item, inventory) and not _area_1_should_forbid_star_piece
        )


class _Area2Location(ProgressLocation):
    def can_accept(self, item: Item, inventory: Inventory | None = None) -> bool:
        return (
            super().can_accept(item, inventory) and not _area_2_should_forbid_star_piece
        )


class _Area3Location(ProgressLocation):
    def can_accept(self, item: Item, inventory: Inventory | None = None) -> bool:
        return (
            super().can_accept(item, inventory) and not _area_3_should_forbid_star_piece
        )


class _Area4Location(ProgressLocation):
    def can_accept(self, item: Item, inventory: Inventory | None = None) -> bool:
        return (
            super().can_accept(item, inventory) and not _area_4_should_forbid_star_piece
        )


class _Area5Location(ProgressLocation):
    def can_accept(self, item: Item, inventory: Inventory | None = None) -> bool:
        return (
            super().can_accept(item, inventory) and not _area_5_should_forbid_star_piece
        )


class _Area6Location(ProgressLocation):
    def can_accept(self, item: Item, inventory: Inventory | None = None) -> bool:
        return (
            super().can_accept(item, inventory) and not _area_6_should_forbid_star_piece
        )


class _Area7Location(ProgressLocation):
    def can_accept(self, item: Item, inventory: Inventory | None = None) -> bool:
        return (
            super().can_accept(item, inventory) and not _area_7_should_forbid_star_piece
        )


class MariosPadLocation(_Area1Location):
    """Base class for MariosPadLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.MARIOS_PAD
    _tier: int = 2


class MushroomWayLocation(_Area1Location):
    """Base class for MushroomWayLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.MUSHROOM_WAY
    _tier: int = 2


class MushroomKingdomLocation(_Area1Location):
    """Base class for MushroomKingdomLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.MUSHROOM_KINGDOM
    _tier: int = 2


class BanditsWayLocation(_Area1Location):
    """Base class for BanditsWayLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.BANDITS_WAY

    def can_access(self, inventory: Inventory):
        return can_access_bandits_way(self.world, inventory)

    @property
    def tier(self) -> int:
        if self.world.settings.is_flag_value(
            BanditsWayGate, BanditsWayGating.MALLOW
        ) or self.world.settings.is_flag_value(
            BanditsWayGate, BanditsWayGating.HAMMER_BRO
        ):
            return 4
        return 2


class MushroomKingdomOccupiedLocation(_Area1Location):
    """Base class for MushroomKingdomOccupiedLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.MUSHROOM_KINGDOM_OCCUPIED_ONLY

    def can_access(self, inventory: Inventory):
        return can_defeat_bandits_way_boss(self.world, inventory)

    @property
    def tier(self) -> int:
        if self.world.settings.is_flag_value(
            BanditsWayGate, BanditsWayGating.MALLOW
        ) or self.world.settings.is_flag_value(
            BanditsWayGate, BanditsWayGating.HAMMER_BRO
        ):
            return 4
        return 2


class KeroSewersLocation(_Area2Location):
    """Base class for KeroSewersLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.KERO_SEWERS
    _tier: int = 2


class MidasRiverLocation(_Area2Location):
    """Base class for MidasRiverLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.MIDAS_RIVER


class TadpolePondLocation(_Area2Location):
    """Base class for TadpolePondLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.TADPOLE_POND


class RoseWayLocation(_Area2Location):
    """Base class for RoseWayLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.ROSE_WAY
    _tier: int = 2


class RoseTownLocation(_Area2Location):
    """Base class for RoseTownLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.ROSE_TOWN


class ForestLocation(_Area2Location):
    """Base class for ForestLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.ROSE_TOWN

    def can_access(self, inventory: Inventory):
        return can_access_forest(self.world, inventory)

    @property
    def tier(self) -> int:
        if self.world.settings.is_flag_value(ForestMazeGate, ForestMazeGating.OPEN):
            return 2
        return 4


class PipeVaultLocation(_Area2Location):
    """Base class for PipeVaultLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.PIPE_VAULT

    def can_access(self, inventory: Inventory):
        return can_access_pipe_vault(self.world, inventory)

    @property
    def tier(self) -> int:
        if self.world.settings.is_flag_value(PipeVaultGate, PipeVaultGating.OPEN):
            return 2
        return 4


class YosterIsleLocation(_Area2Location):
    """Base class for YosterIsleLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.YOSTER_ISLE

    def can_access(self, inventory: Inventory):
        return can_access_pipe_vault(self.world, inventory)


class MolevilleLocation(_Area3Location):
    """Base class for MolevilleLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.MOLEVILLE


class MinesLocation(_Area3Location):
    """Base class for MinesLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.MOLEVILLE_MINES

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_moleville_entrance(self.world, inventory)

    @property
    def tier(self) -> int:
        if self.world.settings.is_flag_value(Moleville1Gate, Moleville1Gating.OPEN):
            return 2
        return 4


class InnerMinesLocation(_Area3Location):
    """Base class for InnerMinesLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.MOLEVILLE_MINES

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_inner_mines(self.world, inventory)


class BoosterPassLocation(_Area3Location):
    """Base class for BoosterPassLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.BOOSTER_PASS


class BoosterTowerExteriorLocation(_Area3Location):
    """Base class for BoosterTowerExteriorLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.BOOSTER_TOWER


class BoosterTowerLocation(_Area3Location):
    """Base class for BoosterTowerLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.BOOSTER_TOWER

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_tower(self.world, inventory)

    @property
    def tier(self) -> int:
        if self.world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.OPEN):
            return 2
        return 4


class MarrymoreLocation(_Area3Location):
    """Base class for MarrymoreLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.MARRYMORE


class MarrymoreChapelLocation(_Area3Location):
    """Base class for MarrymoreChapelLocation items"""

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_chapel(self.world, inventory)

    @property
    def tier(self) -> int:
        if self.world.settings.is_flag_value(
            MarrymoreGate, MarrymoreGating.KGGG
        ) or self.world.settings.is_flag_value(MarrymoreGate, MarrymoreGating.TOWER):
            return 4
        return 2


class StarHillLocation(_Area4Location):
    """Base class for StarHillLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.STAR_HILL


class SeasideTownLocation(_Area4Location):
    """Base class for SeasideTownLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.SEASIDE_TOWN


class SeaLocation(_Area4Location):
    """Base class for SeaLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.SEA

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_sea(self.world, inventory)

    @property
    def tier(self) -> int:
        if self.world.settings.is_flag_value(SeaGate, SeaGating.OPEN):
            return 2
        return 4


class SunkenShipLocation(_Area4Location):
    """Base class for SunkenShipLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.SUNKEN_SHIP

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_sea(self.world, inventory)

    @property
    def tier(self) -> int:
        if self.world.settings.is_flag_value(SeaGate, SeaGating.OPEN):
            return 2
        return 4


class InnerSunkenShipLocation(_Area4Location):
    """Base class for InnerSunkenShipLocation items"""

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_ship_midboss(self.world, inventory)


class LandsEndLocation(_Area5Location):
    """Base class for LandsEndLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.LANDS_END
    _tier: int = 2


class TempleLocation(_Area5Location):
    """Base class for TempleLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.BELOME_TEMPLE
    _tier: int = 2


class InnerTempleLocation(_Area5Location):
    """Base class for InnerTempleLocation items"""

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_temple(self.world, inventory)

    @property
    def tier(self) -> int:
        if self.world.settings.is_flag_value(BelomeTempleGate, BelomeTempleGating.OPEN):
            return 2
        return 4


class TreasuryLocation(_Area5Location):
    """Base class for TreasuryLocation items"""

    def can_access(self, inventory: Inventory) -> bool:
        return super().can_access(inventory) and inventory.has_item(TempleKey)


class MonstroTownLocation(_Area5Location):
    """Base class for MonstroTownLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.MONSTRO_TOWN

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_monstro_town(self.world, inventory)


class BeanValleyLocation(_Area5Location):
    """Base class for BeanValleyLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.BEAN_VALLEY
    _tier: int = 2


class CasinoLocation(_Area5Location):
    """Base class for CasinoLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.CASINO

    def can_access(self, inventory: Inventory) -> bool:
        return inventory.has_item(BrightCard)


class NimbusTownLocation(_Area6Location):
    """Base class for NimbusTownLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.NIMBUS_LAND


class NimbusCastleLocation(_Area6Location):
    """Base class for NimbusCastleLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.NIMBUS_CASTLE


class NimbusMidCastleLocation(_Area6Location):
    """Base class for NimbusMidCastleLocation items"""

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_inner_nimbus(self.world, inventory)


class NimbusDeepCastleLocation(_Area6Location):
    """Base class for NimbusDeepCastleLocation items"""

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_late_nimbus(self.world, inventory)


class BarrelVolcanoLocation(_Area6Location):
    """Base class for BarrelVolcanoLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.BARREL_VOLCANO

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_volcano(self.world, inventory)

    @property
    def tier(self) -> int:
        if self.world.settings.is_flag_value(
            BarrelVolcanoGate, BarrelVolcanoGating.OPEN
        ):
            return 2
        return 4


class BowsersKeepLocation(_Area7Location):
    """Base class for BowsersKeepLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.BOWSERS_KEEP

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_keep(self.world, inventory)

    @property
    def tier(self) -> int:
        if self.world.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.OPEN):
            return 2
        return 4


class BowsersKeepObstacleLocation(_Area7Location):
    """Base class for BowsersKeepObstacleLocation items"""

    def can_access(self, inventory: Inventory) -> bool:
        if self.world.settings.is_boolean_flag_enabled(BowserDoorShuffle):
            return can_defeat_battle_door_boss(
                self.world, inventory
            )  # Necessary in case of bowser door shuffle.
        return can_access_keep(self.world, inventory)


class OuterFactoryLocation(_Area7Location):
    """Base class for OuterFactoryLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.FACTORY

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_factory(self.world, inventory)

    @property
    def tier(self) -> int:
        if self.world.settings.is_flag_value(
            FactoryGate, FactoryGating.OPEN
        ) and self.world.settings.is_flag_value(
            BowsersKeepGate, BowsersKeepGating.OPEN
        ):
            return 2
        return 4


class MidFactoryLocation(_Area7Location):
    """Base class for MidFactoryLocation items"""

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_first_factory_boss(self.world, inventory)


class InnerFactoryLocation(_Area7Location):
    """Base class for InnerFactoryLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.FACTORY

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_second_factory_boss(self.world, inventory)
