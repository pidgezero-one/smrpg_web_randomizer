# pylint: disable=C0301

"""E0260_UNKNOWN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=MEM_70AA,
            subscript=[
                ASDb(bytearray(b"\xfd$\x12\x00")),
                ASMem700CAndConst(0x00C0),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    0,
                    ["EVENT_260_action_queue_async_0_SUBSCRIPT_face_southeast_6"],
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    64,
                    ["EVENT_260_action_queue_async_0_SUBSCRIPT_face_southwest_8"],
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    128,
                    ["EVENT_260_action_queue_async_0_SUBSCRIPT_face_northwest_10"],
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    192,
                    ["EVENT_260_action_queue_async_0_SUBSCRIPT_face_northeast_12"],
                ),
                ASFaceSoutheast(
                    identifier="EVENT_260_action_queue_async_0_SUBSCRIPT_face_southeast_6"
                ),
                ASJmp(["EVENT_260_ret_1"]),
                ASFaceSouthwest(
                    identifier="EVENT_260_action_queue_async_0_SUBSCRIPT_face_southwest_8"
                ),
                ASJmp(["EVENT_260_ret_1"]),
                ASFaceNorthwest(
                    identifier="EVENT_260_action_queue_async_0_SUBSCRIPT_face_northwest_10"
                ),
                ASJmp(["EVENT_260_ret_1"]),
                ASFaceNortheast(
                    identifier="EVENT_260_action_queue_async_0_SUBSCRIPT_face_northeast_12"
                ),
            ],
        ),
        Return(identifier="EVENT_260_ret_1"),
    ]
)
