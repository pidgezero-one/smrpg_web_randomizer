# Data module for item/shop data.

import enum
import random
import math

from randomizer.data import items
from randomizer.data.items import ItemUnique
from randomizer.logic import utils
from randomizer.logic.patch import Patch
from randomizer.logic import flags
from randomizer.logic.flags import FireworksOptions, PlayableCharacters, SeaGating, BowsersKeepGating


# ************************** Shop data classes

class Shop:
    """Class representing a shop with a list of items."""
    BASE_ADDRESS = 0x3a44df

    # Default per-shop attributes.
    index = 0
    frog_coin_shop = False
    items = []
    retain_size = False
    forced_size = 0
    access = 1
    event_id = None

    def __init__(self, world):
        """

        Args:
            world (randomizer.logic.main.GameWorld):

        """
        self.world = world
        # Get actual item instances for this world.
        self.items = [world.get_item_instance(i) for i in self.items]

    def __str__(self):
        return "<{}: items {}>".format(self.name, self.items)

    def __repr__(self):
        return str(self)

    @property
    def name(self):
        return self.__class__.__name__

    @property
    def rank(self):
        """Rank for the shop based on highest priced item for balancing.

        :rtype: int
        """
        maxprice = max([i.price for i in self.items])
        if self.frog_coin_shop:
            maxprice += 2000
        return maxprice

    def get_patch(self):
        """Get patch for this shop.

        :return: Patch data.
        :rtype: randomizer.logic.patch.Patch
        """
        patch = Patch()
        base_addr = self.BASE_ADDRESS + (self.index * 16)

        data = bytearray()
        for item in self.items:
            data += utils.ByteField(item.index).as_bytes()

        # Fill out extra shop fields with no item value.
        while len(data) < 15:
            data += utils.ByteField(255).as_bytes()

        # First byte is shop flags, don't change those.  Put items one byte later.
        patch.add_data(base_addr + 1, data)

        return patch

    def is_item_allowed(self, item):
        """Check if an item is allowed in this shop given the game world.

        Args:
            item (Item):

        Returns:
            bool: True if item is allowed in this shop/world, False otherwise.

        """
        return True

class NPCShop:
    """Class representing an event-based shop with a list of items."""

    # Default per-shop attributes.
    items = []
    retain_size = True
    event_shop = False
    access = 1

    def __init__(self, world):
        """

        Args:
            world (randomizer.logic.main.GameWorld):

        """
        self.world = world
        # Get actual item instances for this world.
        self.items = [world.get_item_instance(i) for i in self.items]

    def __str__(self):
        return "<{}: items {}>".format(self.name, self.items)

    def __repr__(self):
        return str(self)

    @property
    def name(self):
        return self.__class__.__name__

    @property
    def rank(self):
        """Rank for the shop based on highest priced item for balancing.

        :rtype: int
        """
        maxprice = max([i.price for i in self.items])
        return maxprice

    def is_item_allowed(self, item):
        """Check if an item is allowed in this shop given the game world.

        Args:
            item (Item):

        Returns:
            bool: True if item is allowed in this shop/world, False otherwise.

        """
        return True


class JuiceBarShop(Shop):
    """Extra subclass to identify juice bar shops."""
    pass


class PartialJuiceBarShop(JuiceBarShop):
    pass


# **************** Actual shop classes

class MushroomKingdomShop(Shop):
    index = 0
    items = [items.Mushroom, items.HoneySyrup, items.PickMeUp, items.AbleJuice,
             items.Shirt, items.Pants, items.JumpShoes, items.AntidotePin]
    event_id = 284

    def is_item_allowed(self, item):
        """Check if an item is allowed in this shop given the game world.

        Args:
            item (Item):

        Returns:
            bool: True if item is allowed in this shop/world, False otherwise.

        """
        # For standard mode, make sure the first two characters can equip items.
        first_chars = set(
            [c.index for c in self.world.character_join_order[:2]])
        equip_chars = set([c.index for c in item.equip_chars])
        can_equip = self.world.open_mode or bool(equip_chars & first_chars)
        return item.consumable or ((item.is_armor or item.is_accessory) and can_equip)


class RoseTownItemShop(Shop):
    index = 1
    items = [items.Mushroom, items.HoneySyrup, items.PickMeUp, items.AbleJuice]
    event_id = 525

    def is_item_allowed(self, item):
        """Check if an item is allowed in this shop given the game world.

        Args:
            item (Item):

        Returns:
            bool: True if item is allowed in this shop/world, False otherwise.

        """
        return item.consumable


class RoseTownArmorShop(Shop):
    index = 2
    items = [items.ThickShirt, items.ThickPants, items.JumpShoes,
             items.AntidotePin, items.WakeUpPin, items.TrueformPin, items.FearlessPin]
    event_id = 526

    def is_item_allowed(self, item):
        """Check if an item is allowed in this shop given the game world.

        Args:
            item (Item):

        Returns:
            bool: True if item is allowed in this shop/world, False otherwise.

        """
        # For standard mode, make sure the first three characters can equip items.
        first_chars = set(
            [c.index for c in self.world.character_join_order[:3]])
        equip_chars = set([c.index for c in item.equip_chars])
        can_equip = self.world.open_mode or bool(equip_chars & first_chars)
        return (item.is_armor or item.is_accessory) and can_equip


class DiscipleShop(Shop):
    index = 3
    frog_coin_shop = True
    retain_size = True
    forced_size = 5
    items = [items.SeeYa, items.EarlierTimes, items.ExpBooster, items.CoinTrick, items.ScroogeRing]

    def is_item_allowed(self, item):
        return not utils.isclass_or_instance(item, (items.MimicFight, items.SlotMachineChest, items.Flower, items.YouMissed, items.InvincibilityStar, items.InfiniteCoins))    and not item.is_key and (item.is_equipment or item.unique == ItemUnique.Always or item.unique == ItemUnique.BalancedOnly)

class MolevilleShop(Shop):
    index = 4
    items = [items.PunchGlove, items.FingerShot, items.Cymbals, items.MegaShirt,
             items.MegaCape, items.MegaPants, items.WorkPants, items.MidMushroom, items.MapleSyrup]
    event_id = 1624

    def is_item_allowed(self, item):
        """Check if an item is allowed in this shop given the game world.

        Args:
            item (Item):

        Returns:
            bool: True if item is allowed in this shop/world, False otherwise.

        """
        # For standard mode, make sure the first three characters can equip items.
        first_chars = set(
            [c.index for c in self.world.character_join_order[:3]])
        equip_chars = set([c.index for c in item.equip_chars])
        can_equip = self.world.open_mode or bool(equip_chars & first_chars)
        return item.consumable or ((item.is_armor or item.is_weapon) and can_equip)


class MarrymoreShop(Shop):
    index = 5
    items = [items.SuperHammer, items.HandGun, items.WhompGlove, items.ChompShell, items.HappyShirt, items.HappyPants, items.HappyCape, items.HappyShell, items.BtubRing,
             items.MidMushroom, items.MapleSyrup]
    event_id = 646

    def is_item_allowed(self, item):
        return item.consumable or item.is_equipment


class FrogCoinEmporiumShop(Shop):
    index = 6
    frog_coin_shop = True
    items = [items.SleepyBomb, items.Bracer, items.Energizer, items.Crystalline, items.PowerBlast]
    event_id = 1112


class SeaShop(Shop):
    index = 7
    items = [items.HurlyGloves, items.SuperHammer, items.HandGun, items.WhompGlove, items.SailorShirt, items.SailorPants, items.SailorCape, items.NauticaDress,
             items.MidMushroom, items.MapleSyrup, items.PickMeUp, items.AbleJuice, items.FreshenUp]
    event_id = 3297

    def __init__(self, world):
        super().__init__(world)
        for option in [SeaGating.Find1Star, SeaGating.Find2Star, SeaGating.Find3Star, SeaGating.Find4Star, SeaGating.Find5Star, SeaGating.Find6Star]:
            if world.settings.is_flag_value(flags.SeaGate, option):
                self.access = 2

    def is_item_allowed(self, item):
        return item.consumable or (item.is_armor or item.is_weapon)


class SeasideYaridShop(Shop):
    index = 8
    items = [items.BadMushroom, items.MukuCookie, items.FrightBomb, items.FireBomb, items.IceBomb]
    event_id = 1140

    def is_item_allowed(self, item):
        """Check if an item is allowed in this shop given the game world.

        Args:
            item (Item):

        Returns:
            bool: True if item is allowed in this shop/world, False otherwise.

        """
        return item.consumable


class JuiceBarPartial1(PartialJuiceBarShop):
    index = 9
    items = [items.FroggieDrink]
    event_id = 1179


class JuiceBarPartial2(PartialJuiceBarShop):
    index = 10
    items = [items.FroggieDrink, items.Elixir]
    event_id = 1180


class JuiceBarPartial3(PartialJuiceBarShop):
    index = 11
    items = [items.FroggieDrink, items.Elixir, items.Megalixir]
    event_id = 1181


class JuiceBarFull(JuiceBarShop):
    index = 12
    items = [items.FroggieDrink, items.Elixir, items.Megalixir, items.KerokeroCola]
    access = 2
    event_id = 1182

    def is_item_allowed(self, item):
        """Check if an item is allowed in this shop given the game world.

        Args:
            item (Item):

        Returns:
            bool: True if item is allowed in this shop/world, False otherwise.

        """
        return item.consumable and not item.reuseable


class SeasideWeaponShop(Shop):
    index = 13
    access = 2
    items = [items.TroopaShell, items.Parasol, items.HurlyGloves, items.DoublePunch, items.RibbitStick, items.NokNokShell, items.PunchGlove, items.FingerShot, items.Cymbals,
             items.ChompShell, items.SuperHammer, items.HandGun, items.WhompGlove, items.SlapGlove, items.LuckyHammer]
    event_id = 1173

    def is_item_allowed(self, item):
        """Check if an item is allowed in this shop given the game world.

        Args:
            item (Item):

        Returns:
            bool: True if item is allowed in this shop/world, False otherwise.

        """
        return item.is_weapon


class SeasideArmorShop(Shop):
    index = 14
    access = 2
    items = [items.SailorShirt, items.SailorPants, items.SailorCape, items.NauticaDress, items.Shirt, items.Pants, items.ThickShirt, items.ThickPants, items.MegaShirt,
             items.MegaPants, items.MegaCape, items.HappyShirt, items.HappyPants, items.HappyCape, items.HappyShell]
    event_id = 1174

    def is_item_allowed(self, item):
        """Check if an item is allowed in this shop given the game world.

        Args:
            item (Item):

        Returns:
            bool: True if item is allowed in this shop/world, False otherwise.

        """
        return item.is_armor


class SeasideAccessoryShop(Shop):
    index = 15
    access = 2
    items = [items.JumpShoes, items.AntidotePin, items.WakeUpPin,
             items.FearlessPin, items.TrueformPin, items.ZoomShoes]
    event_id = 1171

    def is_item_allowed(self, item):
        """Check if an item is allowed in this shop given the game world.

        Args:
            item (Item):

        Returns:
            bool: True if item is allowed in this shop/world, False otherwise.

        """
        return item.is_accessory


class SeasideItemShop(Shop):
    index = 16
    access = 2
    items = [items.Mushroom, items.MidMushroom, items.HoneySyrup,
             items.MapleSyrup, items.PickMeUp, items.AbleJuice, items.FreshenUp]
    event_id = 1170

    def is_item_allowed(self, item):
        """Check if an item is allowed in this shop given the game world.

        Args:
            item (Item):

        Returns:
            bool: True if item is allowed in this shop/world, False otherwise.

        """
        return item.consumable


class MonstroTownShop(Shop):
    index = 17
    items = [items.SpikedLink, items.CourageShell, items.MidMushroom,
             items.MapleSyrup, items.PickMeUp, items.AbleJuice, items.FreshenUp]
    event_id = 2054

    def is_item_allowed(self, item):
        return item.consumable or (item.is_armor or item.is_weapon)


class HinopioItemShop(Shop):
    index = 18
    access = 2
    items = [items.MidMushroom, items.MapleSyrup, items.PickMeUp, items.AbleJuice, items.FreshenUp]
    event_id = 1183

    def is_item_allowed(self, item):
        """Check if an item is allowed in this shop given the game world.

        Args:
            item (Item):

        Returns:
            bool: True if item is allowed in this shop/world, False otherwise.

        """
        return item.consumable


class HinopioArmorShop(Shop):
    index = 19
    access = 2
    items = [items.FireShirt, items.FirePants, items.FireCape, items.FireShell, items.FireDress]
    event_id = 1184

    def is_item_allowed(self, item):
        """Check if an item is allowed in this shop given the game world.

        Args:
            item (Item):

        Returns:
            bool: True if item is allowed in this shop/world, False otherwise.

        """
        return item.is_armor


class BabyGoombaShop(Shop):
    index = 20
    items = [items.Mushroom2]
    event_id = 2053

    def is_item_allowed(self, item):
        """Check if an item is allowed in this shop given the game world.

        Args:
            item (Item):

        Returns:
            bool: True if item is allowed in this shop/world, False otherwise.

        """
        return item.consumable


class NimbusLandItemWeaponShop(Shop):
    index = 21
    items = [items.MidMushroom, items.MapleSyrup, items.PickMeUp, items.AbleJuice, items.FreshenUp, items.MegaGlove, items.WarFan, items.HandCannon, items.StickyGlove,
             items.FuzzyShirt, items.FuzzyPants, items.FuzzyCape, items.FuzzyDress]
    event_id = 3643

    def is_item_allowed(self, item):
        return item.consumable or (item.is_armor or item.is_weapon)


class CrocoShop1(Shop):
    index = 22
    items = [items.MidMushroom, items.MapleSyrup, items.PickMeUp, items.FreshenUp,
             items.FireShirt, items.FirePants, items.FireCape, items.FireShell, items.FireDress]
    event_id = 1862
    access = 2

    def __init__(self, world):
        super().__init__(world)
        if world.settings.is_flag_value(flags.BowsersKeepGate, BowsersKeepGating.AlwaysOpen):
            self.access = 1

    def is_item_allowed(self, item):
        return item.consumable or item.is_armor


class CrocoShop2(Shop):
    index = 23
    access = 2
    event_id = 1863
    items = [items.MidMushroom, items.MapleSyrup, items.PickMeUp, items.FreshenUp,
             items.HeroShirt, items.PrincePants, items.StarCape, items.HealShell, items.RoyalDress]

    def is_item_allowed(self, item):
        return item.consumable or item.is_armor


class ToadShop(Shop):
    index = 24
    access = 2
    event_id = 1185
    items = [items.MidMushroom, items.MaxMushroom, items.MapleSyrup,
             items.PickMeUp, items.AbleJuice, items.FreshenUp, items.FroggieDrink]

    def is_item_allowed(self, item):
        """Check if an item is allowed in this shop given the game world.

        Args:
            item (Item):

        Returns:
            bool: True if item is allowed in this shop/world, False otherwise.

        """
        return item.consumable


class RoomServiceShop(NPCShop):
    retain_size = True
    forced_size = 2
    event_shop = True
    access = 2
    event_id = 3688
    items = [items.PickMeUp, items.KerokeroCola]

    def is_item_allowed(self, item):
        """Check if an item is allowed in this shop given the game world.

        Args:
            item (Item):

        Returns:
            bool: True if item is allowed in this shop/world, False otherwise.

        """
        return item.consumable and not item.reuseable


class MolevilleSwapShop(NPCShop):
    retain_size = True
    forced_size = 3
    event_shop = True
    access = 2
    event_id = 1636
    items = [items.FrightBomb, items.FireBomb, items.IceBomb]

    def is_item_allowed(self, item):
        """Check if an item is allowed in this shop given the game world.

        Args:
            item (Item):

        Returns:
            bool: True if item is allowed in this shop/world, False otherwise.

        """
        return utils.isclass_or_instance(item, items.BadMushroom) or utils.isclass_or_instance(item, items.SleepyBomb) or utils.isclass_or_instance(item, items.FrightBomb) or utils.isclass_or_instance(item, items.FireBomb) or utils.isclass_or_instance(item, items.IceBomb) or utils.isclass_or_instance(item, items.RockCandy)

class MolevilleTreasureShop(NPCShop):
    retain_size = True
    forced_size = 3
    event_shop = True
    access = 2
    items = [items.LuckyJewel, items.ProgressiveEgg, items.FryingPan]

    def is_item_allowed(self, item):
        """Check if an item is allowed in this shop given the game world.

        Args:
            item (Item):

        Returns:
            bool: True if item is allowed in this shop/world, False otherwise.

        """
        return not utils.isclass_or_instance(item, (items.MimicFight, items.SlotMachineChest, items.Flower, items.YouMissed, items.InvincibilityStar, items.InfiniteCoins)) and (item.unique == ItemUnique.Always or item.unique == ItemUnique.BalancedOnly)

# ********************* Default shop lists for world


def get_default_shops(world):
    """

    Args:
        world (randomizer.logic.main.GameWorld):

    Returns:
        list[Shop]: Default list of items.

    """
    return [
        MushroomKingdomShop(world),
        RoseTownItemShop(world),
        RoseTownArmorShop(world),
        DiscipleShop(world),
        MolevilleShop(world),
        MarrymoreShop(world),
        FrogCoinEmporiumShop(world),
        SeaShop(world),
        SeasideYaridShop(world),
        JuiceBarPartial1(world),
        JuiceBarPartial2(world),
        JuiceBarPartial3(world),
        JuiceBarFull(world),
        SeasideWeaponShop(world),
        SeasideArmorShop(world),
        SeasideAccessoryShop(world),
        SeasideItemShop(world),
        MonstroTownShop(world),
        HinopioItemShop(world),
        HinopioArmorShop(world),
        BabyGoombaShop(world),
        NimbusLandItemWeaponShop(world),
        CrocoShop1(world),
        CrocoShop2(world),
        ToadShop(world),
    ]


def get_event_shops(world):
    """

    Args:
        world (randomizer.logic.main.GameWorld):

    Returns:
        list[Shop]: Default list of items.

    """
    return [
        RoomServiceShop(world),
        MolevilleSwapShop(world),
        MolevilleTreasureShop(world)
    ]
