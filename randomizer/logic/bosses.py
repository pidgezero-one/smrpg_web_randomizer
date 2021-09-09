# Boss randomization logic for open mode.

import collections
import random
import statistics
import copy

from . import flags, utils
from randomizer.data import bosses, enemies
from randomizer.data.bosses import is_vanilla, has_vanilla_henchmen, sanitize_animation_script, SpriteSize, HenchmanType, SequenceType, CrownHeight
from randomizer.data.formations import FormationMember
from randomizer.data.npcmodeltables import VramStore, SpriteName
from randomizer.data.eventtables import AreaObjects, Sounds
from randomizer.data.objectsequencetables import SequenceSpeeds, _0x08Flags, _0x10Flags
from randomizer.data.roomobjecttables import RadialDirection, Rooms

from randomizer.data.eventscripts.utils.castle_statue_room.bonk import script as statue_bonk
from randomizer.data.eventscripts.utils.castle_statue_room.bonk_mario import script as statue_bonk_mario
from randomizer.data.eventscripts.utils.smithy_room.non_smithy_3792 import script as non_smithy_3792
from randomizer.data.eventscripts.utils.smithy_room.non_smithy_3794 import script as non_smithy_3794
from randomizer.data.eventscripts.utils.smithy_room.non_smithy_room_509 import objects as non_smithy_509_objects


from .utils import fix_directions_for_sequenced_sprite, new_animation, new_command, is_animation_header, remove_sequence_changes_from_action_script, fix_script_for_scarecrow, is_mario_animation_header




def _boss_fight_filter(world, location):
    """

    Args:
        world (randomizer.logic.main.GameWorld):
        location (randomizer.bosses.BossLocation):

    Returns:
        bool: True is location is okay to be included, False otherwise.

    """
    if not utils.isclass_or_instance(location, bosses.BossLocation):
        return False

    bosses_to_ignore = world.settings.get_flag(flags.ShuffledBosses).disabled
    if location.description in [b.value for b in bosses_to_ignore]:
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


            # Put Shelly in the right battle & give it the right arguments to use for new script
            for location, boss in zip(locations, shuffled_bosses):
                if utils.isclass_or_instance(location, bosses.Birdetta):
                    # Do not allow Shelly to join battles that need their own fixed backgrounds
                    # possibly forbid johnny as well, messes up the vram
                    if utils.isclass_or_instance(boss, bosses.BirdettaBoss) or utils.isclass_or_instance(boss, bosses.ExorBoss) or utils.isclass_or_instance(boss, bosses.CloakerDominoBoss) or utils.isclass_or_instance(boss, bosses.KingCalamariBoss) or utils.isclass_or_instance(boss, bosses.CountdownBoss) or utils.isclass_or_instance(boss, bosses.SmithyBoss) or utils.isclass_or_instance(boss, bosses.AxemRangersBoss):
                        target_formation_birdetta = world.get_enemy_formation_by_index(297)
                        target_formation_birdetta.required_battlefield = bosses.Battlefields.Birdo
                    else:
                        pack = world.get_formation_pack_by_index(boss.pack_number)
                        target_formation = world.get_enemy_formation_by_index(pack.formations[0].index)
                        # Only put Shelly in the battle if it won't break the VRAM - 8192 vram size
                        if not (utils.isclass_or_instance(boss, bosses.BowyerBoss) or utils.isclass_or_instance(boss, bosses.JohnnyBoss) or utils.isclass_or_instance(boss, bosses.YaridovichBoss) or utils.isclass_or_instance(boss, bosses.ClerkBoss) or utils.isclass_or_instance(boss, bosses.ManagerBoss) or utils.isclass_or_instance(boss, bosses.DirectorBoss)):
                            # get list of enemy ID vals who should be summoned by shelly
                            summons = []
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
                        # force nimbus battle to have egg background
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
                
                ctr = 0
                # Now adjust stats for each shuffled pack given the total stats for the slot it's going into.
                for boss, stats in zip(shuffled_bosses, location_stats):
                    pack = world.get_formation_pack_by_index(boss.pack_number)
                    formation = world.get_enemy_formation_by_index(pack.formations[0].index)
                    #print(location)
                    #print(location.boss)
                    #print(location.boss.pack_number)
                    #print(pack.formations[0].index)
                    #print(formation)
                    #print("")
                    #print(locations[ctr], boss)
                    #print(stats)
                    ctr += 1

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

                        #print(enemy, enemy.hp, enemy.attack, enemy.defense, enemy.magic_attack, enemy.magic_defense, enemy.evade, enemy.magic_evade)

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

            # Assign packs to their new locations and update can't run flags.
            # Music will be updated later
            for location, boss in zip(locations, shuffled_bosses):
                location.boss = boss
                pack = world.get_formation_pack_by_index(boss.pack_number)
                formation = world.get_enemy_formation_by_index(pack.formations[0].index)
                formation.can_run_away = location.can_run_away


                # unfortunately, smithy aeros generate action scripts on yaridovich that are too long for the game to understand due to their sequence properties
                # find a better solution for this someday, but for now, just removed
                if utils.isclass_or_instance(location, bosses.Yaridovich) and utils.isclass_or_instance(boss, bosses.SmithyBoss):
                    unique_henchmen = [h for h in boss.unique_henchmen if not utils.isclass_or_instance(h, bosses.SmithyAero)]
                    repeatable_henchmen = [h for h in boss.repeatable_henchmen if not utils.isclass_or_instance(h, bosses.SmithyAero)]
                # de-prioritize background npcs that dont have a pierce animation
                elif utils.isclass_or_instance(location, bosses.Director):
                    unique_henchmen = [h for h in boss.unique_henchmen if h.model.animations is not None and h.model.animations.factory_pierce is not None] + [h for h in boss.unique_henchmen if h.model.animations is None or h.model.animations.factory_pierce is None]
                    repeatable_henchmen = [h for h in boss.repeatable_henchmen if h.model.animations is not None and h.model.animations.factory_pierce is not None] + [h for h in boss.repeatable_henchmen if h.model.animations is None or h.model.animations.factory_pierce is None]
                else:
                    unique_henchmen = boss.unique_henchmen
                    repeatable_henchmen = boss.repeatable_henchmen

                # prepare NPC locations to patch the correct models

                if not is_vanilla(boss, location):
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
                                    # world.get_formation_pack_by_index(new_henchman.pack_number) # why was this even herE?
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
                        if index == 0 and utils.isclass_or_instance(location, bosses.Punchinello) and utils.isclass_or_instance(boss, bosses.KingCalamariBoss):
                            new_henchman = bosses.KingCalamariTinyBloober
                        elif len(repeatable_henchmen) > 0:
                            new_henchman = random.choice(repeatable_henchmen)
                        else:
                            new_henchman = None
                        for index2, model in enumerate(henchman):
                            if world.settings.is_flag_value(flags.BossReplaceMinigameSprites, True) or not model.minigames_only:
                                # ignore punchinello's microbombs unless the substituted boss is Hidon, Birdetta, or King Calamari
                                if (utils.isclass_or_instance(location, bosses.Punchinello) and index == 0 and (utils.isclass_or_instance(boss, bosses.KingCalamariBoss) or utils.isclass_or_instance(boss, bosses.HidonBoss) or utils.isclass_or_instance(boss, bosses.BirdettaBoss))) or not (utils.isclass_or_instance(location, bosses.Punchinello) and index == 0):
                                    if new_henchman is not None:
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

            # Update overworld sprites and animations to match the proper boss.
            fight_builders = {}
            sequence_setters = {}

            for boss_location in world.boss_locations:
                boss = boss_location.boss
                # create boss fight initiation builder
                # 353 is the event ID that houses all the boss battle pack fight initiators
                # events for overworld NPCs/tiles that initiate these fights all reference event 353 in some way shape or form
                if 353 not in fight_builders:
                    fight_builders[353] = {
                        "jumps": [],
                        "executions": []
                    }
                # fights with forced backgrounds need to have them, otherwise just use whatever the level's default background is
                formation = boss_location.formation
                if formation.required_battlefield is None:
                    if utils.isclass_or_instance(boss_location, bosses.Mokura):
                        cmds = [new_command(353, 'set_short', [0x700E, boss.pack_number]), new_command(353, 'start_battle_700E')]
                    else:
                        fields = bosses.battlefield_room_table
                        for t, t_r in fields:
                            if boss_location.identifier in t_r:
                                boss_location.battlefield = t
                                break
                        if boss_location.battlefield is None: # default to BV underground if still empty
                            boss_location.battlefield = bosses.Battlefields.BeanValleyUnderground
                        cmds = [new_command(353, 'start_battle', [boss.pack_number, boss_location.battlefield])]
                else:
                    cmds = [new_command(353, 'start_battle', [boss.pack_number, formation.required_battlefield])]
                cmds.append(new_command(353, 'ret'))
                fight_builders[353]["executions"].extend(cmds)
                jmp = new_command(353, 'jmp_if_7000_equals_short', [boss_location.identifier, cmds[0]["identifier"]])
                fight_builders[353]["jumps"].append(jmp)
                
                # put the shuffled boss names in dialogs that use them
                if utils.isclass_or_instance(boss_location, bosses.Booster):
                    world.search_replace_dialog("`TOWER_BOSS_1`", boss.name)
                    random_bosses = random.sample([loc.boss.name for loc in world.boss_locations if not utils.isclass_or_instance(loc, bosses.Booster)], 3)
                    world.search_replace_dialog("`RANDOM_BOSS_NAME_1`", random_bosses[0])
                    world.search_replace_dialog("`RANDOM_BOSS_NAME_2`", random_bosses[1])
                    world.search_replace_dialog("`RANDOM_BOSS_NAME_3`", random_bosses[2])


                # the rest of these operations only matter if the boss is not vanilla
                # handles sprite substitution and modifying action queues to match substituted sprite
                # also handles slot-specific dialog replacements
                
                if not is_vanilla(boss, boss_location):
                    for boss_sprite_location in boss_location.boss_locations:
                        occupant = boss_sprite_location.occupant
                        room_id = boss_sprite_location.room_id
                        npc_id = boss_sprite_location.npc_id

                        # first: special room changes that need to be made in specific cases
                        if utils.isclass_or_instance(boss_location, bosses.Gunyolk):
                            # hide composite NPCs that aren't used if shuffled
                            for i in [1, 2, 3, 4, 5, 6]:
                                world.update_room_npc_property_by_id(470, i, "visible", False)
                            world.update_room_npc_property_by_id(470, npc_id, "y", 85)

                        elif utils.isclass_or_instance(boss_location, bosses.Smithy):
                            # hide composite NPCs that aren't used if shuffled
                            world.rooms[509]["objects"] = copy.deepcopy([{**s} for s in non_smithy_509_objects])


                        elif utils.isclass_or_instance(boss_location, bosses.MegaSmilax):
                            # move NPCs in megasmilax's room
                            world.update_room_npc_property_by_id(254, 0, "visible", False)
                            world.update_room_npc_property_by_id(254, 1, "z", 1)

                            

                        # booster crown in marrymore
                        # elif room_id == 154 and utils.isclass_or_instance(boss_location, bosses.Booster):
                            
                        #     if boss.crown_height == CrownHeight.Tall:
                        #         script = world.eventscripts[3809]
                        #         for command_index, command in enumerate(script):
                        #             if is_animation_header(command, 5):
                        #                 for subscript_command_index, subscript_command in enumerate(command["subscript"]):
                        #                     if subscript_command["command"] == 'transfer_to_xyzf':
                        #                         subscript_command["args"][2] = 3
                        #                         command["subscript"][subscript_command_index] = subscript_command
                        #                 world.eventscripts[3809][command_index]["subscript"] = command["subscript"]
                        #     elif boss.crown_height == CrownHeight.Mid:
                        #         world.update_room_npc_property_by_id(154, 5, "z_half", True)


                        preferred_size = boss_sprite_location.preferred_size
                        # pick the model from what the incoming boss has available according to what the location prefers
                        if preferred_size == SpriteSize.Attack:
                            if occupant.attack_model is not None:
                                preferred_size = SpriteSize.Attack
                            elif occupant.big_model is not None:
                                preferred_size = SpriteSize.Large
                            else:
                                preferred_size = SpriteSize.Small
                        elif preferred_size == SpriteSize.Large:
                            if occupant.big_model is not None:
                                preferred_size = SpriteSize.Large
                            else:
                                preferred_size = SpriteSize.Small
                        elif preferred_size == SpriteSize.Statue:
                            if occupant.statue_model is not None:
                                preferred_size = SpriteSize.Statue
                            else:
                                preferred_size = SpriteSize.Small
                        else:
                            preferred_size = SpriteSize.Small

                        if preferred_size == SpriteSize.Small:
                            model = occupant.small_model
                        elif preferred_size == SpriteSize.Statue:
                            model = occupant.statue_model
                        elif preferred_size == SpriteSize.Large:
                            model = occupant.big_model
                        elif preferred_size == SpriteSize.Attack:
                            model = occupant.attack_model
                        if model is None:
                            raise Exception("what boss did you try to put here?")

                        # set directional capability
                        if model.model_details is not None:
                            model.directional_capability = model.model_details["vram_store"]
                        else:
                            model.directional_capability = world.models[model.model_id]["vram_store"]


                        # replace the models
                        if preferred_size == SpriteSize.Small or preferred_size == SpriteSize.Statue:
                            world.update_room_npc_property_by_id(room_id, npc_id, "model", model.model_id)
                            model_num = model.model_id
                        else:
                            model_num = world.get_room_npc_property_by_id(room_id, npc_id, "model")
                            world.models[model_num] = model.model_details


                        # statues: flip directions where necessary
                        if boss_sprite_location.preferred_size == SpriteSize.Statue:

                            world.update_room_npc_property_by_id(room_id, npc_id, "set_sequence_playback", False)
                            eligible_directions = world.models[model_num]["vram_store"]

                            # replace directions on original room objects
                            if eligible_directions == VramStore._02_SWSE:
                                new_direction = RadialDirection.SOUTHWEST
                                world.update_room_npc_property_by_id(room_id, npc_id, "direction", new_direction)

                            # guarantee freeze
                            if boss_sprite_location.sequence_setter not in sequence_setters:
                                sequence_setters[boss_sprite_location.sequence_setter] = []
                            cmd = new_animation(boss_sprite_location.sequence_setter, 'action_queue_async', npc_id, [{"identifier": "dummy", "command": "sequence_playback_off"}])
                            sequence_setters[boss_sprite_location.sequence_setter].append(cmd)

                            # pixel shifts
                            if (new_direction == RadialDirection.SOUTHEAST or new_direction == RadialDirection.SOUTHWEST) and (model.horizontal_pixel_shift > 0 or model.vertical_pixel_shift > 0):
                                horizontal_shift = 0xFF & (0xFF + model.horizontal_pixel_shift + 1)
                                vertical_shift = 0xFF & (0xFF + model.vertical_pixel_shift + 1)
                                cmd = new_animation(boss_sprite_location.sequence_setter, 'action_queue_async', npc_id, [{"identifier": "dummy", "command": "shift_xy_pixels", "args": [horizontal_shift, vertical_shift]}])
                                sequence_setters[boss_sprite_location.sequence_setter].append(cmd)
                            elif (new_direction == RadialDirection.NORTHEAST or new_direction == RadialDirection.NORTHWEST) and (model.north_facing_horizontal_pixel_shift > 0 or model.north_facing_vertical_pixel_shift > 0):
                                if new_direction == RadialDirection.NORTHEAST:
                                    horizontal_shift = 0xFF & (0xFF + (-1 * model.north_facing_horizontal_pixel_shift) + 1)
                                    vertical_shift = 0xFF & (0xFF + (-1 * model.north_facing_vertical_pixel_shift) + 1)
                                elif new_direction == RadialDirection.NORTHWEST:
                                    horizontal_shift = 0xFF & (0xFF + model.north_facing_horizontal_pixel_shift + 1)
                                    vertical_shift = 0xFF & (0xFF + model.north_facing_vertical_pixel_shift + 1)
                                cmd = new_animation(boss_sprite_location.sequence_setter, 'action_queue_async', npc_id, [{"identifier": "dummy", "command": "shift_xy_pixels", "args": [horizontal_shift, vertical_shift]}])
                                sequence_setters[boss_sprite_location.sequence_setter].append(cmd)


                        # scarecrow directions are mostly inverted, so swap default directions for scarecrow sprites, don't face on trigger
                        current_direction = world.get_room_npc_property_by_id(room_id, npc_id, "direction")
                        new_direction = current_direction
                        if world.models[model_num]["sprite"] == SpriteName._39_RED_SCARECROW:
                            world.update_room_npc_property_by_id(room_id, npc_id, "face_on_trigger", False)
                            if current_direction == RadialDirection.SOUTHWEST:
                                new_direction = RadialDirection.NORTHWEST
                            elif current_direction == RadialDirection.NORTHWEST:
                                new_direction = RadialDirection.SOUTHEAST
                            elif current_direction == RadialDirection.NORTHEAST:
                                new_direction = RadialDirection.SOUTHWEST
                            elif current_direction == RadialDirection.SOUTHEAST:
                                new_direction = RadialDirection.NORTHEAST
                            
                        
                        world.update_room_npc_property_by_id(room_id, npc_id, "direction", new_direction)

                        # set Z half for short npcs in booster's portrait game room so that theyre visible when giving you the item
                        if utils.isclass_or_instance(boss_location, bosses.Booster) and room_id == Rooms._195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM:
                            if utils.isclass_or_instance(boss, bosses.PandoriteBoss) or utils.isclass_or_instance(boss, bosses.HidonBoss) or utils.isclass_or_instance(boss, bosses.BoxBoyBoss) or utils.isclass_or_instance(boss, bosses.ChesterBoss) or utils.isclass_or_instance(boss, bosses.Jinx1Boss) or utils.isclass_or_instance(boss, bosses.Jinx2Boss) or utils.isclass_or_instance(boss, bosses.Jinx3Boss) or utils.isclass_or_instance(boss, bosses.MokuraBoss) or utils.isclass_or_instance(boss, bosses.DodoBoss) or utils.isclass_or_instance(boss, bosses.BirdettaBoss):
                                world.update_room_npc_property_by_id(room_id, npc_id, "z_half", True)





                        # if default model requires a specific sequence or mold, set it now in room loader subroutine
                        sprite_offset = model.sprite_offset
                        if model.model_details is not None and model.model_details["sprite"] == SpriteName._221_YARIDOVICH_OUT_OF_BATTLE and (utils.isclass_or_instance(boss_location, bosses.Boomer) or utils.isclass_or_instance(boss_location, bosses.Smithy)):
                            pass # mid-sized yaridovich should NOT be set to sequence 1 in these particular locations
                        elif model.sequence_type == SequenceType.Mold or model.sequence > 0:
                            if model.sequence_type == SequenceType.Mold:
                                seq = model.mold
                            else:
                                seq = model.sequence
                            if boss_sprite_location.sequence_setter not in sequence_setters:
                                sequence_setters[boss_sprite_location.sequence_setter] = []
                            if model.sequence_type == SequenceType.Mold:
                                cmd = new_animation(boss_sprite_location.sequence_setter, 'action_queue_async', npc_id, [{"identifier": "dummy", "command": "set_sprite_sequence", "args": [model.mold, sprite_offset, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_MOLD]]}])
                            else:
                                cmd = new_animation(boss_sprite_location.sequence_setter, 'action_queue_async', npc_id, [{"identifier": "dummy", "command": "set_sprite_sequence", "args": [model.sequence, sprite_offset, [_0x08Flags.READ_AS_SEQUENCE]]}])
                            sequence_setters[boss_sprite_location.sequence_setter].append(cmd)
                            # and then, get rid of any commands that may un-set the sequence or mold
                            for script_id in boss_sprite_location.target_scripts:
                                script = world.eventscripts[script_id]
                                for command_index, command in enumerate(script):
                                    if is_animation_header(command, npc_id):
                                        command["subscript"] = remove_sequence_changes_from_action_script(command["subscript"])
                                        world.eventscripts[script_id][command_index] = command
                            for script_id in boss_sprite_location.target_action_scripts:
                                world.actionscripts[script_id] = remove_sequence_changes_from_action_script(world.actionscripts[script_id])
                            

                    
                        # replace animation-specific model sprite if necessary
                        if model.animations is not None:
                            if utils.isclass_or_instance(boss_location, bosses.Croco1) and model.animations.bandits_way_distracted is not None and model.animations.bandits_way_distracted.new_sprite_id is not None:
                                world.models[model.model_id]["sprite"] = model.animations.bandits_way_distracted.new_sprite_id
                            elif utils.isclass_or_instance(boss_location, bosses.Punchinello) and model.animations.mines_punch is not None and model.animations.mines_punch.new_sprite_id is not None:
                                world.models[model.model_id]["sprite"] = model.animations.mines_punch.new_sprite_id
                            elif utils.isclass_or_instance(boss_location, bosses.Booster) and model.animations.chapel_laugh is not None and model.animations.chapel_laugh.new_sprite_id is not None:
                                world.models[model.model_id]["sprite"] = model.animations.chapel_laugh.new_sprite_id
                            elif utils.isclass_or_instance(boss_location, bosses.KingCalamari) and model.animations.ship_beckon is not None and model.animations.ship_beckon.new_sprite_id is not None:
                                world.models[model.model_id]["sprite"] = model.animations.ship_beckon.new_sprite_id
                            elif utils.isclass_or_instance(boss_location, bosses.Johnny) and model.animations.ship_chair is not None and model.animations.ship_chair.new_sprite_id is not None:
                                world.models[model.model_id]["sprite"] = model.animations.ship_chair.new_sprite_id
                            elif (utils.isclass_or_instance(boss_location, bosses.Jinx1) or utils.isclass_or_instance(boss_location, bosses.Jinx2) or utils.isclass_or_instance(boss_location, bosses.Jinx3) or utils.isclass_or_instance(boss_location, bosses.Jagger)) and model.animations.dojo_challenge is not None and model.animations.dojo_challenge.new_sprite_id is not None:
                                world.models[model.model_id]["sprite"] = model.animations.dojo_challenge.new_sprite_id
                            elif utils.isclass_or_instance(boss_location, bosses.Dodo) and model.animations.statue_peck is not None and model.animations.statue_peck.new_sprite_id is not None:
                                world.models[model.model_id]["sprite"] = model.animations.statue_peck.new_sprite_id
                            elif utils.isclass_or_instance(boss_location, bosses.Magikoopa) and model.animations.keep_challenge is not None and model.animations.keep_challenge.new_sprite_id is not None:
                                world.models[model.model_id]["sprite"] = model.animations.keep_challenge.new_sprite_id
                            elif utils.isclass_or_instance(boss_location, bosses.Magikoopa) and model.animations.keep_summon is not None and model.animations.keep_summon.new_sprite_id is not None:
                                world.models[model.model_id]["sprite"] = model.animations.keep_summon.new_sprite_id
                            elif utils.isclass_or_instance(boss_location, bosses.Boomer) and model.animations.chandelier_challenge is not None and model.animations.chandelier_challenge.new_sprite_id is not None:
                                world.models[model.model_id]["sprite"] = model.animations.chandelier_challenge.new_sprite_id
                            elif utils.isclass_or_instance(boss_location, bosses.Smithy) and model.animations.endgame_challenge is not None and model.animations.endgame_challenge.new_sprite_id is not None:
                                world.models[model.model_id]["sprite"] = model.animations.endgame_challenge.new_sprite_id

                        # TODO: partitions

                        # SPECIAL ANIMATIONS
                        for script_id in boss_sprite_location.target_scripts:
                            script = world.eventscripts[script_id]

                            # adjust mines punch pause, still perform sanitization at the end
                            if utils.isclass_or_instance(boss_location, bosses.Punchinello) and script_id == 860:
                                pause = 10
                                for command_index, command in enumerate(script):
                                    if is_animation_header(command, npc_id):
                                        if model.animations is not None and model.animations.mines_punch is not None:
                                            if (model.animations.mines_punch.contact_frame or 0) > 0:
                                                pause = model.animations.mines_punch.contact_frame + 8
                                            else:
                                                pause = model.animations.mines_punch.total_duration if model.animations.mines_punch.total_duration is not None else 30
                                        for subscript_command_index, subscript_command in enumerate(command["subscript"]):
                                            if subscript_command["command"] == 'pause':
                                                subscript_command["args"][0] = pause
                                                command["subscript"][subscript_command_index] = subscript_command
                                        world.eventscripts[script_id][command_index]["subscript"] = command["subscript"]
                                    elif is_mario_animation_header(command):
                                        for subscript_command_index, subscript_command in enumerate(command["subscript"]):
                                            if subscript_command["command"] == 'pause':
                                                subscript_command["args"][0] = max(pause - 2, 1)
                                                command["subscript"][subscript_command_index] = subscript_command
                                        world.eventscripts[script_id][command_index]["subscript"] = command["subscript"]
                                    elif command["command"] == "pause":
                                        world.eventscripts[script_id][command_index]["args"][0] = pause - 4
                                        
                            # magikoopa needs pauses adjusted, still perform sanitization at the end
                            if utils.isclass_or_instance(boss_location, bosses.Magikoopa) and model.animations is not None and model.animations.keep_summon is not None and script_id == 941:
                                if model.animations.keep_summon.contact_frame is not None:
                                    world.eventscripts[script_id][1]["args"][0] = model.animations.keep_summon.contact_frame + 16


                            # adjust dojo pause
                            dojo_duration = 0 if (model.animations is None or model.animations.dojo_challenge is None) else (model.animations.dojo_challenge.total_duration or 0)
                            if utils.isclass_or_instance(boss_location, bosses.Jagger) and model.animations is not None and model.animations.dojo_challenge is not None and script_id == 861:
                                for command_index, command in enumerate(script):
                                    if is_animation_header(command, npc_id):
                                        pause = max(45, dojo_duration)
                                        for subscript_command_index, subscript_command in enumerate(command["subscript"]):
                                            if subscript_command["command"] == 'pause' and subscript_command["args"] == 45:
                                                subscript_command["args"][0] = pause
                                                command["subscript"][subscript_command_index] = subscript_command
                                        world.eventscripts[script_id][command_index]["subscript"] = command["subscript"]
                            elif utils.isclass_or_instance(boss_location, bosses.Jinx1) and model.animations is not None and model.animations.dojo_challenge is not None:
                                for command_index, command in enumerate(script):
                                    if is_animation_header(command, npc_id):
                                        for subscript_command_index, subscript_command in enumerate(command["subscript"]):
                                            if (script_id == 862):
                                                pause = max(45, dojo_duration)
                                                if subscript_command["command"] == 'pause' and subscript_command["args"] == 45:
                                                    subscript_command["args"][0] = pause
                                                    command["subscript"][subscript_command_index] = subscript_command
                                        world.eventscripts[script_id][command_index]["subscript"] = command["subscript"]
                            elif utils.isclass_or_instance(boss_location, bosses.Jinx2) and model.animations is not None and model.animations.dojo_challenge is not None:
                                for command_index, command in enumerate(script):
                                    if is_animation_header(command, npc_id):
                                        for subscript_command_index, subscript_command in enumerate(command["subscript"]):
                                            if (script_id == 864):
                                                pause = max(45, dojo_duration)
                                                if subscript_command["command"] == 'pause' and subscript_command["args"] == 45:
                                                    subscript_command["args"][0] = pause
                                                    command["subscript"][subscript_command_index] = subscript_command
                                            elif (script_id == 863):
                                                if subscript_command["command"] == 'pause' and subscript_command["args"] == 18:
                                                    subscript_command["args"][0] = max(18, dojo_duration)
                                                    command["subscript"][subscript_command_index] = subscript_command
                                        world.eventscripts[script_id][command_index]["subscript"] = command["subscript"]
                            elif utils.isclass_or_instance(boss_location, bosses.Jinx3) and model.animations is not None and model.animations.dojo_challenge is not None:
                                for command_index, command in enumerate(script):
                                    if is_animation_header(command, npc_id):
                                        pause = max(45, dojo_duration)
                                        for subscript_command_index, subscript_command in enumerate(command["subscript"]):
                                            if (script_id == 866):
                                                if subscript_command["command"] == 'pause' and subscript_command["args"] == 45:
                                                    subscript_command["args"][0] = pause
                                                    command["subscript"][subscript_command_index] = subscript_command
                                            elif (script_id == 865):
                                                if subscript_command["command"] == 'pause' and subscript_command["args"] == 18:
                                                    subscript_command["args"][0] = max(18, dojo_duration)
                                                    command["subscript"][subscript_command_index] = subscript_command
                                        world.eventscripts[script_id][command_index]["subscript"] = command["subscript"]
                                        

                            # the following script conditions should NOT undergo sequence sanitization in post
                            # dodo statue subroutines need some explicitly written pauses
                            if utils.isclass_or_instance(boss_location, bosses.Dodo) and (script_id == 936):
                                if model.animations is None or model.animations.statue_peck is None:
                                    world.eventscripts[script_id] = statue_bonk
                                else:
                                    rewritten_peck_subroutine = [
                                        {"identifier": 'dummy', "command": 'sequence_playback_on'},
                                        {"identifier": 'dummy', "command": 'set_animation_speed', "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]},
                                        {"identifier": 'dummy', "command": 'pause', "args": [3]},
                                        {"identifier": 'dummy', "command": 'face_southwest'},
                                        {"identifier": 'dummy', "command": 'set_sprite_sequence', "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]}
                                    ]

                                    peck_duration = model.animations.statue_peck.contact_frame
                                    if peck_duration > 19 or peck_duration is None:
                                        raise Exception('%s statue peck animation contact frame is illegal value' % boss.name)
                                    animation_wait = 15 + 16 - peck_duration
                                    animation_duration = peck_duration + 3
                                    rewritten_peck_subroutine.append({"identifier": 'dummy', "command": 'pause', "args": [animation_wait]})
                                    
                                    rewritten_peck_subroutine.append({"identifier": 'dummy', "command": 'sequence_looping_on'})
                                    
                                    # set animation speed & sequence
                                    if model.animations.statue_peck.speed is not None:
                                        rewritten_peck_subroutine.append({"identifier": 'dummy', "command": 'set_animation_speed', "args": [model.animations.statue_peck.speed, [_0x10Flags.SEQUENCE]]})
                                    rewritten_peck_subroutine.append({"identifier": 'dummy', "command": 'set_sprite_sequence', "args": [model.animations.statue_peck.sequence_id, 0, [_0x08Flags.LOOPING_OFF]]}) # no support for increased sprite #, but no use case for it yet
                                    rewritten_peck_subroutine.append({"identifier": 'dummy', "command": 'pause', "args": [animation_duration]})
                                    
                                    rewritten_peck_subroutine.append({"identifier": 'dummy', "command": 'set_sprite_sequence', "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]})
                                    
                                    world.eventscripts[script_id][0]["subscript"] = copy.deepcopy([{**s} for s in rewritten_peck_subroutine])
                            
                            elif utils.isclass_or_instance(boss_location, bosses.Dodo) and (script_id == 937):
                                if model.animations is None or model.animations.statue_peck is None:
                                    world.eventscripts[script_id] = statue_bonk_mario
                                else:
                                    rewritten_peck_subroutine = [
                                        {"identifier": 'dummy', "command": 'sequence_playback_on'},
                                        {"identifier": 'dummy', "command": 'sequence_looping_on'},
                                        {"identifier": 'dummy', "command": 'set_animation_speed', "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]}
                                    ]

                                    if peck_duration > 20 or peck_duration is None:
                                        raise Exception('%s statue peck animation contact frame is illegal value' % boss.name)
                                    animation_wait = max(16 - peck_duration, 0)
                                    animation_duration = 20 - animation_wait
                                    if animation_wait > 0:
                                        rewritten_peck_subroutine.append({"identifier": 'dummy', "command": 'pause', "args": [animation_wait]})
                                    # set animation speed & sequence
                                    if model.animations.statue_peck.speed is not None:
                                        rewritten_peck_subroutine.append({"identifier": 'dummy', "command": 'set_animation_speed', "args": [model.animations.statue_peck.speed, [_0x10Flags.SEQUENCE]]})
                                    rewritten_peck_subroutine.append({"identifier": 'dummy', "command": 'set_sprite_sequence', "args": [model.animations.statue_peck.sequence_id, 0, [_0x08Flags.LOOPING_OFF]]}) # no support for increased sprite #, but no use case for it yet
                                    rewritten_peck_subroutine.append({"identifier": 'dummy', "command": 'pause', "args": [animation_duration]})

                                    rewritten_peck_subroutine.append({"identifier": 'dummy', "command": 'sequence_looping_off'})
                                    
                                    world.eventscripts[script_id][0]["subscript"] = copy.deepcopy([{**s} for s in rewritten_peck_subroutine])

                            elif utils.isclass_or_instance(boss_location, bosses.Dodo) and (script_id == 939) and model.animations is not None and model.animations.statue_intro is not None:
                                rewritten_intro_subroutine = [
                                    {"identifier": 'dummy', "command": 'shift_to_xy_coords', 'args': [2, 56]},
                                    {"identifier": 'dummy', "command": 'shift_southwest_pixels', 'args': [5]},
                                    {"identifier": 'dummy', "command": 'shift_southeast_pixels', 'args': [16]},
                                    {"identifier": 'dummy', "command": 'sequence_playback_off'},
                                    {"identifier": 'dummy', "command": 'set_sprite_sequence', 'args': [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.MIRROR_SPRITE]]},
                                    {"identifier": 'dummy', "command": 'visibility_on'},
                                    {"identifier": 'dummy', "command": 'pause', 'args': [31]},
                                    {"identifier": 'dummy', "command": 'pause', 'args': [31]},
                                    {"identifier": 'dummy', "command": 'set_animation_speed', 'args': [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]},
                                    {"identifier": 'dummy', "command": 'sequence_playback_on'},
                                    {"identifier": 'dummy', "command": 'sequence_looping_on'}
                                ]

                                if model.animations.statue_intro.total_duration is not None:
                                    intro_duration = min(model.animations.statue_intro.total_duration, 66)
                                    if intro_duration < 66:
                                        rewritten_intro_subroutine.append({"identifier": 'dummy', "command": 'pause', 'args': [66 - intro_duration]})
                                    rewritten_intro_subroutine.append({"identifier": 'dummy', "command": 'set_sprite_sequence', 'args': [model.animations.statue_intro.sequence_id, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]})
                                    rewritten_intro_subroutine.append({"identifier": 'dummy', "command": 'pause', 'args': [intro_duration]})
                                else:
                                    rewritten_intro_subroutine.append({"identifier": 'dummy', "command": 'set_sprite_sequence', 'args': [model.animations.statue_intro.sequence_id, 0, [_0x08Flags.MIRROR_SPRITE]]})
                                    rewritten_intro_subroutine.append({"identifier": 'dummy', "command": 'pause', 'args': [66]})

                                rewritten_intro_subroutine.extend([
                                    {"identifier": 'dummy', "command": 'sequence_looping_off'},
                                    {"identifier": 'dummy', "command": 'set_sprite_sequence', 'args': [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]},
                                    {"identifier": 'dummy', "command": 'pause', 'args': [17]}
                                ])

                                world.eventscripts[script_id][0]["subscript"] = copy.deepcopy([{**s} for s in rewritten_intro_subroutine])

                            elif utils.isclass_or_instance(boss_location, bosses.Dodo) and (script_id == 940) and model.animations is not None and model.animations.statue_flustered is not None:
                                rewritten_recoil_subroutine = [
                                    {"identifier": 'dummy', "command": 'shift_to_xy_coords', 'args': [7, 66]},
                                    {"identifier": 'dummy', "command": 'set_sprite_sequence', 'args': [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]},
                                    {"identifier": 'dummy', "command": 'pause', 'args': [20]},
                                    {"identifier": 'dummy', "command": 'set_animation_speed', 'args': [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]},
                                ]

                                rewritten_recoil_subroutine.append({"identifier": 'dummy', "command": 'set_sprite_sequence', 'args': [model.animations.statue_flustered.sequence_id, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.MIRROR_SPRITE]]})
                                rewritten_recoil_subroutine.append({"identifier": 'dummy', "command": 'pause', 'args': [45]})

                                world.eventscripts[script_id][0]["subscript"] = copy.deepcopy([{**s} for s in rewritten_recoil_subroutine])


                            elif utils.isclass_or_instance(boss_location, bosses.Magikoopa) and (script_id == 942):
                                if model.animations is not None and model.animations.keep_summon is not None:
                                    rewritten_keep_subscript = [
                                        {"identifier": 'dummy', "command": 'face_southeast'},
                                        {"identifier": 'dummy', "command": 'pause', 'args': [60]},
                                        {"identifier": 'dummy', "command": 'set_sprite_sequence', 'args': [model.animations.keep_summon.sequence_id, 0, [_0x08Flags.MIRROR_SPRITE, _0x08Flags.READ_AS_SEQUENCE]]},
                                        {"identifier": 'dummy', "command": 'pause', 'args': [model.animations.keep_summon.total_duration if model.animations.keep_summon.total_duration is not None else 39]},
                                    ]
                                else:
                                    rewritten_keep_subscript = [
                                        {"identifier": 'dummy', "command": 'face_southeast'},
                                        {"identifier": 'dummy', "command": 'pause', 'args': [60]}
                                    ]

                                rewritten_keep_event = [
                                    {"identifier": 'EVENT_942_action_queue_async', "command": 'action_queue_async', 'args': [AreaObjects.NPC_1], "subscript": rewritten_keep_subscript},
                                    {"identifier": 'EVENT_942_ret_291', "command": 'ret'},
                                ]

                                world.eventscripts[script_id] = copy.deepcopy([{**s} for s in rewritten_keep_event])

                            # boomer will need pause adjustments
                            elif utils.isclass_or_instance(boss_location, bosses.Boomer) and (script_id == 943):
                                rewritten_chandelier_subscript = [
                                    {"identifier": 'dummy', "command": 'set_animation_speed', 'args': [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]},
                                    {"identifier": 'dummy', "command": 'fixed_f_coord_on'},
                                    {"identifier": 'dummy', "command": 'pause', "args": [20]},
                                    {"identifier": 'dummy', "command": 'set_animation_speed', 'args': [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]}
                                ]
                                if model.animations is not None and model.animations.chandelier_challenge is not None:
                                    rewritten_chandelier_subscript.append({"identifier": 'dummy', "command": 'set_sprite_sequence', "args": [model.animations.chandelier_challenge.sequence_id, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]})
                                    if model.animations.chandelier_challenge.total_duration is not None:
                                        rewritten_chandelier_subscript.append({"identifier": 'dummy', "command": 'pause', "args": [model.animations.chandelier_challenge.total_duration + 29]})
                                    else:
                                        rewritten_chandelier_subscript.append({"identifier": 'dummy', "command": 'pause', "args": [45]})
                                else:
                                    rewritten_chandelier_subscript.append({"identifier": 'dummy', "command": 'pause', "args": [45]})
                                
                                world.eventscripts[script_id][0]["subscript"] = copy.deepcopy([{**s} for s in rewritten_chandelier_subscript])

                            # smithy needs A LOT of adjustments, to the point of complete script replacement and npc removal
                            elif utils.isclass_or_instance(boss_location, bosses.Smithy) and (script_id == 3792):
                                world.eventscripts[script_id] = copy.deepcopy([{**s} for s in non_smithy_3792])
                            elif utils.isclass_or_instance(boss_location, bosses.Smithy) and (script_id == 3794):
                                world.eventscripts[script_id] = copy.deepcopy([{**s} for s in non_smithy_3794])
                                if model.animations is not None and model.animations.endgame_challenge is not None:
                                    if model.animations.endgame_challenge.total_duration is not None:
                                        challenge_duration = model.animations.endgame_challenge.total_duration
                                        if challenge_duration > 55:
                                            world.eventscripts[945][0]["args"] = [challenge_duration]
                                            world.eventscripts[946][0]["subscript"].insert(0, {"identifier": "dummy", "command": "pause", "args": [challenge_duration - 55]})
                                        endgame_animation = {"identifier": "EVENT_944_taunt", "command": 'action_queue_sync', "args": [AreaObjects.NPC_0], "subscript": [{"identifier": "dummy", "command": 'set_sprite_sequence', 'args': [model.animations.endgame_challenge.sequence_id, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.LOOPING_OFF]]}]}
                                        world.eventscripts[944].insert(0, endgame_animation)
                                    else:
                                        endgame_animation = {"identifier": "EVENT_944_taunt", "command": 'action_queue_sync', "args": [AreaObjects.NPC_0], "subscript": [{"identifier": "dummy", "command": 'set_sprite_sequence', 'args': [model.animations.endgame_challenge.sequence_id, 0, [_0x08Flags.READ_AS_SEQUENCE]]}]}
                                        world.eventscripts[944].insert(0, endgame_animation)
                            else:
                                # replace all sequences and molds if appropriate, remove if not
                                for command_index, command in enumerate(script):
                                    if is_animation_header(command, npc_id):
                                        world.eventscripts[script_id][command_index]["subscript"] = sanitize_animation_script(boss_sprite_location.occupant, boss_location, command["subscript"], model)



                        # action scripts
                        for script_id in boss_sprite_location.target_action_scripts:
                            script = world.actionscripts[script_id]

                            # adjust kitchen animation pauses
                            if utils.isclass_or_instance(boss_location, bosses.Magikoopa) and script_id == 1004 and model.animations is not None and model.animations.keep_summon is not None:
                                for subscript_command_index, subscript_command in enumerate(script):
                                    # set the proper animation for the sprite, and determine if it should loop or not
                                    if subscript_command["command"] == 'set_sprite_sequence':
                                        subscript_command["args"][0] = model.animations.keep_summon.sequence_id
                                        world.actionscripts[script_id][subscript_command_index] = subscript_command

                            # adjust booster door height
                            if utils.isclass_or_instance(boss_location, bosses.Booster) and script_id == 519:
                                initial_shift = None
                                if boss.eye_height > 17:
                                    initial_shift = {"identifier": 'ACTION_519_initial_shift', "command": "shift_south_pixels", "args": [boss.eye_height - 17]}
                                elif boss.eye_height < 17:
                                    initial_shift = {"identifier": 'ACTION_519_initial_shift', "command": "shift_north_pixels", "args": [17 - boss.eye_height]}
                                if initial_shift is not None:
                                    world.actionscripts[script_id].insert(0, initial_shift)

                            # replace all sequences and molds if appropriate, remove if not
                            else:
                                world.actionscripts[script_id] = sanitize_animation_script(boss, boss_location, script, model)


                        # if model is a scarecrow, fix all of its directional commands
                        model_info = world.models[model_num]
                        if model_info["sprite"] == SpriteName._39_RED_SCARECROW:
                            for script_id in boss_sprite_location.target_scripts:
                                script = world.eventscripts[script_id]
                                for command_index, command in enumerate(script):
                                    if is_animation_header(command, npc_id):
                                        command["subscript"] = fix_script_for_scarecrow(command["subscript"])
                                        world.eventscripts[script_id][command_index] = command
                            for script_id in boss_sprite_location.target_action_scripts:
                                world.actionscripts[script_id] = fix_script_for_scarecrow(world.actionscripts[script_id])
                        # if default model requires a specific sequence or mold, fix directional commands
                        elif model.sequence_type == SequenceType.Mold or model.sequence > 0:
                            if model.sequence_type == SequenceType.Mold:
                                seq = model.mold
                            else:
                                seq = model.sequence
                            for script_id in boss_sprite_location.target_scripts:
                                script = world.eventscripts[script_id]
                                for command_index, command in enumerate(script):
                                    if is_animation_header(command, npc_id):
                                        command["subscript"] = fix_directions_for_sequenced_sprite(command["subscript"], model.sequence_type, seq, sprite_offset)
                                        world.eventscripts[script_id][command_index] = command
                            for script_id in boss_sprite_location.target_action_scripts:
                                world.actionscripts[script_id] = fix_directions_for_sequenced_sprite(world.actionscripts[script_id], model.sequence_type, seq, sprite_offset)
                            

                                    


                    # Replace the henchmen in each room
                    for u in boss_location.unique_henchmen + boss_location.repeatable_henchmen:
                        for henchman_location in u:
                            occupant = henchman_location.occupant
                            room_id = henchman_location.room_id
                            npc_id = henchman_location.npc_id
                            
                            if occupant is None:
                                # remove this NPC if necessary when boss has nothing to fill
                                if henchman_location.remove_if_empty: # is gunyolk npc 0 getting an occupant when it shouldnt be?
                                    world.update_room_npc_property_by_id(room_id, npc_id, "visible", False)
                                # leave as-is if not required to remove
                            elif not has_vanilla_henchmen(boss, boss_location):
                                # update model packs & pack container events
                                model = occupant.model
                                
                                world.update_room_npc_property_by_id(room_id, npc_id, "model", model.model_id)

                                model.directional_capability = world.models[model.model_id]["vram_store"]
                                
                                # if model requires a specific sequence or mold, set it now in room loader subroutine
                                sprite_offset = model.sprite_offset
                                if model.sequence_type == SequenceType.Mold or model.sequence > 0:
                                    if henchman_location.sequence_setter not in sequence_setters:
                                        sequence_setters[henchman_location.sequence_setter] = []
                                    if model.sequence_type == SequenceType.Mold:
                                        cmd = new_animation(henchman_location.sequence_setter, 'action_queue_async', npc_id, [{"identifier": "dummy", "command": "set_sprite_sequence", "args": [model.mold, sprite_offset, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_MOLD]]}])
                                    else:
                                        cmd = new_animation(henchman_location.sequence_setter, 'action_queue_async', npc_id, [{"identifier": "dummy", "command": "set_sprite_sequence", "args": [model.sequence, sprite_offset, [_0x08Flags.READ_AS_SEQUENCE]]}])
                                    sequence_setters[henchman_location.sequence_setter].append(cmd)
                                    # and then, get rid of any commands that may un-set the sequence or mold
                                    for script_id in henchman_location.target_scripts:
                                        script = world.eventscripts[script_id]
                                        for command_index, command in enumerate(script):
                                            if is_animation_header(command, npc_id):
                                                command["subscript"] = remove_sequence_changes_from_action_script(command["subscript"])
                                                world.eventscripts[script_id][command_index] = command
                                    for script_id in henchman_location.target_action_scripts:
                                        world.actionscripts[script_id] = remove_sequence_changes_from_action_script(world.actionscripts[script_id])
                                
                                # replace animation-specific sprite if necessary
                                if model.animations is not None:
                                    if utils.isclass_or_instance(boss_location, bosses.Booster) and model.animations.tower_bullet is not None and model.animations.tower_bullet.new_sprite_id is not None:
                                        world.models[model.model_id]["sprite"] = model.animations.tower_bullet.new_sprite_id
                                    elif utils.isclass_or_instance(boss_location, bosses.Bundt) and model.animations.kitchen_prep is not None and model.animations.kitchen_prep.new_sprite_id is not None:
                                        world.models[model.model_id]["sprite"] = model.animations.factory_pierce.new_sprite_id
                                    elif utils.isclass_or_instance(boss_location, bosses.Director) and model.animations.factory_pierce is not None and model.animations.factory_pierce.new_sprite_id is not None:
                                        world.models[model.model_id]["sprite"] = model.animations.factory_pierce.new_sprite_id


                                # SPECIAL ANIMATIONS

                                # event scripts
                                for script_id in henchman_location.target_scripts:
                                    # event scripts
                                    script = world.eventscripts[script_id]

                                    # replace all sequences and molds if appropriate, remove if not
                                    for command_index, command in enumerate(script):
                                        if is_animation_header(command, npc_id):
                                            world.eventscripts[script_id][command_index]["subscript"] = sanitize_animation_script(boss, boss_location, command["subscript"], model)

                                # action scripts
                                for script_id in henchman_location.target_action_scripts:
                                    script = world.actionscripts[script_id]

                                    # adjust kitchen animation pauses
                                    if utils.isclass_or_instance(boss_location, bosses.Bundt) and script_id in [330,331] and model.animations is not None and model.animations.kitchen_prep is not None:
                                        for subscript_command_index, subscript_command in enumerate(script):
                                            # set the proper animation for the sprite, and determine if it should loop or not
                                            if subscript_command["command"] == 'set_sprite_sequence':
                                                subscript_command["args"][0] = model.animations.kitchen_prep.sequence_id
                                                cmd_flags = subscript_command["args"][2]
                                                cmd_flags = [f for f in cmd_flags if f is not _0x08Flags.LOOPING_OFF]
                                                if model.animations is not None and model.animations.kitchen_prep.total_duration is not None:
                                                    cmd_flags.append(_0x08Flags.LOOPING_OFF)
                                                subscript_command["args"][2] = copy.deepcopy(cmd_flags)
                                                world.actionscripts[script_id][subscript_command_index] = subscript_command
                                            # set the pause to last for the entirety of the animation, if not looped
                                            elif subscript_command["command"] == 'pause' and subscript_command["args"][0] == 20:
                                                if model.animations is not None and model.animations.kitchen_prep.total_duration is not None:
                                                    subscript_command["args"][0] = model.animations.kitchen_prep.total_duration
                                                    world.actionscripts[script_id][subscript_command_index] = subscript_command
                                            
                                    # overwrite snifit 3's bullet script
                                    elif utils.isclass_or_instance(boss_location, bosses.Booster) and script_id == 386:
                                        # replace the entire contents of snifit bullet script
                                        if model.animations is None or model.animations.tower_bullet is None:
                                            world.actionscripts[script_id] = [
                                                {"identifier": 'ACTION_386_face_southeast_0', "command": 'face_southeast'},
                                                {"identifier": 'ACTION_386_pause_1', "command": 'pause', "args": [18]},
                                                {"identifier": 'ACTION_386_face_southwest_2', "command": 'face_southwest'},
                                                {"identifier": 'ACTION_386_pause_3', "command": 'pause', "args": [18]},
                                                {"identifier": 'ACTION_386_pause_init', "command": 'pause', "args": [56]},
                                                {"identifier": 'ACTION_386_set_bit_18', "command": 'set_bit', "args": [0x7043, 3]},
                                                {"identifier": 'ACTION_386_pause_second', "command": 'pause', "args": [40]},
                                                {"identifier": 'ACTION_386_jmp_27', "command": 'jmp', "args": ['ACTION_386_pause_init']}
                                            ]
                                        elif model.animations.tower_bullet.total_duration is None:
                                            world.actionscripts[script_id] = [
                                                {"identifier": 'ACTION_386_face_southeast_0', "command": 'face_southeast'},
                                                {"identifier": 'ACTION_386_pause_1', "command": 'pause', "args": [18]},
                                                {"identifier": 'ACTION_386_face_southwest_2', "command": 'face_southwest'},
                                                {"identifier": 'ACTION_386_pause_3', "command": 'pause', "args": [18]},
                                                {"identifier": 'ACTION_386_set_sprite_sequence_16', "command": 'set_sprite_sequence', "args": [model.animations.tower_bullet.sequence_id, 0, [_0x08Flags.READ_AS_SEQUENCE]]},
                                                {"identifier": 'ACTION_386_pause_init', "command": 'pause', "args": [56]},
                                                {"identifier": 'ACTION_386_set_bit_18', "command": 'set_bit', "args": [0x7043, 3]},
                                                {"identifier": 'ACTION_386_pause_second', "command": 'pause', "args": [40]},
                                                {"identifier": 'ACTION_386_jmp_27', "command": 'jmp', "args": ['ACTION_386_pause_init']}
                                            ]
                                        else:
                                            contact = model.animations.tower_bullet.total_duration
                                            if model.animations.tower_bullet.contact_frame is not None:
                                                contact = model.animations.tower_bullet.contact_frame
                                            if contact > 63 or contact < 9: # figure out what to do here, how does the math work out if you speed it up...
                                                print("warning: pauses are negative ", occupant)
                                                pass
                                            
                                            world.actionscripts[script_id] = [
                                                {"identifier": 'ACTION_386_face_southeast_0', "command": 'face_southeast'},
                                                {"identifier": 'ACTION_386_pause_1', "command": 'pause', "args": [18]},
                                                {"identifier": 'ACTION_386_face_southwest_2', "command": 'face_southwest'},
                                                {"identifier": 'ACTION_386_pause_3', "command": 'pause', "args": [18]},
                                                {"identifier": 'ACTION_386_pause_init', "command": 'pause', "args": [64 - contact]},
                                            ]
                                            if model.animations.tower_bullet.speed is not None:
                                                world.actionscripts[script_id].append({"identifier": 'dummy', "command": 'set_animation_speed', "args": [model.animations.tower_bullet.speed, [_0x10Flags.SEQUENCE]]})
                                            world.actionscripts[script_id].extend([
                                                {"identifier": 'ACTION_386_set_sprite_sequence_16', "command": 'set_sprite_sequence', "args": [model.animations.tower_bullet.sequence_id, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.LOOPING_OFF]]},
                                                {"identifier": 'ACTION_386_pause_intermediate', "command": 'pause', "args": [contact - 8]},
                                                {"identifier": 'ACTION_386_set_bit_18', "command": 'set_bit', "args": [0x7043, 3]},
                                                {"identifier": 'ACTION_386_pause_second', "command": 'pause', "args": [40]},
                                                {"identifier": 'ACTION_386_jmp_27', "command": 'jmp', "args": ['ACTION_386_pause_init']}
                                            ])
                                            
                                    # overwrite poundette background animation
                                    elif utils.isclass_or_instance(boss_location, bosses.Director) and script_id in [962, 963, 964] and model.animations is not None and model.animations.factory_pierce is not None:
                                        scr = []
                                        for subscript_command_index, subscript_command in enumerate(script):
                                            if subscript_command["command"] == 'set_sprite_sequence':
                                                subs = copy.deepcopy(subscript_command)
                                                subs["args"][0] = model.animations.factory_pierce.sequence_id
                                                if model.animations.factory_pierce.contact_frame is not None:
                                                    if model.animations.factory_pierce.speed is not None:
                                                        scr.append({"identifier": 'ACTION_%i_spd' % script_id, "command": 'set_animation_speed', "args": [model.animations.factory_pierce.speed, [_0x10Flags.SEQUENCE]]})
                                                    initial_wait = 32 - model.animations.factory_pierce.contact_frame
                                                    if initial_wait > 0:
                                                        scr.append({"identifier": 'ACTION_%i_wait_init' % script_id, "command": 'pause', "args": [initial_wait]})
                                                    scr.append(subs)
                                                    scr.append({"identifier": 'ACTION_%i_wait_post' % script_id, "command": 'pause', "args": [model.animations.factory_pierce.contact_frame]})
                                                else:
                                                    subs_reset = copy.deepcopy(subscript_command)
                                                    subs["args"][2] = [s for s in subs["args"][2] if s != _0x08Flags.LOOPING_OFF]
                                                    scr.append(subs)
                                                    scr.append({"identifier": 'ACTION_%i_wait_post' % script_id, "command": 'pause', "args": [32]})
                                                    subs_reset["args"][0] = model.sequence
                                                    subs_reset["args"][2] = [s for s in subs["args"][2] if s != _0x08Flags.LOOPING_OFF].append(_0x08Flags.LOOPING_OFF)
                                                    scr.append(subs_reset)
                                            elif subscript_command["command"] == 'pause' and subscript_command["args"][0] == 32:
                                                pass
                                            else:
                                                scr.append(subscript_command)
                                        world.actionscripts[script_id] = scr

                                    # replace all sequences and molds if appropriate, remove if not
                                    else:
                                        world.actionscripts[script_id] = sanitize_animation_script(boss, boss_location, script, model)
                                
                                # finally, correct directional commands for specific-sequence sprites
                                if model.sequence_type == SequenceType.Mold or model.sequence > 0:
                                    if model.sequence_type == SequenceType.Mold:
                                        seq = model.mold
                                    else:
                                        seq = model.sequence
                                    for script_id in henchman_location.target_scripts:
                                        script = world.eventscripts[script_id]
                                        for command_index, command in enumerate(script):
                                            if is_animation_header(command, npc_id):
                                                command["subscript"] = fix_directions_for_sequenced_sprite(command["subscript"], model.sequence_type, seq, sprite_offset)
                                                world.eventscripts[script_id][command_index] = command
                                    for script_id in henchman_location.target_action_scripts:
                                        world.actionscripts[script_id] = fix_directions_for_sequenced_sprite(world.actionscripts[script_id], model.sequence_type, seq, sprite_offset)
                                

                    # replace relevant dialogs
                    targeted_dialogs = []
                    incoming_dialogs = []
                    for loc in boss_location.boss_locations:
                        targeted_dialogs.extend(loc.dialogs)
                        incoming_dialogs.extend(loc.occupant.dialog_replacements)
                    incoming_dialogs.extend(boss_location.boss.dialog_replacements)
                    targeted_dialogs.extend(boss_location.dialogs_to_replace)
                    uniq = [item for sublist in boss_location.unique_henchmen for item in sublist] + [item for sublist in boss_location.repeatable_henchmen for item in sublist]
                    if not world.settings.is_flag_enabled(flags.BossReplaceMinigameSprites):
                        uniq = [u for u in uniq if not u.minigames_only]
                    else:
                        incoming_dialogs.extend(boss_location.boss.optional_dialog_replacements)
                        for loc in boss_location.boss_locations:
                            incoming_dialogs.extend(loc.occupant.optional_dialog_replacements)
                    for loc in uniq:
                        targeted_dialogs.extend(loc.dialogs)

                    for dialog_id in targeted_dialogs:
                        for d_id, d_data in incoming_dialogs:
                            if d_id == dialog_id:
                                if d_data == bosses.EMPTY_DIALOG:
                                    # ugh, this sucks
                                    # TODO: implement this better
                                    for e_index in [396, 630, 1133, 1134, 1135, 1136, 1137, 1138, 1139, 1141, 1142, 1143, 1274, 1313, 1323, 1346, 2066, 2077, 2353, 3218, 3286, 3287, 3301, 3302, 3316, 3680]:
                                        new_script = []
                                        for cmd in world.eventscripts[e_index]:
                                            if cmd["command"] == "run_dialog" and cmd["args"][0] == d_id:
                                                if utils.isclass_or_instance(boss, bosses.CzarBoss):
                                                    cmd["command"] = "play_sound"
                                                    cmd["args"] = [Sounds._084_SMOKED]
                                                    new_script.append(cmd)
                                                    new_script.append(new_command(e_index, "pause", [60]))
                                                elif utils.isclass_or_instance(boss, bosses.BundtBoss):
                                                    cmd["command"] = "action_queue_async"
                                                    cmd["args"] = [AreaObjects.MEM_70A8]
                                                    cmd["subscript"] = [
                                                        {"identifier": 'dummy', "command": 'face_southwest_7D', "args": [0x00]},
                                                        {"identifier": 'dummy', "command": 'fixed_f_coord_on'},
                                                        {"identifier": 'dummy', "command": 'turn_clockwise_45_degrees_n_times', "args": [4]},
                                                        {"identifier": 'dummy', "command": 'shift_f_direction_pixels', "args": [1]},
                                                        {"identifier": 'dummy', "command": 'pause', "args": [2]},
                                                        {"identifier": 'dummy', "command": 'shift_f_direction_pixels', "args": [3]},
                                                        {"identifier": 'dummy', "command": 'pause', "args": [2]},
                                                        {"identifier": 'dummy', "command": 'turn_clockwise_45_degrees_n_times', "args": [4]},
                                                        {"identifier": 'dummy', "command": 'shift_f_direction_pixels', "args": [4]},
                                                        {"identifier": 'dummy', "command": 'pause', "args": [2]},
                                                        {"identifier": 'dummy', "command": 'turn_clockwise_45_degrees_n_times', "args": [4]},
                                                        {"identifier": 'dummy', "command": 'shift_f_direction_pixels', "args": [1]},
                                                        {"identifier": 'dummy', "command": 'pause', "args": [2]},
                                                        {"identifier": 'dummy', "command": 'shift_f_direction_pixels', "args": [3]},
                                                        {"identifier": 'dummy', "command": 'pause', "args": [2]},
                                                        {"identifier": 'dummy', "command": 'turn_clockwise_45_degrees_n_times', "args": [4]},
                                                        {"identifier": 'dummy', "command": 'shift_f_direction_pixels', "args": [4]},
                                                        {"identifier": 'dummy', "command": 'pause', "args": [10]},
                                                    ]
                                                    new_script.append(cmd)
                                                else:
                                                    cmd["command"] = "pause"
                                                    cmd["args"] = [30]
                                                    new_script.append(cmd)
                                            else:
                                                new_script.append(cmd)
                                        world.eventscripts[e_index] = new_script
                                else:
                                    world.replace_dialog(d_id, d_data)


                # Always set packs for henchmen, vanilla or not
                for u in boss_location.unique_henchmen + boss_location.repeatable_henchmen:
                    # update model packs & pack container events
                    for henchman_location in u:
                        occupant = henchman_location.occupant
                        room_id = henchman_location.room_id
                        npc_id = henchman_location.npc_id

                        #print(boss_location, occupant)

                        #print(henchman_location.event_id, occupant.pack_number, henchman_location.fill_type)
                        if occupant is None:
                            continue
                        elif henchman_location.fill_type == HenchmanType.Event or henchman_location.fill_type == HenchmanType.ExternalEvent:
                            if henchman_location.event_id not in fight_builders:
                                fight_builders[henchman_location.event_id] = {
                                    "jumps": [new_command(henchman_location.event_id, 'set_7000_to_current_level')],
                                    "executions": []
                                }
                            cmds = [new_command(henchman_location.event_id, 'start_battle', [occupant.pack_number, henchman_location.battlefield]), new_command(henchman_location.event_id, 'ret')]
                            fight_builders[henchman_location.event_id]["executions"].extend(copy.deepcopy([{**s} for s in cmds]))
                            jmp = new_command(henchman_location.event_id, 'jmp_if_7000_equals_short', [room_id, cmds[0]["identifier"]])
                            fight_builders[henchman_location.event_id]["jumps"].append(jmp)
                        elif henchman_location.fill_type == HenchmanType.Pack:
                            world.update_room_npc_property_by_id(room_id, npc_id, "battle_pack", occupant.pack_number)

                                
            # finalize battle pack scripts and sequence setter scripts
            for e in fight_builders:
                fight_builders[e]["jumps"].append(new_command(e, "ret"))
                world.eventscripts[e] = copy.deepcopy([{**s} for s in fight_builders[e]["jumps"]]) + copy.deepcopy([{**s} for s in fight_builders[e]["executions"]])
            for e in sequence_setters:
                world.eventscripts[e] = copy.deepcopy([{**s} for s in sequence_setters[e]]) + world.eventscripts[e]

            # figure out partitions



    # *** Make sure certain enemies always have max speed for required battle scripts!

    # Valentina calls Dodo.
    world.get_enemy_instance(enemies.Valentina).speed = 255

    # Axem's ship sets bits and disables itself in phase one.
    world.get_enemy_instance(enemies.AxemRangers).speed = 255

    # Hangin' Shy enemies set Boomer bits and disable themselves.
    world.get_enemy_instance(enemies.HanginShy).speed = 255

    # Exor goes first to set immunity.
    world.get_enemy_instance(enemies.Exor).speed = 255


def randomize_music(world):
    # Randomize boss music for locations if enabled.
    if world.settings.is_flag_enabled(flags.BossShuffleMusic):
        # noinspection PyTypeChecker
        music_choices = [m for m in world.music_pool if m.name not in world.settings.get_flag(flags.ShuffledMusic).disabled]
        for location in world.boss_locations:
            location.music = random.choice(music_choices)
            boss = location.boss
            pack = world.get_formation_pack_by_index(boss.pack_number)
            formation = world.get_enemy_formation_by_index(pack.formations[0].index)
            formation.music = location.music


def get_spoiler(world):
    """Get spoiler for this part of the seed/game world.

    Args:
        world (randomizer.logic.main.GameWorld): Game world to randomize.

    Returns:
        dict: Dictionary of spoiler info.

    """
    spoiler = collections.OrderedDict()

    for boss in world.boss_locations:
        data = collections.OrderedDict()
        data['Boss'] = boss.boss().classname
        spoiler[utils.split_camel_case(boss.description)] = data

    return spoiler
