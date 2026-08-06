from __future__ import annotations
from randomizer.data.variables.event_script_names import (E3074_COIN_CHEST_MULTI_HIT_1)
from randomizer.data.variables.variable_names import (ITEM_ID)
from randomizer.types.prize import (FortuneEnum, StandardPrize)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (JmpToEvent, SetVarToConst)


class InfiniteCoinsPrize(StandardPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [SetVarToConst(ITEM_ID, 240), JmpToEvent(E3074_COIN_CHEST_MULTI_HIT_1)]
        )
    _fortune_type: FortuneEnum = FortuneEnum.COINS


__all__ = ["InfiniteCoinsPrize"]
