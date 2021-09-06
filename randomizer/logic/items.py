# Item/shop randomization logic

import random
import math
import copy

from inspect import isclass

from randomizer.data import items
from randomizer.data.characters import Mario, Mallow, Geno, Bowser, Peach
from randomizer.data.helpers import EquipmentPropertiesOptions, EquipmentCharactersOptions
from . import flags, utils


def _randomize_item(item, safetychecks_on = True):
    """Perform randomization for an item.  Non-equipment will not be shuffled (price is done in the shop logic).

    Args:
        item(randomizer.data.items.Item):
    """
    if not item.is_equipment:
        return

    if item.world.settings.is_flag_value(flags.EquipmentProperties, EquipmentPropertiesOptions.random):
        # Randomize number of attributes to go up or down. Guarantee >= 1 attribute goes up, but none go down.
        # For each set, 1/3 chance all non-zero ones go up/down.  Otherwise, weighted random number of stats.
        # ...attributes going up
        ups = []
        if random.randint(1, 3) == 1:
            ups = [attr for attr in item.EQUIP_STATS if getattr(
                item, attr) > 0]

        if not ups:
            num_up = random.choices(
                [1, 2, 3, 4, 5], weights=[5, 10, 10, 5, 1])[0]
            while True:
                ups = random.sample(item.EQUIP_STATS, num_up)
                if set(ups) & set(item.primary_stats):
                    break

        # ...attributes going down
        if random.randint(1, 3) == 1:
            downs = [attr for attr in item.EQUIP_STATS if getattr(
                item, attr) >= 128]
        else:
            num_down = random.choices([0, 1, 2, 3, 4, 5], weights=[
                                      1, 5, 10, 10, 5, 1])[0]
            downs = random.sample(item.EQUIP_STATS, num_down)

        # Give priority to going up if a stat was picked to go up.
        downs = [d for d in downs if d not in ups]

        # Track increases and decreases for each stat.
        score = item.stat_point_value
        up_vals = dict([(u, 0) for u in ups])
        down_vals = dict([(d, 0) for d in downs])

        # For attributes going down, randomize a number of points to decrease based on the total item score.
        # Distribution is weighted towards the lower half of the range.
        if downs:
            if score != 0:
                down_points = random.randint(0, random.randint(0, score))
            else:
                down_points = random.randint(
                    0, random.randint(0, random.randint(0, 100)))

            # Spread number of "down points" randomly across stats being decreased.  Add this number of points to
            # the "score" of the item so we add stat increases to compensate.
            score += down_points
            for _ in range(down_points):
                attr = random.choice(downs)
                down_vals[attr] += 1

        # Spread number of "up points" randomly across stats being increased.  Treat non-primary stat increase as
        # two points to match the item score calculation.
        while score > 0:
            attr = random.choice(ups)
            up_vals[attr] += 1
            if attr in item.primary_stats:
                score -= 1
            else:
                score -= 2

        # Zero all stats.
        for attr in item.EQUIP_STATS:
            setattr(item, attr, 0)

        # Perform standard mutation on new non-zero stats.
        for attr in up_vals:
            setattr(item, attr, utils.mutate_normal(
                up_vals[attr], minimum=1, maximum=127))

        for attr in down_vals:
            value = utils.mutate_normal(
                down_vals[attr], minimum=1, maximum=127)
            setattr(item, attr, -value)

        # If this is a weapon with a variance value, shuffle that too.
        if item.variance:
            item.variance = utils.mutate_normal(
                item.variance, minimum=1, maximum=127)

        if item.tier == 1:
            odds = 2 / 3
        elif item.tier == 2:
            odds = 1 / 2
        elif item.tier == 3:
            odds = 1 / 4
        elif item.tier == 4:
            odds = 1 / 8
        elif item.tier == 5:
            odds = 3 / 32
        else:
            odds = 0

        # 7.1.3 update: trying lower odds for special properties and buffs, they're too frequent...
        odds /= 2

        if odds > 0:
            # Instant KO protection.
            KO_odds_factor = 1
            if item.is_weapon:
                KO_odds_factor /= 2
            if item.effect_type == items.EffectType.FewEffects:
                KO_odds_factor /= 3
            if item.effect_type in [items.EffectType.Buffs, items.EffectType.ElementalImmunity]:
                KO_odds_factor *= 1.5
            item.prevent_ko = utils.coin_flip(odds * KO_odds_factor)

            # Elemental immunities.
            item.elemental_immunities = []
            item.elemental_resistances = []
            if item.effect_type in [items.EffectType.Normal, items.EffectType.Buffs, items.EffectType.StatusProtection]:
                elemental_multiplier = 0.5
                if item.effect_type == items.EffectType.Normal:
                    elemental_multiplier = 1
                if random.randint(1, 2) == 1:
                    for i in range(4, 7):
                        if utils.coin_flip(odds * elemental_multiplier):
                            item.elemental_immunities.append(i)
                        elif utils.coin_flip(odds * elemental_multiplier):
                            item.elemental_resistances.append(i)
                else:
                    for i in range(4, 7):
                        if utils.coin_flip(odds * elemental_multiplier):
                            item.elemental_resistances.append(i)
                        elif utils.coin_flip(odds * elemental_multiplier):
                            item.elemental_immunities.append(i)
            elif item.effect_type in [items.EffectType.FewEffects, items.EffectType.ElementalResistance]:
                elemental_multiplier1 = 0.5
                elemental_multiplier2 = 0.5
                if item.effect_type == items.EffectType.ElementalResistance:
                    elemental_multiplier1 = 2.5
                    elemental_multiplier2 = 1
                for i in range(4, 7):
                    if utils.coin_flip(odds * elemental_multiplier1):
                        item.elemental_resistances.append(i)
                    elif utils.coin_flip(odds * elemental_multiplier2):
                        item.elemental_immunities.append(i)
            else:
                for i in range(4, 7):
                    if utils.coin_flip(odds * 2):
                        item.elemental_immunities.append(i)
                    elif utils.coin_flip(odds * 2):
                        item.elemental_resistances.append(i)

            # For certain namesake items, keep their status immunities so people don't get confused for safety.
            guaranteed_immunities = []
            if (safetychecks_on and isinstance(item, (items.FearlessPin, items.AntidotePin, items.TrueformPin, items.WakeUpPin))):
                guaranteed_immunities = item.status_immunities

            # Status immunities.
            item.status_immunities = []
            status_multiplier = 1
            if item.effect_type == items.EffectType.StatusProtection:
                status_multiplier = 2
            elif item.effect_type in [items.EffectType.Buffs, items.EffectType.FewEffects]:
                status_multiplier = 0.5
            for i in range(0, 7):
                # Skip berserk status if the safety checks on enemy shuffle is not enabled.
                if i == 4 and not item.world.settings.is_flag_enabled(flags.EnemyNoSafetyChecks):
                    continue

                if utils.coin_flip(odds * status_multiplier):
                    item.status_immunities.append(i)

            # Add guaranteed immunities back.
            for i in guaranteed_immunities:
                if i not in item.status_immunities:
                    item.status_immunities.append(i)

            # Weight weapons more toward buffs than armors. Accessories weight based on their stat totals.
            buff_odds = 1
            if item.is_weapon or item.index in [74, 77, 92]:
                buff_odds = 1 / 2
            elif item.is_armor or item.index in [78, 81, 82, 90, 91]:
                buff_odds = 1 / 5
            if item.effect_type == items.EffectType.Buffs:
                buff_odds *= 2.5
            elif item.effect_type == items.EffectType.Normal:
                pass
            else:
                buff_odds *= 0.25

            # Status buffs.
            item.status_buffs = []
            for i in range(3, 7):
                if utils.coin_flip(odds * buff_odds):
                    item.status_buffs.append(i)

    # "Some buffs added": add one buff to each "standard" armor, make some weapons buff magic
    elif item.world.settings.is_flag_value(flags.EquipmentProperties, EquipmentPropertiesOptions.some):
        immunities_to_add = copy.copy(item.elemental_immunities)
        buffs_to_add = copy.copy(item.status_buffs)
        resistances_to_add = copy.copy(item.elemental_resistances)
        statuses_to_add = copy.copy(item.status_immunities)
        if (isinstance(item, (items.Shirt, items.Pants))):
            statuses_to_add.append(5)
        elif (isinstance(item, (items.ThickShirt, items.ThickPants))):
            buffs_to_add.append(5)
        elif (isinstance(item, (items.MegaShirt, items.MegaPants, items.MegaCape))):
            buffs_to_add.append(6)
        elif (isinstance(item, (items.HappyShirt, items.HappyPants, items.HappyCape, items.HappyShell, items.PolkaDress))):
            item.prevent_ko = True
        elif (isinstance(item, (items.CourageShell))):
            statuses_to_add.append(3)
        elif (isinstance(item, (items.SailorShirt, items.SailorPants, items.SailorCape, items.NauticaDress))):
            immunities_to_add.append(4)
        elif (isinstance(item, (items.FuzzyShirt, items.FuzzyPants, items.FuzzyCape, items.FuzzyDress))):
            immunities_to_add.append(5)
        elif (isinstance(item, (items.FireShirt, items.FirePants, items.FireCape, items.FireShell, items.FireDress))):
            immunities_to_add.append(6)
        elif (isinstance(item, (items.HeroShirt))):
            statuses_to_add.append(6)
        elif (isinstance(item, (items.PrincePants))):
            statuses_to_add.append(0)
        elif (isinstance(item, (items.RoyalDress))):
            statuses_to_add.append(1)
        elif (isinstance(item, (items.HealShell))):
            statuses_to_add.append(2)
        elif (isinstance(item, (items.StarCape))):
            statuses_to_add.append(4)
        elif (isinstance(item, (items.FroggieStick, items.Cymbals, items.RibbitStick, items.SonicCymbal, items.WarFan, items.Parasol))):
            mag = item.magic_attack
            atk = item.attack
            item.attack = mag
            item.magic_attack = atk
        item.status_buffs = buffs_to_add
        item.elemental_immunities = immunities_to_add
        item.elemental_resistances = resistances_to_add
        item.status_immunities = statuses_to_add

    if not item.world.settings.is_flag_value(flags.EquipmentCharacters, EquipmentCharactersOptions.vanilla):
        # Randomize which characters can equip this item.
        # Old linear mode logic: Geno can only equip his own weapons, and nobody else can equip his due to softlocks!
        # This is fixed in open mode.
        if item.world.open_mode or (not item.is_weapon or Geno not in item.equip_chars):
            # Pick random number of characters with lower numbers weighted heavier.

            new_chars = set()

            if item.world.settings.is_flag_value(flags.EquipmentCharacters, EquipmentCharactersOptions.equip_all):
                item.equip_chars = list({Mario, Mallow, Geno, Bowser, Peach})
            elif item.world.settings.is_flag_value(flags.EquipmentCharacters, EquipmentCharactersOptions.random) or (item.world.settings.is_flag_value(flags.EquipmentCharacters, EquipmentCharactersOptions.r_accessories_all) and not item.is_accessory):
                num_equippable = random.randint(1, random.randint(1, 5))

                for _ in range(num_equippable):
                    char_choices = {Mario, Mallow,
                                    Geno, Bowser, Peach} - new_chars

                    # Linear mode: Geno can only equip his own weapons (we checked if this was one of his above).
                    if not item.world.open_mode and item.is_weapon and Geno in char_choices:
                        char_choices.remove(Geno)

                    if not char_choices:
                        break

                    # Now choose a random character to be equipable.
                    char_choices = sorted(char_choices, key=lambda c: c.index)
                    new_chars.add(random.choice(char_choices))

                item.equip_chars = list(new_chars)

            elif item.is_accessory and (item.world.settings.is_flag_value(flags.EquipmentCharacters, EquipmentCharactersOptions.v_accessories_all) or item.world.settings.is_flag_value(flags.EquipmentCharacters, EquipmentCharactersOptions.r_accessories_all)):
                item.equip_chars = list({Mario, Mallow, Geno, Bowser, Peach})


def randomize_all(world):
    """Randomize everything for items for a single seed.

    :type world: randomizer.logic.main.GameWorld
    """
    weapon_stats = []
    weapon_tiers = []
    armor_tiers = []
    mega_armor = []
    happy_armor = []
    sailor_armor = []
    fuzzy_armor = []
    fire_armor = []
    endgame_armor = []
    pins_costs = []
    mid_accessory_costs = []
    high_accessory_costs = []

    if world.settings.is_flag_value(flags.EquipmentProperties, EquipmentPropertiesOptions.random):

        # Base Shuffle for equipment to set up for further shuffling
        for item in world.items:
            if not item.is_equipment:
                continue
            if random.randint(1, 10) == 1:
                item.effect_type = random.choice(
                    [items.EffectType.Normal, items.EffectType.Buffs, items.EffectType.StatusProtection, items.EffectType.ElementalResistance, items.EffectType.ElementalImmunity, items.EffectType.FewEffects])
            if item.is_weapon:
                temp_weapon_stat = (item.attack, item.price)
                weapon_stats.append(temp_weapon_stat)
                weapon_tiers.append(item.tier)
            elif item.is_armor:
                armor_tiers.append(item.tier)
                if item.index in [41, 42, 44]:
                    temp_armor_stat = (item.defense, item.magic_defense)
                    mega_armor.append(temp_armor_stat)
                elif item.index in [45, 46, 47, 48, 49]:
                    temp_armor_stat = (item.defense, item.magic_defense)
                    happy_armor.append(temp_armor_stat)
                elif item.index in [50, 51, 52, 53, 54]:
                    temp_armor_stat = (item.defense, item.magic_defense)
                    sailor_armor.append(temp_armor_stat)
                elif item.index in [55, 56, 57, 58]:
                    temp_armor_stat = (item.defense, item.magic_defense)
                    fuzzy_armor.append(temp_armor_stat)
                elif item.index in [59, 60, 61, 62, 63]:
                    temp_armor_stat = (item.defense, item.magic_defense)
                    fire_armor.append(temp_armor_stat)
                elif item.index in [64, 65, 66, 67, 68]:
                    temp_armor_stat = (item.defense, item.magic_defense)
                    endgame_armor.append(temp_armor_stat)
            elif item.index in [84, 85, 86, 87]:
                pins_costs.append(item.price)
            # Zoom Shoes, Safety Badge, Jump Shoes, Amulet, Rare Scarf, B'Tub Ring, Feather, Signal Ring
            elif item.index in [74, 75, 76, 78, 82, 83, 91, 93]:
                mid_accessory_costs.append(item.price)
            # Safety Ring, Attack Scarf, Ghost Medal, Jinx Belt, Troopa Pin
            elif item.index in [77, 81, 89, 90, 92]:
                high_accessory_costs.append(item.price)
            # Scrooge Ring, EXP Booster, Coin Trick
            elif item.index in [79, 80, 88]:
                high_accessory_costs.append(round(item.price * 62.5))

        random.shuffle(weapon_stats)
        random.shuffle(weapon_tiers)
        random.shuffle(armor_tiers)
        random.shuffle(mega_armor)
        random.shuffle(happy_armor)
        random.shuffle(sailor_armor)
        random.shuffle(fuzzy_armor)
        random.shuffle(fire_armor)
        random.shuffle(endgame_armor)
        random.shuffle(pins_costs)
        random.shuffle(mid_accessory_costs)
        random.shuffle(high_accessory_costs)
        mega_count = 0
        happy_count = 0
        sailor_count = 0
        fuzzy_count = 0
        fire_count = 0
        endgame_count = 0

        for item in world.items:
            if not item.is_equipment:
                continue
            if item.is_weapon:
                temp_weapon_stats = weapon_stats[(item.index - 5)]
                item.attack = temp_weapon_stats[0]
                item.price = temp_weapon_stats[1]
                item.tier = weapon_tiers.pop()
            elif item.is_armor:
                item.tier = armor_tiers.pop()
                if item.index in [41, 42, 44]:
                    temp_armor_stat = mega_armor[mega_count]
                    item.defense = temp_armor_stat[0]
                    item.magic_defense = temp_armor_stat[1]
                    mega_count += 1
                elif item.index in [45, 46, 47, 48, 49]:
                    temp_armor_stat = happy_armor[happy_count]
                    item.defense = temp_armor_stat[0]
                    item.magic_defense = temp_armor_stat[1]
                    happy_count += 1
                elif item.index in [50, 51, 52, 53, 54]:
                    temp_armor_stat = sailor_armor[sailor_count]
                    item.defense = temp_armor_stat[0]
                    item.magic_defense = temp_armor_stat[1]
                    sailor_count += 1
                elif item.index in [55, 56, 57, 58]:
                    temp_armor_stat = fuzzy_armor[fuzzy_count]
                    item.defense = temp_armor_stat[0]
                    item.magic_defense = temp_armor_stat[1]
                    fuzzy_count += 1
                elif item.index in [59, 60, 61, 62, 63]:
                    temp_armor_stat = fire_armor[fire_count]
                    item.defense = temp_armor_stat[0]
                    item.magic_defense = temp_armor_stat[1]
                    fire_count += 1
                elif item.index in [64, 65, 66, 67, 68]:
                    temp_armor_stat = endgame_armor[endgame_count]
                    item.defense = temp_armor_stat[0]
                    item.magic_defense = temp_armor_stat[1]
                    endgame_count += 1
            elif item.index in [84, 85, 86, 87]:
                item.price = pins_costs.pop()
            # Zoom Shoes, Safety Badge, Jump Shoes, Amulet, Rare Scarf, B'Tub Ring, Feather, Signal Ring
            elif item.index in [74, 75, 76, 78, 82, 83, 91, 93]:
                item.price = mid_accessory_costs.pop()
            # Safety Ring, Attack Scarf, Ghost Medal, Jinx Belt, Troopa Pin
            elif item.index in [77, 81, 89, 90, 92]:
                item.price = high_accessory_costs.pop()
            # Scrooge Ring, EXP Booster, Coin Trick
            elif item.index in [79, 80, 88]:
                item.price = round(high_accessory_costs.pop() / 62.5)

        # Designate 1-4 magic weapons
        magic_weapon_count = random.randint(1, 4)
        magic_weapon_candidates = []
        for item in [i for i in world.items if item.is_weapon]:
            magic_weapon_candidates.append(item)
        for item in random.sample(magic_weapon_candidates, magic_weapon_count):
            item.magic_attack = item.attack
            item.attack = 0

        # Safety check that at least four equips have instant death protection for safety.
        if not item.world.settings.is_flag_enabled(flags.EquipmentNoSafety):
            instant_ko_items = len(
                [item for item in world.items if item.prevent_ko])
            if instant_ko_items < 4:
                top_armor = [item for item in world.items if (item.is_armor or item.is_accessory) and item.tier == 1 and
                            not item.prevent_ko]
                for item in random.sample(top_armor, 4 - instant_ko_items):
                    item.prevent_ko = True

    # Shuffle equipment stats and equip characters.
    for item in world.items:
        _randomize_item(item, world.settings.is_flag_enabled(flags.EquipmentNoSafety))

    for item in world.items:
        if item.is_equipment:
            if item.index in (83, 148, 93):
                item.arbitrary_value = 1
            elif item.index == 88:
                item.arbitrary_value = 2
            elif item.index in (76, 79):
                item.arbitrary_value = 1
            elif item.index == 80:
                item.arbitrary_value = 10
            item.rank_value = (
                item.attack * max(
                    0, min(
                        2, (item.attack + item.variance) / (1 if (item.attack - item.variance == 0) else (item.attack - item.variance))
                    )
                ) + max(
                    0, (item.magic_attack / (2 if item.magic_attack < 0 else 1)) + (item.magic_defense / (2 if item.magic_defense < 0 else 1)) + (item.defense / (2 if item.defense < 0 else 1)) + min(20, item.speed / 2)
                ) +
                15 * len(item.status_immunities) +
                15 * len(item.elemental_immunities) +
                7.5 * len(item.elemental_resistances) +
                50 * (1 if item.prevent_ko else 0) +
                30 * len(item.status_buffs) + 
                10 *
                item.arbitrary_value)

    # Calculate list position (used as a factor in pricing)
    ranks = [item for item in world.items if item.is_equipment]
    ranks.sort(key=lambda x: x.rank_value, reverse=True)
    ranks_reverse = sorted(ranks, key=lambda x: x.rank_value)

    for item in world.items:
        if item.is_equipment:
            item.rank_order = (ranks.index(item) + 1 if item in ranks else 0)
            item.rank_order_reverse = (ranks_reverse.index(
                item) + 1 if item in ranks_reverse else 0)
            if item.rank_order <= 15:
                item.tier = 1
            elif item.rank_order <= 35:
                item.tier = 2
            elif item.rank_order <= 55:
                item.tier = 3
            elif item.rank_order <= 75:
                item.tier = 4
            else:
                item.tier = 5

    # Useful debug function to print equipment property table.
    """
    for item in world.items:
        if item.is_equipment:
            print(item.name + " " * (19 - len(item.name)) + ": Sp:" + str(item.speed) + ", At:" + str(item.attack) + ", Df:" + str(item.defense) + ", MA:" + str(item.magic_attack) + ", MD:" + str(item.magic_defense) + "; "
                  + ("KO" if item.prevent_ko else "") + (", " if (item.prevent_ko and item.status_immunities != []) else "") + ("Psn" if (2 in item.status_immunities) else "") + ("Mute" if (0 in item.status_immunities) else "")
                  + ("Slp" if (1 in item.status_immunities) else "")  + ("SCrow" if (6 in item.status_immunities) else "") + ("Mush" if (5 in item.status_immunities) else "") + ("Fear" if (3 in item.status_immunities) else "")
                  + ("Bsrk" if (4 in item.status_immunities) else "") + ("; " if (item.prevent_ko or item.status_immunities != []) else "") + ("Imm: " if item.elemental_immunities != [] else "")
                  + ("Ic" if (4 in item.elemental_immunities) else "") + ("Fi" if (5 in item.elemental_immunities) else "") + ("Th" if (6 in item.elemental_immunities) else "") + ("Ju" if (7 in item.elemental_immunities) else "")
                  + ("; " if item.elemental_immunities != [] else "") + ("Res: " if item.elemental_resistances != [] else "") + ("Ic" if (4 in item.elemental_resistances) else "") + ("Fi" if (5 in item.elemental_resistances) else "")
                  + ("Th" if (6 in item.elemental_resistances) else "") + ("Ju" if (7 in item.elemental_resistances) else "")+ ("; " if item.elemental_resistances != [] else "") + ("Buffs: " if item.status_buffs != [] else "")
                  + ("At" if (3 in item.status_buffs) else "") + ("Df" if (4 in item.status_buffs) else "") + ("MA" if (5 in item.status_buffs) else "") + ("MD" if (6 in item.status_buffs) else ""))
    """

    if world.settings.is_flag_value(flags.PoisonMushroom, True):
        for item in world.items:
            if item.index == 175:
                item.status_immunities = [random.randint(0, 7)]


def get_spoiler(world):
    acc = {}
    
    for location in world.starter_character_checks + world.recruitable_character_checks + world.spotted_character_checks + world.boss_star_checks + world.chest_locations + world.freestanding_item_locations:
        if isinstance(location.item, items.Item):
            item_str = location.item.name
        elif isclass(location.item):
            item_str = location.item.__name__
        else:
            item_str = str(location.item)
        if utils.isclass_or_instance(location.item, items.Coins):
            item_str = 'Coins%i' % location.item.amount
        elif utils.isclass_or_instance(location.item, items.MultiFrogCoin):
            item_str = 'FrogCoins%i' % location.item.amount

        acc[location.name] = item_str

    return acc
