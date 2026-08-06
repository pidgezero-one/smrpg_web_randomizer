from __future__ import annotations
from randomizer.data.variables.event_script_names import (E2493_MIMIC_3)
from randomizer.types.prize import (MimicFightInitiatorPrize)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (JmpToEvent)


class ThirdMimicFightLauncher(MimicFightInitiatorPrize):
    @property
    def chest_grant(self) -> EventScript:
        return EventScript([JmpToEvent(E2493_MIMIC_3)])


__all__ = ["ThirdMimicFightLauncher"]
