"""Apply the results of the shuffler"""

from __future__ import annotations
from typing import cast, TYPE_CHECKING
from uuid import uuid4
import random
import statistics

if TYPE_CHECKING:
    from ..types.gameworld import GameWorld

from randomizer.data.variables.dialog_names import DI1163_BOOSTER_TOWER_DOOR_OPEN, DI2320_TOADSTOOL_ROOM_HINT, DI2908_TREASURE_SELLER_ITEM_2, DI2911_TREASURE_SELLER_ITEM_1, DI2914_TREASURE_SELLER_ITEM_3
from randomizer.data.variables.sprite_names import SPR0096_MARIO_DOLL_SURPRISED, SPR0132_MOLEVILLE_MINE_CART, SPR0135_MINE_CART_BAD_PALETTE, SPR0136_MARIO_IN_MINE_CART, SPR0621_OLD_CLASSIC_MARIO
from ..types.prizelocation import (
    BossFightLocation,
    PrizeRow,
    StarPieceLocation,
    PacketLocation,
    StandingLocation,
    EventLocation,
    TreasureChestLocation,
    TreasureChestLocationRow,
    BoosterHillLocation,
    CharacterRecruitmentLocation,
    TreasureShopLocation,
    ROOM_TO_BATTLEFIELD
)
from ..types.flags import BossShuffleScaleStats, BossScaleOptions, BoosterTowerGate, BoosterTowerGating
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (
    UsableEventScriptCommand,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    Return,
    ClearBit,
    Inc,
    CreatePacketAt7010WithEvent,
    Set7000ToCurrentLevel,
    SummonObjectToSpecificLevel,
    EnableObjectTriggerInSpecificLevel,
    JmpIfVarEqualsConst,
    SetVarToConst,
    StartBattleWithPackAt700E,
    StartBattleAtBattlefield,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.area_object import (
    AreaObject,
)
from smrpgpatchbuilder.datatypes.levels.classes import BaseRoomObject
from ..data.variables.event_script_names import *
from ..data.variables.variable_names import (
    PRIMARY_TEMP_7000,
    STAR_PIECE_GRANT_DIRECTIONAL_BIT,
    STAR_PIECE_GRANT_DIRECTIONAL_BIT_2,
    BOSS_VICTORY_COUNTER,
    BATTLE_PACK_ID,
)
from ..data.variables.room_names import *
from ..data.rooms.npcs import BOWSER_WALKING_DOWN_LEFT_NPC, EMPTY_NPC, GENO_WALKING_DOWN_LEFT_NPC, MALLOW_WALKING_DOWN_LEFT_NPC, MARIO_WALKING_DOWN_LEFT_NPC, TOADSTOOL_WALKING_DOWN_LEFT_NPC
from ..types.flags import CharacterStats
from ..types.prize import BossFightPrize, SpellPrize, CharacterPrize, StandardPrize
from ..types.enemy import Enemy
from ..progression.prizelocations import (
    Mimic1ReloadRewardLocation,
    Mimic2ReloadRewardLocation,
    StarHillStarPiece,
    MarioSpell1,
    MarioSpell2,
    MarioSpell3,
    MarioSpell4,
    MarioSpell5,
    MarioSpell6,
    MallowSpell1,
    MallowSpell2,
    MallowSpell3,
    MallowSpell4,
    MallowSpell5,
    MallowSpell6,
    GenoSpell1,
    GenoSpell2,
    GenoSpell3,
    GenoSpell4,
    GenoSpell5,
    GenoSpell6,
    BowserSpell1,
    BowserSpell2,
    BowserSpell3,
    BowserSpell4,
    BowserSpell5,
    BowserSpell6,
    ToadstoolSpell1,
    ToadstoolSpell2,
    ToadstoolSpell3,
    ToadstoolSpell4,
    ToadstoolSpell5,
    ToadstoolSpell6,
    StartingCharacter1,
    StartingCharacter2,
    StartingCharacter3,
    StartingCharacter4,
    StartingCharacter5,
    MushroomWayCharacter,
    ForestMazeCharacter,
    InnerMinesCharacter,
    MarrymoreCharacter,
    TreasureShopItem1,
    TreasureShopItem2,
    TreasureShopItem3,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import NPC_9, NPC_0, NPC_3, NPC_4, NPC_5
from ..progression.prizes import FirstMimicFightLauncher, SecondMimicFightLauncher

from ..data.rooms.npcs import EMPTY_NPC
from ..data.sprites.subs.bowser.sprite_96 import sprite as BOWSER_96
from ..data.sprites.subs.bowser.sprite_132 import sprite as BOWSER_132
from ..data.sprites.subs.bowser.sprite_135 import sprite as BOWSER_135
from ..data.sprites.subs.bowser.sprite_136 import sprite as BOWSER_136
from ..data.sprites.subs.bowser.sprite_621 import sprite as BOWSER_621
from ..data.sprites.subs.mallow.sprite_96 import sprite as MALLOW_96
from ..data.sprites.subs.mallow.sprite_132 import sprite as MALLOW_132
from ..data.sprites.subs.mallow.sprite_135 import sprite as MALLOW_135
from ..data.sprites.subs.mallow.sprite_136 import sprite as MALLOW_136
from ..data.sprites.subs.mallow.sprite_621 import sprite as MALLOW_621
from ..data.sprites.subs.geno.sprite_96 import sprite as GENO_96
from ..data.sprites.subs.geno.sprite_132 import sprite as GENO_132
from ..data.sprites.subs.geno.sprite_135 import sprite as GENO_135
from ..data.sprites.subs.geno.sprite_136 import sprite as GENO_136
from ..data.sprites.subs.geno.sprite_621 import sprite as GENO_621
from ..data.sprites.subs.peach.sprite_96 import sprite as TOADSTOOL_96
from ..data.sprites.subs.peach.sprite_132 import sprite as TOADSTOOL_132
from ..data.sprites.subs.peach.sprite_135 import sprite as TOADSTOOL_135
from ..data.sprites.subs.peach.sprite_136 import sprite as TOADSTOOL_136
from ..data.sprites.subs.peach.sprite_621 import sprite as TOADSTOOL_621
from ..utils.tower_access_scripts import mario_script, mario_self_script, mallow_script, mallow_self_script, geno_script, geno_self_script, bowser_script, bowser_self_script, toadstool_script, toadstool_self_script



def apply_shuffler_results_to_game_data(world: GameWorld) -> None:
    # This takes the results of the shuffler and uses them to write the event scripts that grant prizes and launch boss fights, scale boss fight stats, put allies and enemies in the overworld where they've been shuffled to, etc

    # set spells and the levels at which they are learned
    for a in world.allies._allies:
        for l in a.levels:
            l.spell_learned = None
    if world.settings.isflag_enabled(CharacterStats):
        mario_spell_levels = sorted([1, *random.sample(range(2, 21), 5)])
        mallow_spell_levels = sorted([1, *random.sample(range(2, 21), 5)])
        geno_spell_levels = sorted([1, *random.sample(range(2, 21), 5)])
        bowser_spell_levels = sorted([1, *random.sample(range(2, 21), 5)])
        toadstool_spell_levels = sorted([1, *random.sample(range(2, 21), 5)])
    else:
        mario_spell_levels = [1, 3, 6, 10, 14, 18]
        mallow_spell_levels = [1, 3, 6, 10, 14, 18]
        geno_spell_levels = [1, 8, 11, 14, 17, None]
        bowser_spell_levels = [1, 12, 15, 18, None, None]
        toadstool_spell_levels = [1, 6, 11, 13, 15, 18]
    for char_id, levels, locations in zip(
        range(0, 5),
        [
            mario_spell_levels,
            toadstool_spell_levels,
            bowser_spell_levels,
            geno_spell_levels,
            mallow_spell_levels,
        ],
        [
            [
                MarioSpell1,
                MarioSpell2,
                MarioSpell3,
                MarioSpell4,
                MarioSpell5,
                MarioSpell6,
            ],
            [
                ToadstoolSpell1,
                ToadstoolSpell2,
                ToadstoolSpell3,
                ToadstoolSpell4,
                ToadstoolSpell5,
                ToadstoolSpell6,
            ],
            [
                BowserSpell1,
                BowserSpell2,
                BowserSpell3,
                BowserSpell4,
                BowserSpell5,
                BowserSpell6,
            ],
            [GenoSpell1, GenoSpell2, GenoSpell3, GenoSpell4, GenoSpell5, GenoSpell6],
            [
                MallowSpell1,
                MallowSpell2,
                MallowSpell3,
                MallowSpell4,
                MallowSpell5,
                MallowSpell6,
            ],
        ],
    ):
        ally = world.allies._allies[char_id]
        assert ally is not None
        for level_num, spell_location in zip(levels, locations):
            if level_num is None:
                continue
            # Spell locations are only added when character spells are shuffled
            if spell_location not in world.locations:
                continue
            level = ally.levels[level_num - 2]
            assert level is not None
            spell_loc = world.get_location(spell_location)
            assert spell_loc is not None
            if spell_loc.prize is not None:
                level.spell_learned = cast(SpellPrize, spell_loc.prize)._spell
    # set starting stats based on where the character is recruited
    for l in [
        StartingCharacter1,
        StartingCharacter2,
        StartingCharacter3,
        StartingCharacter4,
        StartingCharacter5,
        MushroomWayCharacter,
        ForestMazeCharacter,
        InnerMinesCharacter,
        MarrymoreCharacter,
    ]:
        # StartingCharacter2-5 are only added when multiple starting characters are enabled
        if l not in world.locations:
            continue
        loc = cast(CharacterRecruitmentLocation, world.get_location(l))
        if loc.prize is not None:
            charp = cast(CharacterPrize, loc.prize)
            level = charp.starting_level
            ally = charp.ally
            id = ally.index
            char = world.allies._allies[id]
            char.starting_level = level
            char.starting_magic = []
            for lv in range(0, level - 1):
                lvlup = char.levels[lv]
                if lvlup.spell_learned is not None:
                    char.starting_magic.append(lvlup.spell_learned)
                char.starting_max_hp += lvlup.hp_plus
                char.starting_current_hp = char.starting_max_hp
                char.starting_attack += lvlup.attack_plus
                char.starting_defense += lvlup.defense_plus
                char.starting_mg_attack += lvlup.mg_attack_plus
                char.starting_mg_defense += lvlup.mg_defense_plus
                if (lv + 2) % 3 == 0:
                    char.starting_attack += lvlup.attack_plus_bonus
                    char.starting_defense += lvlup.defense_plus_bonus
                elif (lv + 2) % 3 == 1:
                    char.starting_max_hp += lvlup.hp_plus_bonus
                    char.starting_current_hp = char.starting_max_hp
                else:
                    char.starting_mg_attack += lvlup.mg_attack_plus_bonus
                    char.starting_mg_defense += lvlup.mg_defense_plus_bonus

    builders: dict[
        int, tuple[list[UsableEventScriptCommand], list[UsableEventScriptCommand]]
    ] = {}
    # Initialize henchman battle pack selector
    builders[E1189_HENCHMAN_BATTLE_PACK_SELECTOR] = ([], [])
    for place in world.locations.values():
        # Construct prize granter hub events
        # skip frog disciple locations, they're set in shop shuffler
        if isinstance(place, (BossFightLocation, PrizeRow, StarPieceLocation)):
            ctr = place._container_event
            if ctr not in builders:
                builders[ctr] = ([], [])
            if isinstance(place, BossFightLocation):
                decision, execution, henchmen_packs = place.render(world)
                # Add henchmen event script battle packs
                for room_id, pack_id in henchmen_packs:
                    identifier = str(uuid4())
                    builders[E1189_HENCHMAN_BATTLE_PACK_SELECTOR][0].append(
                        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, room_id, [identifier])
                    )
                    builders[E1189_HENCHMAN_BATTLE_PACK_SELECTOR][1].extend([
                        StartBattleAtBattlefield(pack_id, ROOM_TO_BATTLEFIELD[room_id], identifier=identifier),
                        Return(),
                    ])
            elif isinstance(place, TreasureChestLocationRow):
                decision, execution = place.render(world)
            else:
                decision, execution = place.render()
            d_flat = [cmd for l in decision for cmd in l]
            builders[ctr][0].extend(d_flat)
            builders[ctr][1].extend(execution)
            
            if isinstance(place, PacketLocation):
                # set the packet graphic that will load for this prize location type
                cast(
                    CreatePacketAt7010WithEvent,
                    world.event_scripts.get_command_by_identifier(place._replace),
                ).set_packet_id(place.get_packet(world))
            elif isinstance(
                place, (StandingLocation, EventLocation, BoosterHillLocation)
            ):
                npcs = []
                if hasattr(place, "_npc_ids") and hasattr(place, "_rooms"):
                    npcs = zip(place._npc_ids, place._rooms)  # type: ignore
                elif isinstance(place, BoosterHillLocation):
                    npcs = zip(
                        [place._npc_id, place._npc_id],
                        [R014_BOOSTER_HILL, R054_BOOSTER_HILL_DUMMY],
                    )
                for n, room_id in npcs:
                    npc = cast(AreaObject, n)
                    room_id = world.rooms._rooms[room_id]
                    assert room_id is not None
                    if place.prize is not None and place.prize.model is not None:
                        model = place.prize.model().base
                    else:
                        model = EMPTY_NPC
                    cast(BaseRoomObject, room_id.get_npc_by_target_id(npc))._npc = model

            if isinstance(place, StarHillStarPiece):
                # Show the star piece on Star Hill if it's set
                if place.prize is not None:
                    world.event_2496_startup.append(
                        SummonObjectToSpecificLevel(NPC_9, R159_STAR_HILL_AREA_04)
                    )
            if isinstance(place, TreasureShopLocation) and isinstance(place.prize, StandardPrize):
                if hasattr(place.prize, "_nickname"):
                    nn = place.prize.nickname
                    if isinstance(place, TreasureShopItem1):
                        world.update_dialog(DI2911_TREASURE_SELLER_ITEM_1, nn.get_slot_1_dialog())
                    elif isinstance(place, TreasureShopItem2):
                        world.update_dialog(DI2908_TREASURE_SELLER_ITEM_2, nn.get_slot_2_dialog())
                    elif isinstance(place, TreasureShopItem3):
                        world.update_dialog(DI2914_TREASURE_SELLER_ITEM_3, nn.get_slot_3_dialog())

            if isinstance(
                place.prize, (FirstMimicFightLauncher, SecondMimicFightLauncher)
            ):
                # Re-enable mimic fights after opening them, but make sure it applies to every room that contains the check
                # don't want to forget to grab the reload prize and then have the chest be permanently disabled when you change the town state
                assert isinstance(place, TreasureChestLocation)
                contents = []
                npcs = zip(place._npc_ids, place._rooms)
                for n, r in npcs:
                    contents.append(EnableObjectTriggerInSpecificLevel(n, r))
                contents.append(Return())
                if isinstance(place.prize, FirstMimicFightLauncher):
                    if world.get_location(Mimic1ReloadRewardLocation).prize is None:
                        # do not re-enable object trigger if the reload location is empty
                        # should only happen if empty chests is enabled
                        world.event_scripts.get_script_by_id(
                            E0095_REVERT_ALL_CLONE_CHESTS_MIMIC_1
                        ).set_contents([Return()])
                    else:
                        world.event_scripts.get_script_by_id(
                            E0095_REVERT_ALL_CLONE_CHESTS_MIMIC_1
                        ).set_contents(contents)
                elif isinstance(place.prize, SecondMimicFightLauncher):
                    if world.get_location(Mimic2ReloadRewardLocation).prize is None:
                        world.event_scripts.get_script_by_id(
                            E0096_REVERT_ALL_CLONE_CHESTS_MIMIC_2
                        ).set_contents([Return()])
                    else:
                        world.event_scripts.get_script_by_id(
                            E0096_REVERT_ALL_CLONE_CHESTS_MIMIC_2
                        ).set_contents(contents)
        elif isinstance(place, CharacterRecruitmentLocation):
            # this takes care of everything for character gating and recruitment
            place.render(world)

    for key, (decision, execution) in builders.items():
        event_script = world.event_scripts.get_script_by_id(key)
        contents: list[UsableEventScriptCommand] = []
        if key == E0167_BOSS_GRANT_STAR_PIECE:
            contents.extend(
                [
                    ClearBit(STAR_PIECE_GRANT_DIRECTIONAL_BIT),
                    ClearBit(STAR_PIECE_GRANT_DIRECTIONAL_BIT_2),
                    Inc(BOSS_VICTORY_COUNTER),
                ]
            )
        if E0241_FREESTANDING_1_GRANT >= key >= E0227_FREESTANDING_15_GRANT:
            contents.insert(0, Set7000ToCurrentLevel())
        contents.extend([*decision, Return(), *execution])
        event_script.set_contents(contents)



    # Booster Tower gating animation
    # On paper this could go into setup/gating.py, but script insertion depends on who the starting character is, which can be random
    tower_door_room = world.rooms._rooms[R202_BOOSTER_TOWER_ENTRANCE]
    assert tower_door_room is not None
    if not world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.GENO):
        tower_door_room.get_npc_by_target_id(NPC_3)._npc = EMPTY_NPC
    if not world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.TOADSTOOL):
        tower_door_room.get_npc_by_target_id(NPC_4)._npc = EMPTY_NPC
    
    if world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.MARIO):
        world.overworld_dialogs.replace_dialog(DI1163_BOOSTER_TOWER_DOOR_OPEN, """ You can't get inside Booster's\n Tower very easily. You'll need\n a pretty good jumper for that.[await]""")
        if world.overworld_character.ally.index == 0:
            world.event_scripts.get_script_by_id(E1331_TOWER_BREAK_DOWN_DOOR).set_contents(
                mario_self_script.contents
            )
        else:
            world.event_scripts.get_script_by_id(E1331_TOWER_BREAK_DOWN_DOOR).set_contents(
                mario_script.contents
            )
            tower_door_room.get_npc_by_target_id(NPC_0)._npc = MARIO_WALKING_DOWN_LEFT_NPC
    elif world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.MALLOW):
        world.overworld_dialogs.replace_dialog(DI1163_BOOSTER_TOWER_DOOR_OPEN, """ You can't get inside Booster's\n Tower very easily. You'll need\n some pretty magical fluff for that.[await]""")
        if world.overworld_character.ally.index == 4:
            world.event_scripts.get_script_by_id(E1331_TOWER_BREAK_DOWN_DOOR).set_contents(
                mallow_self_script.contents
            )
        else:
            world.event_scripts.get_script_by_id(E1331_TOWER_BREAK_DOWN_DOOR).set_contents(
                mallow_script.contents
            )
            tower_door_room.get_npc_by_target_id(NPC_0)._npc = MALLOW_WALKING_DOWN_LEFT_NPC
    elif world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.GENO):
        world.overworld_dialogs.replace_dialog(DI1163_BOOSTER_TOWER_DOOR_OPEN,""" You can't get inside Booster's\n Tower very easily. You'll need\n a pretty strong gun for that.[await]""")
        if world.overworld_character.ally.index == 3:
            world.event_scripts.get_script_by_id(E1331_TOWER_BREAK_DOWN_DOOR).set_contents(
                geno_self_script.contents
            )
        else:
            world.event_scripts.get_script_by_id(E1331_TOWER_BREAK_DOWN_DOOR).set_contents(
                geno_script.contents
            )
    elif world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.BOWSER):
        world.overworld_dialogs.replace_dialog(DI1163_BOOSTER_TOWER_DOOR_OPEN,""" You can't get inside Booster's\n Tower very easily. You'll need\n a REALLY strong person for that.[await]""")
        if world.overworld_character.ally.index == 2:
            world.event_scripts.get_script_by_id(E1331_TOWER_BREAK_DOWN_DOOR).set_contents(
                bowser_self_script.contents
            )
        else:
            world.event_scripts.get_script_by_id(E1331_TOWER_BREAK_DOWN_DOOR).set_contents(
                bowser_script.contents
            )
            tower_door_room.get_npc_by_target_id(NPC_0)._npc = BOWSER_WALKING_DOWN_LEFT_NPC
    elif world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.TOADSTOOL):
        world.overworld_dialogs.replace_dialog(DI1163_BOOSTER_TOWER_DOOR_OPEN,""" You can't get inside Booster's\n Tower very easily. You'll need\n a pyrotechnician for that.[await]""")
        if world.overworld_character.ally.index == 1:
            world.event_scripts.get_script_by_id(E1331_TOWER_BREAK_DOWN_DOOR).set_contents(
                toadstool_self_script.contents
            )
        else:
            world.event_scripts.get_script_by_id(E1331_TOWER_BREAK_DOWN_DOOR).set_contents(
                toadstool_script.contents
            )
            tower_door_room.get_npc_by_target_id(NPC_0)._npc = TOADSTOOL_WALKING_DOWN_LEFT_NPC
    elif world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.PUNCHINELLO):
        world.overworld_dialogs.replace_dialog(DI1163_BOOSTER_TOWER_DOOR_OPEN,""" You can't get inside Booster's\n Tower very easily. You'll need\n to track down a hot-head for that.[await]""")
    elif world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.MINES):
        world.overworld_dialogs.replace_dialog(DI1163_BOOSTER_TOWER_DOOR_OPEN,""" You can't get inside Booster's\n Tower very easily. You'll need\n to get there via minecart.[await]""")


    # Apply boss stat scaling after all prizes are set
    apply_boss_stat_scaling(world)

    # put the right character clone in the sunken ship mirror room
    # and also sub character sprites in overworld where appropriate
    # some other edge case logic for character-specific stuff could go here too
    clone_room = world.rooms._rooms[R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM]
    assert clone_room is not None
    if world.overworld_character.ally.index == 1:
        clone_room.get_npc_by_target_id(NPC_0)._npc = TOADSTOOL_WALKING_DOWN_LEFT_NPC
        world.sprites.sprites[SPR0096_MARIO_DOLL_SURPRISED] = TOADSTOOL_96
        world.sprites.sprites[SPR0132_MOLEVILLE_MINE_CART] = TOADSTOOL_132
        world.sprites.sprites[SPR0135_MINE_CART_BAD_PALETTE] = TOADSTOOL_135
        world.sprites.sprites[SPR0136_MARIO_IN_MINE_CART] = TOADSTOOL_136
        world.sprites.sprites[SPR0621_OLD_CLASSIC_MARIO] = TOADSTOOL_621
        world.update_dialog(DI2320_TOADSTOOL_ROOM_HINT, " Hello, Princess![await][pause] Did you forget\n something in your room?[await]")
    elif world.overworld_character.ally.index == 2:
        clone_room.get_npc_by_target_id(NPC_0)._npc = BOWSER_WALKING_DOWN_LEFT_NPC
        world.sprites.sprites[SPR0096_MARIO_DOLL_SURPRISED] = BOWSER_96
        world.sprites.sprites[SPR0132_MOLEVILLE_MINE_CART] = BOWSER_132
        world.sprites.sprites[SPR0135_MINE_CART_BAD_PALETTE] = BOWSER_135
        world.sprites.sprites[SPR0136_MARIO_IN_MINE_CART] = BOWSER_136
        world.sprites.sprites[SPR0621_OLD_CLASSIC_MARIO] = BOWSER_621
    elif world.overworld_character.ally.index == 3:
        clone_room.get_npc_by_target_id(NPC_0)._npc = GENO_WALKING_DOWN_LEFT_NPC
        world.sprites.sprites[SPR0096_MARIO_DOLL_SURPRISED] = GENO_96
        world.sprites.sprites[SPR0132_MOLEVILLE_MINE_CART] = GENO_132
        world.sprites.sprites[SPR0135_MINE_CART_BAD_PALETTE] = GENO_135
        world.sprites.sprites[SPR0136_MARIO_IN_MINE_CART] = GENO_136
        world.sprites.sprites[SPR0621_OLD_CLASSIC_MARIO] = GENO_621
    elif world.overworld_character.ally.index == 4:
        clone_room.get_npc_by_target_id(NPC_0)._npc = MALLOW_WALKING_DOWN_LEFT_NPC
        world.sprites.sprites[SPR0096_MARIO_DOLL_SURPRISED] = MALLOW_96
        world.sprites.sprites[SPR0132_MOLEVILLE_MINE_CART] = MALLOW_132
        world.sprites.sprites[SPR0135_MINE_CART_BAD_PALETTE] = MALLOW_135
        world.sprites.sprites[SPR0136_MARIO_IN_MINE_CART] = MALLOW_136
        world.sprites.sprites[SPR0621_OLD_CLASSIC_MARIO] = MALLOW_621



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
    # Get the original prize class for this location
    original_prize_class = location._originally_held
    if original_prize_class is None:
        return (0, 0, 0, 0, 0, 0, 0, 0, 0)

    # Instantiate to get the formation and configuration
    original_prize = original_prize_class()
    if not isinstance(original_prize, BossFightPrize):
        return (0, 0, 0, 0, 0, 0, 0, 0, 0)

    # Enemies completely excluded from all scaling (e.g., WaterCrystal, Hangin' Shy)
    scaling_excluded = set(original_prize.scaling_excluded_enemies)

    # Enemies excluded from HP slicing (they don't take from the pie, so don't contribute to location HP)
    hp_slice_excluded = set(original_prize.hp_slice_excluded_enemies)

    # Formation members participating in HP calculation
    hp_counted_members = [
        m for m in original_prize.formation
        if m is not None and m.enemy not in scaling_excluded and m.enemy not in hp_slice_excluded
    ]

    # Build list of (enemy_instance, enemy_class) tuples for HP calculation
    # Include extra_hp_enemies from the prize (e.g., King Calamari's extra tentacles)
    hp_enemy_pairs: list[tuple[Enemy, type]] = []
    for m in hp_counted_members:
        hp_enemy_pairs.append((cast(Enemy, m.enemy()), m.enemy))
    for e_class in original_prize.extra_hp_enemies:
        if e_class not in scaling_excluded:
            hp_enemy_pairs.append((cast(Enemy, e_class()), e_class))

    # Get HP contribution multipliers from the prize (e.g., Dodo at 0.4)
    hp_multipliers = original_prize.hp_pie_contribution_multipliers

    # Calculate HP with multipliers, XP and coins without multipliers
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

    # Determine anchor enemies for other stats
    anchor_spec = original_prize.anchor_enemy
    if anchor_spec is None:
        # Use all non-excluded formation members
        anchor_classes = [
            m.enemy for m in original_prize.formation
            if m is not None and m.enemy not in scaling_excluded
        ]
    elif isinstance(anchor_spec, list):
        anchor_classes = anchor_spec
    else:
        anchor_classes = [anchor_spec]

    # Calculate other stats from anchor enemies
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

    # Get all formation members
    formation_members = [m for m in prize.formation if m is not None]
    if not formation_members:
        return

    # Enemies completely excluded from scaling for this prize
    scaling_excluded = set(prize.scaling_excluded_enemies)

    # Get enemy classes in formation and all classes to scale (excluding scaling_excluded)
    # m.enemy is already a type[Enemy], not an instance
    enemy_classes_in_formation = {m.enemy for m in formation_members if m.enemy not in scaling_excluded}
    all_enemy_classes = enemy_classes_in_formation | set(prize.additional_enemies_to_scale)

    # Build enemy counts: formation members + extra_hp_enemies (excluding scaling_excluded)
    # Each entry in extra_hp_enemies represents one enemy instance
    enemy_counts: dict[type, int] = {}
    for m in formation_members:
        if m.enemy not in scaling_excluded:
            enemy_counts[m.enemy] = enemy_counts.get(m.enemy, 0) + 1
    for e in prize.extra_hp_enemies:
        if e not in scaling_excluded:
            enemy_counts[e] = enemy_counts.get(e, 0) + 1
            # Extra HP enemies also need to be scaled
            all_enemy_classes.add(e)

    if not enemy_classes_in_formation:
        return  # All formation members were excluded

    # Determine anchor class(es), or None to use average of all formation members
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

    # Get reference stats by averaging the anchor class(es)
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
    # This includes hp_slice_excluded_enemies AND additional_enemies_to_scale
    hp_slice_excluded = set(prize.hp_slice_excluded_enemies) | set(prize.additional_enemies_to_scale)

    # Get pie contribution multipliers (affects how much each enemy counts toward total)
    pie_multipliers = prize.hp_pie_contribution_multipliers

    # Calculate HP pie for non-excluded enemies, accounting for instance counts and pie multipliers
    # Total = sum(class_hp * pie_multiplier * count) for all participating classes
    hp_slice_participant_classes = {c for c in enemy_counts.keys() if c not in hp_slice_excluded}
    total_pie_hp_for_slicing = sum(
        cast(Enemy, c()).hp * pie_multipliers.get(c, 1.0) * enemy_counts[c]
        for c in hp_slice_participant_classes
    ) if hp_slice_participant_classes else 0

    # Calculate pie-adjusted reference HP (for scaling excluded enemies)
    # The reference HP should also use the pie multiplier for consistency
    # Average the pie multipliers across all anchor classes
    avg_pie_multiplier = sum(pie_multipliers.get(c, 1.0) for c in anchor_classes) / len(anchor_classes)
    ref_pie_hp = ref_hp * avg_pie_multiplier
    if total_pie_hp_for_slicing > 0:
        ref_new_hp = round(location_hp * (ref_pie_hp / total_pie_hp_for_slicing))
    else:
        # No participants in slicing - reference gets full location HP
        ref_new_hp = location_hp

    # Calculate total original XP for XP ratio calculation
    total_original_xp = sum(cast(Enemy, c()).xp for c in enemy_classes_in_formation)
    if total_original_xp == 0:
        total_original_xp = 1  # Avoid division by zero

    # Helper to scale a stat relative to reference, clamped to 0-255
    def scale_stat(loc_stat: int, orig_stat: int, ref_orig: float, ratio: float) -> int:
        if ref_orig > 0:
            result = round(loc_stat * (orig_stat / ref_orig) * ratio)
        else:
            result = round(orig_stat * ratio)
        return max(0, min(255, result))

    # Apply stats to each enemy class
    for enemy_class in all_enemy_classes:
        enemy = cast(Enemy, world.get_enemy(cast(type[Enemy], enemy_class)))
        if enemy is None:
            continue

        # Get original stats for this enemy (fresh instance)
        original = cast(Enemy, enemy_class())

        # === HP Calculation ===
        # Get pie-adjusted HP for this enemy (used for determining share of pie)
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

        # Apply ratio multiplier if defined on the enemy itself
        new_hp = round(new_hp * enemy.ratio_hp)
        enemy.set_hp(new_hp)

        # === Other Stats ===
        # All enemies scale relative to reference (average or anchor)
        enemy.set_attack(scale_stat(attack, original.attack, ref_attack, enemy.ratio_attack))
        enemy.set_defense(scale_stat(defense, original.defense, ref_defense, enemy.ratio_defense))
        enemy.set_magic_attack(scale_stat(magic_attack, original.magic_attack, ref_magic_attack, enemy.ratio_magic_attack))
        enemy.set_magic_defense(scale_stat(magic_defense, original.magic_defense, ref_magic_defense, enemy.ratio_magic_defense))
        enemy.set_evade(scale_stat(evade, original.evade, ref_evade, enemy.ratio_evade))
        enemy.set_magic_evade(scale_stat(magic_evade, original.magic_evade, ref_magic_evade, enemy.ratio_magic_evade))

        # === XP Calculation ===
        # Scale XP proportionally based on original XP contribution
        if enemy_class in enemy_classes_in_formation:
            xp_ratio = original.xp / total_original_xp
            enemy.set_xp(round(xp * xp_ratio))


def apply_boss_stat_scaling(world: GameWorld) -> None:
    """Apply stat scaling to boss fights based on settings.

    Modes:
    - VANILLA: No stat changes
    - MATCH: Each location's original stats apply to its current prize
    - RANDOM: Location stats are randomly assigned to prizes (one-to-one)
    """
    if world.settings.is_flag_value(BossShuffleScaleStats, BossScaleOptions.VANILLA):
        return  # No scaling needed

    # Collect all boss fight locations with valid prizes
    boss_locations: list[BossFightLocation] = []
    for location in world.locations.values():
        if isinstance(location, BossFightLocation):
            if isinstance(location.prize, location._originally_held):
                continue
            boss_locations.append(location)

    if not boss_locations:
        return

    # Calculate stats for all locations
    location_stats: list[tuple[BossFightLocation, tuple[int, int, int, int, int, int, int, int, int]]] = []
    for location in boss_locations:
        stats = _calculate_location_stats(location, world)
        if stats[0] > 0:  # Only include if valid stats (HP > 0)
            location_stats.append((location, stats))

    if world.settings.is_flag_value(BossShuffleScaleStats, BossScaleOptions.MATCH):
        # Apply each location's stats to its own prize
        for location, stats in location_stats:
            assert isinstance(location.prize, BossFightPrize)
            _apply_stats_to_prize(location.prize, stats, world)

    elif world.settings.is_flag_value(BossShuffleScaleStats, BossScaleOptions.RANDOM):
        # Create random one-to-one mapping between location stats and prizes
        prizes = [loc.prize for loc, _ in location_stats]
        stats_list = [stats for _, stats in location_stats]

        # Shuffle the stats
        random.shuffle(stats_list)

        # Apply shuffled stats to prizes
        for prize, stats in zip(prizes, stats_list):
            assert isinstance(prize, BossFightPrize)
            _apply_stats_to_prize(prize, stats, world)
