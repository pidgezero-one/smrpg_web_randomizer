from __future__ import annotations
from randomizer.data.variables.event_script_names import (E2816_ASYNC_NO_ANIMATION_FROG_COIN, E3083_FREESTANDING_SHUFFLED_FROG_COIN)
from randomizer.types.prize import (FrogCoinQuantityPrize)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (JmpToEvent)


class FrogCoin1Prize(FrogCoinQuantityPrize):
    _amount = 1

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3083_FREESTANDING_SHUFFLED_FROG_COIN)])

    @property
    def river_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E2816_ASYNC_NO_ANIMATION_FROG_COIN)])


__all__ = ["FrogCoin1Prize"]
