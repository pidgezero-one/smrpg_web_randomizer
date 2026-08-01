from __future__ import annotations
from randomizer.data.variables.event_script_names import (E3146_FREESTANDING_BIG_COIN)
from randomizer.types.prize import (CoinQuantityPrize)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (JmpToEvent)


class Coins10Prize(CoinQuantityPrize):
    _amount: int = 10

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3146_FREESTANDING_BIG_COIN)])


__all__ = ["Coins10Prize"]
