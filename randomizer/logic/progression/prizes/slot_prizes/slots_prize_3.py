from __future__ import annotations
from randomizer.data.variables.event_script_names import (E2492_BEAN_VALLEY_BOTTOM_RIGHT_PIPE_BASEMENT_ORIGINAL_SLOT_MACHINE)
from randomizer.types.prize import (SlotsPrize)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (JmpToEvent)


class SlotsPrize3(SlotsPrize):
    _logic_event = E2492_BEAN_VALLEY_BOTTOM_RIGHT_PIPE_BASEMENT_ORIGINAL_SLOT_MACHINE
    _override_id = 532

    @property
    def chest_grant(self) -> EventScript:
        return EventScript(
            [
                JmpToEvent(
                    E2492_BEAN_VALLEY_BOTTOM_RIGHT_PIPE_BASEMENT_ORIGINAL_SLOT_MACHINE
                )
            ]
        )


__all__ = ["SlotsPrize3"]
