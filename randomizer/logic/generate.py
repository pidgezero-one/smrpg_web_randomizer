"""One entry point for producing a seed and persisting it.

Generation itself (`randomizer.main.create`) is already a pure function of seed,
settings and an optional cached placement. What was not shared was everything
around it: looking up a stored placement, and writing the Seed row. That lived in
two near-identical copies inside the view handlers, so anything calling
generation from outside the request cycle - a queue worker, a management command,
a test - had to become a third copy.

This module is that shared path. Views, workers and tooling should all call
`generate_seed`; nothing outside it should need to know how the placement cache
is keyed or what a Seed row looks like.

No Django view, form or HTTP import belongs here, so a worker process can import
it without pulling in the request layer.
"""

from __future__ import annotations

import base64
import logging
from typing import Callable

from django.db import transaction

from randomizer.logic.build_world import compute_seed_hash
from randomizer.logic.rom.shuffler_cache import ShufflerCacheError
from randomizer.main import VERSION, create
from randomizer.models import Seed
from randomizer.types.gameworld import GameWorld
from randomizer.types.settings import Settings

logger = logging.getLogger(__name__)


def load_placement_cache(
    seed: int | str, settings: Settings, debug_mode: bool
) -> bytes | None:
    """A previous run's placement for this exact seed and hashed flag string.

    The seed hash deliberately excludes cosmetics, so changing a palette or a
    name flag reuses the placement and skips the search entirely - which is the
    whole point of storing it. Callers that key their own work (a queue keying
    jobs, say) must key on `settings.flag_string`, not on the full flag string
    including the cosmetic `R(...)` group, or they will miss every cache hit.

    Offset overrides mutate flags during generation and are a debug-only path, so
    they never reuse a cache.
    """
    if debug_mode or settings.prize_offset is not None or settings.mimic_offset is not None:
        return None
    row = (
        Seed.objects.filter(hash=compute_seed_hash(VERSION, seed, settings.flag_string))
        .only("placement")
        .first()
    )
    if row is None or not row.placement:
        return None
    return base64.b64decode(row.placement)


def encode_placement(world: GameWorld) -> str:
    """The world's placement blob, ready for `Seed.placement`."""
    return base64.b64encode(world.placement_result).decode() if world.placement_result else ""


def build_world_for(
    seed: int | str,
    settings: Settings,
    *,
    debug_mode: bool = False,
    debug_bps_patches: bool = False,
    progress_callback: Callable[[str, int], None] | None = None,
) -> GameWorld:
    """Generate a world, replaying a stored placement when one is available.

    A stored blob that no longer applies - written against different flags, or by
    a build with different location/prize classes - is not fatal. It is reported
    and the seed is generated from scratch, which is what would have happened
    before any of it was cached.
    """
    cache = load_placement_cache(seed, settings, debug_mode)
    if cache is not None:
        try:
            return create(
                seed,
                settings,
                progress_callback=progress_callback,
                debug_bps_patches=debug_bps_patches,
                placement_cache=cache,
            )
        except ShufflerCacheError as exc:
            logger.warning(
                "stored placement rejected for seed %r (%s), regenerating", seed, exc
            )
    return create(
        seed,
        settings,
        progress_callback=progress_callback,
        debug_bps_patches=debug_bps_patches,
    )


def save_seed(world: GameWorld, seed: int | str, *, debug_mode: bool, race_mode: bool) -> Seed:
    """Persist the world as a Seed row, replacing any row with the same hash."""
    with transaction.atomic():
        Seed.objects.filter(hash=world.hash).delete()
        row = Seed(
            hash=world.hash,
            seed=seed,
            version=VERSION,
            mode="open",  # Deprecated but required by model
            debug_mode=debug_mode,
            flags=world.settings.flag_string,
            file_select_char=world.file_select_character,
            file_select_hash=world.file_select_hash,
            race_mode=race_mode,
            spoiler=world.spoiler,
            placement=encode_placement(world),
        )
        row.save()
    return row


def generate_seed(
    seed: int | str,
    settings: Settings,
    *,
    debug_mode: bool = False,
    race_mode: bool = False,
    debug_bps_patches: bool = False,
    progress_callback: Callable[[str, int], None] | None = None,
) -> tuple[GameWorld, Seed]:
    """Generate a seed and store it, reusing a cached placement when possible.

    The same call covers both jobs a queue needs: a brand new seed finds no
    stored placement and runs the full search, while a permalink revisit - the
    same seed and gameplay flags with different cosmetics - finds one and skips
    it. Callers do not choose between the two.
    """
    world = build_world_for(
        seed,
        settings,
        debug_mode=debug_mode,
        debug_bps_patches=debug_bps_patches,
        progress_callback=progress_callback,
    )
    return world, save_seed(world, seed, debug_mode=debug_mode, race_mode=race_mode)


__all__ = [
    "build_world_for",
    "encode_placement",
    "generate_seed",
    "load_placement_cache",
    "save_seed",
]
