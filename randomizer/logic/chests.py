# Chest randomization logic.

import math
import random
import enum
import copy

from scipy.stats import gamma

from randomizer.data import items, locations, chests
from randomizer.data.helpers import FireworksOptions, WinConditions, ItemQualities, ShopQualities, PlayableCharacters, BanditsWayGating, ForestMazeGating, BoosterTowerGating, SeaGating, ShuffleLocationSelector
from randomizer.data.items import ItemUnique
from randomizer.data.locations import Area
from randomizer.data.keys import KeyItemLocation
from randomizer.logic import flags, keys, utils

class RandomGrantEnum(enum.Enum):
    RegularItem = enum.auto()
    Equip = enum.auto()
    Coins = enum.auto()
    FrogCoins = enum.auto()
    Flower = enum.auto()
    RecoveryMushroom = enum.auto()
    SlotMachine = enum.auto()
    EXPStar = enum.auto()

chest_grant_table = [
    (2, RandomGrantEnum.SlotMachine),
    (8, RandomGrantEnum.RecoveryMushroom),
    (8, RandomGrantEnum.Flower),
    (8, RandomGrantEnum.FrogCoins),
    (8, RandomGrantEnum.Coins),
    (19, RandomGrantEnum.Equip),
    (37, RandomGrantEnum.RegularItem)
]

star_chest_grant_table = [
    (2, RandomGrantEnum.SlotMachine),
    (8, RandomGrantEnum.EXPStar),
    (8, RandomGrantEnum.RecoveryMushroom),
    (8, RandomGrantEnum.Flower),
    (8, RandomGrantEnum.FrogCoins),
    (8, RandomGrantEnum.Coins),
    (19, RandomGrantEnum.Equip),
    (39, RandomGrantEnum.RegularItem)
]

starter_grant_table = [
    (2, RandomGrantEnum.RegularItem)
]

shop_grant_table = [
    (2, RandomGrantEnum.Equip)
]

npc_grant_table = [
    (5, RandomGrantEnum.RecoveryMushroom),
    (10, RandomGrantEnum.FrogCoins),
    (5, RandomGrantEnum.Coins),
    (10, RandomGrantEnum.Equip),
    (20, RandomGrantEnum.RegularItem)
]

overworld_grant_table = [
    (5, RandomGrantEnum.RecoveryMushroom),
    (15, RandomGrantEnum.Flower),
    (15, RandomGrantEnum.FrogCoins),
    (55, RandomGrantEnum.Coins),
    (5, RandomGrantEnum.Equip),
    (5, RandomGrantEnum.RegularItem)
]

area_1 = [Area.MariosPad, Area.MushroomWay, Area.MushroomKingdom, Area.BanditsWay]
area_2 = [Area.KeroSewers, Area.MidasRiver, Area.TadpolePond, Area.RoseWay, Area.RoseTown, Area.RoseTownClouds, Area.ForestMaze, Area.PipeVault]
area_3 = [Area.Moleville, Area.MolevilleMines, Area.BoosterPass, Area.BoosterTower, Area.BoosterHill, Area.Marrymore]
area_4 = [Area.StarHill, Area.SeasideTown, Area.Sea, Area.SunkenShip]
area_5 = [Area.LandsEnd, Area.BelomeTemple, Area.MonstroTown, Area.Casino, Area.BeanValley]
area_6 = [Area.NimbusLand, Area.BarrelVolcano]
area_7 = [Area.BowsersKeep, Area.Factory, Area.InnerFactory]
area_8 = [Area.YosterIsle]

class Inventory(list):
    """List subclass for item inventory during key item shuffle logic."""

    def has_item_count(self, item, value = 1):
        """

        Args:
            item: Item class to check for.

        Returns:
            bool: True if inventory contains this item, False otherwise.

        """

        # this really should be illegal, I'm so sorry
        classes = [i for i in self if type(i) == type]
        instances = [i for i in self if isinstance(i, items.Item)]
        if type(item) == type:
            exists = [i for i in classes if item == i] + [i for i in instances if utils.isclass_or_instance(i, item)]
        else:
            exists = [i for i in classes if utils.isclass_or_instance(item, i)] + [i for i in instances if i == item]
        return len(exists) >= value

    def has_item(self, item):
        """

        Args:
            item: Item class to check for.

        Returns:
            bool: True if inventory contains this item, False otherwise.

        """

        return self.has_item_count(item, 1)


def _intershuffle_chests(chest_locations):
    """Shuffle the contents of the provided list of chests between each other.

    Args:
        chest_locations(list[randomizer.data.chests.Chest]):

    """
    chests_to_shuffle = chest_locations[:]
    random.shuffle(chests_to_shuffle)

    for chest in chests_to_shuffle:
        # Get other chests in this group that are able to swap items and pick one.
        options = [swap for swap in chest_locations if swap != chest and chest.item_allowed(swap.item) and
                   swap.item_allowed(chest.item)]
        if options:
            swap = random.choice(options)
            chest.item, swap.item = swap.item, chest.item


def _place_items(world, _items, locations, base_inventory=None, allow_replacements=True):
    # update this with get_item_instance
    """Place the given list of items within the given locations, and optionally a given starting inventory.

    Args:
        world (randomizer.logic.main.GameWorld):
        items (Inventory):
        locations (list[randomizer.data.locations.ItemLocation]):
        base_inventory (Inventory):

    """
    if base_inventory is None:
        base_inventory = Inventory()

    remaining_fill_items = Inventory(_items)

    # print("INITIAL_INVENTORY ", remaining_fill_items)

    # if len(remaining_fill_items) > len([l for l in locations if not l.has_item]):
    #    raise ValueError("Trying to fill more items than available locations")

    # For each required item, place it assuming we can get all other items.

    # Get items we can get assuming we have everything but the one we're placing.

    blocked_star_piece_areas = []

    item_loop = copy.copy(_items)

    #print(locations)
    #print(len(locations))
    #print(base_inventory)
    
    # Place best restricted equip 30% chance
    if world.settings.is_flag_value(flags.RestrictSpecialEquips, True):
        equips = [i for i in _items if i.special_equip]
        equips.sort(key=lambda x: x.rank_value, reverse=True) # use best item of the 10, to account for stat randomization
        jumps2_location_open = [l for l in locations if utils.isclass_or_instance(l, chests.SuperJumps100) and l.access == 2]
        if len(jumps2_location_open) > 0:
            bias = random.randint(1, 10)
            if bias <= 3:
                item = equips[0] 
                item_loop.remove(item)
                remaining_fill_items.remove(item)
                jumps2_location_open[0].item = item


    for item in item_loop:

        if type(item) == type:
            item = item(world)

        remaining_fill_items_without_this_item = copy.copy(remaining_fill_items)
        try:
            remaining_fill_items_without_this_item.remove(item)
        except:
            print(item, remaining_fill_items_without_this_item)
        assumed_items = _collect_items(
            world, remaining_fill_items_without_this_item + base_inventory)

        # print (item, [i for i in assumed_items if utils.isclass_or_instance(i, items.RecruitedCharacter)])


        #for l in locations:
        #    if utils.isclass_or_instance(l, chests.BanditsWay1):
        #        print (item, l.can_access(assumed_items))

        # filter down locations if eligible for biased shuffling
        # 80% chance that better items appear in locations with more gating, and vice versa
        if world.settings.is_flag_value(flags.RestrictSpecialEquips, True) and item.special_equip:
            fillable_locations = [l for l in locations if not l.has_item and l.can_access(assumed_items)
                            and l.item_allowed(item)]
        elif item.tier > 0 and not item.is_key and world.settings.is_flag_value(flags.BiasItemShuffle, True):
            if item.tier >= 3:
                chooser = random.randint(1, 10)
                if chooser > 2:
                    fillable_locations = [l for l in locations if not l.has_item and l.can_access(assumed_items)
                            and l.item_allowed(item) and l.access == 1]
                if chooser <= 2 or len(fillable_locations) == 0:
                    fillable_locations = [l for l in locations if not l.has_item and l.can_access(assumed_items)
                            and l.item_allowed(item) and l.access != 1]
            else:
                chooser = random.randint(1, 10)
                if chooser > 2:
                    fillable_locations = [l for l in locations if not l.has_item and l.can_access(assumed_items)
                            and l.item_allowed(item) and l.access >= 2]
                if chooser <= 2 or len(fillable_locations) == 0:
                    fillable_locations = [l for l in locations if not l.has_item and l.can_access(assumed_items)
                            and l.item_allowed(item) and l.access < 2]
        elif utils.isclass_or_instance(item, items.StarPiece):
            fillable_locations = [l for l in locations if not l.has_item and l.can_access(assumed_items)
                            and l.item_allowed(item) and not l.area in blocked_star_piece_areas]
        else:
            fillable_locations = [l for l in locations if not l.has_item and l.can_access(assumed_items)
                            and l.item_allowed(item)]
        # if star piece is blocked by world map restriction, loosen up on it
        if not fillable_locations and utils.isclass_or_instance(item, items.StarPiece):
            fillable_locations = [l for l in locations if not l.has_item and l.can_access(assumed_items)
                            and l.item_allowed(item)]
        
        #print (item, len(fillable_locations))
        # print(item, fillable_locations)
        if fillable_locations:

            # Prioritize frog shop and treasure seller since those are highly restrictive
            priority = [l for l in fillable_locations if utils.isclass_or_instance(l, chests.TreasureSellerReward) or utils.isclass_or_instance(l, chests.FrogCoinShopItem)]
            if len(priority) > 0:
                fillable_locations = priority

            #print(item, remaining_fill_items.index(item), len(remaining_fill_items), len(fillable_locations))
            #if remaining_fill_items.index(item) > 0:
            #    print("     ", item, remaining_fill_items)
            remaining_fill_items.remove(item)

            # Place item in the first fillable location.
            if allow_replacements and not(item.is_key or item.special_equip) and not(utils.isclass_or_instance(fillable_locations[0], chests.FrogCoinShopItem) or utils.isclass_or_instance(fillable_locations[0], chests.TreasureSellerReward))  and item.tier == 1 and item.price != 0 and world.settings.is_flag_value(flags.ReplaceItems, True):
                fillable_locations[0].item = items.Coins(world, item.price // 2)
            else:
                fillable_locations[0].item = item

            # Populate corresponding spotted character, if eligible (currently only affects Forest Maze access)
            if utils.isclass_or_instance(fillable_locations[0], chests.MarrymoreCharacter):
                if utils.isclass_or_instance(item, items.MarioRecruit):
                    spotted = items.MarioSpotted
                elif utils.isclass_or_instance(item, items.MallowRecruit):
                    spotted = items.MallowSpotted
                elif utils.isclass_or_instance(item, items.GenoRecruit):
                    spotted = items.GenoSpotted
                elif utils.isclass_or_instance(item, items.BowserRecruit):
                    spotted = items.BowserSpotted
                elif utils.isclass_or_instance(item, items.ToadstoolRecruit):
                    spotted = items.ToadstoolSpotted
                if spotted is not None:
                    set_item(world.spotted_character_checks, chests.MarrymoreCharacterSpotted, world.get_item_instance(spotted))
                    base_inventory.append(spotted)
            
            # Restrict star piece location eligibility if the proper flag is enabled
            if utils.isclass_or_instance(item, items.StarPiece) and world.settings.is_flag_value(flags.StarPiecesRestrictedByArea, True):
                if fillable_locations[0].area in area_1:
                    blocked_star_piece_areas.extend(area_1)
                elif fillable_locations[0].area in area_2:
                    blocked_star_piece_areas.extend(area_2)
                elif fillable_locations[0].area in area_3:
                    blocked_star_piece_areas.extend(area_3)
                elif fillable_locations[0].area in area_4:
                    blocked_star_piece_areas.extend(area_4)
                elif fillable_locations[0].area in area_5:
                    blocked_star_piece_areas.extend(area_5)
                elif fillable_locations[0].area in area_6:
                    blocked_star_piece_areas.extend(area_6)
                elif fillable_locations[0].area in area_7:
                    blocked_star_piece_areas.extend(area_7)
                elif fillable_locations[0].area in area_8:
                    blocked_star_piece_areas.extend(area_8)

            # if this is a mimic, set all chests dependent on that mimic to have the same area property as this chest
            # so that way we don't run the risk of violating StarPiecesRestrictedByArea by populating chests w/ unknown locations under MimicsAnywhere
            chests_missing_locations = []
            if utils.isclass_or_instance(item, items.PandoriteFight):
                chests_missing_locations = [c for c in world.chest_locations if utils.isclass_or_instance(c, chests.PandoriteReward1) or utils.isclass_or_instance(c, chests.PandoriteReward2) or utils.isclass_or_instance(c, chests.PandoriteBoss)]
            elif utils.isclass_or_instance(item, items.PandoriteFight):
                chests_missing_locations = [c for c in world.chest_locations if utils.isclass_or_instance(c, chests.HidonReward1) or utils.isclass_or_instance(c, chests.HidonReward2) or utils.isclass_or_instance(c, chests.HidonBoss)]
            elif utils.isclass_or_instance(item, items.BoxBoyFight):
                chests_missing_locations = [c for c in world.chest_locations if utils.isclass_or_instance(c, chests.BoxBoyBoss)]
            for c in chests_missing_locations:
                c.area = fillable_locations[0].area
        else:
            # print("")
            # print("")
            # print("")
            # print(item, locations)
            # print("")
            # print("")
            # print("")
            pass

    item_loop = Inventory(remaining_fill_items)
    # print("")
    # print("")
    # print("")
    # print("leftover: ", item_loop)
    # for l in locations:
    #     print(l)
    # print("")
    # print("")
    # print("")

    return remaining_fill_items



def _collect_items(world, collected=None):
    """Collect the available items in the world.

    Args:
        world (randomizer.logic.main.GameWorld): Game world
        collected (Inventory): Already collected items to start.

    Returns:
        Inventory: Collected items.

    """
    my_items = Inventory()
    if collected is not None:
        my_items.extend(collected)

    available_locations = []
    available_locations += [l for l in world.recruitable_character_checks if l.has_item]
    available_locations += [l for l in world.spotted_character_checks if l.has_item]
    available_locations += [l for l in world.starter_character_checks if l.has_item]
    available_locations += [l for l in world.chest_locations if l.has_item]
    available_locations += [l for l in world.freestanding_item_locations if l.has_item]
    available_locations += [l for l in world.boss_star_checks if l.has_item]

    # print(available_locations)
    # Search all locations and collect items until we can't get any more.
    while True:
        search_locations = [
            l for l in available_locations if l.can_access(my_items)]
        available_locations = [
            l for l in available_locations if l not in search_locations]
        found_items = Inventory([world.get_item_instance(l.item) for l in search_locations])
        my_items.extend(found_items)
        if len(found_items) == 0:
            break

    return my_items


def fill_locations(world, locations_to_fill, required_items, extra_items=None, existing_inventory=None):
    """Fill the given locations with the given required and extra items.

    Args:
        world (randomizer.logic.main.GameWorld): Game world to randomize.
        locations_to_fill (list[randomizer.data.locations.ItemLocation]): Locations to fill.
        required_items (Inventory): Required items to place.
        extra_items (Inventory): Extra items to place.

    """
    
    # Clear existing items to start.
    for location in locations_to_fill:
        location.item = None

    if extra_items is None:
        extra_items = Inventory()

    if existing_inventory is None:
        existing_inventory = Inventory()

    # Sanity check to make sure we're filling the right number of spots.
    # if len(locations_to_fill) < len(required_items) + len(extra_items):
    #     raise ValueError("Not enough locations for number of items.")

    # Remove prohibited star piece boss checks
    bosses_to_completely_ignore = world.settings.get_flag(flags.EnabledBossChecks).disabled
    if world.settings.is_flag_value(flags.WinCondition,WinConditions.factory):
        bosses_to_completely_ignore.append(ShuffleLocationSelector.InnerFactoryBossFinal)
    if world.settings.is_flag_value(flags.WinCondition,WinConditions.sealed):
        bosses_to_completely_ignore.append(ShuffleLocationSelector.CulexBoss)
    locations_to_fill = [l for l in locations_to_fill if l.description not in bosses_to_completely_ignore]

    # Shuffle locations, required items and extra items.
    random.shuffle(locations_to_fill)
    random.shuffle(required_items)
    random.shuffle(extra_items)

    remainder = []
    star_pieces = []

    # Fill required items. Keys, star pieces, characters, and important items that should only appear once.
    # With Progressive Fireworks, two of them should be in the general pool, so take care of that now.
    if world.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.progressive):
        required_items = [r for r in required_items if not utils.isclass_or_instance(r, items.ProgressiveFireworks)]
        required_items.extend([items.ProgressiveFireworks(world), items.ProgressiveFireworks(world), items.ProgressiveFireworks(world)])
    remainder = _place_items(world, required_items, locations_to_fill, existing_inventory, False)
    # Figure out what to do about remaining fireworks

    #print("placing required items...")
    # If any required items were left over (due to star piece shuffle, KIs anywhere, progressive fireworks, etc), handle them first
    locations_to_fill = [l for l in locations_to_fill if not l.has_item]
    remainder = _place_items(world, remainder, locations_to_fill, existing_inventory)
    #print("unplaced required items: ", remainder)
    if len([l for l in remainder if utils.isclass_or_instance(l, items.RecruitedCharacter)]) > 0:
        # try again in randomizer_all loop if characters could not be placed in a possible manner
        return remainder
    
    # Fill the rest of items
    # Tackle items that are not frog coins, flowers, or mushrooms first, in case we have more items than locations (may happen on Original Item Pool)
    regular_items = [i for i in extra_items if not utils.isclass_or_instance(i, items.Flower) and not utils.isclass_or_instance(i, items.RecoveryMushroom) and not utils.isclass_or_instance(i, items.FrogCoin)]
    expendable_items = [i for i in extra_items if utils.isclass_or_instance(i, items.Flower) or utils.isclass_or_instance(i, items.RecoveryMushroom) or utils.isclass_or_instance(i, items.FrogCoin)]

    # Reverse remaining empty locations, then fill extra items.
    locations_to_fill = [l for l in locations_to_fill if not l.has_item]
    locations_to_fill.reverse()
    # Prioritize frog shop and treasure seller since those are highly restrictive
    priority = [l for l in locations_to_fill if utils.isclass_or_instance(l, chests.TreasureSellerReward) or utils.isclass_or_instance(l, chests.FrogCoinShopItem)]
    locations_to_fill = [l for l in locations_to_fill if l not in priority]
    locations_to_fill = priority + locations_to_fill

    _place_items(world, regular_items, locations_to_fill, existing_inventory)
    # Rest of spots can be filled up with as many flowers/mushrooms/frog coins as we have available
    # This will likely not be a concern outside of Original Item Pool
    _place_items(world, expendable_items, locations_to_fill, existing_inventory)

    # If we have items left over, return them. Calling function will raise an error if leftover items are important
    collected_items = set(_collect_items(world))
    leftover = set(required_items + star_pieces + extra_items) - collected_items
    return leftover


def set_item(collection, location, item):
    for i in range(len(collection)):
        if utils.isclass_or_instance(collection[i], location):
            collection[i].item = item

def get_max_item_quality(world):
    tiers_allowed = 1
    if world.settings.is_flag_value(flags.ItemQuality, ItemQualities.t1):
        tiers_allowed = 4
    elif world.settings.is_flag_value(flags.ItemQuality, ItemQualities.t2):
        tiers_allowed = 3
    elif world.settings.is_flag_value(flags.ItemQuality, ItemQualities.t3):
        tiers_allowed = 2
    return tiers_allowed

def generate_nonrequired_item(world, table, chest):

    max_tier = get_max_item_quality(world)
    weights, possible_options = list(zip(*table))
    result = random.choices(possible_options, weights=weights, k=1)[0]
    if result == RandomGrantEnum.SlotMachine:
        item = world.get_item_instance(items.SlotMachineChest)
    elif result == RandomGrantEnum.RecoveryMushroom:
        item = world.get_item_instance(items.RecoveryMushroom)
    elif result == RandomGrantEnum.Flower:
        item = world.get_item_instance(items.Flower)
    elif result == RandomGrantEnum.EXPStar:
        all_choices = [world.get_item_instance(i) for i in [items.BanditsWayStar, items.KeroSewersStar, items.MolevilleMinesStar, items.SeaStar, items.LandsEndVolcanoStar, items.LandsEndVolcanoStar, items.NimbusLandStar, items.LandsEndStar2, items.LandsEndStar3]]
        item = random.choice(all_choices)(world)
    elif result == RandomGrantEnum.Coins:
        if utils.isclass_or_instance(chest, chests.OverworldItem):
            rand = random.randint(1, 10)
            if rand > 3:
                item = world.get_item_instance(items.Coins10)
            else:
                item = world.get_item_instance(items.Coins1)
        else:
            value = gamma.rvs(80, size=1)[0] // 1
            item = items.Coins(world, value)
    elif result == RandomGrantEnum.FrogCoins:
        if utils.isclass_or_instance(chest, chests.OverworldItem):
            item = world.get_item_instance(items.FrogCoin)
        else:
            rand = random.randint(1, 10)
            if rand > 1:
                item = world.get_item_instance(items.FrogCoin)
            else:
                possibilities = [2, 3, 4, 5, 6, 7, 8, 9, 10]
                value = random.choices(possibilities, weights=(10, 9, 8, 7, 6, 5, 4, 3, 2), k=1)[0]
                item = items.MultiFrogCoin(world, value)
    elif result == RandomGrantEnum.Equip or result == RandomGrantEnum.RegularItem:
        if result == RandomGrantEnum.Equip:
            all_choices = [i for i in world.items if (i.unique == ItemUnique.Never or (i.unique == ItemUnique.BalancedOnly and not world.settings.is_flag_value(flags.ItemQuality, ItemQualities.original))) and i.is_equipment and i.tier >= max_tier]
        else:
            all_choices = [i for i in world.items if (i.unique == ItemUnique.Never or (i.unique == ItemUnique.BalancedOnly and not world.settings.is_flag_value(flags.ItemQuality, ItemQualities.original))) and i.tier >= max_tier]
        if utils.isclass_or_instance(chest, chests.TreasureSellerReward):
            all_choices = [i for i in all_choices if i.unique == ItemUnique.BalancedOnly]
        possibilities = [1, 2, 3, 4, 5]
        if world.settings.is_flag_value(flags.BiasItemShuffle, True):
            if chest.access == 1:
                weights=[3, 10, 30, 35, 22]
            elif chest.access == 2:
                weights=[5, 20, 40, 25, 10]
            elif chest.access == 4:
                weights=[100, 0, 0, 0, 0]
        else:
            weights=[10, 20, 40, 20, 10]
        possibilities = possibilities[max_tier-1:]
        weights = tuple(weights[max_tier-1:])
        choices = []
        while len(choices) == 0:
            # is it possible for this to loop infinitely?
            value = random.choices(possibilities, weights, k=1)[0]
            choices = [i for i in all_choices if i.tier == value]
        item = random.choice(choices)
        # print(possibilities, weights, value, item, item.tier)
    else:
        raise Exception("couldn't place a randomly generated item at %r" % chest)
    return item

def randomize_all(world):
    """

    Args:
        world (randomizer.logic.main.GameWorld): Game world to randomize.

    """


    # Open mode-specific shuffles.
    if world.open_mode:

        # Collect pool of locations that need item assignments
        locations_to_completely_ignore = world.settings.get_flag(flags.EnabledFreestandingChecks).disabled

        inventory = Inventory([])

        # Contents of excluded chests will still be shuffled, they just will not contain progression items.
        # Excluded freestanding items will remain vanilla.
        # Excluded boss checks will receive "None"
        # Character locations cannot be excluded, but will receive "None" if unassigned
        if world.settings.is_flag_enabled(flags.ShuffleItems):
            all_locations = world.chest_locations.copy() + [c for c in world.freestanding_item_locations if c.description not in locations_to_completely_ignore] + world.boss_star_checks.copy() + world.recruitable_character_checks.copy() + world.spotted_character_checks.copy()
        else:
            all_locations = world.boss_star_checks.copy() + world.recruitable_character_checks.copy() + world.spotted_character_checks.copy()
        # remove unused checks
        # bucket girl
        if world.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.vanilla) or world.settings.is_flag_value(flags.BucketWarp, True):
            all_locations = [a for a in all_locations if not utils.isclass_or_instance(a, chests.BucketGirl)]
        # fireworks shuffle
        if world.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.vanilla):
            all_locations = [a for a in all_locations if not utils.isclass_or_instance(a, chests.FireworksShop)]
            #inventory.append(items.Fireworks(world))
        # beetlemania shuffle
        if world.settings.is_flag_value(flags.ShuffleBeetlemania, False):
            all_locations = [a for a in all_locations if not utils.isclass_or_instance(a, chests.MushroomKingdomInn)]
            #inventory.append(items.Beetlemania(world))
        # magikoopa's chest shuffle
        if world.settings.is_flag_value(flags.ShuffleMagikoopaChest, False):
            all_locations = [a for a in all_locations if not utils.isclass_or_instance(a, chests.BowsersKeepMagikoopa)]
            #inventory.append(items.InfiniteCoins(world))
        # mimics shuffle
        if world.settings.is_flag_value(flags.MimicsAnywhere, False):
            all_locations = [a for a in all_locations if not utils.isclass_or_instance(a, chests.PandoriteChest) and not utils.isclass_or_instance(a, chests.HidonChest) and not utils.isclass_or_instance(a, chests.BeanValleyBoxBoyRoom1)]
            #inventory.extend([items.PandoriteFight(world), items.HidonFight(world), items.BoxBoyFight(world)])
        # slots shuffle
        if world.settings.is_flag_value(flags.SlotsAnywhere, False):
            all_locations = [a for a in all_locations if not utils.isclass_or_instance(a, chests.BeanValleyLeftPiranhaPipe) and not utils.isclass_or_instance(a, chests.BeanValleyBottomLeftPiranhaPipe) and not utils.isclass_or_instance(a, chests.BeanValleyBottomRightPiranhaPipeUpper)]
            #inventory.extend([items.SlotMachineChest(world), items.SlotMachineChest(world), items.SlotMachineChest(world)])
        # exp stars shuffle
        if world.settings.is_flag_value(flags.EXPStarsAnywhere, False):
            #inventory.extend([c.item for c in all_locations if utils.isclass_or_instance(c.item, items.InvincibilityStar)])
            all_locations = [a for a in all_locations if not utils.isclass_or_instance(a, chests.BanditsWayStarChest) and not utils.isclass_or_instance(a, chests.KeroSewersStarChest) and not utils.isclass_or_instance(a, chests.MolevilleMinesStarChest) and not utils.isclass_or_instance(a, chests.SeaStarChest) and not utils.isclass_or_instance(a, chests.LandsEndStarChest1) and not utils.isclass_or_instance(a, chests.LandsEndStarChest2) and not utils.isclass_or_instance(a, chests.LandsEndStarChest3) and not utils.isclass_or_instance(a, chests.NimbusCastleStarChest) and not utils.isclass_or_instance(a, chests.BarrelVolcanoStarRoom)]
        # star piece shuffle
        if world.settings.is_flag_value(flags.ShuffleStarPieces, False):
            #inventory.extend([c.item for c in all_locations if utils.isclass_or_instance(c.item, items.StarPiece)])
            all_locations = [a for a in all_locations if not utils.isclass_or_instance(a, chests.BossStarPiece)]
        # remove frog disciple checks and treasure seller if shop shuffle is off or if shops empty
        if world.settings.is_flag_value(flags.ShuffleShops, False) or world.settings.is_flag_value(flags.ShopQuality, ShopQualities.empty):
            #inventory.extend([c.item for c in all_locations if utils.isclass_or_instance(c, chests.FrogCoinShopItem)])
            #inventory.extend([c.item for c in all_locations if utils.isclass_or_instance(c, chests.TreasureSellerReward)])
            all_locations = [a for a in all_locations if not utils.isclass_or_instance(a, chests.FrogCoinShopItem) and not utils.isclass_or_instance(a, chests.TreasureSellerReward)]
        all_locations = [a for a in all_locations if not utils.isclass_or_instance(a, chests.CharacterSpotted)]
        
        # populate starting characters
        number_of_starting_characters = world.settings.get_flag(flags.StartingCharacters).value
        starting_party = [None]*5
        allCharacters = [PlayableCharacters.mario, PlayableCharacters.mallow,
                        PlayableCharacters.geno, PlayableCharacters.bowser, PlayableCharacters.toadstool]
        charactersInSeed = [c for c in allCharacters if c in world.settings.get_flag(
            flags.AvailableCharacters).enabled]
        # throw error if any required chars are excluded
        if PlayableCharacters.mario in world.settings.get_flag(flags.AvailableCharacters).disabled and (world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.mario) or world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.mario) or world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.mario) or world.settings.is_flag_value(flags.SeaGate, SeaGating.mario)):
            raise Exception('cannot exclude Mario when required for area access')
        if PlayableCharacters.mallow in world.settings.get_flag(flags.AvailableCharacters).disabled and (world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.mallow) or world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.mallow) or world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.mallow) or world.settings.is_flag_value(flags.SeaGate, SeaGating.mallow)):
            raise Exception('cannot exclude Mallow when required for area access')
        if PlayableCharacters.geno in world.settings.get_flag(flags.AvailableCharacters).disabled and (world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.geno) or world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.geno) or world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.geno) or world.settings.is_flag_value(flags.SeaGate, SeaGating.geno)):
            raise Exception('cannot exclude Geno when required for area access')
        if PlayableCharacters.bowser in world.settings.get_flag(flags.AvailableCharacters).disabled and (world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.bowser) or world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.bowser) or world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.bowser) or world.settings.is_flag_value(flags.SeaGate, SeaGating.bowser)):
            raise Exception('cannot exclude Bowser when required for area access')
        if PlayableCharacters.toadstool in world.settings.get_flag(flags.AvailableCharacters).disabled and (world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.toadstool) or world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.toadstool) or world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.toadstool) or world.settings.is_flag_value(flags.SeaGate, SeaGating.toadstool)):
            raise Exception('cannot exclude Toadstool when required for area access')
        # throw error if not enough chars to fill desired party
        if len(charactersInSeed) < number_of_starting_characters:
            raise Exception('not enough characters to fill desired starting party')
        random.shuffle(charactersInSeed)
        starter = world.settings.get_flag(flags.StartingCharacter).value
        if starter != PlayableCharacters.random:
            charactersInSeed = [c for c in charactersInSeed if c != starter]
            charactersInSeed.insert(0, starter)
        starting_characters = charactersInSeed[:number_of_starting_characters]
        for i in range(len(starting_characters)):
            starting_party[i] = starting_characters[i]
        # set starters
        for i in range(len(starting_characters)):
            if i == 0:
                location = chests.StarterCharacter1
            elif i == 1:
                location = chests.StarterCharacter2
            elif i == 2:
                location = chests.StarterCharacter3
            elif i == 3:
                location = chests.StarterCharacter4
            elif i == 4:
                location = chests.StarterCharacter5
            else:
                raise Exception("invalid starter character index %i" % i)
            if starting_characters[i] == PlayableCharacters.mario:
                character = items.MarioRecruit
            elif starting_characters[i] == PlayableCharacters.mallow:
                character = items.MallowRecruit
            elif starting_characters[i] == PlayableCharacters.geno:
                character = items.GenoRecruit
            elif starting_characters[i] == PlayableCharacters.bowser:
                character = items.BowserRecruit
            elif starting_characters[i] == PlayableCharacters.toadstool:
                character = items.ToadstoolRecruit
            else:
                raise Exception("invalid character %r" % starting_characters[i])
            character = world.get_item_instance(character)
            set_item(world.starter_character_checks, location, character)
            inventory.append(character)

        remainder = []

        # will this work? combining classes and instances?
        # Collect required base item pool
        # key items + characters
        required_item_pool = [i for i in world.items if i.is_key] + [world.get_item_instance(char) for char in [items.MarioRecruit, items.MallowRecruit, items.GenoRecruit, items.BowserRecruit, items.ToadstoolRecruit] if char.description in [c for c in charactersInSeed if c not in starting_characters]]
        # add star pieces
        if world.settings.is_flag_value(flags.ShuffleStarPieces, True):
            total_star_pieces = world.settings.get_flag(flags.TotalStarPieces).value
            star_pieces = [world.get_item_instance(s) for s in [items.StarPiece1, items.StarPiece2, items.StarPiece3, items.StarPiece4, items.StarPiece5, items.StarPiece6, items.StarPiece7]]
            required_item_pool += (star_pieces[0:total_star_pieces])
        # apply fireworks settings
        if world.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.shuffle1):
            required_item_pool.append(world.get_item_instance(items.Fireworks))
        elif world.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.progressive):
            # put one in required pool, sort two more into random locations after
            required_item_pool.extend([world.get_item_instance(items.ProgressiveFireworks)] * 3)


        extra_item_pool = []
        # non-key items which should always only appear up to a certain # of times
        # bright card, if not a KI
        if world.settings.is_flag_value(flags.CasinoWarp, False):
            required_item_pool.append(world.get_item_instance(items.BrightCard))
        # beetlemania
        if world.settings.is_flag_value(flags.ShuffleBeetlemania, True):
            required_item_pool.append(world.get_item_instance(items.Beetlemania))
        # mimics anywhere
        if world.settings.is_flag_value(flags.MimicsAnywhere, True):
            required_item_pool += [world.get_item_instance(f) for f in [items.PandoriteFight, items.HidonFight, items.BoxBoyFight]]
        # if Restrict Special Equips is on, must guarantee all ten appear once
        if world.settings.is_flag_value(flags.RestrictSpecialEquips, True):
            required_item_pool += [i for i in world.items if i.special_equip]
        # if star piece hints is on, must guarantee signal ring
        if world.settings.is_flag_value(flags.StarPieceHints, True):
            required_item_pool.append(world.get_item_instance(items.SignalRing))
        # other items
        if not world.settings.is_flag_value(flags.ItemQuality, ItemQualities.empty):
            if world.settings.is_flag_value(flags.ShuffleShops, False) and not world.settings.is_flag_value(flags.ShopQuality, ShopQualities.empty):
                # add 2 progressive eggs if one is guaranteed in treasure shop
                required_item_pool += ([world.get_item_instance(items.ProgressiveEgg)] * 2)
            else:
                # add 3 otherwise
                required_item_pool += ([world.get_item_instance(items.ProgressiveEgg)] * 3)
            # magikoopa's chest shuffle
            if world.settings.is_flag_value(flags.ShuffleMagikoopaChest, True):
                required_item_pool.append(world.get_item_instance(items.InfiniteCoins))
            limited_items = [world.get_item_instance(i) for i in [items.GoodieBag, items.YouMissed, items.SeeYa, items.EarlierTimes, items.StarEgg, items.Wallet, items.LuckyJewel]]
            max_tier = get_max_item_quality(world)
            required_item_pool += [i for i in limited_items if i.tier <= max_tier]

        # balanced only: populate extra_item_pool with existing item pool
        if world.settings.is_flag_value(flags.ItemQuality, ItemQualities.original):
            filtered = [world.get_item_instance(c.item) for c in all_locations if c.item is not None and c.item.index not in [i.index for i in required_item_pool + extra_item_pool + inventory if i is not None]]
            unique_balanced = [i for i in filtered if filtered.count(i) == 1]
            required_item_pool += unique_balanced
            extra_item_pool += [i for i in filtered if i not in unique_balanced]

        # sanitize
        for index, r in enumerate(required_item_pool):
            if type(r) == type:
                required_item_pool[index] = r(world)
        for index, r in enumerate(extra_item_pool):
            if type(r) == type:
                extra_item_pool[index] = r(world)

        remainder_check = copy.copy(required_item_pool)


        #print("items: ", len([i for i in required_item_pool + extra_item_pool if not(utils.isclass_or_instance(i, items.StarPiece) or utils.isclass_or_instance(i, items.RecruitedCharacter))]))
        #print("locations: ", len([i for i in all_locations if not(utils.isclass_or_instance(i, chests.BossStarPiece) or utils.isclass_or_instance(i, chests.CharacterRecruit))]))

        #print([i for i in all_locations if utils.isclass_or_instance(i, chests.InvisibleFlagLocation)])
        # keep rolling until characters are placed in a logically completable way
        while True:
            remainder = fill_locations(world, copy.copy(all_locations), copy.copy(required_item_pool), copy.copy(extra_item_pool), copy.copy(inventory))
            if len([i for i in remainder if utils.isclass_or_instance(i, items.RecruitedCharacter)]) == 0:
                break

        if remainder:
            excluded_important_items = [i for i in remainder if i.is_key or i in remainder_check or utils.isclass_or_instance(i, items.RecruitedCharacter)]
            if len(excluded_important_items) > 0:
                raise ValueError("Items were not placed: {!r}".format(
                    excluded_important_items))


        # next step: fill empty grants, if any, with randomly generated items
        all_remaining_locations = [a for a in all_locations if not a.has_item and (utils.isclass_or_instance(a, chests.Chest) or utils.isclass_or_instance(a, chests.NPCReward) or utils.isclass_or_instance(a, chests.OverworldItem))]
        
        
        for chest in all_remaining_locations:
            if world.settings.is_flag_value(flags.ItemQuality, ItemQualities.empty):
                if not utils.isclass_or_instance(chest, chests.FrogCoinShopItem):
                    chest.item = world.get_item_instance(items.Nothing)
                else:
                    chest.item = world.get_item_instance(items.GoodieBag)
            else:
                item = None
                if utils.isclass_or_instance(chest, chests.StarAllowedChest):
                    item = generate_nonrequired_item(world, star_chest_grant_table, chest)
                elif utils.isclass_or_instance(chest, chests.Chest):
                    item = generate_nonrequired_item(world, chest_grant_table, chest)
                elif utils.isclass_or_instance(chest, chests.StarterItem):
                    item = generate_nonrequired_item(world, starter_grant_table, chest)
                elif utils.isclass_or_instance(chest, chests.TreasureSellerReward) or utils.isclass_or_instance(chest, chests.FrogCoinShopItem):
                    item = generate_nonrequired_item(world, shop_grant_table, chest)
                elif utils.isclass_or_instance(chest, chests.NPCReward):
                    item = generate_nonrequired_item(world, npc_grant_table, chest)
                elif utils.isclass_or_instance(chest, chests.OverworldItem):
                    item = generate_nonrequired_item(world, overworld_grant_table, chest)
                if item:
                    if item.tier == 5 and item.price != 0 and world.settings.is_flag_value(flags.ReplaceItems, True):
                        item = items.Coins(world, item.price // 2)
                    chest.item = item
                # Ignore empty boss locations and empty character recruit locations, those SHOULD be empty if they don't receive an item
            #print(chest, chest.access, item.tier)
        
        # print(required_item_pool)
        # print(len(required_item_pool), len(extra_item_pool))
        for l in all_locations:
            pass
        # todo: character animations
        # will need to sub in characters for animations where no char is recruited (ie who goes in marrymore in a solo challenge?)
        # at some point, will need to figure out partitioning for rooms where coins end up
