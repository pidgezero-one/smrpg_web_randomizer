# pylint: disable=C0301

"""E1711_BANDITS_WAY_TRAMPOLINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
        EnterArea(
            room_id=R076_BANDITS_WAY_AREA_01,
            face_direction=SOUTH,
            x=4,
            y=52,
            z=0,
            run_entrance_event=True),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASDb(bytearray(b"\xc8\x00")),
                ASAddConstToVar(Z_COORD_2, 2304),
                ASDb(bytearray(b"\x99")),
                ASJumpToHeight(height=0, silent=True),
                ASPause(
                    1, identifier="EVENT_1711_action_queue_async_2_SUBSCRIPT_pause_5"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_1711_action_queue_async_2_SUBSCRIPT_pause_5"]
                ),
                ASPlaySound(sound=SO058_INSERT, channel=4),
            ]),
        Return(),
    ]
)
