# pylint: disable=C0301

"""E1950_KEEP_GOOMBA_BATTLE_ROOM_EXIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeOutToBlack(sync=False),
        EnterArea(
            room_id=R376_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2B_1ST_FIGHT_CHEWY,
            face_direction=NORTHEAST,
            x=2,
            y=63,
            z=0),
        JmpToEvent(E2180_KEEP_CHEWY_BATTLE_ROOM_LOADER),
    ]
)
