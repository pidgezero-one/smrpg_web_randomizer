# pylint: disable=C0301

"""E1854_KEEP_DONKEY_ROOM_BACKGROUND"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(TEMP_70A9, 22, identifier="EVENT_1854_set_0"),
        StartLoopNTimes(4),
        Pause(1, identifier="EVENT_1854_pause_2"),
        JmpIfObjectNotInSpecificLevel(
            MEM_70A9,
            R456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS,
            ["EVENT_1854_summon_to_level_5"]),
        Jmp(["EVENT_1854_pause_2"]),
        SummonObjectToSpecificLevel(
            MEM_70A9,
            R456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS,
            identifier="EVENT_1854_summon_to_level_5"),
        ActionQueueSync(
            target=NPC_8,
            subscript=[ASSetSpriteSequence(index=2, looping=False, mirror_sprite=True)]),
        SetSyncActionScript(MEM_70A9, A0824_KEEP_DONKEY_ROOM_BARRELS),
        Pause(68),
        Inc(TEMP_70A9),
        EndLoop(),
        Pause(20),
        Pause(1, identifier="EVENT_1854_pause_12"),
        JmpIfObjectInSpecificLevel(
            MEM_70A9,
            R456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS,
            ["EVENT_1854_pause_12"]),
        SummonObjectToSpecificLevel(
            MEM_70A9, R456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS
        ),
        ClearBit(TEMP_7043_1),
        SetBit(TEMP_7043_0),
        Pause(2),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASPlaySound(sound=SO119_CZAR_DRAGON_ROAR, channel=4),
                ASSetSpriteSequence(index=2, looping=False, mirror_sprite=True),
            ]),
        SetSyncActionScript(MEM_70A9, A0824_KEEP_DONKEY_ROOM_BARRELS),
        Pause(1, identifier="EVENT_1854_pause_20"),
        JmpIfObjectInSpecificLevel(
            MEM_70A9,
            R456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS,
            ["EVENT_1854_pause_20"]),
        SummonObjectToSpecificLevel(
            MEM_70A9, R456_BOWSERS_KEEP_6DOOR_ACTION_ROOM_1C_GORILLA_THROWING_BARRELS
        ),
        SetBit(TEMP_7043_1),
        SetBit(TEMP_7043_0),
        Pause(2),
        ActionQueueSync(
            target=NPC_8,
            subscript=[ASSetSpriteSequence(index=2, looping=False, mirror_sprite=True)]),
        SetSyncActionScript(MEM_70A9, A0824_KEEP_DONKEY_ROOM_BARRELS),
        Pause(20),
        Jmp(["EVENT_1854_set_0"]),
    ]
)
