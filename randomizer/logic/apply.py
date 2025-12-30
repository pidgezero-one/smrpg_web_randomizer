"""Apply the results of the shuffler"""

from typing import cast
import random

from randomizer.data.variables.dialog_names import DI2908_TREASURE_SELLER_ITEM_2, DI2911_TREASURE_SELLER_ITEM_1, DI2914_TREASURE_SELLER_ITEM_3
from ..types.gameworld import GameWorld
from ..types.prizelocation import (
    BossFightLocation,
    PrizeRow,
    StarPieceLocation,
    SpellSlotLocation,
    PacketLocation,
    StandingLocation,
    EventLocation,
    TreasureChestLocation,
    BoosterHillLocation,
    CharacterRecruitmentLocation,
    TreasureShopLocation
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (
    UsableEventScriptCommand,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    Return,
    ClearBit,
    Inc,
    CreatePacketAt7010WithEvent,
    SummonObjectToSpecificLevel,
    EnableObjectTriggerInSpecificLevel,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.area_object import (
    AreaObject,
)
from smrpgpatchbuilder.datatypes.levels.classes import BaseRoomObject
from ..data.variables.event_script_names import *
from ..data.variables.variable_names import (
    STAR_PIECE_GRANT_DIRECTIONAL_BIT,
    STAR_PIECE_GRANT_DIRECTIONAL_BIT_2,
    BOSS_VICTORY_COUNTER,
)
from ..data.variables.room_names import *
from ..data.rooms.npcs import EMPTY_NPC
from ..types.flags import CharacterStats
from ..types.prize import SpellPrize, CharacterPrize, StandardPrize
from ..progression.prizelocations import (
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
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import NPC_9
from ..progression.prizes import FirstMimicFightLauncher, SecondMimicFightLauncher


def apply_shuffler_results(world: GameWorld) -> None:

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
        loc = cast(CharacterRecruitmentLocation, world.get_location(l))
        assert loc is not None
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
    for place in world.locations.values():
        # Construct prize granter hub events
        # skip frog disciple locations, they're set in shop shuffler
        if isinstance(place, (BossFightLocation, PrizeRow, StarPieceLocation)):
            ctr = place._container_event
            if ctr not in builders:
                builders[ctr] = ([], [])
            if isinstance(place, BossFightLocation):
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
                # set NPCs for non-packets
                # TODO: need to seriously revisit vram stuff here
                # old code might have been mostly working?
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
                    room = world.rooms._rooms[room_id]
                    assert room is not None
                    if place.prize is not None and place.prize.model is not None:
                        model = place.prize.model().base
                    else:
                        model = EMPTY_NPC
                    cast(BaseRoomObject, room.get_npc_by_target_id(npc))._npc = model
            elif isinstance(place, BossFightLocation):
                # TODO: boss shuffler happens here
                # see if we can defer dialog setters until cosmetics section, or at least the parts that search/replace names (remake might affect stuff)
                pass

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
                        world.overworld_dialogs.replace_dialog(DI2911_TREASURE_SELLER_ITEM_1, nn.get_slot_1_dialog())
                    elif isinstance(place, TreasureShopItem2):
                        world.overworld_dialogs.replace_dialog(DI2908_TREASURE_SELLER_ITEM_2, nn.get_slot_2_dialog())
                    elif isinstance(place, TreasureShopItem3):
                        world.overworld_dialogs.replace_dialog(DI2914_TREASURE_SELLER_ITEM_3, nn.get_slot_3_dialog())

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
                    world.event_scripts.get_script_by_id(
                        E0095_REVERT_ALL_CLONE_CHESTS_MIMIC_1
                    ).set_contents(contents)
                elif isinstance(place.prize, SecondMimicFightLauncher):
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
            contents.extend([*decision, Return(), *execution])
            event_script.set_contents(contents)

    # events

    # treasure chests
    # npcs
    # freestanding
    # boss fights
    # star pieces

    # disable empty chests

    # change room contents

    # inc packet size in any room that has an exp star
