from __future__ import annotations
from randomizer.data.physical_objects.items import (EmptyObject)
from randomizer.data.variables.event_script_names import (E3070_YOU_MISSED_MASHER_CHEST, E3081_YOU_MISSED)
from randomizer.types.prize import (FortuneEnum, StandardPrize)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (JmpToEvent)


class YouMissed(StandardPrize):
    _model = EmptyObject
    # BoosterTowerFallingChestLocation flips this so the prize's chest_grant jumps to the
    # masher-chest variant; every other holder (annoying empty chests) keeps E3081.
    _masher_chest: bool = False
    _fortune_type: FortuneEnum = FortuneEnum.YIKES

    @property
    def chest_grant(self) -> EventScript:
        if self._masher_chest:
            return EventScript([JmpToEvent(E3070_YOU_MISSED_MASHER_CHEST)])
        return EventScript([JmpToEvent(E3081_YOU_MISSED)])


__all__ = ["YouMissed"]
