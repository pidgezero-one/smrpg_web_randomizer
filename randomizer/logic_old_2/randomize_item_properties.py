"""Randomization logic for item properties (not shuffling)."""

from copy import copy
from enum import StrEnum
from random import choice, choices, randint, sample, shuffle
from randomizer.entities.items.items import (
    Amulet,
    AntidotePin,
    AttackScarf,
    BtubRing,
    CoinTrick,
    CourageShell,
    Cymbals,
    ExpBooster,
    FearlessPin,
    Feather,
    FireCape,
    FireDress,
    FirePants,
    FireShell,
    FireShirt,
    FroggieStick,
    FuzzyCape,
    FuzzyDress,
    FuzzyPants,
    FuzzyShirt,
    GhostMedal,
    HappyCape,
    HappyPants,
    HappyShell,
    HappyShirt,
    HealShell,
    HeroShirt,
    JinxBelt,
    JumpShoes,
    MegaCape,
    MegaPants,
    MegaShirt,
    Mushroom2,
    NauticaDress,
    Pants,
    Parasol,
    PolkaDress,
    PrincePants,
    RareScarf,
    RibbitStick,
    RoyalDress,
    SafetyBadge,
    SafetyRing,
    SailorCape,
    SailorPants,
    SailorShirt,
    ScroogeRing,
    Shirt,
    SignalRing,
    SonicCymbal,
    StarCape,
    ThickPants,
    ThickShirt,
    TroopaPin,
    TrueformPin,
    WakeUpPin,
    WarFan,
    ZoomShoes)
from randomizer.types.items.classes import Accessory, Armor, Equipment, Weapon
from randomizer.types.items.constants import EQUIP_STATS
from randomizer.types.items.enums import EffectType
from randomizer.types.overworld_scripts.arguments.area_objects import (
    BOWSER,
    GENO,
    MALLOW,
    MARIO,
    TOADSTOOL)
from randomizer.types.overworld_scripts.event_scripts.commands.commands import (
    JmpToEvent)
from randomizer.types.overworld_scripts.event_scripts.ids.script_ids import (
    E0021_FOREST_MAZE_MUSHROOM_GRANT,
    E0042_GRANT_ANY_CONSUMABLE_TIER_2_CAP,
    E0051_GRANT_ANY_CONSUMABLE_EXCLUDE_WORST_CUSTOM_CAP,
    E0057_GRANT_ANY_CONSUMABLE_CUSTOM_CAP,
    E0622_MARRYMORE_INN_ELDERLY_GUEST_TIP_SUBROUTINE_1,
    E0626_MARRYMORE_INN_ELDERLY_GUEST_TIP_SUBROUTINE_FLOWERBOX,
    E1973_CLONE_RESERVED,
    E2649_CASINO_GRATE_GUY_RANDOM_PRIZE_GRANTER,
    E2670_TOWER_KNIFE_GUY_CONSOLATION_PRIZE)
from randomizer.types.spells.enums import Element, Status, TempStatBuff
from randomizer.types.world.classes import GameWorld
from randomizer.types.world.flags.enums import (
    EquipmentCharactersOptions,
    EquipmentPropertiesOptions)
from randomizer.types.world.flags.flags import (
    EnemyNoSafetyChecks,
    EquipmentCharacters,
    EquipmentNoSafety,
    EquipmentProperties,
    PoisonMushroom)
from randomizer.utils.number import coin_flip, mutate_normal
from randomizer.utils.snippets.es_any_mushroom import script as random_mushroom


def _calculate_rank_value(item: Armor | Weapon | Accessory) -> int:
    attack_factor = (item.attack + item.variance) / (
        1 if item.attack - item.variance == 0 else item.attack - item.variance
    )
    attack_weight = item.attack * max(0, min(2, attack_factor))

    magic_attack_factor = item.magic_attack / (2 if item.magic_attack < 0 else 1)
    magic_defense_factor = item.magic_defense / (2 if item.magic_defense < 0 else 1)
    defense_factor = item.defense / (2 if item.defense < 0 else 1)
    speed_factor = min(20, item.speed / 2)
    other_stat_weight = max(
        0, magic_attack_factor + magic_defense_factor + defense_factor + speed_factor
    )

    return round(
        attack_weight
        + other_stat_weight
        + 15 * len(item.status_immunities)
        + 15 * len(item.elemental_immunities)
        + 7.5 * len(item.elemental_resistances)
        + 50 * (1 if item.prevent_ko else 0)
        + 30 * len(item.temp_buffs)
        + 10 * item.arbitrary_value
    )


def _randomize_equip_properties(item: Armor | Weapon | Accessory) -> None:
    assert item.world is not None
    world = item.world
    settings = world.settings

    safety_checks = not settings.is_boolean_flag_enabled(EquipmentNoSafety)
    enemy_safety_checks = not settings.is_boolean_flag_enabled(EnemyNoSafetyChecks)

    if settings.is_flag_value(EquipmentProperties, EquipmentPropertiesOptions.RANDOM):
        # Randomize number of attributes to go up or down.
        # Guarantee >= 1 attribute goes up, but none go down.
        # For each set, 1/3 chance all non-zero ones go up/down.
        # Otherwise, weighted random number of stats.

        # ...attributes going up
        directions = [0, 0, 0, 0, 0]
        values = [0, 0, 0, 0, 0]
        if randint(1, 3) == 1:
            directions = [
                int(item.attack > 0),
                int(item.defense > 0),
                int(item.magic_attack > 0),
                int(item.magic_defense > 0),
                int(item.speed > 0),
            ]
        if len([d for d in directions if d != 0]) == 0:
            num_up = choices([1, 2, 3, 4, 5], weights=[5, 10, 10, 5, 1])[0]
            ups = sample([0, 1, 2, 3, 4], k=num_up)
            for index in ups:
                directions[index] = 1

        # ...attributes going down
        if randint(1, 3) == 1:
            directions = [
                directions[0] or -1 * int(item.attack >= 128),
                directions[1] or -1 * int(item.defense >= 128),
                directions[2] or -1 * int(item.magic_attack >= 128),
                directions[3] or -1 * int(item.magic_defense >= 128),
                directions[4] or -1 * int(item.speed >= 128),
            ]
        else:
            num_down = choices([0, 1, 2, 3, 4, 5], weights=[1, 5, 10, 10, 5, 1])[0]
            # Give priority to going up if a stat was picked to go up.
            valid_indices = [ind for ind, x in enumerate(directions) if x == 0]
            downs = sample(valid_indices, k=min(num_down, len(valid_indices)))
            for index in downs:
                directions[index] = -1

        up_indices = [ind for ind, x in enumerate(directions) if x > 0]
        down_indices = [ind for ind, x in enumerate(directions) if x < 0]

        # Track increases and decreases for each stat.
        score = item.stat_point_value
        # For attributes going down, randomize a number of points to decrease
        # based on the total item score.
        # Distribution is weighted towards the lower half of the range.
        if len(down_indices):
            upper_bound = 100
            if score != 0:
                upper_bound = score
            down_points = randint(0, randint(0, randint(0, upper_bound)))

            # Spread number of "down points" randomly across stats being decreased.
            # Add this number of points to
            # the "score" of the item so we add stat increases to compensate.
            score += down_points
            for _ in range(down_points):
                index = choice(down_indices)
                values[index] += 1

        # Spread number of "up points" randomly across stats being increased.
        # Treat non-primary stat increase as
        # two points to match the item score calculation.
        while score > 0:
            index = choice(up_indices)
            values[index] += 1
            if EQUIP_STATS[index] in item.primary_stats:
                score -= 1
            else:
                score -= 2

        # Perform standard mutation on new non-zero stats.
        for index in up_indices:
            values[index] = mutate_normal(values[index], minimum=1, maximum=127)
        for index in down_indices:
            values[index] = mutate_normal(values[index], minimum=1, maximum=127)

        for fxn, direction, value in zip(
            [
                item.set_attack,
                item.set_defense,
                item.set_magic_attack,
                item.set_magic_defense,
                item.set_speed,
            ],
            directions,
            values):
            if direction != 0:
                fxn(value * direction)

        # If this is a weapon with a variance value, shuffle that too.
        if isinstance(item, Weapon) and item.variance:
            item.set_variance(mutate_normal(item.variance, minimum=1, maximum=127))

        # Now, choose buffs and such
        # items that are normally bad in vanilla should be less likely to get good stuff
        odds = 0
        if item.tier == 4:
            odds = 1 / 2
        elif item.tier == 3:
            odds = 1 / 4
        elif item.tier == 2:
            odds = 1 / 8
        elif item.tier == 1:
            odds = 3 / 32
        odds /= 2

        if odds > 0:
            # Instant KO protection.
            ko_odds_factor: float = 1.0
            if isinstance(item, Weapon):
                ko_odds_factor /= 2
            if item.effect_type == EffectType.FEW_EFFECTS:
                ko_odds_factor /= 3
            if item.effect_type in [
                EffectType.BUFFS,
                EffectType.ELEMENTAL_IMMUNITY,
            ]:
                ko_odds_factor *= 1.5
            item.set_prevent_ko(coin_flip(odds * ko_odds_factor))

            # Elemental immunities.
            immunities = []
            resistances = []
            elemental_multiplier: float = 2.0

            element_pool = [Element.FIRE, Element.ICE, Element.THUNDER]

            if item.effect_type in [
                EffectType.NORMAL,
                EffectType.BUFFS,
                EffectType.STATUS_PROTECTION,
            ]:
                elemental_multiplier = 0.5
                if item.effect_type == EffectType.NORMAL:
                    elemental_multiplier = 1
                if randint(1, 2) == 1:
                    for immunity in element_pool:
                        if coin_flip(odds * elemental_multiplier):
                            immunities.append(immunity)
                        elif coin_flip(odds * elemental_multiplier):
                            resistances.append(immunity)
                else:
                    for immunity in element_pool:
                        if coin_flip(odds * elemental_multiplier):
                            resistances.append(immunity)
                        elif coin_flip(odds * elemental_multiplier):
                            immunities.append(immunity)
            elif item.effect_type in [
                EffectType.FEW_EFFECTS,
                EffectType.ELEMENTAL_RESISTANCE,
            ]:
                elemental_multiplier = 0.5
                elemental_sub_multiplier = 0.5
                if item.effect_type == EffectType.ELEMENTAL_RESISTANCE:
                    elemental_multiplier = 1.5
                    elemental_sub_multiplier = 1.0
                for immunity in element_pool:
                    if coin_flip(odds * elemental_multiplier):
                        resistances.append(immunity)
                    elif coin_flip(odds * elemental_sub_multiplier):
                        immunities.append(immunity)
            else:
                for immunity in element_pool:
                    if coin_flip(odds * elemental_multiplier):
                        immunities.append(immunity)
                    elif coin_flip(odds * elemental_multiplier):
                        resistances.append(immunity)

            # Status immunities.

            status_pool = [
                Status.MUTE,
                Status.SLEEP,
                Status.FEAR,
                Status.POISON,
                Status.MUSHROOM,
                Status.SCARECROW,
            ]
            # Berserk doesn't exist if safety checks are enabled, so exclude it to avoid
            # confusing the player in that case.
            if not enemy_safety_checks:
                status_pool.append(Status.BERSERK)

            # For certain namesake items, keep their status immunities
            # so people don't get confused, for safety.
            guaranteed_immunities = []
            if safety_checks and isinstance(
                item,
                (
                    FearlessPin,
                    AntidotePin,
                    TrueformPin,
                    WakeUpPin)):
                guaranteed_immunities = item.status_immunities

            status_immunities = []
            status_multiplier = 1

            if item.effect_type == EffectType.STATUS_PROTECTION:
                status_multiplier = 2
            elif item.effect_type in [
                EffectType.BUFFS,
                EffectType.FEW_EFFECTS,
            ]:
                status_multiplier = 0.5

            for status in status_pool:
                if coin_flip(odds * status_multiplier):
                    status_immunities.append(status)

            status_immunities.extend(guaranteed_immunities)
            status_immunities = list(set(status_immunities))

            item.set_status_immunities(status_immunities)

            # Temp buffs

            temp_buffs = []

            buff_pool = [
                TempStatBuff.ATTACK,
                TempStatBuff.DEFENSE,
                TempStatBuff.MAGIC_ATTACK,
                TempStatBuff.MAGIC_DEFENSE,
            ]

            buff_odds = 1.0
            if isinstance(item, (Weapon, ZoomShoes, SafetyRing, TroopaPin)):
                buff_odds = 1 / 2
            elif isinstance(
                item, (Armor, Amulet, AttackScarf, RareScarf, JinxBelt, Feather)
            ):
                buff_odds = 1 / 5
            if item.effect_type == EffectType.BUFFS:
                buff_odds *= 2.5
            elif item.effect_type != EffectType.NORMAL:
                buff_odds *= 0.25

            for buff in buff_pool:
                if coin_flip(odds * buff_odds):
                    temp_buffs.append(buff)

            item.set_temp_buffs(temp_buffs)

    elif settings.is_flag_value(EquipmentProperties, EquipmentPropertiesOptions.SOME):
        if isinstance(item, (Shirt, Pants)):
            item.append_status_immunity(Status.MUSHROOM)
        elif isinstance(item, (ThickShirt, ThickPants)):
            item.append_temp_buff(TempStatBuff.MAGIC_ATTACK)
        elif isinstance(item, (MegaShirt, MegaPants, MegaCape)):
            item.append_temp_buff(TempStatBuff.MAGIC_DEFENSE)
        elif isinstance(
            item, (HappyShirt, HappyPants, HappyCape, HappyShell, PolkaDress)
        ):
            item.set_prevent_ko(True)
        elif isinstance(item, CourageShell):
            item.append_status_immunity(Status.FEAR)
        elif isinstance(item, (SailorShirt, SailorPants, SailorCape, NauticaDress)):
            item.append_elemental_immunity(Element.ICE)
        elif isinstance(item, (FuzzyShirt, FuzzyPants, FuzzyCape, FuzzyDress)):
            item.append_elemental_immunity(Element.THUNDER)
        elif isinstance(item, (FireShell, FirePants, FireCape, FireShirt, FireDress)):
            item.append_elemental_immunity(Element.FIRE)
        elif isinstance(item, HeroShirt):
            item.append_status_immunity(Status.SCARECROW)
        elif isinstance(item, PrincePants):
            item.append_status_immunity(Status.MUTE)
        elif isinstance(item, RoyalDress):
            item.append_status_immunity(Status.SLEEP)
        elif isinstance(item, HealShell):
            item.append_status_immunity(Status.POISON)
        elif isinstance(item, StarCape):
            if not enemy_safety_checks:
                item.append_status_immunity(Status.BERSERK)
            else:
                item.append_status_immunity(Status.SCARECROW)
        elif isinstance(
            item, (FroggieStick, Cymbals, RibbitStick, SonicCymbal, WarFan, Parasol)
        ):
            mag = item.magic_attack
            atk = item.attack
            item.set_magic_attack(atk)
            item.set_attack(mag)

    character_pool = [MARIO, MALLOW, GENO, BOWSER, TOADSTOOL]

    if settings.is_flag_value(
        EquipmentCharacters, EquipmentCharactersOptions.EQUIP_ALL
    ) or (
        isinstance(item, Accessory)
        and (
            settings.is_flag_value(
                EquipmentCharacters,
                EquipmentCharactersOptions.VANILLA_ACCESSORIES_ALL)
            or settings.is_flag_value(
                EquipmentCharacters,
                EquipmentCharactersOptions.RANDOM_ACCESSORIES_ALL)
        )
    ):
        item.set_equip_chars(character_pool)
    elif not settings.is_flag_value(
        EquipmentCharacters, EquipmentCharactersOptions.VANILLA
    ):
        item.set_equip_chars(choices(character_pool, k=randint(1, len(character_pool))))


class _ShufflerDictKeys(StrEnum):
    WEAPON_STATS = "weapon_stats"
    WEAPON_TIERS = "weapon_tiers"
    ARMOR_TIERS = "armor_tiers"
    MEGA_ARMOR = "mega_armor"
    HAPPY_ARMOR = "happy_armor"
    SAILOR_ARMOR = "sailor_armor"
    FUZZY_ARMOR = "fuzzy_armor"
    FIRE_ARMOR = "fire_armor"
    ENDGAME_ARMOR = "endgame_armor"
    PINS_COSTS = "pins_costs"
    MID_ACCESSORY_COSTS = "mid_accessory_costs"
    HIGH_ACCESSORY_COSTS = "high_accessory_costs"


def _preshuffle_all_items(world: GameWorld):
    if not world.settings.is_flag_value(
        EquipmentProperties, EquipmentPropertiesOptions.RANDOM
    ):
        return
    destinations = {
        _ShufflerDictKeys.WEAPON_STATS: [],
        _ShufflerDictKeys.WEAPON_TIERS: [],
        _ShufflerDictKeys.ARMOR_TIERS: [],
        _ShufflerDictKeys.MEGA_ARMOR: [],
        _ShufflerDictKeys.HAPPY_ARMOR: [],
        _ShufflerDictKeys.SAILOR_ARMOR: [],
        _ShufflerDictKeys.FUZZY_ARMOR: [],
        _ShufflerDictKeys.FIRE_ARMOR: [],
        _ShufflerDictKeys.ENDGAME_ARMOR: [],
        _ShufflerDictKeys.PINS_COSTS: [],
        _ShufflerDictKeys.MID_ACCESSORY_COSTS: [],
        _ShufflerDictKeys.HIGH_ACCESSORY_COSTS: [],
    }

    for item in world.items:
        if not isinstance(item, Equipment):
            continue

        if randint(1, 10) == 1:
            item.set_effect_type(
                choice(
                    [
                        EffectType.NORMAL,
                        EffectType.BUFFS,
                        EffectType.STATUS_PROTECTION,
                        EffectType.ELEMENTAL_RESISTANCE,
                        EffectType.ELEMENTAL_IMMUNITY,
                        EffectType.FEW_EFFECTS,
                    ]
                )
            )

        if isinstance(item, Weapon):
            weapon_stat_tuple = (item.attack, item.price)
            destinations[_ShufflerDictKeys.WEAPON_STATS].append(weapon_stat_tuple)
            destinations[_ShufflerDictKeys.WEAPON_TIERS].append(item.tier)
        elif isinstance(item, Armor):
            destinations[_ShufflerDictKeys.ARMOR_TIERS].append(item.tier)
            armor_stat_tuple = (item.defense, item.magic_defense)
            dest = ""
            if isinstance(item, (MegaShirt, MegaPants, MegaCape)):
                dest = _ShufflerDictKeys.MEGA_ARMOR
            elif isinstance(
                item, (HappyShirt, HappyPants, HappyCape, HappyShell, PolkaDress)
            ):
                dest = _ShufflerDictKeys.HAPPY_ARMOR
            elif isinstance(
                item,
                (SailorShirt, SailorPants, SailorCape, CourageShell, NauticaDress)):
                dest = _ShufflerDictKeys.SAILOR_ARMOR
            elif isinstance(item, (FuzzyShirt, FuzzyPants, FuzzyCape, FuzzyDress)):
                dest = _ShufflerDictKeys.FUZZY_ARMOR
            elif isinstance(
                item, (FireShirt, FirePants, FireCape, FireShell, FireDress)
            ):
                dest = _ShufflerDictKeys.FIRE_ARMOR
            elif isinstance(
                item, (HeroShirt, PrincePants, StarCape, HealShell, RoyalDress)
            ):
                dest = _ShufflerDictKeys.ENDGAME_ARMOR
            if dest != "":
                destinations[dest].append(armor_stat_tuple)
        elif isinstance(item, (AntidotePin, WakeUpPin, FearlessPin, TrueformPin)):
            destinations[_ShufflerDictKeys.PINS_COSTS].append(item.price)
        elif isinstance(
            item,
            (
                ZoomShoes,
                SafetyBadge,
                JumpShoes,
                Amulet,
                RareScarf,
                BtubRing,
                Feather,
                SignalRing)):
            destinations[_ShufflerDictKeys.MID_ACCESSORY_COSTS].append(item.price)
        elif isinstance(
            item, (SafetyRing, AttackScarf, GhostMedal, JinxBelt, TroopaPin)
        ):
            destinations[_ShufflerDictKeys.HIGH_ACCESSORY_COSTS].append(item.price)
        elif isinstance(item, (ScroogeRing, ExpBooster, CoinTrick)):
            destinations[_ShufflerDictKeys.HIGH_ACCESSORY_COSTS].append(
                round(item.price * 62.5)
            )

    for destination in destinations.values():
        shuffle(destination)
    mega_count = 0
    happy_count = 0
    sailor_count = 0
    fuzzy_count = 0
    fire_count = 0
    endgame_count = 0

    for item in world.items:
        if not isinstance(item, Equipment):
            continue

        if isinstance(item, Weapon):
            temp_stats = destinations[_ShufflerDictKeys.WEAPON_STATS][item.item_id - 5]
            item.set_attack(int(temp_stats[0]))
            item.set_price(int(temp_stats[1]))
            item.set_tier(int(destinations[_ShufflerDictKeys.WEAPON_TIERS].pop()))
        elif isinstance(item, Armor):
            item.set_tier(int(destinations[_ShufflerDictKeys.ARMOR_TIERS].pop()))
            stat = None
            if isinstance(item, (MegaShirt, MegaPants, MegaCape)):
                stat = destinations[_ShufflerDictKeys.MEGA_ARMOR][mega_count]
                mega_count += 1
            elif isinstance(
                item, (HappyShirt, HappyPants, HappyCape, HappyShell, PolkaDress)
            ):
                stat = destinations[_ShufflerDictKeys.HAPPY_ARMOR][happy_count]
                happy_count += 1
            elif isinstance(
                item,
                (SailorShirt, SailorPants, SailorCape, CourageShell, NauticaDress)):
                stat = destinations[_ShufflerDictKeys.SAILOR_ARMOR][sailor_count]
                sailor_count += 1
            elif isinstance(item, (FuzzyShirt, FuzzyPants, FuzzyCape, FuzzyDress)):
                stat = destinations[_ShufflerDictKeys.FUZZY_ARMOR][fuzzy_count]
                fuzzy_count += 1
            elif isinstance(
                item, (FireShirt, FirePants, FireCape, FireShell, FireDress)
            ):
                stat = destinations[_ShufflerDictKeys.FIRE_ARMOR][fire_count]
                fire_count += 1
            elif isinstance(
                item, (HeroShirt, PrincePants, StarCape, HealShell, RoyalDress)
            ):
                stat = destinations[_ShufflerDictKeys.ENDGAME_ARMOR][endgame_count]
                endgame_count += 1
            if stat is not None:
                item.set_defense(int(stat[0]))
                item.set_magic_defense(int(stat[1]))
        elif isinstance(item, (AntidotePin, WakeUpPin, FearlessPin, TrueformPin)):
            item.set_price(int(destinations[_ShufflerDictKeys.PINS_COSTS].pop()))
        elif isinstance(
            item,
            (
                ZoomShoes,
                SafetyBadge,
                JumpShoes,
                Amulet,
                RareScarf,
                BtubRing,
                Feather,
                SignalRing)):
            item.set_price(
                int(destinations[_ShufflerDictKeys.MID_ACCESSORY_COSTS].pop())
            )
        elif isinstance(
            item, (SafetyRing, AttackScarf, GhostMedal, JinxBelt, TroopaPin)
        ):
            item.set_price(
                int(destinations[_ShufflerDictKeys.HIGH_ACCESSORY_COSTS].pop())
            )
        elif isinstance(item, (ScroogeRing, ExpBooster, CoinTrick)):
            item.set_price(
                round(destinations[_ShufflerDictKeys.MID_ACCESSORY_COSTS].pop() / 62.5)
            )


def randomize_all_items(world: GameWorld):
    """Randomize items."""

    # Base Shuffle for equipment to set up for further shuffling
    _preshuffle_all_items(world)

    # Designate 1-4 magic weapons
    magic_weapon_count: int = randint(1, 4)
    magic_weapon_candidates: list[Weapon] = []
    for item in [i for i in world.items if isinstance(i, Weapon)]:
        magic_weapon_candidates.append(item)
    for item in sample(magic_weapon_candidates, magic_weapon_count):
        item.set_magic_attack(item.attack)
        item.set_attack(0)

    # Safety check that at least four equips have instant death protection for safety.
    if not world.settings.is_boolean_flag_enabled(EquipmentNoSafety):
        instant_ko_item_count = len([i for i in world.items if i.prevent_ko])
        if instant_ko_item_count < 4:
            top_armor = [
                i
                for i in world.items
                if isinstance(i, (Armor, Accessory))
                and i.tier == 1
                and not i.prevent_ko
            ]
            for item in sample(top_armor, 4 - instant_ko_item_count):
                item.set_prevent_ko(True)

    equipment = [i for i in world.items if isinstance(i, (Weapon, Armor, Accessory))]

    # Shuffle equipment stats and equipment characters.
    for item in equipment:
        _randomize_equip_properties(item)

    # Score each item depending on how "good" it is.
    for item in equipment:
        if isinstance(item, (BtubRing)):
            item.set_rank_value(_calculate_rank_value(item))

    # Calculate list position (used as a factor in pricing)
    ranked_equipment = copy(equipment)
    ranked_equipment.sort(key=lambda x: x.rank_value, reverse=True)
    ranked_equipment_reverse = sorted(ranked_equipment, key=lambda x: x.rank_value)

    for item in equipment:
        item.set_rank_order(
            ranked_equipment.index(item) + 1 if item in ranked_equipment else 0
        )
        item.set_rank_order_reverse(
            ranked_equipment_reverse.index(item) + 1
            if item in ranked_equipment_reverse
            else 0
        )
        if item.rank_order <= 15:
            item.set_tier(4)
        elif item.rank_order <= 35:
            item.set_tier(3)
        elif item.rank_order <= 55:
            item.set_tier(2)
        else:
            item.set_tier(1)

    # Set the status effect of the fake mushroom.
    if world.settings.is_boolean_flag_enabled(PoisonMushroom):
        enemy_safety_checks = not world.settings.is_boolean_flag_enabled(
            EnemyNoSafetyChecks
        )
        status_pool = [
            Status.MUTE,
            Status.SLEEP,
            Status.FEAR,
            Status.POISON,
            Status.MUSHROOM,
            Status.SCARECROW,
        ]
        if not enemy_safety_checks:
            status_pool.append(Status.BERSERK)

        mushroom = next(i for i in world.items if isinstance(i, Mushroom2))
        mushroom.set_status_immunities([choice(status_pool)])

    # Modify certain events to guarantee better tip items.
    world.event_scripts.get_script_by_id(E0021_FOREST_MAZE_MUSHROOM_GRANT).set_contents(
        random_mushroom.contents
    )
    world.event_scripts.get_script_by_id(
        E2670_TOWER_KNIFE_GUY_CONSOLATION_PRIZE
    ).set_contents([JmpToEvent(E0057_GRANT_ANY_CONSUMABLE_CUSTOM_CAP)])
    world.event_scripts.get_script_by_id(
        E2649_CASINO_GRATE_GUY_RANDOM_PRIZE_GRANTER
    ).set_contents([JmpToEvent(E0057_GRANT_ANY_CONSUMABLE_CUSTOM_CAP)])
    world.event_scripts.get_script_by_id(
        E0622_MARRYMORE_INN_ELDERLY_GUEST_TIP_SUBROUTINE_1
    ).set_contents([JmpToEvent(E0051_GRANT_ANY_CONSUMABLE_EXCLUDE_WORST_CUSTOM_CAP)])
    world.event_scripts.get_script_by_id(
        E0626_MARRYMORE_INN_ELDERLY_GUEST_TIP_SUBROUTINE_FLOWERBOX
    ).set_contents([JmpToEvent(E0051_GRANT_ANY_CONSUMABLE_EXCLUDE_WORST_CUSTOM_CAP)])
    world.event_scripts.get_script_by_id(E1973_CLONE_RESERVED).set_contents(
        [JmpToEvent(E0042_GRANT_ANY_CONSUMABLE_TIER_2_CAP)]
    )
