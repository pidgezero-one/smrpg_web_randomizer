# E3166_ACTIVE_MINECART_MARIO_COLLISION_CHECK_PROPERTIES

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Db(bytearray(b"\xc7\x80"), identifier="EVENT_3166_set_7010_to_object_xyz_0"),
        JmpIfVarNotEqualsConst(X_COORD_1, 22, ["EVENT_3166_action_queue_async_6"]),
        JmpIfVarNotEqualsConst(Y_COORD_1, 74, ["EVENT_3166_action_queue_async_6"]),
        ActionQueueAsync(target=MARIO, subscript=[ASSetPriority(3), ASShadowOff()]),
        Pause(1),
        Jmp(["EVENT_3166_set_7010_to_object_xyz_0"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASObjectMemoryModifyBits(arg_1=0x09, set_flags=[5], clear_bits=[4, 6]),
                ASShadowOn(),
            ],
            identifier="EVENT_3166_action_queue_async_6",
        ),
        Pause(1),
        Jmp(["EVENT_3166_set_7010_to_object_xyz_0"]),
    ]
)
