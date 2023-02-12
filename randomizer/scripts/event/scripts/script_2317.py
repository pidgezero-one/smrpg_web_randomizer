# E2317_GARDENER_CLOUD_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FreezeCamera(),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASWalkToXYCoords(x=0, y=76),
                ASShiftNorthPixels(8),
                ASShiftEastPixels(17),
            ],
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASShiftToXYCoords(x=4, y=111),
                ASOverwriteSolidity(),
                ASSetWalkingSpeed(FASTEST),
                ASShiftZDownSteps(8),
                ASSetSpriteSequence(
                    index=7,
                    sprite_offset=6,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASSetPriority(2),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
                ASShiftWestPixels(5),
                ASSetSpriteSequence(
                    index=14, is_mold=True, is_sequence=True, looping=True
                ),
            ],
        ),
        SetBit(TEMP_GARDENER_EXTERIOR_1),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASDb(bytearray(b" \x01")),
                ASDb(bytearray(b"$\x1c\x00\x00\x00")),
                ASShiftZUpSteps(6),
                ASBPL262728(),
                ASSetSpriteSequence(
                    index=14,
                    sprite_offset=6,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASPause(16),
                ASSetSpriteSequence(
                    index=4, sprite_offset=1, is_sequence=True, looping=True
                ),
                ASFaceNorthwest(),
                ASJumpToHeight(160),
                ASShiftNorthwestSteps(2),
                ASOverwriteSolidity(
                    cant_pass_walls=True,
                    bit_4=True,
                    cant_pass_npcs=True,
                    cant_walk_through=True,
                    bit_7=True,
                ),
                ASShiftNorthwestPixels(8),
            ],
        ),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        UnfreezeCamera(),
        Return(),
    ]
)
