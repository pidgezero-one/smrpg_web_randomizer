# pylint: disable=C0301

"""E1708_BANDITS_WAY_5_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_7076_0, ["EVENT_1708_jmp_if_bit_clear_3"]),
        JmpIfBitSet(EXP_STAR_BIT_5, ["EVENT_1708_jmp_if_bit_clear_3"]),
        SetVarToConst(TIMER_7022, 30),
        JmpIfBitClear(
            BANDITS_WAY_LIBERATED,
            ["EVENT_1708_jmp_if_bit_clear_9"],
            identifier="EVENT_1708_jmp_if_bit_clear_3"),
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromCurrentLevel(NPC_2),
        RemoveObjectFromCurrentLevel(NPC_3),
        RemoveObjectFromCurrentLevel(NPC_4),
        ActionQueueSync(
            target=NPC_9,
            subscript=[
                ASVisibilityOn(),
                ASJumpToHeight(0),
                ASSetSolidityBits(cant_walk_through=True),
            ]),
        JmpIfBitClear(
            MUSHROOM_KINGDOM_OCCUPIED,
            ["EVENT_1708_jmp_if_bit_clear_15"],
            identifier="EVENT_1708_jmp_if_bit_clear_9"),
        RemoveObjectFromCurrentLevel(NPC_5),
        RemoveObjectFromCurrentLevel(NPC_6),
        RemoveObjectFromCurrentLevel(NPC_7),
        RunEventAsSubroutine(E0760_BANDITS_WAY_AREA_05_SHUFFLED_NPC_ANIMATION_LOADER),
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        Return(),
        JmpIfBitClear(
            BANDITS_WAY_CUTSCENE_5_VIEWED,
            ["EVENT_1708_set_bit_20"],
            identifier="EVENT_1708_jmp_if_bit_clear_15"),
        RunEventAsSubroutine(E0760_BANDITS_WAY_AREA_05_SHUFFLED_NPC_ANIMATION_LOADER),
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        JmpToSubroutine(["EVENT_1708_action_queue_async_37"]),
        RunBackgroundEvent(
            event_id=E1709_BANDITS_WAY_5_LOADER_BACKGROUND_2, return_on_level_exit=True
        ),
        Return(),
        SetBit(BANDITS_WAY_CUTSCENE_5_VIEWED, identifier="EVENT_1708_set_bit_20"),
        RunEventAsSubroutine(E0760_BANDITS_WAY_AREA_05_SHUFFLED_NPC_ANIMATION_LOADER),
        RunEventAsSubroutine(E0014_STANDARD_ROOM_LOADER),
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
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
                ASJumpToHeight(96),
                ASPause(8),
                ASResetProperties(),
                ASFaceSouthwest(),
                ASPause(20),
                ASFaceNorthwest(),
            ]),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASPlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
                ASSetAllSpeeds(VERY_FAST),
                ASWalkSoutheastSteps(3),
                ASShiftSouthSteps(11),
                ASWalkSoutheastSteps(4),
                ASSetAllSpeeds(FASTEST),
                ASStartLoopNTimes(1),
                ASWalkSoutheastSteps(4),
                ASShiftSouthSteps(2),
                ASWalkSoutheastSteps(4),
                ASWalkSouthwestSteps(8),
                ASWalkNorthwestSteps(8),
                ASShiftNorthSteps(2),
                ASWalkNortheastSteps(8),
                ASEndLoop(),
            ]),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASWalk1StepEast(),
                ASShiftSouthSteps(7),
                ASWalkSoutheastSteps(8),
                ASShiftSouthSteps(6),
                ASPause(80),
                ASSetWalkingSpeed(VERY_FAST),
                ASShiftNorthSteps(13),
                ASWalkNorthwestSteps(8),
                ASSetWalkingSpeed(NORMAL),
            ]),
        StopEmbeddedActionScript(NPC_8),
        JmpToSubroutine(["EVENT_1708_action_queue_async_37"]),
        RunBackgroundEvent(
            event_id=E1709_BANDITS_WAY_5_LOADER_BACKGROUND_2, return_on_level_exit=True
        ),
        Return(),
        ActionQueueAsync(
            target=NPC_5,
            subscript=[
                ASTransferToXYZF(x=10, y=90, z=0, direction=EAST),
                ASFaceNortheast(),
            ],
            identifier="EVENT_1708_action_queue_async_37"),
        ActionQueueAsync(
            target=NPC_6,
            subscript=[
                ASTransferToXYZF(x=14, y=102, z=0, direction=EAST),
                ASFaceNortheast(),
            ]),
        SetBit(TEMP_7044_2),
        ClearBit(TEMP_7043_7),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASTransferToXYZF(x=11, y=115, z=0, direction=EAST),
                ASFaceNortheast(),
                ASVisibilityOn(),
            ]),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASTransferToXYZF(x=6, y=98, z=0, direction=EAST),
                ASFaceNortheast(),
            ]),
        SetSyncActionScript(NPC_5, A0472_BANDITS_WAY_5_GOOMBA),
        SetSyncActionScript(NPC_6, A0472_BANDITS_WAY_5_GOOMBA),
        SetSyncActionScript(NPC_7, A0472_BANDITS_WAY_5_GOOMBA),
        SetSyncActionScript(NPC_8, A0469_BANDITS_WAY_5_LOADER_BOSS),
        Return(),
    ]
)
