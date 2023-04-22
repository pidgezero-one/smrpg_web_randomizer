"""A0590_KEEP_FINAL_ROOM_CHANDELIER_STRING"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FixedFCoordOn(),
        WalkSouthPixels(1, identifier="ACTION_590_shift_south_pixels_1"),
        WalkNorthPixels(1),
        WalkSouthPixels(1),
        WalkNorthPixels(1),
        Pause(40),
        JmpIfRandom2of3(["ACTION_590_pause_9", "ACTION_590_pause_11"]),
        Pause(50),
        Jmp(["ACTION_590_shift_south_pixels_1"]),
        Pause(120, identifier="ACTION_590_pause_9"),
        Jmp(["ACTION_590_shift_south_pixels_1"]),
        Pause(100, identifier="ACTION_590_pause_11"),
        WalkSouthPixels(1),
        WalkNorthPixels(1),
        Pause(90),
        JmpIfRandom1of2(["ACTION_590_pause_9"]),
        Jmp(["ACTION_590_shift_south_pixels_1"]),
    ]
)
