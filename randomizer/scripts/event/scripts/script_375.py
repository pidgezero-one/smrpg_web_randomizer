# E0375_TALK_TO_CHANCELLOR_AFTER_MUSHROOM_KINGDOM_BOSS

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlayMusicAtDefaultVolume(
            M02_MUSHROOM_KINGDOM, identifier="EVENT_375_play_music_default_volume_0"
        ),
        EnterArea(
            room_id=R018_MUSHROOM_KINGDOM_CASTLE_THRONE_ROOM,
            face_direction=NORTHEAST,
            x=16,
            y=30,
            z=2,
        ),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FASTEST), ASShiftEastPixels(16)],
        ),
        FadeInFromBlack(sync=True, duration=200),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetWalkingSpeed(VERY_SLOW),
                ASSetSequenceSpeed(FAST),
                ASShiftNorthwestPixels(8),
                ASFaceSouthwest(),
                ASPause(20),
                ASWalk1StepSoutheast(),
                ASFaceSouthwest(),
                ASPause(20),
                ASWalk1StepNorthwest(),
                ASFaceSouthwest(),
                ASPause(20),
                ASShiftSoutheastPixels(8),
                ASFaceSouthwest(),
            ],
        ),
        PauseScriptUntilEffectDone(),
        SetBit(UNKNOWN_7065_5),
        SetBit(UNKNOWN_7065_6),
        SetBit(UNKNOWN_7065_7),
        SetBit(MAP_DIRECTIONAL_MUSHROOM_KINGDOM_KERO_SEWERS),
        SetBit(TEMP_7042_0),
        SetBit(MUSHROOM_KINGDOM_LIBERATED),
        JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
        Return(),
    ]
)
