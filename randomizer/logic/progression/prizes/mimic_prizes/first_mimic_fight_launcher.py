from __future__ import annotations
from randomizer.data.variables.event_script_names import (E3124_MIMIC_1_CHEST)
from randomizer.types.prize import (MimicFightInitiatorPrize)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (JmpToEvent)


class FirstMimicFightLauncher(MimicFightInitiatorPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E3124_MIMIC_1_CHEST)])


__all__ = ["FirstMimicFightLauncher"]
