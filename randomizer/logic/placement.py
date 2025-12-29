"""Core placement algorithms for randomizer."""
from __future__ import annotations
from typing import TYPE_CHECKING, Callable
import random
from copy import copy

from .utils import debug_time
from ..types.prize import (
    KeyPrize,
    StarPiecePrize,
    CharacterPrize,
    SlotsPrize,
    EXPStarPrize,
    MimicFightInitiatorPrize,
    CoinPrize,
    FrogCoinPrize,
    SpellPrize,
    BossFightPrize, 
    ItemPrize
)
from ..types.prizelocation import FrogDiscipleLocation
from ..types.logic import Inventory

if TYPE_CHECKING:
    from ..types.gameworld import GameWorld
    from ..types.prizelocation import PrizeLocation
    from ..types.prize import Prize


def collect_accessible_items(world: GameWorld) -> Inventory:
    progress = True
    accessible_items = Inventory()
    checked = []
    while progress:
        progress = False
        accessible_locations = [
            l for l in world.locations.values()
            if l.can_access(accessible_items, world)
        ]
        for loc in accessible_locations:
            if loc in checked:
                continue
            if loc.has_item:
                accessible_items.append(loc.prize)
                checked.append(loc)
                progress = True
    return accessible_items



def place(
    world: GameWorld,
    to_place: list[Prize],
    can_overflow: bool = False,
    on_placed: Callable[[Prize, PrizeLocation], None] | None = None,
    force_frog_disciple: bool = False
):
    pending = copy(to_place)
    while pending:
        length_at_start = len(pending)
        #print(length_at_start, "items to place...")
        #print([type(i).__name__ for i in pending])
        random.shuffle(pending)
        for _, item in enumerate(pending):
            player_has = collect_accessible_items(world)
            #print(f"  Inventory: {[type(i).__name__ for i in player_has]}")
            accessible_locations = [
                l for l in world.locations.values()
                if l.can_access(player_has, world)
                and l.can_accept(item, player_has, world)
                and not l.has_item
            ]
            #print(f"  Accessible locations for {type(item).__name__}: {[type(l).__name__ for l in accessible_locations]}")
            if len(accessible_locations) == 0:
                # Move onto the next item to see if it can be placed
                continue
            if force_frog_disciple: 
                frog_locations = [
                    l for l in accessible_locations
                    if isinstance(l, FrogDiscipleLocation)
                ]
                if len(frog_locations) > 0:
                    accessible_locations = frog_locations
            random.shuffle(accessible_locations)
            accessible_locations[0].set_prize(item)
            pending.remove(item)
            if on_placed:
                on_placed(item, accessible_locations[0])
            break
            # Start again from the beginning of the now-shortened pending list

        if len(pending) == 0:
            break
        if len(pending) == length_at_start:
            if not can_overflow:
                print(f"{len(pending)} unplaced")
                """ print("")
                print("")
                print("")
                print("inventory:")
                inv = collect_accessible_items(world)
                for i in inv:
                    print(f"  - {type(i).__name__}")
                print("")
                print("unplaced:")
                for i in pending:
                    print(f"  - {type(i).__name__}")
                print("")
                for l in world.locations.values():
                    access_string = f", can_access={l.can_access(collect_accessible_items(world), world)}, can_accept={[l.can_accept(item, inv, world) for item in pending if l.can_accept(item, inv, world)]}"
                    print(f"{type(l).__name__}: has_item={type(l.prize).__name__ if l.prize is not None else False}{access_string if l.prize is None else ''}") """
                raise Exception(f"No progress made in placement; cannot place {pending}.")
            else:
                print(f"{len([type(p).__name__ for p in pending])} unplaced, but overflow allowed")
                break
            
