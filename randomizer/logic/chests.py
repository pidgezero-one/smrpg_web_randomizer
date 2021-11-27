# Chest randomization logic.

import math
import random
import enum
import copy

from scipy.stats import gamma

from randomizer.data import items, locations, chests, bosses
from randomizer.data.chests import PacketType 
from randomizer.data.helpers import FireworksOptions, WinConditions, ItemQualities, ShopQualities, PlayableCharacters, BanditsWayGating, ForestMazeGating, BoosterTowerGating, SeaGating, ShuffleLocationSelector
from randomizer.data.items import ItemUnique
from randomizer.data.locations import Area
from randomizer.data.keys import KeyItemLocation
from randomizer.logic import flags, keys, utils
from randomizer.data.eventscripts.utils.slot_machine.event import script as slot_machine_commands
from randomizer.data.eventscripts.utils.slot_machine.objects import objects as slot_machine_npcs
from randomizer.data.eventtables import AreaObjects
from randomizer.data import characters

dummy_allpurpose_item = items.RegularItem(None)
dummy_allpurpose_item.consumable = True
dummy_allpurpose_item.price = 1
dummy_allpurpose_item.unique = ItemUnique.BalancedOnly

reward_table = [
    (2, items.SlotMachineChest),
    (5, items.InvincibilityStar),
    (5, items.RecoveryMushroom),
    (7, items.Flower),
    (6, items.FrogCoin),
    (6, items.Coins),
    (69, dummy_allpurpose_item)
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
        chest_locations(list[randomizer.chests.Chest]):

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

        # no more than one slot machine per room, too many NPCs to handle
        if utils.isclass_or_instance(item, items.SlotMachineChest):
            rooms_arrays_that_already_have_slot_machines = [l.rooms for l in locations if utils.isclass_or_instance(l.item, items.SlotMachineChest)]
            rooms_that_already_have_slot_machines = [item for sublist in rooms_arrays_that_already_have_slot_machines for item in sublist]
            for r in rooms_that_already_have_slot_machines:
                fillable_locations = [l for l in fillable_locations if r not in l.rooms]

        # bias star pieces toward boss locations, slightly, even if SPs Anywhere enabled
        if world.settings.is_flag_enabled(flags.StarPieceAvailability) and utils.isclass_or_instance(item, items.StarPiece):
            if random.randint(0, 9) > 5:
                fillable_locations = [l for l in fillable_locations if l.star_location]
        
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
            if allow_replacements and fillable_locations[0].item_allowed(items.Coins) and not(item.is_key or item.special_equip) and item.tier == 5 and item.price != 0 and world.settings.is_flag_value(flags.ReplaceItems, True):
                fillable_locations[0].item = items.Coins(item.price // 2, world)
                #print ("default:", item, item.tier, items.Coins(item.price // 2, world).amount)
            else:
                fillable_locations[0].item = item

            # Populate corresponding spotted character, if eligible (currently only affects Forest Maze access)
            if utils.isclass_or_instance(fillable_locations[0], chests.MarrymoreCharacter) or utils.isclass_or_instance(fillable_locations[0], chests.MushroomWayCharacter):
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
                    if utils.isclass_or_instance(fillable_locations[0], chests.MarrymoreCharacter):
                        set_item(world.spotted_character_checks, chests.MarrymoreCharacterSpotted, world.get_item_instance(spotted))
                    elif utils.isclass_or_instance(fillable_locations[0], chests.MushroomWayCharacter):
                        set_item(world.spotted_character_checks, chests.MushroomWayCharacterSpotted, world.get_item_instance(spotted))
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
                chests_missing_locations = [c for c in world.chest_locations + world.boss_star_checks if utils.isclass_or_instance(c, chests.PandoriteReward1) or utils.isclass_or_instance(c, chests.PandoriteReward2) or utils.isclass_or_instance(c, chests.PandoriteBoss)]
            elif utils.isclass_or_instance(item, items.PandoriteFight):
                chests_missing_locations = [c for c in world.chest_locations + world.boss_star_checks if utils.isclass_or_instance(c, chests.HidonReward1) or utils.isclass_or_instance(c, chests.HidonReward2) or utils.isclass_or_instance(c, chests.HidonBoss)]
            elif utils.isclass_or_instance(item, items.BoxBoyFight):
                chests_missing_locations = [c for c in world.chest_locations + world.boss_star_checks if utils.isclass_or_instance(c, chests.BoxBoyBoss)]
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

def generate_nonrequired_item(world, chest):

    max_tier = get_max_item_quality(world)
    table = [t for t in reward_table if chest.item_allowed(t[1])]
    if not world.settings.is_flag_enabled(flags.SlotsAnywhere):
        table = [t for t in reward_table if not utils.isclass_or_instance(t[1], items.SlotMachineChest)]
    if not world.settings.is_flag_enabled(flags.EXPStarsAnywhere):
        table = [t for t in reward_table if not utils.isclass_or_instance(t[1], items.InvincibilityStar)]

    weights, possible_options = list(zip(*table))
    result = random.choices(possible_options, weights=weights, k=1)[0]
    if result == items.InvincibilityStar:
        all_choices = [world.get_item_instance(i) for i in [items.BanditsWayStar, items.KeroSewersStar, items.MolevilleMinesStar, items.SeaStar, items.LandsEndVolcanoStar, items.LandsEndVolcanoStar, items.NimbusLandStar, items.LandsEndStar2, items.LandsEndStar3]]
        item = world.get_item_instance(random.choice(all_choices))
    elif result == items.Coins:
        if utils.isclass_or_instance(chest, chests.OverworldItem):
            rand = random.randint(1, 10)
            if rand > 3:
                item = world.get_item_instance(items.Coins10)
            else:
                item = world.get_item_instance(items.Coins1)
        else:
            value = gamma.rvs(80, size=1)[0] // 1
            #print ("nonrequired:", item, item.tier, items.Coins(value, world).amount)
            item = items.Coins(value, world)
    elif result == items.FrogCoin:
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
    elif utils.isclass_or_instance(result, items.RegularItem):
        all_choices = [i for i in world.items if (i.unique == ItemUnique.Never or (i.unique == ItemUnique.BalancedOnly and not world.settings.is_flag_value(flags.ItemQuality, ItemQualities.original))) and i.tier >= max_tier and chest.item_allowed(i)]
        if utils.isclass_or_instance(chest, chests.TreasureSellerReward):
            all_choices = [i for i in all_choices if i.unique == ItemUnique.BalancedOnly]
        else:
            all_equips = [i for i in all_choices if i.is_equipment]
            all_nonequips = [i for i in all_choices if not i.is_equipment]
            if len(all_equips) > 0 and len(all_nonequips) > 0:
                if random.randint(0, 2) == 0:
                    all_choices = [i for i in all_choices if i.is_equipment]
                else:
                    all_choices = [i for i in all_choices if not i.is_equipment]
        if len(all_choices) == 0:
            raise Exception("could not fill chest %r" % chest)
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
        value = random.choices(possibilities, weights, k=1)[0]
        while len(choices) == 0:
            choices = [i for i in all_choices if i.tier == value]
            # if empty, keep trying worse tiers
            p_index = possibilities.index(value)
            if p_index == len(possibilities) - 1:
                break
            value = possibilities[p_index + 1]
        if len(choices) == 0:
            raise Exception("could not fill chest %r" % chest)
        item = random.choice(choices)
        if chest.item_allowed(items.Coins) and item.tier == 5 and item.price != 0 and world.settings.is_flag_value(flags.ReplaceItems, True):
            item = items.Coins(item.price // 2, world)
    else:
        item = world.get_item_instance(result)
    return item

def randomize_all(world):
    """

    Args:
        world (randomizer.logic.main.GameWorld): Game world to randomize.

    """


    # Open mode-specific shuffles.
    if world.open_mode:



        # Collect pool of locations that need item assignments
        overworld_items_to_include = world.settings.get_flag(flags.EnabledFreestandingChecks).enabled
        #print(overworld_items_to_include)
        locations_to_completely_ignore = [w.description for w in world.freestanding_item_locations if w.description not in overworld_items_to_include]
        #print(locations_to_completely_ignore)
        
        inventory = Inventory([])

        # Contents of excluded chests will still be shuffled, they just will not contain progression items.
        # Excluded freestanding items will remain vanilla.
        # Excluded boss checks will receive "None"
        # Character locations cannot be excluded, but will receive "None" if unassigned
        all_locations = []
        if world.settings.is_flag_enabled(flags.ShuffleItems):
            all_locations += world.chest_locations.copy() + [c for c in world.freestanding_item_locations if c.description not in locations_to_completely_ignore]
            # housekeeping: if pool is set to empty, disable all freestanding items that aren't candidates for KI/star shuffle
            if world.settings.is_flag_value(flags.ItemQuality, ItemQualities.empty):
                for c in world.freestanding_item_locations:
                    if c.description in locations_to_completely_ignore:
                        c.item = None
        if world.settings.is_flag_enabled(flags.ShuffleStarPieces):
            all_locations += world.boss_star_checks.copy()
        if world.settings.is_flag_enabled(flags.ShuffleCharacters):
            for c in world.spotted_character_checks + world.recruitable_character_checks:
                c.item = None
            all_locations += world.recruitable_character_checks.copy() + world.spotted_character_checks.copy()

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
        
        # Do chest overrides and remove them from the pool.
        if "items" in world.settings.override and "override" in world.settings.override["items"]:
            for c in world.settings.override["items"]["override"]:
                chest = eval('chests.%s' % c)
                item = eval('items.%s' % world.settings.override["items"]["override"][c])
                for l in all_locations:
                    if utils.isclass_or_instance(l, chest):
                        l.item = item
                        all_locations.remove(l)
                        break

        #print(all_locations)


        remainder = []
        required_item_pool = []
        extra_item_pool = []

        # populate starting characters
        if world.settings.is_flag_enabled(flags.ShuffleCharacters):
            number_of_starting_characters = world.settings.get_flag(flags.StartingCharacters).value
            starting_party = [None]*5
            allCharacters = [PlayableCharacters.mario, PlayableCharacters.mallow,
                            PlayableCharacters.geno, PlayableCharacters.bowser, PlayableCharacters.toadstool]
            charactersInSeed = [c for c in allCharacters if c in world.settings.get_flag(
                flags.AvailableCharacters).enabled]
            #print (charactersInSeed)
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
            required_item_pool += [world.get_item_instance(char) for char in [items.MarioRecruit, items.MallowRecruit, items.GenoRecruit, items.BowserRecruit, items.ToadstoolRecruit] if char.description in [c for c in charactersInSeed if c not in starting_characters]]
        
        # Collect required base item pool
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

        if world.settings.is_flag_enabled(flags.ShuffleItems):
            # key items
            required_item_pool += [i for i in world.items if i.is_key and not i.is_subitem]

            # non-key items which should always only appear up to a certain # of times
            # bright card, if not a KI
            if world.settings.is_flag_value(flags.CasinoWarp, False):
                required_item_pool.append(world.get_item_instance(items.BrightCard))
            # if star piece hints is on, must guarantee signal ring
            if world.settings.is_flag_value(flags.StarPieceHints, True):
                required_item_pool.append(world.get_item_instance(items.SignalRing))
            # mimics anywhere
            if world.settings.is_flag_value(flags.MimicsAnywhere, True):
                required_item_pool += [world.get_item_instance(f) for f in [items.PandoriteFight, items.HidonFight, items.BoxBoyFight]]
            # other items
            if not world.settings.is_flag_value(flags.ItemQuality, ItemQualities.empty):
                # beetlemania
                if world.settings.is_flag_value(flags.ShuffleBeetlemania, True):
                    required_item_pool.append(world.get_item_instance(items.Beetlemania))
                # if Restrict Special Equips is on, must guarantee all ten appear once
                if world.settings.is_flag_value(flags.RestrictSpecialEquips, True):
                    required_item_pool += [i for i in world.items if i.special_equip]
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
            # keep one YouMissed :)
            else:
                required_item_pool.append(world.get_item_instance(items.YouMissed))

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

        # if this is a real rom attempt with no overrides specified in debug config, error out if required items weren't placed
        if not ("items" in world.settings.override and "override" in world.settings.override["items"] and len(world.settings.override["items"]["override"]) > 0):
            if remainder:
                excluded_important_items = [i for i in remainder if i.is_key or i in remainder_check or utils.isclass_or_instance(i, items.RecruitedCharacter)]
                if len(excluded_important_items) > 0:
                    for l in all_locations:
                        print(l)
                    raise ValueError("Items were not placed: {!r}".format(
                        excluded_important_items))


        # next step: fill empty grants, if any, with randomly generated items
        all_remaining_locations = [a for a in all_locations if not a.has_item and (utils.isclass_or_instance(a, chests.Chest) or utils.isclass_or_instance(a, chests.NPCReward) or utils.isclass_or_instance(a, chests.OverworldItem))]
        
        
        for chest in all_remaining_locations:
            if world.settings.is_flag_value(flags.ItemQuality, ItemQualities.empty):
                if not utils.isclass_or_instance(chest, chests.FrogCoinShopItem):
                    chest.item = None
                else:
                    chest.item = world.get_item_instance(items.GoodieBag)
            else:
                item = generate_nonrequired_item(world, chest)
                if item:
                    if chest.item_allowed(items.Coins) and item.tier == 5 and item.price != 0 and world.settings.is_flag_value(flags.ReplaceItems, True):
                        #print("empty grants:", item, item.tier, items.Coins(item.price // 2, world))
                        item = items.Coins(item.price // 2, world)
                    chest.item = item
                # Ignore empty boss locations and empty character recruit locations, those SHOULD be empty if they don't receive an item
            
        
        # at some point, will need to figure out partitioning for rooms where coins end up

        ######### write granter scripts for characters/items/star pieces
        # these event scripts are referenced by all item grant locations in the game and are usually based on room ID

        grant_builders = {}

        
        # sanitize exp stars, etc. 
        for c in world.recruitable_character_checks + world.chest_locations + world.freestanding_item_locations + world.boss_star_checks:
            if type(c.item) == type:
                c.item = c.item(world)
            


        # shuffling finished - now apply it to the game



        if world.settings.is_flag_enabled(flags.ShuffleCharacters):
            character_order = [None] * 5
        else:
            character_order = [items.MarioRecruit, items.MallowRecruit,
                            items.GenoRecruit, items.BowserRecruit, items.ToadstoolRecruit]



        # recruitable characters - characters aree treated as items as far as the logic is concerned, so this goes here
        for c in world.starter_character_checks:
            if utils.isclass_or_instance(c, chests.StarterCharacter1):
                character_order[0] = c.item

        # recruitable characters - characters aree treated as items as far as the logic is concerned, so this goes here
        for c in world.recruitable_character_checks:
            if utils.isclass_or_instance(c, chests.StarterCharacter1):
                print(c, c.item)
            if c.event is not None and c.event not in grant_builders:
                grant_builders[c.event] = {
                    "jumps": [utils.new_command(c.event, 'set_7000_to_current_level')],
                    "executions": []
                }
            if c.item is not None:
                for d in c.dialogs_to_replace:
                    for id, dat in c.item.dialog_replacements:
                        if d == id:
                            world.replace_dialog(id, dat)
                cmd = utils.new_command(c.event, 'jmp_to_event', [c.item.container_script])
                grant_builders[c.event]["executions"].append(cmd)
                for r in c.rooms:
                    jmp = utils.new_command(c.event, 'jmp_if_7000_equals_short', [r, cmd["identifier"]])
                    grant_builders[c.event]["jumps"].append(jmp)
                # forest maze gating
                if utils.isclass_or_instance(c, chests.StarterCharacter1):
                    character_order[0] = c.item
                elif utils.isclass_or_instance(c, chests.MushroomWayCharacter):
                    character_order[1] = c.item
                    if (world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.mario) and utils.isclass_or_instance(c.item, items.MarioRecruit)) or (world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.mallow) and utils.isclass_or_instance(c.item, items.MallowRecruit)) or (world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.geno) and utils.isclass_or_instance(c.item, items.GenoRecruit)) or (world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.bowser) and utils.isclass_or_instance(c.item, items.BowserRecruit)) or (world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.toadstool) and utils.isclass_or_instance(c.item, items.ToadstoolRecruit)):
                        world.prepend_bits(202, [[0x7066, 3], [0x706E, 3]])
                elif utils.isclass_or_instance(c, chests.MolevilleMinesCharacter):
                    character_order[3] = c.item
                    if (world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.mario) and utils.isclass_or_instance(c.item, items.MarioRecruit)) or (world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.mallow) and utils.isclass_or_instance(c.item, items.MallowRecruit)) or (world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.geno) and utils.isclass_or_instance(c.item, items.GenoRecruit)) or (world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.bowser) and utils.isclass_or_instance(c.item, items.BowserRecruit)) or (world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.toadstool) and utils.isclass_or_instance(c.item, items.ToadstoolRecruit)):
                        world.prepend_bits(201, [[0x7066, 3], [0x706E, 3]])
                elif utils.isclass_or_instance(c, chests.MarrymoreCharacter):
                    character_order[4] = c.item
                    world.search_replace_dialog("`MARRYMORE_CHARACTER`", c.item.description)
                    random_character = random.choice([i.description for i in [items.MarioRecruit, items.MallowRecruit, items.GenoRecruit, items.BowserRecruit, items.ToadstoolRecruit] if not utils.isclass_or_instance(c.item, i)])
                    world.search_replace_dialog("`RANDOM_CHARACTER_NAME`", random_character)
                    if (world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.mario) and utils.isclass_or_instance(c.item, items.MarioRecruit)) or (world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.mallow) and utils.isclass_or_instance(c.item, items.MallowRecruit)) or (world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.geno) and utils.isclass_or_instance(c.item, items.GenoRecruit)) or (world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.bowser) and utils.isclass_or_instance(c.item, items.BowserRecruit)) or (world.settings.is_flag_value(flags.ForestMazeGate, ForestMazeGating.toadstool) and utils.isclass_or_instance(c.item, items.ToadstoolRecruit)):
                        world.prepend_bits(200, [[0x7066, 3], [0x706E, 3]])
                elif utils.isclass_or_instance(c, chests.ForestMazeCharacter):
                    character_order[2] = c.item
            elif not utils.isclass_or_instance(c, chests.MolevilleMinesCharacter): # replace with Toad if empty
                if utils.isclass_or_instance(c, chests.MarrymoreCharacter):
                    world.search_replace_dialog("`MARRYMORE_CHARACTER`", "Toad")
                    world.search_replace_dialog("`RANDOM_CHARACTER_NAME`", "Yoshi")

        # replace overworld sprites - in-game is replaced with toad or dyna if no char, but unused chars must always be in ending credits
        playable_character_order = copy.deepcopy(character_order)

        if world.settings.is_flag_enabled(flags.ShuffleCharacters):
            empty_char_indexes = []
            for ind, char in enumerate(character_order):
                if char is None:
                    empty_char_indexes.append(ind)
            remaining_chars = []
            for chrclass in [items.MarioRecruit, items.ToadstoolRecruit, items.BowserRecruit, items.MallowRecruit, items.GenoRecruit]:
                used = False
                for o in character_order:
                    if utils.isclass_or_instance(o, chrclass):
                        used = True
                if not used:
                    remaining_chars.append(chrclass)
            random.shuffle(remaining_chars)
            for ind, char in zip(empty_char_indexes, remaining_chars):
                character_order[ind] = char
        else:
            character_order = [items.MarioRecruit, items.ToadstoolRecruit, items.BowserRecruit, items.MallowRecruit, items.GenoRecruit]

        pickups = [None, chests.MushroomWayCharacter, chests.ForestMazeCharacter, chests.MolevilleMinesCharacter, chests.MarrymoreCharacter]
        print(character_order)
        print(playable_character_order)
        for cindex, (recruitable, ending, chest) in enumerate(zip(playable_character_order, character_order, pickups)):
            if chest is None:
                continue
            sprites = {}
            if (cindex == 0 and world.settings.is_flag_enabled(flags.PlayAsStarter)) or (utils.isclass_or_instance(ending, items.MarioRecruit) and not world.settings.is_flag_enabled(flags.PlayAsStarter)):
                sprites = ending.sprites_primary
            else:
                sprites = ending.sprites_secondary
            if recruitable is not None:
                if not ((utils.isclass_or_instance(chest, chests.ForestMazeCharacter) and utils.isclass_or_instance(recruitable, items.GenoRecruit)) or (utils.isclass_or_instance(chest, chests.MarrymoreCharacter) and utils.isclass_or_instance(recruitable, items.ToadstoolRecruit))):
                    for room_id, npc, eventscripts, actionscripts in chest.npcs:
                        # replace model
                        world.update_room_npc_property_by_id(room_id, npc, "model", recruitable.model)
                        # format scripts
                        for script_id in eventscripts:
                            for command_index, cmd in enumerate(world.eventscripts[script_id]):
                                if utils.is_animation_header(cmd, npc):
                                    world.eventscripts[script_id][command_index]["subscript"] = utils.sanitize_character_animation_script(sprites, cmd["subscript"], room_id)
                        for script_id in actionscripts:
                            world.actionscripts[script_id] = utils.sanitize_character_animation_script(sprites, world.actionscripts[script_id], room_id)
            elif not utils.isclass_or_instance(c, chests.MolevilleMinesCharacter):
                toad_sprites = {
                    "south": (0, 6, True),
                    "defend": (0, 1, True),
                    "face_north": (0, 1, False),
                    "face_south": (0, 0, False),
                    "shocked_loop": (0, 0, False),
                    "shocked_loop_backwards": (0, 1, False),
                    "shocked_backwards_sequence": (0, 1, False),
                    "crying": (0, 0, False),
                    "crying_backwards": (0, 1, False),
                    "looking_down_static": (0, 0, True),
                    "looking_down": (0, 0, False),
                    "floored": (0, 0, True),
                    "hurt": (0, 0, True),
                    "shaking_head": (0, 0, False),
                    "shaking_head_backward": (0, 1, False),
                    "sleeping": (0, 1, False),
                    "salute": (0, 0, False),
                    "distracted": (0, 0, False),
                    "displeased": (0, 1, False),
                    "challenge": (0, 1, False),
                }
                for room_id, npc, eventscripts, actionscripts in chest.npcs:
                    world.update_room_npc_property_by_id(room_id, npc, "model", 64)
                    for script_id in eventscripts:
                        for command_index, cmd in enumerate(world.eventscripts[script_id]):
                            if utils.is_animation_header(cmd, npc):
                                world.eventscripts[script_id][command_index]["subscript"] = utils.sanitize_character_animation_script(toad_sprites, cmd["subscript"], room_id)
                    for script_id in actionscripts:
                        for command_index, cmd in enumerate(world.actionscripts[script_id]):
                            world.actionscripts[script_id] = utils.sanitize_character_animation_script(toad_sprites, world.actionscripts[script_id], room_id)
            for room_id, npc, eventscripts, actionscripts in chest.credits_npcs:
                world.update_room_npc_property_by_id(room_id, npc, "model", ending.model)
                for script_id in eventscripts:
                    for command_index, cmd in enumerate(world.eventscripts[script_id]):
                        if utils.is_animation_header(cmd, npc):
                            world.eventscripts[script_id][command_index]["subscript"] = utils.sanitize_character_animation_script(sprites, cmd["subscript"], room_id)
                for script_id in actionscripts:
                    world.actionscripts[script_id] = utils.sanitize_character_animation_script(sprites, world.actionscripts[script_id], room_id)

        # update the sprites in the world models
        if not utils.isclass_or_instance(character_order[0], items.MarioRecruit) and world.settings.is_flag_enabled(flags.PlayAsStarter):
            mario_models = [(index, copy.deepcopy(m)) for (index, m) in enumerate(world.models) if m is not None and m["sprite"] in characters.Mario.original_weapon_sprite_ids]
            if utils.isclass_or_instance(character_order[0], items.MallowRecruit):
                nc = characters.Mallow
                ni = items.MallowRecruit
            elif utils.isclass_or_instance(character_order[0], items.GenoRecruit):
                nc = characters.Geno
                ni = items.GenoRecruit
            elif utils.isclass_or_instance(character_order[0], items.BowserRecruit):
                nc = characters.Bowser
                ni = items.BowserRecruit
            else:
                nc = characters.Peach
                ni = items.ToadstoolRecruit
            incoming_models = [(index, copy.deepcopy(m)) for (index, m) in enumerate(world.models) if m is not None and m["sprite"] in nc.original_weapon_sprite_ids]
            replacements = zip(characters.Mario.original_weapon_sprite_ids, nc.original_weapon_sprite_ids)
            for mario, incoming in replacements:
                if mario is not None and incoming is not None:
                    for m_i, m in mario_models:
                        if m["sprite"] == mario:
                            m["sprite"] = incoming
                            m["vram_store"] = 0
                            world.models[m_i] = m
                    for m_i, m in incoming_models:
                        if m["sprite"] == incoming:
                            m["sprite"] = mario
                            m["vram_store"] = 7
                            world.models[m_i] = m
            # jinx dojo
            for script_id in [2066, 2068, 2076, 2077]:
                for command_index, cmd in enumerate(world.eventscripts[script_id]):
                    if utils.is_animation_header(cmd, 0):
                        world.eventscripts[script_id][command_index]["subscript"] = utils.sanitize_character_animation_script(ni.sprites_primary, cmd["subscript"], room_id)
        

        # chests
        for c in [x for x in world.chest_locations if not utils.isclass_or_instance(x, chests.OverworldItem)] + [x for x in world.freestanding_item_locations if not utils.isclass_or_instance(x, chests.OverworldItem) and not utils.isclass_or_instance(x, chests.SunkenShipCoinSnake)]:
            if c.event is not None and c.event not in grant_builders:
                grant_builders[c.event] = {
                    "jumps": [],
                    "executions": []
                }
                if utils.isclass_or_instance(c, chests.OverworldItem):
                    grant_builders[c.event]["jumps"].append(utils.new_command(c.event, 'set_7000_to_current_level'))
            if c.item is not None and not utils.isclass_or_instance(c, chests.FrogCoinShopItem):
                for d in c.dialogs_to_replace:
                    for id, dat in c.item.dialog_replacements:
                        if d == id:
                            world.replace_dialog(id, dat)
                cmds = []
                # physical chests
                if utils.isclass_or_instance(c, chests.Chest): 
                    # slot machines - doesn't take a 70A7 value
                    if utils.isclass_or_instance(c.item, items.SlotMachineChest): 
                        for i, r in enumerate(c.rooms):
                            # count NPCs in room
                            ctr = world.get_npc_count_by_room_id(r)
                            # insert a slot machine script with the NPC IDs adjusted to this room
                            slot_logic = copy.deepcopy([{**s} for s in slot_machine_commands])
                            for j, cmd in enumerate(slot_logic):
                                if cmd["command"] in ["stop_embedded_action_script", "pause_action_script", "set_action_script_sync", "summon_to_current_level", "action_queue_async", "action_queue_sync", "remove_from_current_level"] and cmd["args"][0] >= 0x16 and cmd["args"][0] <= 0x1A:
                                    cmd["args"][0] = cmd["args"][0] - 2 + ctr
                                elif cmd["command"] == "start_battle":
                                    battlefield = None
                                    for b_f in bosses.battlefield_room_table:
                                        if r in b_f[1]:
                                            battlefield = b_f[0]
                                            break
                                    for b_l in world.boss_locations:
                                        if utils.isclass_or_instance(b_l, bosses.BoxBoy):
                                            cmd["args"][0] = b_l.boss.pack_number
                                            if b_l.formation.required_battlefield is not None:
                                                battlefield = b_l.formation.required_battlefield
                                            cmd["args"][1] = battlefield
                                            break
                                slot_logic[j] = cmd

                            old_new_identifiers = {}
                            # prefix the event identifiers correctly
                            for cmd in slot_logic:
                                old_new_identifiers[cmd["identifier"]] = 'EVENT_%i_%i_%s' % (c.event, r, cmd["identifier"])
                            for index, cmd in enumerate(slot_logic):
                                if cmd["identifier"] in old_new_identifiers:
                                    slot_logic[index]["identifier"] = old_new_identifiers[cmd["identifier"]]
                            for old_id in old_new_identifiers:
                                for index, cmd in enumerate(slot_logic):
                                    if "args" in cmd and old_id in cmd["args"]:
                                        cmdindex = cmd["args"].index(old_id)
                                        slot_logic[index]["args"][cmdindex] = old_new_identifiers[old_id]
                            # add slot machine NPCs to this room
                            cmds.extend(copy.deepcopy([{**s} for s in slot_logic]))
                            world.rooms[r]["objects"].extend(slot_machine_npcs)
                            jmp = utils.new_command(c.event, 'jmp_if_7000_equals_short', [r, cmds[0]["identifier"]])
                            grant_builders[c.event]["jumps"].append(jmp)
                        grant_builders[c.event]["executions"].extend(cmds)
                    # mimics - update battlefield
                    elif utils.isclass_or_instance(c.item, items.PandoriteFight) or utils.isclass_or_instance(c.item, items.HidonFight) or utils.isclass_or_instance(c.item, items.BoxBoyFight):
                        battlefield = None
                        for b_f in bosses.battlefield_room_table:
                            if c.rooms[0] in b_f[1]:
                                battlefield = b_f[0]
                                break
                        boss = None
                        pack_number = None
                        for b_l in world.boss_locations:
                            if (utils.isclass_or_instance(c.item, items.PandoriteFight) and utils.isclass_or_instance(b_l, bosses.Pandorite)) or (utils.isclass_or_instance(c.item, items.HidonFight) and utils.isclass_or_instance(b_l, bosses.Hidon)) or (utils.isclass_or_instance(c.item, items.BoxBoyFight) and utils.isclass_or_instance(b_l, bosses.BoxBoy)):
                                pack_number = b_l.boss.pack_number
                                boss = b_l.boss
                                if b_l.formation.required_battlefield is not None:
                                    battlefield = b_l.formation.required_battlefield
                                break
                        if boss is not None:
                            for cmd_index, cmd in enumerate(world.eventscripts[353]):
                                if cmd["command"] == "start_battle" and cmd["args"][0] == pack_number:
                                    cmd["args"][1] = battlefield
                                    world.eventscripts[353][cmd_index] = cmd
                                    break
                        # add jumps
                        cmds.append(utils.new_command(c.event, 'jmp_to_event', [c.item.get_chest_event(c.event)]))
                        grant_builders[c.event]["executions"].extend(cmds)
                        for r in c.rooms:
                            jmp = utils.new_command(c.event, 'jmp_if_7000_equals_short', [r, cmds[0]["identifier"]])
                            grant_builders[c.event]["jumps"].append(jmp)
                    else:
                        if c.manual_70A7 or len([r for r in c.rooms if r > 509]) > 0:
                            # set 70A7 manually if chest is used multiple times
                            manual_70A7 = (c.item.chest_70A7_upper << 4) + c.item.chest_70A7_lower
                            cmds.append(utils.new_command(c.event, 'set', [0x70A7, manual_70A7]))
                        else:
                            # set 70A7 on chest itself
                            for r, npc_id in zip(c.rooms, c.npc_ids):
                                world.update_room_npc_property_by_id(r, npc_id, "item_offset", c.item.chest_70A7_upper)
                                world.update_room_npc_property_by_id(r, npc_id, "star_offset", c.item.chest_70A7_lower)
                        if utils.isclass_or_instance(c.item, items.Coins) or utils.isclass_or_instance(c.item, items.MultiFrogCoin):
                            cmds.append(utils.new_command(c.event, 'set', [0x70BC, c.item.multiplier]))
                        elif utils.isclass_or_instance(c.item, items.StarPiece):
                            hint_variable, hint_bit = c.item.hint_bit
                            cmds.append(utils.new_command(c.event, 'set_bit', [hint_variable, hint_bit]))
                            cmds.append(utils.new_command(c.event, 'run_event_as_subroutine', [3092]))
                        # jump based on type
                        if world.settings.is_flag_value(flags.QuickHitCoins, True) and (utils.isclass_or_instance(c.item, items.Coins) or utils.isclass_or_instance(c.item, items.MultiFrogCoin)):
                            cmds.append(utils.new_command(c.event, 'jmp_to_event', [c.item.quick_chest_event]))
                        elif c.item.chest_event:
                            evt = c.item.get_chest_event(c.event)
                            if evt == 3089:
                                evt = c.item.model.chest_event
                                for r in c.rooms:
                                    if r in [242]:
                                        evt = 883
                            cmds.append(utils.new_command(c.event, 'jmp_to_event', [evt]))
                        # add jumps
                        grant_builders[c.event]["executions"].extend(cmds)
                        for r in c.rooms:
                            jmp = utils.new_command(c.event, 'jmp_if_7000_equals_short', [r, cmds[0]["identifier"]])
                            grant_builders[c.event]["jumps"].append(jmp)
                # npc rewards
                else:
                    # starter items
                    if utils.isclass_or_instance(c, chests.StarterItem):
                        world.eventscripts[2497].insert(0, utils.new_command(2497, 'put_inventory', [c.item.index]))
                    else:
                        if utils.isclass_or_instance(c.item, items.RegularItem):
                            # set 70A7 for granting a normal item
                            cmds.append(utils.new_command(c.event, 'set', [0x70A7, c.item.chest_70A7_lower]))
                        elif utils.isclass_or_instance(c.item, items.Coins) or utils.isclass_or_instance(c.item, items.MultiFrogCoin):
                            # set 7000 for quantity
                            cmds.append(utils.new_command(c.event, 'set', [0x7000, c.item.amount]))
                        if utils.isclass_or_instance(c, chests.OverworldItem):
                            this_event = c.item.overworld_event
                        else:
                            this_event = c.item.npc_event
                        if utils.isclass_or_instance(c.item, items.StarPiece):
                            hint_variable, hint_bit = c.item.hint_bit
                            cmds.append(utils.new_command(c.event, 'set_bit', [hint_variable, hint_bit]))
                            cmds.append(utils.new_command(c.event, 'run_event_as_subroutine', [3092]))
                        
                        cmds.append(utils.new_command(c.event, 'jmp_to_event', [this_event]))
                        grant_builders[c.event]["executions"].extend(cmds)
                        for r in c.rooms:
                            jmp = utils.new_command(c.event, 'jmp_if_7000_equals_short', [r, cmds[0]["identifier"]])
                            grant_builders[c.event]["jumps"].append(jmp)
                        # coin snake considerations
                        if utils.isclass_or_instance(c, chests.SunkenShipCoinSnake):
                            model_id = c.item.model.model
                            action_script = c.item.model.action_script
                            for r, npc_id in zip(c.rooms, c.npc_ids):
                                world.update_room_npc_property_by_id(r, npc_id, "model", model_id)
                            # set the right sequence on the object in AS 199 and 200
                            action_script_contents = copy.deepcopy([{**s} for s in world.actionscripts[action_script] if s["command"] != "ret"])
                            for ind in [199, 200]:
                                as_ = copy.deepcopy([{**s} for s in world.actionscripts[ind]])
                                as_.pop()
                                working_script = [{**a, "identifier": a["identifier"].replace("ACTION_%i_"%str(action_script), "ACTION_%i_"%str(ind))} for a in action_script_contents] + as_
                                for subs_index, sub_cmd in enumerate(working_script):
                                    if "args" in sub_cmd:
                                        for sub_cmd_arg_index, sub_cmd_arg in enumerate(sub_cmd["args"]):
                                            if type(sub_cmd_arg) == str:
                                                sub_cmd["args"][sub_cmd_arg_index] = sub_cmd_arg.replace("ACTION_%i_"%str(action_script), "ACTION_%i_"%str(ind))
                                        working_script[subs_index] = sub_cmd
                                world.actionscripts[ind] = working_script
                            # remove coin sequences if necessary
                            if not utils.isclass_or_instance(c.item, items.Coins) and not utils.isclass_or_instance(c.item, items.FrogCoin) and not utils.isclass_or_instance(c.item, items.MultiFrogCoin):
                                e_3215 = copy.deepcopy([{**s} for s in world.eventscripts[3215]])
                                for command_index in range(len(e_3215)):
                                    command = e_3215[command_index]
                                    if "subscript" in command:
                                        subscript = [ss for ss in command["subscript"] if ss["command"] != 'set_sprite_sequence']
                                        e_3215[command_index]["subscript"] = subscript
                                e_3216 = copy.deepcopy([{**s} for s in world.eventscripts[3216]])
                                for command_index in range(len(e_3216)):
                                    command = e_3216[command_index]
                                    if "subscript" in command:
                                        subscript = [ss for ss in command["subscript"] if ss["command"] != 'set_sprite_sequence']
                                        e_3216[command_index]["subscript"] = subscript
                                world.eventscripts[3215] = e_3215
                                world.eventscripts[3216] = e_3216
            elif utils.isclass_or_instance(c, chests.Chest) and c.item is None:
                if world.settings.is_flag_enabled(flags.AnnoyingChests):
                    c.item = items.YouMissed
                else:
                    # disable empty chests
                    if utils.isclass_or_instance(c, chests.BowsersKeepDoorReward1):
                        world.eventscripts[192][0:0] = [
                            {"identifier": 'EVENT_192_set_bk_1', "command": 'set', "args": [0x7000, 512]},
                            {"identifier": 'EVENT_192_set_bk_1_', "command": 'set_mem_704x_at_7000_bit'}
                        ]
                    elif utils.isclass_or_instance(c, chests.BowsersKeepDoorReward2):
                        world.eventscripts[192][0:0] = [
                            {"identifier": 'EVENT_192_set_bk_2', "command": 'set', "args": [0x7000, 513]},
                            {"identifier": 'EVENT_192_set_bk_2_', "command": 'set_mem_704x_at_7000_bit'}
                        ]
                    elif utils.isclass_or_instance(c, chests.BowsersKeepDoorReward3):
                        world.eventscripts[192][0:0] = [
                            {"identifier": 'EVENT_192_set_bk_3', "command": 'set', "args": [0x7000, 514]},
                            {"identifier": 'EVENT_192_set_bk_3_', "command": 'set_mem_704x_at_7000_bit'}
                        ]
                    elif utils.isclass_or_instance(c, chests.BowsersKeepDoorReward4):
                        world.eventscripts[192][0:0] = [
                            {"identifier": 'EVENT_192_set_bk_4', "command": 'set', "args": [0x7000, 515]},
                            {"identifier": 'EVENT_192_set_bk_4_', "command": 'set_mem_704x_at_7000_bit'}
                        ]
                    elif utils.isclass_or_instance(c, chests.BowsersKeepDoorReward5):
                        world.eventscripts[192][0:0] = [
                            {"identifier": 'EVENT_192_set_bk_5', "command": 'set', "args": [0x7000, 516]},
                            {"identifier": 'EVENT_192_set_bk_5_', "command": 'set_mem_704x_at_7000_bit'}
                        ]
                    elif utils.isclass_or_instance(c, chests.BowsersKeepDoorReward6):
                        world.eventscripts[192][0:0] = [
                            {"identifier": 'EVENT_192_set_bk_6', "command": 'set', "args": [0x7000, 517]},
                            {"identifier": 'EVENT_192_set_bk_6_', "command": 'set_mem_704x_at_7000_bit'}
                        ]
                    elif utils.isclass_or_instance(c, chests.PandoriteReward2):
                        world.eventscripts[3124].insert(0, utils.new_command(3124, "disable_trigger", [AreaObjects.MEM_70A8]))
                    elif utils.isclass_or_instance(c, chests.HidonReward2):
                        world.eventscripts[3126].insert(0, utils.new_command(3126, "disable_trigger", [AreaObjects.MEM_70A8]))
                    elif utils.isclass_or_instance(c, chests.KeroSewersBeforeBelomeUpper2):
                        world.eventscripts[1582] = [scr for scr in world.eventscripts[1582] if scr["command"] != 'enable_trigger_in_level']
                    else:
                        for chest_npc, chest_level in zip(c.npc_ids, c.rooms):
                            world.eventscripts[192].insert(0, utils.new_command(192, 'disable_trigger_in_level', [0x14 + chest_npc, chest_level]))

                
                                
        # freestanding items
        for c in [x for x in world.freestanding_item_locations if utils.isclass_or_instance(x, chests.OverworldItem)] + [x for x in world.chest_locations if utils.isclass_or_instance(x, chests.OverworldItem) or utils.isclass_or_instance(x, chests.SunkenShipCoinSnake)]:
            # print (c)
            if c.event is not None and c.event not in grant_builders:
                grant_builders[c.event] = {
                    "jumps": [],
                    "executions": []
                }
                if utils.isclass_or_instance(c, chests.OverworldItem):
                    grant_builders[c.event]["jumps"].append(utils.new_command(c.event, 'set_7000_to_current_level'))
            if c.item is not None:
                for d in c.dialogs_to_replace:
                    for id, dat in c.item.dialog_replacements:
                        if d == id:
                            world.replace_dialog(id, dat)
                cmds = []
                if utils.isclass_or_instance(c, chests.PacketItem): 
                    # generate the right packet for the item
                    generator = copy.deepcopy([{**s} for s in world.eventscripts[c.script_id]])
                    if c.preferred == PacketType.Falling:
                        packetType = c.item.model.falling_packet
                    else:
                        packetType = c.item.model.static_packet
                    generator[0]["args"][0] = packetType
                    world.eventscripts[c.script_id] = generator
                else:
                    if not (utils.isclass_or_instance(c.item, items.Coins) or utils.isclass_or_instance(c.item, items.FrogCoin) and c.description in world.settings.get_flag(flags.EnabledFreestandingChecks).enabled):
                        # set the NPC and action script for the item if it's NOT an excluded COIN overworld item location
                        model_id = c.item.model.model
                        action_script = c.item.model.action_script
                        is_floating = c.item.model.hover
                        for r, npc_id in zip(c.rooms, c.npc_ids):
                            # special case for rooms that have a lot of big sprites
                            if r in [125] and model_id not in [499, 194, 195, 111, 196]:
                                model_id = 111
                                action_script = 773
                                is_floating = False
                            world.update_room_npc_property_by_id(r, npc_id, "model", model_id)
                            world.update_room_npc_property_by_id(r, npc_id, "action_script", action_script)
                            world.update_room_npc_property_by_id(r, npc_id, "z_half", is_floating)
                # sett the item grant
                if utils.isclass_or_instance(c.item, items.StarPiece):
                    hint_variable, hint_bit = c.item.hint_bit
                    cmds.append(utils.new_command(c.event, 'set_bit', [hint_variable, hint_bit]))
                    cmds.append(utils.new_command(c.event, 'run_event_as_subroutine', [3092]))
                if utils.isclass_or_instance(c.item, items.RegularItem):
                    # set 70A7 for granting a normal item
                    cmds.append(utils.new_command(c.event, 'set', [0x70A7, c.item.chest_70A7_lower]))
                if utils.isclass_or_instance(c, chests.MidasRiverTunnelItem): 
                    # midas river grant
                    cmds.append(utils.new_command(c.event, 'jmp_to_event', [c.item.overworld_midas_event]))
                    # make sure midas river item's forced action script references the appropriate sequence setter subroutine for the item itself
                    new_midas_cmd = []
                    for as_index, cmd in enumerate(world.actionscripts[c.midas_action_script]):
                        if cmd["command"] == 'jmp_to_subroutine':
                            cmd["args"][0] = world.actionscripts[c.item.model.action_script][0]["identifier"]
                            new_midas_cmd.append(cmd)
                        elif cmd["command"] != 'set_sprite_sequence' and not utils.isclass_or_instance(c.item, items.Coins) and not utils.isclass_or_instance(c.item, items.FrogCoin):
                            new_midas_cmd.append(cmd)
                    world.actionscripts[c.midas_action_script] = new_midas_cmd
                elif utils.isclass_or_instance(c, chests.BoosterTowerMasher) or not utils.isclass_or_instance(c, chests.OverworldItem): 
                    # npc grants that should be treated as overworld items
                    cmds.append(utils.new_command(c.event, 'jmp_to_event', [c.item.npc_event]))
                else:
                    # all other overworld item grant
                    cmds.append(utils.new_command(c.event, 'jmp_to_event', [c.item.overworld_event]))
                grant_builders[c.event]["executions"].extend(cmds)
                # generate room-based jumps
                for r in c.rooms:
                    jmp = utils.new_command(c.event, 'jmp_if_7000_equals_short', [r, cmds[0]["identifier"]])
                    grant_builders[c.event]["jumps"].append(jmp)
                # edit action script if midas tunnel #3 item is not a coin
                if utils.isclass_or_instance(c, chests.MidasRiverBottomLeftCave) and not utils.isclass_or_instance(c.item, items.Coins) and not utils.isclass_or_instance(c.item, items.FrogCoin):
                    world.actionscripts[298] = [a for a in world.actionscripts[298] if a["command"] != 'set_sprite_sequence']
                # for elder key, need to forcefully set the sequence/mold of the item in script 1335
                if utils.isclass_or_instance(c, chests.BoosterTowerPortraits):
                    action_script_contents = [{**a, "identifier": "EVENT_1335_" + a["identifier"]} for a in world.actionscripts[c.item.model.action_script] if a["command"] != "ret"]
                    for i, command in enumerate(world.eventscripts[1335]):
                        if utils.is_animation_header(command, 7):
                            command["subscript"] = copy.deepcopy([{**s} for s in action_script_contents])
                            for subs_index, sub_cmd in enumerate(command["subscript"]):
                                if "args" in sub_cmd:
                                    for sub_cmd_arg_index, sub_cmd_arg in enumerate(sub_cmd["args"]):
                                        if type(sub_cmd_arg) == str:
                                            sub_cmd["args"][sub_cmd_arg_index] = "EVENT_1335_" + sub_cmd_arg
                                    command["subscript"][subs_index] = sub_cmd
                            world.eventscripts[1335][i] = command
                            break # only apply to first command
                # for booster tower, need to do the same
                if utils.isclass_or_instance(c, chests.BoosterTowerMasher):
                    for i, command in enumerate(world.eventscripts[2342]):
                        if command["command"] == "set_action_script_sync" and (command["args"][0] - 0x14) in c.npc_ids:
                            command["args"][1] = c.item.model.action_script
                            world.eventscripts[2342][i] = command
                            break # only apply to first command
            elif utils.isclass_or_instance(c, chests.BoosterTowerMasher):
                # disable empty chests
                world.eventscripts[192].insert(0, utils.new_command(192, 'disable_trigger_in_level', [0x14, 197]))
                world.prepend_bits(192, [[0x7048, 0]])


        # boss star pieces
        for c in world.boss_star_checks:
            if c.event is not None and c.event not in grant_builders:
                grant_builders[c.event] = {
                    "jumps": [utils.new_command(c.event, 'inc', [0x70E6])],
                    "executions": []
                }
            if c.item is not None:
                for d in c.dialogs_to_replace:
                    for id, dat in c.item.dialog_replacements:
                        if d == id:
                            world.replace_dialog(id, dat)
                hint_variable, hint_bit = c.item.hint_bit
                grant_builders[c.event]["executions"].append(utils.new_command(c.event, 'set_bit', [hint_variable, hint_bit]))
                grant_builders[c.event]["executions"].append(utils.new_command(c.event, 'run_event_as_subroutine', [3092]))
                cmd = utils.new_command(c.event, 'jmp_to_event', [3092])
                grant_builders[c.event]["executions"].append(cmd)
                for r in c.rooms:
                    jmp = utils.new_command(c.event, 'jmp_if_7000_equals_short', [r, cmd["identifier"]])
                    grant_builders[c.event]["jumps"].append(jmp)
            elif utils.isclass_or_instance(c, chests.StarHillStarPiece1):
                # remove freestanding star if empty
                world.eventscripts[2405].pop(0)
                
        # finalize granter scripts
        for e in grant_builders:
            grant_builders[e]["jumps"].append(utils.new_command(e, "ret"))
            world.eventscripts[e] = copy.deepcopy([{**s} for s in grant_builders[e]["jumps"]]) + copy.deepcopy([{**s} for s in grant_builders[e]["executions"]])

        # if star piece signal ring hints turned on, set the appropriate bit checks in each area
        if world.settings.is_flag_value(flags.StarPieceHints, True):
            for c in world.recruitable_character_checks + world.chest_locations + world.freestanding_item_locations + world.boss_star_checks:
                if c.item is not None and utils.isclass_or_instance(c.item, items.StarPiece):
                    #print(c.area, c.name, c.item)
                    hint_event = None
                    if c.area == Area.MariosPad:
                        hint_event = 3887
                    elif c.area == Area.MushroomWay:
                        hint_event = 3888
                    elif c.area == Area.MushroomKingdom:
                        hint_event = 3889
                    elif c.area == Area.BanditsWay:
                        hint_event = 3890
                    elif c.area == Area.KeroSewers:
                        hint_event = 3891
                    elif c.area == Area.MidasRiver:
                        hint_event = 3892
                    elif c.area == Area.TadpolePond:
                        hint_event = 3893
                    elif c.area == Area.RoseWay:
                        hint_event = 3894
                    elif c.area == Area.RoseTown:
                        hint_event = 3895
                    elif c.area == Area.ForestMaze:
                        hint_event = 3896
                    elif c.area == Area.Moleville or c.area == Area.MolevilleMines:
                        hint_event = 3897
                    elif c.area == Area.BoosterPass:
                        hint_event = 3898
                    elif c.area == Area.BoosterTower:
                        hint_event = 3899
                    elif c.area == Area.PipeVault:
                        hint_event = 3900
                    elif c.area == Area.YosterIsle:
                        hint_event = 3901
                    elif c.area == Area.Marrymore:
                        hint_event = 3902
                    elif c.area == Area.StarHill:
                        hint_event = 3903
                    elif c.area == Area.SeasideTown:
                        hint_event = 3904
                    elif c.area == Area.Sea:
                        hint_event = 3905
                    elif c.area == Area.SunkenShip:
                        hint_event = 3906
                    elif c.area == Area.LandsEnd:
                        hint_event = 3907
                    elif c.area == Area.BelomeTemple:
                        hint_event = 3908
                    elif c.area == Area.MonstroTown:
                        hint_event = 3909
                    elif c.area == Area.Casino:
                        hint_event = 3910
                    elif c.area == Area.BeanValley:
                        hint_event = 3911
                    elif c.area == Area.NimbusLand:
                        hint_event = 3912
                    elif c.area == Area.BarrelVolcano:
                        hint_event = 3913
                    elif c.area == Area.BowsersKeep:
                        hint_event = 3914
                    elif c.area == Area.Factory:
                        hint_event = 3915
                    elif c.area == Area.InnerFactory:
                        hint_event = 3916
                    if hint_event is not None:
                        # get name of sound command
                        sound_command = [cmd for cmd in world.eventscripts[hint_event] if cmd["command"] == 'play_sound'][0]
                        hint_var, hint_bit = c.item.hint_bit
                        world.eventscripts[hint_event].insert(0, utils.new_command(hint_event, "jmp_if_bit_clear", [hint_var, hint_bit, sound_command["identifier"]]))



def get_spoiler(world):
    acc = []
    
    for location in world.starter_character_checks + world.recruitable_character_checks + world.spotted_character_checks + world.boss_star_checks + world.chest_locations + world.freestanding_item_locations:
        if isinstance(location, chests.InvisibleFlagLocation):
            acc.append(location.name)

    return acc