# pylint: disable=C0301

"""E0512_ROSE_TOWN_OCCUPIED_INN_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RememberLastObject(),
        Db(bytearray(b"\xc7\x80")),
        CompareVarToConst(X_COORD_1, 3),
        JmpIfComparisonResultIsLesser(["EVENT_512_fade_out_music_to_volume_207"]),
        JmpToEvent(E0261_FADE_MUSIC_ROOM_LOADER),
        FadeOutMusicToVolume(
            duration=1, volume=96, identifier="EVENT_512_fade_out_music_to_volume_207"
        ),
        FadeInFromBlack(sync=False),
        RunDialog(
            dialog_id=DI0000_INN_BANNER,
            above_object=NPC_12,
            closable=False,
            sync=True,
            multiline=False,
            use_background=False,
            bit_6=True),
        Return(),
    ]
)
