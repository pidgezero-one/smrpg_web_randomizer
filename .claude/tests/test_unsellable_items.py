"""Tests for the no_sell bit, the ProtectSpecialItems flag, and the
unsellable_items ASM patch."""

import itertools

NO_SELL_BIT = 0x40
ITEMS_BASE = 0x3A014D


def _byte0(item) -> int:
    return item.render()[ITEMS_BASE + item.item_id * 18][0]


class _FakeWorld:
    """Minimal stand-in for GameWorld: apply_item_protection only touches
    ``settings`` and ``get_item``."""

    def __init__(self, settings) -> None:
        from copy import deepcopy
        from randomizer.data.items.items import ITEMS

        self.settings = settings
        self.items = deepcopy(ITEMS)

    def get_item(self, item_class: type):
        found = next((i for i in self.items.items if isinstance(i, item_class)), None)
        assert found is not None, f"{item_class} not in ItemCollection"
        return found


def _protect(*options):
    from randomizer.types.settings import Settings
    from randomizer.types.flags import ProtectSpecialItems
    from randomizer.logic.pre_shuffle.item_protection import apply_item_protection

    settings = Settings()
    flag = settings.get_flag(ProtectSpecialItems)
    for option in options:
        flag.enable(option)
    world = _FakeWorld(settings)
    apply_item_protection(world)
    return world


def test_no_sell_lives_in_the_randomizer_item_layer_not_patchbuilder():
    # no_sell is a randomizer feature, not a game feature. smrpgpatchbuilder must
    # stay unaware of it so this ships without a wheel release.
    import smrpgpatchbuilder.datatypes.items.classes as pb
    from randomizer.types.item import RegularItem

    assert "no_sell" not in vars(pb.Item), "no_sell leaked into smrpgpatchbuilder"

    class _Probe(RegularItem):
        _item_id = 148
        _price = 100
        _no_sell = True

    assert _Probe().no_sell is True
    assert _byte0(_Probe()) & NO_SELL_BIT


def test_no_sell_on_a_price_zero_item_fails_loudly():
    # ItemBase.render() early-returns before the stat block when price == 0, so
    # the bit would silently never land. Raise rather than protect nothing.
    import pytest
    from randomizer.types.item import RegularItem

    class _Probe(RegularItem):
        _item_id = 124  # Temple Key's slot
        _price = 0
        _no_sell = True

    with pytest.raises(ValueError, match="nonzero price"):
        _Probe().render()


def test_debug_candy_is_always_protected_without_any_flag():
    from randomizer.data.items.items import DebugCandyItem

    assert _byte0(DebugCandyItem()) & NO_SELL_BIT


def test_nothing_else_is_protected_by_default():
    from randomizer.data.items.items import (
        LuckyJewelItem, SeeYaItem, EarlierTimesItem, GoodieBagItem,
        MysteryEggItem, LambsLureItem, SheepAttackItem, StarEggItem,
    )

    world = _protect()  # no options enabled
    for cls in (LuckyJewelItem, SeeYaItem, EarlierTimesItem, GoodieBagItem,
                MysteryEggItem, LambsLureItem, SheepAttackItem, StarEggItem):
        assert not _byte0(world.get_item(cls)) & NO_SELL_BIT, cls.__name__


def test_selecting_an_option_protects_exactly_its_items():
    from randomizer.types.flags import ProtectedItemEnum
    from randomizer.data.items.items import LuckyJewelItem, SeeYaItem

    world = _protect(ProtectedItemEnum.LUCKY_JEWEL)
    assert _byte0(world.get_item(LuckyJewelItem)) & NO_SELL_BIT
    assert not _byte0(world.get_item(SeeYaItem)) & NO_SELL_BIT


def test_progressive_eggs_option_covers_all_three_eggs():
    from randomizer.types.flags import ProtectedItemEnum
    from randomizer.data.items.items import (
        MysteryEggItem, LambsLureItem, SheepAttackItem, StarEggItem,
    )

    world = _protect(ProtectedItemEnum.PROGRESSIVE_EGGS)
    for cls in (MysteryEggItem, LambsLureItem, SheepAttackItem):
        assert _byte0(world.get_item(cls)) & NO_SELL_BIT, cls.__name__
    # Star Egg is a separate option, not part of the progressive chain.
    assert not _byte0(world.get_item(StarEggItem)) & NO_SELL_BIT


def test_every_flag_option_maps_to_at_least_one_item():
    from randomizer.types.flags import ProtectedItemEnum
    from randomizer.logic.pre_shuffle.item_protection import _PROTECTED_ITEMS

    assert set(_PROTECTED_ITEMS) == set(ProtectedItemEnum)
    for option, classes in _PROTECTED_ITEMS.items():
        assert classes, f"{option} maps to no items"


def test_protection_does_not_leak_between_seeds():
    from randomizer.types.flags import ProtectedItemEnum
    from randomizer.data.items.items import LuckyJewelItem

    protected = _protect(ProtectedItemEnum.LUCKY_JEWEL)
    assert _byte0(protected.get_item(LuckyJewelItem)) & NO_SELL_BIT
    # A fresh world must not inherit the previous world's bit via class state.
    fresh = _protect()
    assert not _byte0(fresh.get_item(LuckyJewelItem)) & NO_SELL_BIT
    assert not _byte0(LuckyJewelItem()) & NO_SELL_BIT


def test_flag_string_round_trips_for_every_subset():
    from randomizer.types.settings import Settings
    from randomizer.types.flags import ProtectSpecialItems, ProtectedItemEnum

    options = list(ProtectedItemEnum)
    for size in range(len(options) + 1):
        for combo in itertools.combinations(options, size):
            settings = Settings()
            flag = settings.get_flag(ProtectSpecialItems)
            for option in combo:
                flag.enable(option)
            encoded = settings.get_flag_string()

            restored = Settings()
            restored.set_from_flag_string(encoded)
            assert set(restored.get_flag(ProtectSpecialItems).enabled) == set(combo), encoded


def test_hooks_do_not_overrun_their_replaced_instructions():
    from randomizer.patches.asm import unsellable_items

    patch = unsellable_items.get_patch()
    # $C3:3EF0 hook must end exactly at $3EFA (LDA $7FF8AF).
    assert 0x033EF0 + len(patch[0x033EF0]) == 0x033EFA
    # $C3:2BCD hook must end exactly at $2BD5 (JSR $2630).
    assert 0x032BCD + len(patch[0x032BCD]) == 0x032BD5
    # $C3:51CC hook must end exactly at $51D7 (LDA #$18, the message stub).
    assert 0x0351CC + len(patch[0x0351CC]) == 0x0351D7
    # The store at $C3:5230 is left vanilla: the $51CC gate refuses first, so it
    # is unreachable with a protected item.
    assert 0x035230 not in patch
    # The two sell-list rewrites are operand-only: 2 bytes each, leaving the
    # JSR opcode at $C3:4006 / $C3:401A intact.
    assert len(patch[0x034007]) == 2
    assert len(patch[0x03401B]) == 2


def test_hook_branches_land_on_the_vanilla_buzz_stubs():
    from randomizer.patches.asm import unsellable_items

    patch = unsellable_items.get_patch()

    sell = patch[0x033EF0]
    assert sell[0] == 0x20 and sell[1:3] == bytes([0x00, 0xF0])  # JSR $F000
    assert sell[3] == 0xF0                                        # BEQ
    assert 0x3EF5 + sell[4] == 0x3F3C                             # -> buzz stub

    discard = patch[0x032BCD]
    assert discard[0] == 0x20 and discard[1:3] == bytes([0x50, 0xF0])  # JSR $F050
    assert discard[3] == 0xF0                                          # BEQ
    assert 0x2BD2 + discard[4] == 0x2BEC                                # -> buzz stub

    # The maxed-out gate branches on the ALLOWED path (BNE -> confirm window);
    # refusal falls through into the vanilla message-#$18 stub at $C3:51D7.
    maxed = patch[0x0351CC]
    assert maxed[0] == 0x20 and maxed[1:3] == bytes([0x90, 0xF0])  # JSR $F090
    assert maxed[3] == 0xD0                                        # BNE, not BEQ
    assert 0x51D1 + maxed[4] == 0x51E2                             # -> confirm
    assert set(maxed[5:]) == {0xEA}                                # pad to $51D7


def test_free_space_block_stays_inside_its_claimed_page():
    from randomizer.patches.asm import unsellable_items

    block = unsellable_items.get_patch()[0x03F000]
    # $C3:F000-F3FF is the vanilla $FF run we claimed. Overflowing it would
    # walk into live bank-C3 data.
    assert len(block) <= 0x400


def test_no_collision_with_other_bank_c3_patches():
    # A miniature patch-audit: every other module that writes bank C3 must not
    # overlap our hooks. uncap_coins in particular writes $C3:3F03-09, nine
    # bytes past the sell hook.
    from randomizer.patches.asm import (
        unsellable_items, uncap_coins, uncap_max_fp, show_equips,
        grid_menu_navigation, menu_item_always_available, key_item_inventory,
        star_piece_sprite_fix, disable_garden_intro,
    )

    def spans(mod):
        return [range(off, off + len(b)) for off, b in mod.get_patch().items()]

    ours = spans(unsellable_items)
    others = [
        (mod.__name__, r)
        for mod in (uncap_coins, uncap_max_fp, show_equips, grid_menu_navigation,
                    menu_item_always_available, key_item_inventory,
                    star_piece_sprite_fix, disable_garden_intro)
        for r in spans(mod)
    ]

    for mine in ours:
        for name, theirs in others:
            overlap = range(max(mine.start, theirs.start), min(mine.stop, theirs.stop))
            assert not len(overlap), (
                f"unsellable_items {hex(mine.start)}-{hex(mine.stop - 1)} "
                f"collides with {name} at {hex(overlap.start)}"
            )
