# pylint: disable=C0301

"""E2067_DOJO_FIGHT_1_FINISHED"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASSetSequenceSpeed(FAST),
                ASSetSpriteSequence(index=9, is_sequence=True, looping=True),
                ASPause(45),
                ASResetProperties(),
                ASFaceNortheast(),
                ASPause(45),
                ASSetAllSpeeds(FASTER),
                ASWalkToXYCoords(x=5, y=9),
                ASFaceNortheast(),
            ],
            identifier="EVENT_2067_action_queue_async_0"),
        ActionQueueSync(
            target=NPC_1, subscript=[ASPause(80), ASFixedFCoordOff(), ASFaceSoutheast()]
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASPause(15),
                ASFaceSoutheast(),
                ASPause(30),
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(NORMAL),
                ASShadowOn(),
                ASJumpToHeight(48),
                ASWalkSoutheastSteps(1),
            ]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASPause(5),
                ASSetWalkingSpeed(SLOW),
                ASWalkSoutheastSteps(2),
                ASWalkSouthwestSteps(2),
                ASShadowOff(),
                ASSetWalkingSpeed(VERY_SLOW),
                ASWalkSouthwestSteps(1),
                ASPause(15),
                ASResetProperties(),
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(VERY_FAST),
                ASSetSequenceSpeed(FAST),
                ASJumpToHeight(height=48, silent=True),
                ASPlaySound(sound=SO121_AXEM_RANGER_TELEPORT, channel=4),
            ]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASWalkSoutheastPixels(4),
                ASVisibilityOff(),
                ASWalkSoutheastPixels(8),
                ASVisibilityOn(),
                ASWalkSoutheastPixels(4),
                ASPause(1),
                ASFixedFCoordOff(),
                ASPause(1),
                ASFaceNorthwest(),
                ASPause(1),
                ASFixedFCoordOn(),
                ASPause(1),
                ASJumpToHeight(height=48, silent=True),
                ASPlaySound(sound=SO121_AXEM_RANGER_TELEPORT, channel=4),
                ASWalkSouthwestPixels(4),
                ASVisibilityOff(),
                ASWalkSouthwestPixels(32),
            ]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASVisibilityOn(),
                ASWalkSouthwestPixels(4),
                ASPause(1),
                ASFixedFCoordOff(),
                ASPause(1),
                ASFaceNortheast(),
                ASPause(1),
                ASFixedFCoordOn(),
                ASPause(1),
                ASJumpToHeight(height=48, silent=True),
                ASPlaySound(sound=SO121_AXEM_RANGER_TELEPORT, channel=4),
                ASWalkNorthwestPixels(4),
                ASVisibilityOff(),
                ASWalkNorthwestPixels(10),
                ASVisibilityOn(),
                ASWalkNorthwestPixels(4),
                ASPause(1),
                ASFixedFCoordOff(),
                ASPause(1),
                ASFaceNortheast(),
                ASPause(5),
            ]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetAllSpeeds(NORMAL),
                ASSetSpriteSequence(
                    index=3, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASPause(20),
                ASResetProperties(),
                ASFaceSouthwest(),
            ]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASPause(25),
                ASPlaySound(sound=SO121_AXEM_RANGER_TELEPORT, channel=4),
                ASWalkNorthwestPixels(4),
                ASVisibilityOff(),
                ASWalkNorthwestPixels(10),
                ASVisibilityOn(),
                ASWalkNorthwestPixels(4),
                ASPause(1),
                ASFixedFCoordOff(),
                ASPause(1),
                ASFaceSoutheast(),
            ]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASPause(1),
                ASFixedFCoordOn(),
                ASPause(1),
                ASPlaySound(sound=SO121_AXEM_RANGER_TELEPORT, channel=4),
                ASWalkNortheastPixels(4),
                ASVisibilityOff(),
                ASWalkNortheastPixels(16),
                ASVisibilityOn(),
                ASWalkNortheastPixels(4),
                ASPause(1),
                ASFixedFCoordOff(),
                ASPause(1),
            ]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASFaceSouthwest(),
                ASPause(1),
                ASFixedFCoordOn(),
                ASPause(1),
                ASPlaySound(sound=SO121_AXEM_RANGER_TELEPORT, channel=4),
                ASWalkSoutheastPixels(4),
                ASVisibilityOff(),
                ASWalkSoutheastPixels(10),
                ASVisibilityOn(),
                ASWalkSoutheastPixels(4),
                ASPause(1),
                ASFaceSouthwest(),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASFixedFCoordOff(),
            ]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetAllSpeeds(FAST),
                ASSetSpriteSequence(index=8, is_sequence=True, looping=True),
                ASPause(30),
                ASSetAllSpeeds(NORMAL),
                ASPause(30),
                ASResetProperties(),
                ASFaceNortheast(),
                ASPause(10),
            ]),
        SetBit(DOJO_BOSS_1_DEFEATED),
        JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
        Return(),
    ]
)
