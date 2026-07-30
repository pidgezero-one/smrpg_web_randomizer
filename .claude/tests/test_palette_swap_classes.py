"""The palette-swap class table is generated from sprite data. It must not drift.

A class is a set of sprite ids whose definitions are byte-identical once
`palette_offset` is stripped, restricted to sprites that have real graphics and a
palette other than SPAL000_NOTHING. Without that filter the empty
protagonist-remap slots (sprites 31-37, 847-927, 997-1023) collapse into one
false 119-member class.
"""
from randomizer.data.sprites import palette_swap_classes as table
from randomizer.management.commands.palette_swap_classes import build_tables


def test_table_matches_regeneration():
    """Regenerating from current sprite data must reproduce the checked-in table."""
    pure, shifted = build_tables()
    assert pure == table.PURE
    assert shifted == table.SHIFTED


def test_no_sprite_is_in_both_tables():
    assert set(table.PURE) & set(table.SHIFTED) == set()


def test_canonical_sprites_are_not_themselves_merged():
    """A canonical target must never itself be a merge source, or merging is
    order-dependent."""
    merged = set(table.PURE) | set(table.SHIFTED)
    canonicals = set(table.PURE.values()) | {c for c, _ in table.SHIFTED.values()}
    assert canonicals & merged == set()


def test_known_pure_duplicates_present():
    """Sprite 386 is a byte-identical duplicate of 263 (Piranha Plant) at the
    same palette_offset, so merging it needs no palette work at all."""
    assert table.PURE[386] == 263


def test_known_offset_shift_present():
    """Bandana Blue (331) is Bandana Red (267) at pack offset 1."""
    assert table.SHIFTED[331] == (267, 1)


def test_bandana_class_splits_across_both_tables():
    """[267, 331, 380] at offsets [0, 1, 0]: 380 is a free duplicate of 267,
    331 needs a bump."""
    assert table.PURE[380] == 267
    assert table.SHIFTED[331] == (267, 1)
