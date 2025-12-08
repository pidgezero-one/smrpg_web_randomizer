# pylint: disable=C0301

"""E3951_STAR_PIECE_CREDITS_INIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY,
            face_direction=NORTHWEST,
            x=4,
            y=48,
            z=0),
        RunStarPieceSequence(8),
        PaletteSet(palette_set=163, row=1),
        PaletteSet(palette_set=164, row=1),
        PaletteSet(palette_set=166, row=1),
        PaletteSet(palette_set=167, row=1),
        PaletteSet(palette_set=165, row=1),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASWalkEastPixels(16),
                ASWalk1StepNorth(),
            ]),
        ActionQueueSync(
            target=LAYER_2,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASWalk1StepWest(),
                ASWalkNorthwestSteps(2),
            ]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASTransferToXYZF(x=5, y=90, z=0, direction=EAST),
                ASTransferXYZFPixels(x=8, y=4, z=0, direction=EAST),
                ASSetPriority(3),
                ASFaceNorthwest(),
            ]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASTransferXYZFPixels(x=16, y=4, z=0, direction=EAST),
                ASSetPriority(3),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASTransferXYZFPixels(x=8, y=0, z=0, direction=EAST),
                ASSetPriority(3),
            ]),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASTransferXYZFPixels(x=8, y=0, z=0, direction=EAST),
                ASSetPriority(3),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASTransferXYZFPixels(x=8, y=0, z=0, direction=EAST),
                ASSetPriority(3),
                ASSetSpriteSequence(
                    index=6, is_sequence=True, looping=True, mirror_sprite=True
                ),
            ]),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASTransferXYZFPixels(x=4, y=208, z=0, direction=EAST),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
            ]),
        Pause(30),
        FadeInFromColour(duration=60, colour=WHITE),
        PauseScriptUntilEffectDone(),
        Pause(170),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(SLOW),
                ASShiftSouthSteps(6),
                ASWalkSouthPixels(12),
                ASSetWalkingSpeed(NORMAL),
                ASWalkSouthPixels(4),
                ASShiftSouthSteps(11),
            ]),
        Pause(328),
        ActionQueueSync(
            target=LAYER_2,
            subscript=[ASSetWalkingSpeed(VERY_SLOW), ASWalk1StepSoutheast()]),
        Pause(2),
        SetSyncActionScript(MARIO, A0229_ENDING_CUTSCENE_EFFECT),
        SetSyncActionScript(NPC_0, A0229_ENDING_CUTSCENE_EFFECT),
        SetSyncActionScript(NPC_1, A0229_ENDING_CUTSCENE_EFFECT),
        SetSyncActionScript(NPC_2, A0229_ENDING_CUTSCENE_EFFECT),
        SetSyncActionScript(NPC_4, A0229_ENDING_CUTSCENE_EFFECT),
        RememberLastObject(),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY,
            mod_id=1),
        Pause(1),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY,
            mod_id=0),
        Pause(180),
        Db(bytearray(b"_")),
        Pause(404),
        PaletteSetMorphs(palette_type=FADE_TO, palette_set=12, duration=161, row=1),
        PaletteSetMorphs(palette_type=FADE_TO, palette_set=12, duration=162, row=5),
        PaletteSetMorphs(palette_type=FADE_TO, palette_set=12, duration=84, row=8),
        PaletteSetMorphs(palette_type=FADE_TO, palette_set=12, duration=85, row=10),
        PaletteSetMorphs(palette_type=FADE_TO, palette_set=12, duration=86, row=11),
        PaletteSetMorphs(palette_type=FADE_TO, palette_set=12, duration=141, row=9),
        PaletteSetMorphs(palette_type=FADE_TO, palette_set=12, duration=140, row=13),
        PauseScriptUntilEffectDone(),
        Pause(216),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R269_ENDING_CREDITS_NIMBUS_LAND_PRINCE_MALLOW,
            mod_id=0),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R269_ENDING_CREDITS_NIMBUS_LAND_PRINCE_MALLOW,
            mod_id=1),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R269_ENDING_CREDITS_NIMBUS_LAND_PRINCE_MALLOW,
            mod_id=2),
        FadeOutToBlack(sync=True, duration=120),
        PauseScriptUntilEffectDone(),
        Pause(60, identifier="EVENT_3951_pause_329"),
        PlayMusicAtDefaultVolume(M71_ENDING_PART_2),
        Pause(130),
        RunEventSequence(scene=SC13_RUN_STAR_PIECE_END_SEQUENCE, value=0),
        Pause(8),
        EnterArea(
            room_id=R269_ENDING_CREDITS_NIMBUS_LAND_PRINCE_MALLOW,
            face_direction=SOUTHWEST,
            x=17,
            y=40,
            z=2),
        JmpToEvent(E3804_ENDING_CREDITS_CORONATION_NPCS),
    ]
)
