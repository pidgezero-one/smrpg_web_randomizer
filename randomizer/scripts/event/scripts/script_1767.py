# E1767_TEMPLE_FORTUNE_RESULTS_ROOM_GATE_OPENS

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnableControlsUntilReturn([]),
        SetBit(HAS_A_PRIZE_FORTUNE),
        ClearBit(BELOME_FORTUNE_1),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R421_BELOME_TEMPLE_AREA_04_ROOM_DETERMINED_BY_FORTUNE,
            mod_id=0,
        ),
        PlaySound(sound=SO017_OPEN_FRONT_GATE, channel=6),
        ActionQueueAsync(
            target=LAYER_1,
            subscript=[
                ASSetWalkingSpeed(SLOW),
                ASShiftSouthSteps(3),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASTransferXYZFSteps(x=0, y=0, z=18, direction=EAST),
                ASShiftZUpPixels(1),
                ASFloatingOn(),
                ASSetSolidityBits(bit_4=True),
                ASObjectMemorySetBit(arg_1=0x0B, bits=[3]),
                ASShadowOn(),
                ASVisibilityOn(),
                ASPause(
                    1, identifier="EVENT_1767_action_queue_async_6_SUBSCRIPT_pause_7"
                ),
                ASJmpIfObjectInAir(
                    NPC_4, ["EVENT_1767_action_queue_async_6_SUBSCRIPT_pause_7"]
                ),
                ASSetSequenceSpeed(FAST),
                ASSetSpriteSequence(index=0, looping=False),
                ASPause(5),
                ASPlaySound(sound=SO010_TRAMPOLINE, channel=6),
                ASPause(55),
            ],
        ),
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASPause(
                    1, identifier="EVENT_1767_action_queue_sync_7_SUBSCRIPT_pause_0"
                ),
                ASSet700CToObjectCoord(
                    object=DUMMY_0X07, coord=COORD_Z, pixel=True, bit_7=True
                ),
                ASJmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["EVENT_1767_ret_8"]),
                ASJumpToHeight(0),
                ASJmp(["EVENT_1767_action_queue_sync_7_SUBSCRIPT_pause_0"]),
            ],
        ),
        Return(identifier="EVENT_1767_ret_8"),
    ]
)
