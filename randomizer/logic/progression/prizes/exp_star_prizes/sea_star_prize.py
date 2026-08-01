from __future__ import annotations
from randomizer.data.variables.event_script_names import (E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST)
from randomizer.data.variables.variable_names import (ITEM_ID)
from randomizer.types.prize import (EXPStarPrize)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (JmpToEvent, SetVarToConst)


class SeaStarPrize(EXPStarPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                SetVarToConst(ITEM_ID, 16 + 3),
                JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST),
            ]
        )


__all__ = ["SeaStarPrize"]
