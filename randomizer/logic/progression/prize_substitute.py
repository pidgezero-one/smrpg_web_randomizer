"""Substitute-prize policy.

Lives here rather than in types/prize.py because choosing a substitute needs the
CONCRETE prize classes. A base-class module importing its own subclasses is the
inverted dependency that forced a deferred import; keeping the policy above both
layers lets every import sit at module level.
"""

from __future__ import annotations

import random

from typing import TYPE_CHECKING

from randomizer.logic.progression.prizes import (
    Coins10Prize,
    FrogCoin1Prize,
    RecoveryMushroomPrize,
)
from randomizer.types.flags import (
    BiasItemShuffle,
    ItemQuality,
    ItemQualityOptions,
)
from randomizer.types.prize import Prize

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld
    from randomizer.types.prizelocation import PrizeLocation


class RandomPrizeSubstitute(Prize):
    def _draw(
        self, world: GameWorld, pool: Sequence[type[ItemPrize]]
    ) -> type[ItemPrize]:
        """Pick from the least-used classes in pool, then record the pick.

        Plain random.choice samples with replacement, so a ~158-draw fill over
        a ~120-class pool leaves roughly 18 classes with 3+ copies and a quarter of
        the pool unused. Dealing from the least-used tranche spreads the fill: every
        class appears once before any appears twice.
        """
        # ponytail: strict least-used deal - no repeats until the pool exhausts.
        # Loosen to count <= least + 1 if seeds read too uniform.
        counts = world.substitute_draw_counts
        least = min(counts.get(prize_cls, 0) for prize_cls in pool)
        chosen = random.choice(
            [prize_cls for prize_cls in pool if counts.get(prize_cls, 0) == least]
        )
        counts[chosen] = counts.get(chosen, 0) + 1
        return chosen

    def generate(self, world: GameWorld, location: PrizeLocation) -> Prize:

        pool: list[type] = []
        if world.settings.is_flag_value(
            ItemQuality, ItemQualityOptions.COMPLETELY_RANDOM
        ):
            if world.settings.isflag_enabled(BiasItemShuffle):
                if location._bias:
                    pool = (
                        world.high_impact_items
                        + world.highest_impact_items
                        + world.high_impact_equip
                        + world.highest_impact_equip
                    )
                else:
                    pool = (
                        world.low_impact_items
                        + world.high_impact_items
                        + world.low_impact_equip
                        + world.high_impact_equip
                    )
            else:
                pool = (
                    world.low_impact_items
                    + world.high_impact_items
                    + world.highest_impact_items
                    + world.low_impact_equip
                    + world.high_impact_equip
                    + world.highest_impact_equip
                )
            pool = [world.item_to_prize.get(pool_item) for pool_item in pool]
            pool = [prize for prize in pool if prize is not None]
            return self._draw(world, pool)()
        elif world.settings.is_flag_value(
            ItemQuality, ItemQualityOptions.MOSTLY_RANDOM
        ):
            roll = random.randint(1, 100)
            if world.settings.isflag_enabled(BiasItemShuffle):
                if location._bias:
                    if roll <= 40:
                        pool = world.high_impact_items + world.high_impact_equip
                    elif roll <= 95:
                        pool = world.low_impact_items + world.low_impact_equip
                    else:
                        pool = world.highest_impact_items + world.highest_impact_equip
                else:
                    if roll <= 75:
                        pool = world.low_impact_items + world.low_impact_equip
                    elif roll <= 99:
                        pool = world.high_impact_items + world.high_impact_equip
                    else:
                        pool = world.highest_impact_items + world.highest_impact_equip
            else:
                if roll <= 65:
                    pool = world.low_impact_items + world.low_impact_equip
                elif roll <= 95:
                    pool = world.high_impact_items + world.high_impact_equip
                else:
                    pool = world.highest_impact_items + world.highest_impact_equip
            pool = [world.item_to_prize.get(pool_item) for pool_item in pool]
            pool = [prize for prize in pool if prize is not None]
            return self._draw(world, pool)()
        elif world.settings.is_flag_value(
            ItemQuality, ItemQualityOptions.COMPLETELY_EMPTY
        ):
            return EmptyPrize()
        else:
            return random.choice(
                [
                    FPFlowerPrize,
                    RecoveryMushroomPrize,
                    FrogCoin1Prize,
                    Coins10Prize,
                ]
            )()


__all__ = ["RandomPrizeSubstitute"]
