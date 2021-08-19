# Boss randomization logic for open mode.

import collections
import random
import statistics

from randomizer.data import bosses, enemies
from randomizer.data.formations import FormationMember
from . import flags, utils




def _boss_fight_filter(world, location):
    """

    Args:
        world (randomizer.logic.main.GameWorld):
        location (randomizer.data.bosses.BossLocation):

    Returns:
        bool: True is location is okay to be included, False otherwise.

    """
    if not utils.isclass_or_instance(location, bosses.BossLocation):
        return False

    bosses_to_ignore = world.settings.get_flag(flags.ShuffledBosses).disabled
    if location.description in bosses_to_ignore:
        return False

    return True


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def set_henchman_run_flags(world, boss, henchman):
    if henchman.pack_number is not None:
        henchman_pack = world.get_formation_pack_by_index(henchman.pack_number)
        for f in henchman_pack.formations:
            # dont run away
            if utils.isclass_or_instance(boss, bosses.MackBoss) or utils.isclass_or_instance(boss, bosses.BoosterBoss):
                world.get_enemy_formation_by_index(f.index).music_run_flags = 3
            # do run away
            else:
                world.get_enemy_formation_by_index(f.index).music_run_flags = 1

def randomize_all(world):
    """Randomize the boss locations.

    Args:
        world (randomizer.logic.main.GameWorld): Game world to randomize.

    """
    # Open mode-specific shuffles.
    if world.open_mode:
        # Shuffle boss encounters.
        if world.settings.is_flag_enabled(flags.BossShuffle):
            locations = [b for b in world.boss_locations if _boss_fight_filter(world, b)]
            shuffled_locations = locations[:]
            random.shuffle(shuffled_locations)
            #alpha testing: set the order manually
            # shuffle_count = 0
            # while shuffle_count < 5:
            #     position_iterator = 0
            #     while position_iterator < 1:
            #         for location in shuffled_locations:
            #             if position_iterator < 1:
            #                 shuffled_locations.append(shuffled_locations.pop(shuffled_locations.index(location)))
            #                 position_iterator += 1
            #     shuffle_count += 1

            # index_jinx = -1
            # index_jagger = -1
            # index_countdown = -1
            # index_exor = -1
            # for l in locations:
            #     if l.name == 'Jinx3':
            #         index_jinx = locations.index(l)
            #     if l.name == 'Jagger':
            #         index_jagger = locations.index(l)
            #
            # for l in shuffled_locations:
            #     if l.name == 'Countdown':
            #         index_countdown = shuffled_locations.index(l)
            #     if l.name == 'Booster':
            #         index_exor = shuffled_locations.index(l)
            # print(index_jinx, index_jagger, index_countdown, index_exor)
            #
            # swapPositions(shuffled_locations, index_jinx, index_exor)
            # swapPositions(shuffled_locations, index_jagger, index_countdown)

            shuffled_bosses = [b.boss for b in shuffled_locations]

            # Randomize boss music for locations if enabled.
            if world.settings.is_flag_enabled(flags.BossShuffleMusic):
                # noinspection PyTypeChecker
                music_choices = [m for m in world.music_pool if m.name not in world.settings.get_flag(flags.ShuffledMusic).disabled]
                for location in locations:
                    location.music = random.choice(music_choices)


            # Put Shelly in the right battle & give it the right arguments to use for new script
            for location, boss in zip(locations, shuffled_bosses):
                if utils.isclass_or_instance(location, bosses.Birdetta):
                    # Do not allow Shelly to join battles that need their own fixed backgrounds
                    if utils.isclass_or_instance(boss, bosses.BirdettaBoss) or utils.isclass_or_instance(boss, bosses.ExorBoss) or utils.isclass_or_instance(boss, bosses.CloakerDominoBoss) or utils.isclass_or_instance(boss, bosses.KingCalamariBoss) or utils.isclass_or_instance(boss, bosses.CountdownBoss) or utils.isclass_or_instance(boss, bosses.SmithyBoss) or utils.isclass_or_instance(boss, bosses.AxemRangersBoss):
                        pass
                    else:
                        # i hope this works. i dont understand when python passes objects by value or reference
                        # get list of enemy ID vals who should be summoned by shelly
                        summons = []
                        target_formation = world.get_enemy_formation_by_index(boss.pack_number)
                        for index, member in enumerate(target_formation.members):
                            if not member.hidden_at_start:
                                summons.append(0x28 + member.index)
                                target_formation.members[index].hidden_at_start = True
                        target_formation.members.append(FormationMember(len(target_formation.members), False, world.get_enemy_instance(enemies.Shelly), 171, 103))
                        # shelly will modify its summon script at the time of patch build
                        world.get_enemy_instance(enemies.Shelly).summons = summons
                        # if target formation has a loder event, move it into shelly's script instead
                        world.get_enemy_instance(enemies.Shelly).summon_event = target_formation.event_at_start
                        target_formation.event_at_start = None
                        # force shelly battle to have egg background
                        target_formation.required_battlefield = bosses.Battlefields.Birdo
                        # now, fix birdetta background, hide her instance of shelly, and have her be starting enemy
                        target_formation_birdetta = world.get_enemy_formation_by_index(297)
                        target_formation_birdetta.required_battlefield = None
                        target_formation_birdetta.members[0].hidden_at_start = False
                        target_formation_birdetta.members[1].hidden_at_start = True


            # Scale boss stats accordingly if keep stats not enabled.
            if world.settings.is_flag_value(flags.BossShuffleScaleStats, True):
                # First calculate total stats for each slot based on anchors and stats shuffled already.
                location_stats = []
                for location in locations:
                    pack = world.get_formation_pack_by_index(location.boss.pack_number)
                    formation = world.get_enemy_formation_by_index(pack.formations[0].index)
                    elist = formation.stat_total_enemies
                    # HP
                    # For Exor fight, only count Exor and average of Left + Right Eye mandatory HP.
                    if any(e for e in elist if utils.isclass_or_instance(e, enemies.Exor)):
                        hp = 0
                        eyes = 0
                        for e in elist:
                            if utils.isclass_or_instance(e, enemies.Exor):
                                hp += e.hp
                            elif utils.isclass_or_instance(e, (enemies.LeftEye, enemies.RightEye)):
                                eyes += e.hp
                        hp += int(eyes / 2)
                        xp = sum(e.xp for e in elist if utils.isclass_or_instance(e, enemies.Exor))
                        coins = sum(e.coins for e in elist if utils.isclass_or_instance(e, enemies.Exor))
                    # For Cloaker/Domino, count average HP of each phase of the fight.
                    elif any(e for e in elist if utils.isclass_or_instance(e, enemies.Cloaker)):
                        dudes = 0
                        sneks = 0
                        for e in elist:
                            if utils.isclass_or_instance(e, (enemies.Cloaker, enemies.Domino)):
                                dudes += e.hp
                            elif utils.isclass_or_instance(e, (enemies.Earthlink, enemies.MadAdder)):
                                sneks += e.hp
                        hp = int(round((dudes / 2) + (sneks / 2)))
                        xp = sum(e.xp for e in elist if utils.isclass_or_instance(e, (enemies.Cloaker, enemies.Domino)))
                        coins = sum(e.coins for e in elist if utils.isclass_or_instance(e, (enemies.Cloaker, enemies.Domino)))
                    # For Dodo/Valentina, count 40% of Dodo's HP.
                    elif any(e for e in elist if utils.isclass_or_instance(e, enemies.Valentina)):
                        dodo = 0
                        valentina = 0
                        for e in elist:
                            if utils.isclass_or_instance(e, enemies.Dodo):
                                dodo += e.hp * 0.4
                            elif utils.isclass_or_instance(e, enemies.Valentina):
                                valentina += e.hp
                        hp = int(round(dodo + valentina))
                        xp = sum(e.xp for e in elist)
                        coins = sum(e.coins for e in elist)
                    # For King Calimari, need special exp calc
                    elif any(e for e in elist if utils.isclass_or_instance(e, enemies.KingCalamari)):
                        hp = sum(e.hp for e in elist)
                        xp = sum(e.xp for e in elist if utils.isclass_or_instance(e, enemies.KingCalamari))
                        coins = sum(e.coins for e in elist if utils.isclass_or_instance(e, enemies.KingCalamari))
                    # For Megasmilax, need special exp calc
                    elif any(e for e in elist if utils.isclass_or_instance(e, enemies.Megasmilax)):
                        hp = sum(e.hp for e in elist)
                        xp = sum(e.xp for e in elist if utils.isclass_or_instance(e, enemies.Megasmilax))
                        coins = sum(e.coins for e in elist if utils.isclass_or_instance(e, enemies.Megasmilax))
                    # For Axems, need special exp calc
                    elif any(e for e in elist if utils.isclass_or_instance(e, enemies.AxemRangers)):
                        hp = sum(e.hp for e in elist)
                        xp = sum(e.xp for e in elist if utils.isclass_or_instance(e, enemies.AxemRangers))
                        coins = sum(e.coins for e in elist if utils.isclass_or_instance(e, enemies.AxemRangers))
                    # For Belome 2, need special exp calc
                    elif any(e for e in elist if utils.isclass_or_instance(e, enemies.Belome2)):
                        hp = sum(e.hp for e in elist)
                        xp = sum(e.xp for e in world.enemies if utils.isclass_or_instance(e, (enemies.Belome2, enemies.MarioClone)))
                        coins = sum(e.coins for e in world.enemies if
                                    utils.isclass_or_instance(e, (enemies.Belome2, enemies.MarioClone)))
                    # For Culex, need special exp calc
                    elif any(e for e in elist if utils.isclass_or_instance(e, enemies.Culex)):
                        hp = sum(e.hp for e in elist)
                        xp = sum(e.xp for e in world.enemies if
                                 utils.isclass_or_instance(e, (enemies.Culex, enemies.WindCrystal, enemies.WaterCrystal,
                                                enemies.FireCrystal, enemies.EarthCrystal)))
                        coins = sum(e.coins for e in world.enemies if
                                    utils.isclass_or_instance(e, (enemies.Culex, enemies.WindCrystal, enemies.WaterCrystal,
                                                   enemies.FireCrystal, enemies.EarthCrystal)))
                    # For Johnny, need special exp calc
                    elif any(e for e in elist if utils.isclass_or_instance(e, enemies.Johnny)):
                        hp = sum(e.hp for e in elist)
                        xp = 0
                        coins = 0
                        for e in world.enemies:
                            if utils.isclass_or_instance(e, enemies.Johnny):
                                xp += e.xp
                                coins += e.coins
                            elif utils.isclass_or_instance(e, enemies.BandanaBlue):
                                xp += 4 * e.xp
                                coins += 4 * e.coins
                    # Anything else, just sum all HP/xp/coins.
                    else:
                        hp = sum(e.hp for e in elist)
                        xp = sum(e.xp for e in elist)
                        coins = sum(e.coins for e in elist)

                    # For other stats, if there's an anchor then take that enemy's stats.  Otherwise average them.
                    anchor = formation.shuffle_anchor
                    if anchor:
                        attack = anchor.attack
                        defense = anchor.defense
                        magic_attack = anchor.magic_attack
                        magic_defense = anchor.magic_defense
                        evade = anchor.evade
                        magic_evade = anchor.magic_evade
                    else:
                        attack = int(round(statistics.mean(e.attack for e in elist)))
                        defense = int(round(statistics.mean(e.defense for e in elist)))
                        magic_attack = int(round(statistics.mean(e.magic_attack for e in elist)))
                        magic_defense = int(round(statistics.mean(e.magic_defense for e in elist)))
                        evade = int(round(statistics.mean(e.evade for e in elist)))
                        magic_evade = int(round(statistics.mean(e.magic_evade for e in elist)))

                    location_stats.append({
                        'hp': hp,
                        'attack': attack,
                        'defense': defense,
                        'magic_attack': magic_attack,
                        'magic_defense': magic_defense,
                        'evade': evade,
                        'magic_evade': magic_evade,
                        'xp': xp,
                        'coins': coins,
                    })

                # Now adjust stats for each shuffled pack given the total stats for the slot it's going into.
                for location, stats in zip(shuffled_locations, location_stats):
                    pack = world.get_formation_pack_by_index(location.boss.pack_number)
                    formation = world.get_enemy_formation_by_index(pack.formations[0].index)
                    for i, enemy in enumerate(formation.stat_scaling_enemies):
                        # Do not raise King Bomb's stats more than normal.
                        no_raise = utils.isclass_or_instance(enemy, enemies.KingBomb)
                        # dont raise def on jinx clone or bahamutt, gets ridiculous and or boring. attack tho, learn 2 block
                        no_raise_defense = utils.isclass_or_instance(enemy, enemies.BahamuttMagikoopa) or utils.isclass_or_instance(enemy, enemies.BahamuttChester) or utils.isclass_or_instance(enemy, enemies.JinxClone)


                        enemy.hp = min(int(round(stats['hp'] * enemy.ratio_hp)), enemy.hp if no_raise else 65535)
                        enemy.attack = min(int(round(stats['attack'] * enemy.ratio_attack)),
                                           enemy.attack if no_raise else 255)
                        enemy.defense = min(int(round(stats['defense'] * enemy.ratio_defense)),
                                            enemy.defense if no_raise or no_raise_defense else 255)
                        enemy.magic_attack = min(int(round(stats['magic_attack'] * enemy.ratio_magic_attack)),
                                                 enemy.magic_attack if no_raise else 255)
                        enemy.magic_defense = min(int(round(stats['magic_defense'] * enemy.ratio_magic_defense)),
                                                  enemy.magic_defense if no_raise or no_raise_defense else 255)
                        enemy.evade = min(int(round(stats['evade'] * enemy.ratio_evade)), 100)
                        enemy.magic_evade = min(int(round(stats['magic_evade'] * enemy.ratio_magic_evade)), 100)

                        # For snek fight, the XP/coins need to be put on Cloaker/Domino 2 because you fight either one.
                        if formation.index == 309:
                            if utils.isclass_or_instance(enemy, (enemies.Cloaker2, enemies.Domino2)):
                                enemy.xp = min(stats['xp'], 0xffff)
                                enemy.coins = min(stats['coins'], 255)
                            else:
                                enemy.xp = 0
                                enemy.coins = 0
                        # For Countdown fight, use the Ding-A-Lings because Countdown disables himself.
                        elif formation.index == 295:
                            if utils.isclass_or_instance(enemy, enemies.DingALing):
                                enemy.xp = min(int(round(stats['xp'] / 2)), 0xffff)
                                enemy.coins = min(int(round(stats['coins'] / 2)), 255)
                            else:
                                enemy.xp = 0
                                enemy.coins = 0
                        # Otherwise give the first enemy all the XP/coins, except for Hammer Bros that need half.
                        elif i == 0:
                            if utils.isclass_or_instance(enemy, enemies.HammerBro):
                                enemy.xp = min(int(round(stats['xp'] / 2)), 0xffff)
                                enemy.coins = min(int(round(stats['coins'] / 2)), 255)
                            else:
                                enemy.xp = min(stats['xp'], 0xffff)
                                enemy.coins = min(stats['coins'], 255)
                        else:
                            enemy.xp = 0
                            enemy.coins = 0

            # What to do about EXP?

            # Assign packs to their new locations and update music and can't run flags.
            for location, boss in zip(locations, shuffled_bosses):
                pack = world.get_formation_pack_by_index(boss.pack_number)
                formation = world.get_enemy_formation_by_index(pack.formations[0].index)
                formation.music = location.music
                formation.can_run_away = location.can_run_away
                location.boss = boss

                unique_henchmen = boss.unique_henchmen
                repeatable_henchmen = boss.repeatable_henchmen

                # prepare NPC locations to patch the correct models

                #set boss model to each room associated with this location
                for index, model in enumerate(location.boss_locations):
                    if world.settings.is_flag_value(flags.BossReplaceMinigameSprites, True) or not model.minigames_only:
                        location.boss_locations[index].occupant = boss

                # set priority henchmen to locations that can take them
                for index, henchman in enumerate(location.unique_henchmen):
                    for index2, model in enumerate(henchman):
                        if world.settings.is_flag_value(flags.BossReplaceMinigameSprites, True) or not model.minigames_only:
                            # if the boss has unique henchmen to donate, use it
                            requires_henchman_with_pack = location.unique_henchmen[index][index2].fill_type is not bosses.HenchmanType.NPCOnly
                            eligible_repeatable_henchmen = [r for r in repeatable_henchmen if ((requires_henchman_with_pack and r.pack_number is not None) or not requires_henchman_with_pack)]
                            
                            if index < len(unique_henchmen) and not (requires_henchman_with_pack and unique_henchmen[index].pack_number is None):
                                new_unique_henchman = unique_henchmen[index]
                                new_henchman = new_unique_henchman
                                world.get_formation_pack_by_index(new_henchman.pack_number)
                                location.unique_henchmen[index][index2].occupant = new_henchman
                                set_henchman_run_flags(world, boss, new_henchman)
                            # otherwise, repeatable henchmen can fill the npc slot if permitted
                            elif len(eligible_repeatable_henchmen) > 0:
                                new_henchman = random.choice(eligible_repeatable_henchmen)
                                if location.unique_henchmen[index][index2].repeatable_allowed:
                                    location.unique_henchmen[index][index2].occupant = new_henchman
                                    set_henchman_run_flags(world, boss, new_henchman)
                                elif location.unique_henchmen[index][index2].remove_if_empty:
                                    location.unique_henchmen[index][index2].occupant = None
                            # remove if no repeatables available & npc should be hidden if empty
                            elif location.unique_henchmen[index][index2].remove_if_empty:
                                location.unique_henchmen[index][index2].occupant = None

                # set npcs that require non-unique henchmen
                for index, henchman in enumerate(location.repeatable_henchmen):
                    for index2, model in enumerate(henchman):
                        if world.settings.is_flag_value(flags.BossReplaceMinigameSprites, True) or not model.minigames_only:
                            # ignore punchinello's microbombs unless the substituted boss is Hidon, Birdetta, or King Calamari
                            if (utils.isclass_or_instance(location, bosses.Punchinello) and (utils.isclass_or_instance(boss, bosses.KingCalamariBoss) or utils.isclass_or_instance(boss, bosses.HidonBoss) or utils.isclass_or_instance(boss, bosses.BirdettaBoss))) or not utils.isclass_or_instance(location, bosses.Punchinello):
                                if len(repeatable_henchmen) > 0:
                                    if utils.isclass_or_instance(location, bosses.Punchinello) and utils.isclass_or_instance(boss, bosses.KingCalamariBoss):
                                        new_henchman = bosses.KingCalamariTinyBloober
                                    else:
                                        new_henchman = random.choice(repeatable_henchmen)
                                    location.repeatable_henchmen[index][index2].occupant = new_henchman
                                    set_henchman_run_flags(world, boss, new_henchman)
                                elif location.repeatable_henchmen[index][index2].remove_if_empty:
                                    location.repeatable_henchmen[index][index2].occupant = None
                    

                # *** Special cases

                # For Boomer fight, "hide" the Hangin' Shy enemies by moving them off the screen.  This is needed
                # because they set bits for the Boomer fight and disable themselves.  Also make sure speed is max.
                if not utils.isclass_or_instance(location, bosses.Boomer) and utils.isclass_or_instance(boss, bosses.BoomerBoss):
                    formation.members[1].x_pos = 0
                    formation.members[1].y_pos = 255
                    formation.members[2].x_pos = 0
                    formation.members[2].y_pos = 255



    # *** Make sure certain enemies always have max speed for required battle scripts!

    # Valentina calls Dodo.
    world.get_enemy_instance(enemies.Valentina).speed = 255

    # Axem's ship sets bits and disables itself in phase one.
    world.get_enemy_instance(enemies.AxemRangers).speed = 255

    # Hangin' Shy enemies set Boomer bits and disable themselves.
    world.get_enemy_instance(enemies.HanginShy).speed = 255

    # Exor goes first to set immunity.
    world.get_enemy_instance(enemies.Exor).speed = 255


def get_spoiler(world):
    """Get spoiler for this part of the seed/game world.

    Args:
        world (randomizer.logic.main.GameWorld): Game world to randomize.

    Returns:
        dict: Dictionary of spoiler info.

    """
    spoiler = collections.OrderedDict()

    # Extra mapping for some special names that don't quite translate directly.
    special_names = {
        'Hammer Bro': 'Hammer Bros',
        'Knife Guy': 'Clown Bros',
        'Grate Guy': 'Clown Bros',
        'Dodo Solo': 'Dodo',
        'Smilax': 'Megasmilax',
        'Cloaker': 'Cloaker & Domino',
        'Domino': 'Cloaker & Domino',
    }

    for boss in world.boss_locations:
        data = collections.OrderedDict()
        if utils.isclass_or_instance(boss, bosses.StarLocation) and boss.has_star:
            data['Star Piece'] = 'Yes'
        if utils.isclass_or_instance(boss, bosses.BossLocation):
            name = utils.split_camel_case(boss.formation.bosses[0].name)
            data['Boss'] = special_names.get(name, name)
        spoiler[utils.split_camel_case(boss.name)] = data

    return spoiler
