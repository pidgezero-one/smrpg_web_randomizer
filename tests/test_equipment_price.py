"""Tests for equipment rank-based pricing."""


def test_calc_equip_rank_is_module_level_and_counts_buffs():
    from randomizer.logic.shufflers.equipment import calc_equip_rank
    from randomizer.data.items.items import TeamworkBandItem

    tb = TeamworkBandItem()
    # Vanilla TeamworkBand: zero raw stats, four temp buffs.
    assert tb.attack == 0
    assert tb.defense == 0
    assert tb.magic_attack == 0
    assert tb.magic_defense == 0
    assert len(tb.temp_buffs) == 4
    # 30 per buff, nothing else -> 120.
    assert calc_equip_rank(tb) == 120
