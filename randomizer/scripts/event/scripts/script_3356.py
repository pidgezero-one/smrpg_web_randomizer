# pylint: disable=C0301

"""E3356_KEEP_RESPAWN_IN_LOBBY_UPON_FAILURE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeOutMusicFDA3(),
        PlayMusicAtDefaultVolume(M53_SILENCE),
        SetBit(UNKNOWN_BOWSERS_KEEP_707F_0),
        EnterArea(
            room_id=R454_BOWSERS_KEEP_AREA_08_ROOM_WITH_6_DOORS,
            face_direction=NORTHEAST,
            x=5,
            y=36,
            z=0,
            run_entrance_event=True),
        Return(),
        ClearBit(UNKNOWN_BOWSERS_KEEP_707F_0, identifier="EVENT_3356_clear_bit_5"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=8, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASPause(1),
            ]),
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        Pause(1, identifier="EVENT_3356_pause_8"),
        Set7000ToPressedButton(),
        JmpIf7000AllBitsClear(bits=[], destinations=["EVENT_3356_pause_8"]),
        FadeInMusic(M66_BOWSERS_CASTLE_2ND_TIME),
        SetVarToConst(TEMP_70AE, 20),
        SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
        Return(),
    ]
)
