"""Generic location classes belonging to world areas, with associated access logic."""

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

from randomizer.types.progress_locations.classes import (
    Inventory,
    ProgressLocation,
    LocationWorldArea,
)
from randomizer.types.world.flags import BowserDoorShuffle


class MariosPadLocation(ProgressLocation):
    """Base class for MariosPadLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.MARIOS_PAD


class MushroomWayLocation(ProgressLocation):
    """Base class for MushroomWayLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.MUSHROOM_WAY


class MushroomKingdomLocation(ProgressLocation):
    """Base class for MushroomKingdomLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.MUSHROOM_KINGDOM


class BanditsWayLocation(ProgressLocation):
    """Base class for BanditsWayLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.BANDITS_WAY

    def can_access(self, inventory: Inventory):
        return can_access_bandits_way(self.world, inventory)


class MushroomKingdomOccupiedLocation(ProgressLocation):
    """Base class for MushroomKingdomOccupiedLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.MUSHROOM_KINGDOM_OCCUPIED_ONLY

    def can_access(self, inventory: Inventory):
        return can_defeat_bandits_way_boss(self.world, inventory)


class KeroSewersLocation(ProgressLocation):
    """Base class for KeroSewersLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.KERO_SEWERS


class MidasRiverLocation(ProgressLocation):
    """Base class for MidasRiverLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.MIDAS_RIVER


class TadpolePondLocation(ProgressLocation):
    """Base class for TadpolePondLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.TADPOLE_POND


class RoseWayLocation(ProgressLocation):
    """Base class for RoseWayLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.ROSE_WAY


class RoseTownLocation(ProgressLocation):
    """Base class for RoseTownLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.ROSE_TOWN


class ForestLocation(ProgressLocation):
    """Base class for ForestLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.ROSE_TOWN

    def can_access(self, inventory: Inventory):
        return can_access_forest(self.world, inventory)


class PipeVaultLocation(ProgressLocation):
    """Base class for PipeVaultLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.PIPE_VAULT

    def can_access(self, inventory: Inventory):
        return can_access_pipe_vault(self.world, inventory)


class YosterIsleLocation(ProgressLocation):
    """Base class for YosterIsleLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.YOSTER_ISLE

    def can_access(self, inventory: Inventory):
        return can_access_pipe_vault(self.world, inventory)


class MolevilleLocation(ProgressLocation):
    """Base class for MolevilleLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.MOLEVILLE


class MinesLocation(ProgressLocation):
    """Base class for MinesLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.MOLEVILLE_MINES

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_moleville_entrance(self.world, inventory)


class InnerMinesLocation(MinesLocation):
    """Base class for InnerMinesLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.MOLEVILLE_MINES

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_inner_mines(self.world, inventory)


class BoosterPassLocation(ProgressLocation):
    """Base class for BoosterPassLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.BOOSTER_PASS


class BoosterTowerExteriorLocation(ProgressLocation):
    """Base class for BoosterTowerExteriorLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.BOOSTER_TOWER


class BoosterTowerLocation(ProgressLocation):
    """Base class for BoosterTowerLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.BOOSTER_TOWER

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_tower(self.world, inventory)


class MarrymoreLocation(ProgressLocation):
    """Base class for MarrymoreLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.MARRYMORE


class MarrymoreChapelLocation(MarrymoreLocation):
    """Base class for MarrymoreChapelLocation items"""

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_chapel(self.world, inventory)


class StarHillLocation(ProgressLocation):
    """Base class for StarHillLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.STAR_HILL


class SeasideTownLocation(ProgressLocation):
    """Base class for SeasideTownLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.SEASIDE_TOWN


class SeaLocation(ProgressLocation):
    """Base class for SeaLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.SEA

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_sea(self.world, inventory)


class SunkenShipLocation(ProgressLocation):
    """Base class for SunkenShipLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.SUNKEN_SHIP

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_sea(self.world, inventory)


class InnerSunkenShipLocation(SunkenShipLocation):
    """Base class for InnerSunkenShipLocation items"""

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_ship_midboss(self.world, inventory)


class LandsEndLocation(ProgressLocation):
    """Base class for LandsEndLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.LANDS_END


class TempleLocation(ProgressLocation):
    """Base class for TempleLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.BELOME_TEMPLE


class InnerTempleLocation(TempleLocation):
    """Base class for InnerTempleLocation items"""

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_temple(self.world, inventory)


class TreasuryLocation(InnerTempleLocation):
    """Base class for TreasuryLocation items"""

    def can_access(self, inventory: Inventory) -> bool:
        return super().can_access(inventory) and inventory.has_item(TempleKey)


class MonstroTownLocation(ProgressLocation):
    """Base class for MonstroTownLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.MONSTRO_TOWN

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_monstro_town(self.world, inventory)


class BeanValleyLocation(ProgressLocation):
    """Base class for BeanValleyLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.BEAN_VALLEY


class CasinoLocation(ProgressLocation):
    """Base class for CasinoLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.CASINO

    def can_access(self, inventory: Inventory) -> bool:
        return inventory.has_item(BrightCard)


class NimbusTownLocation(ProgressLocation):
    """Base class for NimbusTownLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.NIMBUS_LAND


class NimbusCastleLocation(ProgressLocation):
    """Base class for NimbusCastleLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.NIMBUS_CASTLE


class NimbusMidCastleLocation(NimbusCastleLocation):
    """Base class for NimbusMidCastleLocation items"""

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_inner_nimbus(self.world, inventory)


class NimbusDeepCastleLocation(NimbusCastleLocation):
    """Base class for NimbusDeepCastleLocation items"""

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_late_nimbus(self.world, inventory)


class BarrelVolcanoLocation(ProgressLocation):
    """Base class for BarrelVolcanoLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.BARREL_VOLCANO

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_volcano(self.world, inventory)


class BowsersKeepLocation(ProgressLocation):
    """Base class for BowsersKeepLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.BOWSERS_KEEP

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_keep(self.world, inventory)


class BowsersKeepObstacleLocation(BowsersKeepLocation):
    """Base class for BowsersKeepObstacleLocation items"""

    def can_access(self, inventory: Inventory) -> bool:
        if self.world.settings.is_boolean_flag_enabled(BowserDoorShuffle):
            return can_defeat_battle_door_boss(
                self.world, inventory
            )  # Necessary in case of bowser door shuffle.
        return can_access_keep(self.world, inventory)


class OuterFactoryLocation(ProgressLocation):
    """Base class for OuterFactoryLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.FACTORY

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_factory(self.world, inventory)


class MidFactoryLocation(OuterFactoryLocation):
    """Base class for MidFactoryLocation items"""

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_first_factory_boss(self.world, inventory)


class InnerFactoryLocation(ProgressLocation):
    """Base class for InnerFactoryLocation items"""

    _world_area: LocationWorldArea = LocationWorldArea.FACTORY

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_second_factory_boss(self.world, inventory)
