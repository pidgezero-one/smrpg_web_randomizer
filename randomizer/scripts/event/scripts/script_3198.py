# pylint: disable=C0301

"""E3198_SHYGUY_CART_PUSHES_MARIO_INTO_SMALLER_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PauseScriptIfMenuOpen(identifier="EVENT_3198_pause_script_if_menu_open_0"),
        DisableObjectTrigger(NPC_1),
        SetBit(TEMP_7044_7),
        ResumeActionScript(NPC_1),
        ResumeActionScript(NPC_6),
        PlaySound(sound=SO048_MINECART_START, channel=6),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(
                    cant_pass_walls=True, cant_pass_npcs=True, bit_7=True
                ),
                ASTransferToObjectXY(MEM_70A8),
                ASShiftXYPixels(x=240, y=8),
                ASSetSpriteSequence(
                    index=6, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASSetWalkingSpeed(FAST),
                ASWalkToXYCoords(x=2, y=124),
                ASVisibilityOff(),
            ]),
        RemoveObjectFromCurrentLevel(NPC_6),
        RemoveObjectFromSpecificLevel(
            NPC_6, R285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM
        ),
        EnterArea(
            room_id=R286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM,
            face_direction=SOUTHWEST,
            x=20,
            y=25,
            z=0),
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        ClearBit(TEMP_7043_0),
        RunBackgroundEvent(
            event_id=E3413_MINES_SHYGUY_COLLIDE_WITH_BOXES, return_on_level_exit=True
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASVisibilityOn(),
                ASClearSolidityBits(cant_pass_npcs=True, bit_7=True),
                ASSetSpriteSequence(
                    index=6, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASWalkToXYCoords(x=20, y=26),
                ASSetBit(TEMP_7043_2),
                ASJumpToHeight(height=128, silent=True),
                ASPause(16),
                ASWalkSouthwestSteps(2),
                ASPause(
                    1, identifier="EVENT_3198_action_queue_sync_11_SUBSCRIPT_pause_8"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_3198_action_queue_sync_11_SUBSCRIPT_pause_8"]
                ),
                ASSetSpriteSequence(
                    index=0,
                    sprite_offset=3,
                    is_mold=True,
                    is_sequence=True,
                    looping=True),
                ASJumpToHeight(height=32, silent=True),
                ASPause(16),
                ASSetWalkingSpeed(NORMAL),
                ASResetProperties(),
                ASFaceSoutheast(),
                ASSetSolidityBits(
                    cant_pass_walls=True, cant_pass_npcs=True, bit_7=True
                ),
            ]),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASPause(
                    1, identifier="EVENT_3198_action_queue_sync_12_SUBSCRIPT_pause_0"
                ),
                ASJmpIfBitClear(
                    TEMP_7043_2, ["EVENT_3198_action_queue_sync_12_SUBSCRIPT_pause_0"]
                ),
                ASPlaySound(sound=SO021_RUMBLING, channel=6),
                ASSetWalkingSpeed(FAST),
                ASStartLoopNTimes(3),
                ASWalkSouthwestPixels(4),
                ASWalkNortheastPixels(4),
                ASEndLoop(),
                ASSetWalkingSpeed(NORMAL),
            ]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASShiftToXYCoords(x=21, y=24),
                ASSetSpriteSequence(index=7, is_sequence=True, looping=True),
                ASPause(6),
                ASVisibilityOn(),
                ASWalkSouthwestSteps(2),
                ASStartLoopNTimes(1),
                ASWalkWestPixels(2),
                ASWalkEastPixels(2),
                ASEndLoop(),
                ASSetWalkingSpeed(VERY_SLOW),
                ASWalk1StepNortheast(),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASPause(32),
                ASSetSpriteSequence(
                    index=9, is_mold=True, is_sequence=True, looping=True
                ),
                ASSequenceLoopingOff(),
                ASSequencePlaybackOff(),
            ]),
        JmpIfBitSet(
            RUNAWAY_MINECART_ITEM_OBTAINED, ["EVENT_3198_action_queue_async_16"]
        ),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASSetSequenceSpeed(FAST),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASShiftToXYCoords(x=21, y=24),
                ASTransferXYZFPixels(x=0, y=0, z=8, direction=EAST),
                ASSequencePlaybackOn(),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=True),
                ASPause(6),
                ASVisibilityOn(),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=False),
                ASWalkSouthwestSteps(2),
                ASStartLoopNTimes(1),
                ASWalkWestPixels(2),
                ASWalkEastPixels(2),
                ASEndLoop(),
                ASJumpToHeight(128),
                ASSequenceLoopingOn(),
                ASSetAllSpeeds(NORMAL),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=False),
                ASPlaySound(sound=SO079_YELP_IN_DISTANCE, channel=4),
                ASSetBit(TEMP_7043_0),
                ASBounceToXYWithHeight(x=21, y=28, height=0),
                ASPause(8),
                ASSetAllSpeeds(VERY_FAST),
                ASPlaySound(sound=SO024_TAPPING_FEET, channel=4),
                ASResetProperties(),
                ASSequenceLoopingOn(),
                ASJumpToHeight(48),
                ASPause(20),
                ASJumpToHeight(48),
                ASPause(20),
                ASPlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
                ASWalkToXYCoords(x=19, y=32),
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASDb(bytearray(b"\xfd\xf2")),
            ],
            identifier="EVENT_3198_action_queue_async_16"),
        SummonObjectToSpecificLevel(
            NPC_0,
            R286_MOLEVILLE_MINES_AREA_12_2LEVEL_ROOM_LEADS_TO_LONG_MINECART_TRACKS_ROOM),
        RemoveObjectFromSpecificLevel(
            NPC_1, R285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM
        ),
        RemoveObjectFromSpecificLevel(
            NPC_0,
            R287_MOLEVILLE_MINES_AREA_14_2LEVEL_ROOM_FROM_LONG_MINECART_TRACKS_ROOM),
        Return(),
    ]
)
