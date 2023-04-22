# pylint: disable=C0301

"""E1952_KEEP_ENTER_MARATHON_PUZZLE_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeOutToBlack(sync=False),
        EnterArea(
            room_id=R466_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1C_WORD_PROBLEM,
            face_direction=NORTHEAST,
            x=12,
            y=97,
            z=0,
        ),
        JmpToEvent(E3364_KEEP_LOGIC_GAME_LOADER),
    ]
)
