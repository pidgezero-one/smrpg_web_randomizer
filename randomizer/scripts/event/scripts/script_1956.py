# pylint: disable=C0301

"""E1956_KEEP_ENTER_BUTTON_GAME_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeOutToBlack(sync=False),
        EnterArea(
            room_id=R465_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2B_GREEN_SWITCHES,
            face_direction=NORTHEAST,
            x=22,
            y=33,
            z=0,
        ),
        JmpToEvent(E3358_KEEP_BALL_SOLITAIRE_LOADER),
    ]
)
