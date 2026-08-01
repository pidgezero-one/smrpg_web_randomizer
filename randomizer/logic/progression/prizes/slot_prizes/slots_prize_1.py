from __future__ import annotations
from randomizer.data.variables.event_script_names import (E2490_BEAN_VALLEY_LEFTMOST_PIPE_BASEMENT_ORIGINAL_SLOT_MACHINE)
from randomizer.types.prize import (SlotsPrize)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (JmpToEvent)


class SlotsPrize1(SlotsPrize):
    _logic_event = E2490_BEAN_VALLEY_LEFTMOST_PIPE_BASEMENT_ORIGINAL_SLOT_MACHINE
    _override_id = 530

    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [JmpToEvent(E2490_BEAN_VALLEY_LEFTMOST_PIPE_BASEMENT_ORIGINAL_SLOT_MACHINE)]
        )


__all__ = ["SlotsPrize1"]
