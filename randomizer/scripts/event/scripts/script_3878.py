# pylint: disable=C0301

"""E3878_CASINO_TRAMPOLINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(target=NPC_1, subscript=[ASFaceNorthwest()]),
        Pause(10),
        RunDialog(
            dialog_id=DI1207_GRATE_GUY_WARNS_YOU_ABOUT_FACTORY_TRAMPOLINE,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfDialogOptionBSelected(["EVENT_3878_action_queue_async_56_"]),
        RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
        SetBit(CASINO_WARP_DIRECTIONAL_BIT),
        JmpToEvent(E3791_OPEN_FACTORY_FINAL_BOSS_ROOM),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[ASFaceSouthwest()],
            identifier="EVENT_3878_action_queue_async_56_",
        ),
        Return(),
    ]
)
