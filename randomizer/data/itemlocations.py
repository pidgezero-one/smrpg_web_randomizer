# Data module for chest data.

from randomizer.data import items, ItemUnique
from randomizer.logic.utils import isclass_or_instance
from . import locations

# locations inherit world, and therefore settings
# inventory does not
# how to make work with optional gating?

# ******* Chest location classes

class Chest(locations.ItemLocation):
    """Subclass for treasure chest location."""
    ms_override = False
    shopsanity = False
    coinsanity = False
    dialogs_to_replace = []


# ******* NPC reward data classes

class NPCReward(locations.ItemLocation):
    """Subclass for NPC reward location."""

    def item_allowed(self, item):
        # NPC rewards cannot contain "You Missed!" or chest-only rewards.
        return super().item_allowed(item) and not isclass_or_instance(item, (items.MimicFight, items.SlotMachineChest, items.Flower, items.YouMissed, items.InvincibilityStar, items.InfiniteCoins))


class StarterItem(NPCReward):

    def item_allowed(self, item):
        return super().item_allowed(item) and item.consumable


class TreasureSellerReward(NPCReward):
    """Subclass for Moleville treasure seller NPC to check access.  Need to beat mines to unlock this."""

    shopsanity = True

    def item_allowed(self, item):
        # update this when shuffle modes integrated
        return super().item_allowed(item) and (item.unique == ItemUnique.Always or (item.unique == ItemUnique.BalancedOnly and true))

    @staticmethod
    def can_access(inventory):
        return locations.can_access_mines_back(inventory)

# ******* Overworld item classes


class OverworldItem(locations.ItemLocation):
    """Subclass for NPC reward location."""

    coinsanity = True
    npc_ids = None

    def item_allowed(self, item):
        # NPC rewards cannot contain "You Missed!" or chest-only rewards.
        # FIXME: Non-KI NPC rewards don't work with progressive cards for now.  Remove this when fixed.

        return super().item_allowed(item) and not isclass_or_instance(item, (items.MimicFight, items.SlotMachineChest, items.MultiFrogCoin, items.YouMissed, items.InvincibilityStar, items.InfiniteCoins))


class PacketItem(OverworldItem):
    """Subclass for NPC reward location."""
    script_id = None

    def item_allowed(self, item):
        # NPC rewards cannot contain "You Missed!" or chest-only rewards.
        # FIXME: Non-KI NPC rewards don't work with progressive cards for now.  Remove this when fixed.
        return super().item_allowed(item) and not isclass_or_instance(item, (items.MimicFight, items.SlotMachineChest, items.MultiFrogCoin, items.YouMissed, items.InvincibilityStar, items.InfiniteCoins))

# ******* Boss star piece classes

class BossStarPiece(locations.ItemLocation):
    """Subclass for boss star piece location."""
    shopsanity = False
    coinsanity = False
    dialogs_to_replace = []
    item = None
    

    def item_allowed(self, item):
        # Can only be Star Piece, or empty
        return isclass_or_instance(item, item.StarPiece)

# ******* Character recruitment classes

class CharacterRecruit(locations.ItemLocation):
    """Subclass for character recruit location."""
    shopsanity = False
    coinsanity = False
    dialogs_to_replace = []
    item = None
    
    def item_allowed(self, item):
        # Can only be Star Piece, or empty
        return isclass_or_instance(item, item.Character)

class StarterCharacterRecruit(locations.CharacterRecruit):
    pass


class MidasRiverTunnelItem(OverworldItem):
    pass


class BelomeTempleTreasure(OverworldItem):
    """Subclass for Belome Temple rewards."""

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.TempleKey)


# ****************************** Actual chest classes

# *** Marios Pad

class StarterCharacter1(StarterCharacterRecruit):
    area = locations.Area.MariosPad
    description = "Starter character 1"
    item = items.MarioRecruit
    event = 192

class StarterCharacter2(StarterCharacterRecruit):
    area = locations.Area.MariosPad
    description = "Starter character 2"
    event = 192

class StarterCharacter3(StarterCharacterRecruit):
    area = locations.Area.MariosPad
    description = "Starter character 3"
    event = 192

class StarterCharacter4(StarterCharacterRecruit):
    area = locations.Area.MariosPad
    description = "Starter character 4"
    event = 192

class StarterCharacter5(StarterCharacterRecruit):
    area = locations.Area.MariosPad
    description = "Starter character 5"
    event = 192

class MariosPadBed(NPCReward):
    description = "Mushroom Kingdom eastern guard rescue (invasion)"
    area = locations.Area.MariosPad
    item = items.DryBonesFlag
    rooms = [189]
    event = 253
    key = True


class MariosPadStarter1(StarterItem):
    description = "Starter item 1"
    area = locations.Area.MariosPad
    item = items.Mushroom
    rooms = [189]
    event = 252


class MariosPadStarter2(StarterItem):
    description = "Starter item 2"
    area = locations.Area.MariosPad
    item = items.Mushroom
    rooms = [189]
    event = 251


class MariosPadStarter3(StarterItem):
    description = "Starter item 3"
    area = locations.Area.MariosPad
    item = items.Mushroom
    rooms = [189]
    event = 250


class MariosPadStarter4(StarterItem):
    description = "Starter item 4"
    area = locations.Area.MariosPad
    item = items.Mushroom
    rooms = [189]
    event = 249


# *** Mushroom Way

class MushroomWay1(Chest):
    description = "Mushroom Way first chest"
    area = locations.Area.MushroomWay
    item = items.Coins(Chest, 5)
    rooms = [203]
    event = 247


class MushroomWay2(Chest):
    description = "Mushroom Way second chest"
    area = locations.Area.MushroomWay
    item = items.Coins(Chest, 8)
    rooms = [203]
    event = 246


class MushroomWay3(Chest):
    description = "Mushroom Way flower jump left chest"
    area = locations.Area.MushroomWay
    item = items.Flower
    rooms = [204]
    event = 247


class MushroomWay4(Chest):
    description = "Mushroom Way second room right chest"
    area = locations.Area.MushroomWay
    item = items.RecoveryMushroom
    rooms = [204]
    event = 246


class ToadRescue1(NPCReward):
    description = "Mushroom Way first Toad reward"
    area = locations.Area.MushroomWay
    item = items.HoneySyrup
    missable = True
    rooms = [203]
    event = 253


class ToadRescue2(NPCReward):
    description = "Mushroom Way second Toad reward"
    area = locations.Area.MushroomWay
    item = items.FlowerTab
    missable = True
    rooms = [204]
    event = 253


class HammerBrosReward(NPCReward):
    description = "Mushroom Way boss reward"
    area = locations.Area.MushroomWay
    item = items.Hammer
    rooms = [205]
    event = 253


class MushroomWayCharacter(CharacterRecruit):
    area = locations.Area.MushroomWay
    description = "Mushroom Way character join"
    item = items.MallowRecruit
    rooms = [205]
    event = 186


class MushroomWayStarPiece(BossStarPiece):
    area = locations.Area.MushroomWay
    description = "Mushroom Way boss star piece"
    rooms = [205]
    event = 167



# *** Mushroom Kingdom

class MushroomKingdomHallway(Chest):
    area = locations.Area.MushroomKingdom
    description = "Mushroom Kingdom castle main hallway chest"
    item = items.FrogCoin
    rooms = [17, 325]
    event = 247


class MushroomKingdomVault1(Chest):
    area = locations.Area.MushroomKingdom
    description = "Mushroom Kingdom vault left chest"
    rooms = [31]
    event = 247
    item = items.Coins10


class MushroomKingdomVault2(Chest):
    area = locations.Area.MushroomKingdom
    description = "Mushroom Kingdom vault right chest"
    rooms = [31]
    event = 246
    item = items.RecoveryMushroom


class MushroomKingdomVault3(Chest):
    area = locations.Area.MushroomKingdom
    description = "Mushroom Kingdom vault middle chest"
    rooms = [31]
    event = 245
    item = items.Flower


class InvasionVault1(Chest):
    area = locations.Area.MushroomKingdom
    description = "Mushroom Kingdom vault left chest (invasion)"
    item = items.Coins10
    rooms = [331]
    event = 247
    missable = True
    # bandits way access


class InvasionVault2(Chest):
    area = locations.Area.MushroomKingdom
    description = "Mushroom Kingdom vault right chest (invasion)"
    item = items.RecoveryMushroom
    rooms = [331]
    event = 246
    missable = True
    # bandits way access


class InvasionVault3(Chest):
    area = locations.Area.MushroomKingdom
    description = "Mushroom Kingdom vault middle chest (invasion)"
    item = items.Flower
    rooms = [331]
    event = 245
    missable = True
    # bandits way access


class InvasionEasternGuard(NPCReward):
    area = locations.Area.MushroomKingdom
    description = "Mushroom Kingdom eastern guard rescue (invasion)"
    rooms = [190]
    event = 253
    item = items.Coins10
    missable = True


class WalletGuy1(NPCReward):
    area = locations.Area.MushroomKingdom
    description = "Wallet reward 1"
    rooms = [190, 191]
    event = 252
    item = items.FlowerTab
    missable = True


class WalletGuy2(NPCReward):
    area = locations.Area.MushroomKingdom
    description = "Wallet reward 2"
    rooms = [190, 191]
    event = 251
    item = items.FrogCoin
    missable = True
    # requires marrymore access


class MushroomKingdomStore(NPCReward):
    area = locations.Area.MushroomKingdom
    description = "Mushroom Kingdom shop free item"
    rooms = [483, 491]
    event = 253
    item = items.PickMeUp


class MushroomKingdomStoreExchange(NPCReward):
    area = locations.Area.MushroomKingdom
    description = "Mushroom Kingdom shop Rare Frog Coin exchange"
    rooms = [483, 491]
    event = 252
    item = items.CricketPie
    key = True
    # optionally requires bandits way access


class MushroomKingdomStoreBasement1(Chest):
    area = locations.Area.MushroomKingdom
    description = "Mushroom Kingdom shop basement left chest"
    rooms = [492]
    event = 247
    item = items.Flower


class MushroomKingdomStoreBasement2(Chest):
    area = locations.Area.MushroomKingdom
    description = "Mushroom Kingdom shop basement right chest"
    rooms = [492]
    event = 246
    item = items.Flower


class PeachSurprise(NPCReward):
    area = locations.Area.MushroomKingdom
    description = "Mushroom Kingdom Toadstool's room chair item"
    item = items.Mushroom
    rooms = [20, 328]
    event = 253


class InvasionToadRescue(NPCReward):
    description = "Mushroom Kingdom Toadstool's room toad rescue item (invasion)"
    item = items.FlowerTab
    missable = True
    rooms = [20, 328]
    event = 252
    # bandits way access


class InvasionFamily(NPCReward):
    area = locations.Area.MushroomKingdom
    description = "Mushroom Kingdom invasion family rescue"
    rooms = [480, 481]
    script = 253
    item = items.FlowerTab
    missable = True
    # bandits way access


class InvasionGuestRoom(NPCReward):
    area = locations.Area.MushroomKingdom
    description = "Mushroom Kingdom invasion guest room"
    rooms = [330]
    script = 253
    item = items.WakeUpPin
    missable = True
    # bandits way access

class InvasionStarPiece(BossStarPiece):
    description = "Mushroom Kingdom invasion boss star piece"
    area = locations.Area.MushroomKingdom
    rooms = [326]
    event = 167
    item = items.StarPiece
    # bandits way access



class MushroomKingdomInn(NPCReward):
    area = locations.Area.MushroomKingdom
    description = "Mushroom Kingdom gameboy kid"
    rooms = [493]
    event = 253
    item = items.Beetlemania
    # bandits way access


# *** Bandit's Way

class BanditsWay1(Chest):
    description = "Bandit's Way flower chest"
    area = locations.Area.BanditsWay
    rooms = [207]
    event = 247
    item = items.KerokeroCola
    # bandits way access


class BanditsWayCoin1(OverworldItem):
    description = "Bandit's Way 1st coin"
    area = locations.Area.BanditsWay
    rooms = [207]
    event = 239
    npc_ids = [3]
    item = items.Coins1
    # bandits way access


class BanditsWayCoin2(OverworldItem):
    description = "Bandit's Way 2nd coin"
    area = locations.Area.BanditsWay
    rooms = [207]
    event = 240
    npc_ids = [4]
    item = items.Coins1
    # bandits way access


class BanditsWayCoin3(OverworldItem):
    description = "Bandit's Way 3rd coin"
    area = locations.Area.BanditsWay
    rooms = [207]
    event = 241
    npc_ids = [5]
    item = items.Coins1
    # bandits way access


class BanditsWay2(Chest):
    description = "Bandit's Way long room chest"
    area = locations.Area.BanditsWay
    rooms = [77]
    event = 253
    item = items.RecoveryMushroom
    # bandits way access


class BanditsWayStarChest(Chest):
    description = "Bandit's Way star chest"
    area = locations.Area.BanditsWay
    rooms = [78]
    event = 253
    item = items.BanditsWayStar
    # bandits way access


class BanditsWayDogJump(Chest):
    description = "Bandit's Way dog jump chest"
    rooms = [78]
    event = 252
    area = locations.Area.BanditsWay
    item = items.Flower
    # bandits way access


class BanditsWayCroco(Chest):
    description = "Bandit's Way Croco chase chest"
    area = locations.Area.BanditsWay
    rooms = [206]
    event = 247
    item = items.RecoveryMushroom
    # bandits way access


class Croco1Reward(NPCReward):
    description = "Bandit's Way boss reward 1"
    area = locations.Area.BanditsWay
    rooms = [206]
    event = 253
    item = items.RareFrogCoin
    key = True
    # bandits way access


class Croco1Reward2(NPCReward):
    description = "Bandit's Way boss reward 2"
    area = locations.Area.BanditsWay
    rooms = [206]
    event = 252
    item = items.Wallet
    # bandits way access

class BanditsWayStarPiece(BossStarPiece):
    area = locations.Area.BanditsWay
    description = "Bandit's Way boss star piece"
    rooms = [206]
    event = 167
    # bandits way access


# *** Kero Sewers


class KeroSewersPandoriteRoom(Chest):
    description = "Kero Sewers stairway room left chest"
    area = locations.Area.KeroSewers
    item = items.Flower
    rooms = [60]
    event = 247


class PandoriteChest(Chest):
    description = "Kero Sewers stairway room right chest"
    area = locations.Area.KeroSewers
    item = items.PandoriteFight
    rooms = [60]
    event = 246


class PandoriteReward1(NPCReward):
    description = "Mimic #1 first reward"
    item = items.TrueformPin
    rooms = [512]
    event = 253
    
    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.PandoriteFight)


class PandoriteReward2(Chest):
    description = "Mimic #1 reload reward"
    item = items.Coins(Chest, 50)
    rooms = [512]
    event = 245
    
    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.PandoriteFight)

class PandoriteBoss(BossStarPiece):
    description = "Mimic #1 star piece"
    rooms = [512]
    event = 167
    
    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.PandoriteFight)

class KeroSewersStarChest(Chest):
    description = "Kero Sewers four rat room chest"
    area = locations.Area.KeroSewers
    item = items.KeroSewersStar
    rooms = [59]
    event = 247


class KeroSewersBeforeBelomeLower(Chest):
    description = "Kero Sewers before boss lower chest"
    area = locations.Area.KeroSewers
    item = items.RecoveryMushroom
    rooms = [301]
    event = 247


class KeroSewersBeforeBelomeUpper1(Chest):
    description = "Kero Sewers before boss upper chest, before Land's End"
    area = locations.Area.KeroSewers
    item = items.Flower
    rooms = [301]
    event = 246
    missable = True


class KeroSewersBeforeBelomeUpper2(Chest):
    description = "Kero Sewers before boss upper chest, after Land's End"
    area = locations.Area.KeroSewers
    item = items.CricketJam
    rooms = [301]
    event = 245
    key = True


class KeroSewersBoss(BossStarPiece):
    description = "Kero Sewers boss star piece"
    area = locations.Area.KeroSewers
    rooms = [302]
    event = 167


# *** Midas River

class MidasRiverFirstTime(NPCReward):
    description = "Midas River first play reward"
    area = locations.Area.MidasRiver
    item = items.NokNokShell
    rooms = [67]
    event = 253


class MidasRiverBottomLeftCave(MidasRiverTunnelItem):
    description = "Midas River bottom left tunnel freestanding frog coin"
    area = locations.Area.MidasRiver
    item = items.FrogCoin
    rooms = [72]
    event = 241
    npc_ids = [1]


class MidasRiverBottomRightCave(MidasRiverTunnelItem):
    description = "Midas River bottom right tunnel freestanding flower"
    area = locations.Area.MidasRiver
    item = items.Flower
    rooms = [73]
    event = 241
    npc_ids = [4]

# *** Tadpole Pond


class CricketPieReward(NPCReward):
    description = "Tadpole Pond Cricket Pie exchange"
    area = locations.Area.TadpolePond
    item = items.FroggieStick
    rooms = [75]
    event = 253
    key = True

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.CricketPie)


class CricketJamReward(NPCReward):
    description = "Tadpole Pond Cricket Jam exchange"
    area = locations.Area.TadpolePond
    rooms = [75]
    event = 252
    item = items.MultiFrogCoin(NPCReward, 10)

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.CricketJam)


class MelodyBay1(NPCReward):
    description = "Melody Bay song 1 reward"
    area = locations.Area.TadpolePond
    item = items.ProgressiveCard
    rooms = [74]
    event = 253
    key = True


class MelodyBay2(NPCReward):
    description = "Melody Bay song 2 reward"
    area = locations.Area.TadpolePond
    item = items.ProgressiveCard
    rooms = [74]
    event = 252
    key = True

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.BambinoBomb)


class MelodyBay3(NPCReward):
    description = "Melody Bay song 3 reward"
    area = locations.Area.TadpolePond
    item = items.ProgressiveCard
    rooms = [74]
    event = 251
    key = True

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.BambinoBomb)

# *** Rose Way


class RoseWayPlatform(Chest):
    description = "Rose Way swinging Shy Guy chest"
    area = locations.Area.RoseWay
    rooms = [80]
    event = 247
    item = items.FrogCoin


class RoseWayFlower(OverworldItem):
    description = "Rose Way freestanding flower"
    area = locations.Area.RoseWay
    item = items.Flower
    rooms = [79]
    event = 241
    npc_ids = [7]


class RoseWayMushroom(OverworldItem):
    description = "Rose Way freestanding mushroom"
    area = locations.Area.RoseWay
    item = items.RecoveryMushroom
    rooms = [79]
    event = 240
    npc_ids = [8]


class RoseWayCoin1(OverworldItem):
    description = "Rose Way freestanding coin 1"
    area = locations.Area.RoseWay
    item = items.Coins10
    rooms = [79]
    event = 235
    npc_ids = [18]


class RoseWayCoin2(OverworldItem):
    description = "Rose Way freestanding coin 2"
    area = locations.Area.RoseWay
    item = items.Coins10
    rooms = [79]
    event = 236
    npc_ids = [19]


class RoseWayCoin3(OverworldItem):
    description = "Rose Way freestanding coin 3"
    area = locations.Area.RoseWay
    item = items.Coins10
    rooms = [79]
    event = 237
    npc_ids = [20]


class RoseWayCoin4(OverworldItem):
    description = "Rose Way freestanding coin 4"
    area = locations.Area.RoseWay
    item = items.Coins10
    rooms = [79]
    event = 238
    npc_ids = [21]


class RoseWayCoin5(OverworldItem):
    description = "Rose Way freestanding coin 5"
    area = locations.Area.RoseWay
    item = items.Coins10
    rooms = [79]
    event = 239
    npc_ids = [22]


class RoseWayFiveChests1(Chest):
    description = "Rose Way five-chest area top middle chest"
    area = locations.Area.RoseWay
    rooms = [81]
    event = 247
    item = items.RecoveryMushroom


class RoseWayFiveChests2(Chest):
    description = "Rose Way five-chest area bottom left chest"
    area = locations.Area.RoseWay
    rooms = [81]
    event = 246
    item = items.Coins(Chest, 5)


class RoseWayFiveChests3(Chest):
    description = "Rose Way five-chest top right chest"
    area = locations.Area.RoseWay
    rooms = [81]
    event = 245
    item = items.Coins(Chest, 5)


class RoseWayFiveChests4(Chest):
    description = "Rose Way five-chest top left chest"
    area = locations.Area.RoseWay
    rooms = [81]
    event = 244
    item = items.Coins(Chest, 5)


class RoseWayFiveChests5(Chest):
    description = "Rose Way five-chest bottom right chest"
    area = locations.Area.RoseWay
    rooms = [81]
    event = 243
    item = items.Coins(Chest, 5)

# *** Rose Town


class RoseTownFlag(NPCReward):
    description = "Rose Town behind sign"
    rooms = [83, 84]
    event = 253
    area = locations.Area.RoseTown
    item = items.GreaperFlag
    key = True


class RoseTownStore1(Chest):
    area = locations.Area.RoseTown
    description = "Rose Town shop right chest"
    rooms = [87]
    event = 247
    item = items.Flower


class RoseTownStore2(Chest):
    area = locations.Area.RoseTown
    description = "Rose Town shop left chest"
    rooms = [87]
    event = 246
    item = items.FrogCoin


class GardenerCloud1(Chest):
    area = locations.Area.RoseTownClouds
    description = "Rose Town gardener right chest"
    rooms = [419]
    event = 247
    item = items.LazyShellArmor

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.Seed) and inventory.has_item(items.Fertilizer)


class GardenerCloud2(Chest):
    area = locations.Area.RoseTownClouds
    description = "Rose Town gardener left chest"
    rooms = [419]
    event = 246
    item = items.LazyShellWeapon

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.Seed) and inventory.has_item(items.Fertilizer)


class RoseTownToad(NPCReward):
    description = "Rose Town Inn Toad gift"
    area = locations.Area.RoseTown
    rooms = [95, 96]
    event = 253
    item = items.FlowerTab


class Gaz(NPCReward):
    area = locations.Area.RoseTown
    description = "Rose Town (unoccupied) Gaz gift"
    rooms = [86]
    event = 253
    item = items.FingerShot
    # forest access


class RoseTownTreasureHouse1(Chest):
    description = "Rose Town upper house left chest"
    area = locations.Area.RoseTown
    rooms = [93, 94]
    event = 247
    item = items.Flower


class RoseTownTreasureHouse2(Chest):
    description = "Rose Town upper house right chest"
    area = locations.Area.RoseTown
    rooms = [93, 94]
    event = 246
    item = items.Flower


class RoseTownTreasureHouseMazeReward(NPCReward):
    description = "Rose Town upper house Maze Secret prize"
    area = locations.Area.RoseTown
    rooms = [93, 94]
    event = 253
    item = items.FrogCoin
    # forest access


class RoseTownTreasureHouse3(Chest):
    description = "Rose Town upper house top floor chest"
    area = locations.Area.RoseTown
    rooms = [97, 98]
    event = 246
    item = items.FrogCoin

# *** Forest Maze


class ForestMaze1(Chest):
    description = "Forest Maze 1st room chest"
    area = locations.Area.ForestMaze
    rooms = [223]
    event = 247
    item = items.KerokeroCola
    # forest access


class ForestMaze2(Chest):
    description = "Forest Maze first chest after underground"
    area = locations.Area.ForestMaze
    rooms = [228]
    event = 247
    item = items.FrogCoin
    # forest access


class ForestMazeUnderground1(Chest):
    description = "Forest Maze wiggler chest"
    area = locations.Area.ForestMaze
    rooms = [242]
    event = 247
    item = items.KerokeroCola
    # forest access


class ForestMazeUnderground2(Chest):
    description = "Forest Maze bottom right stump chest"
    area = locations.Area.ForestMaze
    rooms = [242]
    event = 246
    item = items.Flower
    # forest access


class ForestMazeUnderground3(Chest):
    description = "Forest Maze middle left stump chest"
    area = locations.Area.ForestMaze
    rooms = [242]
    event = 245
    item = items.YouMissed
    # forest access


class ForestMazeRedEssence(Chest):
    description = "Forest Maze before maze chest"
    area = locations.Area.ForestMaze
    rooms = [227]
    event = 247
    item = items.RedEssence
    # forest access


class ForestMazeSecret1(Chest):
    description = "Forest Maze secret top right chest"
    area = locations.Area.ForestMaze
    rooms = [234]
    event = 247
    item = items.FrogCoin
    # forest access


class ForestMazeSecret2(Chest):
    description = "Forest Maze secret bottom right chest"
    area = locations.Area.ForestMaze
    rooms = [234]
    event = 246
    item = items.Flower
    # forest access


class ForestMazeSecret3(Chest):
    description = "Forest Maze secret top middle chest"
    area = locations.Area.ForestMaze
    rooms = [234]
    event = 245
    item = items.Flower
    # forest access


class ForestMazeSecret4(Chest):
    description = "Forest Maze secret bottom middle chest"
    area = locations.Area.ForestMaze
    rooms = [234]
    event = 244
    item = items.Flower
    # forest access


class ForestMazeSecret5(Chest):
    description = "Forest Maze secret left chest"
    area = locations.Area.ForestMaze
    rooms = [234]
    event = 243
    item = items.RecoveryMushroom
    # forest access


class ForestMazeCharacter(CharacterRecruit):
    area = locations.Area.ForestMaze
    description = "Forest Maze character recruit"
    item = items.GenoRecruit
    rooms = [232]
    event = 186
    # forest access


class ForestMazeBoss(BossStarPiece):
    area = locations.Area.ForestMaze
    description = "Forest Maze boss star piece"
    rooms = [232]
    event = 167
    item = items.StarPiece
    # forest access


# *** Pipe Vault

class PipeVaultSlide1(Chest):
    area = locations.Area.PipeVault
    description = "Pipe Vault slide room back chest"
    rooms = [125]
    event = 245
    item = items.Flower


class PipeVaultSlide2(Chest):
    area = locations.Area.PipeVault
    description = "Pipe Vault slide room middle chest"
    rooms = [125]
    event = 246
    item = items.FrogCoin


class PipeVaultSlide3(Chest):
    area = locations.Area.PipeVault
    description = "Pipe Vault slide room front chest"
    rooms = [125]
    event = 247
    item = items.FrogCoin


class PipeVaultSlideCoin1(OverworldItem):
    area = locations.Area.PipeVault
    description = "Pipe Vault slide room freestanding coin 1"
    rooms = [125]
    event = 237
    item = items.Coins1
    npc_ids = [0]


class PipeVaultSlideCoin2(OverworldItem):
    area = locations.Area.PipeVault
    description = "Pipe Vault slide room freestanding coin 2"
    rooms = [125]
    event = 238
    item = items.Coins1
    npc_ids = [1]


class PipeVaultSlideCoin3(OverworldItem):
    area = locations.Area.PipeVault
    description = "Pipe Vault slide room freestanding coin 3"
    rooms = [125]
    event = 239
    item = items.Coins1
    npc_ids = [2]


class PipeVaultSlideCoin4(OverworldItem):
    area = locations.Area.PipeVault
    description = "Pipe Vault slide room freestanding coin 4"
    rooms = [125]
    event = 240
    item = items.Coins1
    npc_ids = [3]


class PipeVaultSlideCoin5(OverworldItem):
    area = locations.Area.PipeVault
    description = "Pipe Vault slide room freestanding coin 5"
    rooms = [125]
    event = 241
    item = items.Coins1
    npc_ids = [4]


class PipeVaultSlideFrogCoin(OverworldItem):
    area = locations.Area.PipeVault
    description = "Pipe Vault slide room freestanding frog coin"
    rooms = [125]
    event = 236
    item = items.FrogCoin
    npc_ids = [5]


class PipeVaultNippers1(Chest):
    area = locations.Area.PipeVault
    description = "Pipe Vault nipper room first chest"
    rooms = [128]
    event = 247
    item = items.Flower
    npc_ids = [6]


class PipeVaultNippers2(Chest):
    area = locations.Area.PipeVault
    description = "Pipe Vault nipper room second chest"
    rooms = [128]
    event = 246
    item = items.Coins(Chest, 20)


class GoombaThumping1(NPCReward):
    area = locations.Area.PipeVault
    description = "Pipe Vault Goomba Thumpin first prize"
    rooms = [143]
    event = 253
    item = items.FlowerTab


class GoombaThumping2(NPCReward):
    area = locations.Area.PipeVault
    description = "Pipe Vault Goomba Thumpin second prize"
    rooms = [143]
    event = 252
    item = items.FlowerJar


# *** Yo'ster Isle

class YosterIsleEntrance(Chest):
    description = "Yo'ster Isle entrance chest"
    area = locations.Area.YosterIsle
    rooms = [33]
    item = items.FrogCoin
    event = 247


class YosterIsleRaceReward1(NPCReward):
    description = "Yo'ster Isle first race prize item 1"
    area = locations.Area.YosterIsle
    rooms = [34]
    item = items.YoshiCookie
    event = 253


class YosterIsleRaceReward2(NPCReward):
    description = "Yo'ster Isle invisible GOAL item"
    area = locations.Area.YosterIsle
    rooms = [34]
    item = items.YoshiCookie
    event = 251


class YosterIsleRaceReward3(NPCReward):
    description = "Yo'ster Isle first race prize item 2"
    area = locations.Area.YosterIsle
    rooms = [34]
    item = items.YoshiCookie
    event = 250


class YosterIsleFlag(NPCReward):
    description = "Yo'ster Isle first race prize item 3"
    area = locations.Area.YosterIsle
    rooms = [34]
    key = True
    item = items.BigBooFlag
    event = 252

# *** Moleville


class BucketGirl(NPCReward):
    description = "Moleville bucket girl"
    area = locations.Area.Moleville
    rooms = [108]
    event = 253
    item = items.FrogCoin
    dialogs_to_replace = [2911]

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.BambinoBomb)
    # bucket warp needs to be off
    # if shuffle FW: needs one FW
    # if progressive FW: needs three progressive FW


class TreasureSeller1(TreasureSellerReward):
    description = "Moleville first treasure shop item"
    area = locations.Area.Moleville
    rooms = [336]
    event = 253
    item = items.LuckyJewel
    dialogs_to_replace = [2911]

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.BambinoBomb)


class TreasureSeller2(TreasureSellerReward):
    description = "Moleville second treasure shop item"
    area = locations.Area.Moleville
    rooms = [336]
    event = 252
    item = items.MysteryEgg
    dialogs_to_replace = [2908]

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.BambinoBomb)
        # may also need ship access


class TreasureSeller3(TreasureSellerReward):
    description = "Moleville third treasure shop item"
    area = locations.Area.Moleville
    rooms = [336]
    event = 251
    item = items.FryingPan
    dialogs_to_replace = [2914]

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.BambinoBomb)
        # also needs volcano access


class FireworksShop(NPCReward):
    # Fireworks shuffle/progressive ONLY
    area = locations.Area.Moleville
    rooms = [339]
    event = 253
    item = items.Fireworks
    key = True

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.BambinoBomb)


# *** Moleville Mines

class MolevilleMinesStarChest(Chest):
    description = "Moleville Mines two-level traintrack room chest"
    area = locations.Area.MolevilleMines
    rooms = [285]
    event = 247
    item = items.MolevilleMinesStar

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.BambinoBomb)


class MolevilleMinesShyGuy(OverworldItem):
    description = "Moleville Mines shy guy cart"
    area = locations.Area.MolevilleMines
    rooms = [286]
    event = 241
    npc_ids = [2]
    item = items.FrogCoin

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.BambinoBomb)


class MolevilleMinesCoins(Chest):
    description = "Moleville Mines near final train tracks chest"
    area = locations.Area.MolevilleMines
    rooms = [280]
    event = 247
    item = items.Coins(Chest, 150)

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.BambinoBomb)


class MolevilleMinesPunchinello1(Chest):
    description = "Moleville Mines before boss left chest"
    area = locations.Area.MolevilleMines
    rooms = [288]
    event = 247
    item = items.RecoveryMushroom

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.BambinoBomb)


class MolevilleMinesPunchinello2(Chest):
    description = "Moleville Mines before boss upper chest"
    area = locations.Area.MolevilleMines
    rooms = [288]
    event = 246
    item = items.Flower

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.BambinoBomb)


class MolevilleMinesBoss2(BossStarPiece):
    description = "Moleville Mines final boss star piece"
    area = locations.Area.MolevilleMines
    rooms = [271]
    event = 167
    item = items.StarPiece

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.BambinoBomb)

class MolevilleMinesCharacter(CharacterRecruit):
    area = locations.Area.ForestMaze
    description = "Moleville Mines character recruit"
    item = items.BowserRecruit
    rooms = [284]
    event = 186

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.BambinoBomb)


class CrocoFlunkie1(NPCReward):
    description = "Moleville Mines trampoline bandit"
    area = locations.Area.MolevilleMines
    rooms = [273]
    event = 253
    item = items.FlowerTab
    missable = True


class CrocoFlunkie2(NPCReward):
    description = "Moleville Mines left bandit"
    area = locations.Area.MolevilleMines
    rooms = [277]
    event = 253
    item = items.FlowerTab
    missable = True


class CrocoFlunkie3(NPCReward):
    description = "Moleville Mines right bandit"
    area = locations.Area.MolevilleMines
    rooms = [283]
    event = 253
    item = items.FlowerTab
    missable = True


class Croco2Item(NPCReward):
    description = "Moleville Mines first boss item"
    area = locations.Area.MolevilleMines
    rooms = [518]
    event = 253
    item = items.BambinoBomb
    key = True


class MolevilleMinesBoss1(BossStarPiece):
    description = "Moleville Mines first boss star piece"
    area = locations.Area.MolevilleMines
    rooms = [518]
    event = 167

# *** Booster Pass


class BoosterPass1(Chest):
    description = "Booster Pass main area left chest"
    area = locations.Area.BoosterPass
    rooms = [100]
    event = 247
    item = items.Flower


class BoosterPass2(Chest):
    description = "Booster Pass main area right chest"
    area = locations.Area.BoosterPass
    rooms = [100]
    event = 246
    item = items.RockCandy


class BoosterPassBush(NPCReward):
    description = "Booster Pass main area bush check"
    area = locations.Area.BoosterPass
    rooms = [100]
    event = 253
    item = items.FrogCoin
    coinsanity = True


class BoosterPassFlower(OverworldItem):
    description = "Booster Pass freestanding flower"
    area = locations.Area.BoosterPass
    rooms = [101]
    event = 241
    npc_ids = [6]
    item = items.Flower


class BoosterPassSecret1(Chest):
    area = locations.Area.BoosterPass
    description = "Booster Pass secret middle chest"
    rooms = [401]
    event = 247
    item = items.FrogCoin
    # tower access


class BoosterPassSecret2(Chest):
    area = locations.Area.BoosterPass
    description = "Booster Pass secret right chest"
    rooms = [401]
    event = 246
    item = items.Flower
    # tower access


class BoosterPassSecret3(Chest):
    area = locations.Area.BoosterPass
    description = "Booster Pass secret left chest"
    rooms = [401]
    event = 245
    item = items.KerokeroCola
    # tower access


# *** Booster Tower

class BoosterTowerSpookum(Chest):
    description = "Booster Tower first stairway chest"
    area = locations.Area.BoosterTower
    item = items.FrogCoin
    rooms = [196]
    event = 247
    # tower access


class BoosterTowerThwomp(Chest):
    description = "Booster Tower upper thwomp room chest"
    area = locations.Area.BoosterTower
    item = items.RecoveryMushroom
    rooms = [36]
    event = 247
    # tower access


class BoosterTowerKnifeGuy(NPCReward):
    description = "Booster Tower Knife Guy reward"
    area = locations.Area.BoosterTower
    item = items.BrightCard
    rooms = [39]
    event = 253
    # tower access
    key = True
    # false if casino warp is off


class BoosterTowerRoomKey(OverworldItem):
    description = "Booster Tower checkerboard room item"
    area = locations.Area.BoosterTower
    item = items.RoomKey
    key = True
    coinsanity = False
    rooms = [41]
    event = 228
    npc_ids = [5]
    # tower access


class BoosterTowerFrogCoin1(OverworldItem):
    description = "Booster Tower checkerboard room freestanding frog coin 1"
    area = locations.Area.BoosterTower
    item = items.FrogCoin
    rooms = [41]
    event = 241
    npc_ids = [0]
    # tower access


class BoosterTowerFrogCoin2(OverworldItem):
    description = "Booster Tower checkerboard room freestanding frog coin 2"
    area = locations.Area.BoosterTower
    item = items.FrogCoin
    rooms = [41]
    event = 240
    npc_ids = [1]
    # tower access


class BoosterTowerFrogCoin3(OverworldItem):
    description = "Booster Tower checkerboard room freestanding frog coin 3"
    area = locations.Area.BoosterTower
    item = items.FrogCoin
    rooms = [41]
    event = 239
    npc_ids = [2]
    # tower access


class BoosterTowerFrogCoin4(OverworldItem):
    description = "Booster Tower checkerboard room freestanding frog coin 4"
    area = locations.Area.BoosterTower
    item = items.FrogCoin
    rooms = [41]
    event = 238
    npc_ids = [3]
    # tower access


class BoosterTowerCoin1(OverworldItem):
    description = "Booster Tower checkerboard room freestanding coin 1"
    area = locations.Area.BoosterTower
    item = items.Coins1
    rooms = [41]
    event = 237
    npc_ids = [7]
    # tower access


class BoosterTowerCoin2(OverworldItem):
    description = "Booster Tower checkerboard room freestanding coin 2"
    area = locations.Area.BoosterTower
    item = items.Coins1
    rooms = [41]
    event = 236
    npc_ids = [8]
    # tower access


class BoosterTowerCoin3(OverworldItem):
    description = "Booster Tower checkerboard room freestanding coin 3"
    area = locations.Area.BoosterTower
    item = items.Coins1
    rooms = [41]
    event = 235
    npc_ids = [9]
    # tower access


class BoosterTowerCoin4(OverworldItem):
    description = "Booster Tower checkerboard room freestanding coin 4"
    area = locations.Area.BoosterTower
    item = items.Coins1
    rooms = [41]
    event = 234
    npc_ids = [10]
    # tower access


class BoosterTowerCoin5(OverworldItem):
    description = "Booster Tower checkerboard room freestanding coin 5"
    area = locations.Area.BoosterTower
    item = items.Coins1
    rooms = [41]
    event = 233
    npc_ids = [11]
    # tower access


class BoosterTowerCoin6(OverworldItem):
    description = "Booster Tower checkerboard room freestanding coin 6"
    area = locations.Area.BoosterTower
    item = items.Coins1
    rooms = [41]
    event = 232
    npc_ids = [12]
    # tower access


class BoosterTowerCoin7(OverworldItem):
    description = "Booster Tower checkerboard room freestanding coin 7"
    area = locations.Area.BoosterTower
    item = items.Coins1
    rooms = [41]
    event = 231
    npc_ids = [13]
    # tower access


class BoosterTowerCoin8(OverworldItem):
    description = "Booster Tower checkerboard room freestanding coin 8"
    area = locations.Area.BoosterTower
    item = items.Coins1
    rooms = [41]
    event = 230
    npc_ids = [14]
    # tower access


class BoosterTowerCoin9(OverworldItem):
    description = "Booster Tower checkerboard room freestanding coin 9"
    area = locations.Area.BoosterTower
    item = items.Coins1
    rooms = [41]
    event = 229
    npc_ids = [15]
    # tower access


class BoosterTowerMasher(OverworldItem):
    description = "Booster Tower Masher chest"
    area = locations.Area.BoosterTower
    rooms = [197]
    event = 253
    item = items.Masher
    npc_ids = [3]
    # tower access


class BoosterTowerParachute(Chest):
    description = "Booster Tower parachute room chest"
    area = locations.Area.BoosterTower
    item = items.FrogCoin
    rooms = [35]
    event = 247
    # tower access


class BoosterTowerParachuteCrevice(NPCReward):
    description = "Booster Tower parachute room stair crevice"
    area = locations.Area.BoosterTower
    item = items.FrogCoin
    coinsanity = True
    rooms = [35]
    event = 253
    # tower access


class BoosterTowerZoomShoes(Chest):
    description = "Booster Tower Room Key chest"
    area = locations.Area.BoosterTower
    item = items.ZoomShoes
    rooms = [48]
    event = 247

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.RoomKey)
    # tower access


class BoosterTowerTop1(Chest):
    description = "Booster Tower top floor lower chest"
    area = locations.Area.BoosterTower
    rooms = [199]
    script = 247
    item = items.FrogCoin
    # tower access


class BoosterTowerTop2(Chest):
    description = "Booster Tower top floor upper chest"
    area = locations.Area.BoosterTower
    rooms = [199]
    script = 246
    item = items.GoodieBag
    # tower access


class BoosterTowerTop3(Chest):
    description = "Booster Tower top floor corner chest"
    area = locations.Area.BoosterTower
    rooms = [199]
    script = 245
    item = items.RecoveryMushroom
    # tower access


class BoosterTowerRailway(NPCReward):
    area = locations.Area.BoosterTower
    description = "Booster Tower railway room"
    rooms = [194]
    event = 253
    item = items.FlowerTab
    # tower access


class BoosterTowerPortraits(OverworldItem):
    area = locations.Area.BoosterTower
    description = "Booster Tower portrait prize"
    rooms = [195]
    event = 241
    npc_ids = [7]
    item = items.ElderKey
    coinsanity = False
    key = True
    # tower access


class BoosterTowerChomp(OverworldItem):
    area = locations.Area.BoosterTower
    description = "Booster Tower Elder Key room"
    rooms = [200]
    event = 241
    npc_ids = [0]
    item = items.Chomp
    coinsanity = False
    # tower access

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.ElderKey)


class BoosterTowerCurtainGame(NPCReward):
    area = locations.Area.BoosterTower
    description = "Booster Tower curtain prize"
    rooms = [192]
    event = 253
    item = items.Amulet
    missable = True
    # tower access


class BoosterTowerStarPiece1(BossStarPiece):
    area = locations.Area.BoosterTower
    description = "Booster Tower curtain room boss star piece"
    rooms = [192]
    event = 167


class BoosterTowerStarPiece2(BossStarPiece):
    area = locations.Area.BoosterTower
    description = "Booster Tower balcony boss star piece"
    rooms = [258]
    event = 167



# *** Marrymore

class MarrymorePrize1(NPCReward):
    area = locations.Area.Marrymore
    description = "Marrymore Suite total stays prize 1"
    item = items.FlowerTab
    rooms = [9]
    event = 253


class MarrymorePrize2(NPCReward):
    area = locations.Area.Marrymore
    description = "Marrymore Suite total stays prize 2"
    item = items.FlowerJar
    rooms = [9]
    event = 252


class MarrymorePrize3(NPCReward):
    area = locations.Area.Marrymore
    item = items.MultiFrogCoin(NPCReward, 5)
    description = "Marrymore Suite total stays prize 3"
    rooms = [9]
    event = 251


class MarrymorePrize4(NPCReward):
    area = locations.Area.Marrymore
    item = items.MultiFrogCoin(NPCReward, 10)
    description = "Marrymore Suite total stays prize 4"
    rooms = [9]
    event = 250


class MarrymorePrize5(NPCReward):
    area = locations.Area.Marrymore
    item = items.MultiFrogCoin(NPCReward, 15)
    description = "Marrymore Suite total stays prize 5"
    rooms = [9]
    event = 249


class MarrymorePrize6(NPCReward):
    area = locations.Area.Marrymore
    item = items.MultiFrogCoin(NPCReward, 20)
    description = "Marrymore Suite total stays prize 6"
    rooms = [9]
    event = 248


class MarrymoreInn(Chest):
    area = locations.Area.Marrymore
    description = "Marrymore Inn regular room chest"
    item = items.FrogCoin
    rooms = [9]
    event = 247


class MarrymoreStarPiece(BossStarPiece):
    area = locations.Area.Marrymore
    description = "Marrymore boss star piece"
    rooms = [154]
    event = 167


class MarrymoreCharacter(CharacterRecruit):
    area = locations.Area.Marrymore
    description = "Marrymore character join"
    item = items.PeachRecruit
    rooms = [154]
    event = 186
    # marrymore access


# *** Star Hill


class StarHillStarPiece1(BossStarPiece):
    area = locations.Area.StarHill
    description = "Star Hill freestanding star piece"
    rooms = [157]
    event = 167
    item = items.StarPiece



# *** Seaside Town

class SeasideTownBoss(BossStarPiece):
    description = "Seaside Town boss star piece"
    area = locations.Area.SeasideTown
    rooms = [315]
    event = 167
    item = items.StarPiece


class SeasideTownBossPrize(OverworldItem):
    area = locations.Area.SeasideTown
    description = "Seaside Town boss prize"
    rooms = [316]
    event = 241
    npc_ids = [0]
    item = items.ShedKey
    key = True
    coinsanity = False

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.ShedKey)
    # may also need ship access


class SeasideTownRescue(NPCReward):
    area = locations.Area.SeasideTown
    description = "Seaside Town shed rescue"
    rooms = [314]
    event = 253
    item = items.FlowerBox

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.ShedKey)
    # may also need ship access


# *** Sea

class SeaStarChest(Chest):
    area = locations.Area.Sea
    description = "Sea starslap room chest"
    rooms = [134]
    event = 247
    item = items.SeaStar
    # ship access


class SeaSaveRoom1(Chest):
    area = locations.Area.Sea
    description = "Sea save room back chest"
    rooms = [132]
    event = 245
    item = items.FrogCoin
    # ship access


class SeaSaveRoom2(Chest):
    area = locations.Area.Sea
    description = "Sea save room middle chest"
    rooms = [132]
    event = 246
    item = items.Flower
    # ship access


class SeaSaveRoom3(Chest):
    area = locations.Area.Sea
    description = "Sea save room front chest"
    rooms = [132]
    event = 247
    item = items.RecoveryMushroom
    # ship access


class SeaWhirlpoolChest(Chest):
    description = "Sea whirlpool room chest"
    area = locations.Area.Sea
    rooms = [133]
    event = 247
    item = items.MaxMushroom
    # ship access


# *** Sunken Ship

class SunkenShipRatStairs(Chest):
    area = locations.Area.SunkenShip
    description = "Sunken Ship first stairway chest"
    rooms = [167]
    event = 247
    item = items.Coins(Chest, 100)
    # ship access


class SunkenShipRatStairsFlower(PacketItem):
    area = locations.Area.SunkenShip
    description = "Sunken Ship first stairway freestanding flower"
    rooms = [167]
    script_id = 3385
    event = 241
    item = items.Flower
    # ship access


class SunkenShipShop(Chest):
    area = locations.Area.SunkenShip
    description = "Sunken Ship shop area chest"
    rooms = [169]
    event = 247
    item = items.Coins(Chest, 100)
    # ship access


class SunkenShipCoins1(Chest):
    area = locations.Area.SunkenShip
    description = "Sunken Ship outside clone room left chest"
    rooms = [175]
    event = 247
    item = items.Coins(Chest, 100)
    # ship access


class SunkenShipCoins2(Chest):
    area = locations.Area.SunkenShip
    description = "Sunken Ship outside clone room right chest"
    rooms = [175]
    event = 246
    item = items.Coins(Chest, 100)
    # ship access


class SunkenShipCloneRoom(Chest):
    area = locations.Area.SunkenShip
    description = "Sunken Ship clone room chest"
    rooms = [179]
    event = 247
    item = items.KerokeroCola
    # ship access


class SunkenShipFrogCoinRoom(Chest):
    area = locations.Area.SunkenShip
    description = "Sunken Ship hidden box room chest"
    rooms = [183]
    event = 247
    item = items.FrogCoin
    # ship access


class SunkenShipHidonMushroom(Chest):
    area = locations.Area.SunkenShip
    description = "Sunken Ship Hidon's room left chest"
    rooms = [184]
    event = 247
    item = items.RecoveryMushroom
    # ship access


class SunkenShipHidonChest(Chest):
    area = locations.Area.SunkenShip
    description = "Sunken Ship Hidon's room right chest"
    rooms = [184]
    event = 246
    item = items.HidonFight
    # ship access


class HidonReward1(NPCReward):
    description = "Mimic #2 first reward"
    rooms = [513]
    event = 253
    item = items.SafetyBadge
    
    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.HidonFight)


class HidonReward2(Chest):
    description = "Mimic #2 reload reward"
    rooms = [513]
    event = 245
    item = items.Coins(Chest, 100)
    
    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.HidonFight)

class HidonBoss(BossStarPiece):
    description = "Mimic #2 star piece"
    rooms = [513]
    event = 167
    
    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.HidonFight)


class SunkenShipUnderwaterFrogCoin1(OverworldItem):
    description = "Sunken Ship underwater freestanding frog coin 1"
    area = locations.Area.SunkenShip
    item = items.FrogCoin
    rooms = [187]
    event = 241
    npc_ids = [0]
    # ship access


class SunkenShipUnderwaterFrogCoin2(OverworldItem):
    description = "Sunken Ship underwater freestanding frog coin 2"
    area = locations.Area.SunkenShip
    item = items.FrogCoin
    rooms = [187]
    event = 240
    npc_ids = [1]
    # ship access


class SunkenShipUnderwaterFrogCoin3(OverworldItem):
    description = "Sunken Ship underwater freestanding frog coin 3"
    area = locations.Area.SunkenShip
    item = items.FrogCoin
    rooms = [187]
    event = 239
    npc_ids = [2]
    # ship access


class SunkenShipUnderwaterFrogCoin4(OverworldItem):
    description = "Sunken Ship underwater freestanding frog coin 4"
    area = locations.Area.SunkenShip
    item = items.FrogCoin
    rooms = [187]
    event = 238
    npc_ids = [3]
    # ship access


class SunkenShipSafetyRing(Chest):
    description = "Sunken Ship hidden underwater room chest"
    area = locations.Area.SunkenShip
    rooms = [185]
    event = 247
    item = items.SafetyRing
    # ship access


class SunkenShipBandanaReds(Chest):
    description = "Sunken Ship near final boss chest"
    area = locations.Area.SunkenShip
    item = items.RecoveryMushroom
    rooms = [24]
    event = 247
    # ship access


class SunkenShipBlooberRoom(OverworldItem):
    description = "Sunken Ship large pool freestanding frog coin"
    area = locations.Area.SunkenShip
    item = items.FrogCoin
    rooms = [27]
    event = 241
    npc_ids = [5]
    # ship access


class SunkenShipTrampolinePuzzle(PacketItem):
    area = locations.Area.SunkenShip
    description = "Sunken Ship trampoline puzzle prize"
    rooms = [163]
    event = 241
    script_id = 3383
    item = items.Flower
    # ship access


class SunkenShipTroopaPuzzle(PacketItem):
    area = locations.Area.SunkenShip
    description = "Sunken Ship troopa cannonball prize"
    rooms = [166]
    event = 241
    script_id = 3384
    item = items.RecoveryMushroom
    # ship access


class SunkenShip3DMaze(PacketItem):
    area = locations.Area.SunkenShip
    description = "Sunken Ship 3D maze prize"
    rooms = [168]
    event = 241
    script_id = 3386
    item = items.RoyalSyrup
    coinsanity = False
    # ship access


class SunkenShipCoinSnake(NPCReward):
    area = locations.Area.SunkenShip
    description = "Sunken Ship coin snake puzzle prize"
    rooms = [171]
    event = 253
    npc_ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    item = items.Coins(NPCReward, 150)
    # Needs special considerations for the sound played in 3216
    # and the sequences performed in 3216 and 3215
    # depending on the item
    # ship access


class SunkenShipCannonballPuzzle(PacketItem):
    area = locations.Area.SunkenShip
    description = "Sunken Ship cannonball puzzle prize"
    rooms = [172]
    event = 241
    script_id = 3387
    item = items.Mushroom
    coinsanity = False
    # ship access


class SunkenShipBarrelPuzzle(PacketItem):
    area = locations.Area.SunkenShip
    description = "Sunken Ship barrel switch prize"
    rooms = [176]
    event = 241
    script_id = 3389
    item = items.RecoveryMushroom
    # ship access



class SunkenShipMidboss(BossStarPiece):
    description = "Sunken Ship password boss star piece"
    area = locations.Area.SunkenShip
    rooms = [177]
    event = 167
    # ship access


class SunkenShipBoss(BossStarPiece):
    description = "Sunken Ship final boss star piece"
    area = locations.Area.SunkenShip
    rooms = [28]
    event = 167
    # ship access


# *** Land's End


class LandsEndRedEssence(Chest):
    area = locations.Area.LandsEnd
    description = "Land's End first chest"
    rooms = [137]
    event = 247
    item = items.RedEssence


class LandsEndChowPit1(Chest):
    area = locations.Area.LandsEnd
    description = "Land's End chow pit left chest"
    rooms = [138]
    event = 247
    item = items.KerokeroCola


class LandsEndChowPit2(Chest):
    area = locations.Area.LandsEnd
    description = "Land's End chow pit right chest"
    rooms = [138]
    event = 246
    item = items.FrogCoin


class LandsEndBeeRoom(Chest):
    area = locations.Area.LandsEnd
    description = "Land's End bee room chest"
    rooms = [141]
    event = 247
    item = items.FrogCoin


class LandsEndSecret1(Chest):
    area = locations.Area.LandsEnd
    description = "Land's End grotto first chest"
    rooms = [270]
    event = 247
    item = items.FrogCoin


class LandsEndSecret2(Chest):
    area = locations.Area.LandsEnd
    description = "Land's End grotto corner chest"
    rooms = [270]
    event = 246
    item = items.FrogCoin


class LandsEndShyAway(Chest):
    area = locations.Area.LandsEnd
    description = "Land's End grotto near sewer chest"
    rooms = [401]
    event = 247
    item = items.RecoveryMushroom


class LandsEndStarChest1(Chest):
    area = locations.Area.LandsEnd
    description = "Land's End whirlpool 1st underground chest"
    rooms = [263]
    event = 172
    item = items.LandsEndVolcanoStar


class LandsEndStarChest2(Chest):
    area = locations.Area.LandsEnd
    description = "Land's End 1st purchase chest"
    rooms = [262]
    event = 172
    item = items.LandsEndStar2


class LandsEndStarChest3(Chest):
    area = locations.Area.LandsEnd
    description = "Land's End 2nd purchase chest"
    rooms = [262]
    event = 173
    item = items.LandsEndStar3


class TroopaClimb(NPCReward):
    area = locations.Area.LandsEnd
    description = "Land's End Troopa Climb sub-12 second prize"
    rooms = [407]
    event = 253
    item = items.TroopaPin


class LandsEndStarPiece1(BossStarPiece):
    area = locations.Area.LandsEnd
    description = "Land's End/Belome Temple cloud star piece"
    rooms = [519]
    event = 167


# *** Belome Temple

class BelomeTempleFortuneTeller(Chest):
    area = locations.Area.BelomeTemple
    description = "Belome Temple first fortune-telling room chest"
    rooms = [420]
    event = 247
    item = items.Coins(Chest, 50)


class BelomeTempleFortune1(Chest):
    area = locations.Area.BelomeTemple
    description = "Belome Temple left-middle-right fortune chest"
    rooms = [421]
    event = 247
    item = items.RecoveryMushroom


class BelomeTempleFortune2(Chest):
    area = locations.Area.BelomeTemple
    description = "Belome Temple left-right-middle fortune chest"
    rooms = [421]
    event = 246
    item = items.YoshiCookie


class BelomeTempleFortune3(Chest):
    area = locations.Area.BelomeTemple
    description = "Belome Temple right-left-middle fortune chest"
    rooms = [421]
    event = 245
    item = items.Flower


class BelomeTempleFortune4(Chest):
    area = locations.Area.BelomeTemple
    description = "Belome Temple right-middle-left fortune chest"
    rooms = [421]
    event = 244
    item = items.Coins(Chest, 100)


class BelomeTempleAfterFortune1(Chest):
    area = locations.Area.BelomeTemple
    description = "Belome Temple after fortune area right chest"
    rooms = [425]
    event = 247
    item = items.FrogCoin


class BelomeTempleAfterFortune2(Chest):
    area = locations.Area.BelomeTemple
    description = "Belome Temple after fortune area lower left chest"
    rooms = [425]
    event = 246
    item = items.Coins(Chest, 150)


class BelomeTempleAfterFortune3(Chest):
    area = locations.Area.BelomeTemple
    description = "Belome Temple after fortune area middle chest"
    rooms = [425]
    event = 245
    item = items.FrogCoin


class BelomeTempleAfterFortune4(Chest):
    area = locations.Area.BelomeTemple
    description = "Belome Temple after fortune area upper left chest"
    rooms = [425]
    event = 244
    item = items.FrogCoin


class BelomeTempleTreasureFlower1(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = "Belome Temple vault flower 1"
    rooms = [422]
    npc_ids = [0]
    event = 241
    item = items.Flower


class BelomeTempleTreasureFlower2(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = "Belome Temple vault flower 2"
    rooms = [422]
    npc_ids = [1]
    event = 240
    item = items.Flower


class BelomeTempleTreasureFlower3(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = "Belome Temple vault flower 3"
    rooms = [422]
    npc_ids = [2]
    event = 239
    item = items.Flower


class BelomeTempleTreasureFlower4(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = "Belome Temple vault flower 4"
    rooms = [422]
    npc_ids = [3]
    event = 238
    item = items.Flower


class BelomeTempleTreasureFrogCoin1(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = "Belome Temple vault frog coin 1"
    rooms = [422]
    npc_ids = [4]
    event = 237
    item = items.FrogCoin


class BelomeTempleTreasureFrogCoin2(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = "Belome Temple vault frog coin 2"
    rooms = [422]
    npc_ids = [5]
    event = 236
    item = items.FrogCoin


class BelomeTempleTreasureFrogCoin3(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = "Belome Temple vault frog coin 3"
    rooms = [422]
    npc_ids = [6]
    event = 235
    item = items.FrogCoin


class BelomeTempleTreasureFrogCoin4(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = "Belome Temple vault frog coin 4"
    rooms = [422]
    npc_ids = [7]
    event = 234
    item = items.FrogCoin


class BelomeTempleTreasureFrogCoin5(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = "Belome Temple vault frog coin 5"
    rooms = [422]
    npc_ids = [8]
    event = 233
    item = items.FrogCoin


class BelomeTempleTreasureFrogCoin6(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = "Belome Temple vault frog coin 6"
    rooms = [422]
    npc_ids = [9]
    event = 232
    item = items.FrogCoin


class BelomeTempleTreasureFrogCoin7(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = "Belome Temple vault frog coin 7"
    rooms = [422]
    npc_ids = [10]
    event = 231
    item = items.FrogCoin


class BelomeTempleTreasureFrogCoin8(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = "Belome Temple vault frog coin 8"
    rooms = [422]
    npc_ids = [11]
    event = 230
    item = items.FrogCoin


class BelomeTempleTreasure1(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = "Belome Temple vault middle item bag"
    rooms = [422]
    npc_ids = [14]
    event = 228
    item = items.RoyalSyrup
    coinsanity = False


class BelomeTempleTreasure2(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = "Belome Temple vault left item bag"
    rooms = [422]
    npc_ids = [13]
    event = 229
    item = items.MaxMushroom
    coinsanity = False


class BelomeTempleTreasure3(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = "Belome Temple vault right item bag"
    rooms = [422]
    npc_ids = [15]
    event = 227
    item = items.FireBomb
    coinsanity = False

class BelomeTempleBoss(BossStarPiece):
    description = "Belome Temple boss star piece"
    area = locations.Area.BelomeTemple
    rooms = [268]
    event = 167



# *** Monstro Town

class MonstroTownEntrance(Chest):
    area = locations.Area.MonstroTown
    description = "Monstro Town entrance chest"
    rooms = [267]
    event = 257
    item = items.FrogCoin


class MonstroTownThwomp(OverworldItem):
    area = locations.Area.MonstroTown
    description = "Monstro Town thwomp key"
    rooms = [324]
    event = 241
    npc_ids = [0]
    item = items.TempleKey
    key = True


class JinxDojoReward(NPCReward):
    area = locations.Area.MonstroTown
    description = "Monstro Town dojo prize"
    rooms = [255]
    event = 253
    item = items.JinxBelt

class DojoBoss1(BossStarPiece):
    description = "Monstro Town dojo first fight star piece"
    area = locations.Area.MonstroTown
    rooms = [255]
    event = 167

class DojoBoss2(BossStarPiece):
    description = "Monstro Town dojo second fight star piece"
    area = locations.Area.MonstroTown
    rooms = [515]
    event = 167

class DojoBoss3(BossStarPiece):
    description = "Monstro Town dojo third fight star piece"
    area = locations.Area.MonstroTown
    rooms = [516]
    event = 167


class DojoBoss4(BossStarPiece):
    description = "Monstro Town dojo fourth fight star piece"
    area = locations.Area.MonstroTown
    rooms = [517]
    event = 167


class CulexBoss(BossStarPiece):
    description = "Monstro Town sealed door star piece"
    area = locations.Area.MonstroTown
    rooms = [351]
    event = 167



class CulexReward(NPCReward):
    area = locations.Area.MonstroTown
    description = "Monstro Town sealed door prize"
    rooms = [351]
    event = 253
    item = items.QuartzCharm

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.ShinyStone)


class SuperJumps30(NPCReward):
    area = locations.Area.MonstroTown
    description = "Monstro Town Super Jump first prize"
    rooms = [397]
    event = 253
    item = items.AttackScarf
    # cannot gate all characters who learn Super Jump


class SuperJumps100(NPCReward):
    area = locations.Area.MonstroTown
    description = "Monstro Town Super Jump second prize"
    rooms = [397]
    event = 252
    item = items.SuperSuit
    # cannot gate all characters who learn Super Jump


class ThreeMustyFears(NPCReward):
    area = locations.Area.MonstroTown
    description = "Monstro Town flag exchange prize"
    rooms = [399]
    event = 253
    item = items.GhostMedal

    @staticmethod
    def can_access(inventory):
        return (inventory.has_item(items.BigBooFlag) and inventory.has_item(items.GreaperFlag) and
                inventory.has_item(items.DryBonesFlag))


# *** Bean Valley

class BeanValley1(Chest):
    description = "Bean Valley south upper level chest"
    area = locations.Area.BeanValley
    rooms = [252]
    event = 247
    item = items.Flower


class BeanValley2(Chest):
    description = "Bean Valley north upper level chest"
    area = locations.Area.BeanValley
    rooms = [252]
    event = 246
    item = items.FrogCoin


class BeanValleyLeftPiranhaPipe(Chest):
    area = locations.Area.BeanValley
    description = "Bean Valley left piranha pipe chest"
    rooms = [334]
    event = 247
    item = items.SlotMachineChest


class BeanValleyBottomLeftPiranhaPipe(Chest):
    area = locations.Area.BeanValley
    description = "Bean Valley bottom left piranha pipe chest"
    rooms = [348]
    event = 247
    item = items.SlotMachineChest


class BeanValleyBottomRightPiranhaPipeUpper(Chest):
    area = locations.Area.BeanValley
    description = "Bean Valley bottom right piranha pipe upper chest"
    rooms = [349]
    event = 247
    item = items.SlotMachineChest


class BeanValleyBottomRightPiranhaPipeLower(Chest):
    area = locations.Area.BeanValley
    description = "Bean Valley bottom right piranha pipe lower chest"
    rooms = [349]
    event = 246
    item = items.KerokeroCola


class BeanValleyBoxBoyRoom1(Chest):
    area = locations.Area.BeanValley
    description = "Bean Valley right piranha pipe left chest"
    rooms = [335]
    event = 247
    item = items.BoxBoyFight

class BoxBoyBoss(BossStarPiece):
    description = "Mimic #2 star piece"
    rooms = [514]
    event = 167
    
    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.BoxBoyFight)


class BeanValleyBoxBoyRoom2(Chest):
    area = locations.Area.BeanValley
    description = "Bean Valley right piranha pipe right chest"
    rooms = [335]
    event = 246
    item = items.RedEssence


class BeanValleyBoxBoyRoomHidden(NPCReward):
    area = locations.Area.BeanValley
    description = "Bean Valley right piranha pipe hidden stairway item"
    rooms = [335]
    event = 253
    item = items.FrogCoin
    coinsanity = True


class BeanValleyPiranhaPlants(Chest):
    description = "Bean Valley chest above Box Boy's room"
    area = locations.Area.BeanValley
    rooms = [251]
    event = 247
    item = items.FrogCoin


class BeanValleyMegasmilaxRoom(NPCReward):
    description = "Bean Valley boss reward"
    area = locations.Area.BeanValley
    rooms = [254]
    event = 253
    item = items.Seed
    key = True

class BeanValleyBoss(BossStarPiece):
    description = "Bean Valley boss star piece"
    area = locations.Area.BeanValley
    rooms = [254]
    event = 167



class BeanValleyBeanstalk(Chest):
    area = locations.Area.BeanValley
    description = "Bean Valley clouds solo vine chest"
    rooms = [379]
    event = 247
    item = items.Flower


class BeanValleyBeanstalkFrogCoin(OverworldItem):
    area = locations.Area.BeanValley
    description = "Bean Valley middle vine room freestanding frog coin"
    rooms = [379]
    event = 241
    npc_ids = [6]
    item = items.FrogCoin


class BeanValleyBeanstalkCoin1(OverworldItem):
    area = locations.Area.BeanValley
    description = "Bean Valley middle vine room lowest freestanding coin"
    rooms = [379]
    event = 240
    npc_ids = [3]
    item = items.Coins10


class BeanValleyBeanstalkCoin2(OverworldItem):
    area = locations.Area.BeanValley
    description = "Bean Valley middle vine room middle freestanding coin"
    rooms = [379]
    event = 239
    npc_ids = [4]
    item = items.Coins10


class BeanValleyBeanstalkCoin3(OverworldItem):
    area = locations.Area.BeanValley
    description = "Bean Valley middle vine room highest freestanding coin"
    rooms = [379]
    event = 238
    npc_ids = [5]
    item = items.Coins10


class BeanValleyEastBeanstalkCoin1(OverworldItem):
    area = locations.Area.BeanValley
    description = "Bean Valley east vine room lowest freestanding coin"
    rooms = [380]
    event = 241
    npc_ids = [3]
    item = items.Coins10


class BeanValleyEastBeanstalkCoin2(OverworldItem):
    area = locations.Area.BeanValley
    description = "Bean Valley east vine room lowest freestanding coin"
    rooms = [380]
    event = 240
    npc_ids = [4]
    item = items.Coins10


class BeanValleyEastBeanstalkCoin3(OverworldItem):
    area = locations.Area.BeanValley
    description = "Bean Valley east vine room middle freestanding coin"
    rooms = [380]
    event = 239
    npc_ids = [5]
    item = items.Coins10


class BeanValleyEastBeanstalkCoin4(OverworldItem):
    area = locations.Area.BeanValley
    description = "Bean Valley east vine room higher freestanding coin"
    rooms = [380]
    event = 238
    npc_ids = [6]
    item = items.Coins10


class BeanValleyEastBeanstalkCoin5(OverworldItem):
    area = locations.Area.BeanValley
    description = "Bean Valley east vine room highest freestanding coin"
    rooms = [380]
    event = 237
    npc_ids = [7]
    item = items.Coins10


class BeanValleyWestBeanstalkCoin1(OverworldItem):
    area = locations.Area.BeanValley
    description = "Bean Valley west vine room lower freestanding coin"
    rooms = [381]
    event = 241
    npc_ids = [4]
    item = items.Coins10


class BeanValleyWestBeanstalkCoin2(OverworldItem):
    area = locations.Area.BeanValley
    description = "Bean Valley west vine room middle freestanding coin"
    rooms = [381]
    event = 240
    npc_ids = [5]
    item = items.Coins10


class BeanValleyWestBeanstalkCoin3(OverworldItem):
    area = locations.Area.BeanValley
    description = "Bean Valley west vine room upper freestanding coin"
    rooms = [381]
    event = 239
    npc_ids = [6]
    item = items.Coins10


class BeanValleyWestBeanstalkFrogCoin(OverworldItem):
    area = locations.Area.BeanValley
    description = "Bean Valley west vine room freestanding frog coin"
    rooms = [381]
    event = 238
    npc_ids = [7]
    item = items.FrogCoin


class BeanValleyCloud1(Chest):
    area = locations.Area.BeanValley
    description = "Bean Valley clouds upper left chest"
    rooms = [372]
    event = 247
    item = items.FrogCoin


class BeanValleyCloud2(Chest):
    area = locations.Area.BeanValley
    description = "Bean Valley clouds upper right chest"
    rooms = [372]
    event = 246
    item = items.RareScarf


class BeanValleyFall1(Chest):
    area = locations.Area.BeanValley
    description = "Bean Valley clouds lower left chest"
    rooms = [373]
    event = 247
    item = items.Flower


class BeanValleyFall2(Chest):
    area = locations.Area.BeanValley
    description = "Bean Valley clouds lower right chest"
    rooms = [373]
    event = 246
    item = items.Flower


class BeanValleyFirstVineRoomFrogCoin(OverworldItem):
    area = locations.Area.BeanValley
    description = "Bean Valley lowest vine room freestanding frog coin"
    rooms = [378]
    script = 241
    npc_ids = [3]
    item = items.FrogCoin


class BeanValleyFirstVineRoomMiddleCoin(OverworldItem):
    area = locations.Area.BeanValley
    description = "Bean Valley lowest vine room middle freestanding coin"
    rooms = [378]
    script = 240
    npc_ids = [4]
    item = items.Coins10


class BeanValleyFirstVineRoomUpperCoin(OverworldItem):
    area = locations.Area.BeanValley
    description = "Bean Valley lowest vine room upper freestanding coin"
    rooms = [378]
    script = 239
    npc_ids = [5]
    item = items.Coins10


class BeanValleyFirstVineRoomLowerCoin(OverworldItem):
    area = locations.Area.BeanValley
    description = "Bean Valley lowest vine room lower freestanding coin"
    rooms = [378]
    script = 238
    npc_ids = [6]
    item = items.Coins10

# *** Grate Guy's Casino


class CasinoGrateGuyPrize(NPCReward):
    area = locations.Area.Casino
    description = "Grate Guy's Casino LOTW prize"
    rooms = [92]
    event = 253
    item = items.StarEgg

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.BrightCard)


# *** Nimbus Land

class NimbusLandShop(Chest):
    area = locations.Area.NimbusLand
    description = "Nimbus Land shop chest"
    rooms = [344]
    event = 247
    item = items.FrogCoin


class NimbusLandInn(NPCReward):
    area = locations.Area.NimbusLand
    description = "Nimbus Land dream cushion 1st item"
    shops = [346]
    script = 253
    item = items.RedEssence


class NimbusLandInn2(NPCReward):
    area = locations.Area.NimbusLand
    description = "Nimbus Land dream cushion 2nd item"
    shops = [346]
    script = 252
    item = items.RedEssence


class NimbusCastleBeforeBirdetta1(Chest):
    description = "Nimbus Castle (occupied) 5-door room chest"
    area = locations.Area.NimbusLand
    rooms = [118]
    event = 247
    item = items.Flower
    missable = True


class NimbusCastleBeforeBirdetta2(Chest):
    area = locations.Area.NimbusLand
    description = "Nimbus Castle west two-level room chest"
    rooms = [111, 500]
    event = 247
    item = items.Flower


class NimbusCastleBirdetta(NPCReward):
    area = locations.Area.NimbusLand
    description = "Nimbus Castle giant egg prize"
    rooms = [409]
    event = 253
    item = items.CastleKey2
    key = True

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.CastleKey1)

class NimbusCastleStarPiece2(BossStarPiece):
    description = "Nimbus Land giant egg boss star piece"
    area = locations.Area.NimbusLand
    rooms = [409]
    event = 167

    @staticmethod
    def can_access(inventory):
        return inventory.has_item(items.CastleKey1)

class NimbusCastleOutOfBounds1(Chest):
    area = locations.Area.NimbusLand
    description = "Nimbus Castle west stairway room left chest"
    rooms = [410]
    event = 247
    item = items.FrogCoin


class NimbusCastleOutOfBounds2(Chest):
    area = locations.Area.NimbusLand
    description = "Nimbus Castle west stairway room right chest"
    rooms = [410]
    event = 246
    item = items.FrogCoin


class NimbusCastleSingleGoldBird(Chest):
    area = locations.Area.NimbusLand
    description = "Nimbus Castle single gold bird room chest"
    rooms = [113]
    event = 247
    item = items.RecoveryMushroom


class NimbusCastleAfterEgg1(Chest):
    description = "Nimbus Castle east two-level room lower chest"
    area = locations.Area.NimbusLand
    rooms = [114, 498]
    event = 247
    item = items.Flower

    @staticmethod
    def can_access(inventory):
        return locations.can_clear_nimbus_castle(inventory)


class NimbusCastleAfterEgg2(Chest):
    description = "Nimbus Castle east two-level room upper chest"
    area = locations.Area.NimbusLand
    rooms = [114, 498]
    event = 246
    item = items.FrogCoin

    @staticmethod
    def can_access(inventory):
        return locations.can_clear_nimbus_castle(inventory)


class NimbusCastleStarPiece3(BossStarPiece):
    description = "Nimbus Land final boss star piece"
    area = locations.Area.NimbusLand
    rooms = [430]
    event = 167

    @staticmethod
    def can_access(inventory):
        return locations.can_clear_nimbus_castle(inventory)

class NimbusCastleStarChest(Chest):
    description = "Nimbus Castle post-throne chest (occupied)"
    area = locations.Area.NimbusLand
    rooms = [121]
    event = 247
    item = items.NimbusLandStar
    missable = True

    @staticmethod
    def can_access(inventory):
        return locations.can_clear_nimbus_castle(inventory)


class NimbusCastleStarAfterValentina(Chest):
    description = "Nimbus Castle post-throne chest (unoccupied)"
    area = locations.Area.NimbusLand
    rooms = [121]
    event = 246
    item = items.Flower

    @staticmethod
    def can_access(inventory):
        return locations.can_clear_nimbus_castle(inventory)


class NimbusCastleCornerChestAfterValentina(Chest):
    description = "Nimbus Castle (unoccupied) 5-door room chest"
    area = locations.Area.NimbusLand
    rooms = [499]
    event = 247
    item = items.FrogCoin

    @staticmethod
    def can_access(inventory):
        return locations.can_clear_nimbus_castle(inventory)


class NimbusLandRightSide(NPCReward):
    description = "Nimbus Land post-invasion off-cloud item"
    area = locations.Area.NimbusLand
    rooms = [438]
    event = 253
    item = items.Fertilizer
    key = True

    @staticmethod
    def can_access(inventory):
        return locations.can_clear_nimbus_castle(inventory)


class DodoReward(NPCReward):
    description = "Nimbus Land Dodo's statue game prize"
    area = locations.Area.NimbusLand
    rooms = [110]
    event = 253
    item = items.Feather
    missable = True


class NimbusLandStarPiece1(BossStarPiece):
    description = "Nimbus Land statue keeper boss star piece"
    area = locations.Area.NimbusLand
    rooms = [520]
    event = 167

class NimbusLandPrisoners(NPCReward):
    area = locations.Area.NimbusLand
    description = "Nimbus Castle west cellar civilian"
    rooms = [414]
    event = 253
    item = items.FlowerJar


class NimbusLandPrisoners2(NPCReward):
    area = locations.Area.NimbusLand
    description = "Nimbus Castle west cellar guard"
    rooms = [414]
    event = 252
    item = items.CastleKey1
    key = True


class NimbusLandSignalRing(OverworldItem):
    area = locations.Area.NimbusLand
    description = "Nimbus Land post-invasion upper right house"
    rooms = [345]
    npc_ids = [5]
    event = 241
    item = items.SignalRing
    coinsanity = False

    @staticmethod
    def can_access(inventory):
        return locations.can_clear_nimbus_castle(inventory)


class NimbusLandCellar(NPCReward):
    area = locations.Area.NimbusLand
    description = "Nimbus Castle post-invasion north cellar"
    rooms = [413]
    event = 253
    item = items.FlowerJar

    @staticmethod
    def can_access(inventory):
        return locations.can_clear_nimbus_castle(inventory)


# *** Barrel Volcano

class BarrelVolcanoSecret1(Chest):
    area = locations.Area.BarrelVolcano
    description = "Barrel Volcano secret room left chest"
    rooms = [355]
    event = 247
    item = items.Flower
    # volcano access


class BarrelVolcanoSecret2(Chest):
    area = locations.Area.BarrelVolcano
    description = "Barrel Volcano secret room right chest"
    rooms = [355]
    event = 246
    item = items.Flower
    # volcano access


class BarrelVolcanoReverse(OverworldItem):
    area = locations.Area.BarrelVolcano
    description = "Barrel Volcano reverse lava recoil frog coin"
    rooms = [383]
    event = 241
    npc_ids = [4]
    item = items.FrogCoin
    # volcano access


class BarrelVolcanoDonut1(Chest):
    area = locations.Area.BarrelVolcano
    description = "Barrel Volcano first donut lift room right freestanding frog coin"
    rooms = [358]
    event = 241
    item = items.FrogCoin
    # volcano access


class BarrelVolcanoDonut2(Chest):
    area = locations.Area.BarrelVolcano
    description = "Barrel Volcano first donut lift room left freestanding frog coin"
    rooms = [358]
    event = 240
    item = items.FrogCoin
    # volcano access


class BarrelVolcanoLavaPool(Chest):
    area = locations.Area.BarrelVolcano
    description = "Barrel Volcano lava pool freestanding frog coin"
    rooms = [361]
    event = 241
    item = items.FrogCoin
    # volcano access


class BarrelVolcanoBeforeStar1(Chest):
    area = locations.Area.BarrelVolcano
    description = "Barrel Volcano second arrow sign room left chest"
    rooms = [384]
    event = 247
    item = items.Flower
    # volcano access


class BarrelVolcanoBeforeStar2(Chest):
    area = locations.Area.BarrelVolcano
    description = "Barrel Volcano second arrow sign room right chest"
    rooms = [384]
    event = 246
    item = items.Coins(Chest, 100)
    # volcano access


class BarrelVolcanoStarRoom(Chest):
    area = locations.Area.BarrelVolcano
    description = "Barrel Volcano star chest"
    rooms = [385]
    event = 247
    item = items.LandsEndVolcanoStar
    # volcano access


class BarrelVolcanoSaveRoom1(Chest):
    area = locations.Area.BarrelVolcano
    description = "Barrel Volcano save room lower chest"
    rooms = [366]
    event = 247
    item = items.Flower
    # volcano access


class BarrelVolcanoSaveRoom2(Chest):
    area = locations.Area.BarrelVolcano
    description = "Barrel Volcano save room upper chest"
    rooms = [366]
    event = 246
    item = items.FrogCoin
    # volcano access


class BarrelVolcanoHinopio(Chest):
    area = locations.Area.BarrelVolcano
    description = "Barrel Volcano Hinopio shop chest"
    rooms = [367]
    event = 247
    item = items.Coins(Chest, 100)
    # volcano access

class BarrelVolcanoBoss1(BossStarPiece):
    description = "Barrel Volcano first boss star piece"
    area = locations.Area.BarrelVolcano
    rooms = [352]
    event = 167
    # volcano access

class BarrelVolcanoBoss2(BossStarPiece):
    description = "Barrel Volcano second boss star piece"
    area = locations.Area.BarrelVolcano
    rooms = [393]
    event = 167
    item = items.StarPiece
    # volcano access


# *** Bowser's Keep

class BowsersKeepDarkRoom(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep dark room chest"
    rooms = [453]
    event = 247
    item = items.RecoveryMushroom
    # keep access


class BowsersKeepCrocoShop1(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep near first shop left chest"
    rooms = [451]
    event = 247
    item = items.Coins(Chest, 150)
    # keep access


class BowsersKeepCrocoShop2(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep near first shop right chest"
    rooms = [451]
    event = 246
    item = items.RecoveryMushroom
    # keep access


class BowsersKeepMagikoopa(Chest):
    description = "Bowser's Keep Magikoopa's room chest"
    area = locations.Area.BowsersKeep
    rooms = [266]
    script = 247
    item = items.InfiniteCoins
    # keep access


class BowsersKeepBossChester(BossStarPiece):
    description = "Bowser's Keep battle door star piece"
    area = locations.Area.BowsersKeep
    rooms = [461]
    event = 167


class BowsersKeepBoss1(BossStarPiece):
    description = "Bowser's Keep first boss star piece"
    area = locations.Area.BowsersKeep
    rooms = [266]
    event = 167
    # keep access


class BowsersKeepInvisibleBridge1(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep 6-door invisble bridge bottom chest"
    rooms = [322]
    script = 247
    item = items.FrightBomb
    # keep access


class BowsersKeepInvisibleBridge2(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep 6-door invisble bridge right chest"
    rooms = [322]
    script = 246
    item = items.RoyalSyrup
    # keep access


class BowsersKeepInvisibleBridge3(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep 6-door invisble bridge left chest"
    rooms = [322]
    script = 245
    item = items.IceBomb
    # keep access


class BowsersKeepInvisibleBridge4(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep 6-door invisble bridge top chest"
    rooms = [322]
    script = 244
    item = items.RockCandy
    # keep access


class BowsersKeepInvisibleBridgeCoin1(OverworldItem):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep 6-door invisble bridge bottom left coin"
    rooms = [322]
    script = 241
    npc_ids = [8]
    item = items.Coins10
    # keep access


class BowsersKeepInvisibleBridgeCoin2(OverworldItem):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep 6-door invisble bridge bottom right coin"
    rooms = [322]
    script = 240
    npc_ids = [9]
    item = items.Coins10
    # keep access


class BowsersKeepInvisibleBridgeCoin3(OverworldItem):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep 6-door invisble bridge top left coin"
    rooms = [322]
    script = 239
    npc_ids = [10]
    item = items.Coins10
    # keep access


class BowsersKeepInvisibleBridgeCoin4(OverworldItem):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep 6-door invisble bridge top right coin"
    rooms = [322]
    script = 238
    npc_ids = [11]
    item = items.Coins10
    # keep access


class BowsersKeepMovingPlatforms1(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep X-Y platform room left exit chest"
    rooms = [458]
    event = 247
    item = items.Flower
    # keep access


class BowsersKeepMovingPlatforms2(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep X-Y platform room left entrance chest"
    rooms = [458]
    event = 246
    item = items.RedEssence
    # keep access


class BowsersKeepMovingPlatforms3(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep X-Y platform room right entrance chest"
    rooms = [458]
    event = 245
    item = items.MaxMushroom
    # keep access


class BowsersKeepMovingPlatforms4(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep X-Y platform room right exit chest"
    rooms = [458]
    event = 244
    item = items.FireBomb
    # keep access


class BowsersKeepElevatorPlatforms(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep 6-door elevator platform room chest"
    rooms = [321]
    script = 247
    item = items.KerokeroCola
    # keep access


class BowsersKeepCannonballRoom1(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep cannonball room lower right chest"
    rooms = [457]
    event = 247
    item = items.Flower
    # keep access


class BowsersKeepCannonballRoom2(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep cannonball room exit chest"
    rooms = [457]
    event = 246
    item = items.Flower
    # keep access


class BowsersKeepCannonballRoom3(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep cannonball room lower left chest"
    rooms = [457]
    event = 245
    item = items.PickMeUp
    # keep access


class BowsersKeepCannonballRoom4(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep cannonball room upper right chest"
    rooms = [457]
    event = 244
    item = items.RockCandy
    # keep access


class BowsersKeepCannonballRoom5(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep cannonball room upper left chest"
    rooms = [457]
    event = 243
    item = items.MaxMushroom
    # keep access


class BowsersKeepCannonballRoomCoin1(OverworldItem):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep cannonball room freestanding coin 1"
    rooms = [457]
    event = 241
    npc_ids = [8]
    item = items.Coins10
    # keep access


class BowsersKeepCannonballRoomCoin2(OverworldItem):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep cannonball room freestanding coin 2"
    rooms = [457]
    event = 240
    npc_ids = [9]
    item = items.Coins10
    # keep access


class BowsersKeepCannonballRoomCoin3(OverworldItem):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep cannonball room freestanding coin 3"
    rooms = [457]
    event = 239
    npc_ids = [10]
    item = items.Coins10
    # keep access


class BowsersKeepCannonballRoomCoin4(OverworldItem):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep cannonball room freestanding coin 4"
    rooms = [457]
    event = 238
    npc_ids = [11]
    item = items.Coins10
    # keep access


class BowsersKeepCannonballRoomCoin5(OverworldItem):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep cannonball room freestanding coin 5"
    rooms = [457]
    event = 237
    npc_ids = [12]
    item = items.Coins10
    # keep access


class BowsersKeepCannonballRoomCoin6(OverworldItem):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep cannonball room freestanding coin 6"
    rooms = [457]
    event = 236
    npc_ids = [13]
    item = items.Coins10
    # keep access


class BowsersKeepCannonballRoomCoin7(OverworldItem):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep cannonball room freestanding coin 7"
    rooms = [457]
    event = 235
    npc_ids = [14]
    item = items.Coins10
    # keep access


class BowsersKeepCannonballRoomCoin8(OverworldItem):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep cannonball room freestanding coin 8"
    rooms = [457]
    event = 234
    npc_ids = [15]
    item = items.Coins10
    # keep access


class BowsersKeepRotatingPlatforms1(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep rotating platform room entrance chest"
    rooms = [455]
    event = 247
    item = items.Flower
    # keep access


class BowsersKeepRotatingPlatforms2(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep rotating platform lower left chest"
    rooms = [455]
    event = 246
    item = items.Flower
    # keep access


class BowsersKeepRotatingPlatforms3(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep rotating platform right chest"
    rooms = [455]
    event = 245
    item = items.FireBomb
    # keep access


class BowsersKeepRotatingPlatforms4(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep rotating platform center chest"
    rooms = [455]
    event = 244
    item = items.RoyalSyrup
    # keep access


class BowsersKeepRotatingPlatforms5(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep rotating platform upper left chest"
    rooms = [455]
    event = 243
    item = items.PickMeUp
    # keep access


class BowsersKeepRotatingPlatforms6(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep rotating platform exit chest"
    rooms = [455]
    event = 242
    item = items.KerokeroCola
    # keep access


class BowsersKeepDoorReward1(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep door prize 1"
    rooms = [144, 446]
    event = 247
    item = items.SonicCymbal
    # keep access


class BowsersKeepDoorReward2(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep door prize 2"
    rooms = [144, 446]
    event = 246
    item = items.SuperSlap
    # keep access


class BowsersKeepDoorReward3(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep door prize 3"
    rooms = [144, 446]
    event = 245
    item = items.DrillClaw
    # keep access


class BowsersKeepDoorReward4(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep door prize 4"
    rooms = [144, 446]
    event = 244
    item = items.StarGun
    # keep access


class BowsersKeepDoorReward5(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep door prize 5"
    rooms = [144, 446]
    event = 243
    item = items.RockCandy
    # keep access


class BowsersKeepDoorReward6(Chest):
    area = locations.Area.BowsersKeep
    description = "Bowser's Keep door prize 6"
    rooms = [144, 446]
    event = 242
    item = items.RockCandy
    # keep access


class BowsersKeepBoss2(BossStarPiece):
    description = "Bowser's Keep second boss star piece"
    area = locations.Area.BowsersKeep
    rooms = [521]
    event = 167
    # keep access

class BowsersKeepBoss3(BossStarPiece):
    description = "Bowser's Keep third boss star piece"
    area = locations.Area.BowsersKeep
    rooms = [522]
    event = 167
    # keep access


# *** Factory

class FactorySaveRoom(Chest):
    area = locations.Area.Factory
    description = "Outer Factory early save room chest"
    rooms = [237]
    event = 247
    item = items.RecoveryMushroom
    # factory access


class FactoryBoltPlatforms(Chest):
    area = locations.Area.Factory
    description = "Outer Factory bot platform chest"
    rooms = [239]
    event = 247
    item = items.UltraHammer
    # factory access


class FactoryBoss1(BossStarPiece):
    description = "Outer Factory first boss star piece"
    area = locations.Area.Factory
    rooms = [223]
    event = 167
    # factory access

class FactoryFallingAxems(Chest):
    area = locations.Area.Factory
    description = "Outer Factory falling axem room chest"
    rooms = [434]
    event = 247
    item = items.RecoveryMushroom
    # factory access


class FactoryTreasurePit1(Chest):
    area = locations.Area.Factory
    description = "Outer Factory pit back chest"
    rooms = [443]
    event = 247
    item = items.RecoveryMushroom
    # factory access


class FactoryTreasurePit2(Chest):
    area = locations.Area.Factory
    description = "Outer Factory pit front chest"
    rooms = [443]
    event = 245
    item = items.Flower
    # factory access


class FactoryConveyorPlatforms1(Chest):
    area = locations.Area.Factory
    description = "Outer Factory conveyor room right chest"
    rooms = [475]
    event = 247
    item = items.RoyalSyrup
    # factory access


class FactoryConveyorPlatforms2(Chest):
    area = locations.Area.Factory
    description = "Outer Factory conveyor room left chest"
    rooms = [475]
    event = 246
    item = items.MaxMushroom
    # factory access


class FactoryBehindSnakes1(Chest):
    area = locations.Area.Factory
    description = "Outer Factory room behind machine yarid right chest"
    rooms = [443]
    event = 246
    item = items.RecoveryMushroom
    # factory access


class FactoryBehindSnakes2(Chest):
    area = locations.Area.Factory
    description = "Outer Factory room behind machine yarid left chest"
    rooms = [443]
    event = 244
    item = items.Flower
    # factory access

class FactoryBoss2(BossStarPiece):
    description = "Outer Factory second boss star piece"
    area = locations.Area.Factory
    rooms = [103]
    event = 167
    # factory access

class FactoryToadGift(NPCReward):
    area = locations.Area.Factory
    description = "Inner Factory toad gift"
    rooms = [406]
    event = 253
    item = items.RockCandy
    # factory access

class InnerFactoryBoss1(BossStarPiece):
    description = "Inner Factory first boss star piece"
    area = locations.Area.Factory
    rooms = [469]
    event = 167
    # factory access

class InnerFactoryBoss2(BossStarPiece):
    description = "Inner Factory second boss star piece"
    area = locations.Area.Factory
    rooms = [470]
    event = 167
    # factory access

class InnerFactoryBoss3(BossStarPiece):
    description = "Inner Factory third boss star piece"
    area = locations.Area.Factory
    rooms = [471]
    event = 167
    # factory access

class InnerFactoryBoss4(BossStarPiece):
    description = "Inner Factory fourth boss star piece"
    area = locations.Area.Factory
    rooms = [472]
    event = 167
    # factory access


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
        MariosPadBed(world),
        MariosPadStarter1(world),
        MariosPadStarter2(world),
        MariosPadStarter3(world),
        MariosPadStarter4(world),
        MushroomWay1(world),
        MushroomWay2(world),
        MushroomWay3(world),
        MushroomWay4(world),
        ToadRescue1(world),
        ToadRescue2(world),
        HammerBrosReward(world),
        MushroomKingdomHallway(world),
        MushroomKingdomVault1(world),
        MushroomKingdomVault2(world),
        MushroomKingdomVault3(world),
        InvasionVault1(world),
        InvasionVault2(world),
        InvasionVault3(world),
        InvasionEasternGuard(world),
        WalletGuy1(world),
        WalletGuy2(world),
        MushroomKingdomStore(world),
        MushroomKingdomStoreExchange(world),
        MushroomKingdomStoreBasement1(world),
        MushroomKingdomStoreBasement2(world),
        PeachSurprise(world),
        InvasionToadRescue(world),
        InvasionFamily(world),
        InvasionGuestRoom(world),
        MushroomKingdomInn(world),
        BanditsWay1(world),
        BanditsWay2(world),
        BanditsWayStarChest(world),
        BanditsWayDogJump(world),
        BanditsWayCroco(world),
        Croco1Reward(world),
        Croco1Reward2(world),
        KeroSewersPandoriteRoom(world),
        PandoriteChest(world),
        PandoriteReward1(world),
        PandoriteReward2(world),
        KeroSewersStarChest(world),
        KeroSewersBeforeBelomeLower(world),
        KeroSewersBeforeBelomeUpper1(world),
        KeroSewersBeforeBelomeUpper2(world),
        MidasRiverFirstTime(world),
        CricketPieReward(world),
        CricketJamReward(world),
        MelodyBay1(world),
        MelodyBay2(world),
        MelodyBay3(world),
        RoseWayPlatform(world),
        RoseWayFiveChests1(world),
        RoseWayFiveChests2(world),
        RoseWayFiveChests3(world),
        RoseWayFiveChests4(world),
        RoseWayFiveChests5(world),
        RoseTownFlag(world),
        RoseTownStore1(world),
        RoseTownStore2(world),
        GardenerCloud1(world),
        GardenerCloud2(world),
        RoseTownToad(world),
        Gaz(world),
        RoseTownTreasureHouse1(world),
        RoseTownTreasureHouse2(world),
        RoseTownTreasureHouseMazeReward(world),
        RoseTownTreasureHouse3(world),
        ForestMaze1(world),
        ForestMaze2(world),
        ForestMazeUnderground1(world),
        ForestMazeUnderground2(world),
        ForestMazeUnderground3(world),
        ForestMazeRedEssence(world),
        ForestMazeSecret1(world),
        ForestMazeSecret2(world),
        ForestMazeSecret3(world),
        ForestMazeSecret4(world),
        ForestMazeSecret5(world),
        PipeVaultSlide1(world),
        PipeVaultSlide2(world),
        PipeVaultSlide3(world),
        PipeVaultNippers1(world),
        PipeVaultNippers2(world),
        GoombaThumping1(world),
        GoombaThumping2(world),
        YosterIsleEntrance(world),
        YosterIsleRaceReward1(world),
        YosterIsleRaceReward2(world),
        YosterIsleRaceReward3(world),
        YosterIsleFlag(world),
        BucketGirl(world),
        TreasureSeller1(world),
        TreasureSeller2(world),
        TreasureSeller3(world),
        FireworksShop(world),
        MolevilleMinesStarChest(world),
        MolevilleMinesShyGuy(world),
        MolevilleMinesCoins(world),
        MolevilleMinesPunchinello1(world),
        MolevilleMinesPunchinello2(world),
        CrocoFlunkie1(world),
        CrocoFlunkie2(world),
        CrocoFlunkie3(world),
        Croco2Item(world),
        BoosterPass1(world),
        BoosterPass2(world),
        BoosterPassFlower(world),
        BoosterPassSecret1(world),
        BoosterPassSecret2(world),
        BoosterPassSecret3(world),
        BoosterTowerSpookum(world),
        BoosterTowerThwomp(world),
        BoosterTowerKnifeGuy(world),
        BoosterTowerRoomKey(world),
        BoosterTowerMasher(world),
        BoosterTowerParachute(world),
        BoosterTowerZoomShoes(world),
        BoosterTowerTop1(world),
        BoosterTowerTop2(world),
        BoosterTowerTop3(world),
        BoosterTowerRailway(world),
        BoosterTowerPortraits(world),
        BoosterTowerChomp(world),
        BoosterTowerCurtainGame(world),
        MarrymorePrize1(world),
        MarrymorePrize2(world),
        MarrymorePrize3(world),
        MarrymorePrize4(world),
        MarrymorePrize5(world),
        MarrymorePrize6(world),
        MarrymoreInn(world),
        SeasideTownBossPrize(world),
        SeasideTownRescue(world),
        SeaStarChest(world),
        SeaSaveRoom1(world),
        SeaSaveRoom2(world),
        SeaSaveRoom3(world),
        SeaWhirlpoolChest(world),
        SunkenShipRatStairs(world),
        SunkenShipShop(world),
        SunkenShipCoins1(world),
        SunkenShipCoins2(world),
        SunkenShipCloneRoom(world),
        SunkenShipFrogCoinRoom(world),
        SunkenShipHidonMushroom(world),
        SunkenShipHidonChest(world),
        HidonReward1(world),
        HidonReward2(world),
        SunkenShipSafetyRing(world),
        SunkenShipBandanaReds(world),
        SunkenShip3DMaze(world),
        SunkenShipCannonballPuzzle(world),
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
        TroopaClimb(world),
        BelomeTempleFortuneTeller(world),
        BelomeTempleFortune1(world),
        BelomeTempleFortune2(world),
        BelomeTempleFortune3(world),
        BelomeTempleFortune4(world),
        BelomeTempleAfterFortune1(world),
        BelomeTempleAfterFortune2(world),
        BelomeTempleAfterFortune3(world),
        BelomeTempleAfterFortune4(world),
        BelomeTempleTreasure1(world),
        BelomeTempleTreasure2(world),
        BelomeTempleTreasure3(world),
        MonstroTownEntrance(world),
        MonstroTownThwomp(world),
        JinxDojoReward(world),
        CulexReward(world),
        SuperJumps30(world),
        SuperJumps100(world),
        ThreeMustyFears(world),
        BeanValley1(world),
        BeanValley2(world),
        BeanValleyLeftPiranhaPipe(world),
        BeanValleyBottomLeftPiranhaPipe(world),
        BeanValleyBottomRightPiranhaPipeUpper(world),
        BeanValleyBottomRightPiranhaPipeLower(world),
        BeanValleyBoxBoyRoom1(world),
        BeanValleyBoxBoyRoom2(world),
        BeanValleyPiranhaPlants(world),
        BeanValleyMegasmilaxRoom(world),
        BeanValleyBeanstalk(world),
        BeanValleyBeanstalkFrogCoin(world),
        BeanValleyCloud1(world),
        BeanValleyCloud2(world),
        BeanValleyFall1(world),
        BeanValleyFall2(world),
        CasinoGrateGuyPrize(world),
        NimbusLandShop(world),
        NimbusLandInn(world),
        NimbusLandInn2(world),
        NimbusCastleBeforeBirdetta1(world),
        NimbusCastleBeforeBirdetta2(world),
        NimbusCastleBirdetta(world),
        NimbusCastleOutOfBounds1(world),
        NimbusCastleOutOfBounds2(world),
        NimbusCastleSingleGoldBird(world),
        NimbusCastleAfterEgg1(world),
        NimbusCastleAfterEgg2(world),
        NimbusCastleStarChest(world),
        NimbusCastleStarAfterValentina(world),
        NimbusCastleCornerChestAfterValentina(world),
        NimbusLandRightSide(world),
        DodoReward(world),
        NimbusLandPrisoners(world),
        NimbusLandPrisoners2(world),
        NimbusLandSignalRing(world),
        NimbusLandCellar(world),
        BarrelVolcanoSecret1(world),
        BarrelVolcanoSecret2(world),
        BarrelVolcanoBeforeStar1(world),
        BarrelVolcanoBeforeStar2(world),
        BarrelVolcanoStarRoom(world),
        BarrelVolcanoSaveRoom1(world),
        BarrelVolcanoSaveRoom2(world),
        BarrelVolcanoHinopio(world),
        BowsersKeepDarkRoom(world),
        BowsersKeepCrocoShop1(world),
        BowsersKeepCrocoShop2(world),
        BowsersKeepMagikoopa(world),
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
        FactoryTreasurePit1(world),
        FactoryTreasurePit2(world),
        FactoryConveyorPlatforms1(world),
        FactoryConveyorPlatforms2(world),
        FactoryBehindSnakes1(world),
        FactoryBehindSnakes2(world),
        FactoryToadGift(world),

    ]

def get_freestanding_item_checks(world):
    """Get reward lists for freestanding coins, frog coins, flowers, and mushrooms.

    Args:
        world (randomizer.logic.main.GameWorld):

    Returns:
        list[ItemLocation]: List of default freestanding objects.
    """
    return [
        # Chests
        BanditsWayCoin1(world),
        BanditsWayCoin2(world),
        BanditsWayCoin3(world),
        MidasRiverBottomLeftCave(world),
        MidasRiverBottomRightCave(world),
        RoseWayFlower(world),
        RoseWayMushroom(world),
        RoseWayCoin1(world),
        RoseWayCoin2(world),
        RoseWayCoin3(world),
        RoseWayCoin4(world),
        RoseWayCoin5(world),
        PipeVaultSlideCoin1(world),
        PipeVaultSlideCoin2(world),
        PipeVaultSlideCoin3(world),
        PipeVaultSlideCoin4(world),
        PipeVaultSlideCoin5(world),
        PipeVaultSlideFrogCoin(world),
        BoosterPassBush(world),
        BoosterPassFlower(world),
        BoosterTowerFrogCoin1(world),
        BoosterTowerFrogCoin2(world),
        BoosterTowerFrogCoin3(world),
        BoosterTowerFrogCoin4(world),
        BoosterTowerCoin1(world),
        BoosterTowerCoin2(world),
        BoosterTowerCoin3(world),
        BoosterTowerCoin4(world),
        BoosterTowerCoin5(world),
        BoosterTowerCoin6(world),
        BoosterTowerCoin7(world),
        BoosterTowerCoin8(world),
        BoosterTowerCoin9(world),
        BoosterTowerParachuteCrevice(world),
        SunkenShipRatStairsFlower(world),
        SunkenShipUnderwaterFrogCoin1(world),
        SunkenShipUnderwaterFrogCoin2(world),
        SunkenShipUnderwaterFrogCoin3(world),
        SunkenShipUnderwaterFrogCoin4(world),
        SunkenShipBlooberRoom(world),
        SunkenShipTrampolinePuzzle(world),
        SunkenShipTroopaPuzzle(world),
        SunkenShipCoinSnake(world),
        SunkenShipBarrelPuzzle(world),
        BelomeTempleTreasureFlower1(world),
        BelomeTempleTreasureFlower2(world),
        BelomeTempleTreasureFlower3(world),
        BelomeTempleTreasureFlower4(world),
        BelomeTempleTreasureFrogCoin1(world),
        BelomeTempleTreasureFrogCoin2(world),
        BelomeTempleTreasureFrogCoin3(world),
        BelomeTempleTreasureFrogCoin4(world),
        BelomeTempleTreasureFrogCoin5(world),
        BelomeTempleTreasureFrogCoin6(world),
        BelomeTempleTreasureFrogCoin7(world),
        BelomeTempleTreasureFrogCoin8(world),
        BeanValleyBoxBoyRoomHidden(world),
        BeanValleyBeanstalkFrogCoin(world),
        BeanValleyBeanstalkCoin1(world),
        BeanValleyBeanstalkCoin2(world),
        BeanValleyBeanstalkCoin3(world),
        BeanValleyEastBeanstalkCoin1(world),
        BeanValleyEastBeanstalkCoin2(world),
        BeanValleyEastBeanstalkCoin3(world),
        BeanValleyEastBeanstalkCoin4(world),
        BeanValleyEastBeanstalkCoin5(world),
        BeanValleyWestBeanstalkCoin1(world),
        BeanValleyWestBeanstalkCoin2(world),
        BeanValleyWestBeanstalkCoin3(world),
        BeanValleyWestBeanstalkFrogCoin(world),
        BeanValleyFirstVineRoomFrogCoin(world),
        BeanValleyFirstVineRoomMiddleCoin(world),
        BeanValleyFirstVineRoomUpperCoin(world),
        BeanValleyFirstVineRoomLowerCoin(world),
        BarrelVolcanoReverse(world),
        BarrelVolcanoDonut1(world),
        BarrelVolcanoDonut2(world),
        BarrelVolcanoLavaPool(world),
        BowsersKeepInvisibleBridgeCoin1(world),
        BowsersKeepInvisibleBridgeCoin2(world),
        BowsersKeepInvisibleBridgeCoin3(world),
        BowsersKeepInvisibleBridgeCoin4(world),
        BowsersKeepCannonballRoomCoin1(world),
        BowsersKeepCannonballRoomCoin2(world),
        BowsersKeepCannonballRoomCoin3(world),
        BowsersKeepCannonballRoomCoin4(world),
        BowsersKeepCannonballRoomCoin5(world),
        BowsersKeepCannonballRoomCoin6(world),
        BowsersKeepCannonballRoomCoin7(world),
        BowsersKeepCannonballRoomCoin8(world),

    ]

def get_boss_star_piece_checks(world):
    """Get list of star piece exclusive locations.

    Args:
        world (randomizer.logic.main.GameWorld):

    Returns:
        list[ItemLocation]: List of exclusive star piece location objects.
    """
    return [
        MushroomWayStarPiece(world),
        InvasionStarPiece(world),
        BanditsWayStarPiece(world),
        PandoriteBoss(world),
        KeroSewersBoss(world),
        ForestMazeBoss(world),
        MolevilleMinesBoss1(world),
        MolevilleMinesBoss2(world),
        BoosterTowerStarPiece1(world),
        BoosterTowerStarPiece2(world),
        MarrymoreStarPiece(world),
        StarHillStarPiece1(world),
        SeasideTownBoss(world),
        HidonBoss(world),
        SunkenShipMidboss(world),
        SunkenShipBoss(world),
        LandsEndStarPiece1(world),
        BelomeTempleBoss(world),
        DojoBoss1(world),
        DojoBoss2(world),
        DojoBoss3(world),
        DojoBoss4(world),
        CulexBoss(world),
        BoxBoyBoss(world),
        BeanValleyBoss(world),
        NimbusLandStarPiece1(world),
        NimbusCastleStarPiece2(world),
        NimbusCastleStarPiece3(world),
        BarrelVolcanoBoss1(world),
        BarrelVolcanoBoss2(world),
        BowsersKeepBossChester(world),
        BowsersKeepBoss1(world),
        BowsersKeepBoss2(world),
        BowsersKeepBoss3(world),
        FactoryBoss1(world),
        FactoryBoss2(world),
        InnerFactoryBoss1(world),
        InnerFactoryBoss2(world),
        InnerFactoryBoss3(world),
        InnerFactoryBoss4(world)
    ]

def get_starter_character_checks(world):
    """Get list of starter character placeholders.

    Args:
        world (randomizer.logic.main.GameWorld):

    Returns:
        list[ItemLocation]: List of starter character placeholder objects.
    """
    return [
        StarterCharacter1(world),
        StarterCharacter2(world),
        StarterCharacter3(world),
        StarterCharacter4(world),
        StarterCharacter5(world)

    ]

def get_recruitable_character_checks(world):
    """Get list of recruitable character locations.

    Args:
        world (randomizer.logic.main.GameWorld):

    Returns:
        list[ItemLocation]: List of recruitable character location objects..
    """
    return [
        MushroomWayCharacter(world),
        ForestMazeCharacter(world),
        MolevilleMinesCharacter(world),
        MarrymoreCharacter(world)
    ]

class ShuffleLocationSelector(enum.Enum):
    """Enumeration for enabling and disabling locations"""
    StarterCharacter1 = enum.Value("Starter character 1")
    StarterCharacter2 = enum.Value("Starter character 2")
    StarterCharacter3 = enum.Value("Starter character 3")
    StarterCharacter4 = enum.Value("Starter character 4")
    StarterCharacter5 = enum.Value("Starter character 5")
    MariosPadBed = enum.Value("Mushroom Kingdom eastern guard rescue (invasion)")
    MariosPadStarter1 = enum.Value("Starter item 1")
    MariosPadStarter2 = enum.Value("Starter item 2")
    MariosPadStarter3 = enum.Value("Starter item 3")
    MariosPadStarter4 = enum.Value("Starter item 4")
    MushroomWay1 = enum.Value("Mushroom Way first chest")
    MushroomWay2 = enum.Value("Mushroom Way second chest")
    MushroomWay3 = enum.Value("Mushroom Way flower jump left chest")
    MushroomWay4 = enum.Value("Mushroom Way second room right chest")
    ToadRescue1 = enum.Value("Mushroom Way first Toad reward")
    ToadRescue2 = enum.Value("Mushroom Way second Toad reward")
    HammerBrosReward = enum.Value("Mushroom Way boss reward")
    MushroomWayCharacter = enum.Value("Mushroom Way character join")
    MushroomWayStarPiece = enum.Value("Mushroom Way boss star piece")
    MushroomKingdomHallway = enum.Value("Mushroom Kingdom castle main hallway chest")
    MushroomKingdomVault1 = enum.Value("Mushroom Kingdom vault left chest")
    MushroomKingdomVault2 = enum.Value("Mushroom Kingdom vault right chest")
    MushroomKingdomVault3 = enum.Value("Mushroom Kingdom vault middle chest")
    InvasionVault1 = enum.Value("Mushroom Kingdom vault left chest (invasion)")
    InvasionVault2 = enum.Value("Mushroom Kingdom vault right chest (invasion)")
    InvasionVault3 = enum.Value("Mushroom Kingdom vault middle chest (invasion)")
    InvasionEasternGuard = enum.Value("Mushroom Kingdom eastern guard rescue (invasion)")
    WalletGuy1 = enum.Value("Wallet reward 1")
    WalletGuy2 = enum.Value("Wallet reward 2")
    MushroomKingdomStore = enum.Value("Mushroom Kingdom shop free item")
    MushroomKingdomStoreExchange = enum.Value("Mushroom Kingdom shop Rare Frog Coin exchange")
    MushroomKingdomStoreBasement1 = enum.Value("Mushroom Kingdom shop basement left chest")
    MushroomKingdomStoreBasement2 = enum.Value("Mushroom Kingdom shop basement right chest")
    PeachSurprise = enum.Value("Mushroom Kingdom Toadstool's room chair item")
    InvasionToadRescue = enum.Value("Mushroom Kingdom Toadstool's room toad rescue item (invasion)")
    InvasionFamily = enum.Value("Mushroom Kingdom invasion family rescue")
    InvasionGuestRoom = enum.Value("Mushroom Kingdom invasion guest room")
    InvasionStarPiece = enum.Value("Mushroom Kingdom invasion boss star piece")
    MushroomKingdomInn = enum.Value("Mushroom Kingdom gameboy kid")
    BanditsWay1 = enum.Value("Bandit's Way flower chest")
    BanditsWayCoin1 = enum.Value("Bandit's Way 1st coin")
    BanditsWayCoin2 = enum.Value("Bandit's Way 2nd coin")
    BanditsWayCoin3 = enum.Value("Bandit's Way 3rd coin")
    BanditsWay2 = enum.Value("Bandit's Way long room chest")
    BanditsWayStarChest = enum.Value("Bandit's Way star chest")
    BanditsWayDogJump = enum.Value("Bandit's Way dog jump chest")
    BanditsWayCroco = enum.Value("Bandit's Way Croco chase chest")
    Croco1Reward = enum.Value("Bandit's Way boss reward 1")
    Croco1Reward2 = enum.Value("Bandit's Way boss reward 2")
    BanditsWayStarPiece = enum.Value("Bandit's Way boss star piece")
    KeroSewersPandoriteRoom = enum.Value("Kero Sewers stairway room left chest")
    PandoriteChest = enum.Value("Kero Sewers stairway room right chest")
    PandoriteReward1 = enum.Value("Mimic #1 first reward")
    PandoriteReward2 = enum.Value("Mimic #1 reload reward")
    PandoriteBoss = enum.Value("Mimic #1 star piece")
    KeroSewersStarChest = enum.Value("Kero Sewers four rat room chest")
    KeroSewersBeforeBelomeLower = enum.Value("Kero Sewers before boss lower chest")
    KeroSewersBeforeBelomeUpper1 = enum.Value("Kero Sewers before boss upper chest, before Land's End")
    KeroSewersBeforeBelomeUpper2 = enum.Value("Kero Sewers before boss upper chest, after Land's End")
    KeroSewersBoss = enum.Value("Kero Sewers boss star piece")
    MidasRiverFirstTime = enum.Value("Midas River first play reward")
    MidasRiverBottomLeftCave = enum.Value("Midas River bottom left tunnel freestanding frog coin")
    MidasRiverBottomRightCave = enum.Value("Midas River bottom right tunnel freestanding flower")
    CricketPieReward = enum.Value("Tadpole Pond Cricket Pie exchange")
    CricketJamReward = enum.Value("Tadpole Pond Cricket Jam exchange")
    MelodyBay1 = enum.Value("Melody Bay song 1 reward")
    MelodyBay2 = enum.Value("Melody Bay song 2 reward")
    MelodyBay3 = enum.Value("Melody Bay song 3 reward")
    RoseWayPlatform = enum.Value("Rose Way swinging Shy Guy chest")
    RoseWayFlower = enum.Value("Rose Way freestanding flower")
    RoseWayMushroom = enum.Value("Rose Way freestanding mushroom")
    RoseWayCoin1 = enum.Value("Rose Way freestanding coin 1")
    RoseWayCoin2 = enum.Value("Rose Way freestanding coin 2")
    RoseWayCoin3 = enum.Value("Rose Way freestanding coin 3")
    RoseWayCoin4 = enum.Value("Rose Way freestanding coin 4")
    RoseWayCoin5 = enum.Value("Rose Way freestanding coin 5")
    RoseWayFiveChests1 = enum.Value("Rose Way five-chest area top middle chest")
    RoseWayFiveChests2 = enum.Value("Rose Way five-chest area bottom left chest")
    RoseWayFiveChests3 = enum.Value("Rose Way five-chest top right chest")
    RoseWayFiveChests4 = enum.Value("Rose Way five-chest top left chest")
    RoseWayFiveChests5 = enum.Value("Rose Way five-chest bottom right chest")
    RoseTownFlag = enum.Value("Rose Town behind sign")
    RoseTownStore1 = enum.Value("Rose Town shop right chest")
    RoseTownStore2 = enum.Value("Rose Town shop left chest")
    GardenerCloud1 = enum.Value("Rose Town gardener right chest")
    GardenerCloud2 = enum.Value("Rose Town gardener left chest")
    RoseTownToad = enum.Value("Rose Town Inn Toad gift")
    Gaz = enum.Value("Rose Town (unoccupied) Gaz gift")
    RoseTownTreasureHouse1 = enum.Value("Rose Town upper house left chest")
    RoseTownTreasureHouse2 = enum.Value("Rose Town upper house right chest")
    RoseTownTreasureHouseMazeReward = enum.Value("Rose Town upper house Maze Secret prize")
    RoseTownTreasureHouse3 = enum.Value("Rose Town upper house top floor chest")
    ForestMaze1 = enum.Value("Forest Maze 1st room chest")
    ForestMaze2 = enum.Value("Forest Maze first chest after underground")
    ForestMazeUnderground1 = enum.Value("Forest Maze wiggler chest")
    ForestMazeUnderground2 = enum.Value("Forest Maze bottom right stump chest")
    ForestMazeUnderground3 = enum.Value("Forest Maze middle left stump chest")
    ForestMazeRedEssence = enum.Value("Forest Maze before maze chest")
    ForestMazeSecret1 = enum.Value("Forest Maze secret top right chest")
    ForestMazeSecret2 = enum.Value("Forest Maze secret bottom right chest")
    ForestMazeSecret3 = enum.Value("Forest Maze secret top middle chest")
    ForestMazeSecret4 = enum.Value("Forest Maze secret bottom middle chest")
    ForestMazeSecret5 = enum.Value("Forest Maze secret left chest")
    ForestMazeCharacter = enum.Value("Forest Maze character recruit")
    ForestMazeBoss = enum.Value("Forest Maze boss star piece")
    PipeVaultSlide1 = enum.Value("Pipe Vault slide room back chest")
    PipeVaultSlide2 = enum.Value("Pipe Vault slide room middle chest")
    PipeVaultSlide3 = enum.Value("Pipe Vault slide room front chest")
    PipeVaultSlideCoin1 = enum.Value("Pipe Vault slide room freestanding coin 1")
    PipeVaultSlideCoin2 = enum.Value("Pipe Vault slide room freestanding coin 2")
    PipeVaultSlideCoin3 = enum.Value("Pipe Vault slide room freestanding coin 3")
    PipeVaultSlideCoin4 = enum.Value("Pipe Vault slide room freestanding coin 4")
    PipeVaultSlideCoin5 = enum.Value("Pipe Vault slide room freestanding coin 5")
    PipeVaultSlideFrogCoin = enum.Value("Pipe Vault slide room freestanding frog coin")
    PipeVaultNippers1 = enum.Value("Pipe Vault nipper room first chest")
    PipeVaultNippers2 = enum.Value("Pipe Vault nipper room second chest")
    GoombaThumping1 = enum.Value("Pipe Vault Goomba Thumpin first prize")
    GoombaThumping2 = enum.Value("Pipe Vault Goomba Thumpin second prize")
    YosterIsleEntrance = enum.Value("Yo'ster Isle entrance chest")
    YosterIsleRaceReward1 = enum.Value("Yo'ster Isle first race prize item 1")
    YosterIsleRaceReward2 = enum.Value("Yo'ster Isle invisible GOAL item")
    YosterIsleRaceReward3 = enum.Value("Yo'ster Isle first race prize item 2")
    YosterIsleFlag = enum.Value("Yo'ster Isle first race prize item 3")
    BucketGirl = enum.Value("Moleville bucket girl")
    TreasureSeller1 = enum.Value("Moleville first treasure shop item")
    TreasureSeller2 = enum.Value("Moleville second treasure shop item")
    TreasureSeller3 = enum.Value("Moleville third treasure shop item")
    FireworksShop = enum.Value("Moleville Mines two-level traintrack room chest")
    MolevilleMinesShyGuy = enum.Value("Moleville Mines shy guy cart")
    MolevilleMinesCoins = enum.Value("Moleville Mines near final train tracks chest")
    MolevilleMinesPunchinello1 = enum.Value("Moleville Mines before boss left chest")
    MolevilleMinesPunchinello2 = enum.Value("Moleville Mines before boss upper chest")
    MolevilleMinesBoss2 = enum.Value("Moleville Mines final boss star piece")
    MolevilleMinesCharacter = enum.Value("Moleville Mines character recruit")
    CrocoFlunkie1 = enum.Value("Moleville Mines trampoline bandit")
    CrocoFlunkie2 = enum.Value("Moleville Mines left bandit")
    CrocoFlunkie3 = enum.Value("Moleville Mines right bandit")
    Croco2Item = enum.Value("Moleville Mines first boss item")
    MolevilleMinesBoss1 = enum.Value("Moleville Mines first boss star piece")
    BoosterPass1 = enum.Value("Booster Pass main area left chest")
    BoosterPass2 = enum.Value("Booster Pass main area right chest")
    BoosterPassBush = enum.Value("Booster Pass main area bush check")
    BoosterPassFlower = enum.Value("Booster Pass freestanding flower")
    BoosterPassSecret1 = enum.Value("Booster Pass secret middle chest")
    BoosterPassSecret2 = enum.Value("Booster Pass secret right chest")
    BoosterPassSecret3 = enum.Value("Booster Pass secret left chest")
    BoosterTowerSpookum = enum.Value("Booster Tower first stairway chest")
    BoosterTowerThwomp = enum.Value("Booster Tower upper thwomp room chest")
    BoosterTowerKnifeGuy = enum.Value("Booster Tower Knife Guy reward")
    BoosterTowerRoomKey = enum.Value("Booster Tower checkerboard room item")
    BoosterTowerFrogCoin1 = enum.Value("Booster Tower checkerboard room freestanding frog coin 1")
    BoosterTowerFrogCoin2 = enum.Value("Booster Tower checkerboard room freestanding frog coin 2")
    BoosterTowerFrogCoin3 = enum.Value("Booster Tower checkerboard room freestanding frog coin 3")
    BoosterTowerFrogCoin4 = enum.Value("Booster Tower checkerboard room freestanding frog coin 4")
    BoosterTowerCoin1 = enum.Value("Booster Tower checkerboard room freestanding coin 1")
    BoosterTowerCoin2 = enum.Value("Booster Tower checkerboard room freestanding coin 2")
    BoosterTowerCoin3 = enum.Value("Booster Tower checkerboard room freestanding coin 3")
    BoosterTowerCoin4 = enum.Value("Booster Tower checkerboard room freestanding coin 4")
    BoosterTowerCoin5 = enum.Value("Booster Tower checkerboard room freestanding coin 5")
    BoosterTowerCoin6 = enum.Value("Booster Tower checkerboard room freestanding coin 6")
    BoosterTowerCoin7 = enum.Value("Booster Tower checkerboard room freestanding coin 7")
    BoosterTowerCoin8 = enum.Value("Booster Tower checkerboard room freestanding coin 8")
    BoosterTowerCoin9 = enum.Value("Booster Tower checkerboard room freestanding coin 9")
    BoosterTowerMasher = enum.Value("Booster Tower Masher chest")
    BoosterTowerParachute = enum.Value("Booster Tower parachute room chest")
    BoosterTowerParachuteCrevice = enum.Value("Booster Tower parachute room stair crevice")
    BoosterTowerZoomShoes = enum.Value("Booster Tower Room Key chest")
    BoosterTowerTop1 = enum.Value("Booster Tower top floor lower chest")
    BoosterTowerTop2 = enum.Value("Booster Tower top floor upper chest")
    BoosterTowerTop3 = enum.Value("Booster Tower top floor corner chest")
    BoosterTowerRailway = enum.Value("Booster Tower railway room")
    BoosterTowerPortraits = enum.Value("Booster Tower portrait prize")
    BoosterTowerChomp = enum.Value("Booster Tower Elder Key room")
    BoosterTowerCurtainGame = enum.Value("Booster Tower curtain prize")
    BoosterTowerStarPiece1 = enum.Value("Booster Tower curtain room boss star piece")
    BoosterTowerStarPiece2 = enum.Value("Booster Tower balcony boss star piece")
    MarrymorePrize1 = enum.Value("Marrymore Suite total stays prize 1")
    MarrymorePrize2 = enum.Value("Marrymore Suite total stays prize 2")
    MarrymorePrize3 = enum.Value("Marrymore Suite total stays prize 3")
    MarrymorePrize4 = enum.Value("Marrymore Suite total stays prize 4")
    MarrymorePrize5 = enum.Value("Marrymore Suite total stays prize 5")
    MarrymorePrize6 = enum.Value("Marrymore Suite total stays prize 6")
    MarrymoreInn = enum.Value("Marrymore Inn regular room chest")
    MarrymoreStarPiece = enum.Value("Marrymore boss star piece")
    MarrymoreCharacter = enum.Value("Marrymore character join")
    StarHillStarPiece1 = enum.Value("Star Hill freestanding star piece")
    SeasideTownBoss = enum.Value("Seaside Town boss star piece")
    SeasideTownBossPrize = enum.Value("Seaside Town boss prize")
    SeasideTownRescue = enum.Value("Seaside Town shed rescue")
    SeaStarChest = enum.Value("Sea starslap room chest")
    SeaSaveRoom1 = enum.Value("Sea save room back chest")
    SeaSaveRoom2 = enum.Value("Sea save room middle chest")
    SeaSaveRoom3 = enum.Value("Sea save room front chest")
    SeaWhirlpoolChest = enum.Value("Sea whirlpool room chest")
    SunkenShipRatStairs = enum.Value("Sunken Ship first stairway chest")
    SunkenShipRatStairsFlower = enum.Value("Sunken Ship first stairway freestanding flower")
    SunkenShipShop = enum.Value("Sunken Ship shop area chest")
    SunkenShipCoins1 = enum.Value("Sunken Ship outside clone room left chest")
    SunkenShipCoins2 = enum.Value("Sunken Ship outside clone room right chest")
    SunkenShipCloneRoom = enum.Value("Sunken Ship clone room chest")
    SunkenShipFrogCoinRoom = enum.Value("Sunken Ship hidden box room chest")
    SunkenShipHidonMushroom = enum.Value("Sunken Ship Hidon's room left chest")
    SunkenShipHidonChest = enum.Value("Sunken Ship Hidon's room right chest")
    HidonReward1 = enum.Value("Mimic #2 first reward")
    HidonReward2 = enum.Value("Mimic #2 reload reward")
    HidonBoss = enum.Value("Mimic #2 star piece")
    SunkenShipUnderwaterFrogCoin1 = enum.Value("Sunken Ship underwater freestanding frog coin 1")
    SunkenShipUnderwaterFrogCoin2 = enum.Value("Sunken Ship underwater freestanding frog coin 2")
    SunkenShipUnderwaterFrogCoin3 = enum.Value("Sunken Ship underwater freestanding frog coin 3")
    SunkenShipUnderwaterFrogCoin4 = enum.Value("Sunken Ship underwater freestanding frog coin 4")
    SunkenShipSafetyRing = enum.Value("Sunken Ship hidden underwater room chest")
    SunkenShipBandanaReds = enum.Value("Sunken Ship near final boss chest")
    SunkenShipBlooberRoom = enum.Value("Sunken Ship large pool freestanding frog coin")
    SunkenShipTrampolinePuzzle = enum.Value("Sunken Ship trampoline puzzle prize")
    SunkenShipTroopaPuzzle = enum.Value("Sunken Ship troopa cannonball prize")
    SunkenShip3DMaze = enum.Value("Sunken Ship 3D maze prize")
    SunkenShipCoinSnake = enum.Value("Sunken Ship coin snake puzzle prize")
    SunkenShipCannonballPuzzle = enum.Value("Sunken Ship cannonball puzzle prize")
    SunkenShipBarrelPuzzle = enum.Value("Sunken Ship barrel switch prize")
    SunkenShipMidboss = enum.Value("Sunken Ship password boss star piece")
    SunkenShipBoss = enum.Value("Sunken Ship final boss star piece")
    LandsEndRedEssence = enum.Value("Land's End first chest")
    LandsEndChowPit1 = enum.Value("Land's End chow pit left chest")
    LandsEndChowPit2 = enum.Value("Land's End chow pit right chest")
    LandsEndBeeRoom = enum.Value("Land's End bee room chest")
    LandsEndSecret1 = enum.Value("Land's End grotto first chest")
    LandsEndSecret2 = enum.Value("Land's End grotto corner chest")
    LandsEndShyAway = enum.Value("Land's End grotto near sewer chest")
    LandsEndStarChest1 = enum.Value("Land's End whirlpool 1st underground chest")
    LandsEndStarChest2 = enum.Value("Land's End 1st purchase chest")
    LandsEndStarChest3 = enum.Value("Land's End 2nd purchase chest")
    TroopaClimb = enum.Value("Land's End Troopa Climb sub-12 second prize")
    LandsEndStarPiece1 = enum.Value("Land's End/Belome Temple cloud star piece")
    BelomeTempleFortuneTeller = enum.Value("Belome Temple first fortune-telling room chest")
    BelomeTempleFortune1 = enum.Value("Belome Temple left-middle-right fortune chest")
    BelomeTempleFortune2 = enum.Value("Belome Temple left-right-middle fortune chest")
    BelomeTempleFortune3 = enum.Value("Belome Temple right-left-middle fortune chest")
    BelomeTempleFortune4 = enum.Value("Belome Temple right-middle-left fortune chest")
    BelomeTempleAfterFortune1 = enum.Value("Belome Temple after fortune area right chest")
    BelomeTempleAfterFortune2 = enum.Value("Belome Temple after fortune area lower left chest")
    BelomeTempleAfterFortune3 = enum.Value("Belome Temple after fortune area middle chest")
    BelomeTempleAfterFortune4 = enum.Value("Belome Temple after fortune area upper left chest")
    BelomeTempleTreasureFlower1 = enum.Value("Belome Temple vault flower 1")
    BelomeTempleTreasureFlower2 = enum.Value("Belome Temple vault flower 2")
    BelomeTempleTreasureFlower3 = enum.Value("Belome Temple vault flower 3")
    BelomeTempleTreasureFlower4 = enum.Value("Belome Temple vault flower 4")
    BelomeTempleTreasureFrogCoin1 = enum.Value("Belome Temple vault frog coin 1")
    BelomeTempleTreasureFrogCoin2 = enum.Value("Belome Temple vault frog coin 2")
    BelomeTempleTreasureFrogCoin3 = enum.Value("Belome Temple vault frog coin 3")
    BelomeTempleTreasureFrogCoin4 = enum.Value("Belome Temple vault frog coin 4")
    BelomeTempleTreasureFrogCoin5 = enum.Value("Belome Temple vault frog coin 5")
    BelomeTempleTreasureFrogCoin6 = enum.Value("Belome Temple vault frog coin 6")
    BelomeTempleTreasureFrogCoin7 = enum.Value("Belome Temple vault frog coin 7")
    BelomeTempleTreasureFrogCoin8 = enum.Value("Belome Temple vault frog coin 8")
    BelomeTempleTreasure1 = enum.Value("Belome Temple vault middle item bag")
    BelomeTempleTreasure2 = enum.Value("Belome Temple vault left item bag")
    BelomeTempleTreasure3 = enum.Value("Belome Temple vault right item bag")
    BelomeTempleBoss = enum.Value("Belome Temple boss star piece")
    MonstroTownEntrance = enum.Value("Monstro Town entrance chest")
    MonstroTownThwomp = enum.Value("Monstro Town thwomp key")
    JinxDojoReward = enum.Value("Monstro Town dojo prize")
    DojoBoss1 = enum.Value("Monstro Town dojo first fight star piece")
    DojoBoss2 = enum.Value("Monstro Town dojo second fight star piece")
    DojoBoss3 = enum.Value("Monstro Town dojo third fight star piece")
    DojoBoss4 = enum.Value("Monstro Town dojo fourth fight star piece")
    CulexBoss = enum.Value("Monstro Town sealed door star piece")
    CulexReward = enum.Value("Monstro Town sealed door prize")
    SuperJumps30 = enum.Value("Monstro Town Super Jump first prize")
    SuperJumps100 = enum.Value("Monstro Town Super Jump second prize")
    ThreeMustyFears = enum.Value("Monstro Town flag exchange prize")
    BeanValley1 = enum.Value("Bean Valley south upper level chest")
    BeanValley2 = enum.Value("Bean Valley north upper level chest")
    BeanValleyLeftPiranhaPipe = enum.Value("Bean Valley left piranha pipe chest")
    BeanValleyBottomLeftPiranhaPipe = enum.Value("Bean Valley bottom left piranha pipe chest")
    BeanValleyBottomRightPiranhaPipeUpper = enum.Value("Bean Valley bottom right piranha pipe upper chest")
    BeanValleyBottomRightPiranhaPipeLower = enum.Value("Bean Valley bottom right piranha pipe lower chest")
    BeanValleyBoxBoyRoom1 = enum.Value("Bean Valley right piranha pipe left chest")
    BoxBoyBoss = enum.Value("Mimic #2 star piece")
    BeanValleyBoxBoyRoom2 = enum.Value("Bean Valley right piranha pipe right chest")
    BeanValleyBoxBoyRoomHidden = enum.Value("Bean Valley right piranha pipe hidden stairway item")
    BeanValleyPiranhaPlants = enum.Value("Bean Valley chest above Box Boy's room")
    BeanValleyMegasmilaxRoom = enum.Value("Bean Valley boss star piece")
    BeanValleyBeanstalk = enum.Value("Bean Valley clouds solo vine chest")
    BeanValleyBeanstalkFrogCoin = enum.Value("Bean Valley middle vine room freestanding frog coin")
    BeanValleyBeanstalkCoin1 = enum.Value("Bean Valley middle vine room lowest freestanding coin")
    BeanValleyBeanstalkCoin2 = enum.Value("Bean Valley middle vine room middle freestanding coin")
    BeanValleyBeanstalkCoin3 = enum.Value("Bean Valley middle vine room highest freestanding coin")
    BeanValleyEastBeanstalkCoin1 = enum.Value("Bean Valley east vine room lowest freestanding coin")
    BeanValleyEastBeanstalkCoin2 = enum.Value("Bean Valley east vine room lowest freestanding coin")
    BeanValleyEastBeanstalkCoin3 = enum.Value("Bean Valley east vine room middle freestanding coin")
    BeanValleyEastBeanstalkCoin4 = enum.Value("Bean Valley east vine room higher freestanding coin")
    BeanValleyEastBeanstalkCoin5 = enum.Value("Bean Valley east vine room highest freestanding coin")
    BeanValleyWestBeanstalkCoin1 = enum.Value("Bean Valley west vine room lower freestanding coin")
    BeanValleyWestBeanstalkCoin2 = enum.Value("Bean Valley west vine room middle freestanding coin")
    BeanValleyWestBeanstalkCoin3 = enum.Value("Bean Valley west vine room upper freestanding coin")
    BeanValleyWestBeanstalkFrogCoin = enum.Value("Bean Valley west vine room freestanding frog coin")
    BeanValleyCloud1 = enum.Value("Bean Valley clouds upper left chest")
    BeanValleyCloud2 = enum.Value("Bean Valley clouds upper right chest")
    BeanValleyFall1 = enum.Value("Bean Valley clouds lower left chest")
    BeanValleyFall2 = enum.Value("Bean Valley clouds lower right chest")
    BeanValleyFirstVineRoomFrogCoin = enum.Value("Bean Valley lowest vine room freestanding frog coin")
    BeanValleyFirstVineRoomMiddleCoin = enum.Value("Bean Valley lowest vine room middle freestanding coin")
    BeanValleyFirstVineRoomUpperCoin = enum.Value("Bean Valley lowest vine room upper freestanding coin")
    BeanValleyFirstVineRoomLowerCoin = enum.Value("Bean Valley lowest vine room lower freestanding coin")
    CasinoGrateGuyPrize = enum.Value("Grate Guy's Casino LOTW prize")
    NimbusLandShop = enum.Value("Nimbus Land shop chest")
    NimbusLandInn = enum.Value("Nimbus Land dream cushion 1st item")
    NimbusLandInn2 = enum.Value("Nimbus Land dream cushion 2nd item")
    NimbusCastleBeforeBirdetta1 = enum.Value("Nimbus Castle (occupied) 5-door room chest")
    NimbusCastleBeforeBirdetta2 = enum.Value("Nimbus Castle west two-level room chest")
    NimbusCastleBirdetta = enum.Value("Nimbus Castle giant egg prize")
    NimbusCastleStarPiece2 = enum.Value("Nimbus Land giant egg boss star piece")
    NimbusCastleOutOfBounds1 = enum.Value("Nimbus Castle west stairway room left chest")
    NimbusCastleOutOfBounds2 = enum.Value("Nimbus Castle west stairway room right chest")
    NimbusCastleSingleGoldBird = enum.Value("Nimbus Castle single gold bird room chest")
    NimbusCastleAfterEgg1 = enum.Value("Nimbus Castle east two-level room lower chest")
    NimbusCastleAfterEgg2 = enum.Value("Nimbus Castle east two-level room upper chest")
    NimbusCastleStarPiece3 = enum.Value("Nimbus Land final boss star piece")
    NimbusCastleStarChest = enum.Value("Nimbus Castle post-throne chest (occupied)")
    NimbusCastleStarAfterValentina = enum.Value("Nimbus Castle post-throne chest (unoccupied)")
    NimbusCastleCornerChestAfterValentina = enum.Value("Nimbus Castle (unoccupied) 5-door room chest")
    NimbusLandRightSide = enum.Value("Nimbus Land post-invasion off-cloud item")
    DodoReward = enum.Value("Nimbus Land Dodo's statue game prize")
    NimbusLandStarPiece1 = enum.Value("Nimbus Land statue keeper boss star piece")
    NimbusLandPrisoners = enum.Value("Nimbus Castle west cellar civilian")
    NimbusLandPrisoners2 = enum.Value("Nimbus Castle west cellar guard")
    NimbusLandSignalRing = enum.Value("Nimbus Land post-invasion upper right house")
    NimbusLandCellar = enum.Value("Nimbus Castle post-invasion north cellar")
    BarrelVolcanoSecret1 = enum.Value("Barrel Volcano secret room left chest")
    BarrelVolcanoSecret2 = enum.Value("Barrel Volcano secret room right chest")
    BarrelVolcanoReverse = enum.Value("Barrel Volcano reverse lava recoil frog coin")
    BarrelVolcanoDonut1 = enum.Value("Barrel Volcano first donut lift room right freestanding frog coin")
    BarrelVolcanoDonut2 = enum.Value("Barrel Volcano first donut lift room left freestanding frog coin")
    BarrelVolcanoLavaPool = enum.Value("Barrel Volcano lava pool freestanding frog coin")
    BarrelVolcanoBeforeStar1 = enum.Value("Barrel Volcano second arrow sign room left chest")
    BarrelVolcanoBeforeStar2 = enum.Value("Barrel Volcano second arrow sign room right chest")
    BarrelVolcanoStarRoom = enum.Value("Barrel Volcano star chest")
    BarrelVolcanoSaveRoom1 = enum.Value("Barrel Volcano save room lower chest")
    BarrelVolcanoSaveRoom2 = enum.Value("Barrel Volcano save room upper chest")
    BarrelVolcanoHinopio = enum.Value("Barrel Volcano Hinopio shop chest")
    BarrelVolcanoBoss1 = enum.Value("Barrel Volcano first boss star piece")
    BarrelVolcanoBoss2 = enum.Value("Barrel Volcano second boss star piece")
    BowsersKeepDarkRoom = enum.Value("Bowser's Keep dark room chest")
    BowsersKeepCrocoShop1 = enum.Value("Bowser's Keep near first shop left chest")
    BowsersKeepCrocoShop2 = enum.Value("Bowser's Keep near first shop right chest")
    BowsersKeepMagikoopa = enum.Value("Bowser's Keep Magikoopa's room chest")
    BowsersKeepBossChester = enum.Value("Bowser's Keep battle door star piece")
    BowsersKeepBoss1 = enum.Value("Bowser's Keep first boss star piece")
    BowsersKeepInvisibleBridge1 = enum.Value("Bowser's Keep 6-door invisble bridge bottom chest")
    BowsersKeepInvisibleBridge2 = enum.Value("Bowser's Keep 6-door invisble bridge right chest")
    BowsersKeepInvisibleBridge3 = enum.Value("Bowser's Keep 6-door invisble bridge left chest")
    BowsersKeepInvisibleBridge4 = enum.Value("Bowser's Keep 6-door invisble bridge top chest")
    BowsersKeepInvisibleBridgeCoin1 = enum.Value("Bowser's Keep 6-door invisble bridge bottom left coin")
    BowsersKeepInvisibleBridgeCoin2 = enum.Value("Bowser's Keep 6-door invisble bridge bottom right coin")
    BowsersKeepInvisibleBridgeCoin3 = enum.Value("Bowser's Keep 6-door invisble bridge top left coin")
    BowsersKeepInvisibleBridgeCoin4 = enum.Value("Bowser's Keep 6-door invisble bridge top right coin")
    BowsersKeepMovingPlatforms1 = enum.Value("Bowser's Keep X-Y platform room left exit chest")
    BowsersKeepMovingPlatforms2 = enum.Value("Bowser's Keep X-Y platform room left entrance chest")
    BowsersKeepMovingPlatforms3 = enum.Value("Bowser's Keep X-Y platform room right entrance chest")
    BowsersKeepMovingPlatforms4 = enum.Value("Bowser's Keep X-Y platform room right exit chest")
    BowsersKeepElevatorPlatforms = enum.Value("Bowser's Keep 6-door elevator platform room chest")
    BowsersKeepCannonballRoom1 = enum.Value("Bowser's Keep cannonball room lower right chest")
    BowsersKeepCannonballRoom2 = enum.Value("Bowser's Keep cannonball room exit chest")
    BowsersKeepCannonballRoom3 = enum.Value("Bowser's Keep cannonball room lower left chest")
    BowsersKeepCannonballRoom4 = enum.Value("Bowser's Keep cannonball room upper right chest")
    BowsersKeepCannonballRoom5 = enum.Value("Bowser's Keep cannonball room upper left chest")
    BowsersKeepCannonballRoomCoin1 = enum.Value("Bowser's Keep cannonball room freestanding coin 1")
    BowsersKeepCannonballRoomCoin2 = enum.Value("Bowser's Keep cannonball room freestanding coin 2")
    BowsersKeepCannonballRoomCoin3 = enum.Value("Bowser's Keep cannonball room freestanding coin 3")
    BowsersKeepCannonballRoomCoin4 = enum.Value("Bowser's Keep cannonball room freestanding coin 4")
    BowsersKeepCannonballRoomCoin5 = enum.Value("Bowser's Keep cannonball room freestanding coin 5")
    BowsersKeepCannonballRoomCoin6 = enum.Value("Bowser's Keep cannonball room freestanding coin 6")
    BowsersKeepCannonballRoomCoin7 = enum.Value("Bowser's Keep cannonball room freestanding coin 7")
    BowsersKeepCannonballRoomCoin8 = enum.Value("Bowser's Keep cannonball room freestanding coin 8")
    BowsersKeepRotatingPlatforms1 = enum.Value("Bowser's Keep rotating platform room entrance chest")
    BowsersKeepRotatingPlatforms2 = enum.Value("Bowser's Keep rotating platform lower left chest")
    BowsersKeepRotatingPlatforms3 = enum.Value("Bowser's Keep rotating platform right chest")
    BowsersKeepRotatingPlatforms4 = enum.Value("Bowser's Keep rotating platform center chest")
    BowsersKeepRotatingPlatforms5 = enum.Value("Bowser's Keep rotating platform upper left chest")
    BowsersKeepRotatingPlatforms6 = enum.Value("Bowser's Keep rotating platform exit chest")
    BowsersKeepDoorReward1 = enum.Value("Bowser's Keep door prize 1")
    BowsersKeepDoorReward2 = enum.Value("Bowser's Keep door prize 2")
    BowsersKeepDoorReward3 = enum.Value("Bowser's Keep door prize 3")
    BowsersKeepDoorReward4 = enum.Value("Bowser's Keep door prize 4")
    BowsersKeepDoorReward5 = enum.Value("Bowser's Keep door prize 5")
    BowsersKeepDoorReward6 = enum.Value("Bowser's Keep door prize 6")
    BowsersKeepBoss2 = enum.Value("Bowser's Keep second boss star piece")
    BowsersKeepBoss3 = enum.Value("Bowser's Keep third boss star piece")
    FactorySaveRoom = enum.Value("Outer Factory early save room chest")
    FactoryBoltPlatforms = enum.Value("Outer Factory bot platform chest")
    FactoryBoss1 = enum.Value("Outer Factory first boss star piece")
    FactoryFallingAxems = enum.Value("Outer Factory falling axem room chest")
    FactoryTreasurePit1 = enum.Value("Outer Factory pit back chest")
    FactoryTreasurePit2 = enum.Value("Outer Factory pit front chest")
    FactoryConveyorPlatforms1 = enum.Value("Outer Factory conveyor room right chest")
    FactoryConveyorPlatforms2 = enum.Value("Outer Factory conveyor room left chest")
    FactoryBehindSnakes1 = enum.Value("Outer Factory room behind machine yarid right chest")
    FactoryBehindSnakes2 = enum.Value("Outer Factory room behind machine yarid left chest")
    FactoryBoss2 = enum.Value("Outer Factory second boss star piece")
    FactoryToadGift = enum.Value("Inner Factory toad gift")
    InnerFactoryBoss1 = enum.Value("Inner Factory first boss star piece")
    InnerFactoryBoss2 = enum.Value("Inner Factory second boss star piece")
    InnerFactoryBoss3 = enum.Value("Inner Factory third boss star piece")
    InnerFactoryBoss4 = enum.Value("Inner Factory fourth boss star piece")
