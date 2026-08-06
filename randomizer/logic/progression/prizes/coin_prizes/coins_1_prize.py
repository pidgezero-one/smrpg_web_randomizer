from __future__ import annotations
from randomizer.data.physical_objects.items import (SmallCoinObject)
from randomizer.data.variables.event_script_names import (E1293_COLLECT_FREESTANDING_SMALL_COIN)
from randomizer.types.prize import (CoinQuantityPrize)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (JmpToEvent)


class Coins1Prize(CoinQuantityPrize):
    _amount: int = 1
    _model = SmallCoinObject

    @property
    def standing_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E1293_COLLECT_FREESTANDING_SMALL_COIN)])


__all__ = ["Coins1Prize"]
