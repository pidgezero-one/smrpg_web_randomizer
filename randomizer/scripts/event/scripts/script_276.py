# pylint: disable=C0301

"""E0276_REFOCUS_CAMERA_ON_SELF"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7016701BToObjectXYZ(MARIO),
        AddConstToVar(X_COORD_2, 63744),
        AddConstToVar(Y_COORD_2, 63744),
        Db(bytearray(b"\xfd\xc7")),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASJmpIfBitSet(
                    TEMP_7049_2,
                    ["EVENT_276_action_queue_async_4_SUBSCRIPT_set_animation_speed_6"]),
                ASJmpIfBitSet(
                    TEMP_7049_6,
                    ["EVENT_276_action_queue_async_4_SUBSCRIPT_set_animation_speed_4"]),
                ASSetWalkingSpeed(FAST),
                ASJmp(["EVENT_276_action_queue_async_4_SUBSCRIPT_db_7"]),
                ASSetWalkingSpeed(
                    FASTEST,
                    identifier="EVENT_276_action_queue_async_4_SUBSCRIPT_set_animation_speed_4"),
                ASJmp(["EVENT_276_action_queue_async_4_SUBSCRIPT_db_7"]),
                ASSetWalkingSpeed(
                    NORMAL,
                    identifier="EVENT_276_action_queue_async_4_SUBSCRIPT_set_animation_speed_6"),
                ASDb(
                    bytearray(b"\x98"),
                    identifier="EVENT_276_action_queue_async_4_SUBSCRIPT_db_7"),
                ASSetWalkingSpeed(NORMAL),
            ]),
        ClearBit(TEMP_7049_2),
        ClearBit(TEMP_7049_6),
        Return(),
    ]
)
