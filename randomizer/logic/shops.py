# Item/shop randomization logic

import random
import math

from inspect import isclass
from scipy.stats import gamma

from randomizer.data import items, shops, chests
from randomizer.data.items import ItemUnique
from . import flags, utils
from randomizer.logic.flags import ShopQualities, ItemQualities


def get_max_item_quality(world):
    tiers_allowed = 4
    if world.settings.is_flag_value(flags.ShopQuality, ShopQualities.Tier1):
        tiers_allowed = 1
    elif world.settings.is_flag_value(flags.ShopQuality, ShopQualities.Tier2):
        tiers_allowed = 2
    elif world.settings.is_flag_value(flags.ShopQuality, ShopQualities.Tier3):
        tiers_allowed = 3
    return tiers_allowed


def randomize_all(world):

    # Shuffle shop contents and prices.
    free_shops = world.settings.is_flag_value(flags.FreeShops, True)

    if world.settings.is_flag_value(flags.ShuffleShops, True):

        # skip all the shuffling logic if shops are supposed to be empty
        if world.settings.is_flag_valued(flags.ShopQuality, ShopQualities.Empty):
            for shop in world.shops:
                shop.items = [world.get_item_instance(items.GoodieBag)]
        else:
            # collect items that CAN appear in shops
            max_tier = get_max_item_quality(world)
            shops_to_fill = [s for s in world.shops if not utils.isclass_or_instance(s, shops.PartialJuiceBarShop) and not utils.isclass_or_instance(s, shops.DiscipleShop)] + [s for s in world.special_shops if not utils.isclass_or_instance(s, shops.MolevilleTreasureShop)]
            original_item_pool = [item for shop in [s.items for s in shops_to_fill] for item in shop]

            # Guarantee that consumable pool from original game ends up in shops no matter what
            game_should_include = [i for i in original_item_pool if i.consumable and not i.reusable]
            # All other eligible items may or may not appear in shops
            game_should_optionally_include = [i for i in world.items if i not in game_should_include and not i.is_key and not i.unique == ItemUnique.Always and not (i.unique == ItemUnique.BalancedOnly and world.settings.is_flag_value(flags.ItemQuality, ItemQualities.Original)) and not (i.special_equip and world.settings.is_flag_value(flags.RestrictSpecialEquips, True))]

            # set disciple and moleville treasure shops
            disciple_shop = [s for s in world.shops if utils.isclass_or_instance(s, shops.DiscipleShop)][0]
            disciple_shop.items = [c.item for c in world.chest_locations if utils.isclass_or_instance(c, chests.FrogCoinShopItem)]
            treasure_shop = [s for s in world.special_shops if utils.isclass_or_instance(s, shops.MolevilleTreasureShop)][0]
            treasure_shop.items = [c.item for c in world.chest_locations if utils.isclass_or_instance(c, chests.TreasureSellerReward)]

            # remove their items from the shop pool
            original_item_pool = [i for i in original_item_pool if i not in disciple_shop.items and i not in treasure_shop.items]
            game_should_include = [i for i in game_should_include if i not in disciple_shop.items and i not in treasure_shop.items]
            game_should_optionally_include = [i for i in game_should_optionally_include if i not in disciple_shop.items and i not in treasure_shop.items]

            # filter by max quality
            original_item_pool = [i for i in original_item_pool if i.tier <= max_tier]
            game_should_include = [i for i in game_should_include if i.tier <= max_tier]
            game_should_optionally_include = [i for i in game_should_optionally_include if i.tier <= max_tier]


            # Establish an array for each shop's items
            for shop in shops_to_fill:
                shops_to_fill.items = []

            if world.settings.is_flag_valued(flags.ShopQuality, ShopQualities.Original):
                item_pool = original_item_pool
            else:
                item_pool = game_should_include

            # place pick me ups in one open permanent normal shop first
            random.choice([a for a in shops_to_fill if a.access == 1 and not utils.isclass_or_instance(a, shops.NPCShop) and not utils.isclass_or_instance(a, shops.SeasideYaridShop) and not a.frog_coin_shop]).items.append(items.PickMeUp)
            for i, o in enumerate(item_pool):
                if utils.isclass_or_instance(o, items.PickMeUp):
                    del item_pool[i]
                    break

            frog_coin_items = disciple_shop.items.copy()

            # place the rest of the necessary items
            for item in item_pool:
                if item in frog_coin_items:
                    continue
                random.shuffle(shops_to_fill)
                eligible_shops = [s for s in shops_to_fill if s.is_item_allowed(item) and not (s.retain_size and len(s.items) >= s.forced_size) and len(s.items) < 14 and item not in (s.items)]
                if world.settings.is_flag_valued(flags.ShopQuality, ShopQualities.Original):
                    shop_pool = eligible_shops
                else:
                    access_1_shops = [s for s in eligible_shops if s.access == 1]
                    access_2_shops = [s for s in eligible_shops if s.access == 2]
                    shop_choice = random.randint(1, 5)
                    if item.tier == 1 or item.tier == 2:
                        if shop_choice <= 4 or len(access_2_shops) == 0:
                            shop_pool = access_1_shops
                        else:
                            shop_pool = access_2_shops
                    elif item.tier == 3 or item.tier == 4:
                        if shop_choice <= 4 or len(access_1_shops) == 0:
                            shop_pool = access_2_shops
                        else:
                            shop_pool = access_1_shops
                    else:
                        raise Exception("what item is this? %r" % item)
                if len(shop_pool) == 0:
                    # skip the item if no eligible shops
                    pass
                else:
                    shop_pool[0].items.append(item)
                if shop_pool[0].frog_coin_shop:
                    frog_coin_items.append(item)

            # fill empty space with extra items
            for shop in shops_to_fill:
                if shop.retain_size:
                    remaining_space = shop.forced_size - len(shop.items)
                else:
                    remaining_space = 14 - len(shop.items)
                if remaining_space == 0:
                    continue
                if world.settings.is_flag_valued(flags.ShopQuality, ShopQualities.Original):
                    item_pool = [i for i in original_item_pool if shop.is_item_allowed(i) and i not in shop.items and i not in frog_coin_items]
                else:
                    good_optional = [i for i in game_should_optionally_include if shop.is_item_allowed(i) and i not in shop.items and (i.tier == 3 or i.tier == 4) and i not in frog_coin_items]
                    good_required = [i for i in game_should_include if shop.is_item_allowed(i) and i not in shop.items and (i.tier == 3 or i.tier == 4) and i not in frog_coin_items]
                    bad_optional = [i for i in game_should_optionally_include if shop.is_item_allowed(i) and i not in shop.items and (i.tier == 1 or i.tier == 2) and i not in frog_coin_items]
                    bad_required = [i for i in game_should_include if shop.is_item_allowed(i) and i not in shop.items and (i.tier == 1 or i.tier == 2) and i not in frog_coin_items]

                    shop_choice = random.randint(1, 5)
                    if shop_choice <= 4:
                        if (shop_choice <= 4 and shop.access == 2) or (shop_choice > 4 and shop.access == 1):
                            item_pool = good_optional
                            if len(item_pool) == 0:
                                item_pool = good_required
                            if len(item_pool) == 0:
                                item_pool = bad_optional
                            if len(item_pool) == 0:
                                item_pool = bad_required
                        else:
                            item_pool = bad_optional
                            if len(item_pool) == 0:
                                item_pool = bad_required
                            if len(item_pool) == 0:
                                item_pool = good_optional
                            if len(item_pool) == 0:
                                item_pool = good_required
                item_pool = list(set([item_pool]))
                if shop.retain_size:
                    sample = remaining_space
                else:
                    if world.settings.is_flag_valued(flags.ShopQuality, ShopQualities.Original):
                        sample = 2
                    else:
                        sample = 4
                    sample = gamma.rvs(sample, size=1)[0] // 1
                    sample = min(sample, remaining_space)
                    sample = min(sample, len(item_pool))
                items_to_add = random.sample(item_pool, sample)
                shop.items.extend(items_to_add)
                if shop.frog_coin_shop:
                    frog_coin_items.extend(items_to_add)
                # juice bar needs at least 4 items
                if utils.isclass_or_instance(shop, shops.JuiceBarFull) and len(shop.items) < 4:
                    items_to_add = random.sample(item_pool, 4-len(shop.items))
                    shop.items.extend(items_to_add)
                shop.items.sort(key=lambda x: x.rank_value)


            # fill partial juice bars
            shop = [s for s in shops_to_fill if utils.isclass_or_instance(s, shops.JuiceBarFull)]
            juice_bar_possible_lengths = list(range(1, len(shop.items)))
            juice_bar_lengths = random.sample(juice_bar_possible_lengths, 3).sort()
            juice_bar1 = [s for s in shops_to_fill if utils.isclass_or_instance(s, shops.JuiceBarPartial1)][0]
            juice_bar2 = [s for s in shops_to_fill if utils.isclass_or_instance(s, shops.JuiceBarPartial2)][0]
            juice_bar3 = [s for s in shops_to_fill if utils.isclass_or_instance(s, shops.JuiceBarPartial3)][0]
            juice_bar1.items = shop.items.copy()[:juice_bar_lengths[0]]
            juice_bar2.items = shop.items.copy()[:juice_bar_lengths[1]]
            juice_bar3.items = shop.items.copy()[:juice_bar_lengths[2]]

            

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
            for shop in world.shops:
                shop.items = sorted(shop.items, key=lambda i: i.order)

    # Check for free shops, and make sure item prices don't go above 9999 or below 1 as a general rule.
    for shop in world.shops:
        for item in shop.items:
            item.price = max(1, min(item.max_price, item.price))
            if free_shops:
                item.price = 1