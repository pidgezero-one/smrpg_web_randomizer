# pylint: disable=C0301

"""E1714_BANDITS_WAY_1_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(target=NPC_0, subscript=[ASWalkWestPixels(4)]),
        RunEventAsSubroutine(E0757_BANDITS_WAY_AREA_01_SHUFFLED_NPC_ANIMATION_LOADER),
        JmpIfBitClear(BANDITS_WAY_CUTSCENE_1_VIEWED, ["EVENT_1714_set_bit_3"]),
        RunEventAsSubroutine(E0014_STANDARD_ROOM_LOADER),
        Jmp(["EVENT_1714_jmp_if_bit_clear_7"]),
        SetBit(BANDITS_WAY_CUTSCENE_1_VIEWED, identifier="EVENT_1714_set_bit_3"),
        FadeInFromBlack(sync=True),
        ActionQueueAsync(
            target=NPC_5,
            subscript=[
                ASVisibilityOn(),
                ASSetSpriteSequence(
                    index=5, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASPause(135),
                ASResetProperties(),
            ]),
        ActionQueueAsync(
            target=NPC_5,
            subscript=[
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
                ASJumpToHeight(96),
                ASPause(8),
                ASFaceSouthwest(),
                ASPause(8),
                ASFaceNorthwest(),
                ASSequenceLoopingOn(),
            ]),
        Pause(10),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASSetPriority(3),
                ASSetAllSpeeds(FAST),
                ASWalk1StepSouthwest(),
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
                ASJumpToHeight(96),
                ASShiftSouthSteps(4),
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
                ASJumpToHeight(108),
                ASWalkSoutheastSteps(6),
                ASObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
                ASSetAllSpeeds(FASTER),
                ASWalkEastSteps(6),
                ASVisibilityOff(),
            ]),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASShiftSouthSteps(4),
                ASSetAllSpeeds(FASTER),
                ASWalkSoutheastSteps(6),
                ASPause(30),
                ASWalkNorthwestSteps(6),
                ASSetWalkingSpeed(FAST),
                ASShiftNorthSteps(4),
                ASSetWalkingSpeed(NORMAL),
            ]),
        JmpIfBitClear(
            SIGNAL_RING_DIRECTIONAL_BIT,
            ["EVENT_1714_ret_17"],
            identifier="EVENT_1714_jmp_if_bit_clear_7"),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1714_ret_17"]),
        RunEventAsSubroutine(E3890_BANDITS_WAY_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_1714_ret_17"),
    ]
)
