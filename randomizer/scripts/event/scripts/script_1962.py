# pylint: disable=C0301

"""E1962_KEEP_ENTER_TERRA_COTTA_BATTLE_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeOutToBlack(sync=False),
        EnterArea(
            room_id=R459_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1A_1ST_FIGHT_TERRA_COTTA,
            face_direction=NORTHEAST,
            x=2,
            y=63,
            z=0),
        JmpToEvent(E2160_KEEP_TERRA_COTTA_BATTLE_ROOM_LOADER),
    ]
)
