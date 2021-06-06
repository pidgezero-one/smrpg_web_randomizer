# Chest randomization logic.

import math
import random

from randomizer.data import items, locations, chests
from randomizer.data.keys import KeyItemLocation
from randomizer.logic import flags, keys
from randomizer.logic.flags import PlayableCharacters, BanditsWayGating, ForestMazeGating, BoosterTowerGating, SeaGating
from . import utils


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


def _place_items(world, items, locations, base_inventory=None):
    """Place the given list of items within the given locations, and optionally a given starting inventory.

    Args:
        world (randomizer.logic.main.GameWorld):
        items (Inventory):
        locations (list[randomizer.data.locations.ItemLocation]):
        base_inventory (Inventory):

    """
    if base_inventory is None:
        base_inventory = Inventory()

    remaining_fill_items = Inventory(items)

    if len(remaining_fill_items) > len([l for l in locations if not l.has_item]):
        raise ValueError("Trying to fill more items than available locations")

    # For each required item, place it assuming we can get all other items.
    for item in items:
        # Get items we can get assuming we have everything but the one we're placing.
        remaining_fill_items.remove(item)
        assumed_items = _collect_items(
            world, remaining_fill_items + base_inventory)

        fillable_locations = [l for l in locations if not l.has_item and l.can_access(assumed_items)
                              and l.item_allowed(item)]
        if not fillable_locations:
            raise ValueError("No available locations for {}, {}".format(
                item, remaining_fill_items))

        # Place item in the first fillable location.
        fillable_locations[0].item = item


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

    # gonna need to modify this based on flags
    available_locations = [l for l in self.recruitable_character_checks + self.starter_character_checks +
                           self.chest_locations + self.freestanding_item_locations + self.boss_star_checks if l.has_item]

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

    # Shuffle locations, required items and extra items.
    random.shuffle(locations_to_fill)
    random.shuffle(required_items)
    random.shuffle(extra_items)

    # Place required items first.
    _place_items(world, required_items, locations_to_fill, existing_inventory)

    # Reverse remaining empty locations, then fill extra items.
    locations_to_fill = [l for l in locations_to_fill if not l.has_item]
    locations_to_fill.reverse()
    _place_items(world, extra_items, locations_to_fill, existing_inventory)

    # Sanity check to make sure we can collect all the items.
    collected_items = set(_collect_items(world))
    leftover = set(required_items + extra_items) - collected_items
    if leftover:
        raise ValueError("Items leftover from collection: {!r}, leftover {!r}".format(
            locations_to_fill, leftover))


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

def randomize_all(world):
    """

    Args:
        world (randomizer.logic.main.GameWorld): Game world to randomize.

    """


    # Open mode-specific shuffles.
    if world.open_mode:

        # Collect pool of locations that need item assignments
        locations_to_not_have_progression = world.settings.get_flag(flags.EnabledRegularChecks).disabled
        locations_to_completely_ignore = world.settings.get_flag(flags.EnabledFreestandingChecks).disabled
        bosses_to_veto = world.settings.get_flag(flags.EnabledBossChecks).disabled

        # Contents of excluded chests will still be shuffled, they just will not contain progression items.
        # Excluded freestanding items will remain vanilla.
        # Excluded boss checks will receive "None"
        # Character locations cannot be excluded, but will receive "None" if unassigned
        all_locations = world.chest_locations.copy() + 
            [c for c in world.freestanding_item_locations if c.description not in [e for e in locations_to_completely_ignore]] +
            world.boss_star_checks.copy()
            world.recruitable_character_checks.copy()
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
        if PlayableCharacters.Mario in world.settings.get_flag(flags.AvailableCharacters).disabled and (world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.RecruitMario) or world.settings.is_flag_value(flagsForestMazeGate, ForestMazeGating.FindMario) or world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.RecruitMario) or world.settings.is_flag_value(flags.SeaGate, SeaGating.RecruitMario)):
            raise Exception('cannot exclude Mario when required for area access')
        if PlayableCharacters.Mallow in world.settings.get_flag(flags.AvailableCharacters).disabled and (world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.RecruitMallow) or world.settings.is_flag_value(flagsForestMazeGate, ForestMazeGating.FindMallow) or world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.RecruitMallow) or world.settings.is_flag_value(flags.SeaGate, SeaGating.RecruitMallow)):
            raise Exception('cannot exclude Mallow when required for area access')
        if PlayableCharacters.Geno in world.settings.get_flag(flags.AvailableCharacters).disabled and (world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.RecruitGeno) or world.settings.is_flag_value(flagsForestMazeGate, ForestMazeGating.FindGeno) or world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.RecruitGeno) or world.settings.is_flag_value(flags.SeaGate, SeaGating.RecruitGeno)):
            raise Exception('cannot exclude Geno when required for area access')
        if PlayableCharacters.Bowser in world.settings.get_flag(flags.AvailableCharacters).disabled and (world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.RecruitBowser) or world.settings.is_flag_value(flagsForestMazeGate, ForestMazeGating.FindBowser) or world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.RecruitBowser) or world.settings.is_flag_value(flags.SeaGate, SeaGating.RecruitBowser)):
            raise Exception('cannot exclude Bowser when required for area access')
        if PlayableCharacters.Toadstool in world.settings.get_flag(flags.AvailableCharacters).disabled and (world.settings.is_flag_value(flags.BanditsWayGate, BanditsWayGating.RecruitToadstool) or world.settings.is_flag_value(flagsForestMazeGate, ForestMazeGating.FindToadstool) or world.settings.is_flag_value(flags.BoosterTowerGate, BoosterTowerGating.RecruitToadstool) or world.settings.is_flag_value(flags.SeaGate, SeaGating.RecruitToadstool)):
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
        required_item_pool = [i for i in world.items if i.is_key] +
            [c for c in world.recruitable_characters if c.description in charactersInSeed and c.description not in starting_characters]
        # add star pieces
        total_star_pieces = world.settings.get_flag(flags.TotalStarPieces).value
        required_item_pool += ([items.StarPiece] * total_star_pieces)
        # apply fireworks settings
        if self.world.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.ShuffleFireworks):
            required_item_pool.append(items.Fireworks)
        elif self.world.settings.is_flag_value(flags.FireworksSetting, FireworksOptions.ProgressiveFireworks):
            required_item_pool += ([items.ProgressiveFireworks] * 3)
            # consideration: two of these will not be able to make it into the key item pool

        extra_item_pool = []
        # items which should always only appear up to a certain # of times
        # progressive egg
        if not world.settings.is_flag_value(flags.ItemQuality, ItemQualities.Original):
            extra_item_pool += ([items.ProgressiveEgg] * 3)
        # bright card, if not a KI
        if world.settings.is_flag_value(flags.CasinoWarp, False):
            extra_item_pool.append(items.BrightCard)
        # beetlemania
        if world.settings.is_flag_value(flags.ShuffleBeetlemania, True):
            extra_item_pool.append(items.Beetlemania)
        # other items
        limited_items = [items.GoodieBag, items.YouMissed, items.SeeYa, items.EarlierTimes, items.SignalRing, items.StarEgg, items.Wallet]
        max_tier = get_max_item_quality(world)
        extra_item_pool += [i for i in limited_items if i.tier <= max_tier]
        # balanced only: populate extra_item_pool with existing item pool
        if world.settings.is_flag_value(flags.ItemQuality, ItemQualities.Original):
            extra_item_pool += [c.item for c in all_locations where c not in required_item_pool and c not in extra_item_pool]

        fill_locations(world, all_locations, required_item_pool, extra_item_pool, inventory)

    # fill in items. event generation can happen in main.py
    # do animations
    # will need to sub in characters for animations where no char is recruited (ie who goes in marrymore in a solo challenge?)

    # Get limitation of items allowed first
    tiers_allowed = 4
    if world.settings.is_flag_enabled(flags.ChestTier1):
        tiers_allowed = 1
    elif world.settings.is_flag_enabled(flags.ChestTier2):
        tiers_allowed = 2
    elif world.settings.is_flag_enabled(flags.ChestTier3):
        tiers_allowed = 3

    coins_allowed = not world.settings.is_flag_enabled(flags.ChestExcludeCoins)
    flowers_allowed = not world.settings.is_flag_enabled(
        flags.ChestExcludeFlowers)
    frogcoins_allowed = not world.settings.is_flag_enabled(
        flags.ChestExcludeFrogCoins)
    mushrooms_allowed = not world.settings.is_flag_enabled(
        flags.ChestExcludeMushrooms)
    stars_allowed = not world.settings.is_flag_enabled(flags.ChestExcludeStars)

    biased = world.settings.is_flag_enabled(flags.ChestShuffleBiased)
    include_key_items = world.settings.is_flag_enabled(
        flags.ChestIncludeKeyItems)

    coins = [items.Coins5, items.Coins8, items.Coins10, items.Coins150, items.Coins100, items.Coins50,
             items.CoinsDoubleBig]
    stars = [items.BanditsWayStar, items.KeroSewersStar, items.MolevilleMinesStar, items.SeaStar,
             items.LandsEndVolcanoStar, items.NimbusLandStar, items.LandsEndStar2, items.LandsEndStar3]

    # Items allowed for leftover chests where there is no valid item remaining for them (coins or mushroom).
    leftovers = coins[:]
    leftovers += [items.FrogCoin, items.RecoveryMushroom]

    forceCoinsInBanditsWay = False
    # special case: coins only if countdown in BW5 -- pre-set it in case B is set but T is not
    for location in world.boss_locations:
        if location.name in ["Croco1"]:
            for enemy in location.pack.common_enemies:
                if enemy.overworld_sprite is not None:
                    shuffled_boss = enemy
                    if shuffled_boss.name is "CountDown":
                        forceCoinsInBanditsWay = True
                        forced_coins = [chest for chest in world.chest_locations if isinstance(
                            chest, chests.BanditsWayCroco)]
                        forced_coins[0].item = random.choice(
                            [i for i in coins])

    # Open mode-specific shuffles.
    if world.open_mode:
        # Same area shuffle.
        if world.settings.is_flag_enabled(flags.ChestShuffle1):
            for area in locations.Area:
                group = [
                    chest for chest in world.chest_locations if chest.area == area]
                if group:
                    _intershuffle_chests(group)
            for chest in world.chest_locations:
                tiered_item = None
                for i in world.items:
                    if chest.item.index == i.index:
                        tiered_item = i
                if ((chest.item in coins and not coins_allowed) or (chest.item in stars and not stars_allowed) or
                        (chest.item == items.Flower and not flowers_allowed) or
                        (chest.item == items.RecoveryMushroom and not mushrooms_allowed) or
                        (chest.item == items.FrogCoin and not frogcoins_allowed) or
                        (tiered_item and tiered_item.hard_tier > tiers_allowed)):
                    # Put "You Missed!" empty item if allowed, otherwise just put some coins if this spot is empty.
                    if chest.item_allowed(items.YouMissed):
                        chest.item = items.YouMissed
                    elif chest.item_allowed(items.Mushroom):
                        chest.item = items.Mushroom
            if forceCoinsInBanditsWay:
                forced_coins = [chest for chest in world.chest_locations if isinstance(
                    chest, chests.BanditsWayCroco)]
                forced_coins[0].item = random.choice([i for i in coins])

        # Empty chests.
        elif world.settings.is_flag_enabled(flags.ChestShuffleEmpty):
            for chest in world.chest_locations:
                if chest.item_allowed(items.YouMissed):
                    chest.item = items.YouMissed

        elif (world.settings.is_flag_enabled(flags.ChestShuffleBiased) or
              world.settings.is_flag_enabled(flags.ChestShuffleChaos)):
            finished_chests = []
            items_already_in_chests = []

            # Here I'm just figuring out the rough distribution of each type to target.
            # We can consider mutating these probabilities.
            ratio_coins = len([chest for chest in world.chest_locations if
                               not isinstance(chest, chests.Reward) and chest.item in coins])
            ratio_frogcoins = len([chest for chest in world.chest_locations if
                                   not isinstance(chest, chests.Reward) and chest.item == items.FrogCoin]) - 2
            ratio_mushrooms = len([chest for chest in world.chest_locations if
                                   not isinstance(chest, chests.Reward) and chest.item == items.RecoveryMushroom])
            ratio_flowers = len([chest for chest in world.chest_locations if
                                 not isinstance(chest, chests.Reward) and chest.item == items.Flower]) - 8
            ratio_stars = len([chest for chest in world.chest_locations if
                               not isinstance(chest, chests.Reward) and chest.item in stars])
            ratio_items = len([chest for chest in world.chest_locations if
                               not isinstance(chest, chests.Reward) and chest.item not in coins and
                               chest.item not in stars and chest.item not in
                               [items.FrogCoin, items.RecoveryMushroom, items.Flower, items.YouMissed]])
            denominator = ratio_items

            # These are the relative ratios used to calculate distribution properties.
            # This is where we build the denominator.
            if coins_allowed:
                denominator += ratio_coins
            if flowers_allowed:
                denominator += ratio_flowers
            if mushrooms_allowed:
                denominator += ratio_mushrooms
            if stars_allowed:
                denominator += ratio_stars
            if frogcoins_allowed:
                denominator += ratio_frogcoins

            # factor in KIs allowed here
            total_chests = ratio_coins + ratio_frogcoins + \
                ratio_mushrooms + ratio_flowers + ratio_stars + ratio_items

            # How should items vs non-items be balanced?
            # Do stars first
            if stars_allowed:
                if world.settings.is_flag_enabled(flags.ChestRandomizeStars):
                    eligible_chests = [chest for chest in world.chest_locations if
                                       chest.item_allowed(items.BanditsWayStar)]
                    # randomize how many stars there will be - usually close to vanilla #
                    num_stars = utils.mutate_normal(min(
                        len(eligible_chests), math.floor(ratio_stars / denominator * total_chests)),
                        minimum=1, maximum=len(eligible_chests))
                    if num_stars > len(eligible_chests):
                        num_stars = len(eligible_chests)
                    while len(finished_chests) < num_stars:
                        chest = random.choice(eligible_chests)
                        if biased:
                            chest.item = random.choice(
                                [star for star in stars if star.hard_tier == chest.access])
                        else:
                            chest.item = random.choice(
                                [star for star in stars])
                        finished_chests.append(chest)
                        eligible_chests.remove(chest)
                        # Don't allow 2 stars in same bandits way room
                        if (isinstance(chest, chests.BanditsWayStarChest) or
                                isinstance(chest, chests.BanditsWayDogJump)):
                            for c in eligible_chests:
                                if (isinstance(c, chests.BanditsWayStarChest) or
                                        isinstance(c, chests.BanditsWayDogJump)):
                                    eligible_chests.remove(c)
                                    num_stars -= 1
                else:
                    eligible_chests = [
                        chest for chest in world.chest_locations if 201 <= chest.item.index <= 208]
                    for chest in eligible_chests:
                        finished_chests.append(chest)
                    for chest in eligible_chests:
                        eligible_chests.remove(chest)
                denominator -= ratio_stars

            if forceCoinsInBanditsWay:
                forced_coins = [chest for chest in world.chest_locations if isinstance(
                    chest, chests.BanditsWayCroco)]
                forced_coins[0].item = random.choice([i for i in coins])
                finished_chests.append(forced_coins[0])

            # then do the rest
            # biasing of items for chest
            def get_eligible_tier(chest_tier):
                selector = random.randint(1, 100)
                if chest_tier == 4:
                    if tiers_allowed == 4:
                        if selector < 88:
                            return 4
                        elif selector < 94:
                            return 3
                        elif selector < 98:
                            return 2
                        else:
                            return 1
                    elif tiers_allowed == 3:
                        if selector < 85:
                            return 3
                        elif selector < 96:
                            return 2
                        else:
                            return 1
                    elif tiers_allowed == 2:
                        if selector < 90:
                            return 2
                        else:
                            return 1
                    elif tiers_allowed == 1:
                        return 1
                elif chest_tier == 3:
                    if tiers_allowed == 4:
                        if selector < 85:
                            return 3
                        elif selector < 91:
                            return 2
                        elif selector < 97:
                            return 4
                        else:
                            return 1
                    elif tiers_allowed == 3:
                        if selector < 85:
                            return 3
                        elif selector < 96:
                            return 2
                        else:
                            return 1
                    elif tiers_allowed == 2:
                        if selector < 90:
                            return 2
                        else:
                            return 1
                    elif tiers_allowed == 1:
                        return 1
                elif chest_tier == 2:
                    if tiers_allowed == 4:
                        if selector < 85:
                            return 2
                        elif selector < 91:
                            return 3
                        elif selector < 97:
                            return 1
                        else:
                            return 4
                    elif tiers_allowed == 3:
                        if selector < 85:
                            return 2
                        elif selector < 96:
                            return 3
                        else:
                            return 1
                    elif tiers_allowed == 2:
                        if selector < 90:
                            return 1
                        else:
                            return 2
                    elif tiers_allowed == 1:
                        return 1
                elif chest_tier == 1:
                    if tiers_allowed == 4:
                        if selector < 85:
                            return 1
                        elif selector < 93:
                            return 2
                        elif selector < 98:
                            return 3
                        else:
                            return 4
                    elif tiers_allowed == 3:
                        if selector < 85:
                            return 1
                        elif selector < 96:
                            return 2
                        else:
                            return 3
                    elif tiers_allowed == 2:
                        if selector < 90:
                            return 1
                        else:
                            return 2
                    elif tiers_allowed == 1:
                        return 1

            excluded_items = [129, 137, 138]
            # Always exclude special equips from shops if Mx is set
            if world.settings.is_flag_enabled(flags.MonstroTownLite):
                monstro = [items.QuartzCharm, items.JinxBelt,
                           items.SuperSuit, items.AttackScarf, items.GhostMedal]
                monstro_locations = [i for i in world.chest_locations if
                                     isinstance(i, (chests.CulexReward, chests.JinxDojoReward, chests.SuperJumps30,
                                                    chests.SuperJumps100, chests.ThreeMustyFears)) and
                                     i not in finished_chests]
            elif world.settings.is_flag_enabled(flags.MonstroTownHard):
                monstro = [items.QuartzCharm, items.JinxBelt, items.SuperSuit, items.AttackScarf, items.GhostMedal,
                           items.FroggieStick, items.Chomp, items.ZoomShoes, items.LazyShellWeapon,
                           items.LazyShellArmor]
                monstro_locations = [i for i in world.chest_locations if
                                     isinstance(i, (chests.CulexReward, chests.JinxDojoReward, chests.SuperJumps30,
                                                    chests.SuperJumps100, chests.ThreeMustyFears,
                                                    chests.CricketPieReward, chests.BoosterTowerChomp,
                                                    chests.BoosterTowerZoomShoes, chests.GardenerCloud1,
                                                    chests.GardenerCloud2)) and
                                     i not in finished_chests]
            else:
                monstro = []
                monstro_locations = []

            chance = random.randint(1, 10)
            # 30% chance that 100 super jump will have the best of the 10 items
            if chance <= 3 and len(monstro) > 0:
                monstro.sort(key=lambda x: x.rank_value, reverse=True)
                item = monstro[1]
                location = [i for i in monstro_locations if isinstance(
                    i, chests.SuperJumps100)][0]
                location.item = item
                monstro.remove(item)
                monstro_locations.remove(location)
                finished_chests.append(location)
                if world.settings.is_flag_enabled(flags.MonstroExcludeElsewhere):
                    excluded_items.append(item.index)
                items_already_in_chests.append(item)

            while len(monstro) > 0:
                item = random.choice(monstro)
                location = random.choice(monstro_locations)
                location.item = item
                monstro.remove(item)
                monstro_locations.remove(location)
                finished_chests.append(location)
                if world.settings.is_flag_enabled(flags.MonstroExcludeElsewhere):
                    excluded_items.append(item.index)
                items_already_in_chests.append(item)

            # Then do key items....
            leftover_key_locations = []
            if include_key_items:
                key_item_locations = [
                    l for l in world.key_locations if keys.item_location_filter(world, l)]

                # Get items to place only from vanilla key item locations, not including other chests/rewards.
                required_items = keys.Inventory([l.item for l in key_item_locations if
                                                 l.item.shuffle_type == items.ItemShuffleType.Required])
                extra_items = keys.Inventory([l.item for l in key_item_locations if
                                              l.item.shuffle_type == items.ItemShuffleType.Extra])

                # Now add all the chest/reward spots to the location list if they haven't been done yet.
                # This excludes the Monstro Town locations if the M flag is on above.
                if not world.settings.is_flag_enabled(flags.ChestExcludeRewards):
                    chest_locations = [l for l in world.chest_locations if l not in finished_chests and
                                       keys.item_location_filter(world, l)]
                else:
                    chest_locations = [l for l in world.chest_locations if l not in finished_chests and
                                       keys.item_location_filter(world, l) and not isinstance(l, chests.Reward)]

                eligible_key_locations = key_item_locations + chest_locations

                # Do the fill, and mark any selected chests as done.
                fill_locations(
                    world, eligible_key_locations, required_items, extra_items)
                for location in eligible_key_locations:
                    if location.has_item:
                        finished_chests.append(location)
                    else:
                        leftover_key_locations.append(location)

            # Chest/reward list plus leftover key item locations from mixing shuffle.
            # Use this for all logic past this point!
            chests_plus_leftovers = world.chest_locations + leftover_key_locations

            # Then make sure wallet is found in exactly 1 chest
            if not world.settings.is_flag_enabled(flags.ChestExcludeRewards):
                eligible_wallet_locations = [
                    chest for chest in chests_plus_leftovers if chest not in finished_chests]
                chest = random.choice(eligible_wallet_locations)
                chest.item = items.Wallet
                finished_chests.append(chest)

            # Then make sure "You Missed" is found in exactly 1 chest
            eligible_empty_locations = [chest for chest in chests_plus_leftovers if chest not in finished_chests and
                                        not isinstance(chest, chests.Reward) and chest.item_allowed(items.YouMissed)]
            chest = random.choice(eligible_empty_locations)
            chest.item = items.YouMissed
            finished_chests.append(chest)

            # Then do the rest
            eligible_chests = [chest for chest in chests_plus_leftovers if
                               not isinstance(chest, (chests.Reward, chests.BowserDoorReward, KeyItemLocation)) and
                               chest not in finished_chests]
            eligible_rewards = [chest for chest in chests_plus_leftovers if
                                isinstance(chest, (chests.Reward, chests.BowserDoorReward, KeyItemLocation)) and
                                chest not in finished_chests]
            eligible_items = [i for i in world.items if i.index not in excluded_items and not i.is_key and
                              i.hard_tier <= tiers_allowed]

            while len(eligible_chests) > 0:
                chest = random.choice(eligible_chests)
                items_for_chest = [
                    i for i in eligible_items if chest.item_allowed(i)]

                if biased:
                    selected_tier = get_eligible_tier(chest.access)
                    adjusted_denominator = ratio_items
                    if coins_allowed and chest.item_allowed(items.Coins150):
                        adjusted_ratio_coins = ratio_coins
                    else:
                        adjusted_ratio_coins = 0

                    if flowers_allowed and chest.item_allowed(items.Flower):
                        adjusted_ratio_flowers = math.floor(
                            ratio_flowers / 1.5 / selected_tier)
                    else:
                        adjusted_ratio_flowers = 0

                    if mushrooms_allowed and chest.item_allowed(items.RecoveryMushroom):
                        adjusted_ratio_mushrooms = math.floor(
                            ratio_mushrooms / 1.5 / selected_tier)
                    else:
                        adjusted_ratio_mushrooms = 0

                    if frogcoins_allowed and chest.item_allowed(items.FrogCoin):
                        adjusted_ratio_frogcoins = math.floor(
                            ratio_frogcoins / 1.5 / selected_tier)
                    else:
                        adjusted_ratio_frogcoins = 0

                    adjusted_denominator += (adjusted_ratio_coins + adjusted_ratio_flowers + adjusted_ratio_mushrooms +
                                             adjusted_ratio_frogcoins)
                    selection = random.randint(1, adjusted_denominator)
                    if flowers_allowed and chest.item_allowed(items.Flower) and selection < adjusted_ratio_flowers:
                        chest.item = items.Flower
                    elif (mushrooms_allowed and chest.item_allowed(items.RecoveryMushroom) and
                          selection < adjusted_ratio_flowers + adjusted_ratio_mushrooms):
                        chest.item = items.RecoveryMushroom
                    elif (frogcoins_allowed and chest.item_allowed(items.FrogCoin) and
                          selection < adjusted_ratio_flowers + adjusted_ratio_mushrooms + adjusted_ratio_frogcoins):
                        chest.item = items.FrogCoin
                    elif (coins_allowed and selected_tier <= 2 and chest.item_allowed(items.Coins150) and
                          selection < adjusted_ratio_flowers + adjusted_ratio_mushrooms + adjusted_ratio_frogcoins +
                          adjusted_ratio_coins):
                        chest.item = random.choice(
                            [i for i in coins if i.hard_tier == selected_tier])
                    else:
                        # 50% chance of rerolling if item is an equip
                        proceed_repeat_item = False
                        while not proceed_repeat_item:
                            # If no possible items are allowed in this chest, make it coins instead.
                            possible_items = [
                                i for i in items_for_chest if i.hard_tier == selected_tier]
                            if not possible_items:
                                possible_items = [
                                    i for i in leftovers if chest.item_allowed(i)]
                            check_item = random.choice(possible_items)
                            if check_item.is_equipment:
                                fifty = random.choice([0, 1])
                                if fifty == 0:
                                    chest.item = check_item
                                    proceed_repeat_item = True
                            else:
                                chest.item = check_item
                                proceed_repeat_item = True
                else:
                    selection = random.randint(1, denominator)
                    if flowers_allowed and chest.item_allowed(items.Flower) and selection < ratio_flowers / 1.5:
                        chest.item = items.Flower
                    elif (mushrooms_allowed and chest.item_allowed(items.RecoveryMushroom) and
                          selection < ratio_flowers / 1.5 + ratio_mushrooms / 1.5):
                        chest.item = items.RecoveryMushroom
                    elif (frogcoins_allowed and chest.item_allowed(items.FrogCoin) and
                          selection < ratio_flowers / 1.5 + ratio_mushrooms / 1.5 + ratio_frogcoins / 1.5):
                        chest.item = items.FrogCoin
                    elif (coins_allowed and chest.item_allowed(items.Coins150) and
                          selection < ratio_flowers / 1.5 + ratio_mushrooms / 1.5 + ratio_frogcoins / 1.5 +
                          ratio_coins):
                        chest.item = random.choice(coins)
                    else:
                        tier_selection = random.randint(1, 100)
                        proceed_repeat_item = False
                        while not proceed_repeat_item:
                            if tiers_allowed == 4:
                                if tier_selection <= 40:
                                    possible_items = [
                                        i for i in items_for_chest if i.hard_tier == 1]
                                elif tier_selection <= 70:
                                    possible_items = [
                                        i for i in items_for_chest if i.hard_tier == 2]
                                elif tier_selection <= 90:
                                    possible_items = [
                                        i for i in items_for_chest if i.hard_tier == 3]
                                else:
                                    possible_items = [
                                        i for i in items_for_chest if i.hard_tier == 4]
                            elif tiers_allowed == 3:
                                if tier_selection <= 40:
                                    possible_items = [
                                        i for i in items_for_chest if i.hard_tier == 1]
                                elif tier_selection <= 75:
                                    possible_items = [
                                        i for i in items_for_chest if i.hard_tier == 2]
                                else:
                                    possible_items = [
                                        i for i in items_for_chest if i.hard_tier == 3]
                            elif tiers_allowed == 2:
                                if tier_selection <= 50:
                                    possible_items = [
                                        i for i in items_for_chest if i.hard_tier == 1]
                                else:
                                    possible_items = [
                                        i for i in items_for_chest if i.hard_tier == 2]
                            else:
                                possible_items = [
                                    i for i in items_for_chest if i.hard_tier == 1]

                            # If no possible items are allowed in this chest, make it coins instead.
                            if not possible_items:
                                possible_items = [
                                    i for i in leftovers if chest.item_allowed(i)]
                            check_item = random.choice(possible_items)

                            # 50% chance of rerolling if item is an equip
                            if check_item.is_equipment:
                                fifty = random.choice([0, 1])
                                if fifty == 0:
                                    chest.item = check_item
                                    proceed_repeat_item = True
                            else:
                                chest.item = check_item
                                proceed_repeat_item = True

                finished_chests.append(chest)
                eligible_chests.remove(chest)

            # If we excluded rewards, remove any reward spots that still have items.  Keep those that are empty because
            # they are left over key item locations from the shuffle above and do need items placed there!
            if world.settings.is_flag_enabled(flags.ChestExcludeRewards):
                eligible_rewards = [
                    r for r in eligible_rewards if not r.has_item]

            if eligible_rewards:
                while len(eligible_rewards) > 0:
                    chest = random.choice(eligible_rewards)
                    items_for_chest = [
                        i for i in eligible_items if chest.item_allowed(i)]

                    # For Cricket Jam reward, always give frog coins for now!  Just randomize the number.
                    if isinstance(chest, chests.CricketJamReward):
                        chest.item = items.FrogCoin
                        chest.num_frog_coins = random.randint(
                            5, random.randint(10, 20))
                    else:
                        proceed_repeat_item = False
                        while not proceed_repeat_item:
                            if biased:
                                selected_tier = get_eligible_tier(chest.access)
                                possible_items = [
                                    i for i in items_for_chest if i.hard_tier == selected_tier]
                            else:
                                tier_selection = random.randint(1, 100)
                                if tiers_allowed == 4:
                                    if tier_selection <= 35:
                                        possible_items = [
                                            i for i in items_for_chest if i.hard_tier == 3]
                                    elif tier_selection <= 60:
                                        possible_items = [
                                            i for i in items_for_chest if i.hard_tier == 2]
                                    elif tier_selection <= 85:
                                        possible_items = [
                                            i for i in items_for_chest if i.hard_tier == 4]
                                    else:
                                        possible_items = [
                                            i for i in items_for_chest if i.hard_tier == 1]
                                elif tiers_allowed == 3:
                                    if tier_selection <= 30:
                                        possible_items = [
                                            i for i in items_for_chest if i.hard_tier == 1]
                                    elif tier_selection <= 60:
                                        possible_items = [
                                            i for i in items_for_chest if i.hard_tier == 2]
                                    else:
                                        possible_items = [
                                            i for i in items_for_chest if i.hard_tier == 3]
                                elif tiers_allowed == 2:
                                    if tier_selection <= 50:
                                        possible_items = [
                                            i for i in items_for_chest if i.hard_tier == 1]
                                    else:
                                        possible_items = [
                                            i for i in items_for_chest if i.hard_tier == 2]
                                else:
                                    possible_items = [
                                        i for i in items_for_chest if i.hard_tier == 1]

                            # If no possible items are allowed in this chest, make it coins instead.
                            if not possible_items:
                                possible_items = [
                                    i for i in leftovers if chest.item_allowed(i)]
                            check_item = random.choice(possible_items)

                            if check_item not in items_already_in_chests or not check_item.is_equipment:
                                items_already_in_chests.append(check_item)
                                chest.item = check_item
                                proceed_repeat_item = True
                            else:
                                fifty = random.choice([0, 1])
                                if fifty == 0:
                                    chest.item = check_item
                                    proceed_repeat_item = True

                    finished_chests.append(chest)
                    eligible_rewards.remove(chest)

        # Replace any sellable items with closest coin equivalent.
        if world.settings.is_flag_enabled(flags.ReplaceItems):

            def closest_coins(n):
                num = n / 2
                diff = abs(num - 5)
                rv = items.Coins5
                if diff > abs(num - 8):
                    diff = abs(num - 8)
                    rv = items.Coins8
                if diff > abs(num - 10):
                    diff = abs(num - 10)
                    rv = items.Coins10
                if diff > abs(num - 20):
                    diff = abs(num - 20)
                    rv = items.CoinsDoubleBig
                if diff > abs(num - 50):
                    diff = abs(num - 50)
                    rv = items.Coins50
                if diff > abs(num - 100):
                    diff = abs(num - 100)
                    rv = items.Coins100
                if diff > abs(num - 150):
                    rv = items.Coins150
                return rv

            for chest in [i for i in world.chest_locations if not isinstance(i, chests.Reward)]:
                if chest.item.hard_tier == 1 and not chest.item.is_key and chest.item.price > 0:
                    if chest.item_allowed(items.Coins150) and not chest.item.frog_coin_item:
                        chest.item = closest_coins(chest.item.price)
                    elif chest.item_allowed(items.FrogCoin) and chest.item.frog_coin_item:
                        chest.item = items.FrogCoin
