"""Assemble all location hints and split across three event scripts.

Extracted from the apply_shuffler_results orchestrator; called once, from
apply_shuffler_results_to_game_data.
"""

from __future__ import annotations

import copy
import math
from typing import TYPE_CHECKING

from randomizer.data.variables.dialog_names import (
    DI2730_FROGFUCIUS_OFFER_HINT,
    DI2758_FROGFUCIUS_DEFAULT_STUFF,
)
from randomizer.data.variables.event_script_names import (
    E0947_HINT_SYSTEM,
    E0991_FROGFUCIUS_HINT_DIALOGUES,
    E1536_HINT_SYSTEM,
    E3088_HINT_SYSTEM,
)
from randomizer.data.variables.variable_names import (INFINITE_COINS_FOUND)
from randomizer.logic.shufflers.items import (should_shuffle)
from randomizer.logic.progression.prizelocations import (
    BoosterTowerIndoorStarPieceRemake,
    BoosterTowerRemakeBossFightPrizeLocation,
    DojoFifthFightStarPiece,
    FireworksShopItemLocation,
    FrogDiscipleLocation1,
    FrogDiscipleLocation2,
    FrogDiscipleLocation3,
    FrogDiscipleLocation4,
    FrogDiscipleLocation5,
    InnerMinesPostgameDrop,
    InnerMinesPostgameStarPiece,
    LandsEndFirstPurchasableChestLocation,
    LandsEndSecondPurchasableChestLocation,
    MarrymoreBigTipLocation,
    MarrymoreBossFightRemakeItemDrop,
    MarrymoreBossFightStarPieceRemake,
    MarrymoreFifthSuitePrizeLocation,
    MarrymoreFirstSuitePrizeLocation,
    MarrymoreFourthSuitePrizeLocation,
    MarrymoreSecondSuitePrizeLocation,
    MarrymoreSixthSuitePrizeLocation,
    MarrymoreThirdSuitePrizeLocation,
    MonstroDojoPostgameClearRewardLocation,
    MonstroFirstSuperJumpRewardLocation,
    MonstroSealedDoorClearRewardLocationPostgame,
    MonstroSealedDoorStarPiecePostgame,
    MonstroSecondSuperJumpRewardLocation,
    MushroomKingdomInnPurchaseLocation,
    ShipPostgameFightItemDrop,
    ShipPostgameStarPiece,
    TempleBossFightStarPiecePostgame,
    TemplePostgameFightItemDrop,
    TreasureShopItem1,
    TreasureShopItem2,
    TreasureShopItem3,
)
from randomizer.logic.progression.prizes import (InfiniteCoinsPrize, StarPiece7)
from randomizer.types.flags import (
    KeyItemsAnywhere,
    ShuffleStarPieces,
    StarPieceAvailability,
    WinCondition,
    WinConditions,
)
from randomizer.types.prizelocation import (
    CharacterRecruitmentLocation as CharRecruitLocationType,
    InvisibleFlagLocation,
    KeyItemLocation,
    StarPieceLocation as StarPieceLocationType,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (BOWSER)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    JmpIfBitSet,
    JmpToEvent,
    Return as ReturnCmd,
    RunDialog,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (
    EventScriptCommandWithJmps,
    UsableEventScriptCommand,
)

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld


def apply_hint_text(world: GameWorld) -> None:
    """Assemble all location hints and split across three event scripts."""

    # Collect hints in world.locations order, skipping empty hints
    super_jump_hints: list[tuple[type, list[UsableEventScriptCommand]]] = []
    postgame_hints: list[tuple[type, list[UsableEventScriptCommand]]] = []
    invisible_flag_hints: list[tuple[type, list[UsableEventScriptCommand]]] = []
    expensive_hints: list[tuple[type, list[UsableEventScriptCommand]]] = []
    regular_hints: list[tuple[type, list[UsableEventScriptCommand]]] = []

    # Locations that need large coin payments to obtain. Hinted after all regular
    # locations, but before the invisible-flag / postgame / super-jump groups.
    expensive_loc_types = (
        MushroomKingdomInnPurchaseLocation,
        MarrymoreFirstSuitePrizeLocation,
        MarrymoreSecondSuitePrizeLocation,
        MarrymoreThirdSuitePrizeLocation,
        MarrymoreFourthSuitePrizeLocation,
        MarrymoreFifthSuitePrizeLocation,
        MarrymoreSixthSuitePrizeLocation,
        MarrymoreBigTipLocation,
        TreasureShopItem1,
        TreasureShopItem2,
        TreasureShopItem3,
        FireworksShopItemLocation,
        LandsEndFirstPurchasableChestLocation,
        LandsEndSecondPurchasableChestLocation,
        FrogDiscipleLocation1,
        FrogDiscipleLocation2,
        FrogDiscipleLocation3,
        FrogDiscipleLocation4,
        FrogDiscipleLocation5,
    )

    # Postgame locations go last, but before the super jump locations
    postgame_loc_types = (
        InnerMinesPostgameStarPiece,
        InnerMinesPostgameDrop,
        BoosterTowerIndoorStarPieceRemake,
        BoosterTowerRemakeBossFightPrizeLocation,
        MarrymoreBossFightStarPieceRemake,
        MarrymoreBossFightRemakeItemDrop,
        ShipPostgameFightItemDrop,
        ShipPostgameStarPiece,
        TempleBossFightStarPiecePostgame,
        TemplePostgameFightItemDrop,
        DojoFifthFightStarPiece,
        MonstroDojoPostgameClearRewardLocation,
        MonstroSealedDoorStarPiecePostgame,
        MonstroSealedDoorClearRewardLocationPostgame,
    )

    # Determine if we should exclude locations that can't hold star pieces,
    # key items, or character recruits
    ki_anywhere = world.settings.isflag_enabled(KeyItemsAnywhere)
    sp_anywhere = world.settings.isflag_enabled(StarPieceAvailability)
    exclude_non_special = not ki_anywhere and not sp_anywhere

    for loc_type, location in world.locations.items():
        hint_commands = location.hint(world)
        if not hint_commands:
            continue

        # Exclude locations disabled by game settings.
        # InvisibleFlagLocation hints always emit: the Musty Fears items exist in
        # every seed regardless of ShuffleItems, so exempt them from the shuffle gate.
        #
        # When star pieces aren't randomized (rstars off), should_shuffle drops every
        # StarPieceLocation, but the seven vanilla holders still contain a star piece
        # in that seed and should be hinted. originally_held is non-None for exactly
        # those seven (StarPiece1..7). The factory piece (StarPiece7) is skipped when
        # the factory boss is the win condition, since it is only collected as the
        # game ends.
        sp_vanilla_holder = (
            not world.settings.isflag_enabled(ShuffleStarPieces)
            and isinstance(location, StarPieceLocationType)
            and location.originally_held is not None
            and not (
                issubclass(location.originally_held, StarPiece7)
                and world.settings.is_flag_value(WinCondition, WinConditions.FACTORY)
            )
        )
        if (
            not should_shuffle(location, world)
            and not isinstance(location, InvisibleFlagLocation)
            and not sp_vanilla_holder
        ):
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

        # Ordering, earliest to latest: regular hints, then the large-payment
        # ("expensive") locations, then invisible flags, then postgame, then super
        # jump. The last four are all deferred so their hints don't crowd out the
        # locations a player can reach and afford earlier.
        if loc_type in (
            MonstroFirstSuperJumpRewardLocation,
            MonstroSecondSuperJumpRewardLocation,
        ):
            super_jump_hints.append((loc_type, hint_commands))
        elif loc_type in postgame_loc_types:
            postgame_hints.append((loc_type, hint_commands))
        elif isinstance(location, InvisibleFlagLocation):
            invisible_flag_hints.append((loc_type, hint_commands))
        elif loc_type in expensive_loc_types:
            expensive_hints.append((loc_type, hint_commands))
        else:
            regular_hints.append((loc_type, hint_commands))

    all_hints = (
        regular_hints
        + expensive_hints
        + invisible_flag_hints
        + postgame_hints
        + super_jump_hints
    )

    if not all_hints:
        return

    for i, (_loc_type, commands) in enumerate(all_hints):
        commands[0].rename(f"hint_{i}")

    chunk_size = math.ceil(len(all_hints) / 3)
    chunks = [
        all_hints[:chunk_size],
        all_hints[chunk_size:chunk_size * 2],
        all_hints[chunk_size * 2:],
    ]
    script_ids = [E0947_HINT_SYSTEM, E1536_HINT_SYSTEM, E3088_HINT_SYSTEM]

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


__all__ = ["apply_hint_text"]
