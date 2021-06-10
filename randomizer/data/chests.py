# Data module for chest data.

import enum
from randomizer.data import items
from randomizer.data.items import ItemUnique
from randomizer.logic.utils import isclass_or_instance
from . import locations
from randomizer.logic import flags
from randomizer.logic.flags import ItemQualities, FireworksOptions, BanditsWayGating, ForestMazeGating, BoosterTowerGating, MarrymoreGating, YaridovichGating, SeaGating, MonstroTownGating, BarrelVolcanoGating, BowsersKeepGating, FactoryGating
from randomizer.data.helpers import ShuffleLocationSelector

# locations inherit world, and therefore settings
# inventory does not
# how to make work with optional gating?

# ******* Chest location classes


class Chest(locations.ItemLocation):
    """Subclass for treasure chest location."""
    access = 1
    shopsanity = False
    coinsanity = False
    manual_70A7 = False
    dialogs_to_replace = []

    def item_allowed(self, item):
        return super().item_allowed(item) and not isclass_or_instance(item, items.InvincibilityStar)




class StarAllowedChest(Chest):
    def item_allowed(self, item):
        return super().item_allowed(item) or isclass_or_instance(item, items.InvincibilityStar)



# ******* NPC reward data classes

class NPCReward(locations.ItemLocation):
    """Subclass for NPC reward location."""
    access = 1
    dialogs_to_replace = []

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
        return super().item_allowed(item) and (item.unique == ItemUnique.Always or item.unique == ItemUnique.BalancedOnly)

    
    def can_access(self, inventory):
        return inventory.has_item(items.BambinoBomb)

class FrogCoinShopItem(NPCReward):
    shopsanity = True
    key = False

    def item_allowed(self, item):
        # update this when shuffle modes integrated
        return super().item_allowed(item) and not item.is_key and (item.is_equipment or item.unique == ItemUnique.Always or item.unique == ItemUnique.BalancedOnly)


# ******* Overworld item classes


class OverworldItem(locations.ItemLocation):
    """Subclass for NPC reward location."""
    access = 1

    coinsanity = True
    npc_ids = None
    dialogs_to_replace = []

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

        return super().item_allowed(item) and not isclass_or_instance(item, (items.Coins, item.FrogCoin))


# ******* Boss star piece classes


class BossStarPiece(locations.ItemLocation):
    """Subclass for boss star piece location."""
    shopsanity = False
    coinsanity = False
    dialogs_to_replace = []
    item = None

    def item_allowed(self, item):
        # Can only be Star Piece, or empty
        return isclass_or_instance(item, item.StarPiece) or item == None

# ******* Character recruitment classes


class CharacterRecruit(locations.ItemLocation):
    """Subclass for character recruit location."""
    shopsanity = False
    coinsanity = False
    dialogs_to_replace = []
    item = None

    def item_allowed(self, item):
        # Can only be character
        return isclass_or_instance(item, item.RecruitedCharacter) or item == None

class CharacterSpotted(locations.ItemLocation):
    """Subclass for character recruit location."""
    shopsanity = False
    coinsanity = False
    dialogs_to_replace = []
    item = None

    def item_allowed(self, item):
        # Can only be corresponding character
        return isclass_or_instance(item, item.SpottedCharacter)


class StarterCharacterRecruit(CharacterRecruit):
    pass


class MidasRiverTunnelItem(OverworldItem):
    pass


class BelomeTempleTreasure(OverworldItem):
    """Subclass for Belome Temple rewards."""

    
    def can_access(self, inventory):
        return inventory.has_item(items.TempleKey)



# ****************************** Actual chest classes

# *** Marios Pad

class StarterCharacter1(StarterCharacterRecruit):
    area = locations.Area.MariosPad
    description = ShuffleLocationSelector.StarterCharacter1
    item = items.MarioRecruit
    event = 192


class StarterCharacter2(StarterCharacterRecruit):
    area = locations.Area.MariosPad
    description = ShuffleLocationSelector.StarterCharacter2
    event = 192


class StarterCharacter3(StarterCharacterRecruit):
    area = locations.Area.MariosPad
    description = ShuffleLocationSelector.StarterCharacter3
    event = 192


class StarterCharacter4(StarterCharacterRecruit):
    area = locations.Area.MariosPad
    description = ShuffleLocationSelector.StarterCharacter4
    event = 192


class StarterCharacter5(StarterCharacterRecruit):
    area = locations.Area.MariosPad
    description = ShuffleLocationSelector.StarterCharacter5
    event = 192


class MariosPadBed(NPCReward):
    description = ShuffleLocationSelector.MariosPadBed
    area = locations.Area.MariosPad
    item = items.DryBonesFlag
    rooms = [189]
    event = 253
    key = True
    
    def item_allowed(self, item):
        if self.world.flags.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)



class MariosPadStarter1(StarterItem):
    description = ShuffleLocationSelector.MariosPadStarter1
    area = locations.Area.MariosPad
    item = items.Mushroom
    rooms = [189]
    event = 252


class MariosPadStarter2(StarterItem):
    description = ShuffleLocationSelector.MariosPadStarter2
    area = locations.Area.MariosPad
    item = items.Mushroom
    rooms = [189]
    event = 251


class MariosPadStarter3(StarterItem):
    description = ShuffleLocationSelector.MariosPadStarter3
    area = locations.Area.MariosPad
    item = items.Mushroom
    rooms = [189]
    event = 250


class MariosPadStarter4(StarterItem):
    description = ShuffleLocationSelector.MariosPadStarter4
    area = locations.Area.MariosPad
    item = items.Mushroom
    rooms = [189]
    event = 249


# *** Mushroom Way

class MushroomWay1(StarAllowedChest):
    description = ShuffleLocationSelector.MushroomWay1
    area = locations.Area.MushroomWay
    item = items.Coins(Chest, 5)
    rooms = [203]
    event = 247


class MushroomWay2(StarAllowedChest):
    description = ShuffleLocationSelector.MushroomWay2
    area = locations.Area.MushroomWay
    item = items.Coins(Chest, 8)
    rooms = [203]
    event = 246


class MushroomWay3(StarAllowedChest):
    description = ShuffleLocationSelector.MushroomWay3
    area = locations.Area.MushroomWay
    item = items.Flower
    rooms = [204]
    event = 247


class MushroomWay4(StarAllowedChest):
    description = ShuffleLocationSelector.MushroomWay4
    area = locations.Area.MushroomWay
    item = items.RecoveryMushroom
    rooms = [204]
    event = 246


class ToadRescue1(NPCReward):
    description = ShuffleLocationSelector.ToadRescue1
    area = locations.Area.MushroomWay
    item = items.HoneySyrup
    missable = True
    rooms = [203]
    event = 253


class ToadRescue2(NPCReward):
    description = ShuffleLocationSelector.ToadRescue2
    area = locations.Area.MushroomWay
    item = items.FlowerTab
    missable = True
    rooms = [204]
    event = 253


class HammerBrosReward(NPCReward):
    description = ShuffleLocationSelector.HammerBrosReward
    area = locations.Area.MushroomWay
    item = items.Hammer
    rooms = [205]
    event = 253


class MushroomWayCharacter(CharacterRecruit):
    area = locations.Area.MushroomWay
    description = ShuffleLocationSelector.MushroomWayCharacter
    item = items.MallowRecruit
    rooms = [205]
    event = 186


class MushroomWayStarPiece(BossStarPiece):
    area = locations.Area.MushroomWay
    description = ShuffleLocationSelector.MushroomWayStarPiece
    rooms = [205]
    event = 167



# *** Mushroom Kingdom

class MushroomKingdomHallway(Chest):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.MushroomKingdomHallway
    item = items.FrogCoin
    rooms = [17, 325]
    npc_ids = [2, 6]
    event = 247


class MushroomKingdomVault1(Chest):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.MushroomKingdomVault1
    rooms = [31]
    npc_ids = [0]
    event = 247
    item = items.Coins10


class MushroomKingdomVault2(Chest):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.MushroomKingdomVault2
    rooms = [31]
    npc_ids = [1]
    event = 246
    item = items.RecoveryMushroom


class MushroomKingdomVault3(Chest):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.MushroomKingdomVault3
    rooms = [31]
    npc_ids = [2]
    event = 245
    item = items.Flower


class InvasionVault1(StarAllowedChest):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.InvasionVault1
    item = items.Coins10
    rooms = [331]
    npc_ids = [0]
    event = 247
    missable = True
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.AlwaysOpen) or world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.FinishMushroomWay):
            self.access = 1

    def can_access(self, inventory):
        return locations.can_access_bandits_way(self.world, inventory)


class InvasionVault2(StarAllowedChest):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.InvasionVault2
    item = items.RecoveryMushroom
    rooms = [331]
    npc_ids = [1]
    event = 246
    missable = True
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.AlwaysOpen) or world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.FinishMushroomWay):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_bandits_way(self.world, inventory)


class InvasionVault3(StarAllowedChest):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.InvasionVault3
    item = items.Flower
    rooms = [331]
    npc_ids = [2]
    event = 245
    missable = True
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.AlwaysOpen) or world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.FinishMushroomWay):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_bandits_way(self.world, inventory)


class InvasionEasternGuard(NPCReward):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.InvasionEasternGuard
    rooms = [190]
    event = 253
    item = items.Coins10
    missable = True
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.AlwaysOpen) or world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.FinishMushroomWay):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_bandits_way(self.world, inventory)


class WalletGuy1(NPCReward):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.WalletGuy1
    rooms = [190, 191]
    event = 252
    item = items.FlowerTab
    missable = True
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_bandits_way(self.world, inventory)


class WalletGuy2(NPCReward):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.WalletGuy2
    rooms = [190, 191]
    event = 251
    item = items.FrogCoin
    missable = True
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_bandits_way(self.world, inventory) and locations.can_access_marrymore(self.world, inventory)


class MushroomKingdomStore(NPCReward):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.MushroomKingdomStore
    rooms = [483, 491]
    event = 253
    item = items.PickMeUp


class MushroomKingdomStoreExchange(NPCReward):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.MushroomKingdomStoreExchange
    rooms = [483, 491]
    event = 252
    item = items.CricketPie
    key = True
    access = 2
    
    def item_allowed(self, item):
        if self.world.flags.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)

    
    def can_access(self, inventory):
        return locations.can_access_bandits_way(self.world, inventory)


class MushroomKingdomStoreBasement1(Chest):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.MushroomKingdomStoreBasement1
    rooms = [492]
    npc_ids = [0]
    event = 247
    item = items.Flower


class MushroomKingdomStoreBasement2(Chest):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.MushroomKingdomStoreBasement2
    rooms = [492]
    npc_ids = [1]
    event = 246
    item = items.Flower


class PeachSurprise(NPCReward):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.PeachSurprise
    item = items.Mushroom
    rooms = [20, 328]
    event = 253


class InvasionToadRescue(NPCReward):
    description = ShuffleLocationSelector.InvasionToadRescue
    item = items.FlowerTab
    missable = True
    rooms = [20, 328]
    event = 252
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_bandits_way(self.world, inventory)


class InvasionFamily(NPCReward):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.InvasionFamily
    rooms = [480, 481]
    script = 253
    item = items.FlowerTab
    missable = True
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_bandits_way(self.world, inventory)


class InvasionGuestRoom(NPCReward):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.InvasionGuestRoom
    rooms = [330]
    script = 253
    item = items.WakeUpPin
    missable = True
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.AlwaysOpen) or world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.FinishMushroomWay):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_bandits_way(self.world, inventory)

class InvasionStarPiece(BossStarPiece):
    description = ShuffleLocationSelector.InvasionStarPiece
    area = locations.Area.MushroomKingdom
    rooms = [326]
    event = 167
    item = items.StarPiece
    
    def can_access(self, inventory):
        return locations.can_access_bandits_way(self.world, inventory)



class MushroomKingdomInn(NPCReward):
    area = locations.Area.MushroomKingdom
    description = ShuffleLocationSelector.MushroomKingdomInn
    rooms = [493]
    event = 253
    item = items.Beetlemania
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_bandits_way(self.world, inventory)


# *** Bandit's Way

class BanditsWay1(StarAllowedChest):
    description = ShuffleLocationSelector.BanditsWay1
    area = locations.Area.BanditsWay
    rooms = [207]
    npc_ids = [9]
    event = 247
    item = items.KerokeroCola
    
    def can_access(self, inventory):
        return locations.can_access_bandits_way(self.world, inventory)


class BanditsWayCoin1(OverworldItem):
    description = ShuffleLocationSelector.BanditsWayCoin1
    area = locations.Area.BanditsWay
    rooms = [207]
    event = 239
    npc_ids = [3]
    item = items.Coins1
    
    def can_access(self, inventory):
        return locations.can_access_bandits_way(self.world, inventory)


class BanditsWayCoin2(OverworldItem):
    description = ShuffleLocationSelector.BanditsWayCoin2
    area = locations.Area.BanditsWay
    rooms = [207]
    event = 240
    npc_ids = [4]
    item = items.Coins1
    
    def can_access(self, inventory):
        return locations.can_access_bandits_way(self.world, inventory)


class BanditsWayCoin3(OverworldItem):
    description = ShuffleLocationSelector.BanditsWayCoin3
    area = locations.Area.BanditsWay
    rooms = [207]
    event = 241
    npc_ids = [5]
    item = items.Coins1
    
    def can_access(self, inventory):
        return locations.can_access_bandits_way(self.world, inventory)


class BanditsWay2(StarAllowedChest):
    description = ShuffleLocationSelector.BanditsWay2
    area = locations.Area.BanditsWay
    rooms = [77]
    npc_ids = [0]
    event = 253
    item = items.RecoveryMushroom
    
    def can_access(self, inventory):
        return locations.can_access_bandits_way(self.world, inventory)


class BanditsWayStarChest(StarAllowedChest):
    description = ShuffleLocationSelector.BanditsWayStarChest
    area = locations.Area.BanditsWay
    rooms = [78]
    npc_ids = [0]
    event = 253
    item = items.BanditsWayStar
    
    def can_access(self, inventory):
        return locations.can_access_bandits_way(self.world, inventory)


class BanditsWayDogJump(StarAllowedChest):
    description = ShuffleLocationSelector.BanditsWayDogJump
    rooms = [78]
    npc_ids = [1]
    event = 252
    area = locations.Area.BanditsWay
    item = items.Flower
    
    def can_access(self, inventory):
        return locations.can_access_bandits_way(self.world, inventory)


class BanditsWayCroco(StarAllowedChest):
    description = ShuffleLocationSelector.BanditsWayCroco
    area = locations.Area.BanditsWay
    rooms = [206]
    npc_ids = [0]
    event = 247
    item = items.RecoveryMushroom
    
    def can_access(self, inventory):
        return locations.can_access_bandits_way(self.world, inventory)


class Croco1Reward(NPCReward):
    description = ShuffleLocationSelector.Croco1Reward
    area = locations.Area.BanditsWay
    rooms = [206]
    event = 253
    item = items.RareFrogCoin
    key = True
    
    def item_allowed(self, item):
        if self.world.flags.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)

    
    def can_access(self, inventory):
        return locations.can_access_bandits_way(self.world, inventory)


class Croco1Reward2(NPCReward):
    description = ShuffleLocationSelector.Croco1Reward2
    area = locations.Area.BanditsWay
    rooms = [206]
    event = 252
    item = items.Wallet
    
    def can_access(self, inventory):
        return locations.can_access_bandits_way(self.world, inventory)

class BanditsWayStarPiece(BossStarPiece):
    area = locations.Area.BanditsWay
    description = ShuffleLocationSelector.BanditsWayStarPiece
    rooms = [206]
    event = 167
    
    def can_access(self, inventory):
        return locations.can_access_bandits_way(self.world, inventory)


# *** Kero Sewers


class KeroSewersPandoriteRoom(StarAllowedChest):
    description = ShuffleLocationSelector.KeroSewersPandoriteRoom
    area = locations.Area.KeroSewers
    item = items.Flower
    rooms = [60]
    npc_ids = [0]
    event = 247


class PandoriteChest(StarAllowedChest):
    description = ShuffleLocationSelector.PandoriteChest
    area = locations.Area.KeroSewers
    item = items.PandoriteFight
    rooms = [60]
    npc_ids = [1]
    event = 246


class PandoriteReward1(NPCReward):
    description = ShuffleLocationSelector.PandoriteReward1
    item = items.TrueformPin
    rooms = [512]
    event = 253
    access = 2
    
    def can_access(self, inventory):
        return inventory.has_item(items.PandoriteFight)


class PandoriteReward2(Chest):
    description = ShuffleLocationSelector.PandoriteReward2
    item = items.Coins(Chest, 50)
    rooms = [512]
    manual_70A7 = True
    event = 245
    access = 2
    
    def can_access(self, inventory):
        return inventory.has_item(items.PandoriteFight)

class PandoriteBoss(BossStarPiece):
    description = ShuffleLocationSelector.PandoriteBoss
    rooms = [512]
    event = 167
    
    
    def can_access(self, inventory):
        return inventory.has_item(items.PandoriteFight)

class KeroSewersStarChest(StarAllowedChest):
    description = ShuffleLocationSelector.KeroSewersStarChest
    area = locations.Area.KeroSewers
    item = items.KeroSewersStar
    rooms = [59]
    npc_ids = [0]
    event = 247


class KeroSewersBeforeBelomeLower(StarAllowedChest):
    description = ShuffleLocationSelector.KeroSewersBeforeBelomeLower
    area = locations.Area.KeroSewers
    item = items.RecoveryMushroom
    rooms = [301]
    npc_ids = [0]
    event = 247


class KeroSewersBeforeBelomeUpper1(StarAllowedChest):
    description = ShuffleLocationSelector.KeroSewersBeforeBelomeUpper1
    area = locations.Area.KeroSewers
    item = items.Flower
    npc_ids = [1]
    rooms = [301]
    event = 246
    missable = True


class KeroSewersBeforeBelomeUpper2(StarAllowedChest):
    description = ShuffleLocationSelector.KeroSewersBeforeBelomeUpper2
    area = locations.Area.KeroSewers
    item = items.CricketJam
    rooms = [301]
    event = 245
    manual_70A7 = True
    key = True
    
    def item_allowed(self, item):
        if self.world.flags.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)



class KeroSewersBoss(BossStarPiece):
    description = ShuffleLocationSelector.KeroSewersBoss
    area = locations.Area.KeroSewers
    rooms = [302]
    event = 167


# *** Midas River

class MidasRiverFirstTime(NPCReward):
    description = ShuffleLocationSelector.MidasRiverFirstTime
    area = locations.Area.MidasRiver
    item = items.NokNokShell
    rooms = [67]
    event = 253


class MidasRiverBottomLeftCave(MidasRiverTunnelItem):
    description = ShuffleLocationSelector.MidasRiverBottomLeftCave
    area = locations.Area.MidasRiver
    item = items.FrogCoin
    rooms = [72]
    event = 241
    npc_ids = [1]


class MidasRiverBottomRightCave(MidasRiverTunnelItem):
    description = ShuffleLocationSelector.MidasRiverBottomRightCave
    area = locations.Area.MidasRiver
    item = items.Flower
    rooms = [73]
    event = 241
    npc_ids = [4]

# *** Tadpole Pond


class CricketPieReward(NPCReward):
    description = ShuffleLocationSelector.CricketPieReward
    area = locations.Area.TadpolePond
    item = items.FroggieStick
    rooms = [75]
    event = 253
    special_equip = True
    
    def can_access(self, inventory):
        return inventory.has_item(items.CricketPie)


class CricketJamReward(NPCReward):
    description = ShuffleLocationSelector.CricketJamReward
    area = locations.Area.TadpolePond
    rooms = [75]
    event = 252
    item = items.MultiFrogCoin(NPCReward, 10)

    
    def can_access(self, inventory):
        return inventory.has_item(items.CricketJam)


class MelodyBay1(NPCReward):
    description = ShuffleLocationSelector.MelodyBay1
    area = locations.Area.TadpolePond
    item = items.ProgressiveCard
    rooms = [74]
    event = 253
    key = True
    
    def item_allowed(self, item):
        if self.world.flags.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)



class MelodyBay2(NPCReward):
    description = ShuffleLocationSelector.MelodyBay2
    area = locations.Area.TadpolePond
    item = items.ProgressiveCard
    rooms = [74]
    event = 252
    key = True
    access = 2
    
    def item_allowed(self, item):
        if self.world.flags.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)

    def can_access(self, inventory):
        return inventory.has_item(items.BambinoBomb)


class MelodyBay3(NPCReward):
    description = ShuffleLocationSelector.MelodyBay3
    area = locations.Area.TadpolePond
    item = items.ProgressiveCard
    rooms = [74]
    event = 251
    key = True
    access = 2
    
    def item_allowed(self, item):
        if self.world.flags.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)

    def can_access(self, inventory):
        return inventory.has_item(items.BambinoBomb)

# *** Rose Way


class RoseWayPlatform(StarAllowedChest):
    description = ShuffleLocationSelector.RoseWayPlatform
    area = locations.Area.RoseWay
    rooms = [80]
    npc_ids = [0]
    event = 247
    item = items.FrogCoin


class RoseWayFlower(OverworldItem):
    description = ShuffleLocationSelector.RoseWayFlower
    area = locations.Area.RoseWay
    item = items.Flower
    rooms = [79]
    event = 241
    npc_ids = [7]


class RoseWayMushroom(OverworldItem):
    description = ShuffleLocationSelector.RoseWayMushroom
    area = locations.Area.RoseWay
    item = items.RecoveryMushroom
    rooms = [79]
    event = 240
    npc_ids = [8]


class RoseWayCoin1(OverworldItem):
    description = ShuffleLocationSelector.RoseWayCoin1
    area = locations.Area.RoseWay
    item = items.Coins10
    rooms = [79]
    event = 235
    npc_ids = [18]


class RoseWayCoin2(OverworldItem):
    description = ShuffleLocationSelector.RoseWayCoin2
    area = locations.Area.RoseWay
    item = items.Coins10
    rooms = [79]
    event = 236
    npc_ids = [19]


class RoseWayCoin3(OverworldItem):
    description = ShuffleLocationSelector.RoseWayCoin3
    area = locations.Area.RoseWay
    item = items.Coins10
    rooms = [79]
    event = 237
    npc_ids = [20]


class RoseWayCoin4(OverworldItem):
    description = ShuffleLocationSelector.RoseWayCoin4
    area = locations.Area.RoseWay
    item = items.Coins10
    rooms = [79]
    event = 238
    npc_ids = [21]


class RoseWayCoin5(OverworldItem):
    description = ShuffleLocationSelector.RoseWayCoin5
    area = locations.Area.RoseWay
    item = items.Coins10
    rooms = [79]
    event = 239
    npc_ids = [22]


class RoseWayFiveChests1(StarAllowedChest):
    description = ShuffleLocationSelector.RoseWayFiveChests1
    area = locations.Area.RoseWay
    rooms = [81]
    npc_ids = [0]
    event = 247
    item = items.RecoveryMushroom


class RoseWayFiveChests2(StarAllowedChest):
    description = ShuffleLocationSelector.RoseWayFiveChests2
    area = locations.Area.RoseWay
    rooms = [81]
    npc_ids = [1]
    event = 246
    item = items.Coins(Chest, 5)


class RoseWayFiveChests3(StarAllowedChest):
    description = ShuffleLocationSelector.RoseWayFiveChests3
    area = locations.Area.RoseWay
    rooms = [81]
    npc_ids = [2]
    event = 245
    item = items.Coins(Chest, 5)


class RoseWayFiveChests4(StarAllowedChest):
    description = ShuffleLocationSelector.RoseWayFiveChests4
    area = locations.Area.RoseWay
    rooms = [81]
    npc_ids = [3]
    event = 244
    item = items.Coins(Chest, 5)


class RoseWayFiveChests5(StarAllowedChest):
    description = ShuffleLocationSelector.RoseWayFiveChests5
    area = locations.Area.RoseWay
    rooms = [81]
    npc_ids = [4]
    event = 243
    item = items.Coins(Chest, 5)

# *** Rose Town


class RoseTownFlag(NPCReward):
    description = ShuffleLocationSelector.RoseTownFlag
    rooms = [83, 84]
    event = 253
    area = locations.Area.RoseTown
    item = items.GreaperFlag
    key = True
    
    def item_allowed(self, item):
        if self.world.flags.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)



class RoseTownStore1(Chest):
    area = locations.Area.RoseTown
    description = ShuffleLocationSelector.RoseTownStore1
    rooms = [87]
    npc_ids = [4]
    event = 247
    item = items.Flower


class RoseTownStore2(Chest):
    area = locations.Area.RoseTown
    description = ShuffleLocationSelector.RoseTownStore2
    rooms = [87]
    npc_ids = [5]
    event = 246
    item = items.FrogCoin


class GardenerCloud1(Chest):
    area = locations.Area.RoseTownClouds
    description = ShuffleLocationSelector.GardenerCloud1
    rooms = [419]
    npc_ids = [0]
    event = 247
    item = items.LazyShellArmor
    access = 2
    special_equip = True

    def can_access(self, inventory):
        return locations.can_access_forest(self.world, inventory) and inventory.has_item(items.Seed) and inventory.has_item(items.Fertilizer)


class GardenerCloud2(Chest):
    area = locations.Area.RoseTownClouds
    description = ShuffleLocationSelector.GardenerCloud2
    rooms = [419]
    npc_ids = [1]
    event = 246
    item = items.LazyShellWeapon
    access = 2
    special_equip = True

    def can_access(self, inventory):
        return locations.can_access_forest(self.world, inventory) and inventory.has_item(items.Seed) and inventory.has_item(items.Fertilizer)


class RoseTownToad(NPCReward):
    description = ShuffleLocationSelector.RoseTownToad
    area = locations.Area.RoseTown
    rooms = [95, 96]
    event = 253
    item = items.FlowerTab


class Gaz(NPCReward):
    area = locations.Area.RoseTown
    description = ShuffleLocationSelector.Gaz
    rooms = [86]
    event = 253
    item = items.FingerShot
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.AlwaysOpen):
            self.access = 1

    def can_access(self, inventory):
        return locations.can_access_forest(self.world, inventory) 


class RoseTownTreasureHouse1(Chest):
    description = ShuffleLocationSelector.RoseTownTreasureHouse1
    area = locations.Area.RoseTown
    rooms = [93, 94]
    npc_ids = [0, 0]
    event = 247
    item = items.Flower


class RoseTownTreasureHouse2(Chest):
    description = ShuffleLocationSelector.RoseTownTreasureHouse2
    area = locations.Area.RoseTown
    rooms = [93, 94]
    npc_ids = [1, 1]
    event = 246
    item = items.Flower


class RoseTownTreasureHouseMazeReward(NPCReward):
    description = ShuffleLocationSelector.RoseTownTreasureHouseMazeReward
    area = locations.Area.RoseTown
    rooms = [93, 94]
    event = 253
    item = items.FrogCoin
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.AlwaysOpen):
            self.access = 1

    def can_access(self, inventory):
        return locations.can_access_forest(self.world, inventory) 


class RoseTownTreasureHouse3(Chest):
    description = ShuffleLocationSelector.RoseTownTreasureHouse3
    area = locations.Area.RoseTown
    rooms = [97, 98]
    npc_ids = [1, 1]
    event = 246
    item = items.FrogCoin

# *** Forest Maze


class ForestMaze1(StarAllowedChest):
    description = ShuffleLocationSelector.ForestMaze1
    area = locations.Area.ForestMaze
    rooms = [224]
    npc_ids = [2]
    event = 247
    item = items.KerokeroCola

    def can_access(self, inventory):
        return locations.can_access_forest(self.world, inventory) 


class ForestMaze2(StarAllowedChest):
    description = ShuffleLocationSelector.ForestMaze2
    area = locations.Area.ForestMaze
    rooms = [228]
    npc_ids = [2]
    event = 247
    item = items.FrogCoin

    def can_access(self, inventory):
        return locations.can_access_forest(self.world, inventory) 


class ForestMazeUnderground1(StarAllowedChest):
    description = ShuffleLocationSelector.ForestMazeUnderground1
    area = locations.Area.ForestMaze
    rooms = [242]
    npc_ids = [2]
    event = 247
    item = items.KerokeroCola

    def can_access(self, inventory):
        return locations.can_access_forest(self.world, inventory) 


class ForestMazeUnderground2(StarAllowedChest):
    description = ShuffleLocationSelector.ForestMazeUnderground2
    area = locations.Area.ForestMaze
    rooms = [242]
    npc_ids = [3]
    event = 246
    item = items.Flower

    def can_access(self, inventory):
        return locations.can_access_forest(self.world, inventory) 


class ForestMazeUnderground3(StarAllowedChest):
    description = ShuffleLocationSelector.ForestMazeUnderground3
    area = locations.Area.ForestMaze
    rooms = [242]
    npc_ids = [4]
    event = 245
    item = items.YouMissed

    def can_access(self, inventory):
        return locations.can_access_forest(self.world, inventory) 


class ForestMazeRedEssence(StarAllowedChest):
    description = ShuffleLocationSelector.ForestMazeRedEssence
    area = locations.Area.ForestMaze
    rooms = [227]
    npc_ids = [5]
    event = 247
    item = items.RedEssence

    def can_access(self, inventory):
        return locations.can_access_forest(self.world, inventory) 


class ForestMazeSecret1(StarAllowedChest):
    description = ShuffleLocationSelector.ForestMazeSecret1
    area = locations.Area.ForestMaze
    rooms = [234]
    npc_ids = [1]
    event = 247
    item = items.FrogCoin

    def can_access(self, inventory):
        return locations.can_access_forest(self.world, inventory) 


class ForestMazeSecret2(StarAllowedChest):
    description = ShuffleLocationSelector.ForestMazeSecret2
    area = locations.Area.ForestMaze
    rooms = [234]
    npc_ids = [2]
    event = 246
    item = items.Flower

    def can_access(self, inventory):
        return locations.can_access_forest(self.world, inventory) 


class ForestMazeSecret3(StarAllowedChest):
    description = ShuffleLocationSelector.ForestMazeSecret3
    area = locations.Area.ForestMaze
    rooms = [234]
    npc_ids = [3]
    event = 245
    item = items.Flower

    def can_access(self, inventory):
        return locations.can_access_forest(self.world, inventory) 


class ForestMazeSecret4(StarAllowedChest):
    description = ShuffleLocationSelector.ForestMazeSecret4
    area = locations.Area.ForestMaze
    rooms = [234]
    npc_ids = [4]
    event = 244
    item = items.Flower

    def can_access(self, inventory):
        return locations.can_access_forest(self.world, inventory) 


class ForestMazeSecret5(StarAllowedChest):
    description = ShuffleLocationSelector.ForestMazeSecret5
    area = locations.Area.ForestMaze
    rooms = [234]
    npc_ids = [5]
    event = 243
    item = items.RecoveryMushroom

    def can_access(self, inventory):
        return locations.can_access_forest(self.world, inventory) 


class ForestMazeCharacter(CharacterRecruit):
    area = locations.Area.ForestMaze
    description = ShuffleLocationSelector.ForestMazeCharacter
    item = items.GenoRecruit
    rooms = [232]
    event = 186

    def can_access(self, inventory):
        return locations.can_access_forest(self.world, inventory) 


class ForestMazeBoss(BossStarPiece):
    area = locations.Area.ForestMaze
    description = ShuffleLocationSelector.ForestMazeBoss
    rooms = [232]
    event = 167
    item = items.StarPiece

    def can_access(self, inventory):
        return locations.can_access_forest(self.world, inventory) 


# *** Pipe Vault

class PipeVaultSlide1(StarAllowedChest):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.PipeVaultSlide1
    rooms = [125]
    npc_ids = [8]
    event = 245
    item = items.Flower


class PipeVaultSlide2(StarAllowedChest):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.PipeVaultSlide2
    rooms = [125]
    npc_ids = [9]
    event = 246
    item = items.FrogCoin


class PipeVaultSlide3(StarAllowedChest):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.PipeVaultSlide3
    rooms = [125]
    npc_ids = [10]
    event = 247
    item = items.FrogCoin


class PipeVaultSlideCoin1(OverworldItem):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.PipeVaultSlideCoin1
    rooms = [125]
    event = 237
    item = items.Coins1
    npc_ids = [0]


class PipeVaultSlideCoin2(OverworldItem):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.PipeVaultSlideCoin2
    rooms = [125]
    event = 238
    item = items.Coins1
    npc_ids = [1]


class PipeVaultSlideCoin3(OverworldItem):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.PipeVaultSlideCoin3
    rooms = [125]
    event = 239
    item = items.Coins1
    npc_ids = [2]


class PipeVaultSlideCoin4(OverworldItem):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.PipeVaultSlideCoin4
    rooms = [125]
    event = 240
    item = items.Coins1
    npc_ids = [3]


class PipeVaultSlideCoin5(OverworldItem):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.PipeVaultSlideCoin5
    rooms = [125]
    event = 241
    item = items.Coins1
    npc_ids = [4]


class PipeVaultSlideFrogCoin(OverworldItem):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.PipeVaultSlideFrogCoin
    rooms = [125]
    event = 236
    item = items.FrogCoin
    npc_ids = [5]


class PipeVaultNippers1(StarAllowedChest):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.PipeVaultNippers1
    rooms = [128]
    npc_ids = [0]
    event = 247
    item = items.Flower
    npc_ids = [6]


class PipeVaultNippers2(StarAllowedChest):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.PipeVaultNippers2
    rooms = [128]
    npc_ids = [1]
    event = 246
    item = items.Coins(Chest, 20)


class GoombaThumping1(NPCReward):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.GoombaThumping1
    rooms = [143]
    event = 253
    item = items.FlowerTab


class GoombaThumping2(NPCReward):
    area = locations.Area.PipeVault
    description = ShuffleLocationSelector.GoombaThumping2
    rooms = [143]
    event = 252
    item = items.FlowerJar


# *** Yo'ster Isle

class YosterIsleEntrance(Chest):
    description = ShuffleLocationSelector.YosterIsleEntrance
    area = locations.Area.YosterIsle
    rooms = [33]
    npc_ids = [1]
    item = items.FrogCoin
    event = 247


class YosterIsleRaceReward1(NPCReward):
    description = ShuffleLocationSelector.YosterIsleRaceReward1
    area = locations.Area.YosterIsle
    rooms = [34]
    item = items.YoshiCookie
    event = 253


class YosterIsleRaceReward2(NPCReward):
    description = ShuffleLocationSelector.YosterIsleRaceReward2
    area = locations.Area.YosterIsle
    rooms = [34]
    item = items.YoshiCookie
    event = 251


class YosterIsleRaceReward3(NPCReward):
    description = ShuffleLocationSelector.YosterIsleRaceReward3
    area = locations.Area.YosterIsle
    rooms = [34]
    item = items.YoshiCookie
    event = 250


class YosterIsleFlag(NPCReward):
    description = ShuffleLocationSelector.YosterIsleFlag
    area = locations.Area.YosterIsle
    rooms = [34]
    item = items.BigBooFlag
    event = 252
    key = True
    
    def item_allowed(self, item):
        if self.world.flags.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)


# *** Moleville


class BucketGirl(NPCReward):
    description = ShuffleLocationSelector.BucketGirl
    area = locations.Area.Moleville
    rooms = [108]
    event = 253
    item = items.FrogCoin
    dialogs_to_replace = [2911]
    access = 2

    def item_allowed(self, item):
        if self.world.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.Vanilla) or self.world.settings.is_flag_value(flags.BucketWarp, True):
            return False
        return super().item_allowed(item)
    
    def can_access(self, inventory):
        # always have a frog coin if inaccessible
        fireworks_access = False
        if self.world.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.ShuffleFireworks):
            fireworks_access = inventory.has_item(items.ProgressiveFireworks)
        elif self.world.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.ProgressiveFireworks):
            fireworks_access = inventory.has_item_count(items.ProgressiveFireworks, 3)
        return fireworks_access and inventory.has_item(items.BambinoBomb) and self.world.settings.is_flag_value(flags.BucketWarp, False)


class TreasureSeller1(TreasureSellerReward):
    description = ShuffleLocationSelector.TreasureSeller1
    area = locations.Area.Moleville
    rooms = [336]
    event = 253
    item = items.LuckyJewel
    dialogs_to_replace = [2911]
    access = 2

    
    def can_access(self, inventory):
        return inventory.has_item(items.BambinoBomb)


class TreasureSeller2(TreasureSellerReward):
    description = ShuffleLocationSelector.TreasureSeller2
    area = locations.Area.Moleville
    rooms = [336]
    event = 252
    item = items.ProgressiveEgg
    dialogs_to_replace = [2908]
    access = 2
    
    def can_access(self, inventory):
        return inventory.has_item(items.BambinoBomb) and locations.can_access_yaridovich(self, inventory)


class TreasureSeller3(TreasureSellerReward):
    description = ShuffleLocationSelector.TreasureSeller3
    area = locations.Area.Moleville
    rooms = [336]
    event = 251
    item = items.FryingPan
    dialogs_to_replace = [2914]
    access = 2
    
    def can_access(self, inventory):
        return inventory.has_item(items.BambinoBomb) and locations.can_access_volcano(self, inventory)


class FireworksShop(NPCReward):
    # Fireworks shuffle/progressive ONLY
    area = locations.Area.Moleville
    rooms = [339]
    event = 253
    item = items.Fireworks
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if self.world.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.ShuffleFireworks):
            self.key = True
        elif self.world.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.ProgressiveFireworks):
            self.key = True

    
    def item_allowed(self, item):
        if self.world.flags.is_flag_value(flags.KeyItemsAnywhere, False) and (self.world.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.ShuffleFireworks) or self.world.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.ProgressiveFireworks)):
            return super().item_allowed(item) and item.is_key
        else:
            return super().item_allowed(item)

    
    def can_access(self, inventory):
        return inventory.has_item(items.BambinoBomb)


# *** Moleville Mines

class MolevilleMinesStarChest(StarAllowedChest):
    description = ShuffleLocationSelector.FireworksShop
    area = locations.Area.MolevilleMines
    rooms = [285]
    npc_ids = [0]
    event = 247
    item = items.MolevilleMinesStar
    access = 2
    
    def can_access(self, inventory):
        return inventory.has_item(items.BambinoBomb)


class MolevilleMinesShyGuy(OverworldItem):
    description = ShuffleLocationSelector.MolevilleMinesShyGuy
    area = locations.Area.MolevilleMines
    rooms = [286]
    event = 241
    npc_ids = [2]
    item = items.FrogCoin
    access = 2
    
    def can_access(self, inventory):
        return inventory.has_item(items.BambinoBomb)


class MolevilleMinesCoins(StarAllowedChest):
    description = ShuffleLocationSelector.MolevilleMinesCoins
    area = locations.Area.MolevilleMines
    rooms = [280]
    npc_ids = [0]
    event = 247
    item = items.Coins(Chest, 150)
    access = 2
    
    def can_access(self, inventory):
        return inventory.has_item(items.BambinoBomb)


class MolevilleMinesPunchinello1(StarAllowedChest):
    description = ShuffleLocationSelector.MolevilleMinesPunchinello1
    area = locations.Area.MolevilleMines
    rooms = [288]
    npc_ids = [0]
    event = 247
    item = items.RecoveryMushroom
    access = 2
    
    def can_access(self, inventory):
        return inventory.has_item(items.BambinoBomb)


class MolevilleMinesPunchinello2(StarAllowedChest):
    description = ShuffleLocationSelector.MolevilleMinesPunchinello2
    area = locations.Area.MolevilleMines
    rooms = [288]
    npc_ids = [1]
    event = 246
    item = items.Flower
    access = 2
    
    def can_access(self, inventory):
        return inventory.has_item(items.BambinoBomb)


class MolevilleMinesBoss2(BossStarPiece):
    description = ShuffleLocationSelector.MolevilleMinesBoss2
    area = locations.Area.MolevilleMines
    rooms = [271]
    event = 167
    item = items.StarPiece
    access = 2
    
    def can_access(self, inventory):
        return inventory.has_item(items.BambinoBomb)

class MolevilleMinesCharacter(CharacterRecruit):
    area = locations.Area.ForestMaze
    description = ShuffleLocationSelector.MolevilleMinesCharacter
    item = items.BowserRecruit
    rooms = [284]
    event = 186
    
    def can_access(self, inventory):
        return inventory.has_item(items.BambinoBomb)


class CrocoFlunkie1(NPCReward):
    description = ShuffleLocationSelector.CrocoFlunkie1
    area = locations.Area.MolevilleMines
    rooms = [273]
    event = 253
    item = items.FlowerTab
    missable = True

class CrocoFlunkie2(NPCReward):
    description = ShuffleLocationSelector.CrocoFlunkie2
    area = locations.Area.MolevilleMines
    rooms = [277]
    event = 253
    item = items.FlowerTab
    missable = True


class CrocoFlunkie3(NPCReward):
    description = ShuffleLocationSelector.CrocoFlunkie3
    area = locations.Area.MolevilleMines
    rooms = [283]
    event = 253
    item = items.FlowerTab
    missable = True


class Croco2Item(NPCReward):
    description = ShuffleLocationSelector.Croco2Item
    area = locations.Area.MolevilleMines
    rooms = [518]
    event = 253
    item = items.BambinoBomb
    key = True
    
    def item_allowed(self, item):
        if self.world.flags.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)


class MolevilleMinesBoss1(BossStarPiece):
    description = ShuffleLocationSelector.MolevilleMinesBoss1
    area = locations.Area.MolevilleMines
    rooms = [518]
    event = 167

# *** Booster Pass


class BoosterPass1(StarAllowedChest):
    description = ShuffleLocationSelector.BoosterPass1
    area = locations.Area.BoosterPass
    rooms = [100]
    npc_ids = [8]
    event = 247
    item = items.Flower


class BoosterPass2(StarAllowedChest):
    description = ShuffleLocationSelector.BoosterPass2
    area = locations.Area.BoosterPass
    rooms = [100]
    npc_ids = [9]
    event = 246
    item = items.RockCandy


class BoosterPassBush(NPCReward):
    description = ShuffleLocationSelector.BoosterPassBush
    area = locations.Area.BoosterPass
    rooms = [100]
    event = 253
    item = items.FrogCoin
    coinsanity = True


class BoosterPassFlower(OverworldItem):
    description = ShuffleLocationSelector.BoosterPassFlower
    area = locations.Area.BoosterPass
    rooms = [101]
    event = 241
    npc_ids = [6]
    item = items.Flower


class BoosterPassSecret1(StarAllowedChest):
    area = locations.Area.BoosterPass
    description = ShuffleLocationSelector.BoosterPassSecret1
    rooms = [405]
    npc_ids = [10]
    event = 247
    item = items.FrogCoin
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterPassSecret2(StarAllowedChest):
    area = locations.Area.BoosterPass
    description = ShuffleLocationSelector.BoosterPassSecret2
    rooms = [405]
    npc_ids = [11]
    event = 246
    item = items.Flower
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterPassSecret3(StarAllowedChest):
    area = locations.Area.BoosterPass
    description = ShuffleLocationSelector.BoosterPassSecret3
    rooms = [405]
    npc_ids = [12]
    event = 245
    item = items.KerokeroCola
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


# *** Booster Tower

class BoosterTowerSpookum(StarAllowedChest):
    description = ShuffleLocationSelector.BoosterTowerSpookum
    area = locations.Area.BoosterTower
    item = items.FrogCoin
    rooms = [196]
    npc_ids = [7]
    event = 247
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerThwomp(StarAllowedChest):
    description = ShuffleLocationSelector.BoosterTowerThwomp
    area = locations.Area.BoosterTower
    item = items.RecoveryMushroom
    rooms = [36]
    npc_ids = [2]
    event = 247
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerKnifeGuy(NPCReward):
    description = ShuffleLocationSelector.BoosterTowerKnifeGuy
    area = locations.Area.BoosterTower
    item = items.BrightCard
    rooms = [39]
    event = 253
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if self.world.settings.is_flag_value(flags.CasinoWarp, True):
            self.key = True

    def item_allowed(self, item):
        if self.world.flags.is_flag_value(flags.KeyItemsAnywhere, False) and self.world.settings.is_flag_value(flags.CasinoWarp, True):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)

    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerRoomKey(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerRoomKey
    area = locations.Area.BoosterTower
    item = items.RoomKey
    coinsanity = False
    rooms = [41]
    event = 228
    npc_ids = [5]
    key = True
    
    def item_allowed(self, item):
        if self.world.flags.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerFrogCoin1(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerFrogCoin1
    area = locations.Area.BoosterTower
    item = items.FrogCoin
    rooms = [41]
    event = 241
    npc_ids = [0]
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerFrogCoin2(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerFrogCoin2
    area = locations.Area.BoosterTower
    item = items.FrogCoin
    rooms = [41]
    event = 240
    npc_ids = [1]
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerFrogCoin3(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerFrogCoin3
    area = locations.Area.BoosterTower
    item = items.FrogCoin
    rooms = [41]
    event = 239
    npc_ids = [2]
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerFrogCoin4(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerFrogCoin4
    area = locations.Area.BoosterTower
    item = items.FrogCoin
    rooms = [41]
    event = 238
    npc_ids = [3]
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerCoin1(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerCoin1
    area = locations.Area.BoosterTower
    item = items.Coins1
    rooms = [41]
    event = 237
    npc_ids = [7]
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerCoin2(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerCoin2
    area = locations.Area.BoosterTower
    item = items.Coins1
    rooms = [41]
    event = 236
    npc_ids = [8]
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerCoin3(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerCoin3
    area = locations.Area.BoosterTower
    item = items.Coins1
    rooms = [41]
    event = 235
    npc_ids = [9]
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerCoin4(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerCoin4
    area = locations.Area.BoosterTower
    item = items.Coins1
    rooms = [41]
    event = 234
    npc_ids = [10]
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerCoin5(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerCoin5
    area = locations.Area.BoosterTower
    item = items.Coins1
    rooms = [41]
    event = 233
    npc_ids = [11]
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerCoin6(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerCoin6
    area = locations.Area.BoosterTower
    item = items.Coins1
    rooms = [41]
    event = 232
    npc_ids = [12]
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerCoin7(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerCoin7
    area = locations.Area.BoosterTower
    item = items.Coins1
    rooms = [41]
    event = 231
    npc_ids = [13]
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerCoin8(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerCoin8
    area = locations.Area.BoosterTower
    item = items.Coins1
    rooms = [41]
    event = 230
    npc_ids = [14]
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerCoin9(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerCoin9
    area = locations.Area.BoosterTower
    item = items.Coins1
    rooms = [41]
    event = 229
    npc_ids = [15]
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerMasher(OverworldItem):
    description = ShuffleLocationSelector.BoosterTowerMasher
    area = locations.Area.BoosterTower
    rooms = [197]
    event = 253
    item = items.Masher
    npc_ids = [3]
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerParachute(StarAllowedChest):
    description = ShuffleLocationSelector.BoosterTowerParachute
    area = locations.Area.BoosterTower
    item = items.FrogCoin
    rooms = [35]
    npc_ids = [9]
    event = 247
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerParachuteCrevice(NPCReward):
    description = ShuffleLocationSelector.BoosterTowerParachuteCrevice
    area = locations.Area.BoosterTower
    item = items.FrogCoin
    coinsanity = True
    rooms = [35]
    event = 253
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerZoomShoes(StarAllowedChest):
    description = ShuffleLocationSelector.BoosterTowerZoomShoes
    area = locations.Area.BoosterTower
    item = items.ZoomShoes
    rooms = [48]
    npc_ids = [0]
    event = 247
    access = 2
    special_equip = True
    
    def can_access(self, inventory):
        return inventory.has_item(items.RoomKey) and locations.can_access_tower(self, inventory)


class BoosterTowerTop1(StarAllowedChest):
    description = ShuffleLocationSelector.BoosterTowerTop1
    area = locations.Area.BoosterTower
    rooms = [199]
    npc_ids = [0]
    script = 247
    item = items.FrogCoin
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerTop2(StarAllowedChest):
    description = ShuffleLocationSelector.BoosterTowerTop2
    area = locations.Area.BoosterTower
    rooms = [199]
    npc_ids = [1]
    script = 246
    item = items.GoodieBag
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerTop3(StarAllowedChest):
    description = ShuffleLocationSelector.BoosterTowerTop3
    area = locations.Area.BoosterTower
    rooms = [199]
    npc_ids = [5]
    script = 245
    item = items.RecoveryMushroom
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerRailway(NPCReward):
    area = locations.Area.BoosterTower
    description = ShuffleLocationSelector.BoosterTowerRailway
    rooms = [194]
    event = 253
    item = items.FlowerTab
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerPortraits(OverworldItem):
    area = locations.Area.BoosterTower
    description = ShuffleLocationSelector.BoosterTowerPortraits
    rooms = [195]
    event = 241
    npc_ids = [7]
    item = items.ElderKey
    coinsanity = False
    key = True
    
    def item_allowed(self, item):
        if self.world.flags.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerChomp(OverworldItem):
    area = locations.Area.BoosterTower
    description = ShuffleLocationSelector.BoosterTowerChomp
    rooms = [200]
    event = 241
    npc_ids = [0]
    item = items.Chomp
    coinsanity = False
    access = 2
    special_equip = True
    
    def can_access(self, inventory):
        return inventory.has_item(items.ElderKey) and locations.can_access_tower(self, inventory)


class BoosterTowerCurtainGame(NPCReward):
    area = locations.Area.BoosterTower
    description = ShuffleLocationSelector.BoosterTowerCurtainGame
    rooms = [192]
    event = 253
    item = items.Amulet
    missable = True
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerStarPiece1(BossStarPiece):
    area = locations.Area.BoosterTower
    description = ShuffleLocationSelector.BoosterTowerStarPiece1
    rooms = [192]
    event = 167
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)


class BoosterTowerStarPiece2(BossStarPiece):
    area = locations.Area.BoosterTower
    description = ShuffleLocationSelector.BoosterTowerStarPiece2
    rooms = [258]
    event = 167
    
    def can_access(self, inventory):
        return locations.can_access_tower(self, inventory)



# *** Marrymore

class MarrymorePrize1(NPCReward):
    area = locations.Area.Marrymore
    description = ShuffleLocationSelector.MarrymorePrize1
    item = items.FlowerTab
    rooms = [9]
    event = 253


class MarrymorePrize2(NPCReward):
    area = locations.Area.Marrymore
    description = ShuffleLocationSelector.MarrymorePrize2
    item = items.FlowerJar
    rooms = [9]
    event = 252


class MarrymorePrize3(NPCReward):
    area = locations.Area.Marrymore
    item = items.MultiFrogCoin(NPCReward, 5)
    description = ShuffleLocationSelector.MarrymorePrize3
    rooms = [9]
    event = 251


class MarrymorePrize4(NPCReward):
    area = locations.Area.Marrymore
    item = items.MultiFrogCoin(NPCReward, 10)
    description = ShuffleLocationSelector.MarrymorePrize4
    rooms = [9]
    event = 250


class MarrymorePrize5(NPCReward):
    area = locations.Area.Marrymore
    item = items.MultiFrogCoin(NPCReward, 15)
    description = ShuffleLocationSelector.MarrymorePrize5
    rooms = [9]
    event = 249


class MarrymorePrize6(NPCReward):
    area = locations.Area.Marrymore
    item = items.MultiFrogCoin(NPCReward, 20)
    description = ShuffleLocationSelector.MarrymorePrize6
    rooms = [9]
    event = 248


class MarrymoreInn(Chest):
    area = locations.Area.Marrymore
    description = ShuffleLocationSelector.MarrymoreInn
    item = items.FrogCoin
    rooms = [9]
    npc_ids = [0]
    event = 247


class MarrymoreStarPiece(BossStarPiece):
    area = locations.Area.Marrymore
    description = ShuffleLocationSelector.MarrymoreStarPiece
    rooms = [154]
    event = 167
    access = 1
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.MarrymoreGate, MarrymoreGating.FinishBoosterTower):
            self.access = 2
    
    def can_access(self, inventory):
        return locations.can_access_marrymore(self, inventory)


class MarrymoreCharacter(CharacterRecruit):
    area = locations.Area.Marrymore
    description = ShuffleLocationSelector.MarrymoreCharacter
    item = items.ToadstoolRecruit
    rooms = [154]
    event = 186
    
    def can_access(self, inventory):
        return locations.can_access_marrymore(self, inventory)

# populate this with the corresponding character in MarrymoreCharacter
class MarrymoreCharacterSpotted(CharacterSpotted):
    area = locations.Area.BoosterHill
    description = ShuffleLocationSelector.MarrymoreCharacter
    item = items.ToadstoolSpotted


# *** Star Hill


class StarHillStarPiece1(BossStarPiece):
    area = locations.Area.StarHill
    description = ShuffleLocationSelector.StarHillStarPiece1
    rooms = [157]
    event = 167
    item = items.StarPiece



# *** Seaside Town



class FrogDisciple1(FrogCoinShopItem):
    description = ShuffleLocationSelector.FrogDisciple1
    area = locations.Area.SeasideTown
    item = items.SeeYa
class FrogDisciple2(FrogCoinShopItem):
    description = ShuffleLocationSelector.FrogDisciple2
    area = locations.Area.SeasideTown
    item = items.EarlierTimes
class FrogDisciple3(FrogCoinShopItem):
    description = ShuffleLocationSelector.FrogDisciple3
    area = locations.Area.SeasideTown
    item = items.ExpBooster
class FrogDisciple4(FrogCoinShopItem):
    description = ShuffleLocationSelector.FrogDisciple4
    area = locations.Area.SeasideTown
    item = items.CoinTrick
class FrogDisciple5(FrogCoinShopItem):
    description = ShuffleLocationSelector.FrogDisciple5
    area = locations.Area.SeasideTown
    item = items.ScroogeRing


class SeasideTownBoss(BossStarPiece):
    description = ShuffleLocationSelector.SeasideTownBoss
    area = locations.Area.SeasideTown
    rooms = [315]
    event = 167
    item = items.StarPiece
    
    def can_access(self, inventory):
        return locations.can_access_yaridovich(self, inventory)


class SeasideTownBossPrize(OverworldItem):
    area = locations.Area.SeasideTown
    description = ShuffleLocationSelector.SeasideTownBossPrize
    rooms = [316]
    event = 241
    npc_ids = [0]
    item = items.ShedKey
    coinsanity = False
    key = True
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.YaridovichGate, YaridovichGating.AlwaysOpen):
            self.access = 1

    
    def item_allowed(self, item):
        if self.world.flags.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)
    
    def can_access(self, inventory):
        return locations.can_access_yaridovich(self, inventory)


class SeasideTownRescue(NPCReward):
    area = locations.Area.SeasideTown
    description = ShuffleLocationSelector.SeasideTownRescue
    rooms = [314]
    event = 253
    item = items.FlowerBox
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.YaridovichGate, YaridovichGating.AlwaysOpen):
            self.access = 1

    def can_access(self, inventory):
        return inventory.has_item(items.ShedKey) and locations.can_access_yaridovich(self, inventory)


# *** Sea

class SeaStarChest(StarAllowedChest):
    area = locations.Area.Sea
    description = ShuffleLocationSelector.SeaStarChest
    rooms = [134]
    npc_ids = [0]
    event = 247
    item = items.SeaStar
    access = 1
    
    def __init__(self, world):
        super().__init__(world)
        for option in [SeaGating.Find1Star, SeaGating.Find2Star, SeaGating.Find3Star, SeaGating.Find4Star, SeaGating.Find5Star, SeaGating.Find6Star]:
            if world.settings.is_flag_value(flags.SeaGate, option):
                self.access = 2

    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class SeaSaveRoom1(StarAllowedChest):
    area = locations.Area.Sea
    description = ShuffleLocationSelector.SeaSaveRoom1
    rooms = [132]
    npc_ids = [0]
    event = 245
    item = items.FrogCoin
    access = 1
    
    def __init__(self, world):
        super().__init__(world)
        for option in [SeaGating.Find1Star, SeaGating.Find2Star, SeaGating.Find3Star, SeaGating.Find4Star, SeaGating.Find5Star, SeaGating.Find6Star]:
            if world.settings.is_flag_value(flags.SeaGate, option):
                self.access = 2
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class SeaSaveRoom2(StarAllowedChest):
    area = locations.Area.Sea
    description = ShuffleLocationSelector.SeaSaveRoom2
    rooms = [132]
    npc_ids = [1]
    event = 246
    item = items.Flower
    access = 1
    
    def __init__(self, world):
        super().__init__(world)
        for option in [SeaGating.Find1Star, SeaGating.Find2Star, SeaGating.Find3Star, SeaGating.Find4Star, SeaGating.Find5Star, SeaGating.Find6Star]:
            if world.settings.is_flag_value(flags.SeaGate, option):
                self.access = 2
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class SeaSaveRoom3(StarAllowedChest):
    area = locations.Area.Sea
    description = ShuffleLocationSelector.SeaSaveRoom3
    rooms = [132]
    npc_ids = [2]
    event = 247
    item = items.RecoveryMushroom
    access = 1
    
    def __init__(self, world):
        super().__init__(world)
        for option in [SeaGating.Find1Star, SeaGating.Find2Star, SeaGating.Find3Star, SeaGating.Find4Star, SeaGating.Find5Star, SeaGating.Find6Star]:
            if world.settings.is_flag_value(flags.SeaGate, option):
                self.access = 2
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class SeaWhirlpoolChest(StarAllowedChest):
    description = ShuffleLocationSelector.SeaWhirlpoolChest
    area = locations.Area.Sea
    rooms = [133]
    npc_ids = [0]
    event = 247
    item = items.MaxMushroom
    access = 1
    
    def __init__(self, world):
        super().__init__(world)
        for option in [SeaGating.Find1Star, SeaGating.Find2Star, SeaGating.Find3Star, SeaGating.Find4Star, SeaGating.Find5Star, SeaGating.Find6Star]:
            if world.settings.is_flag_value(flags.SeaGate, option):
                self.access = 2
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


# *** Sunken Ship

class SunkenShipRatStairs(StarAllowedChest):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipRatStairs
    rooms = [167]
    npc_ids = [0]
    event = 247
    item = items.Coins(Chest, 100)
    access = 1
    
    def __init__(self, world):
        super().__init__(world)
        for option in [SeaGating.Find1Star, SeaGating.Find2Star, SeaGating.Find3Star, SeaGating.Find4Star, SeaGating.Find5Star, SeaGating.Find6Star]:
            if world.settings.is_flag_value(flags.SeaGate, option):
                self.access = 2
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class SunkenShipRatStairsFlower(PacketItem):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipRatStairsFlower
    rooms = [167]
    script_id = 3385
    event = 241
    item = items.Flower
    access = 1
    
    def __init__(self, world):
        super().__init__(world)
        for option in [SeaGating.Find1Star, SeaGating.Find2Star, SeaGating.Find3Star, SeaGating.Find4Star, SeaGating.Find5Star, SeaGating.Find6Star]:
            if world.settings.is_flag_value(flags.SeaGate, option):
                self.access = 2
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class SunkenShipShop(StarAllowedChest):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipShop
    rooms = [169]
    npc_ids = [0]
    event = 247
    item = items.Coins(Chest, 100)
    access = 1
    
    def __init__(self, world):
        super().__init__(world)
        for option in [SeaGating.Find1Star, SeaGating.Find2Star, SeaGating.Find3Star, SeaGating.Find4Star, SeaGating.Find5Star, SeaGating.Find6Star]:
            if world.settings.is_flag_value(flags.SeaGate, option):
                self.access = 2
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class SunkenShipCoins1(StarAllowedChest):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipCoins1
    rooms = [175]
    npc_ids = [0]
    event = 247
    item = items.Coins(Chest, 100)
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class SunkenShipCoins2(StarAllowedChest):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipCoins2
    rooms = [175]
    npc_ids = [1]
    event = 246
    item = items.Coins(Chest, 100)
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class SunkenShipCloneRoom(StarAllowedChest):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipCloneRoom
    rooms = [179]
    npc_ids = [2]
    event = 247
    item = items.KerokeroCola
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class SunkenShipFrogCoinRoom(StarAllowedChest):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipFrogCoinRoom
    rooms = [183]
    npc_ids = [0]
    event = 247
    item = items.FrogCoin
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class SunkenShipHidonMushroom(StarAllowedChest):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipHidonMushroom
    rooms = [184]
    npc_ids = [1]
    event = 247
    item = items.RecoveryMushroom
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class HidonChest(StarAllowedChest):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.HidonChest
    rooms = [184]
    npc_ids = [2]
    event = 246
    item = items.HidonFight
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class HidonReward1(NPCReward):
    description = ShuffleLocationSelector.HidonReward1
    rooms = [513]
    event = 253
    item = items.SafetyBadge
    access = 2
    
    def can_access(self, inventory):
        return inventory.has_item(items.HidonFight)


class HidonReward2(Chest):
    description = ShuffleLocationSelector.HidonReward2
    rooms = [513]
    event = 245
    manual_70A7 = True
    item = items.Coins(Chest, 100)
    access = 2
    
    def can_access(self, inventory):
        return inventory.has_item(items.HidonFight)

class HidonBoss(BossStarPiece):
    description = ShuffleLocationSelector.HidonBoss
    rooms = [513]
    event = 167
    
    def can_access(self, inventory):
        return inventory.has_item(items.HidonFight)


class SunkenShipUnderwaterFrogCoin1(OverworldItem):
    description = ShuffleLocationSelector.SunkenShipUnderwaterFrogCoin1
    area = locations.Area.SunkenShip
    item = items.FrogCoin
    rooms = [187]
    event = 241
    npc_ids = [0]
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class SunkenShipUnderwaterFrogCoin2(OverworldItem):
    description = ShuffleLocationSelector.SunkenShipUnderwaterFrogCoin2
    area = locations.Area.SunkenShip
    item = items.FrogCoin
    rooms = [187]
    event = 240
    npc_ids = [1]
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class SunkenShipUnderwaterFrogCoin3(OverworldItem):
    description = ShuffleLocationSelector.SunkenShipUnderwaterFrogCoin3
    area = locations.Area.SunkenShip
    item = items.FrogCoin
    rooms = [187]
    event = 239
    npc_ids = [2]
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class SunkenShipUnderwaterFrogCoin4(OverworldItem):
    description = ShuffleLocationSelector.SunkenShipUnderwaterFrogCoin4
    area = locations.Area.SunkenShip
    item = items.FrogCoin
    rooms = [187]
    event = 238
    npc_ids = [3]
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class SunkenShipSafetyRing(StarAllowedChest):
    description = ShuffleLocationSelector.SunkenShipSafetyRing
    area = locations.Area.SunkenShip
    rooms = [185]
    npc_ids = [0]
    event = 247
    item = items.SafetyRing
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class SunkenShipBandanaReds(StarAllowedChest):
    description = ShuffleLocationSelector.SunkenShipBandanaReds
    area = locations.Area.SunkenShip
    item = items.RecoveryMushroom
    rooms = [24]
    npc_ids = [4]
    event = 247
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class SunkenShipBlooberRoom(OverworldItem):
    description = ShuffleLocationSelector.SunkenShipBlooberRoom
    area = locations.Area.SunkenShip
    item = items.FrogCoin
    rooms = [27]
    event = 241
    npc_ids = [5]
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class SunkenShipTrampolinePuzzle(PacketItem):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipTrampolinePuzzle
    rooms = [163]
    event = 241
    script_id = 3383
    item = items.Flower
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class SunkenShipTroopaPuzzle(PacketItem):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipTroopaPuzzle
    rooms = [166]
    event = 241
    script_id = 3384
    item = items.RecoveryMushroom
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class SunkenShip3DMaze(PacketItem):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShip3DMaze
    rooms = [168]
    event = 241
    script_id = 3386
    item = items.RoyalSyrup
    coinsanity = False
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class SunkenShipCoinSnake(NPCReward):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipCoinSnake
    rooms = [171]
    event = 253
    npc_ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    item = items.Coins(NPCReward, 150)
    # Needs special considerations for the sound played in 3216
    # and the sequences performed in 3216 and 3215
    # depending on the item
    # ship access
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class SunkenShipCannonballPuzzle(PacketItem):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipCannonballPuzzle
    rooms = [172]
    event = 241
    script_id = 3387
    item = items.Mushroom
    coinsanity = False
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class SunkenShipBarrelPuzzle(PacketItem):
    area = locations.Area.SunkenShip
    description = ShuffleLocationSelector.SunkenShipBarrelPuzzle
    rooms = [176]
    event = 241
    script_id = 3389
    item = items.RecoveryMushroom
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)



class SunkenShipMidboss(BossStarPiece):
    description = ShuffleLocationSelector.SunkenShipMidboss
    area = locations.Area.SunkenShip
    rooms = [177]
    event = 167
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


class SunkenShipBoss(BossStarPiece):
    description = ShuffleLocationSelector.SunkenShipBoss
    area = locations.Area.SunkenShip
    rooms = [28]
    event = 167
    
    def can_access(self, inventory):
        return locations.can_access_sea(self, inventory)


# *** Land's End


class LandsEndRedEssence(StarAllowedChest):
    area = locations.Area.LandsEnd
    description = ShuffleLocationSelector.LandsEndRedEssence
    rooms = [137]
    npc_ids = [4]
    event = 247
    item = items.RedEssence


class LandsEndChowPit1(StarAllowedChest):
    area = locations.Area.LandsEnd
    description = ShuffleLocationSelector.LandsEndChowPit1
    rooms = [138]
    npc_ids = [6]
    event = 247
    item = items.KerokeroCola


class LandsEndChowPit2(StarAllowedChest):
    area = locations.Area.LandsEnd
    description = ShuffleLocationSelector.LandsEndChowPit2
    rooms = [138]
    npc_ids = [7]
    event = 246
    item = items.FrogCoin


class LandsEndBeeRoom(StarAllowedChest):
    area = locations.Area.LandsEnd
    description = ShuffleLocationSelector.LandsEndBeeRoom
    rooms = [141]
    npc_ids = [6]
    event = 247
    item = items.FrogCoin


class LandsEndSecret1(StarAllowedChest):
    area = locations.Area.LandsEnd
    description = ShuffleLocationSelector.LandsEndSecret1
    rooms = [270]
    npc_ids = [6]
    event = 247
    item = items.FrogCoin


class LandsEndSecret2(StarAllowedChest):
    area = locations.Area.LandsEnd
    description = ShuffleLocationSelector.LandsEndSecret2
    rooms = [270]
    npc_ids = [7]
    event = 246
    item = items.Flower


class LandsEndShyAway(StarAllowedChest):
    area = locations.Area.LandsEnd
    description = ShuffleLocationSelector.LandsEndShyAway
    rooms = [401]
    npc_ids = [6]
    event = 247
    item = items.RecoveryMushroom


class LandsEndStarChest1(StarAllowedChest):
    area = locations.Area.LandsEnd
    description = ShuffleLocationSelector.LandsEndStarChest1
    rooms = [263]
    npc_ids = [5]
    event = 247
    item = items.LandsEndVolcanoStar


class LandsEndStarChest2(StarAllowedChest):
    area = locations.Area.LandsEnd
    description = ShuffleLocationSelector.LandsEndStarChest2
    rooms = [262]
    npc_ids = [18]
    event = 247
    item = items.LandsEndStar2


class LandsEndStarChest3(StarAllowedChest):
    area = locations.Area.LandsEnd
    description = ShuffleLocationSelector.LandsEndStarChest3
    rooms = [262]
    npc_ids = [19]
    event = 246
    item = items.LandsEndStar3


class TroopaClimb(NPCReward):
    area = locations.Area.LandsEnd
    description = ShuffleLocationSelector.TroopaClimb
    rooms = [407]
    event = 253
    item = items.TroopaPin


class LandsEndStarPiece1(BossStarPiece):
    area = locations.Area.LandsEnd
    description = ShuffleLocationSelector.LandsEndStarPiece1
    rooms = [519]
    event = 167


# *** Belome Temple

class BelomeTempleFortuneTeller(Chest):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleFortuneTeller
    rooms = [420]
    npc_ids = [5]
    event = 247
    item = items.Coins(Chest, 50)


class BelomeTempleFortune1(Chest):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleFortune1
    rooms = [421]
    npc_ids = [6]
    event = 247
    item = items.RecoveryMushroom
    access = 2


class BelomeTempleFortune2(Chest):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleFortune2
    rooms = [421]
    npc_ids = [7]
    event = 246
    item = items.YoshiCookie
    access = 2


class BelomeTempleFortune3(Chest):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleFortune3
    rooms = [421]
    npc_ids = [8]
    event = 245
    item = items.Flower
    access = 2


class BelomeTempleFortune4(Chest):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleFortune4
    rooms = [421]
    npc_ids = [9]
    event = 244
    item = items.Coins(Chest, 100)
    access = 2


class BelomeTempleAfterFortune1(Chest):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleAfterFortune1
    rooms = [425]
    npc_ids = [0]
    event = 247
    item = items.FrogCoin


class BelomeTempleAfterFortune2(Chest):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleAfterFortune2
    rooms = [425]
    npc_ids = [1]
    event = 246
    item = items.Coins(Chest, 150)


class BelomeTempleAfterFortune3(Chest):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleAfterFortune3
    rooms = [425]
    npc_ids = [2]
    event = 245
    item = items.FrogCoin


class BelomeTempleAfterFortune4(Chest):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleAfterFortune4
    rooms = [425]
    npc_ids = [3]
    event = 244
    item = items.FrogCoin


class BelomeTempleTreasureFlower1(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasureFlower1
    rooms = [422]
    npc_ids = [0]
    event = 241
    item = items.Flower
    access = 2


class BelomeTempleTreasureFlower2(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasureFlower2
    rooms = [422]
    npc_ids = [1]
    event = 240
    item = items.Flower
    access = 2


class BelomeTempleTreasureFlower3(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasureFlower3
    rooms = [422]
    npc_ids = [2]
    event = 239
    item = items.Flower
    access = 2


class BelomeTempleTreasureFlower4(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasureFlower4
    rooms = [422]
    npc_ids = [3]
    event = 238
    item = items.Flower
    access = 2


class BelomeTempleTreasureFrogCoin1(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasureFrogCoin1
    rooms = [422]
    npc_ids = [4]
    event = 237
    item = items.FrogCoin
    access = 2


class BelomeTempleTreasureFrogCoin2(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasureFrogCoin2
    rooms = [422]
    npc_ids = [5]
    event = 236
    item = items.FrogCoin
    access = 2


class BelomeTempleTreasureFrogCoin3(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasureFrogCoin3
    rooms = [422]
    npc_ids = [6]
    event = 235
    item = items.FrogCoin
    access = 2


class BelomeTempleTreasureFrogCoin4(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasureFrogCoin4
    rooms = [422]
    npc_ids = [7]
    event = 234
    item = items.FrogCoin
    access = 2


class BelomeTempleTreasureFrogCoin5(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasureFrogCoin5
    rooms = [422]
    npc_ids = [8]
    event = 233
    item = items.FrogCoin
    access = 2


class BelomeTempleTreasureFrogCoin6(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasureFrogCoin6
    rooms = [422]
    npc_ids = [9]
    event = 232
    item = items.FrogCoin
    access = 2


class BelomeTempleTreasureFrogCoin7(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasureFrogCoin7
    rooms = [422]
    npc_ids = [10]
    event = 231
    item = items.FrogCoin
    access = 2


class BelomeTempleTreasureFrogCoin8(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasureFrogCoin8
    rooms = [422]
    npc_ids = [11]
    event = 230
    item = items.FrogCoin
    access = 2


class BelomeTempleTreasure1(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasure1
    rooms = [422]
    npc_ids = [14]
    event = 228
    item = items.RoyalSyrup
    coinsanity = False
    access = 2


class BelomeTempleTreasure2(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasure2
    rooms = [422]
    npc_ids = [13]
    event = 229
    item = items.MaxMushroom
    coinsanity = False
    access = 2


class BelomeTempleTreasure3(BelomeTempleTreasure):
    area = locations.Area.BelomeTemple
    description = ShuffleLocationSelector.BelomeTempleTreasure3
    rooms = [422]
    npc_ids = [15]
    event = 227
    item = items.FireBomb
    coinsanity = False
    access = 2

class BelomeTempleBoss(BossStarPiece):
    description = ShuffleLocationSelector.BelomeTempleBoss
    area = locations.Area.BelomeTemple
    rooms = [268]
    event = 167



# *** Monstro Town

class MonstroTownEntrance(Chest):
    area = locations.Area.MonstroTown
    description = ShuffleLocationSelector.MonstroTownEntrance
    rooms = [267]
    npc_ids = [1]
    event = 257
    item = items.FrogCoin
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.MonstroTownGate, MonstroTownGating.AlwaysOpen):
            self.access = 1
    


class MonstroTownThwomp(OverworldItem):
    area = locations.Area.MonstroTown
    description = ShuffleLocationSelector.MonstroTownThwomp
    rooms = [324]
    event = 241
    npc_ids = [0]
    item = items.TempleKey
    key = True
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.MonstroTownGate, MonstroTownGating.AlwaysOpen):
            self.access = 1
    
    def item_allowed(self, item):
        if self.world.flags.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)


class JinxDojoReward(NPCReward):
    area = locations.Area.MonstroTown
    description = ShuffleLocationSelector.JinxDojoReward
    rooms = [255]
    event = 253
    item = items.JinxBelt
    access = 2
    special_equip = True

class DojoBoss1(BossStarPiece):
    description = ShuffleLocationSelector.DojoBoss1
    area = locations.Area.MonstroTown
    rooms = [255]
    event = 167

class DojoBoss2(BossStarPiece):
    description = ShuffleLocationSelector.DojoBoss2
    area = locations.Area.MonstroTown
    rooms = [515]
    event = 167

class DojoBoss3(BossStarPiece):
    description = ShuffleLocationSelector.DojoBoss3
    area = locations.Area.MonstroTown
    rooms = [516]
    event = 167


class DojoBoss4(BossStarPiece):
    description = ShuffleLocationSelector.DojoBoss4
    area = locations.Area.MonstroTown
    rooms = [517]
    event = 167


class CulexBoss(BossStarPiece):
    description = ShuffleLocationSelector.CulexBoss
    area = locations.Area.MonstroTown
    rooms = [351]
    event = 167


class CulexReward(NPCReward):
    area = locations.Area.MonstroTown
    description = ShuffleLocationSelector.CulexReward
    rooms = [351]
    event = 253
    item = items.QuartzCharm
    access = 2
    special_equip = True

    def can_access(self, inventory):
        if self.world.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.ShuffleFireworks):
            return inventory.has_item(items.ProgressiveFireworks) and inventory.has_item(items.BambinoBomb)
        elif self.world.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.ProgressiveFireworks):
            return inventory.has_item_count(items.ProgressiveFireworks, 2)
        else:
            return inventory.has_item(items.Fireworks) and inventory.has_item(items.BambinoBomb)



class SuperJumps30(NPCReward):
    area = locations.Area.MonstroTown
    description = ShuffleLocationSelector.SuperJumps30
    rooms = [397]
    event = 253
    item = items.AttackScarf
    access = 2
    special_equip = True
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.get_flag(flags.SuperJump1Threshold).value < 30:
            self.access = 1

    def can_access(self, inventory):
        return locations.can_super_jump(self, inventory)




class SuperJumps100(NPCReward):
    area = locations.Area.MonstroTown
    description = ShuffleLocationSelector.SuperJumps100
    rooms = [397]
    event = 252
    item = items.SuperSuit
    access = 2
    special_equip = True
    
    # you can lower it if you want, buuuut...
    def __init__(self, world):
        super().__init__(world)
        if world.settings.get_flag(flags.SuperJump2Threshold).value < 100:
            self.access = 1

    def can_access(self, inventory):
        return locations.can_super_jump(self, inventory)


class ThreeMustyFears(NPCReward):
    area = locations.Area.MonstroTown
    description = ShuffleLocationSelector.ThreeMustyFears
    rooms = [399]
    event = 253
    item = items.GhostMedal
    access = 2
    special_equip = True

    def can_access(self, inventory):
        return (inventory.has_item(items.BigBooFlag) and inventory.has_item(items.GreaperFlag) and
                inventory.has_item(items.DryBonesFlag))


# *** Bean Valley

class BeanValley1(StarAllowedChest):
    description = ShuffleLocationSelector.BeanValley1
    area = locations.Area.BeanValley
    rooms = [252]
    npc_ids = [3]
    event = 247
    item = items.Flower


class BeanValley2(StarAllowedChest):
    description = ShuffleLocationSelector.BeanValley2
    area = locations.Area.BeanValley
    rooms = [252]
    npc_ids = [4]
    event = 246
    item = items.FrogCoin


class BeanValleyLeftPiranhaPipe(StarAllowedChest):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyLeftPiranhaPipe
    rooms = [334]
    npc_ids = [0]
    event = 247
    item = items.SlotMachineChest


class BeanValleyBottomLeftPiranhaPipe(StarAllowedChest):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyBottomLeftPiranhaPipe
    rooms = [348]
    npc_ids = [0]
    event = 247
    item = items.SlotMachineChest


class BeanValleyBottomRightPiranhaPipeUpper(StarAllowedChest):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyBottomRightPiranhaPipeUpper
    rooms = [349]
    npc_ids = [0]
    event = 247
    item = items.SlotMachineChest


class BeanValleyBottomRightPiranhaPipeLower(StarAllowedChest):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyBottomRightPiranhaPipeLower
    rooms = [349]
    npc_ids = [2]
    event = 246
    item = items.KerokeroCola


class BeanValleyBoxBoyRoom1(StarAllowedChest):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyBoxBoyRoom1
    rooms = [335]
    npc_ids = [5]
    event = 247
    item = items.BoxBoyFight

class BoxBoyBoss(BossStarPiece):
    description = ShuffleLocationSelector.BoxBoyBoss
    rooms = [514]
    event = 167
    
    
    def can_access(self, inventory):
        return inventory.has_item(items.BoxBoyFight)


class BeanValleyBoxBoyRoom2(StarAllowedChest):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyBoxBoyRoom2
    rooms = [335]
    event = 246
    npc_ids = [7]
    item = items.RedEssence


class BeanValleyBoxBoyRoomHidden(NPCReward):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyBoxBoyRoomHidden
    rooms = [335]
    event = 253
    item = items.FrogCoin
    coinsanity = True


class BeanValleyPiranhaPlants(StarAllowedChest):
    description = ShuffleLocationSelector.BeanValleyPiranhaPlants
    area = locations.Area.BeanValley
    rooms = [251]
    npc_ids = [13]
    event = 247
    item = items.FrogCoin


class BeanValleyMegasmilaxRoom(NPCReward):
    description = ShuffleLocationSelector.BeanValleyMegasmilaxRoom
    area = locations.Area.BeanValley
    rooms = [254]
    event = 253
    item = items.Seed
    key = True
    access = 2
    
    def item_allowed(self, item):
        if self.world.flags.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)

class BeanValleyBoss(BossStarPiece):
    description = ShuffleLocationSelector.BeanValleyBoss
    area = locations.Area.BeanValley
    rooms = [254]
    event = 167


class BeanValleyBeanstalk(StarAllowedChest):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyBeanstalk
    rooms = [379]
    npc_ids = [0]
    event = 247
    item = items.Flower


class BeanValleyBeanstalkFrogCoin(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyBeanstalkFrogCoin
    rooms = [379]
    event = 241
    npc_ids = [6]
    item = items.FrogCoin


class BeanValleyBeanstalkCoin1(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyBeanstalkCoin1
    rooms = [379]
    event = 240
    npc_ids = [3]
    item = items.Coins10


class BeanValleyBeanstalkCoin2(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyBeanstalkCoin2
    rooms = [379]
    event = 239
    npc_ids = [4]
    item = items.Coins10


class BeanValleyBeanstalkCoin3(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyBeanstalkCoin3
    rooms = [379]
    event = 238
    npc_ids = [5]
    item = items.Coins10


class BeanValleyEastBeanstalkCoin1(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyEastBeanstalkCoin1
    rooms = [380]
    event = 241
    npc_ids = [3]
    item = items.Coins10


class BeanValleyEastBeanstalkCoin2(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyEastBeanstalkCoin2
    rooms = [380]
    event = 240
    npc_ids = [4]
    item = items.Coins10


class BeanValleyEastBeanstalkCoin3(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyEastBeanstalkCoin3
    rooms = [380]
    event = 239
    npc_ids = [5]
    item = items.Coins10


class BeanValleyEastBeanstalkCoin4(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyEastBeanstalkCoin4
    rooms = [380]
    event = 238
    npc_ids = [6]
    item = items.Coins10


class BeanValleyEastBeanstalkCoin5(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyEastBeanstalkCoin5
    rooms = [380]
    event = 237
    npc_ids = [7]
    item = items.Coins10


class BeanValleyWestBeanstalkCoin1(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyWestBeanstalkCoin1
    rooms = [381]
    event = 241
    npc_ids = [4]
    item = items.Coins10


class BeanValleyWestBeanstalkCoin2(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyWestBeanstalkCoin2
    rooms = [381]
    event = 240
    npc_ids = [5]
    item = items.Coins10


class BeanValleyWestBeanstalkCoin3(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyWestBeanstalkCoin3
    rooms = [381]
    event = 239
    npc_ids = [6]
    item = items.Coins10


class BeanValleyWestBeanstalkFrogCoin(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyWestBeanstalkFrogCoin
    rooms = [381]
    event = 238
    npc_ids = [7]
    item = items.FrogCoin


class BeanValleyCloud1(StarAllowedChest):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyCloud1
    rooms = [372]
    npc_ids = [1]
    event = 247
    item = items.FrogCoin
    access = 2


class BeanValleyCloud2(StarAllowedChest):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyCloud2
    rooms = [372]
    npc_ids = [2]
    event = 246
    item = items.RareScarf
    access = 2


class BeanValleyFall1(StarAllowedChest):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyFall1
    rooms = [373]
    npc_ids = [1]
    event = 247
    item = items.Flower
    access = 2


class BeanValleyFall2(StarAllowedChest):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyFall2
    rooms = [373]
    npc_ids = [2]
    event = 246
    item = items.Flower
    access = 2


class BeanValleyFirstVineRoomFrogCoin(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyFirstVineRoomFrogCoin
    rooms = [378]
    script = 241
    npc_ids = [3]
    item = items.FrogCoin


class BeanValleyFirstVineRoomMiddleCoin(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyFirstVineRoomMiddleCoin
    rooms = [378]
    script = 240
    npc_ids = [4]
    item = items.Coins10


class BeanValleyFirstVineRoomUpperCoin(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyFirstVineRoomUpperCoin
    rooms = [378]
    script = 239
    npc_ids = [5]
    item = items.Coins10


class BeanValleyFirstVineRoomLowerCoin(OverworldItem):
    area = locations.Area.BeanValley
    description = ShuffleLocationSelector.BeanValleyFirstVineRoomLowerCoin
    rooms = [378]
    script = 238
    npc_ids = [6]
    item = items.Coins10

# *** Grate Guy's Casino


class CasinoGrateGuyPrize(NPCReward):
    area = locations.Area.Casino
    description = ShuffleLocationSelector.CasinoGrateGuyPrize
    rooms = [92]
    event = 253
    item = items.StarEgg
    access = 2
    
    def can_access(self, inventory):
        return inventory.has_item(items.BrightCard)


# *** Nimbus Land

class NimbusLandShop(Chest):
    area = locations.Area.NimbusLand
    description = ShuffleLocationSelector.NimbusLandShop
    rooms = [344]
    npc_ids = [0]
    event = 247
    item = items.FrogCoin


class NimbusLandInn(NPCReward):
    area = locations.Area.NimbusLand
    description = ShuffleLocationSelector.NimbusLandInn
    shops = [346]
    script = 253
    item = items.RedEssence


class NimbusLandInn2(NPCReward):
    area = locations.Area.NimbusLand
    description = ShuffleLocationSelector.NimbusLandInn2
    shops = [346]
    script = 252
    item = items.RedEssence


class NimbusCastleBeforeBirdetta1(StarAllowedChest):
    description = ShuffleLocationSelector.NimbusCastleBeforeBirdetta1
    area = locations.Area.NimbusLand
    rooms = [118]
    npc_ids = [0]
    event = 247
    item = items.Flower
    missable = True


class NimbusCastleBeforeBirdetta2(StarAllowedChest):
    area = locations.Area.NimbusLand
    description = ShuffleLocationSelector.NimbusCastleBeforeBirdetta2
    rooms = [111, 500]
    npc_ids = [2, 0]
    event = 247
    item = items.Flower


class NimbusCastleBirdetta(NPCReward):
    area = locations.Area.NimbusLand
    description = ShuffleLocationSelector.NimbusCastleBirdetta
    rooms = [409]
    event = 253
    item = items.CastleKey2
    key = True
    access = 2
    
    def item_allowed(self, item):
        if self.world.flags.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)

    
    def can_access(self, inventory):
        return inventory.has_item(items.CastleKey1)

class NimbusCastleStarPiece2(BossStarPiece):
    description = ShuffleLocationSelector.NimbusCastleStarPiece2
    area = locations.Area.NimbusLand
    rooms = [409]
    event = 167
    access = 2
    
    def can_access(self, inventory):
        return inventory.has_item(items.CastleKey1)

class NimbusCastleOutOfBounds1(StarAllowedChest):
    area = locations.Area.NimbusLand
    description = ShuffleLocationSelector.NimbusCastleOutOfBounds1
    rooms = [410]
    npc_ids = [0]
    event = 247
    item = items.FrogCoin


class NimbusCastleOutOfBounds2(StarAllowedChest):
    area = locations.Area.NimbusLand
    description = ShuffleLocationSelector.NimbusCastleOutOfBounds2
    rooms = [410]
    npc_ids = [1]
    event = 246
    item = items.FrogCoin


class NimbusCastleSingleGoldBird(StarAllowedChest):
    area = locations.Area.NimbusLand
    description = ShuffleLocationSelector.NimbusCastleSingleGoldBird
    rooms = [113]
    npc_ids = [1]
    event = 247
    item = items.RecoveryMushroom


class NimbusCastleAfterEgg1(StarAllowedChest):
    description = ShuffleLocationSelector.NimbusCastleAfterEgg1
    area = locations.Area.NimbusLand
    rooms = [114, 498]
    npc_ids = [0, 0]
    event = 247
    item = items.Flower
    access = 2
    
    def can_access(self, inventory):
        return locations.can_clear_nimbus_castle(inventory)


class NimbusCastleAfterEgg2(StarAllowedChest):
    description = ShuffleLocationSelector.NimbusCastleAfterEgg2
    area = locations.Area.NimbusLand
    rooms = [114, 498]
    npc_ids = [1, 1]
    event = 246
    item = items.FrogCoin
    access = 2
    
    def can_access(self, inventory):
        return locations.can_clear_nimbus_castle(inventory)


class NimbusCastleStarPiece3(BossStarPiece):
    description = ShuffleLocationSelector.NimbusCastleStarPiece3
    area = locations.Area.NimbusLand
    rooms = [430]
    event = 167
    
    def can_access(self, inventory):
        return locations.can_clear_nimbus_castle(inventory)

class NimbusCastleStarChest(StarAllowedChest):
    description = ShuffleLocationSelector.NimbusCastleStarChest
    area = locations.Area.NimbusLand
    rooms = [121]
    npc_ids = [0]
    event = 247
    item = items.NimbusLandStar
    missable = True
    access = 2
    
    def can_access(self, inventory):
        return locations.can_clear_nimbus_castle(inventory)


class NimbusCastleStarAfterValentina(Chest):
    description = ShuffleLocationSelector.NimbusCastleStarAfterValentina
    area = locations.Area.NimbusLand
    rooms = [121]
    npc_ids = [1]
    event = 246
    item = items.Flower
    access = 2
    
    def can_access(self, inventory):
        return locations.can_clear_nimbus_castle(inventory)


class NimbusCastleCornerChestAfterValentina(Chest):
    description = ShuffleLocationSelector.NimbusCastleCornerChestAfterValentina
    area = locations.Area.NimbusLand
    rooms = [499]
    npc_ids = [0]
    event = 247
    item = items.FrogCoin
    access = 2
    
    def can_access(self, inventory):
        return locations.can_clear_nimbus_castle(inventory)


class NimbusLandRightSide(NPCReward):
    description = ShuffleLocationSelector.NimbusLandRightSide
    area = locations.Area.NimbusLand
    rooms = [438]
    event = 253
    item = items.Fertilizer
    key = True
    access = 2
    
    def item_allowed(self, item):
        if self.world.flags.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)

    
    def can_access(self, inventory):
        return locations.can_clear_nimbus_castle(inventory)


class DodoReward(NPCReward):
    description = ShuffleLocationSelector.DodoReward
    area = locations.Area.NimbusLand
    rooms = [110]
    event = 253
    item = items.Feather
    missable = True
    access = 2

class NimbusLandStarPiece1(BossStarPiece):
    description = ShuffleLocationSelector.NimbusLandStarPiece1
    area = locations.Area.NimbusLand
    rooms = [520]
    event = 167

class NimbusLandPrisoners(NPCReward):
    area = locations.Area.NimbusLand
    description = ShuffleLocationSelector.NimbusLandPrisoners
    rooms = [414]
    event = 253
    item = items.FlowerJar


class NimbusLandPrisoners2(NPCReward):
    area = locations.Area.NimbusLand
    description = ShuffleLocationSelector.NimbusLandPrisoners2
    rooms = [414]
    event = 252
    item = items.CastleKey1
    key = True
    
    def item_allowed(self, item):
        if self.world.flags.is_flag_value(flags.KeyItemsAnywhere, False):
            return super().item_allowed(item) and item.is_key
        return super().item_allowed(item)


class NimbusLandSignalRing(OverworldItem):
    area = locations.Area.NimbusLand
    description = ShuffleLocationSelector.NimbusLandSignalRing
    rooms = [345]
    npc_ids = [5]
    event = 241
    item = items.SignalRing
    coinsanity = False
    access = 2
    
    def can_access(self, inventory):
        return locations.can_clear_nimbus_castle(inventory)


class NimbusLandCellar(NPCReward):
    area = locations.Area.NimbusLand
    description = ShuffleLocationSelector.NimbusLandCellar
    rooms = [413]
    event = 253
    item = items.FlowerJar
    access = 2
    
    def can_access(self, inventory):
        return locations.can_clear_nimbus_castle(inventory)


# *** Barrel Volcano

class BarrelVolcanoSecret1(StarAllowedChest):
    area = locations.Area.BarrelVolcano
    description = ShuffleLocationSelector.BarrelVolcanoSecret1
    rooms = [355]
    npc_ids = [1]
    event = 247
    item = items.Flower
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BarrelVolcanoGate, BarrelVolcanoGating.AlwaysOpen):
            self.access = 1

    def can_access(self, inventory):
        return locations.can_access_volcano(self, inventory)


class BarrelVolcanoSecret2(StarAllowedChest):
    area = locations.Area.BarrelVolcano
    description = ShuffleLocationSelector.BarrelVolcanoSecret2
    rooms = [355]
    npc_ids = [2]
    event = 246
    item = items.Flower
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BarrelVolcanoGate, BarrelVolcanoGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_volcano(self, inventory)


class BarrelVolcanoReverse(OverworldItem):
    area = locations.Area.BarrelVolcano
    description = ShuffleLocationSelector.BarrelVolcanoReverse
    rooms = [383]
    event = 241
    npc_ids = [4]
    item = items.FrogCoin
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BarrelVolcanoGate, BarrelVolcanoGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_volcano(self, inventory)


class BarrelVolcanoDonut1(OverworldItem):
    area = locations.Area.BarrelVolcano
    description = ShuffleLocationSelector.BarrelVolcanoDonut1
    rooms = [358]
    event = 241
    item = items.FrogCoin
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BarrelVolcanoGate, BarrelVolcanoGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_volcano(self, inventory)


class BarrelVolcanoDonut2(OverworldItem):
    area = locations.Area.BarrelVolcano
    description = ShuffleLocationSelector.BarrelVolcanoDonut2
    rooms = [358]
    event = 240
    item = items.FrogCoin
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BarrelVolcanoGate, BarrelVolcanoGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_volcano(self, inventory)


class BarrelVolcanoLavaPool(OverworldItem):
    area = locations.Area.BarrelVolcano
    description = ShuffleLocationSelector.BarrelVolcanoLavaPool
    rooms = [361]
    event = 241
    item = items.FrogCoin
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BarrelVolcanoGate, BarrelVolcanoGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_volcano(self, inventory)


class BarrelVolcanoBeforeStar1(StarAllowedChest):
    area = locations.Area.BarrelVolcano
    description = ShuffleLocationSelector.BarrelVolcanoBeforeStar1
    rooms = [384]
    npc_ids = [0]
    event = 247
    item = items.Flower
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BarrelVolcanoGate, BarrelVolcanoGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_volcano(self, inventory)


class BarrelVolcanoBeforeStar2(StarAllowedChest):
    area = locations.Area.BarrelVolcano
    description = ShuffleLocationSelector.BarrelVolcanoBeforeStar2
    rooms = [384]
    npc_ids = [1]
    event = 246
    item = items.Coins(Chest, 100)
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BarrelVolcanoGate, BarrelVolcanoGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_volcano(self, inventory)


class BarrelVolcanoStarRoom(StarAllowedChest):
    area = locations.Area.BarrelVolcano
    description = ShuffleLocationSelector.BarrelVolcanoStarRoom
    rooms = [385]
    npc_ids = [0]
    event = 247
    item = items.LandsEndVolcanoStar
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BarrelVolcanoGate, BarrelVolcanoGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_volcano(self, inventory)


class BarrelVolcanoSaveRoom1(StarAllowedChest):
    area = locations.Area.BarrelVolcano
    description = ShuffleLocationSelector.BarrelVolcanoSaveRoom1
    rooms = [366]
    npc_ids = [0]
    event = 247
    item = items.Flower
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BarrelVolcanoGate, BarrelVolcanoGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_volcano(self, inventory)


class BarrelVolcanoSaveRoom2(StarAllowedChest):
    area = locations.Area.BarrelVolcano
    description = ShuffleLocationSelector.BarrelVolcanoSaveRoom2
    rooms = [366]
    npc_ids = [1]
    event = 246
    item = items.FrogCoin
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BarrelVolcanoGate, BarrelVolcanoGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_volcano(self, inventory)


class BarrelVolcanoHinopio(StarAllowedChest):
    area = locations.Area.BarrelVolcano
    description = ShuffleLocationSelector.BarrelVolcanoHinopio
    rooms = [367]
    npc_ids = [0]
    event = 247
    item = items.Coins(Chest, 100)
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BarrelVolcanoGate, BarrelVolcanoGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_volcano(self, inventory)

class BarrelVolcanoBoss1(BossStarPiece):
    description = ShuffleLocationSelector.BarrelVolcanoBoss1
    area = locations.Area.BarrelVolcano
    rooms = [352]
    event = 167
    
    def can_access(self, inventory):
        return locations.can_access_volcano(self, inventory)

class BarrelVolcanoBoss2(BossStarPiece):
    description = ShuffleLocationSelector.BarrelVolcanoBoss2
    area = locations.Area.BarrelVolcano
    rooms = [393]
    event = 167
    item = items.StarPiece
    
    def can_access(self, inventory):
        return locations.can_access_volcano(self, inventory)


# *** Bowser's Keep

class BowsersKeepDarkRoom(StarAllowedChest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepDarkRoom
    rooms = [453]
    npc_ids = [0]
    event = 247
    item = items.RecoveryMushroom
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepCrocoShop1(StarAllowedChest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCrocoShop1
    rooms = [451]
    npc_ids = [0]
    event = 247
    item = items.Coins(Chest, 150)
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepCrocoShop2(StarAllowedChest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCrocoShop2
    rooms = [451]
    npc_ids = [1]
    event = 246
    item = items.RecoveryMushroom
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepMagikoopa(Chest):
    description = ShuffleLocationSelector.BowsersKeepMagikoopa
    area = locations.Area.BowsersKeep
    rooms = [266]
    script = 247
    npc_ids = [0]
    item = items.InfiniteCoins
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepBossChester(BossStarPiece):
    description = ShuffleLocationSelector.BowsersKeepBossChester
    area = locations.Area.BowsersKeep
    rooms = [461]
    event = 167
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepBoss1(BossStarPiece):
    description = ShuffleLocationSelector.BowsersKeepBoss1
    area = locations.Area.BowsersKeep
    rooms = [266]
    event = 167
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepInvisibleBridge1(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepInvisibleBridge1
    rooms = [322]
    npc_ids = [4]
    script = 247
    item = items.FrightBomb
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepInvisibleBridge2(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepInvisibleBridge2
    rooms = [322]
    npc_ids = [5]
    script = 246
    item = items.RoyalSyrup
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepInvisibleBridge3(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepInvisibleBridge3
    rooms = [322]
    npc_ids = [6]
    script = 245
    item = items.IceBomb
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepInvisibleBridge4(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepInvisibleBridge4
    rooms = [322]
    npc_ids = [7]
    script = 244
    item = items.RockCandy
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepInvisibleBridgeCoin1(OverworldItem):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepInvisibleBridgeCoin1
    rooms = [322]
    script = 241
    npc_ids = [8]
    item = items.Coins10
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepInvisibleBridgeCoin2(OverworldItem):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepInvisibleBridgeCoin2
    rooms = [322]
    script = 240
    npc_ids = [9]
    item = items.Coins10
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepInvisibleBridgeCoin3(OverworldItem):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepInvisibleBridgeCoin3
    rooms = [322]
    script = 239
    npc_ids = [10]
    item = items.Coins10
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepInvisibleBridgeCoin4(OverworldItem):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepInvisibleBridgeCoin4
    rooms = [322]
    script = 238
    npc_ids = [11]
    item = items.Coins10
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepMovingPlatforms1(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepMovingPlatforms1
    rooms = [458]
    npc_ids = [10]
    event = 247
    item = items.Flower
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepMovingPlatforms2(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepMovingPlatforms2
    rooms = [458]
    npc_ids = [11]
    event = 246
    item = items.RedEssence
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepMovingPlatforms3(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepMovingPlatforms3
    rooms = [458]
    npc_ids = [12]
    event = 245
    item = items.MaxMushroom
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepMovingPlatforms4(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepMovingPlatforms4
    rooms = [458]
    npc_ids = [13]
    event = 244
    item = items.FireBomb
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepElevatorPlatforms(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepElevatorPlatforms
    rooms = [321]
    npc_ids = [8]
    script = 247
    item = items.KerokeroCola
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepCannonballRoom1(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoom1
    rooms = [457]
    npc_ids = [3]
    event = 247
    item = items.Flower
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepCannonballRoom2(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoom2
    rooms = [457]
    npc_ids = [4]
    event = 246
    item = items.Flower
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepCannonballRoom3(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoom3
    rooms = [457]
    npc_ids = [5]
    event = 245
    item = items.PickMeUp
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepCannonballRoom4(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoom4
    rooms = [457]
    npc_ids = [6]
    event = 244
    item = items.RockCandy
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepCannonballRoom5(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoom5
    rooms = [457]
    npc_ids = [7]
    event = 243
    item = items.MaxMushroom
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepCannonballRoomCoin1(OverworldItem):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoomCoin1
    rooms = [457]
    event = 241
    npc_ids = [8]
    item = items.Coins10
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepCannonballRoomCoin2(OverworldItem):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoomCoin2
    rooms = [457]
    event = 240
    npc_ids = [9]
    item = items.Coins10
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepCannonballRoomCoin3(OverworldItem):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoomCoin3
    rooms = [457]
    event = 239
    npc_ids = [10]
    item = items.Coins10
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepCannonballRoomCoin4(OverworldItem):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoomCoin4
    rooms = [457]
    event = 238
    npc_ids = [11]
    item = items.Coins10
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepCannonballRoomCoin5(OverworldItem):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoomCoin5
    rooms = [457]
    event = 237
    npc_ids = [12]
    item = items.Coins10
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepCannonballRoomCoin6(OverworldItem):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoomCoin6
    rooms = [457]
    event = 236
    npc_ids = [13]
    item = items.Coins10
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepCannonballRoomCoin7(OverworldItem):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoomCoin7
    rooms = [457]
    event = 235
    npc_ids = [14]
    item = items.Coins10
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepCannonballRoomCoin8(OverworldItem):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepCannonballRoomCoin8
    rooms = [457]
    event = 234
    npc_ids = [15]
    item = items.Coins10
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepRotatingPlatforms1(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepRotatingPlatforms1
    rooms = [455]
    npc_ids = [1]
    event = 247
    item = items.Flower
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepRotatingPlatforms2(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepRotatingPlatforms2
    rooms = [455]
    npc_ids = [2]
    event = 246
    item = items.Flower
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepRotatingPlatforms3(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepRotatingPlatforms3
    rooms = [455]
    npc_ids = [3]
    event = 245
    item = items.FireBomb
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepRotatingPlatforms4(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepRotatingPlatforms4
    rooms = [455]
    npc_ids = [4]
    event = 244
    item = items.RoyalSyrup
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepRotatingPlatforms5(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepRotatingPlatforms5
    rooms = [455]
    npc_ids = [5]
    event = 243
    item = items.PickMeUp
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepRotatingPlatforms6(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepRotatingPlatforms6
    rooms = [455]
    npc_ids = [6]
    event = 242
    item = items.KerokeroCola
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepDoorReward1(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepDoorReward1
    rooms = [144, 446]
    event = 247
    item = items.SonicCymbal
    manual_70A7 = True
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepDoorReward2(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepDoorReward2
    rooms = [144, 446]
    event = 246
    item = items.SuperSlap
    manual_70A7 = True
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepDoorReward3(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepDoorReward3
    rooms = [144, 446]
    event = 245
    item = items.DrillClaw
    manual_70A7 = True
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepDoorReward4(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepDoorReward4
    rooms = [144, 446]
    event = 244
    item = items.StarGun
    manual_70A7 = True
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepDoorReward5(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepDoorReward5
    rooms = [144, 446]
    event = 243
    item = items.RockCandy
    manual_70A7 = True
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepDoorReward6(Chest):
    area = locations.Area.BowsersKeep
    description = ShuffleLocationSelector.BowsersKeepDoorReward6
    rooms = [144, 446]
    event = 242
    item = items.RockCandy
    manual_70A7 = True
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


class BowsersKeepBoss2(BossStarPiece):
    description = ShuffleLocationSelector.BowsersKeepBoss2
    area = locations.Area.BowsersKeep
    rooms = [521]
    event = 167
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)

class BowsersKeepBoss3(BossStarPiece):
    description = ShuffleLocationSelector.BowsersKeepBoss3
    area = locations.Area.BowsersKeep
    rooms = [522]
    event = 167
    
    def can_access(self, inventory):
        return locations.can_access_keep(self, inventory)


# *** Factory

class FactorySaveRoom(StarAllowedChest):
    area = locations.Area.Factory
    description = ShuffleLocationSelector.FactorySaveRoom
    rooms = [237]
    npc_ids = [1]
    event = 247
    item = items.RecoveryMushroom
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.FactoryGate, FactoryGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_factory(self, inventory)


class FactoryBoltPlatforms(StarAllowedChest):
    area = locations.Area.Factory
    description = ShuffleLocationSelector.FactoryBoltPlatforms
    rooms = [239]
    npc_ids = [7]
    event = 247
    item = items.UltraHammer
    access = 2
    
    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.FactoryGate, FactoryGating.AlwaysOpen):
            self.access = 1
    
    def can_access(self, inventory):
        return locations.can_access_factory(self, inventory)


class FactoryBoss1(BossStarPiece):
    description = ShuffleLocationSelector.FactoryBoss1
    area = locations.Area.Factory
    rooms = [223]
    event = 167
    
    def can_access(self, inventory):
        return locations.can_access_factory(self, inventory)

class FactoryFallingAxems(StarAllowedChest):
    area = locations.Area.Factory
    description = ShuffleLocationSelector.FactoryFallingAxems
    rooms = [434]
    npc_ids = [6]
    event = 247
    item = items.RecoveryMushroom
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_factory(self, inventory)


class FactoryTreasurePit1(StarAllowedChest):
    area = locations.Area.Factory
    description = ShuffleLocationSelector.FactoryTreasurePit1
    rooms = [443]
    npc_ids = [0]
    event = 247
    item = items.RecoveryMushroom
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_factory(self, inventory)


class FactoryTreasurePit2(StarAllowedChest):
    area = locations.Area.Factory
    description = ShuffleLocationSelector.FactoryTreasurePit2
    rooms = [443]
    npc_ids = [2]
    event = 245
    item = items.Flower
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_factory(self, inventory)


class FactoryConveyorPlatforms1(StarAllowedChest):
    area = locations.Area.Factory
    description = ShuffleLocationSelector.FactoryConveyorPlatforms1
    rooms = [475]
    npc_ids = [8]
    event = 247
    item = items.RoyalSyrup
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_factory(self, inventory)


class FactoryConveyorPlatforms2(StarAllowedChest):
    area = locations.Area.Factory
    description = ShuffleLocationSelector.FactoryConveyorPlatforms2
    rooms = [475]
    npc_ids = [9]
    event = 246
    item = items.MaxMushroom
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_factory(self, inventory)


class FactoryBehindSnakes1(StarAllowedChest):
    area = locations.Area.Factory
    description = ShuffleLocationSelector.FactoryBehindSnakes1
    rooms = [443]
    npc_ids = [1]
    event = 246
    item = items.RecoveryMushroom
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_factory(self, inventory)


class FactoryBehindSnakes2(StarAllowedChest):
    area = locations.Area.Factory
    description = ShuffleLocationSelector.FactoryBehindSnakes2
    rooms = [443]
    npc_ids = [3]
    event = 244
    item = items.Flower
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_factory(self, inventory)

class FactoryBoss2(BossStarPiece):
    description = ShuffleLocationSelector.FactoryBoss2
    area = locations.Area.Factory
    rooms = [103]
    event = 167
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_factory(self, inventory)

class FactoryToadGift(NPCReward):
    area = locations.Area.Factory
    description = ShuffleLocationSelector.FactoryToadGift
    rooms = [406]
    event = 253
    item = items.RockCandy
    access = 2
    
    def can_access(self, inventory):
        return locations.can_access_factory(self, inventory)

class InnerFactoryBoss1(BossStarPiece):
    description = ShuffleLocationSelector.InnerFactoryBoss1
    area = locations.Area.Factory
    rooms = [469]
    event = 167
    
    def can_access(self, inventory):
        return locations.can_access_factory(self, inventory)

class InnerFactoryBoss2(BossStarPiece):
    description = ShuffleLocationSelector.InnerFactoryBoss2
    area = locations.Area.Factory
    rooms = [470]
    event = 167
    
    def can_access(self, inventory):
        return locations.can_access_factory(self, inventory)

class InnerFactoryBoss3(BossStarPiece):
    description = ShuffleLocationSelector.InnerFactoryBoss3
    area = locations.Area.Factory
    rooms = [471]
    event = 167
    
    def can_access(self, inventory):
        return locations.can_access_factory(self, inventory)

class InnerFactoryBoss4(BossStarPiece):
    description = ShuffleLocationSelector.InnerFactoryBoss4
    area = locations.Area.Factory
    rooms = [472]
    event = 167
    
    def can_access(self, inventory):
        return locations.can_access_factory(self, inventory)

class InnerFactoryBossFinal(BossStarPiece):
    description = ShuffleLocationSelector.InnerFactoryBossFinal
    area = locations.Area.Factory
    rooms = [496]
    event = 167
    
    def can_access(self, inventory):
        return locations.can_access_final_boss(self, inventory)



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
        HidonChest(world),
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
        InnerFactoryBoss4(world),
        InnerFactoryBossFinal(world)
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

def get_spotted_character_checks(world):
    """Get list of recruitable character locations.

    Args:
        world (randomizer.logic.main.GameWorld):

    Returns:
        list[ItemLocation]: List of recruitable character location objects..
    """
    return [
        MarrymoreCharacterSpotted(world)
    ]
