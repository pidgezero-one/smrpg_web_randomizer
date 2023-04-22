# pylint: disable=C0301

"""E1810_TEMPLE_VAULT_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMPLE_KEY_USED, ["EVENT_1810_jmp_to_event_2"]),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM,
            mod_id=1,
        ),
        JmpToEvent(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_1810_jmp_to_event_2"),
    ]
)
