# Data module for chest data.

from randomizer.data import items
from randomizer.logic.utils import isclass_or_instance
from . import locations


# ******* Chest location classes


class Chest(locations.ItemLocation):
    """Subclass for treasure chest location."""

    ms_override = False


class NonCoinChest(Chest):
    """Subclass for chest that cannot contain coin items."""

    def item_allowed(self, item):
        """

        Args:
            item(randomizer.data.items.Item|type): Item to check.

        Returns:
            bool: True if the given item is allowed to be placed in this spot, False otherwise.

        """
        return super().item_allowed(item) and not isclass_or_instance(item, items.Coins)


class StarAllowedChest(Chest):
    """Subclass for chests that are in the same room as an invincibility star."""

    def item_allowed(self, item):
        """

        Args:
            item(randomizer.data.items.Item|type): Item to check.

        Returns:
            bool: True if the given item is allowed to be placed in this spot, False otherwise.

        """
        return super().item_allowed(item) or isclass_or_instance(
            item, items.InvincibilityStar
        )


class RoseTownGardenerChest(Chest):
    """Subclass for the Lazy Shell chests in Rose Town."""

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.Seed) and inventory.has_item(items.Fertilizer)


class MolevilleMinesBackChest(Chest):
    """Subclass for the back chests in Moleville Mines requiring Bambino Bomb to access."""

    @staticmethod
    def can_access(inventory):
        return locations.can_access_mines_back(inventory)


class BowserDoorReward(Chest):
    """Subclass for Bowser door rewards because they can only be inventory items or you missed."""

    def item_allowed(self, item):
        """

        Args:
            item(randomizer.data.items.Item|type): Item to check.

        Returns:
            bool: True if the given item is allowed to be placed in this spot, False otherwise.

        """
        return super().item_allowed(item) and not isclass_or_instance(
            item, items.ChestReward
        )


# ******* NPC reward data classes


class Reward(locations.ItemLocation):
    """Subclass for NPC reward location."""

    def item_allowed(self, item):
        # NPC rewards cannot contain "You Missed!" or chest-only rewards.
        # FIXME: Non-KI NPC rewards don't work with progressive cards for now.  Remove this when fixed.
        return super().item_allowed(item) and not isclass_or_instance(
            item, (items.AltoCard, items.ChestReward)
        )


class TreasureSellerReward(Reward):
    """Subclass for Moleville treasure seller NPC to check access.  Need to beat mines to unlock this."""

    @staticmethod
    def can_access(inventory):
        return locations.can_access_mines_back(inventory)


class BelomeTempleTreasure(Reward):
    """Subclass for Belome Temple rewards."""

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.TempleKey)


# ****************************** Actual chest classes

# *** Mushroom Way


class MushroomWay1(Chest):
    area = locations.Area.MushroomWay
    addresses = [0x14B389]
    item = items.Coins5
    access = 1


class MushroomWay2(Chest):
    area = locations.Area.MushroomWay
    addresses = [0x14B38D]
    item = items.Coins8
    access = 1


class MushroomWay3(Chest):
    area = locations.Area.MushroomWay
    addresses = [0x14B3DA]
    item = items.Flower
    access = 2


class MushroomWay4(Chest):
    area = locations.Area.MushroomWay
    addresses = [0x14B3DE]
    item = items.RecoveryMushroom
    access = 1


class ToadRescue1(Reward):
    area = locations.Area.MushroomWay
    addresses = [0x1EFEDC]
    item = items.HoneySyrup
    access = 2


class ToadRescue2(Reward):
    area = locations.Area.MushroomWay
    addresses = [0x1EFE1E]
    item = items.FlowerTab
    access = 2


class HammerBrosReward(Reward):
    area = locations.Area.MushroomWay
    addresses = [0x1E94C4]
    item = items.Hammer
    access = 3


# *** Mushroom Kingdom


class MushroomKingdomVault1(Chest):
    area = locations.Area.MushroomKingdom
    addresses = [0x148AD3]
    item = items.Coins10
    access = 1


class MushroomKingdomVault2(Chest):
    area = locations.Area.MushroomKingdom
    addresses = [0x148ADF]
    item = items.RecoveryMushroom
    access = 1


class MushroomKingdomVault3(Chest):
    area = locations.Area.MushroomKingdom
    addresses = [0x148AEB]
    item = items.Flower
    access = 1


class WalletGuy1(Reward):
    area = locations.Area.MushroomKingdom
    addresses = [0x1E3765]
    item = items.FlowerTab
    missable = True
    access = 4


class WalletGuy2(Reward):
    area = locations.Area.MushroomKingdom
    addresses = [0x1E17DE]
    item = items.FrogCoin
    missable = True
    access = 4


class MushroomKingdomStore(Reward):
    area = locations.Area.MushroomKingdom
    addresses = [0x1E65F8]
    item = items.PickMeUp
    access = 1


class PeachSurprise(Reward):
    area = locations.Area.MushroomKingdom
    addresses = [0x1E26B2]
    item = items.Mushroom
    access = 2


class InvasionFamily(Reward):
    area = locations.Area.MushroomKingdom
    addresses = [0x1E3A74, 0x1E39B9]
    item = items.FlowerTab
    missable = True
    access = 3


class InvasionGuestRoom(Reward):
    area = locations.Area.MushroomKingdom
    addresses = [0x1E3373]
    item = items.WakeUpPin
    missable = True
    access = 3


class InvasionGuard(Reward):
    area = locations.Area.MushroomKingdom
    addresses = [0x1E3514]
    item = items.FlowerTab
    missable = True
    access = 3


# *** Bandit's Way


class BanditsWay1(Chest):
    area = locations.Area.BanditsWay
    addresses = [0x14B535]
    item = items.KerokeroCola
    access = 1


class BanditsWay2(Chest):
    area = locations.Area.BanditsWay
    addresses = [0x1495FF]
    item = items.RecoveryMushroom
    access = 1


class BanditsWayStarChest(StarAllowedChest):
    area = locations.Area.BanditsWay
    addresses = [0x14964C]
    item = items.BanditsWayStar
    access = 1


class BanditsWayDogJump(StarAllowedChest):
    area = locations.Area.BanditsWay
    addresses = [0x149650]
    item = items.Flower
    access = 3


class BanditsWayCroco(Chest):
    area = locations.Area.BanditsWay
    addresses = [0x14B494]
    item = items.RecoveryMushroom
    access = 1


class Croco1Reward(Reward):
    area = locations.Area.BanditsWay
    addresses = [0x1E94F0]
    item = items.Wallet
    access = 3


# *** Kero Sewers


class KeroSewersPandoriteRoom(Chest):
    area = locations.Area.KeroSewers
    addresses = [0x149053]
    item = items.Flower
    access = 1


class KeroSewersStarChest(StarAllowedChest):
    area = locations.Area.KeroSewers
    addresses = [0x14901E]
    item = items.KeroSewersStar
    access = 1


class PandoriteReward(Reward):
    area = locations.Area.KeroSewers
    addresses = [0x1E950D]
    item = items.TrueformPin
    access = 3


# *** Midas River


class MidasRiverFirstTime(Reward):
    area = locations.Area.MidasRiver
    addresses = [0x205FD3]
    item = items.NokNokShell
    access = 3


# *** Tadpole Pond


class CricketPieReward(Reward):
    area = locations.Area.TadpolePond
    addresses = [0x1E6636]
    item = items.FroggieStick
    access = 3

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.CricketPie)


class CricketJamReward(Reward):
    area = locations.Area.TadpolePond
    addresses = [0x1E6642]
    item = items.FrogCoin
    access = 3
    num_frog_coins = 10

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.CricketJam)

    def get_patch(self):
        patch = super().get_patch()

        # If we're giving frog coins at this spot, write the number of frog coins to a special address.
        if isclass_or_instance(self.item, items.FrogCoin):
            patch.add_data(0x1E6650, self.num_frog_coins)
        # Otherwise extra bytes are needed to enable this spot to use the regular item granting subroutine.
        else:
            patch.add_data(0x1E6631, bytes([0x40, 0x66]))

        return patch


# *** Rose Way


class RoseWayPlatform(Chest):
    area = locations.Area.RoseWay
    addresses = [0x14973E]
    item = items.FrogCoin
    access = 2


# *** Rose Town


class RoseTownStore1(Chest):
    area = locations.Area.RoseTown
    addresses = [0x1499AD]
    item = items.Flower
    access = 1


class RoseTownStore2(Chest):
    area = locations.Area.RoseTown
    addresses = [0x1499B9]
    item = items.FrogCoin
    access = 1


class GardenerCloud1(RoseTownGardenerChest):
    area = locations.Area.RoseTownClouds
    addresses = [0x14DE24]
    item = items.LazyShellArmor
    access = 4
    ms_override = True


class GardenerCloud2(RoseTownGardenerChest):
    area = locations.Area.RoseTownClouds
    addresses = [0x14DE28]
    item = items.LazyShellWeapon
    access = 4
    ms_override = True


class RoseTownToad(Reward):
    area = locations.Area.RoseTown
    addresses = [0x1E6030]
    item = items.FlowerTab
    missable = True
    access = 3


class Gaz(Reward):
    area = locations.Area.RoseTown
    addresses = [0x1E61FF]
    item = items.FingerShot
    access = 3


# *** Forest Maze


class ForestMaze1(Chest):
    area = locations.Area.ForestMaze
    addresses = [0x14B75E]
    item = items.KerokeroCola
    access = 1


class ForestMaze2(Chest):
    area = locations.Area.ForestMaze
    addresses = [0x14B872]
    item = items.FrogCoin
    access = 1


class ForestMazeUnderground1(Chest):
    area = locations.Area.ForestMaze
    addresses = [0x14BB9D]
    item = items.KerokeroCola
    access = 1


class ForestMazeUnderground2(Chest):
    area = locations.Area.ForestMaze
    addresses = [0x14BBA1]
    item = items.Flower
    access = 3


class ForestMazeUnderground3(Chest):
    area = locations.Area.ForestMaze
    addresses = [0x14BBA5]
    item = items.YouMissed
    access = 2


class ForestMazeRedEssence(Chest):
    area = locations.Area.ForestMaze
    addresses = [0x14B841]
    item = items.RedEssence
    access = 2


# *** Pipe Vault


class PipeVaultSlide1(Chest):
    area = locations.Area.PipeVault
    addresses = [0x14A2B7]
    item = items.Flower
    access = 2


class PipeVaultSlide2(Chest):
    area = locations.Area.PipeVault
    addresses = [0x14A2C3]
    item = items.FrogCoin
    access = 2


class PipeVaultSlide3(Chest):
    area = locations.Area.PipeVault
    addresses = [0x14A2CF]
    item = items.FrogCoin
    access = 2


class PipeVaultNippers1(Chest):
    area = locations.Area.PipeVault
    addresses = [0x14A33E]
    item = items.Flower
    access = 2


class PipeVaultNippers2(Chest):
    area = locations.Area.PipeVault
    addresses = [0x14A34A]
    item = items.CoinsDoubleBig
    access = 2


class GoombaThumping1(Reward):
    area = locations.Area.PipeVault
    addresses = [0x1E3F9C]
    item = items.FlowerTab
    access = 3


class GoombaThumping2(Reward):
    area = locations.Area.PipeVault
    addresses = [0x1E3FAE]
    item = items.FlowerJar
    access = 3


# *** Yo'ster Isle


class YosterIsleEntrance(Chest):
    area = locations.Area.YosterIsle
    addresses = [0x148B39]
    item = items.FrogCoin
    access = 3


# *** Moleville


class TreasureSeller1(TreasureSellerReward):
    area = locations.Area.Moleville
    addresses = [0x1F8CA5]
    item = items.LuckyJewel
    access = 4
    dialogs_to_replace = [2911]


class TreasureSeller2(TreasureSellerReward):
    area = locations.Area.Moleville
    addresses = [0x1F8CD1]
    item = items.MysteryEgg
    access = 4
    dialogs_to_replace = [2908]


class TreasureSeller3(TreasureSellerReward):
    area = locations.Area.Moleville
    addresses = [0x1F8CFD]
    item = items.FryingPan
    access = 4
    dialogs_to_replace = [2914]


# *** Moleville Mines


class MolevilleMinesStarChest(MolevilleMinesBackChest, StarAllowedChest):
    area = locations.Area.MolevilleMines
    addresses = [0x14C4AF]
    item = items.MolevilleMinesStar
    access = 3


class MolevilleMinesCoins(MolevilleMinesBackChest):
    area = locations.Area.MolevilleMines
    addresses = [0x14C3C6]
    item = items.Coins150
    access = 3


class MolevilleMinesPunchinello1(MolevilleMinesBackChest):
    area = locations.Area.MolevilleMines
    addresses = [0x14C546]
    item = items.RecoveryMushroom
    access = 3


class MolevilleMinesPunchinello2(MolevilleMinesBackChest):
    area = locations.Area.MolevilleMines
    addresses = [0x14C552]
    item = items.Flower
    access = 3


class CrocoFlunkie1(Reward):
    area = locations.Area.MolevilleMines
    addresses = [0x202073]
    item = items.FlowerTab
    missable = True
    access = 3


class CrocoFlunkie2(Reward):
    area = locations.Area.MolevilleMines
    addresses = [0x2020CC]
    item = items.FlowerTab
    missable = True
    access = 3


class CrocoFlunkie3(Reward):
    area = locations.Area.MolevilleMines
    addresses = [0x202123]
    item = items.FlowerTab
    missable = True
    access = 3


# *** Booster Pass


class BoosterPass1(Chest):
    area = locations.Area.BoosterPass
    addresses = [0x149C62]
    item = items.Flower
    access = 2


class BoosterPass2(Chest):
    area = locations.Area.BoosterPass
    addresses = [0x149C6E]
    item = items.RockCandy
    access = 1


class BOOSTER_PASS_SECRET_1(Chest):
    area = locations.Area.BoosterPass
    addresses = [0x14DA32]
    item = items.FrogCoin
    access = 3


class BOOSTER_PASS_SECRET_2(Chest):
    area = locations.Area.BoosterPass
    addresses = [0x14DA36]
    item = items.Flower
    access = 3


class BOOSTER_PASS_SECRET_3(Chest):
    area = locations.Area.BoosterPass
    addresses = [0x14DA42]
    item = items.KerokeroCola
    access = 3


# *** Booster Tower


class BOOSTER_TOWER_SPOOKUM(Chest):
    area = locations.Area.BoosterTower
    addresses = [0x14B23E]
    item = items.FrogCoin
    access = 1


class BOOSTER_TOWER_THWOMP(Chest):
    area = locations.Area.BoosterTower
    addresses = [0x148C60]
    item = items.RecoveryMushroom
    access = 1


class BOOSTER_TOWER_MASHER(Reward):
    area = locations.Area.BoosterTower
    addresses = [0x1F9CE9]
    item = items.Masher
    access = 3


class BOOSTER_TOWER_PARACHUTE(Chest):
    area = locations.Area.BoosterTower
    addresses = [0x148C2F]
    item = items.FrogCoin
    access = 1


class BOOSTER_TOWER_ZOOM_SHOES(Chest):
    area = locations.Area.BoosterTower
    addresses = [0x148EAC]
    item = items.ZoomShoes
    access = 3
    ms_override = True

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.RoomKey)


class BOOSTER_TOWER_TOP_1(NonCoinChest):
    area = locations.Area.BoosterTower
    addresses = [0x14B2D1]
    item = items.FrogCoin
    access = 2


class BOOSTER_TOWER_TOP_2(Chest):
    area = locations.Area.BoosterTower
    addresses = [0x14B2E1]
    item = items.GoodieBag
    access = 2


class BOOSTER_TOWER_TOP_3(Chest):
    area = locations.Area.BoosterTower
    addresses = [0x14B325]
    item = items.RecoveryMushroom
    access = 2


class BOOSTER_TOWER_RAILWAY(Reward):
    area = locations.Area.BoosterTower
    addresses = [0x1EE468]
    item = items.FlowerTab
    access = 2


class BoosterTowerChomp(Reward):
    area = locations.Area.BoosterTower
    addresses = [0x1EE27B]
    item = items.Chomp
    access = 3

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.ElderKey)


class BoosterTowerCurtainGame(Reward):
    area = locations.Area.BoosterTower
    addresses = [0x1EF49B]
    item = items.Amulet
    access = 3


# *** Marrymore


class MARRYMORE_INN(Chest):
    area = locations.Area.Marrymore
    addresses = [0x1485D7]
    item = items.FrogCoin
    access = 1


##### NEW TO MARRYMORE #####


# Event 602 contains the # of stays after which you get these prizes.
# Can target that when applying settings.
# Byte 70D7
# test this a lot. unsure what the line that sets 70D7 to 255 is doing
class MARRYMORE_INNSuitePrize1(Reward):
    area = locations.Area.Marrymore
    event = 602
    item = items.FlowerTab
    access = 2


class MARRYMORE_INNSuitePrize2(Reward):
    area = locations.Area.Marrymore
    event = 602
    item = items.FlowerJar
    access = 3


class MARRYMORE_INNSuitePrize3(Reward):
    area = locations.Area.Marrymore
    event = 602
    item = items.FrogCoin
    access = 4


class MARRYMORE_INNSuitePrize4(Reward):
    area = locations.Area.Marrymore
    event = 602
    item = items.FrogCoin
    access = 4


class MARRYMORE_INNSuitePrize5(Reward):
    area = locations.Area.Marrymore
    event = 602
    item = items.FrogCoin
    access = 4


class MARRYMORE_INNSuitePrize6(Reward):
    area = locations.Area.Marrymore
    event = 602
    item = items.FrogCoin
    access = 4


class MARRYMORE_INNTipPrize(Reward):
    area = locations.Area.Marrymore
    event = 603
    item = items.MidMushroom
    access = 2


class MARRYMORE_INNTipPrizeAsBellhop(Reward):
    area = locations.Area.Marrymore
    event = 621
    item = items.MidMushroom
    access = 2


class MARRYMORE_INNTipPrizeAsBellhop2(Reward):
    area = locations.Area.Marrymore
    event = 621
    # make item insertion a method on this class?
    # insert it into world.scripts location of the item
    item = items.MidMushroom
    access = 2


# how about we get rid of the non-depletables and replace them with 70A7 = random # in range?
# maybe have subroutine events that choose a random item with a more complicated algo
# pick an unused consumable and set 70A7 to the result
# run it as a subroutine when granting items in event 603, event 621
# have 4 sub-events: one for each tier of item
# a 5th event determines the random chance of running each of those 4 sub-events
# i.e. maybe you always want marrymore to grant a tier 4, but like, grate guy maybe only 20% of the time

# *** Seaside Town


class SEASIDE_TOWN_RESCUE(Reward):
    area = locations.Area.SeasideTown
    addresses = [0x1ED6C7]
    item = items.FlowerBox
    access = 3

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.ShedKey)


# *** Sea


class SEA_STAR_CHEST(StarAllowedChest):
    area = locations.Area.Sea
    addresses = [0x14A458]
    item = items.SeaStar
    access = 1


class SEA_SAVE_ROOM_1(Chest):
    area = locations.Area.Sea
    addresses = [0x14A40E]
    item = items.FrogCoin
    access = 1


class SEA_SAVE_ROOM_2(Chest):
    area = locations.Area.Sea
    addresses = [0x14A412]
    item = items.Flower
    access = 1


class SEA_SAVE_ROOM_3(Chest):
    area = locations.Area.Sea
    addresses = [0x14A416]
    item = items.RecoveryMushroom
    access = 1


class SeaSaveRoom4(Chest):
    area = locations.Area.Sea
    addresses = [0x14A42F]
    item = items.MaxMushroom
    access = 2


# *** Sunken Ship


class SUNKEN_SHIP_RAT_STAIRS(Chest):
    area = locations.Area.SunkenShip
    addresses = [0x14AC26]
    item = items.Coins100
    access = 1


class SUNKEN_SHIP_SHOP(Chest):
    area = locations.Area.SunkenShip
    addresses = [0x14AC70]
    item = items.Coins100
    access = 3


class SUNKEN_SHIP_COINS_1(Chest):
    area = locations.Area.SunkenShip
    addresses = [0x14AD85]
    item = items.Coins100
    access = 3


class SUNKEN_SHIP_COINS_2(Chest):
    area = locations.Area.SunkenShip
    addresses = [0x14AD89]
    item = items.Coins100
    access = 3


class SUNKEN_SHIP_CLONE_ROOM(Chest):
    area = locations.Area.SunkenShip
    addresses = [0x14AE61]
    item = items.KerokeroCola
    access = 3


class SUNKEN_SHIP_FROG_COIN_ROOM(Chest):
    area = locations.Area.SunkenShip
    addresses = [0x14AEF5]
    item = items.FrogCoin
    access = 3


class SUNKEN_SHIP_HIDON_MUSHROOM(Chest):
    area = locations.Area.SunkenShip
    addresses = [0x14AF0E]
    item = items.RecoveryMushroom
    access = 3


class SUNKEN_SHIP_SAFETY_RING(Chest):
    area = locations.Area.SunkenShip
    addresses = [0x14AF27]
    item = items.SafetyRing
    access = 3


class SUNKEN_SHIP_BANDANA_REDS(Chest):
    area = locations.Area.SunkenShip
    addresses = [0x14895D]
    item = items.RecoveryMushroom
    access = 3


class SUNKEN_SHIP_3D_MAZE(Reward):
    area = locations.Area.SunkenShip
    addresses = [0x203B30]
    item = items.RoyalSyrup
    access = 3


class SUNKEN_SHIP_CANNONBALL_PUZZLE(Reward):
    area = locations.Area.SunkenShip
    addresses = [0x203B57]
    item = items.Mushroom
    access = 2


class SunkenShipHidonReward(Reward):
    area = locations.Area.SunkenShip
    addresses = [0x1E979C]
    item = items.SafetyBadge
    access = 4


# *** Land's End


class LandsEndRedEssence(Chest):
    area = locations.Area.LandsEnd
    addresses = [0x14A4DF]
    item = items.RedEssence
    access = 1


class LandsEndChowPit1(Chest):
    area = locations.Area.LandsEnd
    addresses = [0x14A51C]
    item = items.KerokeroCola
    access = 2


class LandsEndChowPit2(Chest):
    area = locations.Area.LandsEnd
    addresses = [0x14A528]
    item = items.FrogCoin
    access = 2


class LandsEndBeeRoom(Chest):
    area = locations.Area.LandsEnd
    addresses = [0x14A5A2]
    item = items.FrogCoin
    access = 2


class LandsEndSecret1(Chest):
    area = locations.Area.LandsEnd
    addresses = [0x14C1F4]
    item = items.FrogCoin
    access = 1


class LandsEndSecret2(Chest):
    area = locations.Area.LandsEnd
    addresses = [0x14C200]
    item = items.FrogCoin
    access = 1


class LandsEndShyAway(Chest):
    area = locations.Area.LandsEnd
    addresses = [0x14D932]
    item = items.RecoveryMushroom
    access = 1


class LandsEndStarChest1(StarAllowedChest):
    area = locations.Area.LandsEnd
    addresses = [0x14C069]
    item = items.LandsEndVolcanoStar
    access = 2


class LandsEndStarChest2(StarAllowedChest):
    area = locations.Area.LandsEnd
    addresses = [0x14C02C]
    item = items.LandsEndStar2
    access = 2


class LandsEndStarChest3(StarAllowedChest):
    area = locations.Area.LandsEnd
    addresses = [0x14C030]
    item = items.LandsEndStar3
    access = 3


class TroopaClimb(Reward):
    area = locations.Area.LandsEnd
    addresses = [0x1F5282]
    item = items.TroopaPin
    access = 3


# *** Belome Temple


class BelomeTempleFortuneTeller(Chest):
    area = locations.Area.BelomeTemple
    addresses = [0x14DE81]
    item = items.Coins50
    access = 2


class BelomeTempleAfterFortune1(Chest):
    area = locations.Area.BelomeTemple
    addresses = [0x14DF69]
    item = items.FrogCoin
    access = 2


class BelomeTempleAfterFortune2(Chest):
    area = locations.Area.BelomeTemple
    addresses = [0x14DF6D]
    item = items.Coins150
    access = 2


class BelomeTempleAfterFortune3(Chest):
    area = locations.Area.BelomeTemple
    addresses = [0x14DF79]
    item = items.FrogCoin
    access = 2


class BelomeTempleAfterFortune4(Chest):
    area = locations.Area.BelomeTemple
    addresses = [0x14DF7D]
    item = items.FrogCoin
    access = 2


class BelomeTempleTreasure1(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    addresses = [0x1F4FBA]
    item = items.RoyalSyrup
    access = 3


class BelomeTempleTreasure2(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    addresses = [0x1F4FC0]
    item = items.MaxMushroom
    access = 3


class BelomeTempleTreasure3(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    addresses = [0x1F4FC6]
    item = items.FireBomb
    access = 3


# *** Monstro Town


class MonstroTownEntrance(Chest):
    area = locations.Area.MonstroTown
    addresses = [0x14C10D]
    item = items.FrogCoin
    access = 1


class JinxDojoReward(Reward):
    area = locations.Area.MonstroTown
    addresses = [0x1E982A]
    item = items.JinxBelt
    access = 4


class CulexReward(Reward):
    area = locations.Area.MonstroTown
    addresses = [0x1E98BF]
    item = items.QuartzCharm
    access = 4

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.ShinyStone)


class SuperJumps30(Reward):
    area = locations.Area.MonstroTown
    addresses = [0x1F6B41, 0x1F6B6A]
    item = items.AttackScarf
    access = 4


class SuperJumps100(Reward):
    area = locations.Area.MonstroTown
    addresses = [0x1F6B8F]
    item = items.SuperSuit
    access = 4


class ThreeMustyFears(Reward):
    area = locations.Area.MonstroTown
    addresses = [0x1F7160]
    item = items.GhostMedal
    access = 4

    @staticmethod
    def can_access(inventory):
        return (
            inventory.has_item(items.BigBooFlag)
            and inventory.has_item(items.GreaperFlag)
            and inventory.has_item(items.DryBonesFlag)
        )


# *** Bean Valley


class BeanValley1(Chest):
    area = locations.Area.BeanValley
    addresses = [0x14BDE3]
    item = items.Flower
    access = 2


class BeanValley2(Chest):
    area = locations.Area.BeanValley
    addresses = [0x14BDEF]
    item = items.FrogCoin
    access = 1


class BeanValleyBoxBoyRoom(NonCoinChest):
    area = locations.Area.BeanValley
    addresses = [0x14CC58]
    item = items.RedEssence
    access = 2


class BeanValleySlotRoom(NonCoinChest):
    area = locations.Area.BeanValley
    addresses = [0x14CF7E]
    item = items.KerokeroCola
    access = 2


class BeanValleyPiranhaPlants(Chest):
    area = locations.Area.BeanValley
    addresses = [0x14BDB6]
    item = items.FrogCoin
    access = 2


class BeanValleyBeanstalk(NonCoinChest):
    area = locations.Area.BeanValley
    addresses = [0x14D444]
    item = items.Flower
    access = 3


class BeanValleyCloud1(Chest):
    area = locations.Area.BeanValley
    addresses = [0x14D2F1]
    item = items.FrogCoin
    access = 3


class BeanValleyCloud2(NonCoinChest):
    area = locations.Area.BeanValley
    addresses = [0x14D2FD]
    item = items.RareScarf
    access = 3


class BeanValleyFall1(Chest):
    area = locations.Area.BeanValley
    addresses = [0x14D316]
    item = items.Flower
    access = 3


class BeanValleyFall2(NonCoinChest):
    area = locations.Area.BeanValley
    addresses = [0x14D322]
    item = items.Flower
    access = 3


# *** Nimbus Land


class NimbusLandShop(NonCoinChest):
    area = locations.Area.NimbusLand
    addresses = [0x14CE25]
    item = items.FrogCoin
    access = 1


class NimbusLandInn(Reward):
    area = locations.Area.NimbusLand
    addresses = [0x1E122C]
    item = items.RedEssence
    access = 3

    def item_allowed(self, item):
        """FIXME: This spot grants the same item twice, it must be one-time consumables only until item code fixed."""
        return super().item_allowed(item) and item.consumable and not item.reuseable


class NimbusCastleBeforeBirdo1(Chest):
    area = locations.Area.NimbusLand
    addresses = [0x14A088]
    item = items.Flower
    missable = True
    access = 1


class NimbusCastleBeforeBirdo2(Chest):
    area = locations.Area.NimbusLand
    addresses = [0x14EDA7]
    item = items.FrogCoin
    access = 4


class NimbusCastleOutOfBounds1(NonCoinChest):
    area = locations.Area.NimbusLand
    addresses = [0x14DB97]
    item = items.FrogCoin
    access = 2


class NimbusCastleOutOfBounds2(Chest):
    area = locations.Area.NimbusLand
    addresses = [0x14DBA3]
    item = items.FrogCoin
    access = 2


class NimbusCastleSingleGoldBird(Chest):
    area = locations.Area.NimbusLand
    addresses = [0x149F47]
    item = items.RecoveryMushroom
    access = 1


class NimbusCastleStarChest(StarAllowedChest):
    area = locations.Area.NimbusLand
    addresses = [0x14A1A3]
    item = items.NimbusLandStar
    missable = True
    access = 4

    @staticmethod
    def can_access(inventory):
        return locations.can_clear_nimbus_castle(inventory)


class NimbusCastleStarAfterValentina(Chest):
    area = locations.Area.NimbusLand
    addresses = [0x14A1AF]
    item = items.Flower
    access = 4

    @staticmethod
    def can_access(inventory):
        return locations.can_clear_nimbus_castle(inventory)


class DodoReward(Reward):
    area = locations.Area.NimbusLand
    addresses = [0x20936A]
    item = items.Feather
    access = 3


class NimbusLandPrisoners(Reward):
    area = locations.Area.NimbusLand
    addresses = [0x20A9C5]
    item = items.FlowerJar
    missable = True
    access = 3


class NimbusLandSignalRing(Reward):
    area = locations.Area.NimbusLand
    addresses = [0x20A456]
    item = items.SignalRing
    access = 4

    @staticmethod
    def can_access(inventory):
        return locations.can_clear_nimbus_castle(inventory)


class NimbusLandCellar(Reward):
    area = locations.Area.NimbusLand
    addresses = [0x1EA732]
    item = items.FlowerJar
    access = 4

    @staticmethod
    def can_access(inventory):
        return locations.can_clear_nimbus_castle(inventory)


# *** Barrel Volcano


class BarrelVolcanoSecret1(Chest):
    area = locations.Area.BarrelVolcano
    addresses = [0x14D048]
    item = items.Flower
    access = 2


class BarrelVolcanoSecret2(Chest):
    area = locations.Area.BarrelVolcano
    addresses = [0x14D04C]
    item = items.Flower
    access = 2


class BarrelVolcanoBeforeStar1(Chest):
    area = locations.Area.BarrelVolcano
    addresses = [0x14D595]
    item = items.Flower
    access = 1


class BarrelVolcanoBeforeStar2(Chest):
    area = locations.Area.BarrelVolcano
    addresses = [0x14D5A1]
    item = items.Coins100
    access = 1


class BarrelVolcanoStarRoom(StarAllowedChest):
    area = locations.Area.BarrelVolcano
    addresses = [0x14D5CE]
    item = items.LandsEndVolcanoStar
    access = 1


class BarrelVolcanoSaveRoom1(Chest):
    area = locations.Area.BarrelVolcano
    addresses = [0x14D203]
    item = items.Flower
    access = 2


class BarrelVolcanoSaveRoom2(Chest):
    area = locations.Area.BarrelVolcano
    addresses = [0x14D207]
    item = items.FrogCoin
    access = 2


class BarrelVolcanoHinnopio(Chest):
    area = locations.Area.BarrelVolcano
    addresses = [0x14D220]
    item = items.Coins100
    access = 2


# *** Bowser's Keep


class BowsersKeepDarkRoom(Chest):
    area = locations.Area.BowsersKeep
    addresses = [0x14E3B1]
    item = items.RecoveryMushroom
    access = 1


class BowsersKeepCrocoShop1(Chest):
    area = locations.Area.BowsersKeep
    addresses = [0x14E37F]
    item = items.Coins150
    access = 1


class BowsersKeepCrocoShop2(Chest):
    area = locations.Area.BowsersKeep
    addresses = [0x14E38B]
    item = items.RecoveryMushroom
    access = 1
    not_depletable = True


class BowsersKeepInvisibleBridge1(Chest):
    area = locations.Area.BowsersKeep
    addresses = [0x14C9B3]
    item = items.FrightBomb
    access = 2


class BowsersKeepInvisibleBridge2(Chest):
    area = locations.Area.BowsersKeep
    addresses = [0x14C9B7]
    item = items.RoyalSyrup
    access = 2


class BowsersKeepInvisibleBridge3(Chest):
    area = locations.Area.BowsersKeep
    addresses = [0x14C9BB]
    item = items.IceBomb
    access = 2


class BowsersKeepInvisibleBridge4(Chest):
    area = locations.Area.BowsersKeep
    addresses = [0x14C9BF]
    item = items.RockCandy
    access = 2


class BowsersKeepMovingPlatforms1(Chest):
    area = locations.Area.BowsersKeep
    addresses = [0x14E536]
    item = items.Flower
    access = 3


class BowsersKeepMovingPlatforms2(Chest):
    area = locations.Area.BowsersKeep
    addresses = [0x14E542]
    item = items.RedEssence
    access = 3


class BowsersKeepMovingPlatforms3(Chest):
    area = locations.Area.BowsersKeep
    addresses = [0x14E546]
    item = items.MaxMushroom
    access = 3


class BowsersKeepMovingPlatforms4(Chest):
    area = locations.Area.BowsersKeep
    addresses = [0x14E54A]
    item = items.FireBomb
    access = 3


class BowsersKeepElevatorPlatforms(Chest):
    area = locations.Area.BowsersKeep
    addresses = [0x14C97A]
    item = items.KerokeroCola
    access = 2


class BowsersKeepCannonballRoom1(Chest):
    area = locations.Area.BowsersKeep
    addresses = [0x14E4B1]
    item = items.Flower
    access = 2


class BowsersKeepCannonballRoom2(Chest):
    area = locations.Area.BowsersKeep
    addresses = [0x14E4B5]
    item = items.Flower
    access = 2


class BowsersKeepCannonballRoom3(Chest):
    area = locations.Area.BowsersKeep
    addresses = [0x14E4C1]
    item = items.PickMeUp
    access = 2


class BowsersKeepCannonballRoom4(Chest):
    area = locations.Area.BowsersKeep
    addresses = [0x14E4C5]
    item = items.RockCandy
    access = 2


class BowsersKeepCannonballRoom5(Chest):
    area = locations.Area.BowsersKeep
    addresses = [0x14E4C9]
    item = items.MaxMushroom
    access = 2


class BowsersKeepRotatingPlatforms1(Chest):
    area = locations.Area.BowsersKeep
    addresses = [0x14E3FF]
    item = items.Flower
    access = 2


class BowsersKeepRotatingPlatforms2(Chest):
    area = locations.Area.BowsersKeep
    addresses = [0x14E403]
    item = items.Flower
    access = 3


class BowsersKeepRotatingPlatforms3(Chest):
    area = locations.Area.BowsersKeep
    addresses = [0x14E40F]
    item = items.FireBomb
    access = 3


class BowsersKeepRotatingPlatforms4(Chest):
    area = locations.Area.BowsersKeep
    addresses = [0x14E413]
    item = items.RoyalSyrup
    access = 2


class BowsersKeepRotatingPlatforms5(Chest):
    area = locations.Area.BowsersKeep
    addresses = [0x14E417]
    item = items.PickMeUp
    access = 3


class BowsersKeepRotatingPlatforms6(Chest):
    area = locations.Area.BowsersKeep
    addresses = [0x14E41B]
    item = items.KerokeroCola
    access = 2


class BowsersKeepDoorReward1(BowserDoorReward):
    area = locations.Area.BowsersKeep
    addresses = [0x204BFC]
    item = items.SonicCymbal
    access = 4


class BowsersKeepDoorReward2(BowserDoorReward):
    area = locations.Area.BowsersKeep
    addresses = [0x204C02]
    item = items.SuperSlap
    access = 4


class BowsersKeepDoorReward3(BowserDoorReward):
    area = locations.Area.BowsersKeep
    addresses = [0x204C08]
    item = items.DrillClaw
    access = 4


class BowsersKeepDoorReward4(BowserDoorReward):
    area = locations.Area.BowsersKeep
    addresses = [0x204C0E]
    item = items.StarGun
    access = 4


class BowsersKeepDoorReward5(BowserDoorReward):
    area = locations.Area.BowsersKeep
    addresses = [0x204C14]
    item = items.RockCandy
    access = 4


class BowsersKeepDoorReward6(BowserDoorReward):
    area = locations.Area.BowsersKeep
    addresses = [0x204C1A]
    item = items.RockCandy
    access = 4


# *** Factory


class FactorySaveRoom(Chest):
    area = locations.Area.Factory
    addresses = [0x14BAFA]
    item = items.RecoveryMushroom
    access = 4


class FactoryBoltPlatforms(Chest):
    area = locations.Area.Factory
    addresses = [0x14BB6C]
    item = items.UltraHammer
    access = 4


class FactoryFallingAxems(Chest):
    area = locations.Area.Factory
    addresses = [0x14E0C8]
    item = items.RecoveryMushroom
    access = 4


class FACTORY_TREASURE_PIT_1(Chest):
    area = locations.Area.Factory
    addresses = [0x14E2C4]
    item = items.RecoveryMushroom
    access = 4


class FactoryTreasurePit2(NonCoinChest):
    area = locations.Area.Factory
    addresses = [0x14E2CC]
    item = items.Flower
    access = 4


class FactoryConveyorPlatforms1(Chest):
    area = locations.Area.Factory
    addresses = [0x14E9CB]
    item = items.RoyalSyrup
    access = 4


class FactoryConveyorPlatforms2(Chest):
    area = locations.Area.Factory
    addresses = [0x14E9CF]
    item = items.MaxMushroom
    access = 4


class FactoryBehindSnakes1(Chest):
    area = locations.Area.Factory
    addresses = [0x14E2C8]
    item = items.RecoveryMushroom
    access = 4


class FactoryBehindSnakes2(Chest):
    area = locations.Area.Factory
    addresses = [0x14E2D0]
    item = items.Flower
    access = 4


class FactoryToadGift(Reward):
    area = locations.Area.Factory
    addresses = [0x1FF7ED]
    item = items.RockCandy
    access = 4


# ********************* Default objects for world


def get_default_chests(world):
    """Get default vanilla chest and reward list for the world.

    Args:
        world (randomizer.logic.main.GameWorld):

    Returns:
        list[ItemLocation]: List of default chest objects.
    """
    return [
        # Chests
        MushroomWay1(world),
        MushroomWay2(world),
        MushroomWay3(world),
        MushroomWay4(world),
        MushroomKingdomVault1(world),
        MushroomKingdomVault2(world),
        MushroomKingdomVault3(world),
        BanditsWay1(world),
        BanditsWay2(world),
        BanditsWayStarChest(world),
        BanditsWayDogJump(world),
        BanditsWayCroco(world),
        KeroSewersPandoriteRoom(world),
        KeroSewersStarChest(world),
        RoseWayPlatform(world),
        RoseTownStore1(world),
        RoseTownStore2(world),
        GardenerCloud1(world),
        GardenerCloud2(world),
        ForestMaze1(world),
        ForestMaze2(world),
        ForestMazeUnderground1(world),
        ForestMazeUnderground2(world),
        ForestMazeUnderground3(world),
        ForestMazeRedEssence(world),
        PipeVaultSlide1(world),
        PipeVaultSlide2(world),
        PipeVaultSlide3(world),
        PipeVaultNippers1(world),
        PipeVaultNippers2(world),
        YosterIsleEntrance(world),
        MolevilleMinesStarChest(world),
        MolevilleMinesCoins(world),
        MolevilleMinesPunchinello1(world),
        MolevilleMinesPunchinello2(world),
        BoosterPass1(world),
        BoosterPass2(world),
        BOOSTER_PASS_SECRET_1(world),
        BOOSTER_PASS_SECRET_2(world),
        BOOSTER_PASS_SECRET_3(world),
        BOOSTER_TOWER_SPOOKUM(world),
        BOOSTER_TOWER_THWOMP(world),
        BOOSTER_TOWER_MASHER(world),
        BOOSTER_TOWER_PARACHUTE(world),
        BOOSTER_TOWER_ZOOM_SHOES(world),
        BOOSTER_TOWER_TOP_1(world),
        BOOSTER_TOWER_TOP_2(world),
        BOOSTER_TOWER_TOP_3(world),
        MARRYMORE_INN(world),
        SEA_STAR_CHEST(world),
        SEA_SAVE_ROOM_1(world),
        SEA_SAVE_ROOM_2(world),
        SEA_SAVE_ROOM_3(world),
        SeaSaveRoom4(world),
        SUNKEN_SHIP_RAT_STAIRS(world),
        SUNKEN_SHIP_SHOP(world),
        SUNKEN_SHIP_COINS_1(world),
        SUNKEN_SHIP_COINS_2(world),
        SUNKEN_SHIP_CLONE_ROOM(world),
        SUNKEN_SHIP_FROG_COIN_ROOM(world),
        SUNKEN_SHIP_HIDON_MUSHROOM(world),
        SUNKEN_SHIP_SAFETY_RING(world),
        SUNKEN_SHIP_BANDANA_REDS(world),
        LandsEndRedEssence(world),
        LandsEndChowPit1(world),
        LandsEndChowPit2(world),
        LandsEndBeeRoom(world),
        LandsEndSecret1(world),
        LandsEndSecret2(world),
        LandsEndShyAway(world),
        LandsEndStarChest1(world),
        LandsEndStarChest2(world),
        LandsEndStarChest3(world),
        BelomeTempleFortuneTeller(world),
        BelomeTempleAfterFortune1(world),
        BelomeTempleAfterFortune2(world),
        BelomeTempleAfterFortune3(world),
        BelomeTempleAfterFortune4(world),
        MonstroTownEntrance(world),
        BeanValley1(world),
        BeanValley2(world),
        BeanValleyBoxBoyRoom(world),
        BeanValleySlotRoom(world),
        BeanValleyPiranhaPlants(world),
        BeanValleyBeanstalk(world),
        BeanValleyCloud1(world),
        BeanValleyCloud2(world),
        BeanValleyFall1(world),
        BeanValleyFall2(world),
        NimbusLandShop(world),
        NimbusCastleBeforeBirdo1(world),
        NimbusCastleBeforeBirdo2(world),
        NimbusCastleOutOfBounds1(world),
        NimbusCastleOutOfBounds2(world),
        NimbusCastleSingleGoldBird(world),
        NimbusCastleStarChest(world),
        NimbusCastleStarAfterValentina(world),
        BarrelVolcanoSecret1(world),
        BarrelVolcanoSecret2(world),
        BarrelVolcanoBeforeStar1(world),
        BarrelVolcanoBeforeStar2(world),
        BarrelVolcanoStarRoom(world),
        BarrelVolcanoSaveRoom1(world),
        BarrelVolcanoSaveRoom2(world),
        BarrelVolcanoHinnopio(world),
        BowsersKeepDarkRoom(world),
        BowsersKeepCrocoShop1(world),
        BowsersKeepCrocoShop2(world),
        BowsersKeepInvisibleBridge1(world),
        BowsersKeepInvisibleBridge2(world),
        BowsersKeepInvisibleBridge3(world),
        BowsersKeepInvisibleBridge4(world),
        BowsersKeepMovingPlatforms1(world),
        BowsersKeepMovingPlatforms2(world),
        BowsersKeepMovingPlatforms3(world),
        BowsersKeepMovingPlatforms4(world),
        BowsersKeepElevatorPlatforms(world),
        BowsersKeepCannonballRoom1(world),
        BowsersKeepCannonballRoom2(world),
        BowsersKeepCannonballRoom3(world),
        BowsersKeepCannonballRoom4(world),
        BowsersKeepCannonballRoom5(world),
        BowsersKeepRotatingPlatforms1(world),
        BowsersKeepRotatingPlatforms2(world),
        BowsersKeepRotatingPlatforms3(world),
        BowsersKeepRotatingPlatforms4(world),
        BowsersKeepRotatingPlatforms5(world),
        BowsersKeepRotatingPlatforms6(world),
        BowsersKeepDoorReward1(world),
        BowsersKeepDoorReward2(world),
        BowsersKeepDoorReward3(world),
        BowsersKeepDoorReward4(world),
        BowsersKeepDoorReward5(world),
        BowsersKeepDoorReward6(world),
        FactorySaveRoom(world),
        FactoryBoltPlatforms(world),
        FactoryFallingAxems(world),
        FACTORY_TREASURE_PIT_1(world),
        FactoryTreasurePit2(world),
        FactoryConveyorPlatforms1(world),
        FactoryConveyorPlatforms2(world),
        FactoryBehindSnakes1(world),
        FactoryBehindSnakes2(world),
        # NPC rewards
        ToadRescue1(world),
        ToadRescue2(world),
        HammerBrosReward(world),
        WalletGuy1(world),
        WalletGuy2(world),
        MushroomKingdomStore(world),
        PeachSurprise(world),
        InvasionFamily(world),
        InvasionGuestRoom(world),
        InvasionGuard(world),
        Croco1Reward(world),
        PandoriteReward(world),
        MidasRiverFirstTime(world),
        RoseTownToad(world),
        Gaz(world),
        TreasureSeller1(world),
        TreasureSeller2(world),
        TreasureSeller3(world),
        CrocoFlunkie1(world),
        CrocoFlunkie2(world),
        CrocoFlunkie3(world),
        BOOSTER_TOWER_RAILWAY(world),
        BoosterTowerChomp(world),
        BoosterTowerCurtainGame(world),
        SEASIDE_TOWN_RESCUE(world),
        SUNKEN_SHIP_3D_MAZE(world),
        SUNKEN_SHIP_CANNONBALL_PUZZLE(world),
        SunkenShipHidonReward(world),
        BelomeTempleTreasure1(world),
        BelomeTempleTreasure2(world),
        BelomeTempleTreasure3(world),
        JinxDojoReward(world),
        CulexReward(world),
        SuperJumps30(world),
        SuperJumps100(world),
        ThreeMustyFears(world),
        TroopaClimb(world),
        DodoReward(world),
        NimbusLandInn(world),
        NimbusLandPrisoners(world),
        NimbusLandSignalRing(world),
        NimbusLandCellar(world),
        FactoryToadGift(world),
        GoombaThumping1(world),
        GoombaThumping2(world),
        CricketPieReward(world),
        CricketJamReward(world),
    ]
