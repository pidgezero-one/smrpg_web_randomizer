# pylint: disable=C0301

"""E3651_NIMBUS_NORTHEAST_HOUSE_CROCO"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASPlaySound(sound=SO030_SURPRISED_MONSTER, channel=4),
                ASStartLoopNTimes(2),
                ASShiftZUpPixels(8),
                ASShiftZDownPixels(8),
                ASEndLoop(),
            ]),
        ActionQueueSync(
            target=NPC_5,
            subscript=[ASSetSpriteSequence(index=5, is_sequence=True, looping=True)]),
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASFaceSoutheast(),
                ASSetSequenceSpeed(FAST),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetWalkingSpeed(SLOW),
                ASAddZCoord1Step(),
                ASSetAllSpeeds(VERY_FAST),
                ASPlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
                ASDecZCoord1Step(),
                ASWalkSoutheastSteps(6),
            ]),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASTransferToXYZF(x=17, y=54, z=1, direction=EAST),
                ASJumpToHeight(height=108, silent=True),
                ASWalkNorthwestSteps(2),
                ASWalkNorthwestPixels(6),
            ]),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASPlaySound(sound=SO022_CLOSE_DOOR, channel=4),
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSoutheastPixels(2),
                ASStartLoopNTimes(3),
                ASWalkNorthwestPixels(4),
                ASWalkSoutheastPixels(4),
                ASEndLoop(),
                ASWalkNorthwestPixels(2),
            ]),
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(
                    index=2, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASPause(32),
                ASResetProperties(),
                ASSetSequenceSpeed(VERY_FAST),
                ASWalk1StepSouthwest(),
                ASWalkSoutheastSteps(2),
                ASVisibilityOff(),
            ]),
        RemoveObjectFromCurrentLevel(NPC_4),
        RemoveObjectFromSpecificLevel(
            NPC_4, R345_NIMBUS_LAND_TOPRIGHT_HOUSE_CROCO_DROPS_SIGNAL_RING
        ),
        SetBit(NIMBUS_HOUSE_ITEM_SUMMONED),
        Return(),
    ]
)
