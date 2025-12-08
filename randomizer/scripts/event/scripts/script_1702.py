# pylint: disable=C0301

"""E1702_BANDITS_WAY_2_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=MARIO, subscript=[ASObjectMemorySetBit(arg_1=0x0B, bits=[3])]
        ),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASFixedFCoordOn(),
                ASWalkWestPixels(8),
                ASSetWalkingSpeed(NORMAL),
            ]),
        ActionQueueSync(
            target=NPC_7,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASFixedFCoordOn(),
                ASWalkEastPixels(8),
                ASSetWalkingSpeed(NORMAL),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASFixedFCoordOn(),
                ASWalkWestPixels(8),
                ASSetWalkingSpeed(NORMAL),
            ]),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASFixedFCoordOn(),
                ASWalkEastPixels(8),
                ASSetWalkingSpeed(NORMAL),
            ]),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASFixedFCoordOn(),
                ASWalkEastPixels(24),
                ASSetWalkingSpeed(NORMAL),
            ]),
        ActionQueueAsync(
            target=NPC_5,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASFixedFCoordOn(),
                ASWalkEastPixels(8),
                ASSetWalkingSpeed(NORMAL),
            ]),
        SetSyncActionScript(NPC_7, A0477_BANDITS_WAY_1ST_PLATFORMS_STATIC),
        SetVarToConst(SECONDARY_TEMP_7024, 128),
        SetVarToConst(ROSE_WAY_703E, 26),
        JmpIfBitClear(BANDITS_WAY_CUTSCENE_2_VIEWED, ["EVENT_1702_set_bit_20"]),
        RunEventAsSubroutine(E0756_BANDITS_WAY_AREA_02_SHUFFLED_NPC_ANIMATION_LOADER),
        FadeInFromBlack(sync=False),
        Return(),
        SetBit(BANDITS_WAY_CUTSCENE_2_VIEWED, identifier="EVENT_1702_set_bit_20"),
        RunEventAsSubroutine(E0756_BANDITS_WAY_AREA_02_SHUFFLED_NPC_ANIMATION_LOADER),
        FadeInFromBlack(sync=True),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASVisibilityOn(),
                ASSetSpriteSequence(
                    index=5, is_sequence=True, looping=True, mirror_sprite=True
                ),
            ]),
        Pause(60),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
                ASJumpToHeight(96),
                ASPause(8),
                ASResetProperties(),
                ASFaceSouthwest(),
                ASPause(8),
                ASFaceNorthwest(),
            ]),
        FreezeAllNPCsUntilReturn(),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASSetSolidityBits(cant_pass_npcs=True),
                ASSetSolidityBits(bit_7=True),
            ]),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASSequenceLoopingOn(),
                ASSetAllSpeeds(FAST),
                ASWalkNortheastSteps(2),
                ASWalk1StepSoutheast(),
                ASSetVRAMPriority(PRIORITY_3),
                ASSetPriority(3),
                ASFaceNortheast(),
                ASSetSolidityBits(cant_pass_walls=True),
                ASPause(13),
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
                ASJumpToHeight(144),
                ASWalkNortheastSteps(4),
                ASWalkNortheastPixels(16),
                ASFaceSoutheast(),
                ASFixedFCoordOn(),
                ASPause(10),
                ASWalkEastPixels(50),
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
                ASJumpToHeight(80),
                ASWalkEastPixels(40),
                ASPause(
                    1, identifier="EVENT_1702_action_queue_sync_28_SUBSCRIPT_pause_20"
                ),
                ASJmpIfObjectInAir(
                    NPC_8, ["EVENT_1702_action_queue_sync_28_SUBSCRIPT_pause_20"]
                ),
                ASSetAllSpeeds(FAST),
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
                ASJumpToHeight(128),
                ASWalkEastSteps(4),
                ASVisibilityOff(),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASPause(140),
                ASClearSolidityBits(cant_jump_through=True),
                ASPlaySound(sound=SO013_COIN, channel=4),
                ASSetVRAMPriority(PRIORITY_3),
                ASSetPriority(3),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=False),
                ASSetWalkingSpeed(VERY_FAST),
                ASAddZCoord1Step(),
                ASPause(28),
                ASVisibilityOff(),
                ASDb(bytearray(b"\xfd\xf2")),
            ]),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkNortheastSteps(5),
                ASPause(20),
                ASWalkEastSteps(4),
                ASPause(80),
                ASWalkWestSteps(4),
                ASWalkSouthwestSteps(5),
                ASSetWalkingSpeed(VERY_FAST),
            ]),
        UnfreezeAllNPCs(),
        ActionQueueSync(
            target=NPC_6,
            subscript=[
                ASClearSolidityBits(cant_pass_npcs=True),
                ASClearSolidityBits(bit_7=True),
            ]),
        Return(),
    ]
)
