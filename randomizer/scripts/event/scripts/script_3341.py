# E3341_VOLCANO_SMALL_BOSS_PATH_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(
            VOLCANO_HENCHMAN_SHORT_ANIMATION_COMPLETED, ["EVENT_3341_jmp_to_event_6"]
        ),
        RunEventAsSubroutine(
            E0845_VOLCANO_BRIEF_HENCHMAN_ROOM_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        SetBit(VOLCANO_HENCHMAN_SHORT_ANIMATION_COMPLETED),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASDb(bytearray(b"\xfd\xf2")),
                ASShiftNortheastSteps(2),
                ASVisibilityOff(),
            ],
        ),
        Return(),
        JmpToEvent(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3341_jmp_to_event_6"),
    ]
)
