# pylint: disable=C0301

"""E3886_END_GAME_CONTAINER_FROM_ALT_WIN_CONDITIONS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnterArea(
            room_id=R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE,
            face_direction=NORTHEAST,
            x=4,
            y=51,
            z=0,
        ),
        FadeInFromBlack(sync=False),
        JmpToEvent(E3885_END_GAME),
    ]
)
