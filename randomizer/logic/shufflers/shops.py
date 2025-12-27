"""Shop shuffling logic."""
from __future__ import annotations
import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...types.gameworld import GameWorld
    from smrpgpatchbuilder.datatypes.items.classes import BaseItem


def shuffle_shops(world: GameWorld) -> None:
    """Shuffle the contents of all shops based on settings."""
    from smrpgpatchbuilder.datatypes.items.classes import Weapon, Armor, Accessory
    from ...data.items.items import GoodieBagItem, PickMeUpItem
    from ...types.flags import (
        ShopQuality,
        ShopQualities,
        BiasShopShuffle,
        NoPickMeUps,
        FreeShops,
        SeaGate,
        SeaGating,
        MonstroTownGate,
        MonstroTownGating,
        BarrelVolcanoGate,
        BarrelVolcanoGating,
        NimbusGate,
        NimbusGating,
        BowsersKeepGate,
        BowsersKeepGating,
    )
    from ...data.shops.shops import (
        SH03_FROG_DISCIPLE,
        SH06_FROG_COIN_EMPORIUM,
        SH07_SEA_AND_SHIP_SHAMAN,
        SH08_SEASIDE_TOWN_MINION,
        SH09_JUICE_BAR_BASE,
        SH10_JUICE_BAR_ALTO,
        SH11_JUICE_BAR_TENOR,
        SH12_JUICE_BAR_SOPRANO,
        SH13_SEASIDE_WEAPON,
        SH14_SEASIDE_ARMOR,
        SH15_SEASIDE_ACCESSORY,
        SH16_SEASIDE_HEALTH_FOOD,
        SH17_MONSTRO,
        SH18_VOLCANO_ITEM,
        SH19_VOLCANO_ARMOR,
        SH20_GOOMBETTE,
        SH21_NIMBUS_LAND,
        SH22_KEEP_1,
        SH23_KEEP_2,
        SH24_FACTORY_TOAD,
    )
    from ...progression.prizelocations import (
        FrogDiscipleLocation1,
        FrogDiscipleLocation2,
        FrogDiscipleLocation3,
        FrogDiscipleLocation4,
        FrogDiscipleLocation5,
    )

    quality = world.settings.get_flag(ShopQuality).selected
    bias_enabled = world.settings.isflag_enabled(BiasShopShuffle)
    no_pickmeups = world.settings.isflag_enabled(NoPickMeUps)
    free_shops = world.settings.isflag_enabled(FreeShops)

    # Define shop indices for special handling
    FROG_DISCIPLE_SHOP = SH03_FROG_DISCIPLE
    FROG_COIN_EMPORIUM = SH06_FROG_COIN_EMPORIUM
    JUICE_BAR_BASE = SH09_JUICE_BAR_BASE
    JUICE_BAR_ALTO = SH10_JUICE_BAR_ALTO
    JUICE_BAR_TENOR = SH11_JUICE_BAR_TENOR
    JUICE_BAR_SOPRANO = SH12_JUICE_BAR_SOPRANO

    # Get the items from Frog Disciple prize locations (already shuffled)
    frog_disciple_items: list[type[BaseItem] | None] = []
    frog_disciple_locations = [
        FrogDiscipleLocation1,
        FrogDiscipleLocation2,
        FrogDiscipleLocation3,
        FrogDiscipleLocation4,
        FrogDiscipleLocation5,
    ]
    for loc_type in frog_disciple_locations:
        loc = world.locations.get(loc_type)
        if loc and loc.prize:
            # Get the item type from the prize
            from ...types.prize import ItemPrize

            if isinstance(loc.prize, ItemPrize):
                prize_item = loc.prize.item
                if prize_item:
                    frog_disciple_items.append(prize_item)

    # Set Frog Disciple shop contents (don't shuffle into it)
    world.shops.shops[FROG_DISCIPLE_SHOP].set_items(frog_disciple_items)

    # Define should_get_better_items shops
    should_get_better_items = [
        SH06_FROG_COIN_EMPORIUM,
        SH08_SEASIDE_TOWN_MINION,
        SH11_JUICE_BAR_TENOR,
        SH12_JUICE_BAR_SOPRANO,
        SH13_SEASIDE_WEAPON,
        SH14_SEASIDE_ARMOR,
        SH15_SEASIDE_ACCESSORY,
        SH16_SEASIDE_HEALTH_FOOD,
        SH23_KEEP_2,
        SH24_FACTORY_TOAD,
    ]
    if not world.settings.is_flag_value(SeaGate, SeaGating.OPEN):
        should_get_better_items.append(SH07_SEA_AND_SHIP_SHAMAN)
    if not world.settings.is_flag_value(MonstroTownGate, MonstroTownGating.OPEN):
        should_get_better_items.extend([SH17_MONSTRO, SH20_GOOMBETTE])
    if not world.settings.is_flag_value(BarrelVolcanoGate, BarrelVolcanoGating.OPEN):
        should_get_better_items.extend([SH18_VOLCANO_ITEM, SH19_VOLCANO_ARMOR])
    if world.settings.is_flag_value(NimbusGate, NimbusGating.MEGASMILAX):
        should_get_better_items.append(SH21_NIMBUS_LAND)
    if not world.settings.is_flag_value(BowsersKeepGate, BowsersKeepGating.OPEN):
        should_get_better_items.extend([SH22_KEEP_1])

    # Use class-level item impact categories (built by build_item_impact_categories)
    low_impact_items = world.low_impact_items
    high_impact_items = world.high_impact_items
    highest_impact_items = world.highest_impact_items
    low_impact_equip = world.low_impact_equip
    high_impact_equip = world.high_impact_equip
    highest_impact_equip = world.highest_impact_equip

    # Get original shop item types for each shop (for type restrictions)
    original_shop_data: dict[int, dict] = {}
    for shop in world.shops.shops:
        if shop is None:
            continue
        orig_items = [i for i in shop.items if i is not None]
        original_shop_data[shop.index] = {
            "has_weapon": any(issubclass(i, Weapon) for i in orig_items),
            "has_armor": any(issubclass(i, Armor) for i in orig_items),
            "has_accessory": any(issubclass(i, Accessory) for i in orig_items),
            "has_consumable": any(
                not issubclass(i, (Weapon, Armor, Accessory)) for i in orig_items
            ),
            "original_items": orig_items,
            "original_count": len(orig_items),
        }

    # Handle EMPTY mode: only GoodieBag in every shop
    if quality == ShopQualities.EMPTY:
        for shop in world.shops.shops:
            if shop is None:
                continue
            shop.set_items([GoodieBagItem])
        return

    # Build item pools based on quality setting
    def get_item_pool(
        quality: ShopQualities, is_equipment: bool = False
    ) -> tuple[list, list, list]:
        """Returns (low, high, highest) pools based on quality."""
        if is_equipment:
            if quality == ShopQualities.ORIGINAL:
                # Only equipment that was originally in shops
                orig_equip_in_shops: set = set()
                for shop in world.shops.shops:
                    if shop is None or shop.index == FROG_DISCIPLE_SHOP:
                        continue
                    for item in shop.items:
                        if item and issubclass(item, (Weapon, Armor, Accessory)):
                            orig_equip_in_shops.add(item)
                return (
                    [e for e in low_impact_equip if e in orig_equip_in_shops],
                    [e for e in high_impact_equip if e in orig_equip_in_shops],
                    [e for e in highest_impact_equip if e in orig_equip_in_shops],
                )
            elif quality == ShopQualities.MOSTLY_RANDOM:
                return (low_impact_equip, high_impact_equip, [])
            else:  # COMPLETELY_RANDOM
                return (low_impact_equip, high_impact_equip, highest_impact_equip)
        else:
            if quality == ShopQualities.ORIGINAL:
                # Only consumables that were originally in shops
                orig_in_shops: set = set()
                for shop in world.shops.shops:
                    if shop is None or shop.index == FROG_DISCIPLE_SHOP:
                        continue
                    for item in shop.items:
                        if item and not issubclass(
                            item, (Weapon, Armor, Accessory)
                        ):
                            orig_in_shops.add(item)
                return (
                    [i for i in low_impact_items if i in orig_in_shops],
                    [i for i in high_impact_items if i in orig_in_shops],
                    [i for i in highest_impact_items if i in orig_in_shops],
                )
            elif quality == ShopQualities.MOSTLY_RANDOM:
                return (low_impact_items, high_impact_items, [])
            else:  # COMPLETELY_RANDOM
                return (low_impact_items, high_impact_items, highest_impact_items)

    low_consumables, high_consumables, highest_consumables = get_item_pool(
        quality, is_equipment=False
    )
    low_equip, high_equip, highest_equip = get_item_pool(quality, is_equipment=True)

    # Remove Pick Me Ups if setting enabled
    if no_pickmeups:
        low_consumables = [i for i in low_consumables if i != PickMeUpItem]
        high_consumables = [i for i in high_consumables if i != PickMeUpItem]
        highest_consumables = [i for i in highest_consumables if i != PickMeUpItem]

    # Track items placed in Frog Coin Emporium (cannot appear elsewhere)
    frog_emporium_items: set = set()
    # Track items placed in Frog Disciple (can only also appear in Frog Coin Emporium)
    frog_disciple_set = set(frog_disciple_items)

    def can_place_item(
        item_type: type[BaseItem] | None, shop_idx: int, current_items: list
    ) -> bool:
        """Check if an item can be placed in a shop."""
        if item_type is None:
            return False
        # No duplicates in same shop
        if item_type in current_items:
            return False
        # Items in Frog Coin Emporium can't appear elsewhere
        if item_type in frog_emporium_items and shop_idx != FROG_COIN_EMPORIUM:
            return False
        # Items in Frog Disciple can only also appear in Frog Coin Emporium
        if item_type in frog_disciple_set and shop_idx not in [
            FROG_DISCIPLE_SHOP,
            FROG_COIN_EMPORIUM,
        ]:
            return False
        # Check type restrictions
        shop_data = original_shop_data.get(shop_idx, {})
        if issubclass(item_type, Weapon) and not shop_data.get("has_weapon", False):
            return False
        if issubclass(item_type, Armor) and not shop_data.get("has_armor", False):
            return False
        if issubclass(item_type, Accessory) and not shop_data.get(
            "has_accessory", False
        ):
            return False
        if not issubclass(
            item_type, (Weapon, Armor, Accessory)
        ) and not shop_data.get("has_consumable", False):
            return False
        return True

    def select_item(
        shop_idx: int, current_items: list, prefer_high: bool = False
    ) -> type[BaseItem] | None:
        """Select an item for a shop based on bias and availability."""
        is_better_shop = shop_idx in should_get_better_items

        # Build weighted pool
        candidates = []
        weights = []

        # Combine consumables and equipment pools
        all_low = low_consumables + low_equip
        all_high = high_consumables + high_equip
        all_highest = highest_consumables + highest_equip

        if bias_enabled:
            if is_better_shop:
                # Better shops: favor high/highest impact
                for item in all_highest:
                    if can_place_item(item, shop_idx, current_items):
                        candidates.append(item)
                        weights.append(5)
                for item in all_high:
                    if can_place_item(item, shop_idx, current_items):
                        candidates.append(item)
                        weights.append(3)
                for item in all_low:
                    if can_place_item(item, shop_idx, current_items):
                        candidates.append(item)
                        weights.append(1)
            else:
                # Other shops: favor low impact
                for item in all_low:
                    if can_place_item(item, shop_idx, current_items):
                        candidates.append(item)
                        weights.append(5)
                for item in all_high:
                    if can_place_item(item, shop_idx, current_items):
                        candidates.append(item)
                        weights.append(1)
                # Significantly less likely for highest
                for item in all_highest:
                    if can_place_item(item, shop_idx, current_items):
                        candidates.append(item)
                        weights.append(0.2)
        else:
            # No bias: equal weights
            for item in all_low + all_high + all_highest:
                if can_place_item(item, shop_idx, current_items):
                    candidates.append(item)
                    weights.append(1)

        if not candidates:
            return None

        return random.choices(candidates, weights=weights, k=1)[0]

    # Process each shop (except Frog Disciple which is already set)
    shops_to_process = [
        s
        for s in world.shops.shops
        if s is not None and s.index != FROG_DISCIPLE_SHOP
    ]

    # Process Frog Coin Emporium first (its items are exclusive)
    frog_emporium_shop = world.shops.shops[FROG_COIN_EMPORIUM]
    if frog_emporium_shop:
        shop_data = original_shop_data.get(FROG_COIN_EMPORIUM, {})
        target_count = min(15, max(1, shop_data.get("original_count", 5)))
        emporium_new_items: list[type[BaseItem] | None] = []

        for _ in range(target_count):
            item = select_item(
                FROG_COIN_EMPORIUM, emporium_new_items, prefer_high=True
            )
            if item:
                emporium_new_items.append(item)
                frog_emporium_items.add(item)

        frog_emporium_shop.set_items(emporium_new_items)

    # Handle Juice Bar hierarchy (BASE < ALTO < TENOR < SOPRANO)
    juice_bars = [
        JUICE_BAR_BASE,
        JUICE_BAR_ALTO,
        JUICE_BAR_TENOR,
        JUICE_BAR_SOPRANO,
    ]
    juice_bar_items: dict[int, list[type[BaseItem] | None]] = {}

    for i, bar_idx in enumerate(juice_bars):
        shop = world.shops.shops[bar_idx]
        if shop is None:
            continue

        shop_data = original_shop_data.get(bar_idx, {})

        if i == 0:
            # BASE: start fresh
            target_count = max(1, shop_data.get("original_count", 1))
            bar_new_items: list[type[BaseItem] | None] = []
            for _ in range(target_count):
                item = select_item(bar_idx, bar_new_items)
                if item:
                    bar_new_items.append(item)
            juice_bar_items[bar_idx] = bar_new_items
        else:
            # Must be superset of previous (but not same)
            prev_items = list(juice_bar_items.get(juice_bars[i - 1], []))
            bar_new_items = list(prev_items)  # Start with previous items
            # Add at least one more item
            added = 0
            attempts = 0
            while added < 1 and attempts < 50:
                item = select_item(bar_idx, bar_new_items)
                if item and item not in bar_new_items:
                    bar_new_items.append(item)
                    added += 1
                attempts += 1
            # Try to add more up to original count or 15
            target_extra = min(
                15 - len(bar_new_items),
                shop_data.get("original_count", len(bar_new_items))
                - len(prev_items),
            )
            for _ in range(max(0, target_extra - 1)):
                item = select_item(bar_idx, bar_new_items)
                if item and item not in bar_new_items:
                    bar_new_items.append(item)
            juice_bar_items[bar_idx] = bar_new_items

        shop.set_items(juice_bar_items[bar_idx])

    # Process remaining shops
    processed = {FROG_DISCIPLE_SHOP, FROG_COIN_EMPORIUM} | set(juice_bars)
    for shop in shops_to_process:
        if shop.index in processed:
            continue

        shop_data = original_shop_data.get(shop.index, {})
        target_count = min(15, max(1, shop_data.get("original_count", 5)))
        shop_new_items: list[type[BaseItem] | None] = []

        for _ in range(target_count):
            item = select_item(shop.index, shop_new_items)
            if item:
                shop_new_items.append(item)

        if shop_new_items:
            shop.set_items(shop_new_items)
        elif quality == ShopQualities.ORIGINAL:
            # If no items could be placed in ORIGINAL mode, discard
            shop.set_items([])

    # Guarantee Pick Me Ups appear in at least one shop if not disabled
    if not no_pickmeups:
        # Check if any shop contains Pick Me Up
        has_pickmeup = False
        for shop in world.shops.shops:
            if shop is not None and PickMeUpItem in (shop.items or []):
                has_pickmeup = True
                break

        if not has_pickmeup:
            # Find shops that can have consumables and have room
            eligible_shops = []
            for shop in world.shops.shops:
                if shop is None or shop.index == FROG_DISCIPLE_SHOP:
                    continue
                shop_data = original_shop_data.get(shop.index, {})
                if shop_data.get("has_consumable", False):
                    current_items = shop.items or []
                    if (
                        len(current_items) < 15
                        and PickMeUpItem not in current_items
                    ):
                        eligible_shops.append(shop)

            if eligible_shops:
                target_shop = random.choice(eligible_shops)
                current_items: list[type[BaseItem] | None] = list(
                    target_shop.items or []
                )
                current_items.append(PickMeUpItem)
                target_shop.set_items(current_items)

    # Apply FreeShops: set all non-zero prices to 1
    if free_shops:
        for item in world.items.items:
            if item.price > 0:
                item.set_price(1)

    # Apply Frog Coin Emporium price reduction (divide by 5)
    for item_type in frog_emporium_items:
        item = world.items.get_by_type(item_type)
        if item and item.price > 0:
            item.set_price(max(1, item.price // 5))
