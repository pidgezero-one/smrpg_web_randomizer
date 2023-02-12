# E3282_SHIP_BOSS_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0801_SHIP_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
        JmpIfBitSet(SHIP_LIBERATED, ["EVENT_3282_jmp_if_bit_set_129"]),
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        ActionQueueSync(target=SCREEN_FOCUS, subscript=[ASShiftNortheastSteps(3)]),
        ActionQueueAsync(target=MARIO, subscript=[ASWalk1StepNortheast()]),
        ActionQueueSync(target=NPC_1, subscript=[ASWalk1StepSouthwest()]),
        ActionQueueSync(target=NPC_2, subscript=[ASWalk1StepSouthwest()]),
        ActionQueueSync(target=NPC_3, subscript=[ASWalk1StepSouthwest()]),
        ActionQueueAsync(target=NPC_4, subscript=[ASWalk1StepSouthwest()]),
        ActionQueueAsync(target=MARIO, subscript=[ASWalk1StepNortheast()]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASResetProperties(),
                ASFaceSouthwest(),
                ASFixedFCoordOn(),
                ASWalk1StepSouth(),
                ASObjectMemoryModifyBits(arg_1=0x09, set_flags=[5], clear_bits=[4, 6]),
                ASSequenceLoopingOff(),
                ASPause(50),
                ASShiftSouthwestSteps(2),
            ],
        ),
        RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
        ClearBit(TEMP_707C_5),
        ClearBit(TEMP_707C_6),
        ClearBit(TEMP_707C_7),
        RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
        RunEventAsSubroutine(E0210_UNLOCK_SEASIDE_BOSS_IF_GATED_BY_SHIP_BOSS),
        ActionQueueSync(
            target=NPC_0, subscript=[ASFixedFCoordOff(), ASFaceNorthwest()]
        ),
        RestoreAllHP(),
        RestoreAllFP(),
        SetBit(SHIP_LIBERATED),
        Db(bytearray(b"\xfd\x8er\x00(")),
        Pause(30),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASShiftNorthwestSteps(6),
                ASWalk1StepNortheast(),
                ASFaceNorthwest(),
                ASPause(2),
            ],
        ),
        SetBit(JOHNNY_POSITION),
        JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
        Return(),
        JmpIfBitClear(
            JOHNNY_POSITION,
            ["EVENT_3282_jmp_to_event_133"],
            identifier="EVENT_3282_jmp_if_bit_set_129",
        ),
        SetSyncActionScript(NPC_0, A0015_DO_NOTHING),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASShiftToXYCoords(x=24, y=110),
                ASResetProperties(),
                ASSequencePlaybackOn(),
                ASFaceNorthwest(),
            ],
        ),
        JmpToEvent(
            E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3282_jmp_to_event_133"
        ),
    ]
)
