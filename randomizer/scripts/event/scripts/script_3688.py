# pylint: disable=C0301

"""E3688_MARRYMORE_SERVICE_BELL"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Db(bytearray(b"\xc7\x80")),
        CompareVarToConst(Z_COORD_1, 2),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3584_ret_0"]),
        PlaySound(sound=SO143_METRONOME_UPBEAT_DING, channel=6),
        Pause(20),
        PlaySound(sound=SO143_METRONOME_UPBEAT_DING, channel=6),
        Pause(20),
        PlaySound(sound=SO143_METRONOME_UPBEAT_DING, channel=6),
        JmpIfBitSet(TEMP_7044_5, ["EVENT_3584_ret_0"]),
        JmpIfBitSet(BELLHOP_CALLED, ["EVENT_3584_ret_0"]),
        JmpIfBitSet(BELLHOP_UNKNOWN, ["EVENT_3584_ret_0"]),
        SetBit(BELLHOP_CALLED),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASWalkToXYCoords(x=6, y=22),
                ASPause(60),
                ASFaceNorthwest(),
            ]),
        Pause(60),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASFaceNortheast(),
                ASTransferToXYZF(x=3, y=23, z=0, direction=EAST),
                ASVisibilityOn(),
                ASSetWalkingSpeed(FAST),
                ASSetSequenceSpeed(VERY_FAST),
                ASWalkNortheastSteps(3),
                ASWalkSoutheastSteps(1),
                ASSetSequenceSpeed(SLOW),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ]),
        Pause(10),
        RunDialog(
            dialog_id=DI3847_ROOM_SERVICE_MENU,
            above_object=NPC_14,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False),
        JmpToEvent(E3657_ROOM_SERVICE_MENU),
    ]
)
