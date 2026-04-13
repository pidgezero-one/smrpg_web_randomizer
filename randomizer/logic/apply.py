"""Apply the results of the shuffler"""

from __future__ import annotations
from typing import cast, TYPE_CHECKING
from uuid import uuid4
import random
import statistics

from randomizer.types.gameworld import DI2730_FROGFUCIUS_OFFER_HINT
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments import NPC_PALETTE_ROW_1, NPC_PALETTE_ROW_2, NPC_PALETTE_ROW_3 ,NPC_PALETTE_ROW_4,NPC_PALETTE_ROW_5,NPC_PALETTE_ROW_6, NPC_PALETTE_ROW_7

from ..data.variables.event_palette_names import * # holy shit i cannot deal with how slow pylance is, fuck it just import everything
from randomizer.logic.partition_calculator import snapshot_vanilla_room_states, update_changed_room_partitions

if TYPE_CHECKING:
    from ..types.gameworld import GameWorld

from randomizer.data.variables.dialog_names import DI1163_BOOSTER_TOWER_DOOR_OPEN, DI2320_TOADSTOOL_ROOM_HINT, DI2908_TREASURE_SELLER_ITEM_2, DI2911_TREASURE_SELLER_ITEM_1, DI2914_TREASURE_SELLER_ITEM_3
from randomizer.data.variables.sprite_names import SPR0031_ALT_PROTAGONIST_1, SPR0032_ALT_PROTAGONIST_2, SPR0033_ALT_PROTAGONIST_3, SPR0034_ALT_PROTAGONIST_4, SPR0035_ALT_PROTAGONIST_5, SPR0036_ALT_PROTAGONIST_6, SPR0037_ALT_PROTAGONIST_7, SPR0096_MARIO_DOLL_SURPRISED, SPR0132_MOLEVILLE_MINE_CART, SPR0135_MINE_CART_BAD_PALETTE, SPR0136_MARIO_IN_MINE_CART, SPR0621_OLD_CLASSIC_MARIO
from ..types.prizelocation import (
    BossFightLocation,
    PrizeRow,
    RiverLocation,
    StarPieceLocation,
    StandingLocation,
    EventLocation,
    TreasureChestLocation,
    BoosterHillLocation,
    CharacterRecruitmentLocation,
    TreasureShopLocation,
    ROOM_TO_BATTLEFIELD
)
from ..types.flags import BossShuffleScaleStats, BossScaleOptions, BoosterTowerGate, BoosterTowerGating, CharacterLearnedSpells, DifferentiateRepeatedBosses, SpellsAnywhere
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (
    UsableEventScriptCommand,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    JmpIfBitClear,
    PaletteSet,
    PaletteSetMorphs,
    Return,
    ClearBit,
    SetBit,
    Inc,
    Set7000ToCurrentLevel,
    SummonObjectToSpecificLevel,
    JmpIfVarEqualsConst,
    JmpToEvent,
    StartBattleAtBattlefield,
    EnterArea
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import (
    A_SetSpriteSequence,
)
from ..types.ally import SpriteAnimationState
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.area_object import (
    AreaObject,
)
from smrpgpatchbuilder.datatypes.levels.classes import BaseRoomObject, ChestNPC, ChestClone
from ..data.variables.event_script_names import *
from ..data.variables.variable_names import (
    PRIMARY_TEMP_7000,
    SMITHY_BOSS_HUNT_WIN_CONDITION,
    STAR_PIECE_GRANT_DIRECTIONAL_BIT,
    STAR_PIECE_GRANT_DIRECTIONAL_BIT_2,
    BOSS_VICTORY_COUNTER,
    TEMP_704A_2,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments import NORTHWEST
from ..data.variables.room_names import *
from ..data.rooms.npcs import ALLY_CLONE_NPC, BOWSER_WALKING_DOWN_LEFT_NPC, BOWSER_WALKING_DOWN_LEFT_NPC_2, EMPTY_NPC, GENO_WALKING_DOWN_LEFT_NPC_2_CLONEABLE, MALLOW_WALKING_DOWN_LEFT_NPC_2, MARIO_WALKING_DOWN_LEFT_NPC, TOADSTOOL_WALKING_DOWN_LEFT_LOW_VRAM
from ..types.flags import CharacterStats
from ..types.prize import BossFightPrize, ItemPrize, SlotsPrize, SpellPrize, CharacterPrize, StandardPrize
from ..types.enemy import Enemy
from ..progression.prizelocations import (
    Mimic3BossFight,
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
from ..data.enemies.enemies import CULEX3DEnemy
from ..progression.prizes import (
    SmithyBossFight,
    Punchinello2BossFight,
    Booster2BossFight,
    Bundt2BossFight,
    Johnny2Fight,
    Belome3Fight,
    Jinx4BossFight,
    Culex3DBossFight,
)

from ..data.rooms.npcs import EMPTY_NPC
from ..data.physical_objects.items import DefaultItem
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
from ..data.sprites.subs.peach.sprite_962 import sprite as TOADSTOOL_962
from ..data.sprites.subs.peach.sprite_963 import sprite as TOADSTOOL_963
from ..data.sprites.subs.peach.sprite_964 import sprite as TOADSTOOL_964
from ..data.sprites.subs.peach.sprite_965 import sprite as TOADSTOOL_965
from ..data.sprites.subs.peach.sprite_966 import sprite as TOADSTOOL_966
from ..data.sprites.subs.peach.sprite_967 import sprite as TOADSTOOL_967
from ..data.sprites.subs.peach.sprite_968 import sprite as TOADSTOOL_968
from ..data.sprites.subs.bowser.sprite_969 import sprite as BOWSER_969
from ..data.sprites.subs.bowser.sprite_970 import sprite as BOWSER_970
from ..data.sprites.subs.bowser.sprite_971 import sprite as BOWSER_971
from ..data.sprites.subs.bowser.sprite_972 import sprite as BOWSER_972
from ..data.sprites.subs.bowser.sprite_973 import sprite as BOWSER_973
from ..data.sprites.subs.bowser.sprite_974 import sprite as BOWSER_974
from ..data.sprites.subs.bowser.sprite_975 import sprite as BOWSER_975
from ..data.sprites.subs.mallow.sprite_976 import sprite as MALLOW_976
from ..data.sprites.subs.mallow.sprite_977 import sprite as MALLOW_977
from ..data.sprites.subs.mallow.sprite_978 import sprite as MALLOW_978
from ..data.sprites.subs.mallow.sprite_979 import sprite as MALLOW_979
from ..data.sprites.subs.mallow.sprite_980 import sprite as MALLOW_980
from ..data.sprites.subs.mallow.sprite_981 import sprite as MALLOW_981
from ..data.sprites.subs.mallow.sprite_982 import sprite as MALLOW_982
from ..data.sprites.subs.geno.sprite_983 import sprite as GENO_983
from ..data.sprites.subs.geno.sprite_984 import sprite as GENO_984
from ..data.sprites.subs.geno.sprite_985 import sprite as GENO_985
from ..data.sprites.subs.geno.sprite_986 import sprite as GENO_986
from ..data.sprites.subs.geno.sprite_987 import sprite as GENO_987
from ..data.sprites.subs.geno.sprite_988 import sprite as GENO_988
from ..data.sprites.subs.geno.sprite_989 import sprite as GENO_989
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
        # Skip spell assignment if SpellsAnywhere is enabled
        # (spells will be found as items in the world instead of learned at level-up)
        if world.settings.isflag_enabled(SpellsAnywhere):
            continue
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
            if world.settings.is_flag_value(BossShuffleScaleStats, BossScaleOptions.GODMODE):
                level = 30
            ally = charp.ally
            id = ally.index
            char = world.allies._allies[id]
            char.starting_level = level
            # When SpellsAnywhere is enabled, characters don't start with or learn any spells
            # (spells are found as items in the world instead)
            if world.settings.isflag_enabled(SpellsAnywhere):
                char.starting_magic = []
            # When spell shuffling is enabled (but not SpellsAnywhere), rebuild from scratch
            elif world.settings.isflag_enabled(CharacterLearnedSpells):
                char.starting_magic = []
            else:
                # Keep original starting_magic (level-1 spells like Jump)
                char.starting_magic = list(char.starting_magic)
            # Apply stat bonuses from level-ups (and add spells if not SpellsAnywhere)
            for lv in range(0, level - 1):
                lvlup = char.levels[lv]
                # Only add spells from level-ups if SpellsAnywhere is disabled
                if not world.settings.isflag_enabled(SpellsAnywhere):
                    if lvlup.spell_learned is not None and lvlup.spell_learned not in char.starting_magic:
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

    # Godmode: grant all spell-slot spells to each character's starting_magic
    # (only when SpellsAnywhere is disabled, since spells are in the world otherwise)
    if (
        world.settings.is_flag_value(BossShuffleScaleStats, BossScaleOptions.GODMODE)
        and not world.settings.isflag_enabled(SpellsAnywhere)
    ):
        all_spell_locations_by_char: list[tuple[int, list[type]]] = [
            (0, [MarioSpell1, MarioSpell2, MarioSpell3, MarioSpell4, MarioSpell5, MarioSpell6]),
            (1, [ToadstoolSpell1, ToadstoolSpell2, ToadstoolSpell3, ToadstoolSpell4, ToadstoolSpell5, ToadstoolSpell6]),
            (2, [BowserSpell1, BowserSpell2, BowserSpell3, BowserSpell4, BowserSpell5, BowserSpell6]),
            (3, [GenoSpell1, GenoSpell2, GenoSpell3, GenoSpell4, GenoSpell5, GenoSpell6]),
            (4, [MallowSpell1, MallowSpell2, MallowSpell3, MallowSpell4, MallowSpell5, MallowSpell6]),
        ]
        for char_id, spell_locs in all_spell_locations_by_char:
            char = world.allies._allies[char_id]
            for spell_loc_type in spell_locs:
                if spell_loc_type not in world.locations:
                    continue
                spell_loc = world.get_location(spell_loc_type)
                if spell_loc is not None and spell_loc.prize is not None:
                    spell = cast(SpellPrize, spell_loc.prize)._spell
                    if spell not in char.starting_magic:
                        char.starting_magic.append(spell)

    builders: dict[
        int, tuple[list[UsableEventScriptCommand], list[UsableEventScriptCommand]]
    ] = {}
    # Collect all henchman container events used
    henchman_container_events: set[int] = set()
    # Snapshot vanilla NPC states before any shuffling modifies room objects
    snapshot_vanilla_room_states(world)

    # When repeated bosses shouldn't be visually differentiated, copy palette
    # IDs from a canonical source sprite onto each duplicate/variant sprite
    # so they share overworld coloring. Must run before location render so
    # downstream renderers (e.g. KeepAfterObstaclesBossFight setting event
    # palettes 24/25) read the unified palette IDs.
    if not world.settings.isflag_enabled(DifferentiateRepeatedBosses):
        sprite_palette_copies: list[tuple[int, int]] = [
            (190, 189),
            (607, 191),
            (608, 191),
            (727, 191),
            (590, 589),
            (736, 589),
            (739, 55),
            (737, 592),
            (740, 721),
            (742, 633),
            (738, 50),
            (583, 586),
            (584, 586),
            (585, 586),
        ]
        for target_id, source_id in sprite_palette_copies:
            source_palette_id = world.get_sprite(source_id).palette_id
            world.get_sprite(target_id).palette_id = source_palette_id

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
                for container_event, room_id, pack_id in henchmen_packs:
                    henchman_container_events.add(container_event)
                    if container_event not in builders:
                        builders[container_event] = ([], [])
                    identifier = str(uuid4())
                    builders[container_event][0].append(
                        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, room_id, [identifier])
                    )
                    builders[container_event][1].extend([
                        StartBattleAtBattlefield(pack_id, ROOM_TO_BATTLEFIELD[room_id], identifier=identifier),
                        Return(),
                    ])
            else:
                decision, execution = place.render(world)
            d_flat = [cmd for l in decision for cmd in l]
            builders[ctr][0].extend(d_flat)

            # Smithy fight needs special post-battle handling: set TEMP_704A_2
            # and jump to E1011 instead of returning, so the game over / run away
            # check works correctly for multi-phase Smithy battles.
            if isinstance(place.prize, SmithyBossFight):
                patched: list[UsableEventScriptCommand] = []
                for i, cmd in enumerate(execution):
                    patched.append(cmd)
                    if isinstance(cmd, StartBattleAtBattlefield) and i + 1 < len(execution) and isinstance(execution[i + 1], Return):
                        patched.extend([
                            JmpIfBitClear(SMITHY_BOSS_HUNT_WIN_CONDITION, ["smithy_boss_hunt_disabled"]),
	                        EnterArea(room_id=R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE, face_direction=NORTHWEST, x=4, y=48, z=0, run_entrance_event=False),
                            JmpToEvent(E3885_END_GAME),
                            SetBit(TEMP_704A_2, identifier="smithy_boss_hunt_disabled"),
                            JmpToEvent(E1011_POST_MINES_BOSS_CHECK_IF_WON)
                        ])
                    elif isinstance(cmd, Return) and i > 0 and isinstance(execution[i - 1], StartBattleAtBattlefield):
                        continue  # Skip the Return that follows StartBattle
                execution = patched

            builders[ctr][1].extend(execution)

            if isinstance(place.prize, SlotsPrize):
                # special handling: battlefield selection for failed slot machines which fights mimic #3
                proxy_fight = cast(BossFightLocation, world.get_location(Mimic3BossFight))
                slot_pack = proxy_fight.slots_pack_id
                assert slot_pack is not None
                room = place._rooms[0]
                battlefield = ROOM_TO_BATTLEFIELD[room]
                proxy_prize = cast(BossFightPrize, proxy_fight.prize)
                if proxy_prize.force_battlefield is not None:
                    battlefield = proxy_prize.force_battlefield
                identifier = str(uuid4())
                if E0353_BOSS_BATTLE not in builders:
                    builders[E0353_BOSS_BATTLE] = ([], [])
                builders[E0353_BOSS_BATTLE][0].append(JmpIfVarEqualsConst(PRIMARY_TEMP_7000, place.prize.override_id, [identifier]))
                builders[E0353_BOSS_BATTLE][1].extend([
                    StartBattleAtBattlefield(slot_pack, battlefield, identifier=identifier),
                    Return(),
                ])
            
            if isinstance(
                place, (StandingLocation, EventLocation, RiverLocation)
            ) and not isinstance(place, BoosterHillLocation):
                npcs = []
                if hasattr(place, "_npc_ids") and hasattr(place, "_rooms"):
                    npcs = zip(place._npc_ids, place._rooms)  # type: ignore
                for n, room_id_int in npcs:
                    npc = cast(AreaObject, n)
                    room = world.rooms._rooms[room_id_int]
                    assert room is not None, f"Room {room_id_int} not found"
                    if place.prize is not None and place.prize.model is not None:
                        prize_model = place.prize.model
                        if place._model_allowlist is not None and not issubclass(prize_model, tuple(place._model_allowlist)):
                            prize_model = DefaultItem
                        model = prize_model().base
                    else:
                        model = EMPTY_NPC
                    room_obj = room.get_npc_by_target_id(npc)
                    assert room_obj is not None, f"NPC {npc} not found in room {room_id_int}"
                    cast(BaseRoomObject, room_obj)._npc = model

            if isinstance(place, StarHillStarPiece):
                # Show the star piece on Star Hill if it's set
                if place.prize is not None:
                    world.event_2496_startup.append(
                        SummonObjectToSpecificLevel(NPC_9, R159_STAR_HILL_AREA_04)
                    )
            if isinstance(place, TreasureChestLocation) and isinstance(place.prize, ItemPrize):
                item_id = place.prize.item().item_id
                for npc, room_id in zip(place._npc_ids, place._rooms):
                    ao = npc if isinstance(npc, AreaObject) else AreaObject(npc + 0x14)
                    room = world.rooms._rooms[room_id]
                    if room is not None:
                        room_obj = room.get_npc_by_target_id(ao)
                        if isinstance(room_obj, (ChestNPC, ChestClone)):
                            room_obj.set_lower_70a7(item_id & 0x0F)
                            room_obj.set_upper_70a7((item_id >> 4) & 0x0F)
            if isinstance(place, TreasureShopLocation) and isinstance(place.prize, StandardPrize):
                if hasattr(place.prize, "_nickname"):
                    nn = place.prize.nickname
                    if isinstance(place, TreasureShopItem1):
                        world.update_dialog(DI2911_TREASURE_SELLER_ITEM_1, nn.get_slot_1_dialog())
                    elif isinstance(place, TreasureShopItem2):
                        world.update_dialog(DI2908_TREASURE_SELLER_ITEM_2, nn.get_slot_2_dialog())
                    elif isinstance(place, TreasureShopItem3):
                        world.update_dialog(DI2914_TREASURE_SELLER_ITEM_3, nn.get_slot_3_dialog())

        elif isinstance(place, CharacterRecruitmentLocation):
            # this takes care of everything for character gating and recruitment
            place.render(world)
    # Insert Set7000ToCurrentLevel at the beginning of all henchman container events
    for henchman_event in henchman_container_events:
        builders[henchman_event][0].insert(0,
            Set7000ToCurrentLevel(),
        )
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
    assert tower_door_room is not None, f"Room {R202_BOOSTER_TOWER_ENTRANCE} not found"
    tower_npc_0 = tower_door_room.get_npc_by_target_id(NPC_0)
    assert tower_npc_0 is not None, f"NPC_0 not found in room {R202_BOOSTER_TOWER_ENTRANCE}"
    tower_npc_3 = tower_door_room.get_npc_by_target_id(NPC_3)
    assert tower_npc_3 is not None, f"NPC_3 not found in room {R202_BOOSTER_TOWER_ENTRANCE}"
    tower_npc_4 = tower_door_room.get_npc_by_target_id(NPC_4)
    assert tower_npc_4 is not None, f"NPC_4 not found in room {R202_BOOSTER_TOWER_ENTRANCE}"
    if not world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.GENO):
        tower_npc_3._npc = EMPTY_NPC
    if not world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.TOADSTOOL):
        tower_npc_4._npc = EMPTY_NPC

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
            tower_npc_0._npc = MARIO_WALKING_DOWN_LEFT_NPC
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
            tower_npc_0._npc = MALLOW_WALKING_DOWN_LEFT_NPC_2
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
            tower_npc_0._npc = GENO_WALKING_DOWN_LEFT_NPC_2_CLONEABLE
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
            tower_npc_0._npc = BOWSER_WALKING_DOWN_LEFT_NPC_2
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
            tower_npc_0._npc = TOADSTOOL_WALKING_DOWN_LEFT_LOW_VRAM
    elif world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.PUNCHINELLO):
        world.overworld_dialogs.replace_dialog(DI1163_BOOSTER_TOWER_DOOR_OPEN,""" You can't get inside Booster's\n Tower very easily. You'll need\n to track down a hot-head for that.[await]""")
    elif world.settings.is_flag_value(BoosterTowerGate, BoosterTowerGating.MINES):
        world.overworld_dialogs.replace_dialog(DI1163_BOOSTER_TOWER_DOOR_OPEN,""" You can't get inside Booster's\n Tower very easily. You'll need\n to get there via minecart.[await]""")


    # Apply boss stat scaling after all prizes are set
    apply_boss_stat_scaling(world)

    # Update partition buffers for rooms with shuffled sprites
    update_changed_room_partitions(world)

    # Update freestanding frog coin NPCs in rooms with Coins partition
    # to use the animated frog coin NPC and spinning action script
    from smrpgpatchbuilder.datatypes.levels.classes import BufferType
    from ..data.rooms.npcs import FROG_COIN_NPC, STATIC_FROG_COIN_NPC
    from ..data.variables.action_script_names import A0511_PIPE_VAULT_3_CHEST_ROOM_COIN
    from ..types.prize import FrogCoinPrize
    for location in world.locations.values():
        if not isinstance(location, (StandingLocation, RiverLocation)):
            continue
        if location.originally_held is None or not issubclass(location.originally_held, FrogCoinPrize):
            continue
        # Check if any room containing this prize has a Coins partition buffer
        for room_id in location._rooms:
            # Skip room 41 (Booster Tower minesweeper room) - has coins partition but
            # frog coin NPC there uses a different animation system
            if room_id == R041_BOOSTER_TOWER_8F_AREA_01_MINESWEEPER_ROOM_WCOINS_AND_HIDDEN_FIREBALLS:
                continue
            room = world.rooms._rooms[room_id]
            if room is None or room.partition is None:
                continue
            has_coins_buffer = any(
                buf.buffer_type == BufferType.COINS for buf in room.partition.buffers
            )
            if has_coins_buffer:
                # Update all NPCs for this location in this room
                for npc_id in location._npc_ids:
                    npc_obj = room.get_npc_by_target_id(npc_id)
                    if npc_obj is not None and npc_obj._npc == STATIC_FROG_COIN_NPC:
                        npc_obj._npc = FROG_COIN_NPC
                        npc_obj.set_action_script(A0511_PIPE_VAULT_3_CHEST_ROOM_COIN)

    # Set can_run_away for each boss fight location's formation
    # This must happen after all renders to ensure the correct formation is used
    # Each boss fight is unique, so each formation should only be used by one location
    for location in world.locations.values():
        if isinstance(location, BossFightLocation) and location.prize is not None:
            pack = world.battle_packs._packs[location._pack_id]
            for formation in pack.formations:
                formation.set_can_run_away(location.allow_run_away)

    # Allow running away from the three mimic-reserved packs when MimicsAnywhere
    # is enabled, and from the slots-specific mimic 3 pack when SlotsAnywhere is
    # enabled. Clearing both bits 0 and 1 of formation meta byte 3 ($7EFA1E) puts
    # the formation in the 80% flee-success bucket (vs 50% with only can_run_away
    # cleared). Must run after the loop above, which otherwise resets
    # can_run_away to location.allow_run_away (False for mimic locations).
    from ..types.flags import MimicsAnywhere, SlotsAnywhere
    from ..data.variables.pack_names import (
        PACK156_SEWER_CHEST_FIGHT,
        PACK157_SHIP_CHEST_FIGHT,
        PACK158_VALLEY_CHEST_FIGHT,
        PACK160_SLOTS_CHEST_FIGHT,
    )
    if world.settings.isflag_enabled(MimicsAnywhere):
        for pack_id in (PACK156_SEWER_CHEST_FIGHT, PACK157_SHIP_CHEST_FIGHT, PACK158_VALLEY_CHEST_FIGHT):
            for formation in world.battle_packs._packs[pack_id].formations:
                formation.set_can_run_away(True)
                formation.set_unknown_bit(False)
    if world.settings.isflag_enabled(SlotsAnywhere):
        for formation in world.battle_packs._packs[PACK160_SLOTS_CHEST_FIGHT].formations:
            formation.set_can_run_away(True)
            formation.set_unknown_bit(False)

    # put the right character clone in the sunken ship mirror room
    # and also sub character sprites in overworld where appropriate
    # some other edge case logic for character-specific stuff could go here too
    clone_room = world.rooms._rooms[R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM]
    assert clone_room is not None, f"Room {R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM} not found"
    clone_room_npc_0 = clone_room.get_npc_by_target_id(NPC_0)
    assert clone_room_npc_0 is not None, f"NPC_0 not found in room {R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM}"

    
    starter = cast(CharacterPrize, world.get_location(StartingCharacter1).prize).ally
    # Always have sprites available for the file select menu
    if starter.index == 1:
        world.sprites.sprites[SPR0031_ALT_PROTAGONIST_1] = TOADSTOOL_962
        world.sprites.sprites[SPR0032_ALT_PROTAGONIST_2] = TOADSTOOL_963
        world.sprites.sprites[SPR0033_ALT_PROTAGONIST_3] = TOADSTOOL_964
    elif starter.index == 2:
        world.sprites.sprites[SPR0031_ALT_PROTAGONIST_1] = BOWSER_969
        world.sprites.sprites[SPR0032_ALT_PROTAGONIST_2] = BOWSER_970
        world.sprites.sprites[SPR0033_ALT_PROTAGONIST_3] = BOWSER_971
    elif starter.index == 3:
        world.sprites.sprites[SPR0031_ALT_PROTAGONIST_1] = GENO_983
        world.sprites.sprites[SPR0032_ALT_PROTAGONIST_2] = GENO_984
        world.sprites.sprites[SPR0033_ALT_PROTAGONIST_3] = GENO_985
    elif starter.index == 4:
        world.sprites.sprites[SPR0031_ALT_PROTAGONIST_1] = MALLOW_976
        world.sprites.sprites[SPR0032_ALT_PROTAGONIST_2] = MALLOW_977
        world.sprites.sprites[SPR0033_ALT_PROTAGONIST_3] = MALLOW_978

    # Fully commit to the bit if you've changed your overworld character altogether
    if world.overworld_character.ally.index > 0:
        if world.overworld_character.ally.index == 1:
            world.sprites.sprites[SPR0096_MARIO_DOLL_SURPRISED] = TOADSTOOL_96
            world.sprites.sprites[SPR0132_MOLEVILLE_MINE_CART] = TOADSTOOL_132
            world.sprites.sprites[SPR0135_MINE_CART_BAD_PALETTE] = TOADSTOOL_135
            world.sprites.sprites[SPR0136_MARIO_IN_MINE_CART] = TOADSTOOL_136
            world.sprites.sprites[SPR0621_OLD_CLASSIC_MARIO] = TOADSTOOL_621
            world.sprites.sprites[SPR0034_ALT_PROTAGONIST_4] = TOADSTOOL_965
            world.sprites.sprites[SPR0035_ALT_PROTAGONIST_5] = TOADSTOOL_966
            world.sprites.sprites[SPR0036_ALT_PROTAGONIST_6] = TOADSTOOL_967
            world.sprites.sprites[SPR0037_ALT_PROTAGONIST_7] = TOADSTOOL_968
            world.update_dialog(DI2320_TOADSTOOL_ROOM_HINT, " Hello, Princess![await][pause] Did you forget\n something in your room?[await]")
            world.event_scripts.get_command_by_identifier("midas_palette_1", PaletteSet).set_palette_set_starts_at(EPAL0141_TOADSTOOL_ENDING)
            world.event_scripts.get_command_by_identifier("midas_palette_2", PaletteSet).set_palette_set_starts_at(EPAL0141_TOADSTOOL_ENDING)
            world.event_scripts.get_command_by_identifier("midas_palette_3", PaletteSet).set_palette_set_starts_at(EPAL0141_TOADSTOOL_ENDING)
            world.event_scripts.get_command_by_identifier("midas_palette_4", PaletteSet).set_palette_set_starts_at(EPAL0141_TOADSTOOL_ENDING)
            world.event_scripts.get_command_by_identifier("midas_palette_5", PaletteSet).set_palette_set_starts_at(EPAL0141_TOADSTOOL_ENDING)
            world.event_scripts.get_command_by_identifier("midas_palette_6", PaletteSet).set_palette_set_starts_at(EPAL0141_TOADSTOOL_ENDING)
        elif world.overworld_character.ally.index == 2:
            world.sprites.sprites[SPR0096_MARIO_DOLL_SURPRISED] = BOWSER_96
            world.sprites.sprites[SPR0132_MOLEVILLE_MINE_CART] = BOWSER_132
            world.sprites.sprites[SPR0135_MINE_CART_BAD_PALETTE] = BOWSER_135
            world.sprites.sprites[SPR0136_MARIO_IN_MINE_CART] = BOWSER_136
            world.sprites.sprites[SPR0621_OLD_CLASSIC_MARIO] = BOWSER_621
            world.sprites.sprites[SPR0034_ALT_PROTAGONIST_4] = BOWSER_972
            world.sprites.sprites[SPR0035_ALT_PROTAGONIST_5] = BOWSER_973
            world.sprites.sprites[SPR0036_ALT_PROTAGONIST_6] = BOWSER_974
            world.sprites.sprites[SPR0037_ALT_PROTAGONIST_7] = BOWSER_975
            world.event_scripts.get_command_by_identifier("midas_palette_1", PaletteSet).set_palette_set_starts_at(EPAL0140_BOWSER_ENDING)
            world.event_scripts.get_command_by_identifier("midas_palette_1", PaletteSet).set_from_row(NPC_PALETTE_ROW_3)
            world.event_scripts.get_command_by_identifier("midas_palette_2", PaletteSet).set_palette_set_starts_at(EPAL0140_BOWSER_ENDING)
            world.event_scripts.get_command_by_identifier("midas_palette_2", PaletteSet).set_from_row(NPC_PALETTE_ROW_3)
            world.event_scripts.get_command_by_identifier("midas_palette_3", PaletteSet).set_palette_set_starts_at(EPAL0140_BOWSER_ENDING)
            world.event_scripts.get_command_by_identifier("midas_palette_3", PaletteSet).set_from_row(NPC_PALETTE_ROW_3)
            world.event_scripts.get_command_by_identifier("midas_palette_4", PaletteSet).set_palette_set_starts_at(EPAL0140_BOWSER_ENDING)
            world.event_scripts.get_command_by_identifier("midas_palette_4", PaletteSet).set_from_row(NPC_PALETTE_ROW_3)
            world.event_scripts.get_command_by_identifier("midas_palette_5", PaletteSet).set_palette_set_starts_at(EPAL0140_BOWSER_ENDING)
            world.event_scripts.get_command_by_identifier("midas_palette_5", PaletteSet).set_from_row(NPC_PALETTE_ROW_3)
            world.event_scripts.get_command_by_identifier("midas_palette_6", PaletteSet).set_palette_set_starts_at(EPAL0140_BOWSER_ENDING)
            world.event_scripts.get_command_by_identifier("midas_palette_6", PaletteSet).set_from_row(NPC_PALETTE_ROW_3)
        elif world.overworld_character.ally.index == 3:
            world.sprites.sprites[SPR0096_MARIO_DOLL_SURPRISED] = GENO_96
            world.sprites.sprites[SPR0132_MOLEVILLE_MINE_CART] = GENO_132
            world.sprites.sprites[SPR0135_MINE_CART_BAD_PALETTE] = GENO_135
            world.sprites.sprites[SPR0136_MARIO_IN_MINE_CART] = GENO_136
            world.sprites.sprites[SPR0621_OLD_CLASSIC_MARIO] = GENO_621
            world.sprites.sprites[SPR0034_ALT_PROTAGONIST_4] = GENO_986
            world.sprites.sprites[SPR0035_ALT_PROTAGONIST_5] = GENO_987
            world.sprites.sprites[SPR0036_ALT_PROTAGONIST_6] = GENO_988
            world.sprites.sprites[SPR0037_ALT_PROTAGONIST_7] = GENO_989
            world.event_scripts.get_command_by_identifier("midas_palette_1", PaletteSet).set_palette_set_starts_at(EPAL0086_GENO_ENDING)
            world.event_scripts.get_command_by_identifier("midas_palette_2", PaletteSet).set_palette_set_starts_at(EPAL0086_GENO_ENDING)
            world.event_scripts.get_command_by_identifier("midas_palette_3", PaletteSet).set_palette_set_starts_at(EPAL0086_GENO_ENDING)
            world.event_scripts.get_command_by_identifier("midas_palette_4", PaletteSet).set_palette_set_starts_at(EPAL0086_GENO_ENDING)
            world.event_scripts.get_command_by_identifier("midas_palette_5", PaletteSet).set_palette_set_starts_at(EPAL0086_GENO_ENDING)
            world.event_scripts.get_command_by_identifier("midas_palette_6", PaletteSet).set_palette_set_starts_at(EPAL0086_GENO_ENDING)
        elif world.overworld_character.ally.index == 4:
            world.sprites.sprites[SPR0096_MARIO_DOLL_SURPRISED] = MALLOW_96
            world.sprites.sprites[SPR0132_MOLEVILLE_MINE_CART] = MALLOW_132
            world.sprites.sprites[SPR0135_MINE_CART_BAD_PALETTE] = MALLOW_135
            world.sprites.sprites[SPR0136_MARIO_IN_MINE_CART] = MALLOW_136
            world.sprites.sprites[SPR0621_OLD_CLASSIC_MARIO] = MALLOW_621
            world.sprites.sprites[SPR0034_ALT_PROTAGONIST_4] = MALLOW_979
            world.sprites.sprites[SPR0035_ALT_PROTAGONIST_5] = MALLOW_980
            world.sprites.sprites[SPR0036_ALT_PROTAGONIST_6] = MALLOW_981
            world.sprites.sprites[SPR0037_ALT_PROTAGONIST_7] = MALLOW_982
            world.event_scripts.get_command_by_identifier("midas_palette_1", PaletteSet).set_palette_set_starts_at(EPAL0085_MALLOW_ENDING)
            world.event_scripts.get_command_by_identifier("midas_palette_2", PaletteSet).set_palette_set_starts_at(EPAL0085_MALLOW_ENDING)
            world.event_scripts.get_command_by_identifier("midas_palette_3", PaletteSet).set_palette_set_starts_at(EPAL0085_MALLOW_ENDING)
            world.event_scripts.get_command_by_identifier("midas_palette_4", PaletteSet).set_palette_set_starts_at(EPAL0085_MALLOW_ENDING)
            world.event_scripts.get_command_by_identifier("midas_palette_5", PaletteSet).set_palette_set_starts_at(EPAL0085_MALLOW_ENDING)
            world.event_scripts.get_command_by_identifier("midas_palette_6", PaletteSet).set_palette_set_starts_at(EPAL0085_MALLOW_ENDING)
        clone_room_npc_0._npc = ALLY_CLONE_NPC

    # Update the "hide from Toad" animation to use the overworld character's
    # defend mold, so the correct sprite frame shows when cowering.
    ally = world.overworld_character.ally
    defend_mold = ally._sprites_primary.get(SpriteAnimationState.DEFEND_MOLD)
    if defend_mold is not None:
        hide_cmd = world.event_scripts.get_subscript_command_by_identifier(
            "EVENT_273_hide_from_toad_subscript",
            "EVENT_273_hide_from_toad",
            A_SetSpriteSequence,
        )
        hide_cmd.set_index(defend_mold[1])
        hide_cmd = world.event_scripts.get_subscript_command_by_identifier(
            "crouch_for_coin_aq",
            "crouch_for_coin",
            A_SetSpriteSequence,
        )
        hide_cmd.set_index(defend_mold[1])
    # masher animation
    if ally.index != 0:
        world.event_scripts.get_subscript_command_by_identifier("tower_lean_back_aq", "tower_lean_back_1", A_SetSpriteSequence).set_index(ally._sprites_primary.get(SpriteAnimationState.LEAN_BACK)[1])
        world.event_scripts.get_subscript_command_by_identifier("tower_lean_back_aq", "tower_lean_back_2", A_SetSpriteSequence).set_index(ally._sprites_primary.get(SpriteAnimationState.LEAN_BACK)[1])
        world.event_scripts.get_subscript_command_by_identifier("tower_lean_back_aq", "tower_lean_back_full", A_SetSpriteSequence).set_index(ally._sprites_primary.get(SpriteAnimationState.LEAN_BACK_2)[1])
        world.event_scripts.get_subscript_command_by_identifier("main_hall_lean_back_aq", "main_hall_lean_back", A_SetSpriteSequence).set_index(ally._sprites_primary.get(SpriteAnimationState.LEAN_BACK)[1])
        world.event_scripts.get_subscript_command_by_identifier("main_hall_lean_back_aq", "main_hall_lean_back_surprised", A_SetSpriteSequence).set_index(ally._sprites_primary.get(SpriteAnimationState.SHOCKED_SHADOW_BACKWARDS)[1])
        world.event_scripts.get_subscript_command_by_identifier("green_kid_lean_forward_aq", "green_kid_lean_back_1", A_SetSpriteSequence).set_index(ally._sprites_primary.get(SpriteAnimationState.LEAN_BACK)[1])
        world.event_scripts.get_subscript_command_by_identifier("green_kid_lean_forward_aq", "green_kid_lean_forward_1", A_SetSpriteSequence).set_index(ally._sprites_primary.get(SpriteAnimationState.LEAN_FORWARD)[1])
        world.event_scripts.get_subscript_command_by_identifier("green_kid_lean_forward_aq", "green_kid_lean_forward_2", A_SetSpriteSequence).set_index(ally._sprites_primary.get(SpriteAnimationState.LEAN_FORWARD)[1])
    # Set palettes that change when the protagonist changes.
    if ally.index == 2: # bowser shifts a lot of stuff...
        world.event_scripts.get_command_by_identifier("mallow_statue_palette_set", PaletteSet).set_from_row(NPC_PALETTE_ROW_4)
        world.event_scripts.get_command_by_identifier("seaside_palette_morph_1", PaletteSetMorphs).set_row(NPC_PALETTE_ROW_3)
        world.event_scripts.get_command_by_identifier("seaside_palette_morph_1", PaletteSetMorphs).set_row(NPC_PALETTE_ROW_3)
        try:
            world.event_scripts.get_command_by_identifier("kamek_palette", PaletteSetMorphs).set_row(NPC_PALETTE_ROW_3)
            world.event_scripts.get_command_by_identifier("infinite_coin_chest_palette", PaletteSet).set_from_row(NPC_PALETTE_ROW_2)
            world.event_scripts.get_command_by_identifier("kamek_palette_2", PaletteSet).set_from_row(NPC_PALETTE_ROW_3)
            world.event_scripts.get_command_by_identifier("infinite_coin_chest_palette_2", PaletteSet).set_from_row(NPC_PALETTE_ROW_2)
            world.event_scripts.get_command_by_identifier("kamek_palette_br_1", PaletteSet).set_from_row(NPC_PALETTE_ROW_2)
            world.event_scripts.get_command_by_identifier("kamek_palette_br_2", PaletteSet).set_from_row(NPC_PALETTE_ROW_2)
            world.event_scripts.get_command_by_identifier("kamek_palette_br_3", PaletteSet).set_from_row(NPC_PALETTE_ROW_2)
            world.event_scripts.get_command_by_identifier("kamek_palette_br_4", PaletteSet).set_from_row(NPC_PALETTE_ROW_2)
            world.event_scripts.get_command_by_identifier("kamek_palette_br_5", PaletteSet).set_from_row(NPC_PALETTE_ROW_2)
            world.event_scripts.get_command_by_identifier("kamek_palette_br_6", PaletteSet).set_from_row(NPC_PALETTE_ROW_2)
        except:
            pass
    # statue minigame
    if ally.index in [1, 3]:
        world.event_scripts.get_command_by_identifier("protagonist_becomes_gold", PaletteSet).set_palette_set_starts_at(EPAL0109_GENO_PEACH_STATUE)
    elif ally.index == 4:
        world.event_scripts.get_command_by_identifier("protagonist_becomes_gold", PaletteSet).set_palette_set_starts_at(EPAL0108_MALLOW_STATUE)
    # don't do anything for mario/bowser, they both use #111
    # set default palettes for reset reasons
    resets = ["remove_statue_palette_1", "remove_statue_palette_2", "hot_spring_reset_palette"]
    for reset in resets:
        if ally.index == 1:
            world.event_scripts.get_command_by_identifier(reset, PaletteSet).set_palette_set_starts_at(EPAL0141_TOADSTOOL_ENDING)
        elif ally.index == 2:
            world.event_scripts.get_command_by_identifier(reset, PaletteSet).set_palette_set_starts_at(EPAL0140_BOWSER_ENDING)
        elif ally.index == 3:
            world.event_scripts.get_command_by_identifier(reset, PaletteSet).set_palette_set_starts_at(EPAL0086_GENO_ENDING)
        elif ally.index == 4:
            world.event_scripts.get_command_by_identifier(reset, PaletteSet).set_palette_set_starts_at(EPAL0085_MALLOW_ENDING)

    # TODO: ending credits bullshittery

    apply_hint_text(world)



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
        m for m in original_prize.formation_members
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
            m.enemy for m in original_prize.formation_members
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
    formation_members = [m for m in prize.formation_members if m is not None]
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

    # Reference (anchor) enemy's new XP/coins from slicing (for scaling excluded enemies)
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
        new_hp = min(0xFFFF, round(new_hp * enemy.ratio_hp))
        enemy.set_hp(new_hp)

        # === Other Stats ===
        # All enemies scale relative to reference (average or anchor)
        enemy.set_attack(scale_stat(attack, original.attack, ref_attack, enemy.ratio_attack))
        enemy.set_defense(scale_stat(defense, original.defense, ref_defense, enemy.ratio_defense))
        enemy.set_magic_attack(scale_stat(magic_attack, original.magic_attack, ref_magic_attack, enemy.ratio_magic_attack))
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

    elif world.settings.is_flag_value(BossShuffleScaleStats, BossScaleOptions.GODMODE):
        # Normalize all boss combat stats to the reference enemy's average
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


def apply_hint_text(world: GameWorld) -> None:
    """Assemble all location hints and split across three event scripts."""
    import copy
    import math
    from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
        JmpIfBitSet,
        JmpToEvent,
        RunDialog,
        Return as ReturnCmd,
    )
    from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (
        EventScriptCommandWithJmps,
    )
    from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import BOWSER
    from ..data.variables.dialog_names import DI2758_FROGFUCIUS_DEFAULT_STUFF
    from ..data.variables.variable_names import INFINITE_COINS_FOUND
    from ..progression.prizelocations import (
        MonstroFirstSuperJumpRewardLocation,
        MonstroSecondSuperJumpRewardLocation,
    )
    from ..progression.prizes import InfiniteCoinsPrize
    from ..types.prizelocation import (
        KeyItemLocation,
        StarPieceLocation as StarPieceLocationType,
        CharacterRecruitmentLocation as CharRecruitLocationType,
        InvisibleFlagLocation,
    )
    from ..types.flags import KeyItemsAnywhere, StarPieceAvailability
    from ..logic.shufflers.items import should_shuffle

    # Collect hints in world.locations order, skipping empty hints
    super_jump_hints: list[tuple[type, list[UsableEventScriptCommand]]] = []
    regular_hints: list[tuple[type, list[UsableEventScriptCommand]]] = []

    # Determine if we should exclude locations that can't hold star pieces,
    # key items, or character recruits
    ki_anywhere = world.settings.isflag_enabled(KeyItemsAnywhere)
    sp_anywhere = world.settings.isflag_enabled(StarPieceAvailability)
    exclude_non_special = not ki_anywhere and not sp_anywhere

    for loc_type, location in world.locations.items():
        hint_commands = location.hint(world)
        if not hint_commands:
            continue

        # Exclude locations disabled by game settings
        if not should_shuffle(location, world):
            continue

        # If KeyItemsAnywhere and StarPieceAvailability are both off,
        # exclude locations that can't hold star pieces, key items, or character recruits
        if exclude_non_special:
            if not isinstance(
                location,
                (KeyItemLocation, StarPieceLocationType, CharRecruitLocationType),
            ):
                continue

        # Deep copy so we don't mutate class-level _hint lists
        hint_commands = [copy.deepcopy(cmd) for cmd in hint_commands]

        # If this location has the InfiniteCoinsPrize, prepend the infinite coins check
        if isinstance(location.prize, InfiniteCoinsPrize):
            hint_commands.insert(
                0,
                JmpIfBitSet(INFINITE_COINS_FOUND, ["next"]),
            )

        # If this is an InvisibleFlagLocation, prepend its found-bit check
        if isinstance(location, InvisibleFlagLocation):
            hint_commands.insert(
                0,
                JmpIfBitSet(location.bit, ["next"]),
            )

        # Super jump locations go last
        if loc_type in (
            MonstroFirstSuperJumpRewardLocation,
            MonstroSecondSuperJumpRewardLocation,
        ):
            super_jump_hints.append((loc_type, hint_commands))
        else:
            regular_hints.append((loc_type, hint_commands))

    # Combine: regular hints first, then super jump hints at the end
    all_hints = regular_hints + super_jump_hints

    if not all_hints:
        return

    # Assign unique identifiers to the first command of each hint block
    for i, (_loc_type, commands) in enumerate(all_hints):
        commands[0].rename(f"hint_{i}")

    # Split hints into three chunks for three event scripts
    chunk_size = math.ceil(len(all_hints) / 3)
    chunks = [
        all_hints[:chunk_size],
        all_hints[chunk_size:chunk_size * 2],
        all_hints[chunk_size * 2:],
    ]
    script_ids = [E0947_HINT_SYSTEM, E1536_HINT_SYSTEM, E3088_HINT_SYSTEM]

    # Build the final "done" commands for after the last hint
    done_dialog = RunDialog(
        dialog_id=DI2758_FROGFUCIUS_DEFAULT_STUFF,
        above_object=BOWSER,
        closable=True,
        sync=False,
        multiline=True,
        use_background=True,
        identifier="hint_done",
    )
    done_return = ReturnCmd()

    # Replace "next" destinations in each hint block
    # Hints within the same chunk point to the next hint; the last hint in a
    # chunk points to a "chain_to_next" label (JmpToEvent) or "hint_done".
    for i, (_loc_type, commands) in enumerate(all_hints):
        if i < len(all_hints) - 1:
            next_identifier = f"hint_{i + 1}"
        else:
            next_identifier = "hint_done"

        for cmd in commands:
            if isinstance(cmd, EventScriptCommandWithJmps):
                for dest in cmd.destinations:
                    if dest.label == "next":
                        dest._label = next_identifier

    # Get the hint dialog commands from E0991 (area hint text dialogs).
    # These need to be duplicated into each hint script's bank so that
    # identifiers like "booster_tower_hint_text" can be resolved.
    hint_dialog_commands = world.event_scripts.get_script_by_id(
        E0991_FROGFUCIUS_HINT_DIALOGUES
    ).contents

    # Build each chunk's command list and write to its script
    for chunk_idx, chunk in enumerate(chunks):
        if not chunk:
            continue

        flat_commands: list[UsableEventScriptCommand] = []
        for _loc_type, commands in chunk:
            flat_commands.extend(commands)

        if chunk_idx < len(chunks) - 1 and chunks[chunk_idx + 1]:
            # Not the last chunk: append a JmpToEvent to chain to the next script.
            # The last hint in this chunk has "next" pointing to hint_X which is
            # the first hint of the next chunk. Give the chain command that same
            # identifier so the jump resolves to it.
            next_script_id = script_ids[chunk_idx + 1]
            first_hint_idx_of_next = all_hints.index(chunks[chunk_idx + 1][0])
            chain_cmd = JmpToEvent(next_script_id)
            chain_cmd.rename(f"hint_{first_hint_idx_of_next}")
            flat_commands.append(chain_cmd)
        else:
            # Last chunk: append the done dialog and return
            flat_commands.append(done_dialog)
            flat_commands.append(done_return)

        # E0947 is in the same bank as E0991 (hint dialogs), so identifiers
        # like "booster_tower_hint_text" resolve naturally. The other scripts
        # are in different banks and need copies of those dialog commands.
        if script_ids[chunk_idx] != E0947_HINT_SYSTEM:
            flat_commands.extend(copy.deepcopy(hint_dialog_commands))
        else:
            flat_commands.insert(0, RunDialog(dialog_id=DI2730_FROGFUCIUS_OFFER_HINT, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True))

        world.event_scripts.get_script_by_id(script_ids[chunk_idx]).set_contents(
            flat_commands
        )
