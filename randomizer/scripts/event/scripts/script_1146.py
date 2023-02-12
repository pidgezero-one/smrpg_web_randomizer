# E1146_SEASIDE_INITIATE_BOSS_FIGHT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASTransferToXYZF(x=6, y=26, z=0, direction=EAST),
                ASFaceNorthwest(),
                ASVisibilityOn(),
            ],
            identifier="EVENT_1146_action_queue_sync_2",
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=5, y=26, z=0, direction=EAST),
                ASFaceNortheast(),
                ASVisibilityOn(),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASTransferToXYZF(x=6, y=28, z=0, direction=EAST),
                ASFaceNortheast(),
                ASVisibilityOn(),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASTransferToXYZF(x=6, y=24, z=0, direction=EAST),
                ASFaceSouthwest(),
                ASVisibilityOn(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASTransferToXYZF(x=7, y=26, z=0, direction=EAST),
                ASFaceSouthwest(),
                ASVisibilityOn(),
            ],
        ),
        SetSyncActionScript(NPC_0, A0147_SEASIDE_HENCHMAN),
        SetSyncActionScript(NPC_1, A0147_SEASIDE_HENCHMAN),
        SetSyncActionScript(NPC_2, A0147_SEASIDE_HENCHMAN),
        SetSyncActionScript(NPC_3, A0147_SEASIDE_HENCHMAN),
        SetSyncActionScript(NPC_6, A0147_SEASIDE_HENCHMAN),
        RunEventAsSubroutine(
            E0802_SEASIDE_OCCUPIED_BEACH_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetAllSpeeds(FAST),
                ASShiftNorthwestSteps(6),
                ASSetAllSpeeds(NORMAL),
                ASShiftNorthwestSteps(2),
            ],
        ),
        Pause(10),
        ActionQueueAsync(
            target=NPC_6,
            subscript=[
                ASPause(20),
                ASFaceSoutheast(),
                ASPause(30),
                ASJumpToHeight(96),
                ASPause(15),
            ],
        ),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASSetAllSpeeds(VERY_FAST), ASShiftNorthwestSteps(9)],
        ),
        ActionQueueSync(
            target=NPC_6,
            subscript=[ASSetWalkingSpeed(NORMAL), ASShiftNorthwestSteps(4)],
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASPause(45),
                ASVisibilityOff(),
                ASPause(1),
                ASClearSolidityBits(cant_pass_walls=True),
                ASTransferToXYZF(x=1, y=19, z=0, direction=EAST),
                ASSetSequenceSpeed(FAST),
                ASSetSpriteSequence(
                    index=5, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASPause(1),
                ASVisibilityOn(),
                ASPlaySound(sound=SO093_JUMP_INTO_WATER, channel=6),
                ASPause(15),
                ASVisibilityOff(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASPause(45),
                ASClearSolidityBits(cant_pass_walls=True),
                ASTransferToXYZF(x=1, y=19, z=0, direction=EAST),
                ASFaceSoutheast(),
                ASPause(5),
                ASSequenceLoopingOn(),
                ASSetSequenceSpeed(FAST),
                ASVisibilityOn(),
                ASJumpToHeight(128),
                ASShiftSoutheastSteps(2),
                ASSetSequenceSpeed(NORMAL),
            ],
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASVisibilityOff(),
                ASClearSolidityBits(cant_pass_walls=True),
                ASTransferToXYZF(x=2, y=17, z=0, direction=EAST),
                ASSetSequenceSpeed(FAST),
                ASSetSpriteSequence(
                    index=5, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASVisibilityOn(),
                ASPlaySound(sound=SO093_JUMP_INTO_WATER, channel=6),
                ASPause(15),
                ASVisibilityOff(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_5,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASTransferToXYZF(x=2, y=17, z=0, direction=EAST),
                ASFaceSoutheast(),
                ASPause(5),
                ASSequenceLoopingOn(),
                ASSetSequenceSpeed(FAST),
                ASVisibilityOn(),
                ASJumpToHeight(128),
                ASShiftSoutheastSteps(2),
                ASSetSequenceSpeed(NORMAL),
            ],
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASVisibilityOff(),
                ASClearSolidityBits(cant_pass_walls=True),
                ASTransferToXYZF(x=1, y=17, z=0, direction=EAST),
                ASSetSequenceSpeed(FAST),
                ASSetSpriteSequence(
                    index=5, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASVisibilityOn(),
                ASPlaySound(sound=SO093_JUMP_INTO_WATER, channel=6),
                ASPause(15),
                ASVisibilityOff(),
            ],
        ),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASTransferToXYZF(x=1, y=17, z=0, direction=EAST),
                ASFaceSoutheast(),
                ASPause(5),
                ASSequenceLoopingOn(),
                ASSetSequenceSpeed(FAST),
                ASVisibilityOn(),
                ASSetWalkingSpeed(FAST),
                ASJumpToHeight(128),
                ASShiftSoutheastSteps(4),
                ASSequenceLoopingOff(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_6, subscript=[ASFixedFCoordOn(), ASShiftSoutheastSteps(1)]
        ),
        Pause(30),
        ActionQueueAsync(
            target=NPC_8, subscript=[ASSequenceLoopingOn(), ASSetSequenceSpeed(SLOW)]
        ),
        Pause(30),
        ActionQueueAsync(target=NPC_8, subscript=[ASSetSequenceSpeed(NORMAL)]),
        Pause(30),
        ActionQueueAsync(target=NPC_8, subscript=[ASSetSequenceSpeed(FAST)]),
        UnsyncDialog(),
        CloseDialog(),
        ActionQueueAsync(
            target=NPC_4, subscript=[ASShiftSoutheastSteps(1), ASFaceNortheast()]
        ),
        Pause(5),
        ActionQueueAsync(target=NPC_8, subscript=[ASSequenceLoopingOff()]),
        ActionQueueSync(
            target=NPC_4, subscript=[ASShiftNorthwestSteps(1), ASFaceSoutheast()]
        ),
        ActionQueueAsync(
            target=NPC_6, subscript=[ASFixedFCoordOff(), ASShiftSoutheastSteps(3)]
        ),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASSetAllSpeeds(VERY_FAST), ASShiftSoutheastSteps(5)],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASTransferToXYZF(x=8, y=30, z=0, direction=EAST),
                ASVisibilityOn(),
                ASFaceNorthwest(),
                ASResetProperties(),
                ASSetSequenceSpeed(NORMAL),
            ],
        ),
        ActionQueueAsync(
            target=NPC_6,
            subscript=[ASPause(40), ASFaceNorthwest(), ASPause(40), ASFaceSoutheast()],
        ),
        Pause(60),
        JmpToEvent(E1147_SEASIDE_INITIATE_BOSS_FIGHT_ANIMATION),
        Return(),
    ]
)
