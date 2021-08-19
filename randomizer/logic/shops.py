# Item/shop randomization logic

import random
import math
import copy

from inspect import isclass
from scipy.stats import gamma

from randomizer.data import items, shops, chests
from randomizer.data.items import ItemUnique
from randomizer.data.helpers import ShopQualities, ItemQualities
from . import flags, utils


def get_max_item_quality(world):
    tiers_allowed = 1
    if world.settings.is_flag_value(flags.ShopQuality, ShopQualities.t1):
        tiers_allowed = 4
    elif world.settings.is_flag_value(flags.ShopQuality, ShopQualities.t2):
        tiers_allowed = 3
    elif world.settings.is_flag_value(flags.ShopQuality, ShopQualities.t3):
        tiers_allowed = 2
    return tiers_allowed


def randomize_all(world):

    # Shuffle shop contents and prices.
    free_shops = world.settings.is_flag_value(flags.FreeShops, True)

    if world.settings.is_flag_value(flags.ShuffleShops, True):

        # skip all the shuffling logic if shops are supposed to be empty
        if world.settings.is_flag_value(flags.ShopQuality, ShopQualities.empty):
            for shop in world.shops:
                shop.items = [items.GoodieBag(world)]
        else:
            # collect items that CAN appear in shops
            max_tier = get_max_item_quality(world)

            
            # set disciple and moleville treasure shops
            disciple_shop = [s for s in world.shops if utils.isclass_or_instance(s, shops.DiscipleShop)][0]
            disciple_shop.items = [c.item for c in world.chest_locations if utils.isclass_or_instance(c, chests.FrogCoinShopItem)]
            treasure_shop = [s for s in world.special_shops if utils.isclass_or_instance(s, shops.MolevilleTreasureShop)][0]
            treasure_shop.items = [c.item for c in world.chest_locations if utils.isclass_or_instance(c, chests.TreasureSellerReward)]

            frog_coin_items = copy.copy(disciple_shop.items)

            # warning: unsure if this distinguishes between instances and types
            shops_to_fill = [s for s in world.shops if not utils.isclass_or_instance(s, shops.PartialJuiceBarShop) and not utils.isclass_or_instance(s, shops.DiscipleShop)] + [s for s in world.special_shops if not utils.isclass_or_instance(s, shops.MolevilleTreasureShop)]
            original_item_pool = [item for shop in [s.items for s in shops_to_fill] for item in shop if item not in disciple_shop.items and item not in treasure_shop.items]

            # Guarantee that consumable pool from original game ends up in shops no matter what
            game_should_include = [i for i in original_item_pool if i.consumable and i not in disciple_shop.items and i not in treasure_shop.items and not (i.special_equip and world.settings.is_flag_value(flags.RestrictSpecialEquips, True))]
            # All other eligible items may or may not appear in shops
            game_should_optionally_include = [i for i in world.items if i not in disciple_shop.items and i not in treasure_shop.items and i not in game_should_include and not i.is_key and not i.unique == ItemUnique.Always and not (i.unique == ItemUnique.BalancedOnly and world.settings.is_flag_value(flags.ItemQuality, ItemQualities.original)) and not (i.special_equip and world.settings.is_flag_value(flags.RestrictSpecialEquips, True))]


            # filter by max quality
            original_item_pool = [i for i in original_item_pool if i.tier >= max_tier and not (i.special_equip and world.settings.is_flag_value(flags.RestrictSpecialEquips, True))]
            game_should_include = [i for i in game_should_include if i.tier >= max_tier]
            game_should_optionally_include = [i for i in game_should_optionally_include if i.tier >= max_tier]


            # Establish an array for each shop's items
            for shop in shops_to_fill:
                shop.items = []

            if world.settings.is_flag_value(flags.ShopQuality, ShopQualities.original):
                item_pool = original_item_pool
            else:
                item_pool = game_should_include

            initial_item_pool = copy.copy(item_pool)

            #print(item_pool)

            # place pick me ups in one open permanent shop first
            # NO protection from frog coin emporium
            pmu_instance = [i for i in item_pool if utils.isclass_or_instance(i, items.PickMeUp)]
            if (pmu_instance):
                random.choice([a for a in shops_to_fill if a.access == 1 and not utils.isclass_or_instance(a, shops.NPCShop) and not utils.isclass_or_instance(a, shops.SeasideYaridShop)]).items.append(items.PickMeUp(world))
                item_pool.remove(pmu_instance[0])

            item_ids_that_cannot_be_in_a_frog_coin_shop = []

            # place the rest of the necessary items
            for item in item_pool:
                if item in frog_coin_items:
                    continue
                random.shuffle(shops_to_fill)
                eligible_shops = [s for s in shops_to_fill if s.is_item_allowed(item) and not (s.retain_size and len(s.items) >= s.forced_size) and len(s.items) < 14 and item not in (s.items) and not (item.index in item_ids_that_cannot_be_in_a_frog_coin_shop and s.frog_coin_shop)]
                if world.settings.is_flag_enabled(flags.BiasShopShuffle):
                    access_1_shops = [s for s in eligible_shops if s.access == 1]
                    access_2_shops = [s for s in eligible_shops if s.access == 2]
                    shop_choice = random.randint(1, 10)
                    if item.tier == 1 or item.tier == 2:
                        if shop_choice <= 9:
                            shop_pool = access_2_shops
                        if shop_choice > 9 or len(shop_pool) == 0:
                            shop_pool = access_1_shops
                    else:
                        if shop_choice <= 9:
                            shop_pool = access_1_shops
                        if shop_choice > 9 or len(shop_pool) == 0:
                            shop_pool = access_2_shops
                else:
                    shop_pool = eligible_shops
                if len(shop_pool) == 0:
                    # skip the item if no eligible shops
                    pass
                else:
                    shop_pool[0].items.append(item)
                if shop_pool[0].frog_coin_shop:
                    frog_coin_items.append(item)
                else: # items in regular coin shops cannot go in frog coin shops
                    item_ids_that_cannot_be_in_a_frog_coin_shop.append(item.index)

            # fill empty space with extra items
            for shop in shops_to_fill:
                if shop.retain_size:
                    remaining_space = shop.forced_size - len(shop.items)
                else:
                    remaining_space = 14 - len(shop.items)
                if remaining_space == 0:
                    continue
                if utils.isclass_or_instance(shop, shops.ToadShop) and len([i for i in shop.items if utils.isclass_or_instance(i, items.PickMeUp)]) == 0:
                    shop.items.append(items.PickMeUp(world))
                    remaining_space -= 1
                if world.settings.is_flag_enabled(flags.BiasShopShuffle):
                    good_optional = [i for i in game_should_optionally_include if shop.is_item_allowed(i) and i not in shop.items and (i.tier == 3 or i.tier == 4) and i not in frog_coin_items]
                    good_required = [i for i in game_should_include if shop.is_item_allowed(i) and i not in shop.items and (i.tier == 3 or i.tier == 4) and i not in frog_coin_items]
                    bad_optional = [i for i in game_should_optionally_include if shop.is_item_allowed(i) and i not in shop.items and (i.tier == 1 or i.tier == 2) and i not in frog_coin_items]
                    bad_required = [i for i in game_should_include if shop.is_item_allowed(i) and i not in shop.items and (i.tier == 1 or i.tier == 2) and i not in frog_coin_items]

                    shop_choice = random.randint(1, 5)
                    if (shop_choice <= 4 and shop.access == 2) or (shop_choice > 4 and shop.access == 1):
                        extra_item_pool = copy.copy(good_optional)
                        if len(extra_item_pool) == 0:
                            extra_item_pool = copy.copy(good_required)
                        if len(extra_item_pool) == 0:
                            extra_item_pool = copy.copy(bad_optional)
                        if len(extra_item_pool) == 0:
                            extra_item_pool = copy.copy(bad_required)
                    else:
                        extra_item_pool = copy.copy(bad_optional)
                        if len(extra_item_pool) == 0:
                            extra_item_pool = copy.copy(bad_required)
                        if len(extra_item_pool) == 0:
                            extra_item_pool = copy.copy(good_optional)
                        if len(extra_item_pool) == 0:
                            extra_item_pool = copy.copy(good_required)
                else:
                    extra_item_pool = [i for i in initial_item_pool if shop.is_item_allowed(i) and i not in shop.items and i not in frog_coin_items]
                extra_item_pool = list(set(extra_item_pool))
                if shop.retain_size:
                    sample = remaining_space
                    if len(extra_item_pool) < sample:
                        extra_item_pool = list(set([i for i in initial_item_pool + extra_item_pool if shop.is_item_allowed(i) and i not in shop.items and i not in frog_coin_items]))
                else:
                    if world.settings.is_flag_value(flags.ShopQuality, ShopQualities.original):
                        sample = 2
                    else:
                        sample = 4
                    sample = gamma.rvs(sample, size=1)[0] // 1
                    sample = min(sample, remaining_space)
                    sample = min(sample, len(extra_item_pool))
                    sample = max(0, sample)
                items_to_add = random.sample(extra_item_pool, int(round(sample)))
                shop.items.extend(items_to_add)
                if shop.frog_coin_shop:
                    frog_coin_items.extend(items_to_add)
                # juice bar needs at least 4 items
                if utils.isclass_or_instance(shop, shops.JuiceBarFull) and len(shop.items) < 4:
                    items_to_add = random.sample(extra_item_pool, 4-len(shop.items))
                    shop.items.extend(items_to_add)
                shop.items.sort(key=lambda x: x.rank_value)


            # fill partial juice bars
            shop = [s for s in shops_to_fill if utils.isclass_or_instance(s, shops.JuiceBarFull)][0]
            juice_bar_possible_lengths = list(range(1, len(shop.items)))
            juice_bar_lengths = random.sample(juice_bar_possible_lengths, 3)
            juice_bar_lengths.sort()
            juice_bar1 = [s for s in world.shops if utils.isclass_or_instance(s, shops.JuiceBarPartial1)][0]
            juice_bar2 = [s for s in world.shops if utils.isclass_or_instance(s, shops.JuiceBarPartial2)][0]
            juice_bar3 = [s for s in world.shops if utils.isclass_or_instance(s, shops.JuiceBarPartial3)][0]
            juice_bar1.items = copy.copy(shop.items)
            juice_bar1.items = juice_bar1.items[:juice_bar_lengths[0]]
            juice_bar2.items = copy.copy(shop.items)
            juice_bar2.items = juice_bar2.items[:juice_bar_lengths[1]]
            juice_bar3.items = copy.copy(shop.items)
            juice_bar3.items = juice_bar3.items[:juice_bar_lengths[2]]

            

            # ******************************* Phase 3: Repricing

            # Calculate list position (used as a factor in pricing)
            ranks = [item for item in world.items if item.is_equipment]
            ranks.sort(key=lambda x: x.rank_value, reverse=True)
            ranks_reverse = sorted(ranks, key=lambda x: x.rank_value)

            # set frog coin items
            for item in world.items:
                item.frog_coin_item = False

            for item in frog_coin_items:
                item.frog_coin_item = True

            # right... these are not the same instances as the frog coin items. what to do?
            # every item in chest i think needs to be established at World level...
            for item in world.items:
                if not item.is_key:
                    if item.is_equipment:
                        if item.frog_coin_item:
                            item.price = min(item.max_price, max(math.ceil(item.rank_value / 5), 1))
                        else:
                            price = math.ceil(item.rank_value *
                                                (2 + (item.rank_order_reverse / len(ranks_reverse))))
                            price = min(item.max_price, max(2, price))
                            item.price = price
                    else:
                        if item.frog_coin_item:
                            item.price = min(item.max_price, max(math.ceil(item.price / 25), 1))
                        else:
                            item.price = min(item.max_price, max(2, item.price))

            # Sort the list of items by the ordering rank for display, and assign to the shop.
            # DON'T sort moleville treasure shop, that would be extremely bad since those items were placed according to progression logic
            for shop in [i for i in world.shops + world.special_shops if not utils.isclass_or_instance(i, shops.MolevilleTreasureShop)]:
                shop.items = sorted(shop.items, key=lambda i: i.order)

    # Check for free shops, and make sure item prices don't go above 9999 or below 1 as a general rule.
    for shop in world.shops:
        for item in shop.items:
            item.price = max(1, min(item.max_price, item.price))
            if free_shops:
                item.price = 1