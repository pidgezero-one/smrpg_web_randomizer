# Chest randomization logic.

import math
import random
import enum

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
    (10, RandomGrantEnum.RecoveryMushroom),
    (10, RandomGrantEnum.Flower),
    (10, RandomGrantEnum.FrogCoins),
    (10, RandomGrantEnum.Coins),
    (19, RandomGrantEnum.Equip),
    (29, RandomGrantEnum.RegularItem)
]

star_chest_grant_table = [
    (2, RandomGrantEnum.SlotMachine),
    (10, RandomGrantEnum.EXPStar),
    (10, RandomGrantEnum.RecoveryMushroom),
    (10, RandomGrantEnum.Flower),
    (10, RandomGrantEnum.FrogCoins),
    (10, RandomGrantEnum.Coins),
    (19, RandomGrantEnum.Equip),
    (29, RandomGrantEnum.RegularItem)
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

    def has_item(self, item):
        """

        Args:
            item: Item class to check for.

        Returns:
            bool: True if inventory contains this item, False otherwise.

        """
        return any([i for i in self if i == item])

    def has_item_count(self, item, value = 1):
        """

        Args:
            item: Item class to check for.

        Returns:
            bool: True if inventory contains this item, False otherwise.

        """
        incidence = [i for i in self if i == item]
        return any(incidence) and len(incidence) >= value


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


def _place_items(world, _items, locations, base_inventory=None):
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

    # if len(remaining_fill_items) > len([l for l in locations if not l.has_item]):
    #    raise ValueError("Trying to fill more items than available locations")

    # For each required item, place it assuming we can get all other items.

    # Firstly, bias Super Suit (or whatever the best of the 10 special equips ends up being) to the 100 jump location under the right conditions
    if world.settings.is_flag_value(flags.RestrictSpecialEquips, True):
        jumps2_location_open = [l for l in locations if utils.isclass_or_instance(l, chests.SuperJumps100) and l.access == 2]
        if len(jumps2_location_open) > 0:
            bias = random.randint(1, 10)
            if bias <= 3:
                item = remaining_fill_items[0] # best item of the 10, to account for stat randomization
                remaining_fill_items.remove(item)
                jumps2_location_open[0].item = item

    # Get items we can get assuming we have everything but the one we're placing.
    assumed_items = _collect_items(
        world, remaining_fill_items + base_inventory)

    blocked_star_piece_areas = []

    for item in _items:
        # filter down locations if eligible for biased shuffling
        # 80% chance that better items appear in locations with more gating, and vice versa
        if item.tier > 0 and not item.is_key and world.settings.is_flag_value(flags.BiasItemShuffle, True):
            if item.tier == 1 or item.tier == 2:
                chooser = random.randint(1, 10)
                if chooser > 2:
                    fillable_locations = [l for l in locations if not l.has_item and l.can_access(assumed_items)
                            and l.item_allowed(item) and l.access == 1]
                if chooser <= 2 or len(fillable_locations) == 0:
                    fillable_locations = [l for l in locations if not l.has_item and l.can_access(assumed_items)
                            and l.item_allowed(item) and l.access != 1]
            elif item.tier == 3 or item.tier == 4:
                chooser = random.randint(1, 10)
                if chooser > 2:
                    fillable_locations = [l for l in locations if not l.has_item and l.can_access(assumed_items)
                            and l.item_allowed(item) and l.access == 2]
                if chooser <= 2 or len(fillable_locations) == 0:
                    fillable_locations = [l for l in locations if not l.has_item and l.can_access(assumed_items)
                            and l.item_allowed(item) and l.access != 2]
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

        if fillable_locations:
            remaining_fill_items.remove(item)

            # Place item in the first fillable location.
            if item.tier == 1 and item.price != 0 and world.settings.is_flag_value(flags.ReplaceItems, True):
                fillable_locations[0].item = items.Coins(world, item.price // 2)
            else:
                fillable_locations[0].item = item

            # Populate corresponding spotted character, if eligible (currently only affects Forest Maze access)
            if utils.isclass_or_instance(fillable_locations[0], chests.MarrymoreCharacter):
                if item == items.MarioRecruit:
                    spotted = items.MarioSpotted
                elif item == items.MallowRecruit:
                    spotted = items.MallowSpotted
                elif item == items.GenoRecruit:
                    spotted = items.GenoSpotted
                elif item == items.BowserRecruit:
                    spotted = items.BowserSpotted
                elif item == items.ToadstoolRecruit:
                    spotted = items.ToadstoolSpotted
                set_item(world.spotted_character_checks, chests.MarrymoreCharacterSpotted, spotted)
            
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
                chests_missing_locations = [c for c in world.chests if utils.isclass_or_instance(c, chests.PandoriteReward1) or utils.isclass_or_instance(c, chests.PandoriteReward2) or utils.isclass_or_instance(c, chests.PandoriteBoss)]
            elif utils.isclass_or_instance(item, items.PandoriteFight):
                chests_missing_locations = [c for c in world.chests if utils.isclass_or_instance(c, chests.HidonReward1) or utils.isclass_or_instance(c, chests.HidonReward2) or utils.isclass_or_instance(c, chests.HidonBoss)]
            elif utils.isclass_or_instance(item, items.BoxBoyFight):
                chests_missing_locations = [c for c in world.chests if utils.isclass_or_instance(c, chests.BoxBoyBoss)]
            for c in chests_missing_locations:
                c.area = fillable_locations[0].area


            # does this enter the marrymore char sighting into sphere 0?
            assumed_items = _collect_items(
                world, remaining_fill_items + base_inventory)

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

    available_locations = [l for l in world.recruitable_character_checks + world.starter_character_checks + world.chest_locations + world.freestanding_item_locations + world.boss_star_checks if l.has_item]

    # Search all locations and collect items until we can't get any more.
    while True:
        search_locations = [
            l for l in available_locations if l.can_access(world, my_items)]
        available_locations = [
            l for l in available_locations if l not in search_locations]
        found_items = Inventory([l.item for l in search_locations])
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
    if extra_items is None:
        extra_items = Inventory()

    if existing_inventory is None:
        existing_inventory = Inventory()

    # Sanity check to make sure we're filling the right number of spots.
    if len(locations_to_fill) < len(required_items) + len(extra_items):
        raise ValueError("Not enough locations for number of items.")

    # Clear existing items to start.
    for location in locations_to_fill:
        location.item = None

    # Remove prohibited star piece boss checks
    bosses_to_completely_ignore = world.settings.get_flag(flags.EnabledBossChecks).disabled
    if world.settings.is_flag_value(flags.WinCondition, WinConditions.FinalBoss):
        bosses_to_completely_ignore.append(ShuffleLocationSelector.InnerFactoryBossFinal)
    if world.settings.is_flag_value(flags.WinCondition, WinConditions.Culex):
        bosses_to_completely_ignore.append(ShuffleLocationSelector.CulexBoss)
    locations_to_fill = [l for l in locations_to_fill if l.description not in bosses_to_completely_ignore]

    # Shuffle locations, required items and extra items.
    random.shuffle(locations_to_fill)
    random.shuffle(required_items)
    random.shuffle(extra_items)

    # Place required items first.
    equips = []
    # Place the ten Special Equips first if that flag is enabled
    if world.settings.is_flag_value(flags.RestrictSpecialEquips, True):
        equips = [i for i in extra_items if i.special_equip]
        equips.sort(key=lambda x: x.rank_value, reverse=True)
        extra_items = [i for i in extra_items if not i.special_equip]
        remainder = _place_items(world, equips, [l for l in locations_to_fill if l.special_equip], existing_inventory)
        extra_items += remainder

    star_pieces = []
    # Attempt to fill key item locations next if Key Items Anywhere is not enabled
    if not world.settings.is_flag_enabled(flags.KeyItemsAnywhere):
        star_pieces = [i for i in required_items if utils.isclass_or_instance(i, items.StarPiece)]
        required_items = [i for i in required_items if not utils.isclass_or_instance(i, items.StarPiece)]
        remainder += star_pieces
        remainder = _place_items(world, [i for i in required_items if not utils.isclass_or_instance(i, items.StarPiece)], [l for l in locations_to_fill if l.key], existing_inventory)
    else:
        remainder = _place_items(world, required_items, locations_to_fill, existing_inventory)

    # If any required items were left over (due to star piece shuffle, KIs anywhere, progressive fireworks, etc), handle them first
    locations_to_fill = [l for l in locations_to_fill if not l.has_item]
    remainder = _place_items(world, remainder, locations_to_fill, existing_inventory)
    
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
    leftover = set(required_items + star_pieces + extra_items + equips) - collected_items
    return leftover


def set_item(collection, location, item):
    for i in range(len(collection)):
        if utils.isclass_or_instance(collection[i], location):
            collection[i].item = item

def get_max_item_quality(world):
    tiers_allowed = 4
    if world.settings.is_flag_value(flags.ItemQuality, ItemQualities.Tier1):
        tiers_allowed = 1
    elif world.settings.is_flag_value(flags.ItemQuality, ItemQualities.Tier2):
        tiers_allowed = 2
    elif world.settings.is_flag_value(flags.ItemQuality, ItemQualities.Tier3):
        tiers_allowed = 3
    return tiers_allowed

def generate_nonrequired_item(world, table, chest):
    max_tier = get_max_item_quality(world)
    total_chance = 0
    for chance, _ in table:
        total_chance += chance
    proc = random.randint(1, total_chance)
    counter = 0
    result = None
    for chance, res in table:
        counter += chance
        if proc >= counter:
            continue
        else:
            result = res
            break
    if result == RandomGrantEnum.SlotMachine:
        item = items.SlotMachineChest
    elif result == RandomGrantEnum.RecoveryMushroom:
        item = items.RecoveryMushroom
    elif result == RandomGrantEnum.Flower:
        item = items.Flower
    elif result == RandomGrantEnum.EXPStar:
        all_choices = [i for i in world.items if utils.isclass_or_instance(i, items.InvincibilityStar)]
        rand = random.randint(1, len(all_choices))
        item = all_choices[rand - 1]
    elif result == RandomGrantEnum.Coins:
        if utils.isclass_or_instance(chest, chests.OverworldItem):
            rand = random.randint(1, 10)
            if rand > 3:
                item = items.Coins10
            else:
                item = items.Coins1
        else:
            value = gamma.rvs(80, size=1)[0] // 1
            item = items.Coins(world, value)
    elif result == RandomGrantEnum.FrogCoins:
        if utils.isclass_or_instance(chest, chests.OverworldItem):
            item = items.FrogCoin
        else:
            rand = random.randint(1, 10)
            if rand > 1:
                item = items.FrogCoin
            else:
                possibilities = [2, 3, 4, 5, 6, 7, 8, 9, 10]
                value = random.choices(possibilities, weights=(10, 9, 8, 7, 6, 5, 4, 3, 2), k=1)[0]
                item = items.MultiFrogCoin(world, value)
    elif result == RandomGrantEnum.Equip or result == RandomGrantEnum.RegularItem:
        if result == RandomGrantEnum.Equip:
            all_choices = [i for i in world.items if (i.unique == ItemUnique.Never or (i.unique == ItemUnique.BalancedOnly and not world.settings.is_flag_value(flags.ItemQuality, ItemQualities.Original))) and i.is_equipment and i.tier <= max_tier]
        else:
            all_choices = [i for i in world.items if (i.unique == ItemUnique.Never or (i.unique == ItemUnique.BalancedOnly and not world.settings.is_flag_value(flags.ItemQuality, ItemQualities.Original))) and i.tier <= max_tier]
        if utils.isclass_or_instance(chest, chests.TreasureSellerReward):
            all_choices = [i for i in all_choices if i.unique == ItemUnique.BalancedOnly]
        possibilities = [1, 2, 3, 4]
        if world.settings.is_flag_value(flags.BiasItemShuffle, True):
            if chest.access == 1:
                weights=[30, 50, 15, 5]
            elif chest.access == 2:
                weights=[5, 15, 60, 20]
            else:
                weights=[20, 45, 25, 10]
        else:
            weights=[20, 45, 25, 10]
        possibilities = possibilities[:max_tier]
        weights = tuple(weights[:max_tier])
        value = random.choices(possibilities, weights, k=1)[0]
        choices = [i for i in all_choices if i.tier == value]
        rand = random.randint(1, len(choices))
        item = choices[rand - 1]
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
        if world.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.Vanilla) or world.settings.is_flag_value(flags.BucketWarp, True):
            all_locations = [a for a in all_locations if not utils.isclass_or_instance(a, chests.BucketGirl)]
        # fireworks shuffle
        if world.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.Vanilla):
            all_locations = [a for a in all_locations if not utils.isclass_or_instance(a, chests.FireworksShop)]
        # beetlemania shuffle
        if world.settings.is_flag_value(flags.ShuffleBeetlemania, False):
            all_locations = [a for a in all_locations if not utils.isclass_or_instance(a, chests.MushroomKingdomInn)]
        # magikoopa's chest shuffle
        if world.settings.is_flag_value(flags.ShuffleMagikoopaChest, False):
            all_locations = [a for a in all_locations if not utils.isclass_or_instance(a, chests.BowsersKeepMagikoopa)]
        # mimics shuffle
        if world.settings.is_flag_value(flags.SlotsAnywhere, False):
            all_locations = [a for a in all_locations if not utils.isclass_or_instance(a, chests.PandoriteChest) and not utils.isclass_or_instance(a, chests.HidonChest) and not utils.isclass_or_instance(a, chests.BeanValleyBoxBoyRoom1)]
        # slots shuffle
        if world.settings.is_flag_value(flags.MimicsAnywhere, False):
            all_locations = [a for a in all_locations if not utils.isclass_or_instance(a, chests.BeanValleyLeftPiranhaPipe) and not utils.isclass_or_instance(a, chests.BeanValleyBottomLeftPiranhaPipe) and not utils.isclass_or_instance(a, chests.BeanValleyBottomRightPiranhaPipeUpper)]
        # exp stars shuffle
        if world.settings.is_flag_value(flags.EXPStarsAnywhere, False):
            all_locations = [a for a in all_locations if not utils.isclass_or_instance(a, chests.BanditsWayStarChest) and not utils.isclass_or_instance(a, chests.KeroSewersStarChest) and not utils.isclass_or_instance(a, chests.MolevilleMinesStarChest) and not utils.isclass_or_instance(a, chests.SeaStarChest) and not utils.isclass_or_instance(a, chests.LandsEndStarChest1) and not utils.isclass_or_instance(a, chests.LandsEndStarChest2) and not utils.isclass_or_instance(a, chests.LandsEndStarChest3) and not utils.isclass_or_instance(a, chests.NimbusCastleStarChest) and not utils.isclass_or_instance(a, chests.BarrelVolcanoStarRoom)]
        # star piece shuffle
        if world.settings.is_flag_value(flags.ShuffleStarPieces, False):
            all_locations = [a for a in all_locations if not utils.isclass_or_instance(a, chests.BossStarPiece)]
        # remove frog disciple checks and treasure seller if shop shuffle is off or if shops empty
        if world.settings.is_flag_value(flags.ShuffleShops, False) or world.settings.is_flag_value(flags.ShopQuality, ShopQualities.Empty):
            all_locations = [a for a in all_locations if not utils.isclass_or_instance(a, chests.FrogCoinShopItem) and not utils.isclass_or_instance(a, chests.TreasureSellerReward)]
        inventory = Inventory([])

        # populate starting characters
        number_of_starting_characters = world.settings.get_flag(
            flags.StartingCharacters).value
        starting_party = [None]*5
        allCharacters = [PlayableCharacters.Mario, PlayableCharacters.Mallow,
                        PlayableCharacters.Geno, PlayableCharacters.Bowser, PlayableCharacters.Toadstool]
        charactersInSeed = [c for c in allCharacters if c in world.settings.get_flag(
            flags.AvailableCharacters).enabled]
        # throw error if any required chars are excluded
        if PlayableCharacters.Mario in world.settings.get_flag(flags.AvailableCharacters).disabled and (world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.RecruitMario) or world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindMario) or world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.RecruitMario) or world.settings.is_flag_value(flags.SeaGate, SeaGating.RecruitMario)):
            raise Exception('cannot exclude Mario when required for area access')
        if PlayableCharacters.Mallow in world.settings.get_flag(flags.AvailableCharacters).disabled and (world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.RecruitMallow) or world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindMallow) or world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.RecruitMallow) or world.settings.is_flag_value(flags.SeaGate, SeaGating.RecruitMallow)):
            raise Exception('cannot exclude Mallow when required for area access')
        if PlayableCharacters.Geno in world.settings.get_flag(flags.AvailableCharacters).disabled and (world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.RecruitGeno) or world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindGeno) or world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.RecruitGeno) or world.settings.is_flag_value(flags.SeaGate, SeaGating.RecruitGeno)):
            raise Exception('cannot exclude Geno when required for area access')
        if PlayableCharacters.Bowser in world.settings.get_flag(flags.AvailableCharacters).disabled and (world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.RecruitBowser) or world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindBowser) or world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.RecruitBowser) or world.settings.is_flag_value(flags.SeaGate, SeaGating.RecruitBowser)):
            raise Exception('cannot exclude Bowser when required for area access')
        if PlayableCharacters.Toadstool in world.settings.get_flag(flags.AvailableCharacters).disabled and (world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.RecruitToadstool) or world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.FindToadstool) or world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.RecruitToadstool) or world.settings.is_flag_value(flags.SeaGate, SeaGating.RecruitToadstool)):
            raise Exception('cannot exclude Toadstool when required for area access')
        # throw error if not enough chars to fill desired party
        if len(charactersInSeed) < number_of_starting_characters:
            raise Exception('not enough characters to fill desired starting party')
        random.shuffle(charactersInSeed)
        starter = world.settings.get_flag(flags.StartingCharacter).value
        if starter != PlayableCharacters.Random:
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
            if starting_characters[i] == PlayableCharacters.Mario:
                character = items.MarioRecruit
            elif starting_characters[i] == PlayableCharacters.Mallow:
                character = items.MallowRecruit
            elif starting_characters[i] == PlayableCharacters.Geno:
                character = items.GenoRecruit
            elif starting_characters[i] == PlayableCharacters.Bowser:
                character = items.BowserRecruit
            elif starting_characters[i] == PlayableCharacters.Toadstool:
                character = items.ToadstoolRecruit
            elif starting_characters[i] == None:
                character = None
            else:
                raise Exception("invalid character %r" % starting_characters[i])
            set_item(world.starter_character_checks, location, character)
            inventory.append(character)

        # will this work? combining classes and instances?
        # Collect required base item pool
        # key items + characters
        required_item_pool = [i for i in world.items if i.is_key] + [c for c in world.recruitable_characters if c.description in charactersInSeed and c.description not in starting_characters]
        # add star pieces
        if world.settings.is_flag_value(flags.ShuffleStarPieces, True):
            total_star_pieces = world.settings.get_flag(flags.TotalStarPieces).value
            star_pieces = [items.StarPiece1, items.StarPiece2, items.StarPiece3, items.StarPiece4, items.StarPiece5, items.StarPiece6, items.StarPiece7]
            required_item_pool += (star_pieces[0:total_star_pieces])
        # apply fireworks settings
        if world.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.ShuffleFireworks):
            required_item_pool.append(items.Fireworks)
        elif world.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.ProgressiveFireworks):
            required_item_pool += ([items.ProgressiveFireworks] * 3)
            # consideration: two of these will not be able to make it into the key item pool

        extra_item_pool = []
        # non-key items which should always only appear up to a certain # of times
        # bright card, if not a KI
        if world.settings.is_flag_value(flags.CasinoWarp, False):
            extra_item_pool.append(items.BrightCard)
        # beetlemania
        if world.settings.is_flag_value(flags.ShuffleBeetlemania, True):
            extra_item_pool.append(items.Beetlemania)
        # mimics anywhere
        if world.settings.is_flag_value(flags.MimicsAnywhere, True):
            extra_item_pool += [items.PandoriteFight, items.HidonFight, items.BoxBoyFight]
        # if Restrict Special Equips is on, must guarantee all ten appear once
        if world.settings.is_flag_value(flags.RestrictSpecialEquips, True):
            extra_item_pool += [i for i in world.items if i.special_equip]
        # if star piece hints is on, must guarantee signal ring
        if world.settings.is_flag_value(flags.StarPieceHints, True):
            extra_item_pool.append(items.SignalRing)
        # other items
        if not world.settings.is_flag_value(flags.ItemQuality, ItemQualities.Empty):
            if world.settings.is_flag_value(flags.ShuffleShops, False) and not world.settings.is_flag_value(flags.ShopQuality, ShopQualities.Empty):
                # add 2 progressive eggs if one is guaranteed in treasure shop
                extra_item_pool += ([items.ProgressiveEgg] * 2)
            else:
                # add 3 otherwise
                extra_item_pool += ([items.ProgressiveEgg] * 3)
            # magikoopa's chest shuffle
            if world.settings.is_flag_value(flags.ShuffleMagikoopaChest, True):
                extra_item_pool.append(items.InfiniteCoins)
            limited_items = [items.GoodieBag, items.YouMissed, items.SeeYa, items.EarlierTimes, items.StarEgg, items.Wallet, items.LuckyJewel]
            max_tier = get_max_item_quality(world)
            extra_item_pool += [i for i in limited_items if i.tier <= max_tier]
        remainder_check = extra_item_pool.copy()
        # balanced only: populate extra_item_pool with existing item pool
        if world.settings.is_flag_value(flags.ItemQuality, ItemQualities.Original):
            extra_item_pool += [c.item for c in all_locations if c not in required_item_pool and c not in extra_item_pool]

        # place all the items that this seed NEEDS to have by definition
        # event generation can happen in main.py
        remainder = fill_locations(world, all_locations, required_item_pool, extra_item_pool, inventory)
        if remainder:
            excluded_important_items = [i for i in remainder if i.is_key or i in remainder_check or utils.isclass_or_instance(i, items.RecruitedCharacter)]
            if len(excluded_important_items) > 0:
                raise ValueError("Items were not placed: {!r}".format(
                    excluded_important_items))

        # next step: fill empty grants, if any, with randomly generated items
        all_remaining_locations = [a for a in all_locations if not a.has_item and (utils.isclass_or_instance(a, chests.Chest) or utils.isclass_or_instance(a, chests.NPCReward) or utils.isclass_or_instance(a, chests.OverworldItem))]
        for chest in all_remaining_locations:
            if world.settings.is_flag_value(flags.ItemQuality, ItemQualities.Empty):
                if not utils.isclass_or_instance(chest, chests.FrogCoinShopItem):
                    chest.item = items.Nothing
                else:
                    chest.item = items.GoodieBag
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
                    if item.tier == 1 and item.price != 0 and world.settings.is_flag_value(flags.ReplaceItems, True):
                        item = items.Coins(world, item.price // 2)
                    chest.item = item
                # Ignore empty boss locations and empty character recruit locations, those SHOULD be empty if they don't receive an item

        # todo: character animations
        # will need to sub in characters for animations where no char is recruited (ie who goes in marrymore in a solo challenge?)
        # at some point, will need to figure out partitioning for rooms where coins end up
