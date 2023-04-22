# pylint: disable=C0301

"""E3756_HOT_SPRINGS_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(target=NPC_0, subscript=[ASSetPriority(3)]),
        SetBit(NOTE_DIRECTION),
        SetSyncActionScript(NPC_0, A0977_NOTE_WITHOUT_KNIFE),
        FadeInFromBlack(sync=False),
        RunEventAsSubroutine(
            E0832_NIMBUS_LAND_HOT_SPRINGS_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        Return(),
    ]
)
