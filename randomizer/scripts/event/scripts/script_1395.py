# pylint: disable=C0301

"""E1395_MARIOS_HOUSE_LAMP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        MoveScriptToMainThread(),
        SetBit(MARIOS_PAD_OR_MONSTRO_TOWN_SLEEP),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASTransferToXYZF(x=5, y=15, z=0, direction=EAST),
                ASFaceNortheast(),
                ASPause(5),
                ASFaceNorth(),
                ASJumpToHeight(height=35, silent=True),
                ASPause(10),
                ASPlaySound(sound=SO005_BLOCK_SWITCH, channel=4),
            ]),
        TintLayers(
            layers=[LAYER_L1, LAYER_L2, NPC_SPRITES, MINUS_SUB],
            red=112,
            green=104,
            blue=16,
            speed=0),
        PrioritySet(
            mainscreen=[LAYER_L1, LAYER_L2, NPC_SPRITES],
            subscreen=[],
            colour_math=[LAYER_L1, LAYER_L2, NPC_SPRITES, MINUS_SUB]),
        FadeOutMusicToVolume(duration=4, volume=0),
        RemoveObjectFromCurrentLevel(NPC_0),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPause(15),
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(FAST),
                ASWalkNorthwestPixels(32),
                ASSetSpriteSequence(
                    index=8,
                    sprite_offset=2,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True),
                ASJumpToHeight(120),
                ASWalkNorthwestPixels(32),
            ]),
        SummonObjectToCurrentLevel(NPC_0),
        Pause(5),
        CircleMaskShrinkToObject(target=NPC_2, width=0, speed=3, static=True),
        PlaySound(sound=SO054_GOODNIGHT, channel=6),
        RestoreAllHP(),
        RestoreAllFP(),
        Pause(110),
        TintLayers(
            layers=[LAYER_L1, LAYER_L2, NPC_SPRITES, MINUS_SUB],
            red=0,
            green=0,
            blue=0,
            speed=0),
        ResetPrioritySet(),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R189_MARIOS_PIPEHOUSE, mod_id=32
        ),
        PlaySound(sound=SO015_NIGHT_CRICKETS, channel=6),
        Pause(30),
        PlaySound(sound=SO015_NIGHT_CRICKETS, channel=6),
        Pause(15),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASWalkNortheastPixels(16),
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(index=13, is_sequence=True, looping=True),
            ]),
        CircleMaskShrinkToObject(target=NPC_2, width=35, speed=3, static=True),
        Pause(30),
        PlaySound(sound=SO015_NIGHT_CRICKETS, channel=6),
        Pause(10),
        PlaySound(sound=SO015_NIGHT_CRICKETS, channel=6),
        Pause(60),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPlaySound(sound=SO030_SURPRISED_MONSTER, channel=6),
                ASSetSequenceSpeed(VERY_FAST),
                ASSetSpriteSequence(index=14, is_sequence=True, looping=True),
                ASPause(15),
                ASSetSequenceSpeed(NORMAL),
            ]),
        FadeOutMusicToVolume(duration=6, volume=100),
        Set7000ToTappedButton(identifier="EVENT_1395_set_7000_to_tapped_button_34"),
        Pause(1),
        Mem7000AndConst(0x0080),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 128, ["EVENT_1395_apply_tile_mod_39"]),
        Jmp(["EVENT_1395_set_7000_to_tapped_button_34"]),
        ApplyTileModToLevel(
            use_alternate=False,
            room_id=R189_MARIOS_PIPEHOUSE,
            mod_id=32,
            identifier="EVENT_1395_apply_tile_mod_39"),
        CircleMaskShrinkToObject(target=MARIO, width=153, speed=5, static=True),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASResetProperties(),
                ASSetSequenceSpeed(NORMAL),
                ASJumpToHeight(120),
                ASWalkSouthPixels(32),
                ASSetAllSpeeds(NORMAL),
            ]),
        Pause(1),
        PlaySound(sound=SO058_INSERT, channel=6),
        ClearBit(MARIOS_PAD_OR_MONSTRO_TOWN_SLEEP),
        Return(),
    ]
)
