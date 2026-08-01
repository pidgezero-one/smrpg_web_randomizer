from __future__ import annotations
from randomizer.data.variables.event_script_names import (E0256_RETURN)
from randomizer.types.prize import (FortuneEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (JmpToEvent)
from randomizer.logic.progression.prizes.misc_prizes.you_missed import (YouMissed)


class Nothing(YouMissed):
    @property
    def npc_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E0256_RETURN)])
    _fortune_type: FortuneEnum = FortuneEnum.YIKES


__all__ = ["Nothing"]
