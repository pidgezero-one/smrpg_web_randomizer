from randomizer.entities.items.items import BrightCard, TempleKey
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
    can_defeat_temple_boss,
)
from randomizer.types.progress_locations.classes import Inventory, ProgressLocation
from randomizer.types.progress_locations.enums import LocationWorldArea
from randomizer.types.world.flags.flags import BowserDoorShuffle


class MariosPadLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.MariosPad


class MushroomWayLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.MushroomWay


class MushroomKingdomLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.MushroomKingdom


class BanditsWayLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.BanditsWay

    def can_access(self, inventory: Inventory):
        return can_access_bandits_way(self.world, inventory)


class MushroomKingdomOccupiedLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.MushroomKingdomOccupiedOnly

    def can_access(self, inventory: Inventory):
        return can_defeat_bandits_way_boss(self.world, inventory)


class KeroSewersLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.KeroSewers


class MidasRiverLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.MidasRiver


class TadpolePondLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.TadpolePond


class RoseWayLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.RoseWay


class RoseTownLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.RoseTown


class ForestLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.RoseTown

    def can_access(self, inventory: Inventory):
        return can_access_forest(self.world, inventory)


class PipeVaultLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.PipeVault

    def can_access(self, inventory: Inventory):
        return can_access_pipe_vault(self.world, inventory)


class YosterIsleLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.YosterIsle

    def can_access(self, inventory: Inventory):
        return can_access_pipe_vault(self.world, inventory)


class MolevilleLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.Moleville


class MinesLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.MolevilleMines

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_moleville_entrance(self.world, inventory)


class InnerMinesLocation(MinesLocation):
    _world_area: LocationWorldArea = LocationWorldArea.MolevilleMines

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_inner_mines(self.world, inventory)


class BoosterPassLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.BoosterPass


class BoosterTowerExteriorLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.BoosterTower


class BoosterTowerLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.BoosterTower

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_tower(self.world, inventory)


class MarrymoreLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.Marrymore


class MarrymoreChapelLocation(MarrymoreLocation):
    def can_access(self, inventory: Inventory) -> bool:
        return can_access_chapel(self.world, inventory)


class StarHillLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.StarHill


class SeasideTownLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.SeasideTown


class SeaLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.Sea

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_sea(self.world, inventory)


class SunkenShipLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.SunkenShip

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_sea(self.world, inventory)


class InnerSunkenShipLocation(SunkenShipLocation):
    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_ship_midboss(self.world, inventory)


class LandsEndLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.LandsEnd


class TempleLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.BelomeTemple


class InnerTempleLocation(TempleLocation):
    def can_access(self, inventory: Inventory) -> bool:
        return can_access_temple(self.world, inventory)


class TreasuryLocation(InnerTempleLocation):
    def can_access(self, inventory: Inventory) -> bool:
        return super().can_access(inventory) and inventory.has_item(TempleKey)


class MonstroTownLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.MonstroTown

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_monstro_town(self.world, inventory)


class BeanValleyLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.BeanValley


class CasinoLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.Casino

    def can_access(self, inventory: Inventory) -> bool:
        return inventory.has_item(BrightCard)


class NimbusTownLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.NimbusLand


class NimbusCastleLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.NimbusCastle


class NimbusMidCastleLocation(NimbusCastleLocation):
    def can_access(self, inventory: Inventory) -> bool:
        return can_access_inner_nimbus(self.world, inventory)


class NimbusDeepCastleLocation(NimbusCastleLocation):
    def can_access(self, inventory: Inventory) -> bool:
        return can_access_late_nimbus(self.world, inventory)


class BarrelVolcanoLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.BarrelVolcano

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_volcano(self.world, inventory)


class BowsersKeepLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.BowsersKeep

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_keep(self.world, inventory)


class BowsersKeepObstacleLocation(BowsersKeepLocation):
    def can_access(self, inventory: Inventory) -> bool:
        if self.world.settings.is_boolean_flag_enabled(BowserDoorShuffle):
            return can_defeat_battle_door_boss(
                self.world, inventory
            )  # Necessary in case of bowser door shuffle.
        return can_access_keep(self.world, inventory)


class OuterFactoryLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.Factory

    def can_access(self, inventory: Inventory) -> bool:
        return can_access_factory(self.world, inventory)


class MidFactoryLocation(OuterFactoryLocation):
    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_first_factory_boss(self.world, inventory)


class InnerFactoryLocation(ProgressLocation):
    _world_area: LocationWorldArea = LocationWorldArea.Factory

    def can_access(self, inventory: Inventory) -> bool:
        return can_defeat_second_factory_boss(self.world, inventory)


# class BowsersKeepPastBattleDoorsLocation(BowsersKeepLocation):
#     _world_area: LocationWorldArea = LocationWorldArea.BowsersKeep

#     def can_access(self, inventory: Inventory) -> bool:
#         keep_access = can_access_keep(self.world, inventory)

#         if self.world.settings.get_flag(BowserDoorRequirements).value == 6:
#             return keep_access and can_defeat_battle_door_boss(self.world, inventory)
#         return keep_access
