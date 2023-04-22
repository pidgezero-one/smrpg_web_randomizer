# pylint: disable=C0301

"""E0263_BOUNCE_ON_BED"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE,
            face_direction=NORTHWEST,
            x=4,
            y=48,
            z=0,
            run_entrance_event=True,
        ),
        JmpIfBitSet(MARIOS_PAD_OR_MONSTRO_TOWN_SLEEP, ["EVENT_256_ret_0"]),
        Pause(1),
        PlaySound(sound=SO010_TRAMPOLINE, channel=6),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASJumpToHeight(height=96, silent=True),
                ASWalkFDirectionPixels(16),
            ],
        ),
        Return(),
    ]
)
