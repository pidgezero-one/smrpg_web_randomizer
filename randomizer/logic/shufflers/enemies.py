"""Enemy randomization logic."""
from __future__ import annotations
import random
from functools import reduce
from typing import TYPE_CHECKING, cast

from smrpgpatchbuilder.datatypes.spells.enums import Element, Status
from smrpgpatchbuilder.datatypes.enemies.enums import FlowerBonusType
from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (
    FormationMember,
)

from ..utils import mutate_normal

if TYPE_CHECKING:
    from smrpgpatchbuilder.datatypes.items.classes import RegularItem
    from ...types.gameworld import GameWorld


def randomize_enemy_attacks_and_spells(world: GameWorld) -> None:
    """Randomize enemy spell and attack stats and effects."""
    from randomizer.types.spell import EnemySpell

    # Status effects that can be randomly assigned (excluding berserk for safety)
    safe_statuses = [
        Status.MUTE,
        Status.SLEEP,
        Status.POISON,
        Status.FEAR,
        Status.MUSHROOM,
        Status.SCARECROW,
    ]

    # Randomize enemy spells
    for spell in world.spells.spells:
        if not isinstance(spell, EnemySpell):
            continue

        # Mutate FP cost (max 31 due to game limitation)
        new_fp = mutate_normal(int(spell.fp), minimum=1, maximum=31)
        spell.set_fp(new_fp)

        # Shuffle status effects if the spell has any
        if spell.status_effects:
            num_effects = len(spell.status_effects)
            new_effects = random.sample(
                safe_statuses, min(num_effects, len(safe_statuses))
            )
            spell.set_status_effects(new_effects)

        # Mutate power
        new_power = mutate_normal(int(spell.power), minimum=0, maximum=255)
        spell.set_power(int(max(0, min(255, new_power))))

        # Mutate hit rate (cap at 99 if it's an instant KO spell)
        max_hit = 99 if spell.check_ohko else 100
        new_hit_rate = mutate_normal(int(spell.hit_rate), minimum=1, maximum=max_hit)
        spell.set_hit_rate(new_hit_rate)

    # Randomize enemy attacks
    for attack in world.enemy_attacks.attacks:
        # Mutate attack level (0-7 range)
        new_level = mutate_normal(int(attack.attack_level), minimum=0, maximum=7)
        attack.set_attack_level(new_level)

        # Shuffle status effects if the attack has any
        if attack.status_effects:
            num_effects = len(attack.status_effects)
            new_effects = random.sample(
                safe_statuses, min(num_effects, len(safe_statuses))
            )
            attack.set_status_effects(new_effects)

        # Mutate hit rate (cap at 99 if OHKO to allow protection to work, 100 otherwise)
        max_hit = 99 if attack.ohko else 100
        new_hit_rate = mutate_normal(int(attack.hit_rate), minimum=1, maximum=max_hit)
        attack.set_hit_rate(new_hit_rate)


def randomize_enemy_stats(world: GameWorld) -> None:
    """Randomize enemy stats based on EnemyStats flag setting."""
    from randomizer.data.enemies.enemies import (
        SMITHY2Enemy,
        SMITHYTankEnemy,
        SMITHYSafeEnemy2,
        SMITHYMageEnemy,
        SMITHYChestEnemy,
    )
    from randomizer.types.flags import EnemyStats, EnemyStatsShuffleOptions
    from randomizer.types.enemy import Enemy as CustomEnemy

    full_random = (
        world.settings.get_flag(EnemyStats).selected
        == EnemyStatsShuffleOptions.FULL_RANDOM
    )

    # Get list of non-boss enemies for inter-shuffling
    non_boss_enemies = [e for e in world.enemies.enemies if not e.ohko_immune]
    all_enemies = list(world.enemies.enemies)

    # Determine which attributes to shuffle
    if full_random:
        shuffle_attrs = [
            "hp", "speed", "defense", "magic_defense", "evade", "magic_evade",
            "resistances", "weaknesses", "status_immunities",
        ]
    else:
        shuffle_attrs = [
            "hp", "speed", "defense", "magic_defense", "evade", "magic_evade",
        ]

    # Inter-shuffle stats between similar-ranked enemies
    for attr in shuffle_attrs:
        shuffled = list(non_boss_enemies)
        max_index = len(non_boss_enemies) - 1
        done: set = set()

        for i in range(len(non_boss_enemies)):
            if shuffled[i] in done:
                continue
            new_index = i
            while random.randint(0, 1) == 1:
                new_index += 1
            new_index = min(new_index, max_index)
            a, b = shuffled[i], shuffled[new_index]
            done.add(a)
            shuffled[i] = b
            shuffled[new_index] = a

        # Swap attribute values
        swaps = [getattr(s, attr) for s in shuffled]
        for enemy, swapped_val in zip(non_boss_enemies, swaps):
            setter_name = f"set_{attr}"
            if hasattr(enemy, setter_name):
                setter = getattr(enemy, setter_name)
                if isinstance(swapped_val, list):
                    setter(list(swapped_val))
                else:
                    setter(int(swapped_val))

    # Inter-shuffle morph chances randomly (for non-boss enemies)
    if full_random:
        morph_chances = [e.morph_chance for e in non_boss_enemies]
        random.shuffle(morph_chances)
        for chance, enemy in zip(morph_chances, non_boss_enemies):
            enemy.set_morph_chance(chance)

    # Mutate individual enemy stats
    for enemy in all_enemies:
        old_stats = {
            "hp": int(enemy.hp),
            "speed": int(enemy.speed),
            "attack": int(enemy.attack),
            "defense": int(enemy.defense),
            "magic_attack": int(enemy.magic_attack),
            "magic_defense": int(enemy.magic_defense),
            "fp": int(enemy.fp),
            "evade": int(enemy.evade),
            "magic_evade": int(enemy.magic_evade),
        }

        # Mutate numeric stats
        enemy.set_hp(mutate_normal(int(enemy.hp), minimum=1, maximum=32000))
        enemy.set_speed(mutate_normal(int(enemy.speed), minimum=0, maximum=255))
        enemy.set_attack(mutate_normal(int(enemy.attack), minimum=1, maximum=255))
        enemy.set_defense(mutate_normal(int(enemy.defense), minimum=1, maximum=255))
        enemy.set_magic_attack(mutate_normal(int(enemy.magic_attack), minimum=1, maximum=255))
        enemy.set_magic_defense(mutate_normal(int(enemy.magic_defense), minimum=1, maximum=255))
        enemy.set_fp(mutate_normal(int(enemy.fp), minimum=1, maximum=31))
        enemy.set_evade(mutate_normal(int(enemy.evade), minimum=0, maximum=100))
        enemy.set_magic_evade(mutate_normal(int(enemy.magic_evade), minimum=0, maximum=100))

        # For bosses, don't let stats go below vanilla values
        if enemy.ohko_immune:
            for attr, old_val in old_stats.items():
                current_val = int(getattr(enemy, attr))
                if current_val < old_val:
                    setter = getattr(enemy, f"set_{attr}")
                    setter(old_val)

            # Small 1/255 chance for boss to be vulnerable to Geno Whirl
            if random.randint(1, 255) == 1:
                enemy.set_ohko_immune(False)
        else:
            # For non-bosses: 1/3 chance to reverse OHKO immunity
            if random.randint(1, 3) == 3:
                enemy.set_ohko_immune(not enemy.ohko_immune)

            # Randomize morph chance (only in FULL_RANDOM mode)
            if full_random:
                morph_options = [0, 25, 75, 100]
                enemy.set_morph_chance(random.choice(morph_options))

        # FULL_RANDOM: also shuffle elemental resistances/weaknesses
        if full_random:
            _randomize_enemy_elements_and_statuses(enemy)

    # Special logic for Smithy 2: All heads must have the same HP
    try:
        main_head = world.enemies.get_by_type(SMITHY2Enemy)
        for head_type in [SMITHYTankEnemy, SMITHYSafeEnemy2, SMITHYMageEnemy, SMITHYChestEnemy]:
            head = world.enemies.get_by_type(head_type)
            head.set_hp(int(main_head.hp))
    except (KeyError, StopIteration):
        pass

    # Update psychopath messages based on new stats
    for enemy in all_enemies:
        custom_enemy = cast(CustomEnemy, enemy)
        custom_enemy.set_psychopath_message(custom_enemy.build_psychopath_text())


def _randomize_enemy_elements_and_statuses(enemy) -> None:
    """Randomize elemental resistances/weaknesses and status immunities for an enemy."""
    total_immunities = len(enemy.status_immunities) + len(enemy.resistances)
    new_status_immunities = random.randint(
        max(0, total_immunities - 4), min(total_immunities, 4)
    )
    new_resistances = total_immunities - new_status_immunities
    new_status_immunities = max(0, min(4, new_status_immunities))
    new_resistances = max(0, min(4, new_resistances))

    available_statuses = [Status.MUTE, Status.SLEEP, Status.POISON, Status.FEAR]
    enemy.set_status_immunities(
        random.sample(available_statuses, min(new_status_immunities, len(available_statuses)))
    )

    available_elements = [Element.ICE, Element.THUNDER, Element.FIRE, Element.JUMP]

    if random.randint(0, 1) == 0:
        # Prioritize resistances
        new_res = random.sample(available_elements, min(new_resistances, len(available_elements)))
        enemy.set_resistances(new_res)
        potential_weak = list(set(available_elements) - set(new_res))
        potential_weak.append(Element.JUMP)
        potential_weak = list(set(potential_weak))
        current_weak_count = len(enemy.weaknesses)
        enemy.set_weaknesses(
            random.sample(potential_weak, min(current_weak_count, len(potential_weak)))
        )
    else:
        # Prioritize weaknesses
        current_weak_count = len(enemy.weaknesses)
        new_weak = random.sample(available_elements, min(current_weak_count, len(available_elements)))
        enemy.set_weaknesses(new_weak)
        potential_res = list(set(available_elements) - set(new_weak))
        potential_res.append(Element.JUMP)
        potential_res = list(set(potential_res))
        enemy.set_resistances(
            random.sample(potential_res, min(new_resistances, len(potential_res)))
        )

    # Randomize flower bonus type and chance
    flower_types = [
        FlowerBonusType.ATTACK_UP, FlowerBonusType.DEFENSE_UP, FlowerBonusType.HP_MAX,
        FlowerBonusType.ONCE_AGAIN, FlowerBonusType.LUCKY,
    ]
    enemy.set_flower_bonus_type(random.choice(flower_types))
    chance = (random.randint(0, 5) + random.randint(0, 5)) * 10
    enemy.set_flower_bonus_chance(chance)


def randomize_enemy_drops(
    world: GameWorld,
    consumables_group_1: list[type[RegularItem]],
    consumables_group_2: list[type[RegularItem]],
) -> None:
    """Randomize enemy drops (coins, XP, items)."""
    for enemy in world.enemies.enemies:
        # Mutate coins
        enemy.set_coins(mutate_normal(int(enemy.coins), minimum=0, maximum=255))

        # Mutate XP
        old_xp = int(enemy.xp)
        new_xp = mutate_normal(old_xp, minimum=1, maximum=0xFFFF)

        # For bosses, don't let XP go above vanilla; for normal enemies, don't go below
        if enemy.ohko_immune:
            enemy.set_xp(min(old_xp, new_xp))
        else:
            enemy.set_xp(max(old_xp, new_xp))

        # Shuffle reward items
        linked = enemy.common_item_drop == enemy.rare_item_drop

        if enemy.common_item_drop is not None:
            enemy.set_common_item_drop(random.choice(consumables_group_1))

        if linked:
            enemy.set_rare_item_drop(enemy.common_item_drop)
        elif enemy.rare_item_drop is not None:
            enemy.set_rare_item_drop(random.choice(consumables_group_2))

        if enemy.morph_chance > 0:
            enemy.set_yoshi_cookie_item(random.choice(consumables_group_2))


VALID_FORMATION_COORDINATES = [
    (119, 103), (135, 111), (151, 119), (167, 127),
    (103, 111), (119, 119), (135, 127), (151, 135),
    (87, 119), (103, 127), (119, 135), (135, 143),
    (71, 127), (87, 135), (103, 143), (119, 151),
    (55, 135), (71, 143), (87, 151), (103, 159),
    (39, 143), (55, 151), (71, 159), (87, 167),
]


def _get_distance(x1: int, y1: int, x2: int, y2: int) -> float:
    """Calculate Euclidean distance between two points."""
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def _get_collective_distance(x1: int, y1: int, points: list[tuple[int, int]]) -> float:
    """Calculate the product of distances from a point to all other points."""
    if not points:
        return 1.0
    distances = [_get_distance(x1, y1, x2, y2) for x2, y2 in points]
    return reduce(lambda a, b: a * b, distances, 1.0)


def _select_most_distant(
    possible_points: list[tuple[int, int]], used_points: list[tuple[int, int]]
) -> tuple[int, int]:
    """Select the point from possible_points that is most distant from used_points."""
    available = [p for p in possible_points if p not in used_points]
    if not available:
        available = possible_points
    return max(available, key=lambda c: _get_collective_distance(c[0], c[1], used_points))


def generate_formation_coordinates(
    count: int,
    valid_coordinates: list[tuple[int, int]] | None = None,
) -> list[tuple[int, int]]:
    """
    Generate a list of formation coordinates that are well-spaced from each other.

    Args:
        count: The number of coordinates to generate.
        valid_coordinates: Optional list of valid coordinate positions to choose from.
                          Defaults to VALID_FORMATION_COORDINATES.

    Returns:
        A list of (x, y) coordinate tuples.
    """
    if valid_coordinates is None:
        valid_coordinates = VALID_FORMATION_COORDINATES

    if count <= 0:
        return []

    result: list[tuple[int, int]] = []

    for i in range(count):
        if not result:
            # First coordinate: pick randomly
            x, y = random.choice(valid_coordinates)
        else:
            # Subsequent coordinates: maximize distance from already-chosen ones
            sample_size = min(len(valid_coordinates), count * 2)
            candidate_coords = random.sample(valid_coordinates, sample_size)
            x, y = _select_most_distant(candidate_coords, result)

        result.append((x, y))

    return result


def randomize_enemy_formations(world: GameWorld) -> None:
    """Randomize enemy formations."""
    max_enemies = 6

    for pack in world.battle_packs.packs:
        for formation in pack.formations:
            current_members = [m for m in formation.members if m is not None]
            if not current_members:
                continue
            if any(m.hidden_at_start for m in current_members):
                continue
            if not formation.can_run_away:
                continue

            current_enemy_types = list(set(m.enemy for m in current_members))
            candidates = list(current_enemy_types)

            all_enemy_types = [type(e) for e in world.enemies.enemies if not e.ohko_immune]
            while len(candidates) < 3 and all_enemy_types:
                new_enemy = random.choice(all_enemy_types)
                if new_enemy not in candidates:
                    candidates.append(new_enemy)

            num_enemies = random.randint(1, random.randint(3, max_enemies))
            num_enemies = max(num_enemies, len(current_enemy_types))

            chosen_enemies: list[type] = list(current_enemy_types)
            while len(chosen_enemies) < num_enemies:
                sub_candidates = candidates + chosen_enemies
                if not sub_candidates:
                    break
                chosen_enemies.append(random.choice(sub_candidates))

            random.shuffle(chosen_enemies)

            coordinates = generate_formation_coordinates(len(chosen_enemies))

            new_members: list[FormationMember | None] = []
            for enemy_type, (x, y) in zip(chosen_enemies, coordinates):
                new_members.append(
                    FormationMember(enemy=enemy_type, x_pos=x, y_pos=y, hidden_at_start=False)
                )

            formation.set_members(new_members)


def apply_exp_multiplier(world: GameWorld) -> None:
    """Apply EXP multiplier to all enemies based on settings."""
    from randomizer.types.flags import EXPMultiplier, EXPMultiplierOptions

    exp_setting = world.settings.get_flag(EXPMultiplier).selected

    if exp_setting == EXPMultiplierOptions.VANILLA:
        return

    multiplier = 1
    if exp_setting == EXPMultiplierOptions.DOUBLE:
        multiplier = 2
    elif exp_setting == EXPMultiplierOptions.TRIPLE:
        multiplier = 3

    for enemy in world.enemies.enemies:
        current_xp = enemy.xp
        new_xp = min(9999, current_xp * multiplier)
        enemy.set_xp(new_xp)
