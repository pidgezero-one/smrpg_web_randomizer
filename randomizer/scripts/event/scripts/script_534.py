# pylint: disable=C0301

"""E0534_ROSE_TOWN_DAD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TREASURE_HUNTER_HOUSE_PRIZE, ["EVENT_534___run_dialog_66"]),
        JmpIfBitSet(FOREST_MAZE_SECRET_FOUND, ["EVENT_534_play_sound_3"]),
        RunDialog(
            dialog_id=DI0800_FOREST_SECRET_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
        RunEventAsSubroutine(
            E0178_NPC_QUEST_1_CONTAINER, identifier="EVENT_534_play_sound_3"
        ),
        SetBit(TREASURE_HUNTER_HOUSE_PRIZE),
        Return(),
        RunDialog(
            dialog_id=DI0799_DUPLICATE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_534___run_dialog_66"),
        Return(),
    ]
)
