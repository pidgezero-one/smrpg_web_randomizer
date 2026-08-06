"""Scale boss stats to the difficulty of the location they were shuffled into.

Extracted from the apply_shuffler_results orchestrator.
"""

from __future__ import annotations

from typing import TYPE_CHECKING
import random
import statistics
from randomizer.data.enemies.enemies import (CULEX3DEnemy)
from randomizer.logic.progression.prizes import (
    Belome3Fight,
    Booster2BossFight,
    Bundt2BossFight,
    Culex3DBossFight,
    Jinx4BossFight,
    Johnny2Fight,
    Punchinello2BossFight,
    SmithyBossFight,
)
from randomizer.types.enemy import (Enemy)
from randomizer.types.flags import (BossScaleOptions, BossShuffleScaleStats)
from randomizer.types.prize import (BossFightPrize)
from randomizer.types.prizelocation import (BossFightLocation)
from typing import (cast)

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld


# --- Godmode reference enemy (swap this class to re-center normalization) ---
_GODMODE_REFERENCE_ENEMY: type = CULEX3DEnemy

# Fights excluded from Godmode normalization (final boss + postgame)
_GODMODE_EXCLUDED_FIGHTS: tuple[type, ...] = (
    SmithyBossFight,
    Punchinello2BossFight,
    Booster2BossFight,
    Bundt2BossFight,
    Johnny2Fight,
    Belome3Fight,
    Jinx4BossFight,
    Culex3DBossFight,
)

def _calculate_location_stats(
    location: BossFightLocation,
    world: GameWorld,
) -> tuple[int, int, int, int, int, int, int, int, int]:
    """Calculate the summed stats for a location based on its original boss.

    Derives all exclusions and multipliers from the original prize's configuration:
    - HP = sum of formation members participating in HP slicing (not in hp_slice_excluded
      or scaling_excluded), plus extra_hp_enemies, with hp_pie_contribution_multipliers applied
    - Other stats = average of anchor_enemy (or all non-excluded formation members if None)

    Returns (hp, xp, coins, attack, defense, magic_attack, magic_defense, evade, magic_evade)
    """
    original_prize_class = location._originally_held
    if original_prize_class is None:
        return (0, 0, 0, 0, 0, 0, 0, 0, 0)

    original_prize = original_prize_class()
    if not isinstance(original_prize, BossFightPrize):
        return (0, 0, 0, 0, 0, 0, 0, 0, 0)

    # Enemies completely excluded from all scaling (e.g., WaterCrystal, Hangin' Shy)
    scaling_excluded = set(original_prize.scaling_excluded_enemies)

    # Enemies excluded from HP slicing (they don't take from the pie, so don't contribute to location HP)
    hp_slice_excluded = set(original_prize.hp_slice_excluded_enemies)

    hp_counted_members = [
        m for m in original_prize.formation_members
        if m is not None and m.enemy not in scaling_excluded and m.enemy not in hp_slice_excluded
    ]

    # Include extra_hp_enemies from the prize (e.g., King Calamari's extra tentacles)
    hp_enemy_pairs: list[tuple[Enemy, type]] = []
    for m in hp_counted_members:
        hp_enemy_pairs.append((cast(Enemy, m.enemy()), m.enemy))
    for e_class in original_prize.extra_hp_enemies:
        if e_class not in scaling_excluded:
            hp_enemy_pairs.append((cast(Enemy, e_class()), e_class))

    # Get HP contribution multipliers from the prize (e.g., Dodo at 0.4)
    hp_multipliers = original_prize.hp_pie_contribution_multipliers

    hp = 0
    xp = 0
    coins = 0
    for enemy, enemy_class in hp_enemy_pairs:
        multiplier = hp_multipliers.get(enemy_class, 1.0)
        hp += round(enemy.hp * multiplier)
        xp += enemy.xp
        coins += enemy.coins

    # Apply location HP multiplier (e.g., Cloaker/Domino: you only fight 2 of 4 enemies)
    hp = round(hp * original_prize.location_hp_multiplier)

    anchor_spec = original_prize.anchor_enemy
    if anchor_spec is None:
        anchor_classes = [
            m.enemy for m in original_prize.formation_members
            if m is not None and m.enemy not in scaling_excluded
        ]
    elif isinstance(anchor_spec, list):
        anchor_classes = anchor_spec
    else:
        anchor_classes = [anchor_spec]

    if anchor_classes:
        anchor_enemies = [cast(Enemy, c()) for c in anchor_classes]
        attack = int(round(statistics.mean(e.attack for e in anchor_enemies)))
        defense = int(round(statistics.mean(e.defense for e in anchor_enemies)))
        magic_attack = int(round(statistics.mean(e.magic_attack for e in anchor_enemies)))
        magic_defense = int(round(statistics.mean(e.magic_defense for e in anchor_enemies)))
        evade = int(round(statistics.mean(e.evade for e in anchor_enemies)))
        magic_evade = int(round(statistics.mean(e.magic_evade for e in anchor_enemies)))
    else:
        attack = defense = magic_attack = magic_defense = evade = magic_evade = 0

    return (hp, xp, coins, attack, defense, magic_attack, magic_defense, evade, magic_evade)

def _apply_stats_to_prize(
    prize: BossFightPrize,
    stats: tuple[int, int, int, int, int, int, int, int, int],
    world: GameWorld,
) -> None:
    """Apply scaled stats to a prize's enemies using anchor-based ratios.

    HP Slicing:
    - Enemies NOT in hp_slice_excluded_enemies divide the location HP proportionally
      based on their original HP relative to total original HP of participants
    - Enemies IN hp_slice_excluded_enemies (or additional_enemies_to_scale) get HP
      scaled relative to anchor: anchor_new_hp * (original_hp / anchor_original_hp)

    Other Stats:
    - Anchor enemy gets the location stat directly
    - Non-anchor enemies get: location_stat * (original_stat / anchor_original_stat)

    Args:
        prize: The boss fight prize to scale
        stats: (hp, xp, coins, attack, defense, magic_attack, magic_defense, evade, magic_evade)
        world: The game world containing enemy instances
    """
    location_hp, xp, coins, attack, defense, magic_attack, magic_defense, evade, magic_evade = stats

    if location_hp == 0:
        return  # No stats to apply

    formation_members = [m for m in prize.formation_members if m is not None]
    if not formation_members:
        return

    scaling_excluded = set(prize.scaling_excluded_enemies)

    # m.enemy is already a type[Enemy], not an instance
    enemy_classes_in_formation = {m.enemy for m in formation_members if m.enemy not in scaling_excluded}
    all_enemy_classes = enemy_classes_in_formation | set(prize.additional_enemies_to_scale)

    # Each entry in extra_hp_enemies represents one enemy instance
    enemy_counts: dict[type, int] = {}
    for m in formation_members:
        if m.enemy not in scaling_excluded:
            enemy_counts[m.enemy] = enemy_counts.get(m.enemy, 0) + 1
    for e in prize.extra_hp_enemies:
        if e not in scaling_excluded:
            enemy_counts[e] = enemy_counts.get(e, 0) + 1
            all_enemy_classes.add(e)

    if not enemy_classes_in_formation:
        return  # All formation members were excluded

    anchor_spec = prize.anchor_enemy

    # Normalize anchor_spec to a list of classes for averaging, or None for all formation members
    if anchor_spec is None:
        # Use average of all formation enemies as reference
        anchor_classes: list[type] = list(enemy_classes_in_formation)
    elif isinstance(anchor_spec, list):
        # Use average of specified enemies as reference
        anchor_classes = anchor_spec
    else:
        # Single anchor class
        anchor_classes = [anchor_spec]

    anchor_instances = [cast(Enemy, c()) for c in anchor_classes]
    num_anchors = len(anchor_instances)
    ref_hp: float = sum(e.hp for e in anchor_instances) / num_anchors
    ref_attack: float = sum(e.attack for e in anchor_instances) / num_anchors
    ref_defense: float = sum(e.defense for e in anchor_instances) / num_anchors
    ref_magic_attack: float = sum(e.magic_attack for e in anchor_instances) / num_anchors
    ref_magic_defense: float = sum(e.magic_defense for e in anchor_instances) / num_anchors
    ref_evade: float = sum(e.evade for e in anchor_instances) / num_anchors
    ref_magic_evade: float = sum(e.magic_evade for e in anchor_instances) / num_anchors

    # Enemies excluded from HP slicing - they don't take from the pie
    hp_slice_excluded = set(prize.hp_slice_excluded_enemies) | set(prize.additional_enemies_to_scale)

    pie_multipliers = prize.hp_pie_contribution_multipliers

    hp_slice_participant_classes = {c for c in enemy_counts.keys() if c not in hp_slice_excluded}
    total_pie_hp_for_slicing = sum(
        cast(Enemy, c()).hp * pie_multipliers.get(c, 1.0) * enemy_counts[c]
        for c in hp_slice_participant_classes
    ) if hp_slice_participant_classes else 0

    # Calculate pie-adjusted reference HP (for scaling excluded enemies)
    # The reference HP should also use the pie multiplier for consistency
    avg_pie_multiplier = sum(pie_multipliers.get(c, 1.0) for c in anchor_classes) / len(anchor_classes)
    ref_pie_hp = ref_hp * avg_pie_multiplier
    if total_pie_hp_for_slicing > 0:
        ref_new_hp = round(location_hp * (ref_pie_hp / total_pie_hp_for_slicing))
    else:
        # No participants in slicing - reference gets full location HP
        ref_new_hp = location_hp

    # === XP/Coins pie slicing (mirrors HP slicing, accounting for instance counts) ===
    xp_slice_participant_classes = {c for c in enemy_counts.keys() if c not in hp_slice_excluded}
    total_xp_for_slicing = sum(
        cast(Enemy, c()).xp * enemy_counts[c]
        for c in xp_slice_participant_classes
    ) if xp_slice_participant_classes else 0
    total_coins_for_slicing = sum(
        cast(Enemy, c()).coins * enemy_counts[c]
        for c in xp_slice_participant_classes
    ) if xp_slice_participant_classes else 0

    ref_xp: float = sum(cast(Enemy, c()).xp for c in anchor_classes) / len(anchor_classes)
    ref_coins: float = sum(cast(Enemy, c()).coins for c in anchor_classes) / len(anchor_classes)
    if total_xp_for_slicing > 0:
        ref_new_xp = round(xp * (ref_xp / total_xp_for_slicing))
    else:
        ref_new_xp = xp
    if total_coins_for_slicing > 0:
        ref_new_coins = round(coins * (ref_coins / total_coins_for_slicing))
    else:
        ref_new_coins = coins

    def scale_stat(loc_stat: int, orig_stat: int, ref_orig: float, ratio: float) -> int:
        if ref_orig > 0:
            result = round(loc_stat * (orig_stat / ref_orig) * ratio)
        else:
            result = round(orig_stat * ratio)
        return max(0, min(255, result))

    for enemy_class in all_enemy_classes:
        enemy = cast(Enemy, world.get_enemy(cast(type[Enemy], enemy_class)))
        if enemy is None:
            continue

        original = cast(Enemy, enemy_class())

        # === HP Calculation ===
        pie_adjusted_hp = original.hp * pie_multipliers.get(cast(type[Enemy], enemy_class), 1.0)

        if enemy_class in hp_slice_excluded:
            # Excluded from pie - scale relative to reference
            if ref_hp > 0:
                new_hp = round(ref_new_hp * (original.hp / ref_hp))
            else:
                new_hp = original.hp
        elif total_pie_hp_for_slicing > 0:
            # Participate in pie slicing - use pie-adjusted HP for share calculation
            new_hp = round(location_hp * (pie_adjusted_hp / total_pie_hp_for_slicing))
        else:
            new_hp = original.hp

        # Apply hp_slice_multiplier if defined for this enemy class
        # (e.g., Dodo gets 2.5x his calculated HP slice)
        slice_multiplier = prize.hp_slice_multipliers.get(cast(type[Enemy], enemy_class), 1.0)
        new_hp = round(new_hp * slice_multiplier)

        new_hp = min(0xFFFF, round(new_hp * enemy.ratio_hp))
        enemy.set_hp(new_hp)

        # === Other Stats ===
        # All enemies scale relative to reference (average or anchor)
        enemy.set_attack(min(enemy.max_shuffled_attack, scale_stat(attack, original.attack, ref_attack, enemy.ratio_attack)))
        enemy.set_defense(scale_stat(defense, original.defense, ref_defense, enemy.ratio_defense))
        enemy.set_magic_attack(min(enemy.max_shuffled_magic_attack, scale_stat(magic_attack, original.magic_attack, ref_magic_attack, enemy.ratio_magic_attack)))
        enemy.set_magic_defense(scale_stat(magic_defense, original.magic_defense, ref_magic_defense, enemy.ratio_magic_defense))
        enemy.set_evade(min(100, scale_stat(evade, original.evade, ref_evade, enemy.ratio_evade)))
        enemy.set_magic_evade(min(100, scale_stat(magic_evade, original.magic_evade, ref_magic_evade, enemy.ratio_magic_evade)))

        # === XP Calculation (mirrors HP slicing) ===
        if enemy_class in hp_slice_excluded:
            # Excluded from pie - scale relative to anchor
            if ref_xp > 0:
                new_xp = round(ref_new_xp * (original.xp / ref_xp))
            else:
                new_xp = original.xp
        elif total_xp_for_slicing > 0:
            # Participate in pie - divide location XP proportionally (counts in denominator)
            new_xp = round(xp * (original.xp / total_xp_for_slicing))
        else:
            new_xp = original.xp
        enemy.set_xp(max(1, new_xp))

        # === Coins Calculation (mirrors HP slicing) ===
        if enemy_class in hp_slice_excluded:
            if ref_coins > 0:
                new_coins = round(ref_new_coins * (original.coins / ref_coins))
            else:
                new_coins = original.coins
        elif total_coins_for_slicing > 0:
            new_coins = round(coins * (original.coins / total_coins_for_slicing))
        else:
            new_coins = original.coins
        enemy.set_coins(max(0, new_coins))

def apply_boss_stat_scaling(world: GameWorld) -> None:
    """Apply stat scaling to boss fights based on settings.

    Modes:
    - VANILLA: No stat changes
    - MATCH: Each relocated location's original stats apply to its current prize
    - RANDOM: Relocated location stats are randomly assigned to prizes (one-to-one)
    - GODMODE: Every boss is normalized to endgame-level stats

    Note: MATCH/RANDOM only touch bosses that were shuffled to a different
    location; GODMODE scales all boss fights, including those left in place.
    """
    if world.settings.is_flag_value(BossShuffleScaleStats, BossScaleOptions.VANILLA):
        return  # No scaling needed

    # Calculate stats for every boss fight location with a valid prize.
    # Unmoved bosses (prize still on its own location) are kept in the list;
    # MATCH/RANDOM filter them out below, but GODMODE scales them too.
    location_stats: list[tuple[BossFightLocation, tuple[int, int, int, int, int, int, int, int, int]]] = []
    for location in world.locations.values():
        if not isinstance(location, BossFightLocation):
            continue
        stats = _calculate_location_stats(location, world)
        if stats[0] > 0:  # Only include if valid stats (HP > 0)
            location_stats.append((location, stats))

    if not location_stats:
        return

    if world.settings.is_flag_value(BossShuffleScaleStats, BossScaleOptions.MATCH):
        # Unmoved bosses already hold their correct stats, so skip them.
        for location, stats in location_stats:
            if isinstance(location.prize, location._originally_held):
                continue
            assert isinstance(location.prize, BossFightPrize)
            _apply_stats_to_prize(location.prize, stats, world)

    elif world.settings.is_flag_value(BossShuffleScaleStats, BossScaleOptions.RANDOM):
        # Create random one-to-one mapping between location stats and prizes.
        # Only relocated bosses participate in the shuffle.
        moved = [
            (loc, stats) for loc, stats in location_stats
            if not isinstance(loc.prize, loc._originally_held)
        ]
        prizes = [loc.prize for loc, _ in moved]
        stats_list = [stats for _, stats in moved]

        random.shuffle(stats_list)

        for prize, stats in zip(prizes, stats_list):
            assert isinstance(prize, BossFightPrize)
            _apply_stats_to_prize(prize, stats, world)

    elif world.settings.is_flag_value(BossShuffleScaleStats, BossScaleOptions.GODMODE):
        # Normalize every boss's combat stats to the reference enemy's average,
        # including bosses left on their own location (no moved/unmoved filter).
        ref = _GODMODE_REFERENCE_ENEMY()
        culex_avg = round(statistics.mean([ref._attack, ref._defense, ref._magic_attack, ref._magic_defense]))

        for location, stats in location_stats:
            # Skip final boss and postgame fights
            if type(location.prize) in _GODMODE_EXCLUDED_FIGHTS:
                continue

            orig_hp, xp, coins, attack, defense, m_atk, m_def, evade, m_evade = stats
            orig_avg = round(statistics.mean([attack, defense, m_atk, m_def]))
            if orig_avg == 0:
                continue

            sponginess_ratio = orig_hp / orig_avg
            godmode_hp = min(9999, max(1, round(sponginess_ratio * culex_avg)))
            capped_avg = min(255, culex_avg)
            godmode_stats = (godmode_hp, xp, coins, capped_avg, capped_avg, capped_avg, capped_avg, evade, m_evade)

            assert isinstance(location.prize, BossFightPrize)
            _apply_stats_to_prize(location.prize, godmode_stats, world)


__all__ = ["apply_boss_stat_scaling"]
