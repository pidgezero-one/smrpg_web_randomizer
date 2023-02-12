# E3762_NIMBUS_CASTLE_LIBERATED_5_DOOR_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA,
            mod_id=0,
        ),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[ASTransferXYZFPixels(x=0, y=0, z=2, direction=EAST)],
        ),
        RunEventAsSubroutine(
            E0835_NIMBUS_CASTLE_LIBERATED_5_DOOR_ROOM_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
