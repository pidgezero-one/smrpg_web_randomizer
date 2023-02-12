# E3696_NIMBUS_CASTLE_WEST_LOWER_HALL_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_3,
            R116_NIMBUS_CASTLE_AREA_02_LEFT_OF_AREA_01,
            ["EVENT_3585_fade_in_from_black_async_0"],
        ),
        Pause(1),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[ASTransferXYZFPixels(x=8, y=6, z=0, direction=EAST)],
        ),
        FadeInFromBlack(sync=False),
        RunBackgroundEvent(
            event_id=E3697_NIMBUS_CASTLE_WEST_LOWER_HALL_PINWHEEL_ANIMATIONS,
            return_on_level_exit=True,
        ),
        Return(),
    ]
)
